# File Naming Conventions for 53-00-04 Design Exports

**Document ID:** 53-00-04-EXPT-STD-FN  
**Version:** 1.0  
**Date:** 2025-11-22

---

## 1. General Pattern

All export files follow this naming pattern:

```
<ATA>-<SECTION>-<SUBSYSTEM>[-<TYPE>-<ID>][_RevX]_<Description>.<ext>
```

### Components:

- `<ATA>`: ATA chapter (53 for Fuselage)
- `<SECTION>`: Section number (00, 10, 20, etc.)
- `<SUBSYSTEM>`: Subsystem number (00, 01, 02, etc.)
- `<TYPE>`: Export type code (optional)
- `<ID>`: Sequential identifier (001, 002, etc.)
- `_RevX`: Revision identifier (RevA, RevB, RevC, etc.)
- `<Description>`: Brief descriptive name
- `<ext>`: File extension

## 2. Export Type Codes

| Code | Type | Example |
|------|------|---------|
| EXPT | Export | 53-00-04-EXPT-001_STEP_Export_Log.csv |
| CERT | Certification | 53-00-04-CERT-001_Stress_Reports.zip |
| MFG | Manufacturing | 53-20-2000_RevB_MFG_Ply_Book.pdf |
| SPLR | Supplier | 53-00-04-SPLR-A-001_Technical_Data.zip |
| ANLS | Analysis | 53-00-04-ANLS-001_Global_Model_RevD.bdf |
| REV | Review | 53-00-04-REV-PDR-001_Drawing_Package.pdf |
| CUST | Customer | 53-00-04-CUST-001_Maintenance_Manual.pdf |
| DTW | Digital Twin | 53-00-04-DTW-001_Full_Assembly.gltf |
| BL | Baseline | 53-00-04-BL-001_PDR_Baseline.json |
| CM | Configuration | 53-00-04-CM-001_Export_History.csv |
| DPP | Digital Product Passport | 53-00-04-DPP-001_Material_Composition.json |
| SEC | Security | 53-00-04-SEC-001_Export_Control_Matrix.csv |

## 3. Revision Identifiers

- `RevA`: Initial release
- `RevB`, `RevC`, etc.: Subsequent revisions
- `Rev-`: Dash indicates preliminary/draft (e.g., Rev-A)
- Format: Always `_Rev<Letter>` with underscore prefix

## 4. Examples

### CAD Exports
```
53-10-1000_RevC_Forward_Bulkhead_Assembly.step
53-10-2000_RevB_NLG_Bay_Structure.iges
53-10-9000_RevC_Zone_100_Complete_Assembly.jt
```

### Manufacturing Data
```
53-20-2000_RevB_MFG_Ply_Book.pdf
53-40-1004_RevA_MFG_CNC_Program.nc
53-00-04-MFG-WP-001_Forward_Bulkhead.zip
```

### Analysis Models
```
53-00-04-ANLS-001_Global_Model_RevD.bdf
53-00-04-ANLS-002_Spar_Detail_RevC.bdf
```

### Export Logs
```
53-00-04-EXPT-001_STEP_Export_Log.csv
53-00-04-EXPT-002_IGES_Export_Log.csv
```

## 5. Special Cases

### Serial-Number-Specific Files
```
53-00-04-DTW-SN0001-001_Tail_Number_001_Deltas.json
```
Format: `DTW-SN<4-digit-SN>-<ID>`

### Date-Stamped Files (Reviews)
```
53-00-04-REV-WDR-2025-11-22_Review_Package.zip
```
Format: `REV-WDR-YYYY-MM-DD`

### Baseline Manifests
```
53-00-04-BL-001_PDR_Baseline_2025-06-15.json
```
Format: `BL-<ID>_<Name>_YYYY-MM-DD`

## 6. Prohibited Characters

Do NOT use in filenames:
- Spaces (use underscores)
- Special characters: `/ \ : * ? " < > |`
- Unicode characters
- Leading/trailing dots or spaces

## 7. Case Sensitivity

- Use PascalCase or Snake_Case for descriptions
- Type codes are UPPERCASE
- Revision identifiers use capital letters (RevA, RevB)
- File extensions are lowercase

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.

---
