# AMPEL360 Q100 Validators

Python validation utilities for ensuring compliance with Q100 standards and the OPT-IN Framework.

## Overview

This package provides three main validators:

1. **DrawingValidator**: Validates Q100 drawing filename format
2. **CIValidator**: Validates Configuration Item numbers and codes
3. **StructureValidator**: Validates OPT-IN Framework directory structure

## Installation

From the repository root:

```bash
pip install -e tools/validators
```

Or install just the requirements:

```bash
pip install -r requirements.txt
```

## Quick Start

### Drawing Filename Validation

```python
from tools.validators import validate_q100_drawing_filename

# Simple validation (raises ValueError if invalid)
validate_q100_drawing_filename("57-40-1000_RevC_Q100_ALL_ALL_Forward_Wing_Spar.svg")
```

```python
from tools.validators import DrawingValidator

# Detailed validation with error messages
validator = DrawingValidator()
is_valid, error, components = validator.validate(
    "57-40-1000_RevC_Q100_ALL_ALL_Forward_Wing_Spar.svg"
)

if is_valid:
    print(f"Valid drawing! ATA: {components.ata}, Zone: {components.zone}")
else:
    print(f"Invalid: {error}")
```

**Expected Format**: `[ATA]-[ZONE]-[SEQUENCE]-[VAR]_Rev[X]_[MODEL]_[EFF]_[APP]_Description.svg`

**Example**: `57-40-1000_RevC_Q100_ALL_ALL_Forward_Wing_Spar_Assembly.svg`

### CI Number Validation

```python
from tools.validators import validate_ci_number

# Simple validation
validate_ci_number("CI-57-400-SPAR-FWD")
```

```python
from tools.validators import CIValidator

# Detailed validation
validator = CIValidator()
is_valid, error, components = validator.validate("CI-57-400-SPAR-FWD")

# Validate effectivity and applicability codes
valid, error = validator.validate_effectivity("SN0100UP")
valid, error = validator.validate_applicability("PAX")
```

**Expected Format**: `CI-[ATA]-[ZONE]-[TYPE]-[ID]`

**Example**: `CI-57-400-SPAR-FWD`

### Directory Structure Validation

```python
from tools.validators import validate_directory_structure

# Simple validation
is_valid = validate_directory_structure("/path/to/repo")
```

```python
from tools.validators import StructureValidator
from pathlib import Path

# Detailed validation
validator = StructureValidator(Path("/path/to/repo"))

# Validate all ATA chapters
results = validator.validate_all_ata_chapters()

# Generate report
report = validator.generate_report(results)
print(report)

# Check for forbidden file extensions
forbidden = validator.check_file_extensions(validator.opt_in_root)
```

## Command-Line Usage

All validators can be run from the command line:

### Drawing Validator

```bash
python tools/validators/drawing_validator.py 57-40-1000_RevC_Q100_ALL_ALL_Spar.svg

# Multiple files
python tools/validators/drawing_validator.py file1.svg file2.svg file3.svg
```

### CI Validator

```bash
python tools/validators/ci_validator.py CI-57-400-SPAR-FWD

# Multiple CI numbers
python tools/validators/ci_validator.py CI-57-400-SPAR-FWD CI-53-200-DOOR-1L
```

### Structure Validator

```bash
# Validate from repository root
python tools/validators/structure_validator.py .

# Validate specific directory
python tools/validators/structure_validator.py /path/to/repo
```

## Validation Rules

### Drawing Filenames

#### Valid Components

- **ATA**: 2-digit ATA chapter (00-99)
- **ZONE**: 2-digit zone (00-99)
- **SEQUENCE**: 4-digit sequence (0000-9999)
- **VARIANT**: Optional sub-drawing (01, 02, A, B)
- **REVISION**: Draft, A-Z, AA-ZZ
- **MODEL**: Q100 (required)
- **EFFECTIVITY**: ALL, SN0001-0003, SN0100UP, SN0100UP-EXC0105, BLK-A
- **APPLICABILITY**: ALL, PAX, CGO, TEST, CERT
- **DESCRIPTION**: Human-readable name (snake_case)
- **EXTENSION**: .svg, .step, .iges, .jt

#### Examples

✅ **Valid**:
```
57-40-1000_RevC_Q100_ALL_ALL_Forward_Wing_Spar_Assembly.svg
53-20-4000-01_RevB_Q100_SN0100UP_PAX_Passenger_Door_1L.step
85-60-0001_RevDraft_Q100_ALL_ALL_H2_Storage_Infrastructure.svg
```

❌ **Invalid**:
```
57-40-1000_Forward_Wing_Spar.svg                    # Missing Rev, Model, EFF, APP
57-40-1000_v3_Q100_ALL_ALL_Spar.svg                # Wrong revision format
57-40-1000_RevC_Q200_ALL_ALL_Spar.svg              # Wrong model (Q200, not Q100)
57-40-1000_RevC_Q100_INVALID_ALL_Spar.svg          # Invalid effectivity code
```

### CI Numbers

#### Valid Components

- **PREFIX**: CI- (required)
- **ATA**: 2-3 digit ATA chapter (00-100)
- **ZONE**: 2-3 digit zone
- **TYPE**: Uppercase alphanumeric with underscores (SPAR, DOOR, TANK, etc.)
- **ID**: Uppercase alphanumeric with underscores (FWD, AFT, 1L, 2R, etc.)

#### Examples

✅ **Valid**:
```
CI-57-400-SPAR-FWD
CI-53-200-DOOR-1L
CI-28-600-TANK-LH2-LEFT
CI-85-60-H2_STORAGE-GND
```

❌ **Invalid**:
```
CI-53-SPAR-FWD                  # Missing zone
53-400-SPAR-FWD                 # Missing CI- prefix
CI-53-400-spar-fwd              # Lowercase not allowed
CI-999-400-SPAR-FWD             # Invalid ATA chapter
```

### Directory Structure

#### Required Lifecycle Folders (XX-00_GENERAL)

All ATA chapters should have:

1. `01_Overview`
2. `02_Safety`
3. `03_Requirements`
4. `04_Design`
5. `05_Interfaces`
6. `06_Engineering`
7. `07_V_AND_V`
8. `08_Prototyping`
9. `09_Production_Planning`
10. `10_Certification`
11. `11_EIS_Versions_Tags`
12. `12_Services`
13. `13_Subsystems_Components`
14. `14_Ops_Std_Sustain`

#### Required Cross-ATA Buckets

All ATA chapters should have:

1. `10_Operations`
2. `20_Subsystems`
3. `30_Circularity`
4. `40_Software`
5. `50_Structures`
6. `60_Storages`
7. `70_Propulsion`
8. `80_Energy`
9. `90_Tables_Schemas_Diagrams`

#### Forbidden File Extensions

- `.pdf` (use `.md` instead)
- `.xlsx`, `.xls` (use `.csv` instead)
- `.docx`, `.doc` (use `.md` instead)
- `.pptx` (use `.md` + `.svg` instead)

**Exceptions**: External vendor documents, scanned legacy documents, final certification submissions.

## Integration with CI/CD

The validators are integrated into GitHub Actions workflows:

### Q100 Validation Workflow

`.github/workflows/q100-validation.yml` runs on every PR:

- Structure validation
- File format checks
- Drawing filename validation
- Security scanning

### Pre-commit Hooks

Install Git hooks for local validation:

```bash
bash .github/hooks/setup-hooks.sh
```

This validates:
- Q100 model codes in drawings
- Forbidden file extensions
- Safety-critical code compliance

## Batch Validation

### Drawing Filenames

```python
from tools.validators import batch_validate_drawings

filenames = [
    "57-40-1000_RevC_Q100_ALL_ALL_Spar.svg",
    "57-40-1001_RevB_Q100_ALL_ALL_Cap.svg",
    "invalid-filename.svg"
]

results = batch_validate_drawings(filenames)

for filename, (is_valid, error) in results.items():
    if not is_valid:
        print(f"{filename}: {error}")
```

### CI Numbers

```python
from tools.validators import batch_validate_cis

ci_numbers = [
    "CI-57-400-SPAR-FWD",
    "CI-57-400-SPAR-AFT",
    "INVALID-CI"
]

results = batch_validate_cis(ci_numbers)

for ci_number, (is_valid, error) in results.items():
    if not is_valid:
        print(f"{ci_number}: {error}")
```

## Development

### Running Tests

```bash
# Install development dependencies
pip install pytest pytest-cov

# Run tests
pytest tools/validators/

# With coverage
pytest --cov=tools/validators tools/validators/
```

### Adding New Validators

1. Create new validator module in `tools/validators/`
2. Follow the pattern: class-based validator with convenience function
3. Add command-line interface in `__main__` block
4. Update `__init__.py` to export new validator
5. Add tests
6. Update this README

### Code Style

- Follow PEP 8
- Use type hints
- Include docstrings with examples
- Log validation results
- Provide helpful error messages

## Troubleshooting

### Import Errors

If you get import errors, ensure the validators package is installed:

```bash
pip install -e tools/validators
```

Or add the repo root to PYTHONPATH:

```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/repo"
```

### Validation Failures

Check the error messages for specific guidance. Common issues:

- **Drawing filenames**: Ensure Q100 model code is present
- **CI numbers**: Verify ATA chapter is valid
- **Directory structure**: Check folder naming conventions

### Performance

For large repositories, structure validation can be slow. Use:

```python
# Validate specific ATA chapter only
validator = StructureValidator(Path("/path/to/repo"))
results = validator.validate_ata_chapter(
    Path("/path/to/repo/OPT-IN_FRAMEWORK/.../ATA_53-FUSELAGE")
)
```

## Contributing

1. Write tests for new validators
2. Follow existing code patterns
3. Update documentation
4. Run all validators on test data
5. Submit PR with clear description

## License

See repository LICENSE file.

---

**Version**: 1.0.0  
**Last Updated**: 2025-11-23  
**Maintained By**: AMPEL360 Q100 Documentation Team
