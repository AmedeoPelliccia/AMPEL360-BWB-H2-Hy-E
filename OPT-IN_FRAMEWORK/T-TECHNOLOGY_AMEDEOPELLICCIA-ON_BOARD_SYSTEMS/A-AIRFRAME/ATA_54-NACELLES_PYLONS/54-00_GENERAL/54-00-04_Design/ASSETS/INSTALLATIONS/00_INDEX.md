# INSTALLATIONS — ATA 54-00-04 Design Assets

This folder contains installation documentation for nacelle and pylon components including layouts, mounting procedures, routing documentation, and system integration instructions.

## Purpose

Installation documentation ensures proper integration of nacelle and pylon components with:
- Correct spatial arrangement and alignment
- Appropriate mounting and attachment methods
- Safe routing of electrical, hydraulic, and pneumatic systems
- Complete system integration and verification

## Folder Structure

| Subfolder | Description | Asset Count |
|-----------|-------------|-------------|
| [LAYOUTS/](./LAYOUTS/) | Installation layout drawings and spatial arrangements | 3 |
| [MOUNTING/](./MOUNTING/) | Mounting and attachment procedures | 2 |
| [ROUTING/](./ROUTING/) | Cable, harness, and fluid line routing | 2 |
| [SYSTEMS/](./SYSTEMS/) | System integration installations | 2 |
| [ACCESS/](./ACCESS/) | Maintenance access documentation | 1 |
| [TEMPLATES/](./TEMPLATES/) | Installation documentation templates | 1 |

**Total Installation Documents:** 11

---

## Complete Installation Register

| ID | Title | Type | Subfolder | Status | Related Assembly | Related Requirement |
|----|-------|------|-----------|--------|------------------|---------------------|
| 54-00-04-I000 | Installation Title Template | Template | TEMPLATES | Template | N/A | N/A |
| 54-00-04-I001 | Nacelle Installation on Pylon | Layout | LAYOUTS | Planned | ASM-54-NAC-001, ASM-54-PYL-001 | 54-00-03-01-003 |
| 54-00-04-I002 | Pylon-to-Wing Attachment Installation | Mounting | MOUNTING | Planned | ASM-54-PYL-001 | 54-00-03-01-002 |
| 54-00-04-I003 | Engine Mount Installation Procedure | Procedure | MOUNTING | Planned | ASM-54-NAC-001 | 54-00-03-01-005 |
| 54-00-04-I004 | Thrust Reverser Installation Layout | Layout | LAYOUTS | Planned | ASM-54-REV-001 | 54-00-03-01-004 |
| 54-00-04-I005 | SHM Sensor Installation Map | Sensor Placement | SYSTEMS | Planned | ASM-54-NAC-001, ASM-54-PYL-001, ASM-54-REV-001, ASM-54-COW-001 | 54-00-03-07-001 |
| 54-00-04-I006 | Electrical Harness Routing - Nacelle | Cable Routing | ROUTING | Planned | ASM-54-NAC-001 | 54-00-03-05-001 |
| 54-00-04-I007 | Hydraulic Line Routing - Thrust Reverser | Fluid Routing | ROUTING | ASM-54-REV-001 | 54-00-03-05-002 |
| 54-00-04-I008 | Fire Detection System Installation | System | SYSTEMS | Planned | ASM-54-NAC-001 | 54-00-03-06-001 |
| 54-00-04-I009 | Access Panel and Fastener Locations | Access | ACCESS | Planned | ASM-54-NAC-001, ASM-54-COW-001, ASM-54-REV-001, ASM-54-PYL-001 | 54-00-03-06-001 |
| 54-00-04-I010 | Ground Clearance Verification Layout | Clearance Study | LAYOUTS | Planned | ASM-54-NAC-001, ASM-54-PYL-001 | 54-00-03-03-001 |

---

## Statistics Summary

### By Installation Type
- **Layout**: 3 documents (I001, I004, I010)
- **Mounting/Procedure**: 2 documents (I002, I003)
- **Routing**: 2 documents (I006, I007)
- **System**: 2 documents (I005, I008)
- **Access**: 1 document (I009)
- **Template**: 1 document (I000)

### By Status
- **Template**: 1 document
- **Planned**: 10 documents

### By Subfolder
- **LAYOUTS**: 3 installation documents
- **MOUNTING**: 2 installation documents
- **ROUTING**: 2 installation documents
- **SYSTEMS**: 2 installation documents
- **ACCESS**: 1 installation document
- **TEMPLATES**: 1 template document

---

## Installation → Assembly Traceability Matrix

| Installation ID | Related Assemblies | Description |
|-----------------|-------------------|-------------|
| 54-00-04-I001 | ASM-54-NAC-001, ASM-54-PYL-001 | Nacelle to pylon mounting interface |
| 54-00-04-I002 | ASM-54-PYL-001 | Pylon to wing structural attachment |
| 54-00-04-I003 | ASM-54-NAC-001 | Engine mount integration in nacelle |
| 54-00-04-I004 | ASM-54-REV-001 | Thrust reverser system installation |
| 54-00-04-I005 | ASM-54-NAC-001, ASM-54-PYL-001, ASM-54-REV-001, ASM-54-COW-001 | SHM sensors across all primary structures |
| 54-00-04-I006 | ASM-54-NAC-001 | Electrical systems routing in nacelle |
| 54-00-04-I007 | ASM-54-REV-001 | Hydraulic system for reverser actuation |
| 54-00-04-I008 | ASM-54-NAC-001 | Fire detection system in fire zones |
| 54-00-04-I009 | ASM-54-NAC-001, ASM-54-COW-001, ASM-54-REV-001, ASM-54-PYL-001 | Maintenance access across all assemblies |
| 54-00-04-I010 | ASM-54-NAC-001, ASM-54-PYL-001 | Ground clearance verification |

---

## Installation → Requirement Traceability Matrix

| Installation ID | Related Requirements | Requirement Title |
|-----------------|---------------------|-------------------|
| 54-00-04-I001 | 54-00-03-01-003 | Nacelle Pylon Interface Requirements |
| 54-00-04-I002 | 54-00-03-01-002 | Pylon-Wing Structural Interface Requirements |
| 54-00-04-I003 | 54-00-03-01-005 | Engine Mount Interface Requirements |
| 54-00-04-I004 | 54-00-03-01-004 | Thrust Reverser Integration Requirements |
| 54-00-04-I005 | 54-00-03-07-001 | Nacelle Structure SHM Compatibility |
| 54-00-04-I006 | 54-00-03-05-001 | Electrical System Interface Requirements |
| 54-00-04-I007 | 54-00-03-05-002 | Hydraulic System Interface Requirements |
| 54-00-04-I008 | 54-00-03-06-001 | Fire Detection Coverage Requirements |
| 54-00-04-I009 | 54-00-03-06-001 | Maintenance Access Requirements |
| 54-00-04-I010 | 54-00-03-03-001 | Ground Clearance Requirements |

---

## Cross-ATA Chapter References

| Installation ID | Related ATA Chapters | Description |
|-----------------|---------------------|-------------|
| 54-00-04-I001 | 71, 57, 05 | Engine mount, wing interface, maintenance |
| 54-00-04-I002 | 57, 05, 20 | Wing structure, maintenance, standard practices |
| 54-00-04-I003 | 71, 05, 78, 80 | Power plant, maintenance, exhaust, starting |
| 54-00-04-I004 | 78, 29, 24, 31 | Thrust reverser, hydraulic, electrical, indicating |
| 54-00-04-I005 | 95, 45, 24, 53 | SHM/neural networks, CMS, electrical, fuselage SHM |
| 54-00-04-I006 | 24, 26, 31, 78, 95 | Electrical, fire protection, indicating, reverser, SHM |
| 54-00-04-I007 | 29, 78, 05, 12 | Hydraulic, thrust reverser, maintenance, servicing |
| 54-00-04-I008 | 26, 31, 24, 45 | Fire protection, indicating, electrical, CMS |
| 54-00-04-I009 | 05, 51, 12 | Maintenance, structures, servicing |
| 54-00-04-I010 | 05, 32, 08 | Ground handling, landing gear, general dimensions |

---

## Key Installation Parameters Summary

### Torque Requirements
| Installation | Critical Fasteners | Torque Value | Application |
|--------------|-------------------|--------------|-------------|
| I001 | Forward pylon mount (M24) | 450 Nm ±15 Nm | Nacelle-pylon interface |
| I001 | Aft pylon mount (M20) | 320 Nm ±10 Nm | Nacelle-pylon interface |
| I002 | Pylon-wing attachment (M30) | 850 Nm ±25 Nm | Primary load path |
| I003 | Engine mount bolts (M36) | 1200 Nm ±40 Nm | Engine-nacelle interface |
| I004 | Actuator mount bolts (M16) | 180 Nm ±8 Nm | Reverser actuation |
| I007 | AN fittings (-10 size) | 50 Nm ±4 Nm | Hydraulic connections |

### Critical Clearances
| Installation | Clearance Point | Minimum Value | Condition |
|--------------|----------------|---------------|-----------|
| I001 | Wing-to-nacelle | 350 mm | Static, undeflected |
| I001 | Minimum ground clearance (fwd) | 650 mm | Static, on gear |
| I003 | Engine-to-nacelle radial | 25 mm min | All operating conditions |
| I003 | Fan blade tip to nacelle | 15 mm min | Static, cold build |
| I004 | Blocker door to cascade (stowed) | 5 mm min | Reverser stowed |
| I006 | Harness to moving components | 25 mm min | All operating positions |
| I007 | Hydraulic line to hot surfaces | 75 mm min | Core cowl, exhaust (>150°C) |
| I010 | Nacelle forward low point | 650 mm min | Static clearance |
| I010 | Rotation clearance | 250 mm min | +8 deg pitch, MTOW |

### Mounting Points
| Installation | Number of Points | Type |
|--------------|-----------------|------|
| I001 | 6 | Nacelle-pylon interface |
| I002 | 8 | Pylon-wing structural attachment |
| I003 | 4 | Engine mount |
| I004 | 12 | Thrust reverser components |
| I005 | 32 | SHM sensors across structures |
| I006 | 48 | Electrical harness support brackets |
| I007 | 24 | Hydraulic line support clamps |
| I008 | 16 | Fire detection sensing element brackets |
| I009 | 156 | Access panel fasteners (all types) |

---

## Usage Guidelines

### When to Create New Installation Documents

Create new installation documentation when:
1. New component assemblies are added requiring installation procedures
2. Routing changes are needed for systems integration
3. Access provisions change due to design modifications
4. Clearance studies are required for design verification
5. System integration requires new installation guidance

### Installation Documentation Standards

All installation documents must include:
1. **Traceability**: Links to related assemblies, requirements, and drawings
2. **Installation sequence**: Step-by-step procedure
3. **Torque requirements**: Specific values and tolerances for all fasteners
4. **Clearances**: Minimum clearances with operating conditions
5. **Tooling**: Required tools with capacities and specifications
6. **Safety notes**: Critical safety considerations
7. **Cross-references**: Related ATA chapters
8. **Verification**: Methods and acceptance criteria

### File Naming Convention

Follow the established pattern:
```
54-00-04-I<nnn>_INST_<ShortName>.yaml
```

Where:
- `54-00-04` = ATA reference (Chapter 54, Section 00, Subsection 04)
- `I<nnn>` = Installation number (I001, I002, etc.)
- `INST` = Category designator for installations
- `ShortName` = Descriptive name in PascalCase with underscores

### Metadata Requirements

Each installation YAML must contain:
- `id`: Unique installation identifier
- `title`: Descriptive title
- `category`: "INST"
- `installation_type`: Layout|Mounting|Routing|System|Access|Clearance
- `ata_chapter`: "54"
- `description`: Detailed description
- `status`: Current status (Template|Planned|In-Progress|Complete)
- `version`: Version number
- `owner`: Responsible team/organization
- `last_updated`: Date of last update (YYYY-MM-DD)
- `traceability`: Links to assemblies, requirements, drawings
- `installation_parameters`: Detailed installation specifications
- `verification`: Verification methods and status

---

## Coordination with Other Design Assets

### Installation → Drawing Relationships
- Installation layouts reference General Arrangement drawings (D-series)
- Mounting procedures reference Detail and Interface drawings
- Routing documents reference Installation drawings
- Access documentation references all relevant structural drawings

### Installation → Assembly Relationships
- Each installation document traces to one or more assemblies
- Assemblies define component details; installations define integration
- Installation procedures reference assembly build sequences
- Installation verification confirms assembly interfaces

### Installation → Requirement Relationships
- Installation documents implement specific requirements
- Requirements define acceptance criteria; installations define methods
- Each installation document should trace to at least one requirement
- Requirement verification methods include installation verification

---

## Quality and Verification

### Installation Verification Activities
1. **Dimensional verification**: Confirm installation geometry per drawings
2. **Torque verification**: 100% verification of critical fasteners
3. **Clearance verification**: Confirm all minimum clearances maintained
4. **Functional testing**: Verify systems operate correctly after installation
5. **Visual inspection**: Confirm workmanship and proper installation
6. **Documentation**: Complete installation records and sign-offs

### Common Installation Issues
- Incorrect torque application (under or over torque)
- Inadequate clearances due to tolerance stack-up
- Improper routing causing chafing or interference
- Incomplete verification documentation
- Missing or incorrect fasteners
- Contamination during installation (FOD)

### Installation Best Practices
1. Follow installation sequence precisely
2. Use calibrated tooling with current certificates
3. Verify clearances before final torquing
4. Document any deviations from procedures
5. Photograph critical installation steps
6. Maintain FOD control throughout installation
7. Perform functional testing before acceptance

---

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1.0 | 2026-01-02 | Installation Engineering | Initial creation with 11 installation documents |

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **DRAFT** |
| Human Approver | _[to be completed]_ |
| Repository | `AMPEL360-AIR-T` |
| Last AI Update | 2026-01-02 |

---

## References

- [ASSETS README](../README.md) - Parent ASSETS folder documentation
- [INDEX.meta.yaml](../INDEX.meta.yaml) - Master asset index
- [54-00-03_Requirements](../../54-00-03_Requirements/) - Requirements traceability
- [ASSEMBLIES](../ASSEMBLIES/) - Related assembly documentation
- [DRAWINGS](../DRAWINGS/) - Related drawing documentation
- [ATA 54 General](../../README.md) - ATA Chapter 54 overview

---

*This index is maintained by the Installation Engineering team. For questions or updates, contact the document owner.*
