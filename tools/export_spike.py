"""Export original SPIKE source for review without the LEGO application.

The .llsp3 remains the uploadable source. JSON and block listings are review
exports, not Python conversions. Only the Python stored by LEGO is exported .py.
Usage: python tools/export_spike.py path/to/project.llsp3
"""
from __future__ import annotations

import argparse
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile


def block_listing(project: dict) -> str:
    lines = [
        '# Original SPIKE block listing', '',
        'Automatically extracted from the accompanying `.llsp3` project.',
        'Blocks retain their original opcodes, values, units and procedure names.',
        'Indentation shows nested control stacks; each event is a separate stack.',
        'This is a review representation, not an executable program or a Python translation.', '',
    ]
    for target in project.get('targets', []):
        blocks = target.get('blocks', {})
        if not blocks:
            continue
        lines.extend([f'## {target.get("name", "Program")}', ''])
        variables = target.get('variables', {})
        if variables:
            lines.extend(['### Variables', '', '```text'])
            lines.extend(f'{v[0]} = {v[1]!r}' for v in variables.values())
            lines.extend(['```', ''])

        def expression(value, trail=()):
            if isinstance(value, list):
                if len(value) > 1 and value[0] == 12:
                    return f'variable({value[1]!r})'
                if len(value) > 1 and value[0] == 13:
                    return f'list({value[1]!r})'
                return repr(value[1]) if len(value) > 1 else repr(value)
            if not isinstance(value, str) or value not in blocks:
                return repr(value)
            if value in trail:
                return '[cyclic reference]'
            block = blocks[value]
            if not isinstance(block, dict):
                return expression(block, trail)
            fields = [f'{key}={val[0]!r}' for key, val in block.get('fields', {}).items()]
            inputs = [f'{key}={expression(val[1], trail + (value,))}'
                      for key, val in block.get('inputs', {}).items()
                      if not key.startswith('SUBSTACK') and len(val) > 1]
            proc = block.get('mutation', {}).get('proccode')
            if proc:
                fields.insert(0, f'procedure={proc!r}')
            return f'{block["opcode"]}({", ".join(fields + inputs)})'

        visited = set()

        def stack(block_id, depth=0):
            local = set()
            while block_id and block_id in blocks:
                if block_id in local:
                    lines.append('  ' * depth + '[cyclic stack]')
                    break
                local.add(block_id)
                visited.add(block_id)
                block = blocks[block_id]
                lines.append('  ' * depth + expression(block_id))
                for key, val in block.get('inputs', {}).items():
                    if key.startswith('SUBSTACK') and len(val) > 1:
                        lines.append('  ' * (depth + 1) + key + ':')
                        stack(val[1], depth + 2)
                block_id = block.get('next')

        roots = [(key, b) for key, b in blocks.items()
                 if isinstance(b, dict) and b.get('topLevel') and not b.get('shadow')]
        for number, (key, block) in enumerate(roots, 1):
            lines.extend([f'### Stack {number}', '', '```text'])
            stack(key)
            lines.extend(['```', ''])
        comments = target.get('comments', {})
        if comments:
            lines.extend(['### Original comments', ''])
            for comment in comments.values():
                lines.extend([comment.get('text', ''), ''])
    return '\n'.join(lines).rstrip() + '\n'


def export_project(path: Path) -> dict:
    with ZipFile(path) as archive:
        manifest = json.loads(archive.read('manifest.json'))
        summary = {key: manifest.get(key) for key in ('type', 'name', 'created', 'lastsaved', 'slotIndex')}
        if 'projectbody.json' in archive.namelist():
            body = json.loads(archive.read('projectbody.json'))
            if not isinstance(body.get('main'), str):
                raise ValueError(f'{path}: unsupported Python body')
            path.with_suffix('.py').write_text(body['main'], encoding='utf-8', newline='\n')
        elif 'scratch.sb3' in archive.namelist():
            with ZipFile(BytesIO(archive.read('scratch.sb3'))) as scratch:
                body = json.loads(scratch.read('project.json'))
            path.with_suffix('.blocks.json').write_text(
                json.dumps(body, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
            path.with_suffix('.blocks.md').write_text(block_listing(body), encoding='utf-8', newline='\n')
        else:
            raise ValueError(f'{path}: unsupported project format')
        path.with_suffix('.metadata.json').write_text(
            json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
        return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    args = parser.parse_args()
    print(json.dumps(export_project(args.project), ensure_ascii=False, indent=2))
