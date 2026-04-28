# Contributing to AMPEL360-AIR-T

Thank you for contributing to the AMPEL360-AIR-T repository.
This guide covers the conventions and local tooling you need before opening a PR.

---

## Table of Contents

- [Documentation](#documentation)
  - [Link Hygiene — Sempre Annanz, No Acopp](#link-hygiene--sempre-annanz-no-acopp)
  - [Running Lychee Locally](#running-lychee-locally)
  - [Running the Autoreferentiality Checker Locally](#running-the-autoreferentiality-checker-locally)
- [Conventional Commits](#conventional-commits)
- [CI Checks](#ci-checks)

---

## Documentation

### Link Hygiene — *Sempre Annanz, No Acopp*

> **Sempre annanz, no acopp.**
> *Always forward, never loop back on yourself.*

Every cross-reference in the documentation must move the reader **forward** in
the dependency graph.  A document must **never** contain a relative Markdown
link that resolves back to itself — whether in the H1 heading or anywhere in
the body.

**Why this matters:**
- Self-referential links break graph-traversal tooling (Obsidian, Docusaurus,
  lychee, link-graph dashboards).
- They confuse certification auditors navigating requirement chains.
- They pollute backlink indices and generate false positive traceability entries.

Two specific defect classes are enforced by CI:

| Class | Example | Detected by |
|---|---|---|
| H1 self-link | `# [ID](./ID_file.md): Title` inside `ID_file.md` | `scripts/check_autoreferentiality.py` |
| Inline self-link | `](./foo.md)` anywhere inside `foo.md` | `scripts/check_autoreferentiality.py` |
| Broken relative link | Link points to a file that does not exist | [lycheeverse/lychee](https://github.com/lycheeverse/lychee-action) |

---

### Running Lychee Locally

[Lychee](https://github.com/lycheeverse/lychee) checks all relative and
external links in Markdown files.

**Using Docker (no install required):**

```bash
docker run --rm \
  -v "$PWD:/data" \
  lycheeverse/lychee \
  --config /data/.lychee.toml \
  --no-progress \
  "/data/**/*.md"
```

**Using the lychee binary:**

```bash
# Install
cargo install lychee   # or: brew install lychee

# Run
lychee --config .lychee.toml --no-progress "**/*.md"
```

Internal broken links cause a non-zero exit code.
External links that return 403 or 429 are treated as warnings (see
`.lychee.toml` for the full policy).

---

### Running the Autoreferentiality Checker Locally

`scripts/check_autoreferentiality.py` is a self-contained Python 3 script
(stdlib only — no external dependencies).

```bash
# Run against the full OPT-IN_FRAMEWORK tree (default)
python scripts/check_autoreferentiality.py

# Run against a specific subdirectory
python scripts/check_autoreferentiality.py --root OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME

# Run built-in doctests (sanity check)
python scripts/check_autoreferentiality.py --self-test
```

**Sample annotation output** (GitHub Actions format):

```
::error file=OPT-IN_FRAMEWORK/…/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md,line=1::H1 self-link in `53-00-03-01-005_Compatibility_with_SHM_Assumptions.md` at line 1: target `./53-00-03-01-005_Compatibility_with_SHM_Assumptions.md` resolves to this file. Sempre annanz, no acopp. Remove the link from the H1 heading. Replace with plain text, e.g.: `# 53-00-03-01-005 — <title>`
```

**Fix:**

```diff
- # [53-00-03-01-005](./53-00-03-01-005_Compatibility_with_SHM_Assumptions.md): Compatibility with SHM Assumptions
+ # 53-00-03-01-005 — Compatibility with SHM Assumptions
```

Exit code `0` → no issues found.
Exit code `1` → one or more self-referential links detected.
Exit code `2` → `--self-test` failures (should never happen on a clean install).

---

## Conventional Commits

All commits must follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description>
```

Common types used in this repository:

| Type | Usage |
|---|---|
| `ci` | CI/CD workflow changes |
| `docs` | Documentation-only changes |
| `feat` | New features |
| `fix` | Bug fixes |
| `refactor` | Code refactoring |
| `chore` | Maintenance tasks |

Example: `ci(docs): add link + autoreferentiality validator for Markdown`

---

## CI Checks

The following CI checks run automatically on PRs touching `*.md` files:

| Workflow | Checks |
|---|---|
| **Docs — Link & Autoreferentiality Validator** | Broken relative links (lychee), H1 self-links, inline self-links |
| **CI** | Python syntax, tests, dimension/mass checks, doc-meta enforcement |
| **License Compliance** | SPDX headers on source files |

Ensure all checks pass before requesting a review.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-AIR-T`
- Last AI update: _2026-04-28_.

---
