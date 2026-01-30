# 03-40-02-02A - Cryogenic Management Software

**Document ID:** 03-40-02-02A  
**Title:** Cryogenic Management Software for LH2 GSE  
**ATA Chapter:** 03 — Support Information/GSE  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the software requirements for managing cryogenic conditions in liquid hydrogen (LH2) ground support equipment, including temperature control, boil-off management, and thermal conditioning systems operating at -253°C.

---

## 2. Scope

This specification covers:
- Cryogenic temperature monitoring and control
- LH2 boil-off gas (BOG) management
- Thermal conditioning and pre-cooling systems
- Insulation integrity monitoring
- Cryogenic valve control algorithms
- Heat leak detection and mitigation

### 2.1 Cryogenic Systems Coverage
- LH2 storage tanks (ground-based)
- Transfer lines and hoses
- Pre-cooling circuits
- BOG recovery and reliquefaction systems
- Cryogenic pumps and vaporizers

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| [ASME BPVC Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii-1-rules-construction-pressure-vessels-division-1) | Pressure Vessel Code | Cryogenic vessel standards |
| [ISO 21013](https://www.iso.org/standard/79873.html) | Cryogenic Vessels - Pressure-relief Accessories | Safety devices |
| [IEC 60079](https://www.iec.ch/homepage) | Explosive Atmospheres | H2 hazardous area equipment |
| [IEC 61508](https://www.iec.ch/functional-safety) | Functional Safety | SIL 2 requirement |
| [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) | Hydrogen Technologies Code | H2 safety |

---

## 4. Software Description

### 4.1 Overview

The Cryogenic Management Software monitors and controls all thermal aspects of LH2 handling, preventing loss of hydrogen through boil-off, managing thermal stresses, and maintaining safe cryogenic conditions throughout the GSE system.

**Safety Integrity Level:** SIL 2 (IEC 61508)  
**Control Type:** Distributed control with central coordination

### 4.2 Software Specifications

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Temperature Measurement Range | -270°C to +50°C | Full cryogenic to ambient |
| Temperature Accuracy | ±0.5°C | High precision required |
| Control Update Rate | 1 Hz to 10 Hz | Variable by zone |
| BOG Flow Measurement Accuracy | ±2% of reading | Mass flow |
| Safety Integrity Level | SIL 2 | For critical control functions |
| Data Logging Rate | 1 sample/second | High-resolution trending |
| Historical Data Retention | 5 years minimum | Regulatory compliance |

### 4.3 Cryogenic Control Functions

#### 4.3.1 Temperature Monitoring Zones
| Zone | Description | Sensor Count | Alarm Thresholds |
|------|-------------|--------------|------------------|
| Storage Tank | Main LH2 storage | 8-12 sensors | <-255°C, >-250°C |
| Transfer Lines | Active fueling paths | 20-30 sensors | <-255°C, >-248°C |
| Pre-cooling Circuit | Conditioning system | 6-8 sensors | -260°C to -240°C |
| BOG Recovery | Warm gas handling | 4-6 sensors | -100°C to +20°C |
| Interface Points | Aircraft connections | 4 sensors | <-255°C, >-248°C |

#### 4.3.2 Boil-Off Gas (BOG) Management
- **BOG Generation Rate Monitoring**
  - Calculate based on tank level change vs. transfer rate
  - Typical rate: 0.1-0.3% per day for well-insulated tanks
  - Alarm if rate exceeds 0.5% per day (insulation degradation)

- **BOG Recovery Control**
  - Capture and compress BOG for reliquefaction
  - Vent to atmosphere if recovery capacity exceeded (with safety measures)
  - Prioritize BOG usage for pre-cooling operations

- **BOG Prediction Algorithm**
  - Use historical data and ambient conditions
  - Predict BOG generation 24-48 hours ahead
  - Optimize storage and transfer schedules

#### 4.3.3 Pre-Cooling Control
```
Pre-cooling reduces thermal shock during fueling:

1. Initial Temperature Assessment
   - Measure aircraft tank temperature
   - Calculate required cooling energy
   - Estimate pre-cooling duration

2. Controlled Cool-Down
   - Flow cold H2 vapor through tank
   - Gradual temperature reduction: 20-30°C/hour max
   - Monitor tank stress (thermal strain gauges)

3. Readiness Verification
   - Target temperature: -240°C to -250°C
   - Temperature uniformity check
   - Proceed to fueling authorization
```

### 4.4 Thermal Management Algorithms

#### 4.4.1 Heat Leak Detection
- **Baseline Establishment**
  - Measure BOG rate under known conditions
  - Create thermal performance baseline
  - Update quarterly or after maintenance

- **Anomaly Detection**
  - Compare current BOG rate to baseline
  - Identify localized heat leaks (via temperature profiles)
  - Alert for insulation degradation >20% from baseline

#### 4.4.2 Vacuum Insulation Monitoring (for VJ systems)
- Monitor vacuum level in insulation jackets
- Typical vacuum: 10⁻³ to 10⁻⁵ mbar
- Alarm if vacuum degrades beyond 10⁻² mbar

### 4.5 Interfaces

#### 4.5.1 Sensor Interfaces
- Cryogenic temperature sensors (RTD, Pt100, diodes)
- Pressure transducers (cryogenic-rated)
- Level sensors (capacitive, radar)
- Flow meters (mass flow, volumetric)
- Vacuum gauges (Pirani, cold cathode)

#### 4.5.2 Control Outputs
- Cryogenic valve actuators (slow-acting to prevent hammer)
- Variable-speed cryogenic pumps
- BOG compressors
- Heater control (for vaporizers)
- Alarm and indication outputs

---

## 5. Safety and Security Requirements

### 5.1 Safety Requirements

| Requirement ID | Requirement | Target | Verification |
|----------------|-------------|--------|--------------|
| CRYO-SAF-001 | Prevent rapid temperature excursions (>50°C/min) | <30°C/min | Control algorithm |
| CRYO-SAF-002 | Overpressure protection shall activate at 110% design pressure | 110% Pd | Tested |
| CRYO-SAF-003 | BOG vent shall prevent accumulation >5% LEL | <5% LEL | Gas detection |
| CRYO-SAF-004 | Low-level alarm shall prevent pump cavitation | Alert at 20% level | Logic tested |
| CRYO-SAF-005 | Cryogenic valve actuation rate limited to prevent thermal shock | <0.5 Hz | Software enforced |

### 5.2 Operational Parameters

| Parameter | Normal Range | Warning | Alarm/Action |
|-----------|--------------|---------|--------------|
| LH2 Storage Temp | -253°C ± 2°C | ±3°C deviation | ±5°C: Investigate |
| BOG Rate | 0.1-0.3% /day | >0.4% /day | >0.6% /day: Maintenance req'd |
| Vacuum Level (VJ) | 10⁻³ to 10⁻⁵ mbar | >10⁻² mbar | >10⁻¹ mbar: Isolation required |
| Pre-cooling Rate | 20-30°C/hour | >40°C/hour | >50°C/hour: Auto-throttle |
| Heat Leak | <1% above baseline | 5-15% increase | >20%: Inspection required |

---

## 6. Cross-References

### 6.1 Related ATA Chapters
- [ATA 03-00-13](../../03-00_GENERAL/03-00-13_Subsystems_Components/README.md) — GSE Subsystems & Components

### 6.2 Parent Document
- [03-40-02_H2_GSE_Software](./README.md) — H2 GSE Software Overview

### 6.3 Related Software Documents
- 03-40-02-01A — LH2 Fueling Control SW
- 03-40-02-03A — H2 Safety Monitoring SW
- 03-40-06-01A — Safety Critical SW

---

## 7. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
