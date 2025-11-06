# Digital Twin Geometry Model

**Document ID:** AMPEL360-02-11-00-DES-RS-005  
**Version:** 1.0.0

## Overview

**Purpose:** Define the digital representation of aircraft geometry for design, analysis, manufacturing, and lifecycle management.

## Digital Twin Architecture

### Master Geometry Model

**CAD System:** CATIA V6 (primary), Siemens NX (secondary)

**Model Structure:**
- Top assembly: Complete aircraft
- Major sections: 3 (forward, center, aft)
- Sub-assemblies: 150+ major assemblies
- Parts: 12,000+ unique parts

**File Format:**
- Native: CATIA V6 (.CATPart, .CATProduct)
- Exchange: STEP AP242 (ISO 10303-242)
- Neutral: IGES (legacy compatibility)
- Visualization: JT format

### Coordinate System

**Origin:** Datum point (FS 15000, BL 0, WL 5000)

**Axes:**
- X-axis: Positive aft (0° reference)
- Y-axis: Positive right (90°)
- Z-axis: Positive down (270°)

**Units:** Millimeters (all dimensions)

## Model Hierarchy

### Level 1: Aircraft Assembly

**Components:**
- Forward section (FS 0-10000)
- Center section (FS 10000-20000)
- Aft section (FS 20000-28500)
- Wings (integrated with sections)

### Level 2: Major Assemblies

**Examples:**
- Pressure vessel structure
- Wing box assembly
- Landing gear installation
- H₂ tank system
- Flight control surfaces

### Level 3: Sub-Assemblies

**Examples:**
- Frame assemblies
- Rib assemblies
- Panel assemblies
- Systems installations

### Level 4: Detail Parts

**Examples:**
- Skins
- Stringers
- Fittings
- Fasteners

## Geometry Data

### Surfaces

**OML (Outer Mold Line):**
- Definition: Complete external surface
- Accuracy: ±0.1mm (Class A surfaces)
- Format: NURBS surfaces
- Continuity: G2 (curvature continuous)

**IML (Inner Mold Line):**
- Definition: Internal surfaces (cabin, tanks, etc.)
- Accuracy: ±0.5mm
- Format: NURBS surfaces
- Continuity: G1 (tangent continuous)

### Structure

**Wing Box:**
- Spars: 3D solid models
- Ribs: Sheet metal/composite definitions
- Skins: Composite layup definitions
- Fasteners: Simplified representations

**Frames and Stringers:**
- Profiles: Parametric definitions
- Spacing: Design values (600mm frames, 200mm stringers)
- Material: Specified per part
- Orientation: Perpendicular to local surface

## Analysis Models

### FEM (Finite Element Model)

**Source:** CAD geometry (automated)

**Mesh:**
- Elements: 5M+ (global model)
- Type: Shell, solid, beam elements
- Size: 25mm (typical)
- Refinement: 5mm (critical areas)

**Properties:**
- Material: Composite layup or isotropic
- Thickness: As-designed
- Connections: Rigid, flexible, or contact
- Loads: Distributed or point loads

### CFD (Computational Fluid Dynamics)

**Source:** OML geometry (water-tight)

**Mesh:**
- Cells: 10M+ (cruise analysis)
- Type: Tetrahedral, prism layers
- Boundary layer: 20 layers (y+ < 1)
- Domain: Extended far-field

**Conditions:**
- Flight conditions: M0.82, 41,000 ft
- Turbulence: k-ω SST model
- Heat transfer: Conjugate (if required)

## Manufacturing Data

### Tooling Geometry

**Master Tools:**
- Quantity: 3 major tools (section assemblies)
- Definition: CAD models (reverse OML)
- Tolerance: ±0.5mm (tool surface)
- Material: Invar (thermal stability)

**Assembly Fixtures:**
- Type: Determinant assembly
- Locating points: 3-2-1 principle
- Clamping: Vacuum or mechanical
- Verification: CMM check

### Composite Layup

**Ply Books:**
- Source: CAD geometry (surfaces)
- Layers: Up to 50 plies (wing box)
- Orientation: Fiber angles specified
- Thickness: Per ply (0.125mm typical)

**Automated Fiber Placement:**
- Path planning: CAD-based
- Coverage: 95% (AFP), 5% (hand layup)
- Quality: Laser projection verification

## As-Built Data Integration

### Measurement Data

**Source:** Laser tracker, CMM, photogrammetry

**Format:** Point clouds, discrete measurements

**Integration:**
- Comparison: CAD vs. measured
- Deviation: Color maps (visualization)
- Acceptance: Tolerance-based
- Update: Model adjusted if needed

### Serial Number Tracking

**Part Level:**
- Serial number: Unique per part
- Location: Coordinate-based
- History: Installation, removal, repair
- Traceability: Full lifecycle

### Configuration Management

**Baseline:**
- Version: 1.0.0 (frozen 2024-04-01)
- Changes: CCB approval required
- Documentation: Full revision history
- Traceability: Change requests linked

## Operational Digital Twin

### Maintenance Planning

**Access:**
- Model: Used for maintainability analysis
- Procedures: Developed from model
- Tooling: Designed using model
- Training: VR/AR from model

### Damage Assessment

**Incident:**
- Location: Coordinate-based
- Extent: Modeled in digital twin
- Analysis: FEM of damaged structure
- Repair: Planned using model

### Modifications

**Engineering Changes:**
- Design: In digital twin
- Analysis: Using updated model
- Approval: Based on analysis
- Implementation: Guided by model

## Data Management

### PLM System

**Software:** Siemens Teamcenter

**Functions:**
- Version control: Automatic
- Change management: Workflow
- BOM management: Integrated
- Access control: Role-based

### Backup and Archive

**Frequency:**
- Daily: Incremental backup
- Weekly: Full backup
- Monthly: Archive to tape
- Annual: Permanent archive

**Retention:**
- Active design: Unlimited
- Superseded: 10 years
- As-built: Aircraft lifetime + 20 years

## Certification Data

**Type Certificate:**
- Geometry: Fully defined in digital twin
- Validation: Physical measurements
- Conformity: Documented
- Approval: Regulatory authority

**Status:** Digital twin operational  
**Version:** 1.0.0  
**Frozen:** 2024-04-01  
**Approved:** 2024-02-15
