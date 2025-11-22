# 53-00-04-02-002: CI Numbering Convention – ATA 53 Fuselage

## 1. Overview

This document defines the systematic numbering convention for all Configuration Items (CIs) in the AMPEL360 BWB fuselage (ATA 53). Consistent numbering ensures clear identification, traceability, and configuration management throughout the program lifecycle.

## 2. Standard CI Number Format

```yaml
format: "CI-[ATA]-[ZONE]-[TYPE]-[ID]"

components:
  ATA:  "53"                          # Fixed: ATA Chapter 53 (Fuselage)
  ZONE: "3-digit zone number"         # 100, 200, 300, 400, 500, 600
  TYPE: "Component type code"         # FR, SKN, SPAR, BEAM, etc.
  ID:   "Unique identifier"           # Alphanumeric, specific to each CI
```

### Examples

```yaml
examples:
  - number: "CI-53-100-FR-100A"
    description: "Frame 100A in Zone 100"
    
  - number: "CI-53-200-SKN-L01"
    description: "Lower skin panel 01 in Zone 200"
    
  - number: "CI-53-400-SPAR-FWD"
    description: "Forward wing spar in Zone 400"
    
  - number: "CI-53-400-BAY-MLG-L"
    description: "Left main landing gear bay in Zone 400"
    
  - number: "CI-53-600-BHD-AFT"
    description: "Aft pressure bulkhead in Zone 600"
```

## 3. Zone Numbering

| Zone Number | Zone Name | Station Range | Description |
|-------------|-----------|---------------|-------------|
| **100** | Nose Section | 0-150 | Forward bulkhead to cockpit |
| **200** | Forward Cabin | 150-300 | First class and forward economy |
| **300** | Mid Cabin | 300-450 | Main economy cabin |
| **400** | Center Wing Box | 450-600 | Wing integration, gear bays (CRITICAL) |
| **500** | Aft Cabin | 600-750 | Aft cabin and empennage transition |
| **600** | Tail Section | 750-900 | Aft bulkhead to tail |

### Special Zone Designations

- **000**: Top-level (CI-53-000 = entire ATA 53 Fuselage)
- **ALL**: Cross-zone (rare, for components spanning multiple zones)

## 4. Type Codes

### 4.1 Primary Structure Types

| Type Code | Full Name | Description | Examples |
|-----------|-----------|-------------|----------|
| **FR** | Frame | Circumferential structural frames | CI-53-100-FR-100A |
| **SKN** | Skin | Shell panels (upper, lower, side) | CI-53-200-SKN-U01 |
| **SPAR** | Spar | Wing spars, keel beams | CI-53-400-SPAR-FWD |
| **BEAM** | Beam | Floor beams, load beams | CI-53-200-BEAM-FLR-01 |
| **BHD** | Bulkhead | Pressure bulkheads, firewalls | CI-53-100-BHD-FWD |
| **RIB** | Rib | Wing ribs, structural ribs | CI-53-400-RIB-001 |
| **STGR** | Stringer | Longitudinal stiffeners | CI-53-200-STGR-U-L-01 |

### 4.2 Assembly and Integration Types

| Type Code | Full Name | Description | Examples |
|-----------|-----------|-------------|----------|
| **ASSY** | Assembly | Major assemblies | CI-53-400-ASSY-CWB |
| **DOOR** | Door | Door frames and structures | CI-53-200-DOOR-1L |
| **BAY** | Bay | Bays (gear, cargo, equipment) | CI-53-400-BAY-MLG-L |
| **FLR** | Floor | Floor structures and assemblies | CI-53-200-FLR-GRID |

### 4.3 Fittings and Connections

| Type Code | Full Name | Description | Examples |
|-----------|-----------|-------------|----------|
| **FTG** | Fitting | Attachment fittings | CI-53-400-FTG-MLG-01 |
| **LUG** | Lug | Attachment lugs | CI-53-400-LUG-SPAR-01 |
| **SPLICE** | Splice | Joint splices | CI-53-200-SPLICE-SKN-01 |
| **CLAMP** | Clamp | Clamp assemblies | CI-53-300-CLAMP-SYS-01 |

### 4.4 Secondary Structure Types

| Type Code | Full Name | Description | Examples |
|-----------|-----------|-------------|----------|
| **PANEL** | Panel | Interior/exterior panels | CI-53-300-PANEL-INT-01 |
| **FAIRING** | Fairing | Aerodynamic fairings | CI-53-500-FAIRING-AFT-01 |
| **BRACKET** | Bracket | Mounting brackets | CI-53-200-BRACKET-EQ-01 |
| **TRACK** | Track | Seat tracks, cargo tracks | CI-53-200-TRACK-SEAT-L |

### 4.5 Miscellaneous Types

| Type Code | Full Name | Description | Examples |
|-----------|-----------|-------------|----------|
| **ACCESS** | Access | Access panels and doors | CI-53-500-ACCESS-01 |
| **INSP** | Inspection | Inspection panels | CI-53-400-INSP-MLG-01 |
| **SEAL** | Seal | Seals and gaskets | CI-53-200-SEAL-DOOR-1L |

## 5. ID Field Guidelines

The ID field provides unique identification within a type and zone.

### 5.1 Numbering Patterns

**Sequential Numbering**:
- Use for series of similar components
- Format: 001, 002, 003, ... or 01, 02, 03, ...
- Example: CI-53-100-FR-001, CI-53-100-FR-002, ...

**Station-Based**:
- Use station number or frame number
- Format: Based on fuselage station
- Example: CI-53-100-FR-100A (Frame at Station 100)

**Position-Based**:
- Use position indicators
- U = Upper, L = Lower, LH = Left Hand, RH = Right Hand, FWD = Forward, AFT = Aft
- Example: CI-53-200-SKN-U01 (Upper skin panel 01)

**Functional**:
- Use functional descriptors
- Example: CI-53-400-SPAR-FWD (Forward spar), CI-53-400-SPAR-REAR (Rear spar)

### 5.2 Compound IDs

For complex components, combine position and sequence:
- `CI-53-200-BEAM-FLR-L-01`: Floor beam, left side, number 01
- `CI-53-300-STGR-U-LH-05`: Upper stringer, left hand, number 05
- `CI-53-400-FTG-MLG-L-FRONT`: Main gear fitting, left side, front attachment

## 6. Hierarchy Levels

CIs are organized in a hierarchical structure:

```yaml
hierarchy:
  level_1:  "CI-53-000"                   # Top level (entire fuselage)
  level_2:  "CI-53-XXX"                   # Zone level (100, 200, etc.)
  level_3:  "CI-53-XXX-TYPE-ID"           # Component level
  level_4:  "CI-53-XXX-TYPE-ID-SUB"       # Sub-component level (optional)
```

### Example Hierarchy

```
CI-53-000 (ATA 53 Fuselage)
└── CI-53-400 (Center Wing Box)
    ├── CI-53-400-SPAR-FWD (Forward Wing Spar)
    │   ├── CI-53-400-SPAR-FWD-WEB (Spar web)
    │   ├── CI-53-400-SPAR-FWD-CAP-U (Upper cap)
    │   └── CI-53-400-SPAR-FWD-CAP-L (Lower cap)
    ├── CI-53-400-SPAR-REAR (Rear Wing Spar)
    └── CI-53-400-BAY-MLG-L (Left main gear bay)
```

## 7. Special Cases and Exceptions

### 7.1 Assemblies Spanning Multiple Zones

For components that span multiple zones, use the primary zone:
- **CI-53-300-ASSY-WINGBODY**: Wing-body blend assembly (primary in Zone 300)

Alternatively, create separate CIs per zone with interface references.

### 7.2 Mirror Components (Left/Right)

Use position indicators in the ID:
- **CI-53-400-BAY-MLG-L**: Left main gear bay
- **CI-53-400-BAY-MLG-R**: Right main gear bay

### 7.3 Repeated Components

For identical repeated components (e.g., frames), use sequential numbering:
- **CI-53-200-FR-001**, **CI-53-200-FR-002**, etc.

Or station-based:
- **CI-53-200-FR-200A**, **CI-53-200-FR-210A**, etc.

### 7.4 Modification and Variant CIs

For design changes that create variants:
- **Original**: CI-53-200-BEAM-01
- **Variant**: CI-53-200-BEAM-01-M01 (Modification 01)

Document variants in the CI's `CHANGELOG.md`.

## 8. CI Number Assignment Process

### 8.1 New CI Creation

1. **Identify need** for new CI (new component, subdivision, etc.)
2. **Determine zone** where component is located
3. **Select type code** from standard list
4. **Assign unique ID** following guidelines
5. **Check for conflicts** in CI database
6. **Register** in CI database
7. **Create CI folder** and documentation

### 8.2 Approval Authority

| CI Level | Approval Required |
|----------|-------------------|
| Level 1-2 (Top/Zone) | Configuration Control Board (CCB) |
| Level 3 (Component) | Lead Design Engineer + Configuration Manager |
| Level 4 (Sub-component) | Design Engineer + Configuration Manager |

### 8.3 Number Reservation

Design teams may reserve blocks of CI numbers for planned components:
- Request submitted to Configuration Manager
- Block reserved for specific period (e.g., 6 months)
- Unused numbers returned to pool

## 9. Version Control and Changes

### 9.1 CI Number Stability

**Rule**: CI numbers are permanent and do not change once assigned.

**Rationale**: Ensures traceability through requirements, drawings, analyses, tests, and service.

### 9.2 Handling Design Changes

- **Minor changes**: Update CI documentation, increment version
- **Major changes**: May require new CI number if component identity changes significantly
- **Obsolescence**: Mark CI as "Obsolete" in database, do not reuse number

### 9.3 Configuration Management

All CI changes documented in:
- `CI_Definition.yaml` (version field)
- `CHANGELOG.md` (change history)
- `ASSETS/53-00-04-02-A-006_CI_Change_Log.csv` (program-wide log)

## 10. Integration with Other Systems

### 10.1 PLM System

CI numbers are the primary key in the PLM (Product Lifecycle Management) system:
- Link to CAD models
- Link to drawings
- Link to BOMs (Bill of Materials)
- Link to manufacturing plans

### 10.2 Requirements Management

CI numbers link to requirements:
- `Requirements_Traceability.csv` in each CI folder
- Program-level traceability matrix

### 10.3 Analysis and Simulation

CI numbers used in FEA models and analysis reports:
- Element naming in FEA
- Load case identification
- Results reporting

## 11. Documentation Standards

### 11.1 CI Number Usage in Documents

- **Always use full CI number**: "CI-53-400-SPAR-FWD" (not "FWD SPAR" or "Forward Spar")
- **First mention**: Use full number and name: "CI-53-400-SPAR-FWD (Forward Wing Spar)"
- **Subsequent mentions**: May abbreviate if clear from context

### 11.2 CI Number in Drawings

- Drawing number derived from CI number
- Format: `[Zone]-[Sub-zone]-[Sequence]`
- Example: CI-53-400-SPAR-FWD → Drawing 53-40-1000

## 12. Quality Assurance

### 12.1 CI Number Audits

Regular audits to ensure:
- No duplicate CI numbers
- All CIs registered in database
- Naming convention followed
- Documentation complete

### 12.2 Training

All team members working with CIs must complete training on:
- Numbering convention
- CI structure and hierarchy
- Configuration management procedures

## 13. Tools and Resources

- **CI Database**: [ASSETS/53-00-04-02-A-001_CI_Database.csv](ASSETS/53-00-04-02-A-001_CI_Database.csv)
- **CI Hierarchy Tree**: [ASSETS/53-00-04-02-A-002_CI_Hierarchy_Tree.svg](ASSETS/53-00-04-02-A-002_CI_Hierarchy_Tree.svg)
- **CI Template**: [../ASSETS/templates/53-00-04-A-001_CI_Definition_Template.yaml](../ASSETS/templates/53-00-04-A-001_CI_Definition_Template.yaml)
- **Configuration Management Plan**: Program-level document

---

## Document Control

- **Document ID**: 53-00-04-02-002
- **Title**: CI Numbering Convention – ATA 53 Fuselage
- **Version**: 1.0
- **Date**: 2025-11-22
- **Owner**: ATA 53 Configuration Manager
- **Approval**: _[to be completed]_
- **Status**: DRAFT
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

**AI Assistance**:
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Last AI update: _2025-11-22_.
