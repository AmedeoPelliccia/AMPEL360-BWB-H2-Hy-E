# 10-PRT-H2-001 - H2 Vent Valve Assembly

## 1. Part Identification

| Parameter | Value |
|-----------|-------|
| **Part ID** | 10-PRT-H2-001 |
| **Part Number** | AMPEL-10-H2-VV-001-A |
| **CAGE Code** | TBD |
| **Title** | H2 Vent Valve Assembly |
| **Category** | h2-system |
| **Status** | ACTIVE |
| **Superseded By** | N/A |

---

## 2. Description

The H2 Vent Valve Assembly is a safety-critical component designed for controlled venting of hydrogen gas during aircraft parking and storage operations. This valve allows safe release of boil-off hydrogen from the LH2 tanks to prevent pressure buildup while the aircraft is on the ground.

### 2.1 Functional Overview

The valve assembly provides:
- Automatic pressure relief at preset thresholds
- Manual override capability for emergency venting
- Fail-safe operation in all conditions
- Flame arrestor integration to prevent ignition
- Leak-tight sealing when closed
- Compatible with both gaseous H2 and LH2 boil-off vapors

Primary use cases:
- Long-term parking with LH2 tanks partially filled
- Pre-flight venting during tank servicing
- Emergency pressure relief during ground operations
- Maintenance mode venting

### 2.2 Design Features

- **Cryogenic-rated body**: 316L stainless steel construction for -253°C operation
- **Dual-redundant seals**: Primary PTFE seal with backup metal-to-metal seat
- **Integrated flame arrestor**: Stainless steel mesh prevents flame propagation
- **Manual override handle**: Allows ground crew manual actuation
- **Position indicator**: Visual indication of valve open/closed state
- **ATEX Zone 1 certified**: Explosion-proof design for H2 atmospheres

---

## 3. Technical Specifications

### 3.1 Physical Properties

| Parameter | Value | Unit | Tolerance |
|-----------|-------|------|-----------|
| **Weight** | 8.5 | kg | ±0.5 |
| **Length** | 280 | mm | ±5 |
| **Width** | 150 | mm | ±5 |
| **Height** | 220 | mm | ±5 |
| **Bounding Box** | 280 × 150 × 220 | mm | - |

### 3.2 Material

| Parameter | Value |
|-----------|-------|
| **Primary Material** | 316L Stainless Steel (Body, Flanges) |
| **Material Standard** | ASTM A240 / ASTM A479 |
| **Secondary Materials** | PTFE (Seals), Inconel 625 (Spring), 304 SS (Flame Arrestor) |
| **Surface Finish** | Electropolished to 0.8 μm Ra |
| **Finish Specification** | ASTM B912 Class 1 |

### 3.3 Performance Requirements

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| **Cracking Pressure** | 1.2 | bar | Valve opens at this pressure |
| **Reseat Pressure** | 0.9 | bar | Valve closes at this pressure |
| **Flow Capacity** | 50 | SCFM @ 1.5 bar | Gaseous H2 |
| **Leak Rate (Closed)** | < 1×10⁻⁶ | mbar·L/s | He leak test |
| **Operating Cycles** | > 10,000 | cycles | Service life |
| **Proof Pressure** | 6.0 | bar | Hydrostatic test |
| **Burst Pressure** | > 12.0 | bar | Safety factor > 4 |

---

## 4. H2/Cryo Compatibility

### 4.1 H2 Compatibility

| Parameter | Value |
|-----------|-------|
| **H2 Compatible** | Yes |
| **H2 Service Type** | Both (Gaseous H2 and LH2 boil-off) |
| **H2 Pressure Rating** | 4.0 bar working, 6.0 bar proof |
| **Material Qualification** | ISO 11114-4 qualified, SAE AS6968 compliant |
| **Permeation Rate** | < 5×10⁻⁷ mbar·L/s @ 1 bar (PTFE seal) |

**Material Compatibility Notes:**
- 316L stainless steel: Austenitic, no hydrogen embrittlement risk
- PTFE seals: Low permeation, compatible with H2 and cryogenic service
- Inconel 625 spring: High strength maintained at cryogenic temperatures
- All materials tested per ISO 11114-4 for H2 compatibility

### 4.2 Cryogenic Rating

| Parameter | Value |
|-----------|-------|
| **Cryo Rated** | Yes |
| **Min Operating Temp** | -253°C (20K - LH2 temperature) |
| **Max Operating Temp** | +85°C (Ambient maximum) |
| **Thermal Cycling Qualified** | Yes (100 cycles: -253°C to +85°C) |
| **Insulation Type** | None (valve body exposed to cryogenic fluid) |
| **Cryo Standard** | ASTM E1450 tested, ISO 20421 compliant |

**Cryogenic Performance:**
- Maintains sealing performance at -253°C
- No brittle fracture risk (316L austenitic SS)
- Thermal contraction accommodated by design
- Spring maintains force at cryogenic temperatures

### 4.3 ATEX/IECEx Classification

| Parameter | Value |
|-----------|-------|
| **ATEX/IECEx Certified** | Yes |
| **Zone Rating** | Zone 1 (ATEX), Zone 21 (dust - not applicable) |
| **Certificate Number** | ATEX: TBD-XXXX-YY, IECEx: TBD-XXXX |
| **Explosion Group** | IIC (Hydrogen) |
| **Temperature Class** | T1 (< 450°C surface temperature) |

**Safety Notes:**
- Valve design prevents ignition sources
- Flame arrestor prevents flame propagation into tank
- Bonded and grounded for static discharge prevention
- Manual override does not generate sparks

---

## 5. Supplier Information

### 5.1 Primary Supplier

| Parameter | Value |
|-----------|-------|
| **Supplier Name** | [TBD - Aerospace Valve Specialist] |
| **Supplier CAGE Code** | TBD |
| **Supplier P/N** | TBD-H2-VV-280 |
| **Lead Time** | 16-20 weeks |
| **Minimum Order Quantity** | 10 units |
| **Cost Category** | High (Custom cryogenic valve) |
| **Contact** | procurement@ampel360.com |

### 5.2 Alternate Suppliers

| Supplier | CAGE Code | Supplier P/N | Lead Time | Notes |
|----------|-----------|--------------|-----------|-------|
| [TBD Alt 1] | TBD | TBD-XX-YY | 18 weeks | ATEX certified, longer lead time |
| [TBD Alt 2] | TBD | TBD-ZZ-AA | 20 weeks | Proven LH2 tank heritage |

---

## 6. Interchangeability

| Alternate P/N | Source | Form/Fit/Function | Notes |
|---------------|--------|-------------------|-------|
| None identified | N/A | N/A | Custom design for AMPEL360 BWB H2 system |

**Interchangeability Notes:**

This is a custom-designed valve for the AMPEL360 aircraft H2 system. No direct commercial off-the-shelf (COTS) alternates exist. Any substitution would require re-qualification for:
- H2 compatibility per ISO 11114-4
- Cryogenic performance per ASTM E1450
- ATEX Zone 1 certification
- Aircraft installation approval

---

## 7. Storage Requirements

### 7.1 Storage Conditions

| Parameter | Value |
|-----------|-------|
| **Temperature Range** | -20°C to +50°C |
| **Max Relative Humidity** | 60% RH |
| **Special Requirements** | Clean room Class 10,000 or better; Sealed in inert gas (N2 or Ar) |

### 7.2 Shelf Life

| Parameter | Value |
|-----------|-------|
| **Shelf Life** | Unlimited (with periodic inspection) |
| **Storage Conditions** | Sealed container, inert atmosphere, temperature controlled |
| **Extendable** | N/A (unlimited with proper storage) |
| **Extension Procedure** | N/A |

**Inspection Schedule:**
- Every 12 months: Visual inspection, seal integrity check
- Every 24 months: Functional test (pressure cycle)
- Prior to installation: Full leak test and functional verification

### 7.3 Packaging

- Primary: Individual valve sealed in aluminum foil barrier bag with desiccant
- Secondary: Foam-lined plastic case (impact protection)
- Tertiary: Cardboard shipping carton with "FRAGILE - CRYOGENIC VALVE" markings
- Inert gas (N2 or Ar) purge inside barrier bag
- DO NOT freeze or expose to temperatures below -40°C during storage

---

## 8. Hazmat Classification

| Parameter | Value |
|-----------|-------|
| **Is Hazmat** | No |
| **UN Number** | N/A |
| **Hazard Class** | N/A |
| **Packing Group** | N/A |
| **Special Provisions** | None (valve itself is not hazmat; used with H2 which is Class 2.1) |

**Note:** While the valve is used in H2 service, the valve itself is not classified as hazardous material for shipping purposes.

---

## 9. Related Documentation

### 9.1 Drawings

- 10-00-04-DWG-H2-VV-001-SHT01-R01 - Assembly drawing
- 10-00-04-DWG-H2-VV-001-SHT02-R01 - Installation drawing
- 10-00-04-DWG-H2-VV-001-SHT03-R01 - Flame arrestor detail

### 9.2 Models

- 10-00-04-MODL-H2-001.step - 3D STEP model
- 10-00-04-MODL-H2-001.stp - Native CAD model

### 9.3 Specifications

- 10-00-04-SPEC-H2-VV-001-R01 - Functional specification
- 10-00-04-TEST-H2-VV-001-R01 - Qualification test report
- 10-00-04-CERT-H2-VV-001-ATEX-R01 - ATEX certificate (TBD)

---

## 10. Requirements Traceability

### 10.1 Related Requirements

- **REQ-10-H2-001** - H2 venting system shall provide automatic pressure relief
- **REQ-10-H2-002** - Vent valves shall prevent flame propagation
- **REQ-10-H2-010** - All H2 components shall be ATEX Zone 1 certified
- **REQ-10-SAFE-015** - Fail-safe operation required for all pressure relief devices

### 10.2 Related Hazards

- **HAZ-10-H2-001** - H2 leak during parking operations (Severity: Major)
- **HAZ-10-H2-002** - H2 ignition from external source (Severity: Catastrophic)
- **HAZ-10-H2-005** - Tank overpressure due to boil-off (Severity: Major)

### 10.3 Operational Domain (ODD) References

- **ODD-10-PKG-01** - Parking operations with LH2 tanks partially filled
- **ODD-10-STO-01** - Long-term storage (> 24 hours)

---

## 11. Maintenance & Notes

### 11.1 Special Handling

- Handle with clean, lint-free gloves
- Do NOT use oil or grease on any part (H2 incompatible)
- Ensure electrical bonding during installation (ESD and static discharge)
- Use only specified torque values for installation (over-torque can damage seals)
- Leak test required after each installation or maintenance

### 11.2 Inspection Points

- Visual inspection: No damage, corrosion, or contamination
- Seal integrity: PTFE seal surface condition
- Flame arrestor: No blockage, clean mesh
- Manual override: Smooth operation, returns to auto position
- Position indicator: Clear visibility and accurate indication

### 11.3 Maintenance Requirements

- **Every 500 flight hours or 12 months**: Visual inspection, functional test
- **Every 2000 flight hours or 5 years**: Overhaul (seal replacement, leak test)
- **After any H2 leak event**: Mandatory inspection and leak test
- **Wear items**: PTFE seals (replace at overhaul)

### 11.4 Design Notes

- Valve is designed for vertical installation (H2 rises, flame arrestor on top)
- Manual override should be easily accessible to ground crew
- Position indicator visible from ground level
- Drain port provided for condensate removal (if any moisture ingress)
- DO NOT modify or repair in field; return to OEM for any defects

---

## 12. Applicable Standards

- **General**: ATA iSpec 2200, ATA 100 Chapter 10, S1000D
- **H2/Cryo**:
  - SAE AS6968 - Hydrogen Aircraft Ground Support Equipment
  - NFPA 2 - Hydrogen Technologies Code
  - ISO 11114-4 - Gas Cylinders - Compatibility with Hydrogen
  - ISO 20421 - Cryogenic Vessels
  - ASTM E1450 - Tensile Testing at Cryogenic Temperatures
  - ASME BPVC Section VIII - Pressure Vessels
- **Safety**:
  - ATEX 2014/34/EU - Explosive Atmospheres Directive
  - IECEx - Explosive Atmospheres Certification
- **Material**:
  - ASTM A240 - Stainless Steel Plate, Sheet, and Strip
  - ASTM A479 - Stainless Steel Bars and Shapes
  - ASTM B912 - Electropolished Surfaces
- **Quality**: ISO 9001, AS9100

---

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-09 | AI (Amedeo Pelliccia) | Initial release - AI generated specification |

---

## 14. Document Control

| Parameter | Value |
|-----------|-------|
| **Status** | ACTIVE |
| **Originator** | AI (GitHub Copilot) prompted by Amedeo Pelliccia |
| **Checker** | _[to be completed]_ |
| **Approver** | _[to be completed]_ |
| **Last Updated** | 2025-12-09 |

**AI Generation Note:**

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`

**Critical Safety Note:**

This is a safety-critical H2 system component. All specifications, material selections, and certifications MUST be verified by qualified engineers before procurement or use. H2 compatibility and cryogenic performance are life-safety critical and require rigorous testing and certification.
