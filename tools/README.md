# AMPEL360 Tools

This directory contains utility scripts and tools for maintaining the AMPEL360 BWB H₂ Hy-E Q100 INTEGRA aircraft design repository.

## Geometry Baseline Watchdog

### Overview

The Geometry Baseline Watchdog is an automated system that monitors frozen geometry dimensions and prevents unauthorized changes to the aircraft's type-design baseline.

### Components

1. **baseline_dimensions.json** - Single source of truth
   - Location: `02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/01_OVERVIEW/baseline_dimensions.json`
   - Contains frozen geometry parameters for the Q100 INTEGRA configuration
   
2. **check_dimensions.py** - Validation script
   - Location: `tools/check_dimensions.py`
   - Parses engineering analysis documents and compares against baseline
   - Generates deviation reports for ECR processing

3. **GitHub Actions Workflow** - CI automation
   - Location: `.github/workflows/geometry-baseline-watchdog.yml`
   - Automatically runs on PRs and pushes to 02-11-00 directory
   - Creates/updates ECR issues when deviations detected

### Monitored Dimensions

The following frozen dimensions are monitored:

**Aerodynamic Geometry:**
- Wingspan (m)
- Wing area (m²)
- Aspect ratio
- Cruise sweep angle (°)

**Structural Geometry:**
- Overall length (m)
- Center body depth (m)
- Pressure vessel equivalent radius (m)

**Landing Gear Geometry:**
- Main landing gear height (m)
- Nose landing gear height (m)
- Wheelbase (m)
- Main gear track (m)

### How It Works

1. **Automatic Checking**: 
   - When you create a PR or push to main that modifies files in `02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/`
   - The workflow automatically runs `check_dimensions.py`

2. **If No Deviations**:
   - CI check passes ✅
   - PR can be merged normally

3. **If Deviations Detected**:
   - CI check fails ❌
   - A `geometry_deviations_report.md` is generated
   - GitHub automatically creates/updates an ECR issue with labels: `ECR`, `02-11-00`, `geometry-change`
   - The issue includes a detailed table of deviations

### Usage

#### Running Locally

```bash
# From repository root
python3 tools/check_dimensions.py
```

Expected output when dimensions match:
```
[geometry-check] OK – no geometry deviations vs baseline.
```

Expected output when deviations detected:
```
[geometry-check] Deviations detected:
  - wingspan_m: baseline=52.0, current=53.0
```

#### Updating Frozen Geometry (ECR Process)

When geometry changes are approved through the ECR process:

1. Update all relevant engineering documents with new values
2. Update `baseline_dimensions.json` with the new frozen values
3. Commit both changes together in the same PR
4. Reference the ECR issue number in the commit message

This keeps the CI green and marks the official change to the type-design baseline.

### Monitored Documents

The script currently parses geometry from these analysis reports:

- `ANALYSIS_REPORTS/AERODYNAMIC/Lift_Distribution_Analysis.md`
- `ANALYSIS_REPORTS/STRUCTURAL/Pressure_Vessel_Analysis.md`
- `ANALYSIS_REPORTS/CLEARANCE/Ground_Clearance_Calculations.md`

### Extending the Watchdog

To monitor additional dimensions:

1. Add the new parameter to `baseline_dimensions.json`
2. Update `collect_current_values()` in `check_dimensions.py` to parse the value from relevant documents
3. Test locally before committing

### Tolerance

The system uses a strict tolerance of `1e-6` (essentially zero tolerance for numerical changes). Any modification to a frozen dimension will be detected.

### Troubleshooting

**Issue**: CI fails with "Expected file not found"
- **Cause**: Analysis document is missing or moved
- **Solution**: Verify all monitored documents exist at expected paths

**Issue**: CI fails with "Could not find value for..."
- **Cause**: Document format changed or value not present
- **Solution**: Check that dimension values are marked with bold (`**`) and match expected format

**Issue**: False positive deviation
- **Cause**: Floating point rounding or format inconsistency
- **Solution**: Verify values are consistently formatted in documents (e.g., always "52.0", not "52")

### References

- Problem statement: Issue describes the full ECR workflow
- Coordinate system: `02-11-00-TN-002 Coordinate_Systems_and_Reference_Frames`
- Ground clearance: `02-11-00-CLR-001 Ground_Clearance_Calculations`
- Weight & balance: `02-11-00-WB-001 CG_Envelope_Calculation`
