# AMPEL360 Tools

This directory contains utility scripts and tooling for the  
**AMPEL360 BWB H₂ Hy-E Q100 INTEGRA** aircraft design repository.

It is intended as the home for CI/CD helpers, data maintenance scripts, and
other repo-automation utilities.

## Layout

```text
tools/
├── ci/
│   └── check_dimensions.py
└── README.md
````

* `ci/` – Continuous Integration helper scripts
* (future) `cd/` – Continuous Delivery / deployment helpers

---

## Geometry Baseline Watchdog

### Overview

The **Geometry Baseline Watchdog** (`tools/ci/check_dimensions.py`) is an automated
check that monitors *frozen* geometry dimensions and prevents unauthorized
changes to the aircraft’s type-design baseline.

It runs both locally and in CI (GitHub Actions) and compares key geometry
values in engineering analysis documents against the canonical
`baseline_dimensions.json` file.

### Components

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
     * Generate a human-readable deviation report for ECR processing

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

---

### Monitored Dimensions

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

---

### How It Works

1. **Automatic check in CI**

   When a PR or push to `main` modifies:

   * `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/**`
   * `.github/workflows/geometry-baseline-watchdog.yml`
   * `tools/ci/check_dimensions.py`

   the workflow runs:

   ```bash
   python tools/ci/check_dimensions.py
   ```

2. **If no deviations are found**

   * Script prints:
     `[geometry-check] OK – no geometry deviations vs baseline.`
   * CI check passes ✅ and the PR can be merged normally.

3. **If deviations are detected**

   * Script prints a list of changed parameters.
   * A file `geometry_deviations_report.md` is written at the **repo root**.
   * The workflow:

     * Fails the job ❌
     * Creates or updates a GitHub issue labelled:

       * `ECR`
       * `02-11-00`
       * `geometry-change`
     * Embeds the contents of `geometry_deviations_report.md` into the issue.

---

### Running Locally

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

and a `geometry_deviations_report.md` will be generated/updated.

---

### Monitored Documents

The script currently parses geometry from these analysis reports
(relative to the repository root):

* `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/06_ENGINEERING/ANALYSIS_REPORTS/AERODYNAMIC/Lift_Distribution_Analysis.md`
* `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/06_ENGINEERING/ANALYSIS_REPORTS/STRUCTURAL/Pressure_Vessel_Analysis.md`
* `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/06_ENGINEERING/ANALYSIS_REPORTS/CLEARANCE/Ground_Clearance_Calculations.md`

> **Important:**
> These documents must follow the expected markdown formatting patterns
> (e.g. values in `**bold**` with units) so that regex parsing works.
> See `ANALYSIS_REPORTS/GEOMETRY_DIMENSION_TEMPLATES.md` for templates and examples.

---

### Updating Frozen Geometry (ECR Process)

When a geometry change is **approved** through the Engineering Change Request
workflow:

1. Update the relevant engineering analysis documents with the new values.
2. Update `baseline_dimensions.json` with the new frozen values.
3. Commit all affected files in a **single PR**.
4. Reference the ECR issue number in the commit message and/or PR description.

This ensures:

* The CI watchdog remains green.
* The repository history clearly documents changes to the type-design baseline.

---

### Extending the Watchdog

To monitor additional parameters:

1. Add the new key and value to `baseline_dimensions.json`.
2. Extend `collect_current_values()` in `tools/ci/check_dimensions.py` to:

   * Parse the value from the relevant document(s).
   * Use a robust regex pattern with a named capture group `(?P<val>...)`.
3. Run locally to verify the new parameter is picked up and compared.
4. Update this README if necessary.

---

### Tolerance

The comparison currently uses a strict absolute tolerance:

```python
TOLERANCE_ABS = 1e-6
```

This effectively treats any change in a frozen dimension as a deviation.

---

### Troubleshooting

**Problem:** CI fails with `Baseline file not found`
**Cause:** `baseline_dimensions.json` missing or path changed.
**Fix:** Verify the baseline file exists at the documented path.

---

**Problem:** CI fails with `Expected file not found`
**Cause:** One of the monitored analysis reports is missing or renamed.
**Fix:** Restore the file to its expected location or update the script + workflow.

---

**Problem:** CI fails with `Could not find value for '...'`
**Cause:** Document format changed and the regex no longer matches.
**Fix:** Ensure that dimension values are formatted exactly as expected
(e.g. `Wingspan (b): ** 52.0 m`).

---

## Future Extensions

Planned or possible additions:

* `tools/cd/` – Deployment / packaging helpers
* Additional geometry or mass properties watchdogs
* Tools to auto-generate summary tables from source data

---

**Owner:**
Dimensions & Geometry V&V / DevOps (TBD)

For process and governance details, see:

* V&V Plan (14_META_GOVERNANCE)
* Configuration Management Plan (14_META_GOVERNANCE)
* Quality Manual / AS9100 QMS documentation



