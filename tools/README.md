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
│   └── check_mass_properties.py
├── package_geometry_data.py
├── create_release_bundle.py
├── generate_summary_tables.py
└── README.md

/cd/ (at repo root)
├── api.py
├── geometry/                   # Generated geometry reports
├── mass/                       # Generated mass properties reports
└── publications/               # Release bundles and packages
```

* `ci/` – Continuous Integration watchdog scripts
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
  * S1000D publication packager
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
* V&V Plan (14_META_GOVERNANCE)
* Configuration Management Plan (14_META_GOVERNANCE)
* Quality Manual / AS9100 QMS documentation

For process and governance details, see the Configuration Management Plan.
