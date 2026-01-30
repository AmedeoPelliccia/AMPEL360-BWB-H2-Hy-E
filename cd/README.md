# CD - Continuous Delivery Directory

This directory contains outputs from the **CD (Continuous Delivery)** lane of the CGen + CI + CD architecture.

## Directory Structure

```
cd/
├── reports/          # Generated audit and traceability reports
├── publications/     # Release bundles and documentation packages
├── baselines/        # Requirements baselines and snapshots
└── costs/            # Cost analysis and metrics
```

## Subdirectories

### `reports/`
Contains generated reports from the CI and CGen lanes:
- **GenCCC cross-reference audits**: `cross_reference_audit.md`
- **Requirements validation**: `requirements_validation.md`
- **Traceability matrices**: `requirements_traceability_matrix.md`, `verification_coverage_matrix.md`
- **Baseline diffs**: `baseline_diff.md`
- **Summary reports**: Various summary and analysis reports

These reports are generated during CI/CGen workflows and are used for:
- Documentation quality assessment
- Certification traceability
- Change impact analysis
- Compliance verification

### `publications/`
Contains release-ready artifacts:
- **Release bundles**: Compressed archives with complete documentation
- **Geometry packages**: Aircraft geometry and dimensional data
- **Documentation exports**: PDF sets, static site content
- **Release manifests**: Version metadata and contents lists

Publications are created by the CD workflow and published as GitHub Release assets.

### `baselines/`
Contains requirements baselines:
- **Requirements snapshots**: JSON files capturing requirements state at specific points
- **Baseline metadata**: Timestamps, versions, commit references
- **Historical tracking**: Enables requirements evolution tracking

Baselines are created via `/genccc baseline` command or CD workflow triggers.

### `costs/`
Contains cost analysis and resource utilization metrics.

## Usage

### Accessing Reports

Reports are generated automatically during CI/CGen workflows and uploaded as artifacts:

```bash
# Download from GitHub Actions artifacts
# Or view in workflow run summary
```

### Creating Publications

Publications are created automatically on release tags:

```bash
git tag -a v02.20.15 -m "Release v02.20.15"
git push origin v02.20.15
# CD workflow creates publication bundle
```

Or manually via workflow dispatch:

```bash
# GitHub Actions UI > CD - Continuous Delivery > Run workflow
```

### Creating Baselines

Baselines can be created via comment on PRs:

```
/genccc baseline
```

Or via CI/CGen workflows automatically.

## Exclusions

The `cd/` directory is excluded from certain validations:
- Documentation structure enforcement (auto-generated content)
- Cross-reference validation (reports may contain unresolved references)
- Metadata enforcement (reports don't need Document Control sections)

## Integration with CGen + CI + CD

- **CGen Lane**: Generates reports and updates in `cd/reports/`
- **CI Lane**: Validates quality, reads reports for enforcement
- **CD Lane**: Packages content from `cd/` into publication bundles

## Cleaning

The `cd/` directory should generally not be committed to Git except for:
- `costs/` subdirectory (persistent cost tracking)
- Critical baseline snapshots (via explicit commit)

Most content in `cd/` is transient and generated per-workflow.

Add to `.gitignore` if needed:
```
cd/reports/*
cd/publications/*
cd/baselines/*.json
```

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- Status: **APPROVED** – Directory structure documentation
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---

For more information on the CGen + CI + CD architecture, see:
- [CGen Architecture](../tools/ci/genccc/CGEN_ARCHITECTURE.md)
- [Workflow Documentation](../.github/workflows/)
