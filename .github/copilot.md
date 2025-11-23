# GitHub Copilot Instructions for AMPEL360 Q100 BWB H2-Electric Aircraft

## Project Overview

**AMPEL360 Q100** is a revolutionary 100-passenger Blended Wing Body (BWB) hydrogen-electric aircraft designed to **decentralize air travel** and **reduce tourism massification** by enabling direct connections between secondary airports and smaller cities.

### Strategic Mission

```yaml
core_mission: "Sustainable Regional Connectivity"

strategic_objectives:
  decongest_major_hubs:
    - "Enable point-to-point routes bypassing overcrowded hubs"
    - "Reduce environmental footprint at mega-airports"
    - "Distribute air traffic to underutilized regional airports"
    
  prevent_tourism_massification:
    - "Reduce overtourism in Barcelona, Venice, Amsterdam, Prague"
    - "Distribute tourism to secondary cities with capacity"
    - "Protect cultural heritage from tourist overcrowding"
    - "Enable sustainable tourism growth in emerging destinations"
    
  combat_gentrification:
    - "Reduce housing pressure in major tourist hotspots"
    - "Enable economic development in smaller cities"
    - "Preserve local communities and affordability"
    - "Support regional job creation outside mega-cities"
    
  regional_economic_development:
    - "Bring international connectivity to cities 100K-500K population"
    - "Enable business travel without hub transfers"
    - "Support local entrepreneurship and investment"
    - "Bridge digital divide with physical connectivity"

example_routes:
  decentralization:
    - "Bilbao → Lyon (bypass Madrid-Paris hubs)"
    - "Porto → Bologna (bypass Lisbon-Milan hubs)"
    - "Gdansk → Toulouse (direct, no hub connection)"
    
  overtourism_relief:
    instead_of: "Everyone flies to Barcelona"
    distribute_to: ["Girona", "Tarragona", "Zaragoza"]
    benefit: "Spread economic benefits, preserve Barcelona quality"
```

---

## Q100 Model Specification

### Single Baseline Model

```yaml
model_identity:
  model_code: "Q100"
  full_name: "AMPEL360 Q100 Standard"
  designation: "Q = Quantum, 100 = 100 passengers"
  
specifications:
  configuration: "Blended Wing Body (BWB)"
  capacity: "100 passengers (single-class) / 90 passengers (dual-class)"
  range: "3,500 km (1,890 nm)"
  market_category: "Short-Haul"
  cruise_speed: "Mach 0.78"
  
dimensions:
  length: "42.0 m"
  wingspan: "55.0 m"
  cabin_width_max: "22.0 m"
  
weights:
  mtow: "65,000 kg"
  oew: "35,000 kg"
  max_payload: "17,000 kg"
  
fuel:
  type: "Liquid Hydrogen (LH2)"
  capacity: "3,000 kg LH2"
  backup: "500 L SAF"
  
propulsion:
  architecture: "Distributed Electric Propulsion"
  power: "16 MW (4× 4 MW ducted fans)"
  fuel_cells: "20 MW PEM stacks"
  batteries: "5 MWh lithium-ion"
  
structure:
  fuselage_mass: "15,000 kg"
  primary_material: "CFRP (65%)"
  
certification:
  basis: "EASA CS-25 / FAA Part 25"
  special_conditions: "BWB, H2 fuel, distributed propulsion"
  eis_target: "2029-Q2"
```

---

## OPT-IN Framework Architecture

```yaml
framework: "OPT-IN Framework v1.1"
structure:
  O: "Organization (ATA 00-05)"
  P: "Program (ATA 06-12)"
  T: "Technology - On-board Systems (ATA 20-100)"
  I: "Infrastructures (ATA 85-90, 115-116)"
  N: "Neural Networks / DPP / Traceability (ATA 95-100)"

primary_atas:
  ATA_53: "Fuselage (BWB-specific structure)"
  ATA_28: "Fuel System (H2)"
  ATA_85: "Infrastructure Interface Standards (H2 ground support)"
  ATA_95: "Digital Product Passport & Neural Networks"
  ATA_99: "Carbon Accounting & Circularity"
```

---

## File Format Standards (CRITICAL)

### ✅ ALLOWED Formats

```yaml
documents: ".md (Markdown)"
data: ".csv (Comma-separated values)"
drawings: ".svg (Scalable Vector Graphics)"
configs: ".yaml, .json"
code: ".py, .js, .sh"
cad_exports: ".step, .iges, .jt"
```

### ❌ FORBIDDEN Formats

```yaml
never_use:
  - ".pdf (not version-control friendly)"
  - ".xlsx, .xls (use .csv instead)"
  - ".docx, .doc (use .md instead)"
  - ".pptx (use .md + .svg instead)"

exceptions:
  - "External vendor documents (preserve as received)"
  - "Scanned legacy documents (archive only)"
  - "Certification submission (final PDF/A format only)"
```

**Rationale**: Version control, Git diffability, automation, CI/CD compatibility.

---

## Drawing Numbering Convention

### Complete Format

```
[ATA]-[ZONE]-[SEQUENCE]-[VAR]_Rev[X]_[MODEL]_[EFF]_[APP]_Description.svg

Where:
  ATA       = 2-digit ATA chapter (53, 85, etc.)
  ZONE      = 2-digit zone (10, 20, 40, etc.)
  SEQUENCE  = 4-digit sequence number (0000-9999)
  VAR       = Optional sub-drawing (01, 02, A, B)
  Rev[X]    = Revision (Draft, A-Z, AA-ZZ)
  MODEL     = Model identifier (Q100 for this project)
  EFF       = Effectivity (SN range: ALL, SN0100UP, SN0001-0050)
  APP       = Applicability (ALL, PAX, CGO, TEST, CERT)
  Description = Human-readable name (snake_case)
```

### Examples

```
✅ CORRECT:
57-40-1000_RevC_Q100_ALL_ALL_Forward_Wing_Spar_Assembly.svg
53-20-4000_RevB_Q100_SN0100UP_PAX_Passenger_Door_1L.svg
53-60-3000_RevA_Q100_ALL_ALL_LH2_Tank_Left.svg
85-60-01-001_RevA_Q100_ALL_ALL_H2_Storage_Infrastructure.svg

❌ INCORRECT:
57-40-1000_Forward_Wing_Spar.svg                    # Missing Rev + Model + EFF + APP
57-40-1000_v3_Forward_Wing_Spar.svg                # Wrong revision format
57-40-1000_RevC_Forward_Wing_Spar.svg              # Missing Model, EFF, APP
```

---

## Configuration Items (CI) System

### CI Numbering Convention

```
Format: CI-[ATA]-[ZONE]-[TYPE]-[ID]

Example: CI-57-400-SPAR-FWD
  CI     = Configuration Item prefix
  57     = ATA Chapter (Wings)
  400    = Zone (Center Wing Box)
  SPAR   = Type (Spar)
  FWD    = ID (Forward)
```

### CI Definition Template (YAML)

Every CI MUST have a `CI_Definition.yaml`:

```yaml
ci_metadata:
  ci_number: "CI-53-XXX-XXXX-XXX"
  ci_name: "Descriptive Name"
  ata_chapter: "53"
  zone: "XXX"
  model: "Q100"
  parent_ci: "CI-53-XXX"
  
classification:
  type: "[Primary|Secondary]"
  criticality: "[Critical|High|Medium|Low]"
  material_primary: "[CFRP|Aluminum|Titanium|Steel]"
  
status:
  design_status: "[Concept|Design|Released|Obsolete]"
  analysis_status: "[Not Started|In Progress|Complete]"
  
q100_configuration:
  effectivity: "[ALL|SN0100UP|SN0001-0050]"
  applicability: "[ALL|PAX|CGO|TEST|CERT]"
  
traceability:
  requirements: []
  parent_drawing: ""
  specification: ""
  
design_data:
  master_drawing:
    number: "XX-XX-XXXX"
    revision: "X"
    model: "Q100"
    file: "XX-XX-XXXX_RevX_Q100_EFF_APP_Description.svg"
```

---

## Directory Structure Rules

### Mandatory 14-Folder Lifecycle (XX-00_GENERAL)

```
XX-00_GENERAL/
├── XX-00-01_Overview/
├── XX-00-02_Safety/
├── XX-00-03_Requirements/
├── XX-00-04_Design/
├── XX-00-05_Interfaces/
├── XX-00-06_Engineering/
├── XX-00-07_V_AND_V/
├── XX-00-08_Prototyping/
├── XX-00-09_Production_Planning/
├── XX-00-10_Certification/
├── XX-00-11_EIS_Versions_Tags/
├── XX-00-12_Services/
├── XX-00-13_Subsystems_Components/
└── XX-00-14_Ops_Std_Sustain/
```

### Cross-ATA Buckets (Mandatory in Every Chapter)

```
├── XX-10_Operations/
├── XX-20_Subsystems/
├── XX-30_Circularity/
├── XX-40_Software/
├── XX-50_Structures/
├── XX-60_Storages/
├── XX-70_Propulsion/
├── XX-80_Energy/
└── XX-90_Tables_Schemas_Diagrams/
```

---

## Q100 Effectivity & Applicability

### Effectivity Codes (Serial Number Control)

```yaml
ALL:           "All serial numbers (universal parts)"
SN0001-0003:   "Test aircraft (flight test program)"
SN0004:        "Static test article (structural testing)"
SN0005-0010:   "Certification aircraft"
SN0011-0099:   "Pre-production standard"
SN0100UP:      "Series production (from SN0100 onwards)"

format_rules:
  all: "ALL"
  from_sn: "SN0100UP"
  range: "SN0001-0050"
  except: "SN0100UP-EXC0105"
  block: "BLK-A"
```

### Applicability Codes (Configuration Variants)

```yaml
ALL:  "Standard configuration (most common)"
PAX:  "Passenger interior features"
CGO:  "Cargo configuration option"
TEST: "Test aircraft instrumentation (SN0001-0003)"
CERT: "Certification test provisions (SN0004-0010)"
```

---

## Q100 Fuselage Zones

```yaml
zone_100_nose:
  length: "8.0 m"
  function: "Cockpit, avionics, forward bulkhead"
  
zone_200_forward_cabin:
  length: "10.0 m"
  function: "Rows 1-5, doors 1L/1R, forward galley"
  capacity: "30 passengers"
  
zone_300_mid_cabin:
  length: "12.0 m"
  function: "Rows 6-11, overwing exits"
  capacity: "50 passengers"
  
zone_400_center_wing_box:
  length: "8.0 m"
  function: "Wing integration, MLG, H2 tanks, cargo"
  
zone_500_aft_cabin:
  length: "6.0 m"
  function: "Rows 12-15, doors 2L/2R, aft galley"
  capacity: "20 passengers"
  
zone_600_tail:
  length: "4.0 m"
  function: "Aft pressure bulkhead, APU, empennage"
```

---

## Coding Standards

### Python

```python
"""
Q100-specific module docstring.
Follows PEP 8, type hints required, pytest for testing.
"""

from typing import List, Dict, Optional
import logging

def validate_q100_drawing_filename(filename: str) -> bool:
    """
    Validate Q100 drawing filename format.
    
    Format: XX-XX-XXXX_RevX_Q100_EFF_APP_Description.svg
    
    Args:
        filename: Drawing filename to validate
        
    Returns:
        True if valid, raises ValueError if invalid
        
    Example:
        >>> validate_q100_drawing_filename(
        ...     "57-40-1000_RevC_Q100_ALL_ALL_Spar.svg"
        ... )
        True
    """
    logger = logging.getLogger(__name__)
    
    # Validation logic with Q100 checks
    pattern = r'^\d{2}-\d{2}-\d{4}(_\d{2})?_Rev[A-Z]+_Q100_[A-Z0-9\-]+_[A-Z]+_.+\.svg$'
    
    if not re.match(pattern, filename):
        raise ValueError(f"Invalid Q100 drawing filename: {filename}")
    
    logger.info(f"Validated Q100 drawing: {filename}")
    return True
```

### CSV Data Files

```csv
# Q100 Effectivity Matrix
# Model: Q100 (100 passengers, 3,500 km range)
Effectivity_Code,SN_Start,SN_End,Configuration,Purpose
ALL,0001,9999,ALL,Universal parts
SN0001-0003,0001,0003,TEST,Flight test program
SN0100UP,0100,9999,ALL,Series production

# Rules:
# - Headers in first row
# - Snake_case for column names
# - UTF-8 encoding
# - No spaces after commas
```

---

## Assembly Numbering Convention

```
Format: ASM-[ATA]-[ZONE]-[SEQUENCE]_Description.yaml

Example: ASM-53-400-001_Forward_Spar_Assembly.yaml
  ASM    = Assembly prefix
  53     = ATA Chapter
  400    = Zone
  001    = Sequence number
```

### Assembly YAML Template

```yaml
assembly_metadata:
  assembly_id: "ASM-57-400-001"
  assembly_name: "Forward Wing Spar Assembly"
  assembly_revision: "C"
  model: "Q100"
  parent_ci: "CI-57-400-SPAR-FWD"
  
q100_configuration:
  effectivity: "SN0100UP"
  applicability: "ALL"
  
master_drawing:
  number: "57-40-1000"
  revision: "C"
  model: "Q100"
  file: "57-40-1000_RevC_Q100_SN0100UP_ALL_Forward_Wing_Spar.svg"

components:
  - part_number: "57-400-1001-01"
    ci_number: "CI-57-400-SPAR-FWD-WEB"
    description: "Forward Wing Spar Web"
    quantity: 1
    material: "CFRP T800/M21"
    mass_kg: 890.1
    primary_load_path: true
    
assembly_sequence:
  step_001: "Position spar web on assembly jig"
  step_002: "Bond upper cap (adhesive AF-191)"
  step_003: "Install permanent titanium fasteners"
  step_004: "Torque to 50 Nm ±5%"
```

---

## Safety-Critical Code (DO-178C)

```python
# SAFETY-CRITICAL: DAL A - Catastrophic
# Requirement: REQ-Q100-28-H2-001
# Verification: Test case TC-Q100-H2-SHUTDOWN-001

def emergency_shutdown_h2_system() -> bool:
    """
    Emergency shutdown of H2 fuel system.
    
    SAFETY-CRITICAL: Failure is catastrophic.
    DO-178C Level A verification required.
    100% MC/DC coverage mandatory.
    
    Returns:
        True if shutdown successful, False otherwise
    """
    # Dual-redundant valve closure
    valve_1_closed = close_h2_valve_primary()
    valve_2_closed = close_h2_valve_backup()
    
    # Independent sensor verification
    flow_stopped = verify_h2_flow_zero()
    
    # All conditions must be true
    shutdown_success = (
        valve_1_closed and 
        valve_2_closed and 
        flow_stopped
    )
    
    if not shutdown_success:
        trigger_emergency_alert()
    
    return shutdown_success
```

---

## Integration Points

### Strategic Mission Integration

```yaml
when_working_on:
  route_planning_software:
    consider:
      - "Prioritize secondary airport pairs"
      - "Flag overtourism destinations"
      - "Suggest alternative cities with capacity"
      
  market_analysis:
    consider:
      - "Identify cities 100K-500K population"
      - "Calculate hub congestion relief"
      - "Assess regional economic impact"
      
  infrastructure_planning:
    consider:
      - "Secondary airport H2 refueling"
      - "Regional airport upgrades needed"
      - "Local economic development potential"
```

### ATA Cross-References

```yaml
ata_53_fuselage:
  impacts:
    - "ATA 28: H2 fuel system interface"
    - "ATA 95: DPP for structural components"
    - "ATA 99: Manufacturing carbon footprint"
    
ata_85_infrastructure:
  impacts:
    - "ATA 28: H2 ground refueling"
    - "ATA 80: Ground power and energy"
    - "ATA 99: Ground operations carbon"
    
ata_95_neural_networks:
  impacts:
    - "Route optimization for decentralization"
    - "Overtourism prediction models"
    - "Regional connectivity analytics"
```

### Digital Product Passport (DPP)

Every physical component MUST have DPP data:

```json
{
  "dpp_id": "DPP-Q100-CI-57-400-SPAR-FWD",
  "model": "Q100",
  "ci_number": "CI-57-400-SPAR-FWD",
  "serial_number": "SN0105",
  "material_composition": {
    "CFRP_T800_M21": {
      "mass_kg": 2200,
      "carbon_footprint_kg_co2": 58300,
      "recyclability_percent": 85
    }
  },
  "supply_chain": {
    "supplier": "Hexcel Corporation",
    "location": "Salt Lake City, UT, USA",
    "certification": "AS9100D"
  },
  "blockchain_anchor": {
    "network": "Ethereum_Polygon",
    "tx_hash": "0x7d3e9f1a2c5b8e..."
  }
}
```

---

## Commit Message Convention

```
Format: <type>(<scope>): <subject>

Types:
  feat: New feature
  fix: Bug fix
  docs: Documentation
  style: Formatting
  refactor: Code restructure
  test: Tests
  chore: Maintenance

Scopes:
  ATA-XX: Specific ATA chapter
  Q100: Model-specific
  CI: Configuration Items
  DPP: Digital Product Passport
  mission: Strategic mission (decentralization, etc.)

Examples:
  feat(ATA-57): Add CI-57-400-SPAR-FWD for Q100 forward wing spar
  docs(Q100): Update strategic mission with overtourism metrics
  fix(ATA-85): Correct H2 storage capacity calculation
  feat(mission): Add secondary airport route planning module
```

---

## Testing Requirements

### Unit Tests (>80% coverage)

```python
import pytest
from q100_validators import validate_drawing_filename

def test_valid_q100_drawing():
    """Test Q100 drawing filename validation"""
    filename = "57-40-1000_RevC_Q100_ALL_ALL_Forward_Wing_Spar.svg"
    assert validate_drawing_filename(filename) == True

def test_missing_model_code():
    """Test filename missing Q100 model code"""
    filename = "57-40-1000_RevC_ALL_ALL_Forward_Wing_Spar.svg"
    with pytest.raises(ValueError, match="Missing model code Q100"):
        validate_drawing_filename(filename)

# Coverage target: 100% for safety-critical (DAL A/B)
```

---

## Code Review Checklist

### For Copilot to Consider

- [ ] File format correct? (.md, .csv, .svg, .yaml only)
- [ ] Q100 model code present in filenames?
- [ ] CI number valid and linked?
- [ ] Effectivity code valid (ALL, SN0100UP, etc.)?
- [ ] Applicability code valid (ALL, PAX, CGO, etc.)?
- [ ] Requirements traceability present?
- [ ] DPP data included (if physical component)?
- [ ] Strategic mission alignment (if route/market planning)?
- [ ] Tests written (>80% coverage)?
- [ ] Documentation updated?

---

## Common Patterns

### Creating New Q100 CI

```bash
# 1. Create CI directory
mkdir -p ATA_57-WINGS/57-00_GENERAL/57-00-04_Design/02_Configuration_Items/Zone_400/CI-57-400-SPAR-FWD/

# 2. Create CI_Definition.yaml (include model: "Q100")
# 3. Create Design_Description.md
# 4. Create master drawing with Q100 in filename
# 5. Update CI_Database.csv with Q100 effectivity
```

### Creating Q100 Drawing

```bash
# Format: XX-XX-XXXX_RevX_Q100_EFF_APP_Description.svg

# Example:
touch 57-40-1000_RevC_Q100_ALL_ALL_Forward_Wing_Spar_Assembly.svg

# MANDATORY fields:
# - Rev[X]: Revision code
# - Q100: Model identifier
# - Effectivity: SN range
# - Applicability: Configuration
```

---

## Q100 Strategic Mission Queries

### For Route Planning Features

```python
"""When developing route planning software, prioritize:"""

def suggest_q100_routes(origin_city: str, range_km: float = 3500):
    """
    Suggest Q100-compatible routes that support decentralization.
    
    Prioritizes:
    - Secondary airports over major hubs
    - Cities with overtourism pressure → alternative destinations
    - Regional economic development opportunities
    """
    
    # Check if origin is overtourism hotspot
    if is_overtourism_city(origin_city):
        # Suggest nearby alternatives with capacity
        alternatives = get_nearby_cities_with_capacity(origin_city)
        routes = generate_routes(alternatives, range_km=3500)
    else:
        # Normal route generation
        routes = generate_routes(origin_city, range_km=3500)
    
    # Filter for secondary airports
    routes = prioritize_secondary_airports(routes)
    
    return routes
```

---

## Helpful Copilot Prompts

### For Documentation

```
"Generate Q100 README.md for ATA XX bucket following OPT-IN Framework"
"Create CI_Definition.yaml for Q100 [component] in Zone [XXX]"
"Write design description for Q100 [assembly] including BWB specifics"
"Document route network emphasizing decentralization strategy"
```

### For Code

```
"Implement Q100 drawing filename validator with model/effectivity/applicability"
"Create Python script to export Q100 STEP files with validation"
"Write unit tests for Q100 H2 refueling safety interlock (DAL A)"
"Build route optimizer prioritizing secondary airports for Q100"
```

### For Strategic Mission

```
"Generate overtourism relief analysis for Q100 route network"
"Calculate regional economic impact of Q100 service to city [X]"
"Create secondary airport infrastructure requirements for Q100"
"Analyze hub congestion reduction from Q100 point-to-point routes"
```

---

## Validation Tools & Scripts

### Python Validators

Located in `tools/validators/`, these tools ensure Q100 compliance:

#### Drawing Validator

```python
from tools.validators import validate_q100_drawing_filename, DrawingValidator

# Quick validation
validate_q100_drawing_filename("57-40-1000_RevC_Q100_ALL_ALL_Spar.svg")

# Detailed validation
validator = DrawingValidator()
is_valid, error, components = validator.validate(filename)
```

**Validates**:
- ATA chapter format (XX-XX-XXXX pattern)
- Q100 model code presence
- Effectivity codes (ALL, SN0100UP, etc.)
- Applicability codes (ALL, PAX, CGO, TEST, CERT)
- File extensions (.svg, .step, .iges, .jt)

#### CI Validator

```python
from tools.validators import validate_ci_number, CIValidator

# Validate CI number format
validate_ci_number("CI-57-400-SPAR-FWD")

# Validate effectivity and applicability
validator = CIValidator()
valid, error = validator.validate_effectivity("SN0100UP")
valid, error = validator.validate_applicability("PAX")
```

**Validates**:
- CI number format (CI-[ATA]-[ZONE]-[TYPE]-[ID])
- ATA chapter validity
- Effectivity codes
- Applicability codes

#### Structure Validator

```python
from tools.validators import validate_directory_structure, StructureValidator

# Validate entire OPT-IN Framework
validate_directory_structure("/path/to/repo")

# Detailed validation
validator = StructureValidator("/path/to/repo")
results = validator.validate_all_ata_chapters()
report = validator.generate_report(results)
```

**Validates**:
- Mandatory 14-folder lifecycle in XX-00_GENERAL
- Cross-ATA buckets (10_Operations, 20_Subsystems, etc.)
- Forbidden file extensions (.pdf, .xlsx, .docx, .pptx)

### Running Validators

```bash
# Validate drawing filenames
python tools/validators/drawing_validator.py 57-40-1000_RevC_Q100_ALL_ALL_Spar.svg

# Validate CI numbers
python tools/validators/ci_validator.py CI-57-400-SPAR-FWD

# Validate directory structure
python tools/validators/structure_validator.py .
```

---

## Cross-Linking Dashboards

### Data Relationship Hierarchy

```yaml
CI_Database.csv:
  - Contains: All Configuration Items with metadata
  - Links to: Drawing_Register_Zone_XXX.csv
  - References: CI_Definition.yaml files
  - Feeds into: DPP JSON files

Drawing_Register_Zone_XXX.csv:
  - Contains: All drawings per zone
  - Links to: Actual .svg/.step files in ASSETS/DRAWINGS/
  - References: CI numbers
  - Includes: Model, effectivity, applicability

CI_Definition.yaml:
  - Contains: Detailed CI metadata
  - References: Master drawing number
  - Links to: Parent CI
  - Feeds into: DPP generation

DPP_JSON:
  - Contains: Digital Product Passport data
  - References: CI number
  - Links to: Material composition, supply chain
  - Includes: Blockchain anchor
```

### Auto-Update Guidelines

When creating or modifying components, Copilot should update related files:

#### Adding a New CI

1. **Create CI_Definition.yaml** in appropriate zone folder
2. **Add entry to CI_Database.csv** with:
   - CI number
   - Description
   - Zone
   - Effectivity
   - Status
3. **Update Drawing_Register_Zone_XXX.csv** with master drawing info
4. **Create DPP JSON file** with:
   - CI reference
   - Material data
   - Supply chain info
5. **Link in parent documentation** (e.g., zone overview, dashboard)

#### Adding a New Drawing

1. **Create .svg file** with Q100 naming convention
2. **Add to Drawing_Register_Zone_XXX.csv**:
   - Drawing number
   - Revision
   - Model (Q100)
   - Effectivity
   - Applicability
   - CI reference
3. **Update CI_Definition.yaml** master_drawing section
4. **Reference in related documentation**

#### Example Update Sequence

```python
# Copilot should suggest these updates when adding CI-57-400-SPAR-FWD

# 1. Create CI definition
create_file("CI-57-400-SPAR-FWD/CI_Definition.yaml", ci_yaml_content)

# 2. Update CI database
append_to_csv("CI_Database.csv", ci_entry)

# 3. Update drawing register
append_to_csv("Drawing_Register_Zone_400.csv", drawing_entry)

# 4. Create DPP data
create_file("CI-57-400-SPAR-FWD/DPP_Data.json", dpp_json_content)

# 5. Update zone dashboard
update_markdown("Zone_400_Dashboard.md", add_ci_link)
```

### Dashboard Locations

```
OPT-IN_FRAMEWORK/
└── T-TECHNOLOGY/
    └── A-AIRFRAME/
        └── ATA_53-FUSELAGE/
            ├── CI_Database.csv (Master CI list)
            ├── 53-00_GENERAL/
            │   └── 53-00-04_Design/
            │       ├── 02_Configuration_Items/
            │       │   └── Zone_XXX/
            │       │       ├── CI-53-XXX-TYPE-ID/
            │       │       │   ├── CI_Definition.yaml
            │       │       │   ├── Design_Description.md
            │       │       │   └── DPP_Data.json
            │       │       └── Drawing_Register_Zone_XXX.csv
            │       └── ASSETS/
            │           └── DRAWINGS/
            │               └── Zone_XXX/
            │                   └── 53-XX-XXXX_RevX_Q100_EFF_APP_Description.svg
            └── 53-90_Tables_Schemas_Diagrams/
                └── Zone_Dashboards/
```

---

## Security & Compliance

### Safety-Critical Code Requirements

All safety-critical code MUST include:

1. **DO-178C Compliance Tag**:
```python
# SAFETY-CRITICAL: DAL A - Catastrophic
# DO-178C Level A verification required
# 100% MC/DC coverage mandatory
# Requirement: REQ-Q100-28-H2-001
# Verification: Test case TC-Q100-H2-SHUTDOWN-001
```

2. **Design Assurance Level (DAL)** classification:
   - **DAL A** (Catastrophic): Failure causes multiple fatalities
   - **DAL B** (Hazardous): Failure causes serious injury
   - **DAL C** (Major): Failure causes passenger discomfort
   - **DAL D** (Minor): Failure is inconvenient
   - **DAL E** (No Effect): Failure has no safety impact

3. **Traceability**:
   - Link to requirements (REQ-Q100-...)
   - Link to verification tests (TC-Q100-...)
   - Link to hazard analysis

### Security Scanning

#### Bandit (Python Security)

Integrated into CI/CD pipeline (`q100-validation.yml`):

```bash
# Run locally
pip install bandit[toml]
bandit -r tools/ -f screen
```

**Checks for**:
- Hardcoded passwords/secrets
- SQL injection vulnerabilities
- Unsafe deserialization
- Weak cryptography
- Path traversal issues

#### Safety (Dependency Vulnerabilities)

Check Python dependencies for known vulnerabilities:

```bash
# Run locally
pip install safety
safety check
```

### Pre-commit Security Hooks

Install hooks for automatic validation:

```bash
bash .github/hooks/setup-hooks.sh
```

**Validates**:
- Q100 model code in drawings
- Forbidden file extensions
- DO-178C tags on safety-critical code
- Python syntax
- Strategic mission commit scopes

### Compliance Checklist

Before finalizing safety-critical code:

- [ ] DAL classification documented
- [ ] DO-178C compliance tag present
- [ ] Requirements traceability complete
- [ ] Test cases written and linked
- [ ] 100% MC/DC coverage achieved (DAL A/B)
- [ ] Hazard analysis updated
- [ ] Security scan passed (Bandit)
- [ ] Dependencies checked (Safety)
- [ ] Code review completed
- [ ] Verification evidence archived

### Security Contact

For security vulnerabilities in Q100 systems:

1. **Do not open public issues**
2. Contact: [security contact per project policy]
3. Include: Component, version, impact, reproduction steps
4. Encrypt sensitive details

---

## GitHub Actions Workflows

### Copilot Setup Steps

**File**: `.github/workflows/copilot-setup-steps.yml`

Prepares the environment for GitHub Copilot:
- Installs Python 3.11 and dependencies
- Sets up Node.js 20
- Installs validator packages
- Configures doc-meta-enforcer MCP

### Q100 Validation Suite

**File**: `.github/workflows/q100-validation.yml`

Comprehensive validation on every PR:

1. **Structure Validation**: Checks OPT-IN Framework compliance
2. **File Format Validation**: Detects forbidden extensions
3. **Strategic Mission Validation**: Ensures Q100 model codes
4. **Security Scan**: Runs Bandit on Python code

**Triggers**:
- Pull requests to `main`
- Pushes to `main`
- Manual workflow dispatch

### Document Metadata Enforcement

**File**: `.github/workflows/doc-meta.yml`

Validates documentation metadata:
- Document control blocks
- Version information
- AI authorship attribution
- Hyperlink integrity

---

## Resources

- **OPT-IN Framework**: `OPT-IN_FRAMEWORK_STANDARD.md`
- **Validators**: `tools/validators/`
- **Git Hooks**: `.github/hooks/`
- **Workflows**: `.github/workflows/`
- **Instructions**: `.github/instructions/`

### Quick Links

- [Drawing Validator](tools/validators/drawing_validator.py)
- [CI Validator](tools/validators/ci_validator.py)
- [Structure Validator](tools/validators/structure_validator.py)
- [Pre-commit Hooks](/.github/hooks/README.md)
- [Setup Hooks Script](/.github/hooks/setup-hooks.sh)

---

**Last Updated**: 2025-11-23  
**Model**: Q100 (100 passengers, 3,500 km)  
**Framework Version**: OPT-IN v1.1  
**Maintained By**: AMPEL360 Q100 Documentation Team  
**Strategic Focus**: Regional Connectivity & Sustainable Tourism  
**Security**: DO-178C Compliant | Bandit Scanned
