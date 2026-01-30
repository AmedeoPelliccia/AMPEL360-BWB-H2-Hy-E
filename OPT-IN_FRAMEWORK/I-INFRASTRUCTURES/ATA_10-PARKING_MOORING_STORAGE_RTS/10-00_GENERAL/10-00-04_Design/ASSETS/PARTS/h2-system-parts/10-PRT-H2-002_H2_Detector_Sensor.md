# 10-PRT-H2-002 - H2 Detector Sensor

## 1. Part Identification

| Parameter | Value |
|-----------|-------|
| **Part ID** | 10-PRT-H2-002 |
| **Part Number** | AMPEL-10-H2-SEN-002-A |
| **CAGE Code** | TBD |
| **Title** | H2 Detector Sensor |
| **Category** | h2-system |
| **Status** | ACTIVE |
| **Superseded By** | N/A |

---

## 2. Description

The H2 Detector Sensor is a safety-critical component for detecting hydrogen gas leaks during parking and storage operations. The sensor provides continuous monitoring of H2 concentration in the vicinity of the LH2 tanks and fuel system, alerting ground crew to potential hazards.

### 2.1 Functional Overview

The sensor provides:
- Continuous H2 concentration measurement (0-4% vol)
- Alarm outputs at configurable thresholds (typically 1% and 2% vol)
- Fast response time (< 3 seconds to 90% signal)
- Temperature-compensated measurement
- Self-diagnostic capability
- 4-20 mA analog output and digital interface (RS-485)

Primary use cases:
- Continuous monitoring during parking with LH2 onboard
- Leak detection during tank servicing
- Safety zone monitoring around aircraft
- Integration with ground safety systems

### 2.2 Design Features

- **Catalytic bead sensor**: Proven technology, intrinsically safe
- **Explosion-proof housing**: ATEX Zone 1 certified
- **Wide temperature range**: -40°C to +85°C operation
- **Low power consumption**: < 2W typical
- **Field-replaceable sensor element**: 12-month sensor life
- **NEMA 4X enclosure**: Weather-resistant for outdoor use

---

## 3. Technical Specifications

### 3.1 Physical Properties

| Parameter | Value | Unit | Tolerance |
|-----------|-------|------|-----------|
| **Weight** | 0.85 | kg | ±0.1 |
| **Length** | 120 | mm | ±3 |
| **Width** | 80 | mm | ±3 |
| **Height** | 95 | mm | ±3 |
| **Bounding Box** | 120 × 80 × 95 | mm | - |

### 3.2 Material

| Parameter | Value |
|-----------|-------|
| **Primary Material** | 316 Stainless Steel (Housing) |
| **Material Standard** | ASTM A240 |
| **Secondary Materials** | PTFE (Cable gland seals), Ceramic (Sensor element) |
| **Surface Finish** | Electropolished |
| **Finish Specification** | ASTM B912 Class 2 |

### 3.3 Performance Requirements

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| **Measurement Range** | 0 to 4.0 | % vol H2 | Calibrated range |
| **Accuracy** | ±0.1 | % vol | At 1% H2 |
| **Response Time (T90)** | < 3 | seconds | 90% signal |
| **Alarm Threshold 1** | 1.0 | % vol | Configurable (25% LEL) |
| **Alarm Threshold 2** | 2.0 | % vol | Configurable (50% LEL) |
| **Operating Temp** | -40 to +85 | °C | Full specification range |
| **Power Consumption** | 1.8 | W | Typical @ 24VDC |
| **Sensor Life** | 12 | months | Typical, depends on usage |

**Note:** LEL (Lower Explosive Limit) for H2 is 4% by volume in air.

---

## 4. H2/Cryo Compatibility

### 4.1 H2 Compatibility

| Parameter | Value |
|-----------|-------|
| **H2 Compatible** | Yes (designed for H2 detection) |
| **H2 Service Type** | Gaseous H2 only (sensor for gas phase) |
| **H2 Pressure Rating** | Ambient pressure (1 atm) |
| **Material Qualification** | ISO 11114-4 compatible materials |
| **Permeation Rate** | N/A (open sampling) |

**Material Compatibility Notes:**
- 316 stainless steel housing: Excellent H2 compatibility
- Catalytic bead sensor: Designed specifically for H2 detection
- PTFE seals: H2 compatible
- All electrical components intrinsically safe (no spark risk)

### 4.2 Cryogenic Rating

| Parameter | Value |
|-----------|-------|
| **Cryo Rated** | No (ambient temperature sensor) |
| **Min Operating Temp** | -40°C (not cryogenic) |
| **Max Operating Temp** | +85°C |
| **Thermal Cycling Qualified** | Yes (-40°C to +85°C, 100 cycles) |
| **Insulation Type** | N/A (ambient operation) |
| **Cryo Standard** | N/A (not a cryogenic component) |

**Temperature Performance:**
- Sensor operates in ambient air, not in contact with LH2
- Temperature compensation maintains accuracy across -40°C to +85°C
- Housing withstands thermal shock from cold H2 vapor plumes
- Not rated for immersion in LH2 (-253°C)

### 4.3 ATEX/IECEx Classification

| Parameter | Value |
|-----------|-------|
| **ATEX/IECEx Certified** | Yes |
| **Zone Rating** | Zone 1 (ATEX) |
| **Certificate Number** | ATEX: TBD-SENS-H2-YY, IECEx: TBD-SENS-H2-ZZ |
| **Explosion Group** | IIC (Hydrogen) |
| **Temperature Class** | T4 (< 135°C surface temperature) |

**Safety Notes:**
- Intrinsically safe design (IS barrier required for non-IS installations)
- Catalytic sensor operates below ignition temperature
- No arcing or sparking components
- Double-sealed cable entries prevent gas ingress

---

## 5. Supplier Information

### 5.1 Primary Supplier

| Parameter | Value |
|-----------|-------|
| **Supplier Name** | [TBD - Gas Detection Specialist] |
| **Supplier CAGE Code** | TBD |
| **Supplier P/N** | TBD-H2-CAT-120 |
| **Lead Time** | 8-12 weeks |
| **Minimum Order Quantity** | 5 units |
| **Cost Category** | Medium (Industrial gas detector) |
| **Contact** | procurement@ampel360.com |

### 5.2 Alternate Suppliers

| Supplier | CAGE Code | Supplier P/N | Lead Time | Notes |
|----------|-----------|--------------|-----------|-------|
| [TBD Alt 1] | TBD | TBD-H2-XX | 10 weeks | ATEX certified, slightly larger |
| [TBD Alt 2] | TBD | TBD-H2-YY | 12 weeks | Lower cost, same performance |

---

## 6. Interchangeability

| Alternate P/N | Source | Form/Fit/Function | Notes |
|---------------|--------|-------------------|-------|
| TBD-ALT-001 | Alternate Mfr | Equivalent | Requires calibration with H2 gas |
| TBD-ALT-002 | Alternate Mfr | Similar | Different mounting pattern |

**Interchangeability Notes:**

Several COTS H2 sensors are available with similar specifications. Key requirements for alternates:
- ATEX Zone 1 certification for H2 (Group IIC)
- 0-4% vol measurement range minimum
- Response time < 5 seconds
- Temperature range -40°C to +85°C
- 4-20 mA output standard
- All alternates require calibration with certified H2 gas mixture before use

---

## 7. Storage Requirements

### 7.1 Storage Conditions

| Parameter | Value |
|-----------|-------|
| **Temperature Range** | -20°C to +50°C |
| **Max Relative Humidity** | 80% RH (non-condensing) |
| **Special Requirements** | Store in original packaging; Avoid exposure to solvents or strong oxidizers |

### 7.2 Shelf Life

| Parameter | Value |
|-----------|-------|
| **Shelf Life** | 24 months (sealed storage) |
| **Storage Conditions** | Original packaging, temperature controlled, dry environment |
| **Extendable** | No (sensor element degrades) |
| **Extension Procedure** | N/A (replace sensor element if exceeded) |

**Inspection Schedule:**
- Prior to installation: Calibration verification with H2 gas
- Every 12 months in service: Recalibration
- Sensor element replacement: Every 12-18 months (usage dependent)

### 7.3 Packaging

- Primary: Individual sensor in anti-static bag with calibration certificate
- Secondary: Foam-lined cardboard box
- Tertiary: Shipping carton with "CALIBRATED SENSOR - HANDLE WITH CARE" markings
- Desiccant pack included to prevent moisture damage
- Calibration date and expiration date labeled on packaging

---

## 8. Hazmat Classification

| Parameter | Value |
|-----------|-------|
| **Is Hazmat** | No |
| **UN Number** | N/A |
| **Hazard Class** | N/A |
| **Packing Group** | N/A |
| **Special Provisions** | None |

**Note:** Sensor itself is not hazmat. Used for detecting H2 (Class 2.1 flammable gas).

---

## 9. Related Documentation

### 9.1 Drawings

- 10-00-04-DWG-H2-SEN-002-SHT01-R01 - Sensor assembly drawing
- 10-00-04-DWG-H2-SEN-002-SHT02-R01 - Installation and mounting
- 10-00-04-DWG-H2-SEN-002-SHT03-R01 - Wiring diagram

### 9.2 Models

- 10-00-04-MODL-H2-002.step - 3D STEP model
- 10-00-04-MODL-H2-002-Installation.pdf - Installation guide

### 9.3 Specifications

- 10-00-04-SPEC-H2-SEN-002-R01 - Functional specification
- 10-00-04-CAL-H2-SEN-002-R01 - Calibration procedure
- 10-00-04-CERT-H2-SEN-002-ATEX-R01 - ATEX certificate (TBD)

---

## 10. Requirements Traceability

### 10.1 Related Requirements

- **REQ-10-H2-020** - H2 leak detection system required during parking
- **REQ-10-H2-021** - Sensors shall detect H2 at 25% LEL (1% vol)
- **REQ-10-H2-022** - Response time shall be < 5 seconds
- **REQ-10-SAFE-020** - All detection equipment shall be ATEX Zone 1 certified

### 10.2 Related Hazards

- **HAZ-10-H2-001** - H2 leak during parking operations (Severity: Major)
- **HAZ-10-H2-002** - H2 ignition from external source (Severity: Catastrophic)
- **HAZ-10-H2-003** - Undetected H2 accumulation (Severity: Major)

### 10.3 Operational Domain (ODD) References

- **ODD-10-PKG-01** - Parking operations with LH2 tanks
- **ODD-10-STO-01** - Long-term storage monitoring
- **ODD-10-MAINT-01** - Maintenance with H2 system active

---

## 11. Maintenance & Notes

### 11.1 Special Handling

- Handle with care; sensor element is fragile
- Do NOT expose to high concentrations of H2 (> 10% vol) during calibration
- Avoid contact with silicones, sulfur compounds (sensor poisons)
- Always use certified calibration gas (2.0% H2 in air typical)
- Power off before connecting/disconnecting wiring

### 11.2 Inspection Points

- Physical damage to housing or cable
- Corrosion or contamination on sensor inlet
- Cable gland seal integrity
- Electrical connections secure and dry
- Calibration within validity period (12 months)

### 11.3 Maintenance Requirements

- **Every 30 days**: Functional test (bump test with 1% H2 gas)
- **Every 6 months**: Full calibration with certified gas
- **Every 12-18 months**: Sensor element replacement
- **After any impact or damage**: Full calibration verification

### 11.4 Design Notes

- Sensor should be mounted in areas where H2 may accumulate (high points, enclosed spaces)
- Minimum 4 sensors recommended per aircraft (one per quadrant around LH2 tanks)
- Sensors must be wired to ground-based monitoring system with audible/visual alarms
- DO NOT paint over sensor inlet (will block gas diffusion)
- Integration with aircraft fire suppression system recommended

---

## 12. Applicable Standards

- **General**: ATA iSpec 2200, ATA 100 Chapter 10
- **H2 Safety**:
  - SAE AS6968 - Hydrogen Aircraft GSE
  - NFPA 2 - Hydrogen Technologies Code
  - ISO 11114-4 - Gas compatibility
- **Detection Standards**:
  - IEC 60079-29-1 - Gas Detectors - Performance Requirements
  - EN 50271 - Electrical Apparatus for Detection and Measurement of Combustible Gases
- **Safety**: ATEX 2014/34/EU, IECEx
- **Quality**: ISO 9001

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
- Repository: `AMPEL360-BWB-H2-Hy-E`

**Critical Safety Note:**

This is a safety-critical H2 detection component. Proper installation, calibration, and maintenance are life-safety critical. All sensors must be calibrated with certified gas mixtures per IEC 60079-29-1 before use.
