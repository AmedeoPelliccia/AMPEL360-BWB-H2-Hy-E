# AMPEL360 Tools

This directory contains utility scripts and tooling for the  
**AMPEL360 BWB H₂ Hy-E Q100 INTEGRA** aircraft design repository.

It is intended as the home for CI/CD helpers, data maintenance scripts, and
other repo-automation utilities.

## Layout

```text
tools/
├── ci/
│   ├── check_dimensions.py
│   ├── check_mass_properties.py
│   └── doc_meta_enforcer.py
├── genccc/
│   ├── README.md
│   ├── apply.py
│   └── report.py
├── cg/
│   ├── README.md
│   ├── scan.py
│   ├── generate.py
│   ├── expand.py
│   ├── score_relevance.py
│   └── context_index.json
├── create_release_bundle.py
├── generate_summary_tables.py
└── package_geometry_data.py

/cd/ (at repo root)
├── api.py
├── geometry/                   # Generated geometry reports
├── mass/                       # Generated mass properties reports
├── reports/                    # CG scan reports and cross-reference audits
└── publications/               # Release bundles and packages
```

* `ci/` – Continuous Integration watchdog scripts and documentation automation
* `genccc/` – GenCCC cross-reference audit and enforcement tools
* `cg/` – Continuous Generation framework for documentation evolution
* `cd/` – Continuous Delivery artifacts and API (at repo root)
* Root level scripts – Packaging, release, and summary generation tools

---

## CI Watchdog Scripts

### Geometry Baseline Watchdog

**Script:** `tools/ci/check_dimensions.py`

The **Geometry Baseline Watchdog** is an automated check that monitors *frozen* 
geometry dimensions and prevents unauthorized changes to the aircraft's 
type-design baseline.

It runs both locally and in CI (GitHub Actions) and compares key geometry
values in engineering analysis documents against the canonical
`baseline_dimensions.json` file.

#### Components

1. **Baseline dimensions – single source of truth**

   * **File:** `baseline_dimensions.json`
   * **Location:**
     `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/01_OVERVIEW/baseline_dimensions.json`
   * Contains the frozen geometry parameters for the Q100 INTEGRA configuration.

2. **Validation script**

   * **File:** `check_dimensions.py`
   * **Location:** `tools/ci/check_dimensions.py`
   * Responsibilities:

     * Parse selected engineering analysis documents
     * Extract the monitored geometry values
     * Compare them against `baseline_dimensions.json`
     * Generate a deviation report in `cd/geometry/` for ECR processing

3. **GitHub Actions workflow**

   * **File:** `.github/workflows/geometry-baseline-watchdog.yml`
   * Triggers on:

     * Changes under
       `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/**`
     * Changes to the workflow itself
     * Changes to `tools/ci/check_dimensions.py`
   * Behaviour:

     * Runs `python tools/ci/check_dimensions.py`
     * Fails the check if deviations are detected
     * Creates or updates an ECR issue with a deviation report

#### Monitored Dimensions

The following **frozen** geometry quantities are currently monitored:

**Aerodynamic geometry**

* Wingspan *(m)*
* Wing area *(m²)*
* Aspect ratio
* Cruise sweep angle *(deg)*

**Structural geometry**

* Overall length *(m)*
* Center body depth *(m)*
* Pressure vessel equivalent radius *(m)*

**Landing gear geometry**

* Main landing gear height *(m)*
* Nose landing gear height *(m)*
* Wheelbase *(m)*
* Main gear track *(m)*

Any numerical change to these values in the source documents will be detected
against the baseline.

#### Running Locally

From the repository root:

```bash
python3 tools/ci/check_dimensions.py
```

Expected output when everything matches:

```text
[geometry-check] OK – no geometry deviations vs baseline.
```

Example output when a deviation is found:

```text
[geometry-check] Deviations detected:
  - wingspan_m: baseline=52.0, current=53.0
```

and a `cd/geometry/geometry_deviations_report.md` will be generated.

#### Monitored Documents

The script currently parses geometry from these analysis reports:

* `.../06_ENGINEERING/ANALYSIS_REPORTS/AERODYNAMIC/Lift_Distribution_Analysis.md`
* `.../06_ENGINEERING/ANALYSIS_REPORTS/STRUCTURAL/Pressure_Vessel_Analysis.md`
* `.../06_ENGINEERING/ANALYSIS_REPORTS/CLEARANCE/Ground_Clearance_Calculations.md`

---

### Mass Properties Baseline Watchdog

**Script:** `tools/ci/check_mass_properties.py`

The **Mass Properties Baseline Watchdog** monitors *frozen* mass properties 
and center of gravity limits, ensuring they remain consistent with the 
certified design baseline.

Similar to the geometry watchdog, it runs in CI and locally, comparing values
extracted from engineering analysis documents against
`baseline_mass_properties.json`.

#### Components

1. **Baseline mass properties – single source of truth**

   * **File:** `baseline_mass_properties.json`
   * **Location:**
     `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-10-00_AIRCRAFT_GENERAL_DATA/01_OVERVIEW/baseline_mass_properties.json`
   * Contains frozen mass values and CG limits.

2. **Validation script**

   * **File:** `check_mass_properties.py`
   * **Location:** `tools/ci/check_mass_properties.py`
   * Responsibilities:

     * Parse mass and CG data from analysis documents
     * Compare against `baseline_mass_properties.json`
     * Generate deviation report in `cd/mass/` for ECR processing

3. **GitHub Actions workflow** *(planned)*

   * Similar to geometry watchdog
   * Monitors changes to `02-10-00_AIRCRAFT_GENERAL_DATA/**`

#### Monitored Properties

The following **frozen** mass properties are monitored:

**Design Weights**

* MTOW (Maximum Takeoff Weight) *(kg)*
* OEW (Operating Empty Weight) *(kg)*
* MZFW (Maximum Zero Fuel Weight) *(kg)*
* MLW (Maximum Landing Weight) *(kg)*

**Capacity Limits**

* Maximum fuel mass *(kg)*
* Maximum payload *(kg)*

**CG Envelope Limits**

* Forward CG limit *(% MAC)*
* Aft CG limit *(% MAC)*

#### Running Locally

From the repository root:

```bash
python3 tools/ci/check_mass_properties.py
```

Expected output when everything matches:

```text
[mass-check] OK – no mass property deviations vs baseline.
```

Example output when a deviation is found:

```text
[mass-check] Deviations detected:
  - mtow_kg: baseline=186000.0, current=187000.0
```

and a `cd/mass/mass_properties_deviations_report.md` will be generated.

#### Monitored Documents

The script parses mass properties from:

* `.../06_ENGINEERING/ANALYSIS_REPORTS/MASS/Mass_Breakdown_Analysis.md`
* `.../06_ENGINEERING/ANALYSIS_REPORTS/MASS/CG_Envelope_Analysis.md`

---

### Document Metadata Enforcer

**Script:** `tools/ci/doc_meta_enforcer.py`

The **Document Metadata Enforcer** automates documentation maintenance across the entire OPT-IN_FRAMEWORK:

1. **AI Attribution**: Ensures all documents have proper AI generation attribution in Document Control sections
2. **CAOS Awareness**: Adds Computer Aided Operations and Services integration notes where applicable
3. **Internal Linking**: Converts internal document references to proper hyperlinks
4. **Stub Generation**: Creates placeholder documents for missing referenced files

#### Framework Coverage

The tool processes all five OPT-IN_FRAMEWORK areas:

- **I-INFRASTRUCTURES** (2,530 files): Infrastructure and Foundational Systems
- **N-NEURAL_NETWORKS_USERS_TRACEABILITY** (882 files): Neural Networks and AI Systems
- **O-ORGANIZATION** (3,419 files): Organizational Structure and Governance
- **P-PROGRAM** (3,139 files): Program Management and Planning
- **T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS** (5,299 files): Technology and On-Board Systems

**Total: 15,270 markdown files** across all framework areas and ATA chapters.

#### Automation Features

**AI Attribution Management:**
- Automatically adds "Generated by: AI (prompted by Amedeo Pelliccia)" to Document Control sections
- Maintains consistent attribution across all AI-generated documentation
- Updates approval workflow to "To be approved by: [Team Name]"

**CAOS (Computer Aided Operations and Services) Integration:**
- Automatically detects CAOS-related documents based on content and path
- Adds "CAOS Integration: This document is part of the Computer Aided Operations and Services framework" where applicable
- Applies to documents containing operations, automation, neural networks, AI, and services keywords
- Supports the central CAOS behavioral framework across all OPT-IN areas

**Internal Reference Linking:**
- Detects bare internal paths like `01_OVERVIEW/baseline_dimensions.json`
- Converts them to markdown links: `[01_OVERVIEW/baseline_dimensions.json](01_OVERVIEW/baseline_dimensions.json)`
- Skips paths already properly linked
- Supports `.md`, `.csv`, and `.json` file references

**Missing Document Stub Generation:**
- Detects referenced documents that don't exist
- Creates minimal stub documents with standard templates
- For `.md` files: Creates full document with headers and Document Control
- For `.csv` files: Creates placeholder with basic structure
- For `.json` files: Creates placeholder with comment

#### Running Locally

**Check mode** (reports issues without making changes):

```bash
# Default: Check ATA_02-OPERATIONS_INFORMATION only (CI-friendly)
python3 tools/ci/doc_meta_enforcer.py --check

# Check entire OPT-IN_FRAMEWORK directory (retrofit mode)
python3 tools/ci/doc_meta_enforcer.py --check --scope entire
```

**Fix mode** (applies all corrections and creates stubs):

```bash
# Default: Fix ATA_02-OPERATIONS_INFORMATION only
python3 tools/ci/doc_meta_enforcer.py --fix

# Retrofit entire repository (15,000+ markdown files)
python3 tools/ci/doc_meta_enforcer.py --fix --scope entire

# Alternative: use 'full' instead of 'entire'
python3 tools/ci/doc_meta_enforcer.py --fix --scope full
```

**Scope Options:**
- `--scope ata02` (default): Processes only `ATA_02-OPERATIONS_INFORMATION/` directory (CI-friendly, ~500 files)
- `--scope entire` or `--scope full`: Processes entire `OPT-IN_FRAMEWORK/` directory (retrofit mode, ~15,000 files)

Expected output when issues are found:

```text
[doc-meta] Issues found:
  - path/to/file.md: missing AI generation line in Document Control
  - path/to/file.md: added markdown links for internal document references
  - path/to/file.md: referenced missing internal document path/to/missing.md
```

Expected output when everything is compliant:

```text
[doc-meta] OK – all docs compliant.
```

#### CI Integration

The tool runs automatically in GitHub Actions (`.github/workflows/doc-meta.yml`) and:

- Checks all markdown files under `ATA_02-OPERATIONS_INFORMATION/` (default scope for CI performance)
- Fails the CI check if any issues are found
- Provides clear error messages for local fixes
- **Uploads SARIF results** to GitHub Code Scanning for inline PR annotations
- **Creates job summaries** with first 50 lines of issues
- **Uploads full logs** as artifacts (30-day retention)

**SARIF Integration:**

The tool generates [SARIF](https://sarifweb.azurewebsites.net/) (Static Analysis Results Interchange Format) output that integrates with GitHub Code Scanning:

- **Inline annotations**: Issues appear directly on files in PR diffs
- **Three rule types**: `missing-ai-attribution`, `unlinked-internal-reference`, `missing-referenced-document`
- **Clickable help**: Each annotation links to relevant documentation
- **Professional UI**: Same experience as CodeQL and other security scanners

**Note:** CI uses default scope (`--scope ata02`) to keep build times reasonable. For repository-wide retrofits, run locally with `--scope entire`.

To resolve CI failures:

```bash
# Run fix locally (matches CI scope)
python3 tools/ci/doc_meta_enforcer.py --fix

# For comprehensive repository-wide retrofit
python3 tools/ci/doc_meta_enforcer.py --fix --scope entire

# Generate SARIF report for local inspection
python3 tools/ci/doc_meta_enforcer.py --check --sarif results.sarif

# Commit the changes
git add .
git commit -m "Fix document metadata and references"
```

#### Repository-Wide Retrofit

To apply metadata standards across the entire repository (all 5 OPT-IN_FRAMEWORK areas, ~15,000 markdown files):

```bash
# Dry run first - see what would be changed across all framework areas
python3 tools/ci/doc_meta_enforcer.py --check --scope entire 2>&1 | tee retrofit-check.log

# Shows breakdown by framework area:
# - I-INFRASTRUCTURES (2,530 files)
# - N-NEURAL_NETWORKS_USERS_TRACEABILITY (882 files)
# - O-ORGANIZATION (3,419 files)
# - P-PROGRAM (3,139 files)
# - T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS (5,299 files)

# Apply changes with CAOS awareness (may take several minutes)
python3 tools/ci/doc_meta_enforcer.py --fix --scope entire 2>&1 | tee retrofit-fix.log

# Review changes before committing
git status
git diff --stat

# Commit by framework area for manageable PRs
git add OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY
git commit -m "Add AI attribution and CAOS awareness to Neural Networks documentation"

git add OPT-IN_FRAMEWORK/P-PROGRAM
git commit -m "Add AI attribution to Program documentation"

git add OPT-IN_FRAMEWORK/O-ORGANIZATION
git commit -m "Add AI attribution to Organization documentation"
```

**Performance Note:** 
- Processing the entire repository (~15,270 files) takes 5-10 minutes depending on system performance
- The default `--scope ata02` processes ~500 files in under 30 seconds (CI-friendly)
- When using `--scope entire`, CAOS awareness is automatically enabled for applicable documents

#### Use Cases

* **Consistent Attribution**: Ensures all AI-generated docs have proper traceability across all framework areas
* **CAOS Integration**: Automatically identifies and marks CAOS-related documentation
* **Documentation Hygiene**: Automatically maintains internal reference links
* **Prevents Broken Links**: Creates stubs for missing referenced documents
* **Quality Gates**: Enforces documentation standards in CI
* **Developer Productivity**: Automates manual documentation maintenance tasks
* **Repository Retrofit**: Apply standards to existing documentation at scale across all 15,270 files
* **Framework-Wide Compliance**: Ensures consistency across all 5 OPT-IN_FRAMEWORK areas
* **ATA Chapter Coverage**: Processes all ATA chapters across Infrastructure, Neural Networks, Organization, Program, and Technology areas

---

## Packaging and Release Tools

### Geometry Data Packager

**Script:** `tools/package_geometry_data.py`

Creates a tar.gz archive containing frozen geometry baseline data and analysis
reports for external delivery or archival.

#### Usage

```bash
# Create package with default settings
python3 tools/package_geometry_data.py

# Custom output directory
python3 tools/package_geometry_data.py -o /path/to/output

# Add suffix to archive name
python3 tools/package_geometry_data.py --suffix v2.0
```

#### Output

Creates an archive in `cd/publications/` containing:

* `baseline_dimensions.json`
* All analysis reports from `06_ENGINEERING/ANALYSIS_REPORTS/`
* Requirements from `03_REQUIREMENTS/`
* Overview documentation from `01_OVERVIEW/`

Archive filename format: `geometry_baseline_YYYYMMDD-HHMMSS[_suffix].tar.gz`

#### Use Cases

* Providing geometry baseline to external partners
* Creating versioned geometry snapshots for ECR documentation
* Archiving approved configurations
* Input data for external analysis tools

---

### Release Bundle Creator

**Script:** `tools/create_release_bundle.py`

Creates versioned release bundles with manifest files for deployment.

#### Usage

```bash
# Create release bundle
python3 tools/create_release_bundle.py

# Custom output directory
python3 tools/create_release_bundle.py -o /path/to/output
```

#### Output

Creates a tar.gz bundle in `cd/publications/` containing:

* `baseline_mass_properties.json` (if exists)
* Release manifest with metadata
* Timestamp and version information

Archive filename format: `ampel360_release_YYYYMMDD-HHMMSS.tar.gz`

#### Manifest Contents

The manifest JSON includes:

* Generation timestamp
* Mass baseline presence indicator
* Future: geometry package reference
* Future: additional artifact metadata

#### Use Cases

* Creating deliverables for milestone reviews
* Packaging documentation for certification submissions
* Distributing data to stakeholders
* Creating versioned snapshots of project state

---

## Summary Table Generator

**Script:** `tools/generate_summary_tables.py`

Converts CSV analysis results into markdown summary tables for documentation.

#### Usage

```bash
# Generate tables from default CSV files
python3 tools/generate_summary_tables.py

# Process specific CSV files
python3 tools/generate_summary_tables.py file1.csv file2.csv

# Custom output directory
python3 tools/generate_summary_tables.py -o /path/to/output

# Process all CSVs from a directory
python3 tools/generate_summary_tables.py *.csv
```

#### Output

Generates markdown files in
`OPT-IN_FRAMEWORK/.../01_OVERVIEW/TABLES/Generated_Summaries/` by default.

Each CSV file is converted to a markdown table with the same base name.

#### CSV Format

Input CSV files should have:

* First row: Column headers
* Subsequent rows: Data

Example:

```csv
Parameter,Value,Unit,Status
Wingspan,52.0,m,Verified
Wing Area,845.0,m²,Verified
```

Converts to:

```markdown
| Parameter | Value | Unit | Status |
| --- | --- | --- | --- |
| Wingspan | 52.0 | m | Verified |
| Wing Area | 845.0 | m² | Verified |
```

#### Use Cases

* Auto-generating documentation tables from V&V results
* Creating summary tables for design reviews
* Consolidating analysis data for reports
* Maintaining consistency between source data and documentation

---

## CD API Server

**Script:** `cd/api.py` (at repository root)

HTTP API server that executes CI watchdog scripts and returns reports.

#### Starting the Server

```bash
# From repository root
python3 cd/api.py

# Server starts on http://0.0.0.0:8000
```

#### Endpoints

**POST /cd/geometry**

Runs `tools/ci/check_dimensions.py` and returns the result.

Response when no deviations:

```json
{
  "status": "ok",
  "ci_returncode": 0,
  "message": "No geometry deviations vs baseline.",
  "stdout": "[geometry-check] OK – no geometry deviations vs baseline.",
  "stderr": ""
}
```

Response when deviations found:

```json
{
  "status": "deviations",
  "ci_returncode": 1,
  "report_path": "cd/geometry/geometry_deviations_report.md",
  "report_content": "# Geometry Baseline Deviation Detected\n\n...",
  "stdout": "[geometry-check] Deviations detected:...",
  "stderr": ""
}
```

**POST /cd/mass**

Runs `tools/ci/check_mass_properties.py` and returns the result.

Response format is identical to `/cd/geometry`.

**GET /cd/geometry**

Returns the last generated geometry report without running the CI script.

**GET /cd/mass**

Returns the last generated mass properties report without running the CI script.

#### Usage Examples

```bash
# Trigger geometry check
curl -X POST http://localhost:8000/cd/geometry

# Trigger mass properties check
curl -X POST http://localhost:8000/cd/mass

# Read last geometry report
curl http://localhost:8000/cd/geometry

# Read last mass report
curl http://localhost:8000/cd/mass
```

#### Use Cases

* Remote execution of CI checks from external tools
* Integration with custom dashboards
* Automated reporting pipelines
* RESTful access to baseline validation

---

## Extending the Watchdogs

### Adding New Dimensions to Geometry Watchdog

1. Add the new key and value to `baseline_dimensions.json`
2. Extend `collect_current_values()` in `tools/ci/check_dimensions.py`:

   * Parse the value from the relevant document(s)
   * Use a robust regex pattern with a named capture group `(?P<val>...)`
3. Run locally to verify the new parameter is picked up and compared
4. Update this README if necessary

### Adding New Mass Properties

1. Add the new key and value to `baseline_mass_properties.json`
2. Extend `collect_current_values()` in `tools/ci/check_mass_properties.py`
3. Test locally
4. Update documentation

---

## Integration with CI/CD

### GitHub Actions Integration

Both watchdog scripts are designed for GitHub Actions workflows:

```yaml
- name: Run geometry baseline check
  run: python tools/ci/check_dimensions.py

- name: Run mass properties check
  run: python tools/ci/check_mass_properties.py
```

### Example Deployment Pipeline

```bash
#!/bin/bash
# Automated deployment script

# Run all checks
python3 tools/ci/check_dimensions.py
python3 tools/ci/check_mass_properties.py

# Package geometry data
python3 tools/package_geometry_data.py

# Create release bundle
python3 tools/create_release_bundle.py

# Generate summary tables
python3 tools/generate_summary_tables.py

# Upload to artifact storage
# aws s3 cp cd/publications/ s3://artifacts/releases/ --recursive
```

---

## Tolerance Settings

Both watchdog scripts use strict absolute tolerance:

```python
TOLERANCE_ABS = 1e-6
```

This effectively treats any change in a frozen dimension or mass property as a 
deviation, ensuring maximum control over baseline changes.

---

## Troubleshooting

**Problem:** CI fails with `Baseline file not found`  
**Cause:** Baseline JSON file missing or path changed  
**Fix:** Verify the baseline file exists at the documented path

**Problem:** CI fails with `Expected file not found`  
**Cause:** One of the monitored analysis reports is missing or renamed  
**Fix:** Restore the file to its expected location or update the script + workflow

**Problem:** CI fails with `Could not find value for '...'`  
**Cause:** Document format changed and the regex no longer matches  
**Fix:** Ensure dimension/mass values are formatted exactly as expected  
(e.g. `Wingspan (b): **52.0 m`)

**Problem:** API server returns "CI script not found"  
**Cause:** Running API from wrong directory  
**Fix:** Always run `cd/api.py` from the repository root

---

## Future Extensions

Planned or possible additions:

* Additional watchdogs for:
  * Performance parameters
  * System weights breakdown
  * Configuration items
* Enhanced packaging:
  * Docker container builder for analysis tools
  * [S1000D](http://www.s1000d.org/) publication packager
  * Automated changelog generation
* Deployment automation:
  * Rollback scripts
  * Deployment verification
  * Health check endpoints
* API enhancements:
  * Authentication
  * Webhook integrations
  * Real-time notifications

---

## Best Practices

1. **Baseline Changes**: Always use ECR process for frozen baseline updates
2. **Versioning**: Tag releases with semantic versions (v1.0.0)
3. **Documentation**: Keep analysis documents formatted consistently
4. **Testing**: Run watchdogs locally before committing changes
5. **Archival**: Store release bundles in version-controlled artifact storage

---

**Owner:**  
Dimensions & Geometry V&V / DevOps / Configuration Management

**Related Documentation:**
* [Verification & Validation Plan](../OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-00-00_GENERAL/07_V_AND_V/Verification_Validation_Plan.md) (14_META_GOVERNANCE)
* [Configuration Management Plan](../OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-00-00_GENERAL/13_SUBSYSTEMS_COMPONENTS/CONFIGURATION_CONTROL/Configuration_Management_Plan.md) (14_META_GOVERNANCE)
* Quality Manual / [AS9100](https://www.sae.org/standards/content/as9100d/) QMS documentation

For process and governance details, see the [Configuration Management Plan](../OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-00-00_GENERAL/13_SUBSYSTEMS_COMPONENTS/CONFIGURATION_CONTROL/Configuration_Management_Plan.md).
