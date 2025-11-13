# CI/CD Validation Rules for ReFuelEU Compliance

**Document ID:** 02-90-01-007A  
**Version:** 1.0  
**Date:** 2025-11-12  
**Status:** ACTIVE

---

## 1. Purpose

This document defines **automated validation rules** for continuous integration and continuous deployment (CI/CD) of ReFuelEU Aviation compliance data. It provides hard checks (blocking), soft checks (warnings), and integration points for AMPEL360 data pipelines.

---

## 2. Validation Philosophy

### Goals

1. **Early Detection:** Catch compliance errors before annual reporting deadline
2. **Data Quality:** Ensure Article 8 data accuracy and completeness
3. **Regulatory Alignment:** Validate against ReFuelEU regulation requirements
4. **Cross-System Consistency:** Check alignment with Article 9 supplier data, Article 7 airport infrastructure
5. **Audit Trail:** Log all validation results for IV&V and verifier review

### Integration Points

**AMPEL360 Data Sources:**
- **Fuel Management System:** H₂ and SAF uplift logs
- **Flight Operations Database:** Departure airports, flight counts, hours
- **Procurement System:** SAF purchase orders and supplier data
- **DPP/CAOS (ATA 95):** Consolidated data warehouse

**Validation Triggers:**
- **Real-time:** Upon data entry/import (immediate feedback)
- **Daily:** Nightly batch validation of all compliance data
- **Pre-Submission:** Final check before Article 8 report submission (March)
- **CI/CD Pipeline:** Automated tests on code commits affecting compliance logic

---

## 3. Hard Checks (Blocking Errors)

These checks **MUST** pass; failures block report submission.

### HC-01: Reporting Deadlines

**Rule:** Critical dates must be met.

```python
# Pseudocode
def check_reporting_deadlines(reporting_year):
    supplier_data_deadline = f"{reporting_year + 1}-02-14"
    operator_report_deadline = f"{reporting_year + 1}-03-31"
    
    # Check supplier data received
    if supplier_data.received_by > supplier_data_deadline:
        raise BlockingError("Supplier SAF data received after 14-Feb deadline (Art. 9(2))")
    
    # Check operator report submission
    if operator_report.submitted_by > operator_report_deadline:
        raise BlockingError("Operator report submitted after 31-Mar deadline (Art. 8(1))")
    
    return PASS
```

**Article Reference:** Article 8(1), Article 9(2)

---

### HC-02: Schema Validation (Article 8 CSV)

**Rule:** All mandatory columns present and correctly typed.

```python
# Required columns per 02-90-01-002A_Data_Model_Article8.csv
REQUIRED_COLUMNS = [
    'reporting_year',           # INT (YYYY)
    'operator_icao',            # STRING (3-4 chars)
    'operator_name',            # STRING
    'union_airport_icao',       # STRING (4 chars, ICAO format)
    'union_airport_iata',       # STRING (3 chars)
    'fuel_uplift_tonnes',       # FLOAT (≥0)
    'yearly_fuel_required_tonnes', # FLOAT (≥0)
    'yearly_non_tanked_tonnes', # FLOAT (≥0)
    'tanked_for_safety_tonnes', # FLOAT (≥0)
    'flights_count',            # INT (≥0)
    'flight_hours',             # FLOAT (≥0)
    # SAF fields (may be empty if no SAF used)
    'saf_purchase_id',          # STRING (unique if present)
    'saf_supplier_name',        # STRING
    'saf_tonnes',               # FLOAT (≥0)
    'saf_conversion_process',   # STRING (HEFA, FT, AtJ, etc.)
    'saf_feedstock',            # STRING
    'saf_origin_country',       # STRING (ISO 3166-1 alpha-2)
    'saf_life_cycle_emissions_gCO2e_MJ', # FLOAT (0-100)
    'batch_aromatics_volpct',   # FLOAT (0-100)
    'batch_naphthalenes_volpct',# FLOAT (0-100)
    'batch_sulphur_masspct',    # FLOAT (0-5)
    'notes_routes_impacted_article5_2', # STRING (empty or route list)
    'verification_body',        # STRING
    'verification_statement_uri' # STRING (valid URI)
]

def check_schema(csv_data):
    # Check all required columns present
    missing_cols = set(REQUIRED_COLUMNS) - set(csv_data.columns)
    if missing_cols:
        raise BlockingError(f"Missing required columns: {missing_cols}")
    
    # Type validation
    if not csv_data['reporting_year'].dtype == 'int':
        raise BlockingError("reporting_year must be integer")
    
    if not csv_data['fuel_uplift_tonnes'].dtype == 'float':
        raise BlockingError("fuel_uplift_tonnes must be float")
    
    # ... (full type checks)
    
    return PASS
```

**Article Reference:** Article 8(1), Annex II

---

### HC-03: Union Airport Validation

**Rule:** All airports must be valid Union airports per Regulation scope.

```python
# Union airports: EU Member States + EEA (Norway, Iceland, Liechtenstein) + Switzerland
UNION_AIRPORTS = load_icao_list()  # From official source

def check_union_airports(csv_data):
    for airport in csv_data['union_airport_icao'].unique():
        if airport not in UNION_AIRPORTS:
            raise BlockingError(f"Airport {airport} not a valid Union airport")
    
    return PASS
```

**Article Reference:** Article 1 (Scope), Article 2 (Definitions)

---

### HC-04: Non-Negative Fuel Values

**Rule:** All fuel quantities must be ≥ 0.

```python
def check_non_negative_fuel(csv_data):
    fuel_columns = [
        'fuel_uplift_tonnes',
        'yearly_fuel_required_tonnes',
        'yearly_non_tanked_tonnes',
        'tanked_for_safety_tonnes',
        'saf_tonnes'
    ]
    
    for col in fuel_columns:
        if (csv_data[col] < 0).any():
            raise BlockingError(f"{col} contains negative values")
    
    return PASS
```

**Article Reference:** Article 8(1) — Physical quantities cannot be negative

---

### HC-05: Safety Tanking Justification

**Rule:** If `tanked_for_safety_tonnes` > 0 or `yearly_non_tanked_tonnes` > 0, `notes_routes_impacted_article5_2` MUST be non-empty.

```python
def check_safety_tanking_justification(csv_data):
    for idx, row in csv_data.iterrows():
        if row['tanked_for_safety_tonnes'] > 0 or row['yearly_non_tanked_tonnes'] > 0:
            if pd.isna(row['notes_routes_impacted_article5_2']) or row['notes_routes_impacted_article5_2'].strip() == '':
                raise BlockingError(f"Row {idx}: Safety tanking without justification (Art. 5(2))")
    
    return PASS
```

**Article Reference:** Article 5(2) — Safety tanking must be justified

---

### HC-06: Verification Statement Present

**Rule:** `verification_statement_uri` must be valid URI and accessible.

```python
import validators

def check_verification_statement(csv_data):
    for idx, row in csv_data.iterrows():
        uri = row['verification_statement_uri']
        
        if pd.isna(uri) or uri.strip() == '':
            raise BlockingError(f"Row {idx}: Missing verification statement URI")
        
        if not validators.url(uri):
            raise BlockingError(f"Row {idx}: Invalid URI format: {uri}")
        
        # Optional: HTTP check for accessibility (may be slow)
        # response = requests.head(uri, timeout=5)
        # if response.status_code != 200:
        #     raise BlockingError(f"Row {idx}: Verification URI not accessible")
    
    return PASS
```

**Article Reference:** Article 8(2) — Verification requirement per EU ETS Articles 14-15

---

### HC-07: No Double-Claiming SAF

**Rule:** Each `saf_purchase_id` must be unique across all GHG schemes (ReFuelEU, EU ETS, CORSIA).

```python
# Requires cross-scheme registry (implementation TBD by authorities)
def check_no_double_claiming(csv_data, external_schemes_db):
    saf_ids = csv_data['saf_purchase_id'].dropna().unique()
    
    for saf_id in saf_ids:
        # Check if SAF ID used in EU ETS
        if external_schemes_db.check_ets(saf_id):
            raise BlockingError(f"SAF purchase {saf_id} already claimed in EU ETS (Art. 9(3))")
        
        # Check if SAF ID used in CORSIA
        if external_schemes_db.check_corsia(saf_id):
            raise BlockingError(f"SAF purchase {saf_id} already claimed in CORSIA (Art. 9(3))")
    
    return PASS
```

**Article Reference:** Article 9(3) — No double-claiming

**Implementation Note:** Full cross-scheme registry not yet operational; prepare data structure for future integration.

---

### HC-08: SAF Lifecycle Emissions Bounds

**Rule:** SAF lifecycle emissions must be within credible range (0-100 gCO₂e/MJ).

```python
def check_saf_lca_bounds(csv_data):
    saf_rows = csv_data[csv_data['saf_tonnes'] > 0]
    
    for idx, row in saf_rows.iterrows():
        lca = row['saf_life_cycle_emissions_gCO2e_MJ']
        
        if pd.isna(lca):
            raise BlockingError(f"Row {idx}: SAF used but lifecycle emissions missing")
        
        if lca < 0 or lca > 100:
            raise BlockingError(f"Row {idx}: SAF LCA {lca} outside credible range (0-100 gCO₂e/MJ)")
    
    return PASS
```

**Article Reference:** Article 9(2) — SAF characteristics must be provided

---

### HC-09: Fuel Balance Check

**Rule:** `fuel_uplift_tonnes` + `yearly_non_tanked_tonnes` should approximately equal `yearly_fuel_required_tonnes`.

```python
def check_fuel_balance(csv_data, tolerance=0.05):
    for idx, row in csv_data.iterrows():
        uplift = row['fuel_uplift_tonnes']
        non_tanked = row['yearly_non_tanked_tonnes']
        required = row['yearly_fuel_required_tonnes']
        
        total_accounted = uplift + non_tanked
        
        # Allow 5% tolerance for rounding/measurement errors
        if abs(total_accounted - required) / required > tolerance:
            raise BlockingError(f"Row {idx}: Fuel balance mismatch (uplift + non-tanked ≠ required)")
    
    return PASS
```

**Article Reference:** Article 5(1) — Refuelling obligation logic

---

### HC-10: 90% Refuelling Compliance (or Exemption)

**Rule:** `fuel_uplift_tonnes` / `yearly_fuel_required_tonnes` ≥ 0.90, unless exemption documented.

```python
def check_90_percent_rule(csv_data, exemptions_db):
    for idx, row in csv_data.iterrows():
        airport = row['union_airport_icao']
        uplift_pct = row['fuel_uplift_tonnes'] / row['yearly_fuel_required_tonnes']
        
        if uplift_pct < 0.90:
            # Check if exemption exists
            exemption = exemptions_db.get_exemption(airport, row['reporting_year'])
            
            if not exemption:
                raise BlockingError(f"Row {idx}: {airport} uplift {uplift_pct:.1%} < 90% without exemption (Art. 5(1))")
            
            # If exemption exists, validate compliance with exemption conditions
            if uplift_pct < exemption.minimum_required_pct:
                raise BlockingError(f"Row {idx}: {airport} uplift {uplift_pct:.1%} violates exemption condition (min {exemption.minimum_required_pct}%)")
    
    return PASS
```

**Article Reference:** Article 5(1), Article 5(3) — 90% refuelling rule and exemptions

**Integration:** Requires exemptions database from [02-90-01-003A](02-90-01-003A_Exemption_Workflow_Art5-3.md)

---

## 4. Soft Checks (Warnings)

These checks flag potential issues but do not block submission. Manual review recommended.

### SC-01: SAF Batch Quality Alignment

**Rule:** SAF batch quality parameters should align with supplier Article 10 disclosures.

```python
def check_saf_quality_alignment(csv_data, supplier_data_art10):
    for idx, row in csv_data[csv_data['saf_tonnes'] > 0].iterrows():
        purchase_id = row['saf_purchase_id']
        
        supplier_batch = supplier_data_art10.get_batch(purchase_id)
        
        if not supplier_batch:
            warn(f"Row {idx}: SAF batch {purchase_id} not found in supplier Article 10 data")
            continue
        
        # Check aromatics
        if abs(row['batch_aromatics_volpct'] - supplier_batch.aromatics) > 1.0:
            warn(f"Row {idx}: Aromatics mismatch (operator: {row['batch_aromatics_volpct']}% vs supplier: {supplier_batch.aromatics}%)")
        
        # Check lifecycle emissions
        if abs(row['saf_life_cycle_emissions_gCO2e_MJ'] - supplier_batch.lca) > 5.0:
            warn(f"Row {idx}: LCA mismatch (operator: {row['saf_life_cycle_emissions_gCO2e_MJ']} vs supplier: {supplier_batch.lca})")
    
    return PASS_WITH_WARNINGS
```

**Article Reference:** Article 10 — Supplier information; cross-validation

---

### SC-02: H₂ Lifecycle Emissions Reasonability

**Rule:** For AMPEL360, expect green H₂ (LCA ≤ 15 gCO₂e/MJ). Flag if higher.

```python
def check_h2_lca_reasonability(h2_supplier_data):
    for batch in h2_supplier_data:
        if batch.lca_gCO2e_MJ > 15:
            warn(f"H₂ batch {batch.id}: LCA {batch.lca_gCO2e_MJ} gCO₂e/MJ higher than green H₂ target (≤15). Verify production pathway.")
    
    return PASS_WITH_WARNINGS
```

**AMPEL360-Specific:** Hydrogen lifecycle emissions critical for FEL calculation.

---

### SC-03: Flight Operations Consistency

**Rule:** Flight counts and hours should be consistent with distance and block times.

```python
def check_flight_operations_consistency(csv_data, route_db):
    for idx, row in csv_data.iterrows():
        origin = row['union_airport_icao']
        # Assuming destination inferred from route network (or add destination column)
        
        expected_block_time_hrs = route_db.get_avg_block_time(origin)  # per flight
        
        if expected_block_time_hrs:
            expected_hours = row['flights_count'] * expected_block_time_hrs
            actual_hours = row['flight_hours']
            
            if abs(expected_hours - actual_hours) / expected_hours > 0.15:  # 15% tolerance
                warn(f"Row {idx}: Flight hours ({actual_hours}) inconsistent with flights count ({row['flights_count']}) and expected block time")
    
    return PASS_WITH_WARNINGS
```

**Purpose:** Detect data entry errors or unreported operational changes.

---

### SC-04: SAF Supplier Not on Sanctions List

**Rule:** Flag if SAF supplier or origin country on EU sanctions list.

```python
def check_supplier_sanctions(csv_data, sanctions_db):
    for idx, row in csv_data[csv_data['saf_tonnes'] > 0].iterrows():
        supplier = row['saf_supplier_name']
        country = row['saf_origin_country']
        
        if sanctions_db.is_sanctioned(supplier):
            warn(f"Row {idx}: SAF supplier {supplier} on sanctions list; verify legal compliance")
        
        if sanctions_db.is_sanctioned_country(country):
            warn(f"Row {idx}: SAF origin country {country} subject to sanctions; verify exemptions")
    
    return PASS_WITH_WARNINGS
```

**Purpose:** Compliance with EU foreign policy and trade restrictions.

---

### SC-05: Airport H₂ Readiness (Article 7 Cross-Check)

**Rule:** If AMPEL360 operating at airport, check Article 7 report shows H₂ infrastructure.

```python
def check_airport_h2_readiness(csv_data, article7_reports):
    ampel360_airports = csv_data['union_airport_icao'].unique()
    
    for airport in ampel360_airports:
        h2_report = article7_reports.get(airport)
        
        if not h2_report or h2_report.h2_capacity == 0:
            warn(f"Airport {airport}: No H₂ infrastructure reported in Article 7; verify AMPEL360 operations feasible")
    
    return PASS_WITH_WARNINGS
```

**Integration:** Cross-reference with [02-90-01-005A](02-90-01-005A_H2_Electricity_Report_Art7.md)

---

## 5. FEL-Specific Validations

### FEL-01: Dataset Schema

**Rule:** FEL input dataset must match template schema.

```python
FEL_REQUIRED_COLUMNS = [
    'season',
    'route_code',
    'origin_icao',
    'destination_icao',
    'aircraft_type',
    'avg_pax',
    'avg_cargo_kg',
    'fuel_h2_kg',
    'fuel_saf_kg',
    'saf_share_pct',
    'h2_lca_gCO2e_MJ',
    'saf_lca_gCO2e_MJ',
    'flights_count',
    'data_period_start',
    'data_period_end'
]

def check_fel_schema(fel_data):
    missing_cols = set(FEL_REQUIRED_COLUMNS) - set(fel_data.columns)
    if missing_cols:
        raise BlockingError(f"FEL dataset missing columns: {missing_cols}")
    
    return PASS
```

**Reference:** [02-90-01-006A](02-90-01-006A_FEL_Method_Art14.md)

---

### FEL-02: Load Factor Reasonability

**Rule:** Average passengers should be within 50-100% of aircraft capacity.

```python
def check_fel_load_factor(fel_data, aircraft_capacity=220):
    for idx, row in fel_data.iterrows():
        avg_pax = row['avg_pax']
        load_factor = avg_pax / aircraft_capacity
        
        if load_factor < 0.50 or load_factor > 1.00:
            warn(f"FEL Row {idx}: Load factor {load_factor:.1%} outside normal range (50-100%)")
    
    return PASS_WITH_WARNINGS
```

---

### FEL-03: Fuel Consumption Reasonability

**Rule:** H₂ fuel per flight should correlate with distance (physics check).

```python
def check_fel_fuel_consumption(fel_data):
    for idx, row in fel_data.iterrows():
        distance_km = calculate_distance(row['origin_icao'], row['destination_icao'])
        h2_per_flight = row['fuel_h2_kg'] / row['flights_count'] if row['flights_count'] > 0 else 0
        
        # AMPEL360 BWB expected: ~0.5-0.8 kg H₂ per km per flight (rough estimate)
        expected_h2_min = distance_km * 0.4
        expected_h2_max = distance_km * 1.0
        
        if h2_per_flight < expected_h2_min or h2_per_flight > expected_h2_max:
            warn(f"FEL Row {idx}: H₂ consumption {h2_per_flight} kg outside expected range ({expected_h2_min}-{expected_h2_max}) for {distance_km} km")
    
    return PASS_WITH_WARNINGS
```

---

## 6. CI/CD Pipeline Integration

### Pipeline Stages

```yaml
# .github/workflows/refueleu-validation.yml (example GitHub Actions)

name: ReFuelEU Compliance Validation

on:
  push:
    paths:
      - 'data/compliance/article8/**'
      - 'data/compliance/fel/**'
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install pandas validators requests pyyaml
      
      - name: Run Hard Checks (Article 8)
        run: |
          python scripts/validate_article8.py --mode hard --input data/compliance/article8/2024_data.csv
      
      - name: Run Soft Checks (Article 8)
        run: |
          python scripts/validate_article8.py --mode soft --input data/compliance/article8/2024_data.csv
        continue-on-error: true
      
      - name: Run FEL Validations
        run: |
          python scripts/validate_fel.py --input data/compliance/fel/2025_routes.csv
      
      - name: Generate Validation Report
        run: |
          python scripts/generate_validation_report.py --output reports/validation_$(date +%Y%m%d).html
      
      - name: Upload Report
        uses: actions/upload-artifact@v3
        with:
          name: validation-report
          path: reports/validation_*.html
```

### Pre-Commit Hooks

```bash
# .git/hooks/pre-commit

#!/bin/bash
# ReFuelEU data validation pre-commit hook

echo "Running ReFuelEU compliance validation..."

python scripts/validate_article8.py --mode hard --input data/compliance/article8/*.csv

if [ $? -ne 0 ]; then
    echo "❌ HARD CHECK FAILED: Fix blocking errors before committing"
    exit 1
fi

echo "✅ Validation passed"
exit 0
```

---

## 7. Validation Reporting

### Report Format (HTML/PDF)

```html
<!DOCTYPE html>
<html>
<head>
    <title>ReFuelEU Compliance Validation Report</title>
</head>
<body>
    <h1>AMPEL360 ReFuelEU Compliance Validation</h1>
    <p><strong>Report Date:</strong> 2025-03-15</p>
    <p><strong>Reporting Year:</strong> 2024</p>
    
    <h2>Summary</h2>
    <table>
        <tr><td>Hard Checks (Blocking)</td><td class="pass">✅ All Passed (10/10)</td></tr>
        <tr><td>Soft Checks (Warnings)</td><td class="warn">⚠️ 3 Warnings</td></tr>
        <tr><td>FEL Validations</td><td class="pass">✅ All Passed (3/3)</td></tr>
    </table>
    
    <h2>Warnings (Soft Checks)</h2>
    <ul>
        <li><strong>SC-01:</strong> Row 45: SAF batch aromatics mismatch (operator: 8.2% vs supplier: 8.5%)</li>
        <li><strong>SC-03:</strong> Row 12: Flight hours inconsistent with flights count by 12%</li>
        <li><strong>SC-05:</strong> Airport LEMD: No H₂ infrastructure in Article 7 report</li>
    </ul>
    
    <h2>Recommendations</h2>
    <ol>
        <li>Contact SAF supplier to reconcile aromatics data for batch SAF-2024-003</li>
        <li>Review flight hours data entry for LFPG operations</li>
        <li>Confirm LEMD operations plan if Article 7 shows no H₂ capacity</li>
    </ol>
</body>
</html>
```

### Dashboard Integration (ATA 95 CAOS)

**Real-Time Compliance Dashboard:**
- Green/Yellow/Red status per validation rule
- Trend analysis: compliance score over time
- Predictive alerts: "30 days until Article 8 deadline; 2 hard checks still failing"

---

## 8. Audit Trail & Logging

### Log Format

```json
{
  "timestamp": "2025-03-15T14:32:01Z",
  "validation_run_id": "VR-2025-03-15-001",
  "dataset": "article8_2024_data.csv",
  "validation_type": "hard_checks",
  "results": {
    "HC-01": {"status": "PASS", "message": "Deadlines compliant"},
    "HC-02": {"status": "PASS", "message": "Schema valid"},
    "HC-03": {"status": "PASS", "message": "All airports are Union airports"},
    "HC-10": {"status": "FAIL", "message": "Row 23: LEMD uplift 87% < 90% without exemption", "row": 23, "airport": "LEMD"}
  },
  "summary": {
    "total_checks": 10,
    "passed": 9,
    "failed": 1,
    "overall_status": "FAIL"
  },
  "operator": "compliance-pipeline-bot",
  "reviewed_by": null
}
```

### Retention Policy

- **Validation logs:** Retain 3 years (aligns with EU ETS verification retention)
- **Validation reports:** Archive with annual Article 8 submission
- **Audit access:** Available to verifiers, competent authorities, internal auditors

---

## 9. Related Documents

- **[02-90-01-000A_README.md](02-90-01-000A_README.md):** Overall compliance framework
- **[02-90-01-001A_Regulatory_Scope.md](02-90-01-001A_Regulatory_Scope.md):** Regulatory requirements underlying validation rules
- **[02-90-01-002A_Data_Model_Article8.csv](02-90-01-002A_Data_Model_Article8.csv):** Schema being validated
- **[02-90-01-003A to 006A]:** Specific article workflows and data sources

---

## 10. Continuous Improvement

### Rule Updates

**Triggers for updating validation rules:**
- Commission publishes implementing acts with new requirements
- EASA issues clarifications on data formats
- Verifier feedback identifies common errors
- AMPEL360 adds new fuel types or operational modes

**Change Process:**
1. Compliance team proposes rule update
2. Review by IV&V and Legal
3. Update this document (version control)
4. Update CI/CD scripts
5. Test on historical data
6. Deploy to production pipeline

---

## 11. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-12 | AMPEL360 Compliance & IT Teams | Initial CI validation rules document |

---

**End of CI Validation Rules Document**

For implementation code, see: `scripts/validate_article8.py`, `scripts/validate_fel.py` (AMPEL360 internal repository).
