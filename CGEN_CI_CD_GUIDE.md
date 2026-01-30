# CGen + CI + CD Architecture Guide

**Quick Start Guide for AMPEL360 Developers**

---

## 🎯 Overview

The AMPEL360 repository uses a **three-lane architecture** for continuous development:

1. **CGen (Continuous Generation)** - Automates documentation and artifact generation
2. **CI (Continuous Integration)** - Validates all changes
3. **CD (Continuous Delivery)** - Packages and publishes releases

**Key Principle**: **CGen proposes; CI judges; CD publishes**

---

## 🚀 Quick Start

### For Developers

When you create a PR, the system automatically:

1. **CI runs** - Validates your changes (tests, linting, doc checks)
2. **GenCCC analyzes** - Generates cross-reference audit
3. **Reports uploaded** - Download artifacts to review

Your PR will show all validation results. Green checks = good to merge!

### For Documentation Writers

When working on documentation:

1. **Make your changes** in markdown files
2. **Create a PR** as usual
3. **Review GenCCC report** - Shows missing links, broken references
4. **Optional**: Comment `/genccc apply` to auto-fix simple issues

The system will help maintain proper:
- Cross-references between documents
- Document Control sections
- Hyperlinks to standards and regulations

---

## 🔧 CGen Lane - Automated Content Generation

### What CGen Does

CGen automatically generates and updates:

- **Directory indexes** (`00_INDEX.md` files)
- **GenCCC cross-reference reports**
- **Traceability matrices**
- **Summary tables**
- **Requirement skeletons**

### How CGen Works

**On Push to Main** or **Nightly Schedule**:

1. CGen workflow runs
2. Generates/updates documentation
3. **Creates a bot PR** (branch: `cgen/update-YYYYMMDD-HHMMSS`)
4. You review the PR
5. Merge when ready

**Important**: CGen never silently commits. All changes go through PR review.

### Running CGen Tools Locally

#### Generate Directory Indexes

```bash
# Dry-run (safe, see what would change)
python tools/ci/auto_index_generator.py --root OPT-IN_FRAMEWORK --dry-run

# Actually apply changes
python tools/ci/auto_index_generator.py --root OPT-IN_FRAMEWORK --write
```

#### Generate GenCCC Report

```bash
# Generate cross-reference audit
python tools/genccc/report.py

# Check generated report
cat cd/reports/cross_reference_audit.md
```

#### Generate Traceability Matrices

```bash
python tools/genccc/traceability.py
```

---

## ✅ CI Lane - Quality Validation

### What CI Checks

On every PR, CI automatically runs:

- **Python syntax checks**
- **Unit tests** (if present)
- **Dimension validation** (`check_dimensions.py`)
- **Mass property checks** (`check_mass_properties.py`)
- **Document metadata enforcement**
- **GenCCC cross-reference analysis**
- **OPT-IN structure validation**

### Running CI Checks Locally

```bash
# Run all Python syntax checks
python -m py_compile tools/**/*.py

# Run tests (if pytest installed)
pytest

# Check dimensions
python tools/ci/check_dimensions.py

# Check mass properties
python tools/ci/check_mass_properties.py

# Check doc metadata
python tools/ci/doc_meta_enforcer.py --check

# Validate OPT-IN structure
python tools/ci/optin_structure_validator.py
```

### Understanding CI Results

- **✅ Green checks**: All validations passed
- **⚠️ Yellow warnings**: Issues found but not blocking
- **❌ Red failures**: Must be fixed before merge

Download CI artifacts from the workflow run to see detailed reports.

---

## 📦 CD Lane - Release Packaging

### What CD Does

On release tags (e.g., `v02.20.15`):

1. Packages documentation bundles
2. Creates geometry data archives
3. Generates release manifest
4. **Publishes GitHub Release** with artifacts

### Creating a Release

#### Option 1: Tag Release

```bash
# Create and push a tag
git tag -a v02.20.15 -m "Release v02.20.15"
git push origin v02.20.15

# CD workflow automatically runs and creates GitHub Release
```

#### Option 2: Manual Release

1. Go to GitHub Actions
2. Select "CD - Continuous Delivery"
3. Click "Run workflow"
4. Enter version (e.g., `v02.20.15`)
5. Choose prerelease if needed
6. Run workflow

### Release Artifacts

Each release includes:

- Complete OPT-IN Framework documentation
- GenCCC reports
- Traceability matrices
- Geometry and mass baselines
- Release manifest (metadata)

---

## 📂 Directory Structure

```
.github/
  workflows/
    ci.yml          # CI pipeline
    cgen.yml        # CGen pipeline
    cd.yml          # CD pipeline

tools/
  ci/
    auto_index_generator.py      # CGen Lane 1: Directory indexer
    check_dimensions.py          # Dimension validation
    check_mass_properties.py     # Mass property validation
    doc_meta_enforcer.py         # Document metadata enforcement
    optin_structure_validator.py # OPT-IN structure validation
    genccc/
      CGEN_ARCHITECTURE.md       # Architecture documentation
  
  genccc/           # GenCCC cross-reference tools
    report.py       # Generate cross-reference audit
    validate.py     # Requirements validation
    traceability.py # Traceability matrices
    baseline.py     # Baseline management
    generate.py     # Content generation
    apply.py        # Auto-fix application
    agent.py        # Agent-driven resolution

  create_release_bundle.py       # CD: Release bundling
  generate_summary_tables.py     # CGen: Summary tables
  package_geometry_data.py       # CD: Geometry packaging

cd/               # Outputs (excluded from git except structure docs)
  reports/        # Generated reports
  publications/   # Release artifacts
  baselines/      # Requirements baselines
```

---

## 🔄 Typical Workflows

### Scenario 1: Adding New Documentation

1. Create branch: `git checkout -b feature/add-ata-chapter-docs`
2. Add your markdown files
3. Commit and push
4. **Create PR**
5. **CI runs**: Validates your changes
6. **Review GenCCC report**: Check for missing links
7. **Fix any issues** identified
8. **Get approval** and merge
9. **CGen runs**: Updates indexes nightly if needed

### Scenario 2: Fixing Documentation Issues

1. CI identifies broken links in your PR
2. Download GenCCC audit artifact
3. Review broken references
4. Option A: Fix manually
5. Option B: Comment `/genccc apply` for auto-fix
6. Review and merge

### Scenario 3: Releasing New Version

1. Ensure `main` is stable (all CI green)
2. Create release tag: `git tag v02.20.15`
3. Push tag: `git push origin v02.20.15`
4. **CD runs**: Creates release package
5. **GitHub Release** published automatically
6. Verify release artifacts

---

## 🛠️ Advanced: CGen PR Commands

On any PR, you can comment special commands:

### `/genccc apply`

Auto-applies fixes for:
- Missing hyperlinks
- Broken cross-references
- Document Control sections

**Usage**:
```
/genccc apply
```

Workflow pushes changes directly to your PR branch.

### `/genccc baseline`

Creates a requirements baseline snapshot:

**Usage**:
```
/genccc baseline
```

Generates baseline artifact for download.

### `/genccc solve`

Triggers agent-driven resolution (creates child PR):

**Usage**:
```
/genccc solve
```

Creates a child PR with comprehensive fixes.

---

## 📖 Further Reading

- [Full Architecture Documentation](tools/ci/genccc/CGEN_ARCHITECTURE.md)
- [CD Directory Structure](cd/README.md)
- [AMPEL360 Documentation Standard](AMPEL360_DOCUMENTATION_STANDARD.md)
- [OPT-IN Framework Standard](OPT-IN_FRAMEWORK_STANDARD.md)

---

## 🆘 Troubleshooting

### CI is Failing

1. **Check the CI logs** in GitHub Actions
2. **Download artifacts** for detailed reports
3. **Run checks locally** to reproduce
4. **Fix issues** and push again

### CGen PR Not Created

1. Check if there were actual changes
2. Review CGen workflow logs
3. Verify permissions (bot needs write access)

### Release Failed

1. Check CD workflow logs
2. Verify tag format: `vX.Y.Z`
3. Ensure main branch is green
4. Check permissions for release creation

### Need Help?

- Open an issue with label `cgen-support`
- Check workflow logs in Actions tab
- Review architecture docs

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- Status: **APPROVED** – User guide
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---

**Remember**: CGen proposes; CI judges; CD publishes. 🚀
