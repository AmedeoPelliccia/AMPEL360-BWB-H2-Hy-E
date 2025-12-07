# 03-00-09-02-01A - LH2 Fueling GSE Production

**Version:** A  
**Date:** 2025-12-07  
**Status:** DRAFT  
**Document ID:** 03-00-09-02-01A

---

## 1. Purpose

This document defines the production planning and manufacturing requirements for Liquid Hydrogen (LH2) Fueling Ground Support Equipment. It establishes specifications, processes, and quality requirements for producing safe and reliable LH2 fueling systems.

---

## 2. Scope

This document covers production planning for:
- LH2 fueling nozzles and connections
- Cryogenic transfer hoses and couplings
- Flow control and metering systems
- Pressure regulation equipment
- Emergency shutdown systems
- Grounding and bonding systems
- Auxiliary support equipment

---

## 3. Applicable Documents

- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE ARP1796 (GSE Design Requirements)
- SAE AS6968 (Hydrogen Aircraft Refueling)
- ISO 19880 (Gaseous Hydrogen Fueling Stations)
- ASME B31.12 (Hydrogen Piping and Pipelines)
- AWS D1.1 (Structural Welding Code)
- ASME Section VIII (Pressure Vessel Code)
- Reference: 03-00-09-02_H2_GSE_Production

---

## 4. Production Planning Requirements

### 4.1 Overview

LH2 fueling GSE is the most critical equipment category for hydrogen aircraft operations. Production must ensure:
- Absolute safety and reliability at cryogenic temperatures (-253°C)
- Zero-leak performance for hydrogen containment
- Compliance with aviation and hydrogen safety standards
- Traceability of all pressure-boundary materials and welds
- Rigorous testing and validation protocols

### 4.2 Production Specifications

| Parameter | Requirement | Target | Verification |
|-----------|-------------|--------|--------------|
| Operating Temperature | -253°C to +50°C | Design validated | Cryogenic testing |
| Operating Pressure | Up to 10 bar | Per design | Hydrostatic testing |
| Leak Rate | < 1×10⁻⁹ sccs He | Zero detectable leaks | Helium leak testing |
| Flow Rate | 500-2000 kg/hr | As specified | Flow testing |
| Material Compatibility | H2 compatible | 316L SS, Al 5083 | Material certs |
| Surface Finish | Ra < 0.8 µm (wetted) | Smooth finish | Visual/profilometer |
| Welding Quality | 100% radiographic | No defects | NDT inspection |

### 4.3 Schedule

| Milestone | Date | Deliverables |
|-----------|------|--------------|
| Design Freeze | Q2 2025 | Production drawings |
| First Article Build | Q4 2025 | Prototype unit |
| FAI Completion | Q1 2026 | FAI report |
| Pilot Production Start | Q1 2026 | 2 units |
| Rate Production Start | Q3 2026 | 3 units/month |
| Full Rate Production | Q1 2027 | 8 units/month |

---

## 5. Resource Requirements

### 5.1 Facility Requirements

**Specialized Areas:**
- Clean assembly environment (Class 100,000 minimum)
- Cryogenic test facility with LH2 capability
- Hydrogen-safe welding area with proper ventilation
- Pressure testing cell (rated to 1.5x max operating pressure)
- Leak testing facility (helium mass spectrometer)

**Safety Systems:**
- H2 detection and alarm systems
- Emergency ventilation
- Fire suppression (water deluge)
- Grounding and bonding points
- Emergency shutdown controls

### 5.2 Equipment and Tooling

| Equipment | Quantity | Purpose | Specification |
|-----------|----------|---------|---------------|
| TIG Welding Stations | 4 | H2-qualified welding | Auto-TIG with purge |
| Cryogenic Test Chamber | 1 | LN2/LH2 testing | -253°C capable |
| Helium Leak Detector | 2 | Leak testing | 1×10⁻¹⁰ sensitivity |
| Hydrostatic Test Stand | 1 | Pressure testing | 0-20 bar range |
| Flow Test Rig | 1 | Flow calibration | LN2 compatible |
| X-ray Machine | 1 | Weld inspection | Radiographic NDT |
| CMM | 1 | Dimensional inspection | ±0.01mm accuracy |

### 5.3 Workforce Requirements

| Role | Headcount | Key Qualifications |
|------|-----------|-------------------|
| Welding Engineers | 2 | ASME Section IX, cryogenic experience |
| Welders (certified) | 8 | H2 welding certification, 6G qualified |
| Assembly Technicians | 6 | Cryogenic systems, clean assembly |
| Test Technicians | 4 | Cryogenic testing, H2 safety trained |
| Quality Inspectors | 4 | NDT Level II, dimensional inspection |
| Production Engineers | 2 | LH2 systems, production planning |

---

## 6. Quality Requirements

### 6.1 Material Requirements

**Primary Materials:**
- Stainless Steel 316L (pressure boundaries)
- Aluminum 5083 (non-pressure components)
- PTFE/Teflon (seals and gaskets)
- Copper (electrical bonding)

**Material Certification:**
- Mill test certificates for all pressure-boundary materials
- Lot traceability for all materials
- Hydrogen compatibility verification
- Low-temperature impact testing for cryogenic service

### 6.2 Welding Requirements

**Welding Standards:**
- ASME Section IX qualification
- AWS D1.1 procedures
- 100% radiographic inspection of pressure welds
- Magnetic particle or dye penetrant for non-pressure welds

**Welder Certification:**
- 6G position certification
- Cryogenic welding qualification
- H2 systems specialized training
- Annual recertification

**Weld Quality:**
- Zero tolerance for cracks, lack of fusion, or porosity
- Visual inspection per AWS D1.1
- Radiographic inspection per ASME Section V
- Full traceability (welder ID, date, procedure)

### 6.3 Testing and Validation

**Component-Level Testing:**
1. **Dimensional Inspection** - CMM measurement, all critical dimensions
2. **Surface Finish** - Profilometer for wetted surfaces
3. **Material Verification** - PMI (Positive Material Identification)
4. **Weld Inspection** - Radiographic or ultrasonic per design

**Assembly-Level Testing:**
1. **Pressure Test** - Hydrostatic to 1.5x max operating pressure, hold 10 min
2. **Leak Test** - Helium mass spectrometry, < 1×10⁻⁹ sccs
3. **Flow Test** - Calibration with LN2, verify flow rates
4. **Cryogenic Soak Test** - LN2 thermal cycle, 10 cycles minimum
5. **Functional Test** - Full operational sequence with LN2

**Acceptance Criteria:**
- Zero leaks detected
- No permanent deformation after pressure test
- Flow rates within ±5% of specification
- All safety interlocks functional
- Complete traceability documentation

---

## 7. Special Production Considerations

### 7.1 Hydrogen Embrittlement Prevention

**Material Selection:**
- Use only hydrogen-compatible materials (austenitic stainless steels, aluminum alloys)
- Avoid high-strength steels susceptible to embrittlement
- Material certification for H2 service

**Process Control:**
- Minimize cold work in hydrogen-exposed areas
- Control heat input during welding to prevent sensitization
- Post-weld heat treatment where specified
- Avoid galvanic couples that can promote hydrogen absorption

### 7.2 Cryogenic Service Considerations

**Design Validation:**
- Thermal analysis of all components
- Thermal contraction allowance
- Insulation and vapor barrier design
- Boil-off management

**Material Properties:**
- Low-temperature toughness verification (Charpy impact testing)
- Coefficient of thermal expansion compatibility
- Sealant and gasket cryogenic performance

### 7.3 Cleanliness Requirements

**Cleaning Procedures:**
- Solvent cleaning (isopropyl alcohol or equivalent)
- Passivation of stainless steel surfaces
- Clean assembly in controlled environment
- White-glove assembly for internal components

**Contamination Control:**
- Particle count limits per ISO 14644
- No hydrocarbons on oxygen-enriched components
- Moisture control (dew point monitoring)
- Capping and bagging during storage

---

## 8. Production Process Flow

### 8.1 Manufacturing Sequence

1. **Material Receipt and Inspection**
   - Verify certifications
   - Positive Material Identification (PMI)
   - Dimensional inspection of raw materials

2. **Fabrication**
   - Machining per drawings
   - Surface finish verification
   - Deburring and edge break

3. **Welding**
   - Joint preparation and fitup
   - Pre-weld inspection
   - Welding per qualified procedures
   - Post-weld NDT inspection

4. **Cleaning and Passivation**
   - Solvent cleaning
   - Passivation (stainless steel)
   - Drying and purging
   - Cleanliness verification

5. **Assembly**
   - Clean-room assembly
   - Torque verification
   - In-process inspection

6. **Testing**
   - Pressure testing
   - Leak testing
   - Flow calibration
   - Cryogenic validation

7. **Final Inspection and Documentation**
   - Final dimensional check
   - Documentation package assembly
   - Serialization and traceability
   - Certification and release

### 8.2 Cycle Time Targets

| Process Step | Target Cycle Time | Notes |
|--------------|-------------------|-------|
| Fabrication | 5 days | Including inspection |
| Welding | 3 days | Including NDT |
| Cleaning/Passivation | 1 day | Including drying |
| Assembly | 2 days | Clean environment |
| Testing | 5 days | Including cryogenic cycles |
| Final Inspection | 1 day | Documentation |
| **Total** | **17 days** | Per unit |

---

## 9. Safety and Environmental

### 9.1 Production Safety

**Hydrogen Safety Measures:**
- Continuous H2 monitoring (LEL alarm at 1% H2)
- Explosion-proof electrical equipment in H2 areas
- Proper ventilation (10+ air changes per hour)
- No ignition sources near H2 work areas
- Emergency procedures and training

**Cryogenic Safety:**
- PPE for cryogenic handling (face shield, insulated gloves)
- Thermal burn first aid readily available
- Oxygen deficiency monitoring
- Pressure relief systems

### 9.2 Environmental Considerations

- Minimize hydrogen venting (capture and recycle where possible)
- Proper disposal of cleaning solvents
- Waste minimization in fabrication
- Energy-efficient production processes

---

## 10. Supply Chain

### 10.1 Critical Suppliers

| Component | Supplier Type | Lead Time | Notes |
|-----------|---------------|-----------|-------|
| Cryogenic Valves | Strategic Partner | 12 weeks | Long-lead item |
| Flow Meters | Preferred Supplier | 8 weeks | H2 compatible |
| Stainless Steel Tubing | Multiple Sources | 4 weeks | Certified material |
| Cryogenic Hoses | Strategic Partner | 10 weeks | Custom lengths |
| Instrumentation | Preferred Supplier | 6 weeks | Calibrated |

### 10.2 Inventory Strategy

- 3-month inventory for long-lead cryogenic components
- JIT for standard hardware and fasteners
- Safety stock for critical valves and instruments
- Consignment agreements with key suppliers

---

## 11. Cross-References

- Related ATA Chapters:
  - ATA 03-00-02 (Safety)
  - ATA 03-00-04 (Design)
  - ATA 03-00-06 (Engineering)
  - ATA 03-00-07 (V&V)
- Parent Document: 03-00-09-02_H2_GSE_Production
- Related Documents:
  - 03-00-09-02-02A (Cryogenic GSE Manufacturing)
  - 03-00-09-02-04A (H2 GSE Supplier Qualification)
  - 03-00-09-03-03A (GSE Welding Specifications)

---

## 12. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 H2 GSE Production Team | Initial release |

---

**Document Control Information:**
- **Status**: DRAFT
- **Classification**: Internal - Production
- **Distribution**: H2 GSE Production Team, Quality Assurance
