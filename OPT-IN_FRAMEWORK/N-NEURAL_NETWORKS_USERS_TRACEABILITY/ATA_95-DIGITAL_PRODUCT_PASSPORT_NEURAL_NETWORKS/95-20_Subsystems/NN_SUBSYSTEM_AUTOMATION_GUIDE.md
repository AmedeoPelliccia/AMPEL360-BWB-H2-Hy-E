# Neural Network Subsystem Automation Guide

## Overview

This guide documents the automation tools for creating and validating OPT-IN Framework compliant Neural Network subsystems in the AMPEL360 project.

## Available Tools

### 1. Subsystem Generator (`generate_nn_subsystem.py`)

**Location**: `tools/scripts/generate_nn_subsystem.py`

**Purpose**: Automatically generates a complete OPT-IN Framework compliant subsystem structure with all mandatory folders, documents, and templates.

**Usage**:
```bash
python3 tools/scripts/generate_nn_subsystem.py <subsystem_num> <name> <ata_chapter> <ata_name>
```

**Parameters**:
- `subsystem_num`: Two-digit subsystem number (e.g., "27" for 95-20-27)
- `name`: Subsystem name without spaces (e.g., "Flight_Controls")
- `ata_chapter`: Parent ATA chapter number (e.g., "27")
- `ata_name`: Full ATA chapter name in quotes (e.g., "Flight Controls")

**Examples**:

Generate Flight Controls subsystem:
```bash
python3 tools/scripts/generate_nn_subsystem.py 27 Flight_Controls 27 "Flight Controls"
```

Generate Fuel System subsystem:
```bash
python3 tools/scripts/generate_nn_subsystem.py 28 Fuel_System 28 "Fuel (SAF & Cryogenic H2)"
```

Generate Avionics subsystem:
```bash
python3 tools/scripts/generate_nn_subsystem.py 31 Recording_Systems 31 "Recording Systems"
```

**What it Creates**:

1. **Root Documents** (95-20-XX-001 through 95-20-XX-010):
   - Overview document with system description
   - Component specification documents
   - Integration document
   - Safety and certification document
   - Operational procedures document

2. **META Folder** (00_META/):
   - Taxonomy document
   - Traceability matrix (CSV)
   - Assets registry (JSON)
   - CAOS integration hooks

3. **ASSETS Folder**:
   - `Architecture/`: Diagram placeholders
   - `Model_Cards/`: Model card templates
   - `Performance_Data/`: Performance metric placeholders
   - `Test_Data/`: Test result placeholders
   - `Interface_Specs/`: Interface specification templates
   - `Certification/`: Certification document placeholders

4. **Models Folder**:
   - `Source/`: Python source code templates
   - `Trained/`: ONNX model placeholders
   - `Configs/`: YAML configuration templates

5. **Data Folder**:
   - `Training_Datasets/`: Training data placeholders
   - `Validation_Datasets/`: Validation data placeholders
   - `Synthetic_Data/`: Synthetic data placeholders

6. **Tests Folder**:
   - `Unit_Tests/`: Unit test templates
   - `Integration_Tests/`: Integration test templates
   - `HIL_Tests/`: Hardware-in-loop test scenarios

7. **Documentation Folder**:
   - Operations manual placeholder
   - Maintenance procedures placeholder
   - Troubleshooting guide placeholder
   - Training materials folder

### 2. Subsystem Validator (`validate_nn_subsystem.py`)

**Location**: `.github/scripts/validate_nn_subsystem.py`

**Purpose**: Validates that a subsystem structure complies with OPT-IN Framework requirements.

**Usage**:
```bash
python3 .github/scripts/validate_nn_subsystem.py <subsystem_path>
```

**Parameters**:
- `subsystem_path`: Path to subsystem directory (e.g., `OPT-IN_FRAMEWORK/.../95-20-21_NN_ECS`)

**Examples**:

Validate ECS subsystem:
```bash
python3 .github/scripts/validate_nn_subsystem.py \
    OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/95-20_Subsystems/95-20-21_NN_ECS
```

**What it Validates**:

1. **Folder Structure**:
   - ✓ All 18 mandatory folders present
   - ✓ Correct folder hierarchy

2. **Mandatory Documents**:
   - ✓ Overview document (95-20-XX-001)
   - ✓ Integration document (95-20-XX-008)
   - ✓ Safety document (95-20-XX-009)
   - ✓ Operations document (95-20-XX-010)

3. **Naming Conventions**:
   - ✓ Root documents: `95-20-XX-YYY_*`
   - ✓ META documents: `95-20-XX-0YY_*`
   - ✓ ASSET files: `95-20-XX-A-YYY_*`
   - ✓ README.md allowed

4. **Model Cards**:
   - ✓ Proper YAML structure
   - ✓ Required fields present (for non-template cards)
   - ✓ Valid model metadata

5. **Traceability**:
   - ✓ Traceability CSV exists
   - ✓ Required columns present (Requirement, Design, Interface, Engineering, Verification)

**Output**:

Success:
```
================================================================================
Validating Neural Network Subsystem: 95-20-21_NN_ECS
================================================================================

✅ Subsystem structure is valid!
   - All mandatory folders present
   - All mandatory documents present
   - Naming conventions compliant
   - Model cards complete
   - Traceability matrix present
```

Failure:
```
================================================================================
Validating Neural Network Subsystem: 95-20-XX_NN_Invalid
================================================================================

❌ Validation failed with 3 errors:

   - Missing mandatory folder: ASSETS/Model_Cards
   - Missing mandatory document matching pattern: 95-20-XX-009_Safety_and_Certification.md
   - Incorrect naming: Invalid_Document.md
```

## Complete Workflow

### Creating a New Subsystem

**Step 1**: Generate the structure
```bash
cd /path/to/AMPEL360-BWB-H2-Hy-E
python3 tools/scripts/generate_nn_subsystem.py 35 Navigation_Systems 35 "Navigation"
```

**Step 2**: Validate the generated structure
```bash
python3 .github/scripts/validate_nn_subsystem.py \
    OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/95-20_Subsystems/95-20-35_NN_Navigation_Systems
```

**Step 3**: Customize the content
- Update `95-20-35-001_*_Overview.md` with actual system description
- Add component documentation (002-007)
- Update integration document (008)
- Fill in model cards with actual model information
- Update traceability matrix
- Add source code and test files

**Step 4**: Re-validate
```bash
python3 .github/scripts/validate_nn_subsystem.py \
    OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/95-20_Subsystems/95-20-35_NN_Navigation_Systems
```

### Validating an Existing Subsystem

```bash
python3 .github/scripts/validate_nn_subsystem.py \
    OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/95-20_Subsystems/95-20-21_NN_ECS
```

## File Naming Conventions

### Root Documents
- Pattern: `95-20-{subsystem}-{sequence}_{Description}.md`
- Range: 001-010 (core documents), 011-020 (META)
- Example: `95-20-21-001_ECS_NN_Overview.md`

### ASSET Files
- Pattern: `95-20-{subsystem}-A-{sequence}_{Description}.{ext}`
- Ranges:
  - 001-099: Architecture diagrams
  - 101-199: Model cards
  - 201-299: Performance data
  - 301-399: Test data
  - 401-499: Interface specs
  - 501-599: Certification docs
- Example: `95-20-21-A-101_Temp_Predictor_v1.2.yaml`

### Data Files
- Pattern: `95-20-{subsystem}-{sequence}_{Description}.{ext}`
- Range: 601-699
- Example: `95-20-21-601_Cabin_Temp_10k_Flights.parquet`

### Test Files
- Pattern: `95-20-{subsystem}-{sequence}_{Description}.yaml`
- Range: 701-799
- Example: `95-20-21-701_HIL_Test_Scenarios.yaml`

### Documentation Files
- Pattern: `95-20-{subsystem}-{sequence}_{Description}.md`
- Range: 801-899
- Example: `95-20-21-801_Operations_Manual.md`

## Subsystem Checklist

Use this checklist when creating or updating a subsystem:

### Structure
- [ ] All 18 mandatory folders created
- [ ] Folder hierarchy matches template
- [ ] README.md present in root

### Core Documentation
- [ ] 001: Overview document with system description
- [ ] 002-007: Component specifications
- [ ] 008: Integration with parent ATA
- [ ] 009: Safety and certification
- [ ] 010: Operational procedures

### META
- [ ] 011: Taxonomy document
- [ ] 012: Traceability CSV with all required columns
- [ ] 013: Assets registry JSON
- [ ] 014: CAOS integration hooks

### ASSETS
- [ ] Architecture diagrams (drawio + SVG)
- [ ] Model cards for all models (YAML)
- [ ] Performance data files
- [ ] Test result files
- [ ] Interface specifications (YAML)
- [ ] Certification documents (PDF)

### Models
- [ ] Source code for each model (Python)
- [ ] Trained models (ONNX format)
- [ ] Training configs (YAML)
- [ ] Deployment config (YAML)

### Data
- [ ] Training datasets documented
- [ ] Validation datasets documented
- [ ] Synthetic data (if applicable)

### Tests
- [ ] Unit tests for each model
- [ ] Integration tests for interfaces
- [ ] HIL test scenarios (YAML)

### Documentation
- [ ] Operations manual
- [ ] Maintenance procedures
- [ ] Troubleshooting guide
- [ ] Training materials

### Traceability
- [ ] All requirements linked to design
- [ ] All design elements linked to interfaces
- [ ] All interfaces linked to engineering artifacts
- [ ] All artifacts linked to verification
- [ ] Links to parent ATA chapter

### Naming Compliance
- [ ] All files follow naming conventions
- [ ] No naming conflicts or duplicates
- [ ] Sequence numbers properly allocated

## Integration with CI/CD

### GitHub Actions

Add to `.github/workflows/validate-subsystems.yml`:

```yaml
name: Validate NN Subsystems

on:
  push:
    paths:
      - 'OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/95-20_Subsystems/**'
  pull_request:
    paths:
      - 'OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/95-20_Subsystems/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          pip install pyyaml
      
      - name: Validate all subsystems
        run: |
          for subsystem in OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/95-20_Subsystems/95-20-*/; do
            echo "Validating: $subsystem"
            python3 .github/scripts/validate_nn_subsystem.py "$subsystem"
          done
```

## Troubleshooting

### Common Issues

**Issue**: "Missing mandatory folder"
- **Solution**: Run generator script to create missing folders, or create manually

**Issue**: "Incorrect naming"
- **Solution**: Rename file to match pattern `95-20-XX-YYY_*`

**Issue**: "Missing mandatory document"
- **Solution**: Create document with proper naming convention

**Issue**: "Model card parse error"
- **Solution**: Check YAML syntax in model card file

**Issue**: "Missing traceability column"
- **Solution**: Add missing column to CSV (Requirement, Design, Interface, Engineering, Verification)

## Best Practices

1. **Always validate after generation**: Run validator immediately after generating a new subsystem

2. **Use version control**: Commit each logical change to the subsystem structure

3. **Document as you build**: Don't wait until the end to fill in documentation

4. **Follow naming strictly**: The naming convention enables automatic discovery and tooling

5. **Keep traceability updated**: Update traceability matrix as you add components

6. **Use placeholders wisely**: Generator creates placeholders; replace them with actual content

7. **Test incrementally**: Don't wait until completion to test the subsystem

8. **Review regularly**: Periodically validate to catch issues early

## Reference Implementation

The **95-20-21_NN_ECS** subsystem serves as the reference implementation:

Location: `OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/95-20_Subsystems/95-20-21_NN_ECS`

Contents:
- ✅ Complete documentation (001-010)
- ✅ Full META structure (011-014)
- ✅ All ASSET categories with examples
- ✅ Model cards with complete structure
- ✅ Source code templates
- ✅ Test file templates
- ✅ Traceability matrix
- ✅ Passes all validation checks

Use this as a template when creating new subsystems.

## Support

For questions or issues:
- Review the reference implementation (95-20-21_NN_ECS)
- Check validation error messages
- Consult OPT-IN Framework documentation
- Raise an issue in the GitHub repository

## Version History

- **v1.0** (2025-11-17): Initial automation tools release
  - Generator script
  - Validator script
  - Reference implementation (95-20-21_NN_ECS)

---

**Document Control**
- **Version**: 1.0
- **Status**: WORKING
- **Last Updated**: 2025-11-17
- **Maintainer**: AMPEL360 Integration Team
