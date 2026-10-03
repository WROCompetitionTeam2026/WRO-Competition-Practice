"""Check documentation links, asset provenance and SPIKE source export fidelity.

Run from the repository root: python tools/verify_repository.py
These checks inspect repository files; they do not simulate or certify the robot.
"""
from __future__ import annotations

import ast
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile
import xml.etree.ElementTree as ET

from export_spike import block_listing

ROOT = Path(__file__).resolve().parents[1]


def verify() -> list[str]:
    errors = []
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    print(f'Root README: {len(readme):,} characters (minimum 5,000)')
    if len(readme) < 5000:
        errors.append('Root README is below 5,000 characters')

    link_count = 0
    files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts]
    for path in files:
        if path.stat().st_size >= 100 * 1024 * 1024:
            errors.append(f'{path.relative_to(ROOT)} exceeds GitHub normal-file limit')
        if path.suffix == '.svg':
            try:
                ET.parse(path)
            except ET.ParseError as e:
                errors.append(f'{path.relative_to(ROOT)} invalid SVG: {e}')
        if path.suffix == '.json':
            try:
                json.loads(path.read_text(encoding='utf-8'))
            except (json.JSONDecodeError, UnicodeError) as e:
                errors.append(f'{path.relative_to(ROOT)} invalid JSON: {e}')
        if path.suffix == '.py':
            try:
                ast.parse(path.read_text(encoding='utf-8'))
            except SyntaxError as e:
                errors.append(f'{path.relative_to(ROOT)} invalid Python syntax: {e}')
        if path.suffix == '.md':
            text = path.read_text(encoding='utf-8')
            links = re.findall(r'!?\[[^\]\n]*\]\(([^\n)]+)\)', text)
            links.extend(re.findall(r'(?:src|href)="([^"]+)"', text))
            for link in links:
                parsed = urlsplit(link.strip().strip('<>'))
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                link_count += 1
                dest = (path.parent / unquote(parsed.path)).resolve()
                if not dest.is_relative_to(ROOT) or not dest.exists():
                    errors.append(f'{path.relative_to(ROOT)} -> broken local link: {link}')
    print(f'Local Markdown/HTML file links: {link_count}')

    for view in ('front', 'back', 'left', 'right', 'top', 'bottom'):
        if not (ROOT / 'Mechanics/Vehicle Photos' / f'{view}.jpg').is_file():
            errors.append(f'Missing vehicle view: {view}')

    manifest = json.loads((ROOT / 'Docs/import-manifest.json').read_text(encoding='utf-8'))
    cached = {}
    for row in manifest:
        path = ROOT / row['destination']
        if not path.exists():
            errors.append(f'Missing imported asset: {row["destination"]}')
            continue
        if path not in cached:
            cached[path] = hashlib.sha256(path.read_bytes()).hexdigest()
        if cached[path] != row['sha256'] or path.stat().st_size != row['bytes']:
            errors.append(f'Original asset changed: {row["destination"]}')
    print(f'Provenance: {len(manifest)} source paths, {len(cached)} imported asset paths')

    projects = sorted((ROOT / 'Code').rglob('*.llsp3'))
    if len(projects) != 20:
        errors.append(f'Expected 20 supplied projects, found {len(projects)}')
    for path in projects + sorted((ROOT / 'archive/pre-refresh').rglob('*.llsp3')):
        try:
            with ZipFile(path) as archive:
                if archive.testzip() is not None:
                    errors.append(f'Corrupt archive: {path.relative_to(ROOT)}')
                original = json.loads(archive.read('manifest.json'))
                metadata = json.loads(path.with_suffix('.metadata.json').read_text(encoding='utf-8'))
                for key, value in metadata.items():
                    if original.get(key) != value:
                        errors.append(f'Metadata mismatch: {path.relative_to(ROOT)} / {key}')
                if 'scratch.sb3' in archive.namelist():
                    with ZipFile(BytesIO(archive.read('scratch.sb3'))) as scratch:
                        body = json.loads(scratch.read('project.json'))
                    export = json.loads(path.with_suffix('.blocks.json').read_text(encoding='utf-8'))
                    if body != export:
                        errors.append(f'Block export mismatch: {path.relative_to(ROOT)}')
                    if block_listing(body) != path.with_suffix('.blocks.md').read_text(encoding='utf-8'):
                        errors.append(f'Block listing mismatch: {path.relative_to(ROOT)}')
                else:
                    body = json.loads(archive.read('projectbody.json'))['main']
                    if body != path.with_suffix('.py').read_text(encoding='utf-8'):
                        errors.append(f'Python export mismatch: {path.relative_to(ROOT)}')
        except (OSError, ValueError, KeyError) as e:
            errors.append(f'Project inspection failed: {path.relative_to(ROOT)}: {e}')
    print(f'SPIKE projects: {len(projects)} current-source projects + preserved old project')

    source_doc = ROOT / 'Docs/Originals/Historial-de-documentacion.docx'
    corrected_doc = ROOT / 'Docs/Historial-de-documentacion-corregido.docx'
    with ZipFile(source_doc) as source, ZipFile(corrected_doc) as corrected:
        if source.namelist() != corrected.namelist():
            errors.append('Corrected notebook changed package entries')
        for name in source.namelist():
            if name != 'word/document.xml' and source.read(name) != corrected.read(name):
                errors.append(f'Corrected notebook changed layout/media part: {name}')
        original_xml = source.read('word/document.xml').decode('utf-8')
        corrected_xml = corrected.read('word/document.xml').decode('utf-8')
        original_structure = re.sub(r'(<w:t(?:\s[^>]*)?>).*?(</w:t>)', r'\1\2', original_xml, flags=re.DOTALL)
        corrected_structure = re.sub(r'(<w:t(?:\s[^>]*)?>).*?(</w:t>)', r'\1\2', corrected_xml, flags=re.DOTALL)
        if original_structure != corrected_structure:
            errors.append('Corrected notebook modified original formatting structure')
        ET.fromstring(corrected_xml)
    print('Corrected Word notebook: original layout/media/package preserved')
    return errors


if __name__ == '__main__':
    errors = verify()
    if errors:
        for error in errors:
            print('ERROR:', error)
        sys.exit(1)
    print('PASS: source assets, exports, notebook structure and local links verified.')
