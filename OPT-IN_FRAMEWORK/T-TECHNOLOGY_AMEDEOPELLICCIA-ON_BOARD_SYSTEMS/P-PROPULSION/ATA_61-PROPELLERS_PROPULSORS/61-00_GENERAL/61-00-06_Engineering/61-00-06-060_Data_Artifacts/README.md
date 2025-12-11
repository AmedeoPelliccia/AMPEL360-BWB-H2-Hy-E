# 61-00-06-060_Data_Artifacts

## Purpose

This folder contains **raw engineering data, CAD exports, test logs, and evidence artifacts** for ATA 61 Propellers/Propulsors, supporting traceability, reproducibility, and certification.

Data artifact management provides:
- Centralized storage of raw engineering data
- CAD geometry version control
- Test bench data integration
- Evidence packages for V&V and certification
- Metadata and provenance tracking

---

## Scope

Data artifact types include:

### CAD Geometry Exports
- Propeller blade geometry (STEP, IGES, STL)
- Motor housing and structural components
- Assembly models
- Design iterations and version history

### Test Bench Data
- Motor dyno test results
- Blade structural test data
- Wind tunnel measurements
- Thermal test logs

### Raw Simulation Outputs
- Large CFD/FEM result files (not post-processed)
- Convergence histories
- Solver logs and diagnostics
- Mesh files and quality metrics

### Experimental Evidence
- Photos and videos (test setups, failures)
- Sensor calibration records
- Instrumentation specifications
- Data acquisition system logs

### Miscellaneous Artifacts
- Supplier datasheets
- Material property databases
- Standards and reference documents
- Meeting notes and decision logs

---

## Typical Contents

- **CAD files** (`.stp`, `.igs`, `.stl`, `.x_t`)
- **Test data** (CSV, HDF5, binary formats)
- **Simulation raw outputs** (solver-specific formats)
- **Images and diagrams** (PNG, JPEG, SVG)
- **Metadata files** (`.json`, `.yaml` describing artifacts)
- **Provenance logs** (who, when, why, where)

---

## Workflow

### Adding New Data Artifacts:

1. **Identify artifact type and purpose**:
   - CAD geometry, test data, simulation output, etc.

2. **Organize by source and date**:
   - Create subdirectories: `CAD_Exports/`, `Test_Data/`, `Simulation_Raw/`, etc.
   - Use ISO date prefixes for time-series data: `YYYY-MM-DD_Descriptive_Name/`

3. **Create metadata file**:
   - Format: `artifact_name_metadata.json`
   - Include: source, date, purpose, tool/version, contact, related documents

4. **Document provenance**:
   - Who created/measured the data
   - When and where (lab, simulation, supplier)
   - What tool/instrument/method
   - Why (which analysis/study/test)

5. **Link to analysis and reports**:
   - Reference from `../61-00-06-010_Analysis/`, `../61-00-06-030_Simulation/`, etc.
   - Create V&V linkage entries if used for validation

6. **Version control (where feasible)**:
   - Git for text-based data (CSV, JSON, small files)
   - Git LFS for large binary files
   - External storage with links for very large datasets (>100 MB)

---

## Example Metadata File

**File: `Blade_Geometry_v3.2_metadata.json`**
```json
{
  "artifact_name": "Blade_Geometry_v3.2.stp",
  "artifact_type": "CAD_Export",
  "source": "Blade design team (CAD model v3.2)",
  "date_created": "2025-12-10",
  "tool": "CATIA V5 R21",
  "purpose": "CFD mesh generation for cruise performance study",
  "contact": "jane.doe@ampel360.aero",
  "related_documents": [
    "61-00-04-Design/61-00-04-003_Blade_Design.md",
    "61-00-06-020_Models/61-00-06-020-001_CFD_Propeller_Model.md"
  ],
  "file_size_MB": 15.3,
  "checksum_sha256": "a1b2c3d4e5f6...",
  "notes": "Updated blade twist distribution per trade study 61-00-06-040-001"
}
```

---

## Data Organization

Organize artifacts by type and project/campaign:

```
61-00-06-060_Data_Artifacts/
├── CAD_Exports/
│   ├── 2025-12-10_Blade_Geometry_v3.2/
│   │   ├── Blade_Geometry_v3.2.stp
│   │   └── Blade_Geometry_v3.2_metadata.json
│   └── ...
├── Test_Data/
│   ├── 2025-11-20_Motor_Dyno_Test/
│   │   ├── dyno_test_results.csv
│   │   ├── dyno_test_setup.jpg
│   │   └── dyno_test_metadata.json
│   └── ...
├── Simulation_Raw/
│   ├── 2025-12-05_CFD_Cruise_Campaign/
│   │   ├── R001_raw_output.tar.gz
│   │   └── campaign_metadata.json
│   └── ...
├── Experimental_Evidence/
│   ├── 2025-10-15_Blade_Static_Test/
│   │   ├── test_photos/
│   │   ├── load_displacement_data.csv
│   │   └── test_metadata.json
│   └── ...
└── Miscellaneous/
    ├── Supplier_Datasheets/
    ├── Material_Properties/
    └── Standards_References/
```

---

## File Naming Conventions

| Type | Convention | Example |
|:---|:---|:---|
| CAD export | `YYYY-MM-DD_Descriptive_Name_vX.Y.ext` | `2025-12-10_Blade_Geometry_v3.2.stp` |
| Test data | `YYYY-MM-DD_Test_Name/` | `2025-11-20_Motor_Dyno_Test/` |
| Metadata | `artifact_name_metadata.json` | `Blade_Geometry_v3.2_metadata.json` |
| Raw sim output | `RXXX_raw_output.tar.gz` | `R001_raw_output.tar.gz` |

---

## Data Size Management

For very large datasets (>100 MB per file):

- **Option 1**: Use Git LFS (Large File Storage)
- **Option 2**: Store externally (shared drive, cloud) with link in metadata
- **Option 3**: Archive to tape/cold storage with provenance record

Always include:
- File size in metadata
- Checksum (SHA256) for integrity verification
- Retention policy (how long to keep)

---

## Standards and References

- **ISO 15489** — Records management
- **FAIR Principles** — Findable, Accessible, Interoperable, Reusable data
- **Model-Based Systems Engineering (MBSE)** — Artifact traceability
- **DO-178C / DO-254** — Evidence retention for certification

---

## Status

- **Lifecycle Stage**: 06 — Engineering
- **Subfolder**: 060 — Data Artifacts
- **Content Status**: Scaffolded (ready for data artifact storage)
- **Last Updated**: 2025-12-11

---

## Related Folders

- **[../61-00-06-010_Analysis/](../61-00-06-010_Analysis/)** — Analyses using these artifacts
- **[../61-00-06-020_Models/](../61-00-06-020_Models/)** — Models built from CAD/geometry
- **[../61-00-06-030_Simulation/](../61-00-06-030_Simulation/)** — Simulations producing raw outputs
- **[../61-00-06-070_V_AND_V_Linkage/](../61-00-06-070_V_AND_V_Linkage/)** — Validation using test/experimental data
- **[../../61-00-10_Certification/](../../61-00-10_Certification/)** — Evidence packages for certification

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (Enhanced Engineering Template)
- **Owner**: AMPEL360 Engineering WG (Data Management Team)
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

*Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.*
