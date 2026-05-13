# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

"""check_autoreferentiality.py — Detect Markdown files that link to themselves.

Principle: *Sempre annanz, no acopp.*
Documents must move readers forward in the dependency graph.
A file must never contain a relative Markdown link that resolves back to itself.

Two defect classes are detected:
1. **H1 self-link** — the very first heading (`# …`) contains a relative link
   whose target basename matches the host file's own basename, e.g.:
       # [53-00-03-01-005](./53-00-03-01-005_Compatibility_with_SHM_Assumptions.md)
2. **Inline self-link** — any inline Markdown link anywhere in the file whose
   target `](./X.md)` or `](X.md)` resolves to the host file itself.

Usage
-----
    python scripts/check_autoreferentiality.py [--root <dir>] [--self-test]

    --root <dir>   Root directory to scan (default: OPT-IN_FRAMEWORK)
    --self-test    Run built-in doctests and exit

GitHub Actions annotations are emitted to stdout:
    ::error file=<path>,line=<n>::<message>

Exit codes
----------
    0  No self-referential links found.
    1  One or more self-referential links found.
    2  --self-test failures.
"""

from __future__ import annotations

import argparse
import doctest
import os
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------

# Matches a Markdown inline link: [label](target)
# We capture the full link text and the target (URL or path).
_INLINE_LINK_RE = re.compile(r'\[(?P<label>[^\]]*)\]\((?P<target>[^)]+)\)')

# Matches a Markdown H1 line (the document's primary heading).
_H1_RE = re.compile(r'^#\s+(?P<rest>.+)$')


# ---------------------------------------------------------------------------
# Core detection logic
# ---------------------------------------------------------------------------

def _resolve_target_basename(target: str) -> str:
    """Return the bare filename (stem + suffix) of a Markdown link target.

    Strips leading ``./``, query strings, and URL fragments so only the
    path component remains.

    >>> _resolve_target_basename('./53-00-03-01-005_Compatibility_with_SHM_Assumptions.md')
    '53-00-03-01-005_Compatibility_with_SHM_Assumptions.md'
    >>> _resolve_target_basename('53-00-03-01-005_Compatibility_with_SHM.md#section')
    '53-00-03-01-005_Compatibility_with_SHM.md'
    >>> _resolve_target_basename('../sibling/foo.md')
    'foo.md'
    >>> _resolve_target_basename('https://example.com/page.md')
    'page.md'
    """
    # Strip query string and fragment
    target = re.split(r'[?#]', target)[0]
    return Path(target).name


def check_file(filepath: Path) -> list[tuple[int, str]]:
    """Check *filepath* for self-referential Markdown links.

    Returns a list of ``(line_number, message)`` tuples for every finding.
    Line numbers are 1-based.

    >>> import tempfile, os, pathlib
    >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
    ...     _name = pathlib.Path(f.name).name
    ...     _ = f.write(f'# [ID](./{_name}): Title\\n')
    ...     tmp = f.name
    >>> findings = check_file(pathlib.Path(tmp))
    >>> len(findings) >= 1
    True
    >>> findings[0][0]
    1
    >>> os.unlink(tmp)

    >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.md',
    ...         prefix='README',
    ...         delete=False) as f:
    ...     _ = f.write('# Normal heading\\nSome text with [external link](https://example.com).\\n')
    ...     tmp2 = f.name
    >>> check_file(pathlib.Path(tmp2))
    []
    >>> os.unlink(tmp2)
    """
    host_name = filepath.name  # e.g. "53-00-03-01-005_Compatibility_with_SHM_Assumptions.md"
    findings: list[tuple[int, str]] = []

    try:
        lines = filepath.read_text(encoding='utf-8', errors='replace').splitlines()
    except OSError as exc:
        return [(0, f'Cannot read file: {exc}')]

    for lineno, line in enumerate(lines, start=1):
        for match in _INLINE_LINK_RE.finditer(line):
            target = match.group('target').strip()
            # Skip external links (http/https/ftp/mailto)
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+\-.]*://', target):
                continue
            # Skip anchor-only links
            if target.startswith('#'):
                continue
            target_basename = _resolve_target_basename(target)
            if target_basename.lower() == host_name.lower():
                # Determine whether the offending link is in an H1
                h1_match = _H1_RE.match(line)
                if h1_match:
                    kind = 'H1 self-link'
                    suggestion = (
                        f'Remove the link from the H1 heading. '
                        f'Replace with plain text, e.g.: '
                        f'`# {match.group("label")} — <title>`'
                    )
                else:
                    kind = 'Inline self-link'
                    suggestion = (
                        f'Remove or replace the link `{match.group(0)}` '
                        f'— a document must not link to itself.'
                    )
                findings.append((
                    lineno,
                    f'{kind} in `{host_name}` at line {lineno}: '
                    f'target `{target}` resolves to this file. '
                    f'Sempre annanz, no acopp. {suggestion}'
                ))

    return findings


def scan_directory(root: Path) -> list[tuple[Path, int, str]]:
    """Recursively scan *root* for ``*.md`` files and return all findings.

    Each entry is ``(filepath, line_number, message)``.
    """
    results: list[tuple[Path, int, str]] = []
    for md_file in sorted(root.rglob('*.md')):
        for lineno, message in check_file(md_file):
            results.append((md_file, lineno, message))
    return results


# ---------------------------------------------------------------------------
# GitHub Actions annotation helpers
# ---------------------------------------------------------------------------

def emit_annotation(filepath: Path, lineno: int, message: str) -> None:
    """Print a GitHub Actions ``::error`` annotation to stdout."""
    # Normalise to a relative path if possible
    try:
        rel = filepath.relative_to(Path.cwd())
    except ValueError:
        rel = filepath
    print(f'::error file={rel},line={lineno}::{message}')


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Detect self-referential Markdown links (autoreferentiality check).',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        '--root',
        default='OPT-IN_FRAMEWORK',
        help='Root directory to scan (default: OPT-IN_FRAMEWORK)',
    )
    parser.add_argument(
        '--self-test',
        action='store_true',
        help='Run built-in doctests and exit',
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Entry point. Returns exit code."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.self_test:
        print('Running built-in doctests …')
        results = doctest.testmod(verbose=False)
        if results.failed:
            print(f'FAILED: {results.failed} test(s) failed out of {results.attempted}.')
            return 2
        print(f'OK: all {results.attempted} doctest(s) passed.')
        return 0

    root = Path(args.root)
    if not root.exists():
        print(f'::error::Root directory not found: {root}', file=sys.stderr)
        return 1

    findings = scan_directory(root)

    if not findings:
        print(f'✅ No autoreferential links found under `{root}`.')
        return 0

    print(f'❌ Found {len(findings)} autoreferential link(s) under `{root}`:')
    for filepath, lineno, message in findings:
        emit_annotation(filepath, lineno, message)

    return 1


if __name__ == '__main__':
    sys.exit(main())
