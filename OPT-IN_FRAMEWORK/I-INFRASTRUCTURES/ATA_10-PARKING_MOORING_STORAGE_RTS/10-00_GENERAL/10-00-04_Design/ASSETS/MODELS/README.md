# ATA 10 — MODELS Directory

## Purpose

This directory manages **3D CAD models, assemblies, components, and simulations** for the AMPEL360-BWB-H2 aircraft Parking, Mooring, Storage, and Return to Service (RTS) systems. It provides a comprehensive structure for managing design models with special considerations for:

- **Blended Wing Body (BWB)** configuration
- **Hydrogen (H2)** fuel system safety requirements
- **Advanced parking and mooring systems**

## Directory Structure Overview

```
MODELS/
├── cad-native/           # Native CAD files (CATIA, SolidWorks, NX)
├── exchange-formats/     # Neutral formats (STEP, IGES, JT)
├── visualization/        # Lightweight visualization formats (STL, OBJ, glTF)
├── assemblies/           # Assembly-level model documentation
├── components/           # Component-level model documentation
│   ├── tiedown/         # Tiedown system components
│   ├── mooring/         # Mooring system components
│   ├── parking/         # Parking system components
│   └── h2-systems/      # H2 safety equipment components
├── simulations/          # Simulation model documentation
│   ├── fea/             # Finite Element Analysis
│   └── cfd/             # Computational Fluid Dynamics
└── model-templates/      # Templates for model documentation
```

## File Organization

### 1. CAD Native Files (`cad-native/`)

Source CAD files organized by CAD system:

- **CATIA** (`catia/`): CATIA V5/V6 native files (`.CATPart`, `.CATProduct`)
- **SolidWorks** (`solidworks/`): SolidWorks native files (`.sldprt`, `.sldasm`)
- **NX** (`nx/`): Siemens NX native files (`.prt`)

**Storage Guidelines:**
- Store master CAD files here with proper version control
- Include assembly trees and part files
- Use Git LFS for large binary CAD files
- Maintain CAD system version metadata

### 2. Exchange Formats (`exchange-formats/`)

Neutral CAD formats for interoperability:

- **STEP** (`step/`): ISO 10303 STEP files (`.step`, `.stp`) - preferred for long-term archival
- **IGES** (`iges/`): IGES format files (`.igs`, `.iges`) - legacy compatibility
- **JT** (`jt/`): JT Open format (`.jt`) - lightweight visualization and collaboration

**Export Guidelines:**
- Export from native CAD at major milestones
- Use STEP AP242 for complete model data
- Include metadata in STEP header
- Verify geometry integrity after export

### 3. Visualization Formats (`visualization/`)

Lightweight formats for visualization and web display:

- **STL** (`stl/`): Stereolithography files (`.stl`) - for 3D printing and basic visualization
- **OBJ** (`obj/`): Wavefront OBJ files (`.obj`, `.mtl`) - with materials and textures
- **glTF** (`gltf/`): GL Transmission Format (`.gltf`, `.glb`) - web-optimized 3D

**Usage:**
- Generate from STEP or native CAD
- Optimize polygon count for intended use
- Include in documentation and web viewers

### 4. Assemblies (`assemblies/`)

Top-level assembly documentation for major systems:

- `10-MDL-ASM-001_BWB_Parking_Configuration.md` - BWB-specific parking configuration
- `10-MDL-ASM-002_Tiedown_System_Assembly.md` - Complete tiedown system
- `10-MDL-ASM-003_Mooring_Equipment_Assembly.md` - Mooring equipment assembly
- `10-MDL-ASM-004_H2_Safety_Equipment_Assembly.md` - H2 safety equipment assembly

### 5. Components (`components/`)

Component-level model documentation organized by subsystem:

**Tiedown (`tiedown/`):**
- Tiedown rings, fittings, and ground anchors
- Load-bearing attachment points

**Mooring (`mooring/`):**
- Mooring masts, cables, and clamps
- Wind restraint systems

**Parking (`parking/`):**
- Wheel chocks, ground locks, parking brake locks
- Ground handling equipment interfaces

**H2 Systems (`h2-systems/`):**
- H2 vent valves and detector housings
- Cryogenic insulation covers
- Safety equipment specific to hydrogen operations

### 6. Simulations (`simulations/`)

Simulation model documentation and results:

**FEA (`fea/`):**
- Structural analysis of tiedown and mooring loads
- Stress analysis and fatigue calculations
- Material property verification

**CFD (`cfd/`):**
- H2 dispersion analysis for safety scenarios
- Ventilation flow analysis
- Wind load analysis for mooring

### 7. Model Templates (`model-templates/`)

Standardized templates for model documentation:

- `model-specification-template.md` - Template for model specifications
- `model-release-checklist.md` - Checklist for releasing models
- `model-validation-template.md` - Template for model validation

## Naming Conventions

All model files follow the AMPEL360 Assets Standard:

```
10-MDL-<TYPE>-<nnn>_<Descriptive_Name>.<ext>
```

**Type Codes:**
- `ASM` - Assembly
- `TD` - Tiedown component
- `MR` - Mooring component
- `PK` - Parking component
- `H2` - H2 system component
- `SIM` - Simulation model

**Examples:**
```
10-MDL-ASM-001_BWB_Parking_Configuration.md
10-MDL-TD-001_Tiedown_Ring.md
10-MDL-H2-001_H2_Vent_Valve.md
10-SIM-FEA-001_Tiedown_Load_Analysis.md
```

## Supported CAD Systems and Formats

### Primary CAD Systems
- **CATIA V5/V6** - Primary for complex surfaces and assemblies
- **SolidWorks** - Primary for mechanical components
- **Siemens NX** - Advanced simulation integration

### Exchange Formats
- **STEP AP242** (ISO 10303-242) - Long-term archival, recommended
- **IGES 5.3** - Legacy compatibility
- **JT Open** - Lightweight collaboration

### Visualization Formats
- **STL** - 3D printing, basic visualization
- **OBJ + MTL** - Rendering with materials
- **glTF 2.0** - Web-based 3D viewers

## Model Management Workflow

### 1. Model Creation
1. Create model in primary CAD system
2. Follow naming conventions
3. Apply metadata and properties
4. Save to appropriate `cad-native/` subdirectory

### 2. Export and Archive
1. Export to STEP format (AP242 preferred)
2. Save to `exchange-formats/step/`
3. Generate visualization formats as needed
4. Update model documentation

### 3. Documentation
1. Create model documentation using template
2. Include metadata: dimensions, weight, materials
3. Link to related drawings and requirements
4. Reference applicable standards

### 4. Validation
1. Verify geometry integrity
2. Check material properties
3. Validate against requirements
4. Complete validation template

### 5. Release
1. Complete release checklist
2. Obtain required approvals
3. Update INDEX and metadata
4. Archive previous versions

## BWB Configuration Considerations

The Blended Wing Body configuration requires special attention for:

- **Wingspan**: Extended wingspan affects parking envelope and clearances
- **Footprint**: Non-traditional aircraft footprint requires custom parking layouts
- **Ground Clearance**: Different ground clearance affects equipment positioning
- **Wing-Body Integration**: Structural load paths through integrated wing-body
- **Access Points**: Non-standard access for ground equipment

## H2 System Considerations

Hydrogen fuel systems introduce specific requirements:

- **H2 Venting**: Safe venting systems for hydrogen gas
- **Detection**: H2 leak detection equipment and housings
- **Cryogenic Protection**: Insulation for cryogenic fuel systems
- **Safety Zones**: Exclusion zones during fueling and venting
- **Fire Suppression**: Specialized fire suppression equipment
- **Grounding**: Electrical grounding for static discharge

## Related Standards and References

### Aviation Standards
- **ATA iSpec 2200** - Information Standards for Aviation Maintenance
- **ATA 100 Chapter 10** - Parking, Mooring, Storage & RTS
- **CS-25** / **FAR Part 25** - Airworthiness Standards (Large Aircraft)
- **CS-25 Subpart D** - Design and Construction

### Hydrogen Safety
- **SAE AS6968** - Hydrogen Aircraft Systems
- **ISO 14687** - Hydrogen fuel quality
- **SAE AIR7901** - Hydrogen propulsion for aircraft

### CAD and Data Exchange
- **ISO 10303** (STEP) - Product Data Representation and Exchange
  - **AP203** - Configuration controlled 3D design
  - **AP214** - Automotive design
  - **AP242** - Managed model-based 3D engineering
- **LOTAR** - Long-term Archiving and Retrieval
- **MIL-STD-31000** - Technical Data Packages

### Quality and Configuration Management
- **AS9100** - Quality Management Systems for Aviation
- **ISO 9001** - Quality Management
- **MIL-STD-973** - Configuration Management

## Model Data Management

### Version Control
- Use Git for documentation and small CAD files
- Use Git LFS for large binary CAD files
- Tag releases with version numbers
- Maintain change logs

### Metadata
- Store metadata in `model-metadata.schema.json` format
- Include: model ID, version, author, date, status
- Link to requirements and drawings
- Track approvals and reviews

### Traceability
- Link models to requirements (REQ-10-XXX)
- Reference related drawings (10-00-04-AXXX)
- Cross-reference assemblies and components
- Maintain Bill of Materials (BOM)

## Access and Permissions

- **CAD Native Files**: Restricted to design engineers
- **Exchange Formats**: Available to authorized teams
- **Visualization**: Broadly available for review
- **Documentation**: Public within project

## Tools and Software

### CAD Software
- CATIA V5/V6 or later
- SolidWorks 2020 or later
- Siemens NX 12 or later

### Exchange and Validation
- STEP Tools, Inc. - STEP validation
- CAD Exchanger - Format conversion
- Open CASCADE - STEP/IGES processing

### Simulation
- ANSYS - FEA/CFD analysis
- Abaqus - Advanced FEA
- STAR-CCM+ - CFD for H2 dispersion

### Visualization
- Blender - STL/OBJ/glTF export
- MeshLab - Mesh processing
- Three.js - Web-based 3D viewers

## Quality Assurance

All models must:
1. Pass geometry validation checks
2. Include complete metadata
3. Be linked to requirements
4. Have documented validation
5. Receive required approvals
6. Be archived in neutral format (STEP)

## Support and Contact

For questions about model management:
- **Technical Lead**: AMPEL360 Design Team
- **CAD Standards**: Configuration Management
- **H2 Systems**: Safety Engineering

---

## Document Control

- **Document ID**: 10-00-04-MODELS-README
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-12-09
- **Owner**: AMPEL360 ATA 10 Design Team
- **Repository**: AMPEL360-BWB-H2-Hy-E
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.

---

**See Also:**
- [00_INDEX.md](./00_INDEX.md) - Complete model inventory
- [model-metadata.schema.json](./model-metadata.schema.json) - Metadata schema
- [AMPEL360_ASSETS_STANDARD.md](../../../../../../../AMPEL360_ASSETS_STANDARD.md) - Asset naming standards
