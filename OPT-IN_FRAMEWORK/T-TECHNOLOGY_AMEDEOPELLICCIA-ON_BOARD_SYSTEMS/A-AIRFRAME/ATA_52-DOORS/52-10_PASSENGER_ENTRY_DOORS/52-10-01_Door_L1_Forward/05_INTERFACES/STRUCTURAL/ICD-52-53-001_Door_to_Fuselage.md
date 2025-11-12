# Interface Control Document
## Door L1 Forward to Fuselage Structure

**ICD Number:** ICD-52-53-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 53 (Fuselage)

---

## 1. INTERFACE OVERVIEW

### 1.1 Purpose
This ICD defines the structural interface between Door L1 Forward and the fuselage primary structure at Frame Station 100-110.

### 1.2 Scope
This document covers:
- Physical cutout dimensions and tolerances
- Load transfer mechanisms
- Material specifications
- Fastener requirements
- Sealing interface geometry

### 1.3 Applicable Documents
- AMS-QQ-A-250/12: Aluminum Alloy 7075 Specification
- CS-25.783: Fuselage Doors
- CS-25.365: Pressurization Differential Loads
- ICD-52-53-002: Frame Interface
- ICD-52-53-003: Hinge Mounting

---

## 2. PHYSICAL INTERFACE

### 2.1 Dimensional Requirements
- Door cutout: 1,120mm × 1,880mm (±2mm)
- Frame doubler thickness: 8mm (7075-T6 aluminum)
- Step distance: 50mm inboard (plug configuration)
- Corner radii: 150mm (min) for stress relief

### 2.2 Coordinate System
- Origin: Frame Station 100, Waterline 0, Buttline 0
- X: Positive aft (along fuselage)
- Y: Positive right (starboard)
- Z: Positive up (vertical)

### 2.3 Interface Points

| Type | Quantity | Location | Load Capacity |
|------|----------|----------|---------------|
| Hinges | 3 | Left side (Y=-560) | 45 kN each |
| Latches | 8 | Perimeter | 30 kN each |
| Stop fittings | 4 | Corners | 10 kN each |
| Alignment pins | 2 | Top center | Guide only |

---

## 3. LOAD TRANSFER

### 3.1 Operating Loads (8.5 psi differential)
- Total pressure force: 115 kN (distributed across door)
- Hinge loads: 15 kN per hinge (vertical component)
- Latch loads: 10 kN per latch (radial component)
- Moment about hinge line: 25 kN⋅m

### 3.2 Ultimate Loads (17.0 psi differential)
- Total pressure force: 230 kN
- Hinge ultimate: 30 kN per hinge
- Latch ultimate: 20 kN per latch
- Safety factor: 2.0 applied

### 3.3 Emergency Landing Loads
- Forward: 16g longitudinal
- Lateral: 3g lateral
- Vertical: 9g vertical
- Combined with pressure loads per CS-25.561

---

## 4. MATERIALS

### 4.1 Material Specifications

| Component | Material | Specification | Heat Treatment |
|-----------|----------|---------------|----------------|
| Door frame | Al 7075-T6 | AMS-QQ-A-250/12 | T6 temper |
| Frame doublers | Al 7075-T6 | AMS-QQ-A-250/12 | T6 temper |
| Hinge fittings | Ti-6Al-4V | AMS 4928 | Solution + age |
| Latch fittings | 17-4PH SS | AMS 5643 | H1150 |
| Fasteners | A286 | NAS6200 series | Aged |

### 4.2 Coating and Finish
- Aluminum parts: Chromic acid anodize per MIL-A-8625 Type I
- Titanium parts: Passivate per AMS 2700
- Stainless steel: Passivate per AMS-QQ-P-35
- Sealant: PR-1422 Class B or approved equivalent

---

## 5. TOLERANCES

### 5.1 Dimensional Tolerances
- Position: ±1.0mm (cutout perimeter)
- Angularity: ±0.5° (mounting surfaces)
- Surface profile: ±2.0mm (mating surfaces)
- Flatness: 1.0mm over 300mm (seal surfaces)

### 5.2 Fastener Tolerances
- Hole diameter: H7 tolerance (close fit)
- Hole position: ±0.5mm from nominal
- Countersink depth: ±0.2mm
- Edge distance: 2.5D minimum

---

## 6. SEALING

### 6.1 Primary Seal
- Type: Inflatable silicone seal
- Cross-section: 50mm × 25mm (compressed: 45mm × 15mm)
- Inflation pressure: 15 psi nominal
- Material: Silicone per AMS3325

### 6.2 Seal Groove (Fuselage Side)
- Width: 52mm (+1.0/-0.5)
- Depth: 28mm (±0.5)
- Surface finish: Ra 3.2μm max
- Corner radii: 2mm minimum

### 6.3 Environmental Seal
- Conductive seal for EMI protection
- Bonding resistance: <2.5 mΩ per MIL-B-5087
- Lightning protection: Level 1 (direct strike capable)

---

## 7. RESPONSIBILITIES

### 7.1 Interface Ownership

| Item | ATA 52 (Door) | ATA 53 (Fuselage) |
|------|---------------|-------------------|
| Cutout definition | Reference dimensions | Provide cutout |
| Frame doublers | - | Provide & install |
| Door frame | Provide & install | Mount points |
| Hinges | Provide hinges | Provide mount fittings |
| Latches | Provide latches | Provide strike plates |
| Seal (inflatable) | Provide & install | - |
| Seal groove | - | Provide machined groove |
| Lightning protection | Bonding straps | Structural continuity |

### 7.2 Maintenance Access
- External access: Jetway/ladder required
- Internal access: Cabin side panels removable
- Inspection interval: 4,000 flight hours / 24 months

---

## 8. VERIFICATION AND VALIDATION

### 8.1 Verification Methods

- [x] Dimensional inspection (CMM)
- [x] Load test to ultimate (static)
- [x] Seal leak test (<0.05 CFM @ 8.5 psi)
- [x] Fatigue test (60,000 cycles minimum)
- [x] Lightning strike test
- [x] Environmental testing (-55°C to +85°C)

### 8.2 Acceptance Criteria
- All dimensions within tolerance
- Ultimate load test: 1.5× operating load, no permanent deformation
- Leak rate: <0.05 CFM at 8.5 psi differential
- Fatigue: No crack initiation after 60,000 cycles (2× design life)
- Lightning: No structural damage, bonding maintained

### 8.3 Test Requirements
- Static test: Full-scale door/fuselage section
- Pressure cycling: Automated test rig
- Environmental: Temperature/humidity chamber
- Lightning: High voltage lab per DO-160G Section 23

---

## 9. CONFIGURATION CONTROL

### 9.1 Change Control Process
Any changes to this interface require:
1. Engineering change request (ECR)
2. Impact assessment by both ATA 52 and ATA 53 teams
3. Stress analysis update if loads affected
4. Drawing updates with revision control
5. Re-verification testing as required

### 9.2 Impact Assessment
Changes affecting:
- Cutout dimensions: Requires fuselage rework analysis
- Load paths: Requires complete re-analysis
- Materials: Requires corrosion/compatibility review
- Fasteners: Requires installation procedure update

---

## 10. APPENDICES

### Appendix A: Drawings
- DWG-52-53-001-01: Door Cutout Layout
- DWG-52-53-001-02: Frame Doubler Details
- DWG-52-53-001-03: Interface Cross-Section
- DWG-52-53-001-04: Seal Installation Details

### Appendix B: Analysis
- STRESS-52-53-001: Static Stress Analysis
- STRESS-52-53-002: Fatigue Life Analysis
- REPORT-52-53-001: Pressure Test Results

### Appendix C: Test Data
- TEST-52-53-001: Static Load Test Report
- TEST-52-53-002: Leak Test Results
- TEST-52-53-003: Fatigue Test Results

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial release for BWB-H2-Hy-E aircraft |

---

## APPROVALS

| Role | Name | Signature | Date |
|------|------|-----------|------|
| ATA 52 Lead Engineer | A. Pelliccia | ✓ | 2025-11-03 |
| ATA 53 Lead Engineer | [TBD] | - | - |
| Chief Structures Engineer | [TBD] | - | - |
| Certification Engineer | [TBD] | - | - |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
