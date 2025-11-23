---
description: "Python tools for geometry, mass, and documentation automation"
applyTo: "tools/**/*.py"
---

## Python Tools Guidelines

- Target **Python 3.11+** and use type hints where reasonable.
- Keep scripts **idempotent** and safe to run in CI:
  - Operate only on files in the repo.
  - Avoid network calls unless explicitly required.
- Structure:
  - Put core logic into functions or small modules.
  - Reserve the `__main__` block for CLI argument parsing and orchestration.
- Logging:
  - Use the standard `logging` module.
  - Avoid noisy `print` statements in library code.
- Error handling:
  - Fail fast with clear messages when inputs are invalid.
  - Prefer raising well-typed exceptions over silent failures.
- Tests:
  - When you add or change non-trivial logic, add/extend tests (pytest-style) in `tests/` or adjacent `*_tests.py` files.
- Respect **file format policies**:
  - Read/write Markdown, CSV, YAML, JSON, SVG only.
  - Do not create `.xlsx`, `.docx`, or `.pdf` from these tools.
