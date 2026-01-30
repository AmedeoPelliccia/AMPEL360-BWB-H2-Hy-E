# PARTS — Physical Parts Library (ATA 10-00-04)

## 1. Purpose

This directory contains the **parts library** for **ATA 10-00-04_Design** (Parking, Mooring, Storage & RTS), including:

- **Tiedown parts** - Tiedown rings, fittings, anchors, and cables
- **Mooring parts** - Mooring masts, cables, clamps, and storm tie kits
- **Parking parts** - Wheel chocks, ground locks, and parking brake locks
- **H2 system parts** - H2 vent valves, detectors, cryo insulation, tank covers (H2/cryo compatible)
- **Storage parts** - Desiccants, protective covers, pitot covers, inlet plugs
- **Fasteners & hardware** - Specialized bolts, shackles, pins, safety wire
- **Consumables** - Preservation compounds, corrosion inhibitors, desiccant materials

Each **part** has its own dedicated document with:

- Part identification (Part Number, CAGE Code)
- Technical specifications (weight, dimensions, material)
- Performance requirements
- H2/cryo compatibility ratings (for H2 system parts)
- Supplier information
- Interchangeability data
- Storage requirements
- Related documentation and traceability

These parts are referenced by:

- Assemblies in `ASSETS/ASSEMBLIES/`
- Drawings in `ASSETS/DRAWINGS/`
- Models in `ASSETS/MODELS/`
- Bills of Materials in requirements/design documentation
- Installation layouts in `ASSETS/INSTALLATIONS/`

---

## 2. Structure

```text
PARTS/
├── README.md                    # This file
├── 00_INDEX.md                  # Table of contents with links to all parts
├── part-metadata.schema.json    # JSON Schema for part metadata
│
├── tiedown-parts/               # Tiedown rings, fittings, anchors
│   ├── 10-PRT-TD-001_Tiedown_Ring_Assy.md
│   ├── 10-PRT-TD-002_Tiedown_Fitting_Fwd.md
│   ├── 10-PRT-TD-003_Tiedown_Fitting_Aft.md
│   ├── 10-PRT-TD-004_Ground_Anchor_Plate.md
│   └── 10-PRT-TD-005_Tiedown_Cable_Assy.md
│
├── mooring-parts/               # Mooring masts, cables, clamps
│   ├── 10-PRT-MR-001_Mooring_Mast_Assy.md
│   ├── 10-PRT-MR-002_Mooring_Cable_Assy.md
│   ├── 10-PRT-MR-003_Mooring_Clamp.md
│   ├── 10-PRT-MR-004_Mooring_Swivel.md
│   └── 10-PRT-MR-005_Storm_Tie_Kit.md
│
├── parking-parts/               # Wheel chocks, ground locks
│   ├── 10-PRT-PK-001_Wheel_Chock_Main.md
│   ├── 10-PRT-PK-002_Wheel_Chock_Nose.md
│   ├── 10-PRT-PK-003_Ground_Lock_MLG.md
│   ├── 10-PRT-PK-004_Ground_Lock_NLG.md
│   └── 10-PRT-PK-005_Parking_Brake_Lock.md
│
├── h2-system-parts/             # H2-specific parts (cryo-rated, H2 compatible)
│   ├── 10-PRT-H2-001_H2_Vent_Valve_Assy.md
│   ├── 10-PRT-H2-002_H2_Detector_Sensor.md
│   ├── 10-PRT-H2-003_H2_Detector_Housing.md
│   ├── 10-PRT-H2-004_Cryo_Insulation_Blanket.md
│   ├── 10-PRT-H2-005_LH2_Tank_Cover.md
│   └── 10-PRT-H2-006_Emergency_Purge_Valve.md
│
├── storage-parts/               # Protective covers, desiccants
│   ├── 10-PRT-ST-001_Desiccant_Pack.md
│   ├── 10-PRT-ST-002_Protective_Cover_Wing.md
│   ├── 10-PRT-ST-003_Protective_Cover_Engine.md
│   ├── 10-PRT-ST-004_Pitot_Cover.md
│   └── 10-PRT-ST-005_Inlet_Plug_Set.md
│
├── fasteners-hardware/          # Specialized hardware
│   ├── 10-PRT-HW-001_Tiedown_Bolts.md
│   ├── 10-PRT-HW-002_Mooring_Shackles.md
│   ├── 10-PRT-HW-003_Quick_Release_Pins.md
│   └── 10-PRT-HW-004_Safety_Wire_Kit.md
│
├── consumables/                 # Preservation materials
│   ├── 10-PRT-CON-001_Preservation_Compound.md
│   ├── 10-PRT-CON-002_Corrosion_Inhibitor.md
│   └── 10-PRT-CON-003_Desiccant_Material.md
│
└── part-templates/              # Templates for part documentation
    ├── part-specification-template.md
    ├── part-approval-checklist.md
    └── part-obsolescence-template.md
```

---

## 3. Part Numbering Convention

### 3.1 Part ID Format

All parts follow this standardized numbering scheme:

```text
10-PRT-[CATEGORY]-[NNN]_[ShortName]
```

Where:
- **10** = ATA Chapter (Parking, Mooring, Storage & RTS)
- **PRT** = Part designator
- **CATEGORY** = Part category code (see below)
- **NNN** = Sequential number (001-999)
- **ShortName** = Descriptive name in PascalCase with underscores

### 3.2 Category Codes

| Category Code | Description | Example |
|---------------|-------------|---------|
| **TD** | Tiedown parts | 10-PRT-TD-001 |
| **MR** | Mooring parts | 10-PRT-MR-001 |
| **PK** | Parking parts | 10-PRT-PK-001 |
| **H2** | H2 system parts | 10-PRT-H2-001 |
| **ST** | Storage parts | 10-PRT-ST-001 |
| **HW** | Fasteners & hardware | 10-PRT-HW-001 |
| **CON** | Consumables | 10-PRT-CON-001 |

### 3.3 Document Naming

Part documents follow:

```text
[Part_ID]_[ShortName].md
```

**Examples:**
- `10-PRT-TD-001_Tiedown_Ring_Assy.md`
- `10-PRT-H2-001_H2_Vent_Valve_Assy.md`
- `10-PRT-PK-003_Ground_Lock_MLG.md`

---

## 4. Part Lifecycle Management

### 4.1 Part Status

Each part has a lifecycle status:

- **ACTIVE** - Current production or procurement part
- **OBSOLETE** - No longer used but not replaced
- **SUPERSEDED** - Replaced by a newer part (superseded_by field populated)
- **IN_DEVELOPMENT** - Part under design or qualification
- **FOR_REVIEW** - Part specification pending approval

### 4.2 Creating New Parts

1. **Assign Part ID**: Follow numbering convention; use next available number in category
2. **Create Document**: Use template from `part-templates/part-specification-template.md`
3. **Populate Metadata**: Fill all required fields including H2/cryo compatibility (if applicable)
4. **Add to Index**: Update `00_INDEX.md` with new part entry
5. **Review and Approve**: Submit for technical review and approval

### 4.3 Superseding Parts

When a part is superseded:

1. Update old part document:
   - Change status to `SUPERSEDED`
   - Add `superseded_by` field with new Part ID
   - Note supersession reason in revision history
2. Create new part document with improvements
3. Update all assemblies and BOMs referencing old part
4. Update `00_INDEX.md` to reflect changes

---

## 5. H2/Cryo Compatibility Requirements

### 5.1 H2-Compatible Parts

All parts in the **h2-system-parts/** category must include:

- **H2 Compatibility Rating**: Material compatibility with gaseous and liquid hydrogen
- **Cryogenic Rating**: Operating temperature range (especially -253°C for LH2)
- **Material Specification**: Materials proven compatible with hydrogen service
- **Hazmat Classification**: ATEX/IECEx zones if applicable
- **Safety Standards**: Compliance with SAE AS6968, NFPA 2, ISO 11114

### 5.2 H2-Compatible Materials

Preferred materials for H2 system parts:

- **Stainless Steel**: 316L, 304L (austenitic, no hydrogen embrittlement)
- **Aluminum Alloys**: 6061-T6, 5083 (suitable for cryogenic service)
- **Copper Alloys**: C10200, C12200 (oxygen-free copper for seals)
- **Polymers**: PTFE, PCTFE, Kel-F (low-temperature seals)
- **Insulation**: Multilayer insulation (MLI), aerogel blankets

### 5.3 Cryogenic Temperature Ranges

- **LH2 Operating**: -253°C (20K)
- **Cold Shock Test**: -269°C (4K) minimum for qualification
- **Storage Ambient**: -40°C to +85°C (outside operating envelope)

---

## 6. Applicable Standards

### 6.1 General Standards

- **ATA iSpec 2200** - Air Transport Association Information Standards
- **ATA 100** - Chapter 10: Parking, Mooring, Storage
- **S1000D** - International Specification for Technical Publications
- **ISO 9001** - Quality Management Systems

### 6.2 H2-Specific Standards

- **SAE AS6968** - Hydrogen Aircraft Ground Support Equipment
- **NFPA 2** - Hydrogen Technologies Code
- **ISO 11114** - Gas Cylinders - Compatibility of Cylinder and Valve Materials with Gas Contents
- **ISO 14687** - Hydrogen Fuel Quality - Product Specification
- **SAE AIR6464** - Composite Overwrapped Pressure Vessels for Hydrogen Storage

### 6.3 Cryogenic Standards

- **ASTM E1450** - Standard Test Method for Tensile Testing of Structural Alloys in Liquid Helium
- **ISO 20421** - Cryogenic Vessels - Large Transportable Vacuum-Insulated Vessels
- **ASME Section VIII** - Pressure Vessels (Division 1, 2, 3 for cryogenic service)

### 6.4 Safety and Hazmat

- **ATEX 2014/34/EU** - Equipment for Explosive Atmospheres (Europe)
- **IECEx** - International Electrotechnical Commission Explosive Atmospheres Certification
- **IATA DGR** - Dangerous Goods Regulations (for transportable parts)
- **49 CFR** - Hazardous Materials Regulations (USA)

---

## 7. Supplier and Procurement

### 7.1 Supplier Qualification

Suppliers for critical parts (especially H2 system parts) must:

- Demonstrate experience with aerospace-grade components
- Have quality management systems (ISO 9001, AS9100)
- Provide material certificates and test reports
- Support traceability requirements (batch/lot tracking)
- Comply with export control regulations (ITAR/EAR if applicable)

### 7.2 Procurement Data

Part documents include supplier information:

- Supplier name and CAGE code
- Manufacturer part number (for COTS)
- Lead time estimates
- Minimum order quantities
- Cost category (Low/Medium/High)

### 7.3 Interchangeability

When alternate parts exist:

- Document all approved alternates in part specification
- Verify form, fit, and function equivalence
- For H2 parts, verify identical H2/cryo compatibility
- Note any usage restrictions or limitations

---

## 8. Storage and Shelf Life

### 8.1 Storage Requirements

Each part document specifies:

- **Temperature range**: Ambient storage conditions
- **Humidity control**: RH% limits or desiccant requirements
- **Shelf life**: If applicable (especially consumables and seals)
- **Special handling**: Electrostatic discharge (ESD), clean room, etc.

### 8.2 Shelf Life Management

For parts with limited shelf life:

- Track expiration dates in inventory system
- Implement FIFO (First In, First Out) rotation
- Document shelf life extension procedures (if qualified)
- Note any periodic inspection or re-qualification requirements

---

## 9. Traceability and Documentation

### 9.1 Requirements Traceability

Each part document includes:

- **Related Requirements**: REQ-10-XXX IDs
- **Safety/Hazards**: Hazard analysis references
- **Design Constraints**: Operational domain (ODD) references

### 9.2 Related Documentation

Links to:

- **Related Drawings**: Drawing numbers and revisions
- **Related Models**: 3D model references in MODELS/
- **Related Assemblies**: Assembly IDs using this part
- **Related Specifications**: Material specs, test reports

### 9.3 Revision History

All part documents maintain revision history with:

- Revision identifier (A, B, C... or R01, R02, R03...)
- Date of revision
- Author/engineer responsible
- Description of changes

---

## 10. Usage and Integration

For detailed information on a specific part:

1. Navigate to the appropriate category folder
2. Open the part document (e.g., `10-PRT-H2-001_H2_Vent_Valve_Assy.md`)
3. Review specification, H2/cryo compatibility, and supplier data
4. Check related drawings and models in other ASSETS/ folders
5. Verify current status and revision level

For a complete parts list, see **[00_INDEX.md](00_INDEX.md)**.

For part documentation templates, see **part-templates/** folder.

---

## 11. Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**
- **Status**: DRAFT – Subject to human review and approval
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-09
- **Owner**: AMPEL360 Documentation WG
- **Standard**: OPT-IN Framework v1.1

---

**Notes:**
- This structure and README were generated by AI (prompted by Amedeo Pelliccia).
- All content must be reviewed and approved by designated personnel before official use.
- H2/cryo compatibility specifications are critical for safety and must be verified by qualified engineers.
