"""Verifica la documentación, las fotos y la publicación de capturas solamente.

Ejecutar desde el repositorio: python tools/verify_repository.py
Estas comprobaciones revisan archivos; no simulan ni certifican el robot.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import re
import sys
import subprocess
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def verify() -> list[str]:
    errors = []
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    print(f'README principal: {len(readme):,} caracteres (mínimo de referencia: 5,000)')
    if len(readme) < 5000:
        errors.append('Root README is below 5,000 characters')
    if 'Student Engineers' not in readme:
        errors.append('El README debe identificar al equipo como Student Engineers')

    link_count = 0
    tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode('utf-8').split('\0')
    published = {name for name in tracked if name}
    files = [ROOT / name for name in sorted(published) if (ROOT / name).is_file()]
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        if (path.suffix.lower() in ('.llsp3', '.sb3') or path.name.lower().endswith(('.blocks.json', '.blocks.md', '.metadata.json'))
                or (path.suffix == '.py' and path.relative_to(ROOT).parts[0] in ('Code', 'archive'))):
            errors.append(f'Robot program/source export must remain local: {rel}')
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
    print(f'Enlaces internos de Markdown/HTML: {link_count}')

    for view in ('front', 'back', 'left', 'right', 'top', 'bottom'):
        if not (ROOT / 'Mechanics/Vehicle Photos' / f'{view}.jpg').is_file():
            errors.append(f'Missing vehicle view: {view}')

    manifest = json.loads((ROOT / 'Docs/import-manifest.json').read_text(encoding='utf-8'))
    cached = {}
    for row in manifest:
        if row.get('publication') == 'local-only':
            if row.get('destination') is not None:
                errors.append(f'Local-only program has a published destination: {row["source"]}')
            continue
        path = ROOT / row['destination']
        if row['destination'] not in published or not path.exists():
            errors.append(f'Missing imported asset: {row["destination"]}')
            continue
        if path not in cached:
            cached[path] = hashlib.sha256(path.read_bytes()).hexdigest()
        if cached[path] != row['sha256'] or path.stat().st_size != row['bytes']:
            errors.append(f'Original asset changed: {row["destination"]}')
    print(f'Inventario: {len(manifest)} ubicaciones de origen; {len(cached)} archivos originales publicados')

    versions = json.loads((ROOT / 'Docs/software-versions.json').read_text(encoding='utf-8'))
    for version in versions:
        for screenshot in version['screenshots']:
            if screenshot not in published or not (ROOT / screenshot).is_file():
                errors.append(f'Missing program screenshot: {screenshot}')
    screenshots = [name for name in published if name.startswith('Code/') and name.endswith('.png')]
    print(f'Galería de programación: {len(screenshots)} capturas; sin proyectos ni exportaciones del robot publicados')

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
    print('Libreta corregida: formato, contenido multimedia y estructura de Word conservados')
    return errors


if __name__ == '__main__':
    errors = verify()
    if errors:
        for error in errors:
            print('ERROR:', error)
        sys.exit(1)
    print('CORRECTO: capturas, archivos originales, formato de la libreta y enlaces verificados.')
