# 03-90-02-02A - H2 Piping Diagrams

## 1. Purpose

This document establishes standards for creating and maintaining hydrogen piping diagrams for Ground Support Equipment, covering both liquid (LH2) and gaseous (GH2) hydrogen piping systems with emphasis on safety, material compatibility, and operational requirements.

## 2. Scope

This specification covers H2 piping diagrams for:
- LH2 vacuum-insulated piping systems
- GH2 ambient temperature piping systems
- Transfer hose assemblies and connections
- Purge and vent piping
- Sample and instrumentation tubing
- Pipe supports and expansion systems

## 3. Applicable Documents

- [ASME B31.3](https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping) - Process Piping
- [ASME B31.12](https://www.asme.org/codes-standards/find-codes-standards/b31-12-hydrogen-piping-pipelines) - Hydrogen Piping and Pipelines
- [CGA G-5.4](https://www.cganet.com/) - Standard for Hydrogen Piping Systems
- [ISO 21013](https://www.iso.org/standard/71940.html) - Cryogenic Vessels - Pressure Relief Accessories
- [EN 13480](https://www.en-standard.eu/bs-en-13480-3-2017-metallic-industrial-piping-design-and-calculation/) - Metallic Industrial Piping
- [ISO/TR 15916](https://www.iso.org/standard/29316.html) - Basic Considerations for Safety of Hydrogen Systems

## 4. Documentation Description

### 4.1 Overview

H2 piping diagrams provide essential information for:
- Design verification and approval
- Installation and construction
- Pressure testing and commissioning
- Operations and maintenance
- Safety assessments and audits
- Regulatory compliance documentation

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Drawing Scale | 1:50, 1:100, 1:200 typical | ISO 5457 |
| Line Weights | 0.25mm (small), 0.5mm (main), 0.7mm (heavy) | ISO 128 |
| Dimensioning | Millimeters primary | ISO 129 |
| Isometric Views | 30° angles | ASME Y14.3 |
| Symbology | ISA-5.1 compliant | [03-90-01-03A](../03-90-01_GSE_Documentation_Standards/03-90-01-03A_Symbology_Standards.md) |

### 4.3 Content Requirements

#### 4.3.1 Piping Specifications

**LH2 Piping Systems:**

| Attribute | Specification | Notes |
|-----------|---------------|-------|
| Material | 300 series stainless steel (304, 304L, 316, 316L) | H2 embrittlement resistant |
| Design Temperature | -253°C to +65°C | Full cryogenic range |
| Design Pressure | 25 bar typical (varies by application) | With safety factor |
| Insulation | Vacuum jacketed or multilayer | Heat leak minimization |
| Connections | Welded or flanged | No threaded connections in LH2 |
| Cleanliness | Oxygen-clean per CGA G-4.1 | Prevents contamination |

**GH2 Piping Systems:**

| Attribute | Specification | Notes |
|-----------|---------------|-------|
| Material | 316/316L stainless steel preferred | High strength, H2 compatible |
| Design Temperature | -40°C to +85°C | Ambient + margin |
| Design Pressure | 200-450 bar typical | High pressure applications |
| Wall Thickness | Per ASME B31.12 calculations | Including corrosion allowance |
| Connections | Welded (preferred) or high-pressure fittings | Minimize leak paths |
| Pressure Class | ANSI 600, 900, 1500, 2500 | Based on system pressure |

#### 4.3.2 Piping Layout Requirements

**Plan Views:**
- North arrow and scale
- Equipment locations with tags
- Pipe routing with dimensions from reference points
- Elevation changes indicated
- Valve locations with tags
- Support locations
- Clearance zones and access areas

**Isometric Views:**
- 3D representation of pipe routing
- All fittings shown (elbows, tees, reducers)
- Weld joints numbered
- Flange connections identified
- Instrument connections shown
- Slope indicators for drainage
- Support types and locations

**Section Views:**
- Critical areas requiring detailed view
- Underground/buried piping
- Pipe penetrations through walls/floors
- Complex fitting assemblies
- Valve installations

#### 4.3.3 Pipe Identification

**Line Numbering System:**

Format: `XXX-YY-NNN-ZZ-S`

Where:
- **XXX**: Fluid code (LH2, GH2, VNT, PUR)
- **YY**: Nominal pipe size (inches or DN)
- **NNN**: Line sequence number
- **ZZ**: Piping class/pressure rating
- **S**: Insulation type (V=vacuum, M=multilayer, N=none)

**Examples:**
- `LH2-03-001-25-V`: 3" LH2 line, sequence 001, 25 bar, vacuum insulated
- `GH2-02-045-200-N`: 2" GH2 line, sequence 045, 200 bar, not insulated
- `VNT-06-010-10-N`: 6" vent line, sequence 010, 10 bar, not insulated

#### 4.3.4 Valve Specifications

**Valve Schedule Table (on drawings):**

| Tag | Type | Size | Rating | Material | Actuation | Notes |
|-----|------|------|--------|----------|-----------|-------|
| VBV-101 | Ball | DN50 | PN25 | 316L SS | Manual | LH2 service |
| VXV-201 | ESV | DN80 | PN25 | 316L SS | Pneumatic | Emergency shutoff |
| VRV-045 | Relief | DN20 | Set 20 bar | 316 SS | Spring | Primary relief |

**Valve Details Required:**
- Face-to-face dimensions
- Operator type and orientation
- Stem extension (for cryogenic service)
- Position indication (if applicable)
- Locking provisions (if required)

#### 4.3.5 Instrumentation Connections

**Instrument Tap Details:**

| Connection | Type | Size | Notes |
|------------|------|------|-------|
| Pressure | Socket weld or compression | 1/4" or 1/2" typical | Root valves required |
| Temperature | Thermowell | Per sensor size | Insertion length specified |
| Flow | Flanged or welded | Per meter size | Straight run requirements |
| Level | Socket weld | 1/2" typical | Elevation critical |
| Sample | Compression fittings | 1/4" tubing | Purge/drain provisions |

**Tubing Specifications:**
- Material: 316/316L stainless steel
- Size: 1/4" or 1/2" OD typical
- Wall thickness: 0.035" or 0.065"
- Fittings: Compression or tube fittings (Swagelok or equivalent)

#### 4.3.6 Pipe Supports and Restraints

**Support Types:**

| Type | Application | Typical Spacing |
|------|-------------|-----------------|
| Rigid Hanger | Vertical support | Per stress analysis |
| Adjustable Hanger | Alignment during installation | As needed |
| Cryogenic Support | LH2 lines | Minimize heat transfer |
| Expansion Loop | Thermal expansion | Per calculation |
| Anchor | Fixed point | Movement restraint |
| Guide | Directional restraint | Per design |

**Support Details Required:**
- Support tag number
- Load capacity
- Attachment method
- Insulation considerations
- Access for maintenance

#### 4.3.7 Expansion Joints and Flexible Connections

**Expansion Provisions:**

| Type | Application | Movement Capacity |
|------|-------------|-------------------|
| Expansion Loop | LH2 piping | Calculated per thermal contraction |
| Metal Bellows | Limited space | ±25mm typical |
| Flexible Hose | Transfer lines | Per hose specification |
| Slip Joint | GH2 ambient piping | ±50mm typical |

**Design Requirements:**
- Thermal contraction calculation (approx. 0.3% for LH2)
- Pressure thrust forces
- Guided movement path
- Limit stops
- Leak detection provisions

#### 4.3.8 Drainage and Venting

**Drain Points:**
- Low points in piping systems
- Before isolation valves
- At equipment connections
- Drain valve specifications
- Drain collection/disposal method

**Vent Points:**
- High points in piping systems
- After isolation valves
- During filling operations
- Vent line sizing (per CGA G-5.5)
- Vent discharge location and height

#### 4.3.9 Piping Penetrations

**Wall/Floor Penetrations:**
- Sleeve specifications
- Fire-rated sealant (if required)
- Clearances for thermal movement
- Seismic considerations
- Identification both sides

**Underground/Buried Piping:**
- Depth of cover
- Bedding and backfill specifications
- Corrosion protection (if applicable)
- Warning tape or markers
- Cathodic protection (if used)

### 4.4 Material Specifications

**Pipe Materials:**

| Service | Material Grade | Specification |
|---------|----------------|---------------|
| LH2 | 304L, 316L SS | ASTM A312 |
| GH2 (low P) | 304, 316 SS | ASTM A312 |
| GH2 (high P) | 316, 316L SS | ASTM A312 |
| Fittings | Same as pipe | ASTM A403 |
| Flanges | Same as pipe | ASTM A182 |
| Bolting | A193 B8M | ASTM A193 |
| Gaskets | Spiral wound, graphite fill | ASME B16.20 |

**Welding Requirements:**
- Procedure: ASME Section IX qualified
- Inspection: 100% visual, RT or UT per code
- Heat treatment: As required by code
- Cleanliness: Cleaned after welding

### 4.5 Pressure Testing Requirements

**Hydrotest (if applicable):**
- Test pressure: 1.5 × design pressure
- Duration: Per ASME B31.3
- Medium: Water or inert gas (N2)
- Documentation: Test certificate required

**Pneumatic Test (preferred for H2 service):**
- Test medium: Nitrogen or helium
- Test pressure: 1.1 × design pressure
- Leak test: Helium mass spectrometry
- Acceptance: < 10⁻⁶ mbar·L/s

**Cryogenic Test (for LH2):**
- Test medium: Liquid nitrogen (LN2)
- Cold shock test
- Leak test at operating temperature
- Insulation performance verification

### 4.6 Safety Considerations

**Hazardous Area Classification:**
- Zone 0, 1, 2 per IEC 60079
- Extent of zones on drawings
- Electrical equipment specifications
- Ignition source control

**Emergency Isolation:**
- Emergency shutoff valve (ESV) locations
- Actuation method (fail-safe)
- Manual backup provisions
- Position indication (remote)

**Fire Protection:**
- Fire detection points
- Fire suppression (if applicable)
- Fire-resistant coatings/wraps
- Passive fire protection

## 5. Cross-References

- Related ATA Chapters: ATA 12 (Servicing), ATA 28 (Fuel)
- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-02-01A LH2 System Schematics](./03-90-02-01A_LH2_System_Schematics.md)
  - [03-90-02-03A Cryogenic Flow Diagrams](./03-90-02-03A_Cryogenic_Flow_Diagrams.md)
  - [03-90-04 Mechanical Drawings](../03-90-04_Mechanical_Drawings/README.md)
  - [03-90-06-02A H2 Equipment Specs](../03-90-06_Specification_Tables/03-90-06-02A_H2_Equipment_Specs.md)

## 6. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 H2 Systems Engineering | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-08.

---
