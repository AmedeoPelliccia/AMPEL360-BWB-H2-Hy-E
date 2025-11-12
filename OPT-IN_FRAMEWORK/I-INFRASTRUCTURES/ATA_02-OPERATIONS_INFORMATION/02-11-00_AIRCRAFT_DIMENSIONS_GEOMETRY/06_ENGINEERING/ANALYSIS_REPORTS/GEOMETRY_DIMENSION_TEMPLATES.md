# Geometry Dimension Templates

**Purpose:** This document provides standardized templates for reporting frozen geometry dimensions in analysis reports to ensure compatibility with the Geometry Baseline Watchdog CI system.

**Component Code:** 02-11-00  
**Last Updated:** 2025-11-10

---

## Overview

The Geometry Baseline Watchdog parses specific dimensions from analysis reports and compares them against `baseline_dimensions.json`. To ensure proper parsing, dimensions must be formatted according to the patterns below.

**Key formatting requirements:**
- Use bold markers (`**`) around labels
- Include standard units
- Use exact label text as shown
- Values must be numeric (integers or decimals)

---

## Template 1: Aerodynamic Geometry

**File:** `ANALYSIS_REPORTS/AERODYNAMIC/Lift_Distribution_Analysis.md`

**Section:** `### 2.2 Geometry` or similar

**Required format:**

```markdown
### 2.2 Geometry
- **Wingspan (b):** 52.0 m
- **Wing area (S):** 845 m²
- **Aspect ratio (AR):** 3.2
- **Sweep (Λ):** 35° at quarter-chord
```

**Alternative accepted format:**

```markdown
### 2.2 Geometry
Wingspan (b): ** 52.0 m
Wing area (S): ** 845 m²
Aspect ratio (AR): ** 3.2
Sweep (Λ): ** 35°
```

**Monitored parameters:**
| Parameter | Label Format | Units | Baseline Value |
|-----------|--------------|-------|----------------|
| wingspan_m | `Wingspan (b):` | m | 52.0 |
| wing_area_m2 | `Wing area (S):` | m² | 845.0 |
| aspect_ratio | `Aspect ratio (AR):` | (none) | 3.2 |
| cruise_sweep_deg | `Sweep (Λ):` | ° | 35.0 |

**Notes:**
- Use `m²` (Unicode) not `m^2` for wing area
- Additional text after the value (e.g., "at quarter-chord") is acceptable
- The parser is flexible with whitespace

---

## Template 2: Structural/Pressure Vessel Geometry

**File:** `ANALYSIS_REPORTS/STRUCTURAL/Pressure_Vessel_Analysis.md`

**Section:** `### 2.1 Geometry` or similar

**Required format:**

```markdown
### 2.1 Geometry
- **Configuration:** BWB center body, non-circular cross-section
- **Equivalent radius:** 2.1 m (local cylindrical approximation)
- **Length:** 52.5 m
- **Depth:** 4.2 m
```

**Alternative accepted format:**

```markdown
### 2.1 Geometry
Configuration: BWB center body, non-circular cross-section
Equivalent radius: ** 2.1 m (local cylindrical approximation)
Length: ** 52.5 m
Depth: ** 4.2 m
```

**Monitored parameters:**
| Parameter | Label Format | Units | Baseline Value |
|-----------|--------------|-------|----------------|
| pressure_vessel_equiv_radius_m | `Equivalent radius:` | m | 2.1 |
| overall_length_m | `Length:` | m | 52.5 |
| center_body_depth_m | `Depth:` | m | 4.2 |

**Notes:**
- Parenthetical notes after values (e.g., "(local cylindrical approximation)") are acceptable
- Only the numeric value is extracted

---

## Template 3: Landing Gear Geometry

**File:** `ANALYSIS_REPORTS/CLEARANCE/Ground_Clearance_Calculations.md`

**Section:** `### 3.1 Key Dimensions` or similar

**Required format:**

```markdown
### 3.1 Key Dimensions
- **Main landing gear (MLG) height:** 3.2 m (compressed)
- **Nose landing gear (NLG) height:** 2.8 m (compressed)
- **Wheelbase:** 18.0 m (NLG to MLG)
- **Main gear track:** 12.5 m
```

**Alternative accepted format:**

```markdown
### 3.1 Key Dimensions
Main landing gear (MLG) height: ** 3.2 m (compressed)
Nose landing gear (NLG) height: ** 2.8 m (compressed)
Wheelbase: ** 18.0 m (NLG to MLG)
Main gear track: ** 12.5 m
```

**Monitored parameters:**
| Parameter | Label Format | Units | Baseline Value |
|-----------|--------------|-------|----------------|
| mlg_height_m | `Main landing gear (MLG) height:` | m | 3.2 |
| nlg_height_m | `Nose landing gear (NLG) height:` | m | 2.8 |
| wheelbase_m | `Wheelbase:` | m | 18.0 |
| mlg_track_m | `Main gear track:` | m | 12.5 |

**Notes:**
- Parenthetical notes like "(compressed)" or "(NLG to MLG)" are acceptable
- Exact label text including "(MLG)" and "(NLG)" is required

---

## Validation

To validate that your document formatting is correct:

```bash
# Run the checker from repository root
python3 tools/check_dimensions.py
```

**Expected output if formatting is correct:**
```
[geometry-check] OK – no geometry deviations vs baseline.
```

**If formatting is incorrect:**
```
[geometry-check] ERROR: Could not find value for 'parameter_name' using pattern: ...
```

---

## Updating Frozen Dimensions (ECR Process)

When geometry changes are approved through the ECR process:

1. Update the dimension value in the appropriate analysis document(s)
2. Update the corresponding value in `01_OVERVIEW/baseline_dimensions.json`
3. Commit both changes together in the same PR
4. Reference the ECR issue number in the commit message

**Example commit message:**
```
Update wingspan to 53.0m per ECR-2024-001

- Updated Lift_Distribution_Analysis.md
- Updated baseline_dimensions.json
- Assessed impact on FEM, clearance, CG envelope
```

---

## Troubleshooting

### "Could not find value" error

**Cause:** Label text doesn't match exactly or value is missing

**Solution:** Verify label text matches templates above, including:
- Exact spelling and capitalization
- Parentheses like `(b)`, `(S)`, `(AR)`, `(Λ)`, `(MLG)`, `(NLG)`
- Special characters (Greek letters, superscripts)

### "Could not parse float" error

**Cause:** Non-numeric value found where number expected

**Solution:** Ensure value is numeric (e.g., `52.0` not `TBD` or `--`)

### Deviation detected when no change made

**Cause:** Format changed (e.g., `52` vs `52.0`) or actual value differs from baseline

**Solution:** 
- Check that numeric format matches baseline (decimal places)
- Verify no unintended edits were made
- If intentional change, follow ECR process

---

## Parser Flexibility

The watchdog parser is reasonably flexible and accepts:

✅ **Accepted variations:**
- Bullet lists: `- **Label:** value`
- Plain text: `Label: ** value`
- Extra whitespace between elements
- Parenthetical notes after values: `value (note)`
- Additional text on line: `value at quarter-chord`

❌ **Not accepted:**
- Wrong label text: `Wing span` instead of `Wingspan`
- Missing bold markers
- Wrong units: `m^2` instead of `m²` for area
- Non-numeric values: `TBD`, `--`, `N/A`
- Label in bold without value: `**Wingspan (b): 52.0 m**`

---

## Contact

For questions about geometry baseline maintenance or ECR process:
- See: `tools/README.md` 
- See: `01_OVERVIEW/README.md`
- Open an issue with label: `02-11-00`, `geometry-change`

---

**Document Control:**
- Document ID: 02-11-00-TEMPLATES-001
- Version: 1.0
- Status: Active
- Last Updated: 2025-11-10
