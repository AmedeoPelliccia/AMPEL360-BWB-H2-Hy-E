# 53-00-04-01-004: Manufacturing Considerations – AMPEL360 BWB Fuselage

## 1. Overview

This document outlines manufacturing considerations that influence the structural design of the AMPEL360 BWB fuselage. Understanding manufacturing constraints and capabilities during the design phase ensures producibility and cost-effectiveness.

## 2. Design for Manufacturing (DFM) Philosophy

### 2.1 Core Principles
- **Manufacturability from Day One**: Consider manufacturing in all design decisions
- **Minimize Complexity**: Simplify where possible without compromising performance
- **Standard Processes**: Use proven manufacturing methods
- **Tolerance Management**: Design for achievable and economical tolerances
- **Assembly-Friendly**: Design for efficient assembly and integration
- **Inspection Access**: Enable quality control and NDI

### 2.2 DFM Process Integration
- Manufacturing review at all design milestones (PDR, CDR)
- Manufacturing representation on design teams
- Early prototyping of critical features
- Manufacturing feasibility analysis before design freeze

## 3. Composite Manufacturing

### 3.1 Automated Fiber Placement (AFP)

**Description**: Computer-controlled robotic placement of composite tapes.

**Advantages**:
- High repeatability and quality
- Complex contours capability
- Reduced labor cost for large panels
- Fiber steering optimization
- Consistent compaction pressure

**Design Considerations**:
- **Minimum radius**: Typically 75-100 mm for standard AFP heads
- **Access**: Require line-of-sight for AFP head
- **Ply drops**: Design for gradual thickness transitions
- **Steering limits**: Maximum fiber angle change ~5°/inch
- **Tow width**: Standard 1/4" (6.35 mm) or 1/8" (3.175 mm)

**Applications**:
- Large fuselage skins (upper and lower)
- Wing spars and skins
- Frames and stringers

**Process Parameters**:
- Layup rate: ~4-10 kg/hr per head
- Multiple heads increase throughput
- Typical layup accuracy: ±0.5 mm

### 3.2 Hand Layup

**Description**: Manual placement of prepreg plies.

**Advantages**:
- Flexibility for complex geometries
- No special equipment for small quantities
- Access to tight spaces
- Suitable for repairs

**Design Considerations**:
- Labor-intensive (high cost for large areas)
- Operator skill-dependent quality
- Suitable for <10 m² areas
- Good for tight radii and complex contours

**Applications**:
- Complex fittings and brackets
- Localized repairs
- Prototype structures
- Small production quantities

### 3.3 Autoclave Curing

**Description**: Consolidation and cure of composite parts under heat and pressure.

**Advantages**:
- Highest quality (low void content <1%)
- Proven process with extensive database
- Good for structural primary parts

**Design Considerations**:
- **Autoclave size limits**: Typical large autoclaves
  - Diameter: 6-9 m
  - Length: 18-30 m
  - Maximum part size constrained
- **Cure cycle**: Typically 6-8 hours
- **Tooling cost**: High-temperature tools required
- **Throughput**: Limited by cycle time

**Applications**:
- Primary structure skins
- Wing spars
- Critical structural components

**Typical Cure Cycle** (IM7/8552):
- Heat to 180°C at ~2-3°C/min
- Hold at 180°C for 120 min
- Pressure: 0.59-0.69 MPa (85-100 psi)
- Vacuum bag consolidation

### 3.4 Out-of-Autoclave (OOA) Curing

**Description**: Cure under vacuum bag only, no autoclave pressure.

**Advantages**:
- Lower tooling cost (no high-pressure capability needed)
- Larger parts possible (no autoclave size limit)
- Lower capital investment
- Suitable for large fuselage sections

**Design Considerations**:
- Slightly lower mechanical properties than autoclave (typically 5-10%)
- Require careful vacuum bag technique
- Void content control more critical
- Limited to specific resin systems

**Applications**:
- Large fuselage barrel sections
- Secondary structure
- Non-critical panels

### 3.5 Resin Transfer Molding (RTM)

**Description**: Dry fiber preforms infused with resin under pressure.

**Advantages**:
- High-volume production capability
- Good surface finish (both sides)
- Lower material cost (no prepreg storage)
- Complex 3D shapes

**Design Considerations**:
- Tooling cost high (matched dies)
- Fiber volume fraction control
- Resin flow design critical
- Suitable for high production rates

**Applications**:
- Frames and ribs (potential)
- Smaller repeated components
- Future production rate increase

## 4. Metallic Manufacturing

### 4.1 Machining (Aluminum, Titanium)

**Design Considerations**:
- **Wall thickness**: Minimum practical
  - Aluminum: 1.5-2.0 mm
  - Titanium: 2.0-2.5 mm
- **Fillet radii**: R3-R5 mm minimum (tool access)
- **Pocket depth**: Limit to 3× tool diameter
- **Material removal**: Minimize (cost, time)
- **Access for tools**: Consider tool clearance

**Cost Drivers**:
- Machining time (especially titanium)
- Material buy-to-fly ratio (minimize scrap)
- Tool wear (carbide inserts)
- Surface finish requirements

**Applications**:
- Fittings and brackets
- Gear bay beams
- Floor beams
- Seat tracks

### 4.2 Forming (Aluminum)

**Design Considerations**:
- **Bend radii**: Minimum 2-3× thickness
- **Springback**: Design for compensation
- **Stretch forming**: For compound curves
- **Limited to moderate complexity**

**Applications**:
- Floor beam angles
- Simple brackets
- Sheet metal panels

### 4.3 Casting (Titanium)

**Description**: Investment casting for complex titanium fittings.

**Advantages**:
- Near-net shape
- Complex geometries possible
- Reduced machining
- Material savings

**Design Considerations**:
- Wall thickness: 3-5 mm minimum
- Draft angles: 2-5° for removal
- Undercuts avoided
- Finish machining required for critical surfaces
- Lead time: 12-16 weeks typical

**Applications**:
- Wing attachment fittings
- Landing gear beam connections
- Complex high-load fittings

## 5. Joining and Assembly

### 5.1 Mechanical Fastening

**Fastener Types**:
- **Hi-Lok**: Tension fasteners, interference fit
- **Lockbolts**: For high-load joints
- **Rivets**: Secondary structure, low-load
- **Specialty**: Blind fasteners for limited access

**Design Considerations**:
- **Edge distance**: Minimum 2.5× diameter
- **Pitch**: 4-6× diameter typical
- **Countersink depth**: 65-70% of sheet thickness maximum
- **Hole tolerance**: ±0.05 mm for interference fit
- **Installation access**: Consider rivet gun clearance
- **Shimming**: Provide for tolerance buildup (0.5-2.0 mm typical)

**Drilling**:
- CNC drilling for precision and repeatability
- Drill-to-assemble process (no reaming)
- Hole quality critical for fatigue

### 5.2 Bonding

**Adhesive Types**:
- **FM 300 (Epoxy film)**: Structural bonding, 120-180°C cure
- **EA 9396 (Paste)**: Gap-filling, room temp or elevated temp cure
- **AF 163 (Film)**: High-temperature applications

**Design Considerations**:
- **Overlap length**: Minimum 12-15 mm for lap joints
- **Bond thickness**: 0.1-0.3 mm (controlled by adhesive)
- **Surface preparation**: Grit blast or peel ply, critical
- **Cure temperature**: Must be compatible with substrate
- **Fillet**: Design for consistent adhesive fillet
- **Inspection**: Limited NDI capability (requires careful process control)

**Applications**:
- CFRP skin-to-stringer bonding
- Secondary structure bonding
- Doubler installation

### 5.3 Co-Bonding and Co-Curing

**Co-Bonding**: Bonding cured part to uncured part, then cure together.
**Co-Curing**: Curing multiple parts together in single cure cycle.

**Advantages**:
- Reduced part count
- Lower assembly cost
- Excellent bond quality
- Eliminates fasteners in some areas

**Design Considerations**:
- **Thermal expansion matching**: CTE compatibility critical
- **Tooling complexity**: More complex fixtures
- **Cure cycle compatibility**: All parts must use same cycle
- **Inspection**: Before cure only (no second chance)

**Applications**:
- Skins with co-cured stringers
- Frames with co-bonded doublers
- Complex integrated structures

## 6. Tooling Considerations

### 6.1 Composite Tooling

**Tool Types**:
- **Invar (Nickel-Iron alloy)**: Low CTE, expensive
- **Steel**: Durable, moderate CTE
- **Composite Tools**: For moderate temperature, large size
- **Aluminum**: Lower cost, limited reuse

**Design Considerations**:
- Tool CTE must match part CTE
- Tool surface finish drives part surface quality
- Vacuum port locations
- Heating (embedded heaters or external)
- Handling and storage provisions
- Maintenance and inspection

**Tool Life**:
- Invar/Steel: 100-500 cure cycles
- Composite: 20-50 cure cycles

### 6.2 Assembly Fixtures

**Design Considerations**:
- Locating features (tooling holes, datums)
- Clamp and support locations
- Adjustment capability for tolerance variation
- Ergonomics for workers
- Tool access for fastener installation

### 6.3 Tooling Cost and Lead Time

| Tool Type | Typical Cost | Lead Time |
|-----------|--------------|-----------|
| Large autoclave tool (Invar) | $1-3M | 12-18 months |
| Medium tool (steel) | $200-500k | 6-9 months |
| Assembly fixture | $50-200k | 3-6 months |
| Small composite tool | $20-50k | 2-3 months |

## 7. Tolerance Management

### 7.1 Manufacturing Tolerances

**CFRP Parts**:
- Ply thickness: ±10% typical
- Part dimensions: ±1-2 mm (uncured)
- After cure dimensional change: 0.5-1.5%
- Surface waviness: ±0.5 mm per 300 mm

**Metal Parts**:
- Machined dimensions: ±0.1-0.25 mm
- Formed dimensions: ±1-2 mm
- Cast dimensions: ±1-3 mm

### 7.2 Assembly Tolerance Stackup

**Design Strategy**:
- Identify critical interfaces
- Perform tolerance stackup analysis
- Provide shimming provisions (0.5-2.0 mm range)
- Use adjustable fittings where practical
- Drill-to-assemble for hole alignment

**Key Interfaces**:
- Wing-to-fuselage attachment
- Landing gear beam attachment
- Door frame installation

## 8. Non-Destructive Inspection (NDI)

### 8.1 Inspection Methods

**Ultrasonic Testing (UT)**:
- Detects voids, delaminations, porosity
- Through-transmission or pulse-echo
- Design for probe access

**Thermography**:
- Detects near-surface defects
- Requires one-sided access only
- Fast for large areas

**Radiography (X-ray)**:
- Detects voids, foreign objects
- Through-thickness access required
- Slower, higher cost

**Visual Inspection**:
- Surface defects
- Design for access to critical areas

### 8.2 Design for Inspection

- Provide access to critical areas
- Avoid complex geometries that limit probe access
- Mark inspection zones on drawings
- Define accept/reject criteria

## 9. Quality Control

### 9.1 In-Process Inspection

**Composite Layup**:
- Ply count verification
- Ply orientation check (±5° typical tolerance)
- Foreign object debris (FOD) control
- Ply splice location tracking

**Curing**:
- Thermocouple monitoring (multiple locations)
- Pressure monitoring
- Cure cycle recording (full traceability)

**Machining**:
- First article inspection (FAI)
- In-process dimensional checks
- Surface finish measurement

### 9.2 Final Inspection

- Dimensional inspection (CMM for complex parts)
- NDI per specification
- Visual inspection per acceptance criteria
- Functional checks (fit, alignment)
- Documentation and traceability

## 10. Production Rate Considerations

### 10.1 Current Plan

**Initial Production**:
- Rate: 1-2 aircraft per month
- Focus on quality and learning curve
- Flexible assembly sequence

**Mature Production**:
- Target: 5-8 aircraft per month
- Optimized flow and tooling
- Some automation

### 10.2 Design for Rate

- Minimize unique parts (commonality)
- Design for parallel assembly
- Minimize flow-time bottlenecks
- Design for automated processes where practical

## 11. Supplier and Partnership Strategy

### 11.1 Supplier Selection Criteria

- Manufacturing capability and capacity
- Quality management system (AS9100)
- Experience with large composite structures
- Geographic location (logistics)
- Cost competitiveness

### 11.2 Key Supplier Categories

- **Tier 1**: Major subassemblies (e.g., fuselage sections)
- **Tier 2**: Detail parts (e.g., frames, ribs, fittings)
- **Material suppliers**: Prepreg, aluminum, titanium
- **Fastener suppliers**: Hi-Loks, lockbolts, specialty fasteners

### 11.3 Make-Buy Strategy

**Make In-House**:
- Critical and proprietary design features
- Final assembly and integration
- Testing and validation

**Buy from Suppliers**:
- Large composite panels (if supplier capability)
- Standard metal components
- Fasteners and hardware
- Material (prepreg, raw metal)

## 12. Environmental and Safety Considerations

### 12.1 Worker Safety

- Ventilation for composite layup (volatile organics)
- Personal protective equipment (PPE)
- Ergonomic workstations
- Handling equipment for large/heavy parts

### 12.2 Environmental Compliance

- Volatile Organic Compounds (VOC) emissions control
- Waste management (prepreg trim, solvents)
- Energy efficiency in curing ovens/autoclaves
- Water treatment (surface preparation)

## 13. Lessons Learned from Similar Programs

### 13.1 Boeing 787 Composite Fuselage

**Key Lessons**:
- Out-of-autoclave curing successful for large barrels
- Fastener-free barrel sections reduce assembly time
- Shimming provisions essential for tolerance management
- Early supplier involvement critical

### 13.2 Airbus A350 Composite Wing

**Key Lessons**:
- AFP highly successful for large panels
- Co-curing stringers to skins reduces cost and weight
- Resin film infusion (RFI) viable for large parts
- Comprehensive training program for composite manufacturing

### 13.3 BWB Research Programs (X-48, Boeing)

**Key Lessons**:
- Large flat panels require careful buckling analysis
- Tooling for non-circular sections more complex
- Assembly sequence planning critical
- Modular build approach successful

## 14. Manufacturing Readiness Levels (MRL)

**Current Status** (as of 2025-11-22):

| Manufacturing Process | MRL | Target MRL |
|-----------------------|-----|------------|
| AFP for large panels | 7-8 | 9 (full production) |
| OOA curing | 6-7 | 8-9 |
| Ti investment casting | 8-9 | 9 |
| Co-curing stringers | 7-8 | 9 |
| Large assembly fixtures | 5-6 | 8-9 |

**MRL Scale**:
- **MRL 6**: Capability demonstrated in production-relevant environment
- **MRL 7**: Capability demonstrated in production system
- **MRL 8**: Capability proven in low-rate production
- **MRL 9**: Full-rate production demonstrated
- **MRL 10**: Full-rate production proven

## 15. Technology Development and Maturation

### 15.1 Manufacturing Technology Roadmap

**Phase 1 (Current - 2026)**: Mature critical processes
- AFP process optimization
- OOA material system qualification
- Large assembly fixture design and build
- Supplier capability assessments

**Phase 2 (2026-2027)**: Scale-up and validation
- Build and test full-scale demonstrators
- Supplier trial builds
- Process time reduction studies
- First article inspection protocols

**Phase 3 (2027+)**: Production readiness
- Production tooling installation
- Workforce training
- Production rate ramp-up
- Continuous improvement

### 15.2 Risk Mitigation

| Manufacturing Risk | Mitigation |
|--------------------|------------|
| Large panel distortion | Early prototypes, FEA simulation |
| Tolerance stackup | Shimming provisions, adjustable fixtures |
| Supplier delays | Multiple source strategy, early engagement |
| Tooling lead time | Early release of tool designs |
| Skilled labor shortage | Training programs, automation |

## 16. Conclusion

Manufacturing considerations are integral to the design of the AMPEL360 BWB fuselage. By addressing manufacturability, quality, and producibility during the design phase, the program will achieve cost-effective production while maintaining the highest quality standards.

This document should be used in conjunction with:
- [53-00-04-01-001_Design_Philosophy.md](53-00-04-01-001_Design_Philosophy.md)
- [53-00-04-01-003_Material_Strategy.md](53-00-04-01-003_Material_Strategy.md)
- [../02_Configuration_Items/](../02_Configuration_Items/) – CI-level manufacturing plans

---

## Document Control

- **Document ID**: 53-00-04-01-004
- **Title**: Manufacturing Considerations – AMPEL360 BWB Fuselage
- **Version**: 1.0
- **Date**: 2025-11-22
- **Author**: ATA 53 Chief Design Engineer / Manufacturing Engineering
- **Approval**: _[to be completed]_
- **Status**: DRAFT
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.
