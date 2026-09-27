#!/usr/bin/env python3
"""Check the launch text package; does not build or test the application."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

parser = argparse.ArgumentParser()
parser.add_argument('--release', action='store_true', help='also reject unresolved TODO markers')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
required = ['README.md', 'LICENSE', 'CONTRIBUTING.md', 'SECURITY.md', 'CHANGELOG.md',
            '.gitignore', '.github/PULL_REQUEST_TEMPLATE.md',
            '.github/ISSUE_TEMPLATE/bug_report.yml', '.github/ISSUE_TEMPLATE/feature_request.yml',
            'docs/installation.md', 'docs/integrations.md', 'docs/architecture.md', 'docs/privacy.md']
errors = []
for name in required:
    if not (root / name).is_file():
        errors.append('Missing required file: ' + name)
paths = set(root.glob('*.md')) | {root / 'LICENSE'}
for directory in ['docs', 'launch', 'assets', 'examples', '.github']:
    paths.update(p for p in (root / directory).rglob('*') if p.is_file())
links = 0
todo_pattern = re.compile(r'TODO\[[A-Z_]+\]')
for p in sorted(paths):
    if not p.exists():
        continue
    try:
        text = p.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        # Future real visual assets may be added under assets/.
        if p.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.icns'}:
            errors.append('Unexpected non-text file: ' + str(p.relative_to(root)))
        continue
    if p.suffix == '.json':
        try:
            json.loads(text)
        except json.JSONDecodeError as e:
            errors.append(f'{p.relative_to(root)}: {e}')
    if args.release and todo_pattern.search(text):
        errors.append(f'{p.relative_to(root)}: unresolved launch decision')
    if p.suffix != '.md':
        continue
    for target in re.findall(r'!?\[[^\]\n]*\]\(([^)\s]+)\)', text):
        url = urlsplit(target.strip('<>'))
        if url.scheme or url.netloc or not url.path:
            continue
        destination = (p.parent / unquote(url.path)).resolve()
        links += 1
        if not destination.exists():
            errors.append(f'{p.relative_to(root)}: missing local link {target}')
        if not destination.is_relative_to(root):
            errors.append(f'{p.relative_to(root)}: link escapes repository {target}')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'PASS: required files, JSON parsing, and {links} local Markdown file links')
if not args.release:
    print('Draft mode: TODO markers are allowed. App tests and external links were not checked.')
