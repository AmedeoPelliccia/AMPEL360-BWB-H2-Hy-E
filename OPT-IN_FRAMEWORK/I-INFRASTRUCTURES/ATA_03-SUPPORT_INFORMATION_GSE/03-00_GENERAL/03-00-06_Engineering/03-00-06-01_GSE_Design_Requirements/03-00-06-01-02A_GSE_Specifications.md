---
Title: "GSE Technical Specifications — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-06-01-02A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Technical specifications for Ground Support Equipment (GSE) used in AMPEL360 BWB H2 aircraft operations."
Keywords: ["ATA 03","GSE","Specifications","Technical Requirements","Ground Support"]
Compliance:
  - "ATA iSpec 2200"
  - "SAE ARP1796"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  Parent: "../00_INDEX.md"
  Related: "./03-00-06-01-01A_GSE_Design_Standards.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-00-06-01-02A — GSE Technical Specifications

## 1. Purpose

This document defines the **technical specifications** for Ground Support Equipment (GSE) used in servicing the AMPEL360 BWB H2-powered aircraft. These specifications provide quantitative requirements for GSE performance, capacity, and operational characteristics.

## 2. Scope

This document covers technical specifications for:

- **Refueling and fluid servicing equipment** (LH2, hydraulic, water)
- **Electrical ground power units (GPU)**
- **Environmental control units (ACU/PCU)**
- **Towing and ground handling equipment**
- **Lifting and maintenance platforms**
- **Ground communication and monitoring systems**

These specifications complement the design standards in [03-00-06-01-01A_GSE_Design_Standards](./03-00-06-01-01A_GSE_Design_Standards.md).

## 3. Applicable Documents

- [SAE ARP1796](https://www.sae.org/standards/content/arp1796/) — Aerospace Ground Equipment Design Requirements
- [SAE AS6968](https://www.sae.org/standards/content/as6968/) — Hydrogen Aircraft Ground Support Equipment
- [ISO 19880-8](https://www.iso.org/standard/71940.html) — Gaseous Hydrogen Fueling Stations (Airport Applications)
- [MIL-STD-704F](https://standards.nasa.gov/) — Aircraft Electric Power Characteristics
- [03-00-06-02_H2_GSE_Engineering](../03-00-06-02_H2_GSE_Engineering/) — Hydrogen GSE Engineering Details

## 4. LH2 Refueling Equipment Specifications

### 4.1 LH2 Refueling Truck

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Tank Capacity** | 40,000 liters LH2 (≈2,850 kg) | ±2% | Volumetric measurement |
| **Tank Pressure Rating** | 6 bar (87 psi) maximum | Design value | Pressure test at 1.5× |
| **Insulation Performance** | Boil-off rate < 0.5% per day | — | Thermal test over 48 hours |
| **Transfer Rate** | 0-2,000 liters/min variable | ±10% | Flow calibration test |
| **Transfer Pressure** | 3-5 bar (44-73 psi) at nozzle | ±0.2 bar | Pressure gauge calibration |
| **Purity** | 99.995% H2 (5.0 grade minimum) | — | Gas chromatography analysis |
| **Temperature** | -253°C (20K) at 1 atm | ±2°C | Temperature sensor calibration |
| **Leak Tightness** | < 10⁻⁶ mbar·L/s helium equivalent | — | Helium leak test |
| **Grounding Resistance** | < 10 ohms to aircraft | — | Resistance measurement |
| **Hose Length** | 15m (50 ft) nominal | ±0.5m | Physical measurement |
| **Self-Propulsion** | Max speed 25 km/h (15 mph) | — | Speed test |
| **Turning Radius** | < 10m | — | Maneuver test |

### 4.2 LH2 Fueling Hose and Nozzle

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Hose Inner Diameter** | 50mm (2 inches) | ±1mm | Caliper measurement |
| **Hose Pressure Rating** | 10 bar (145 psi) | Design value | Burst pressure test at 4× |
| **Hose Flexibility** | Bend radius < 300mm at -253°C | — | Cold bend test |
| **Nozzle Connection** | SAE AS6968 Class I (standardized) | — | Physical fit check |
| **Breakaway Coupling** | Activate at 200-400 N axial pull | ±50N | Tensile test |
| **Dead-Leg Volume** | < 2 liters | — | Volumetric calculation |

## 5. Ground Power Unit (GPU) Specifications

### 5.1 AC Ground Power Unit

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Power Output** | 120 kVA continuous, 150 kVA peak (5 min) | ±5% | Load bank test |
| **Voltage** | 115/200 VAC 3-phase, 400 Hz | ±3V, ±1 Hz | Oscilloscope measurement |
| **Voltage Regulation** | ±2% under variable load | — | Dynamic load test |
| **Frequency Stability** | 400 Hz ±1% (396-404 Hz) | — | Frequency counter |
| **Total Harmonic Distortion** | < 5% THD | — | Power quality analyzer |
| **Phase Balance** | < 5% imbalance between phases | — | Power analyzer |
| **Power Factor** | 0.8-1.0 | — | Power analyzer |
| **Efficiency** | > 85% at rated load | — | Input/output power measurement |
| **Noise Level** | < 75 dBA at 7m (23 ft) | — | Sound level meter |
| **Fuel Consumption** | < 30 L/hr at full load | — | Fuel flow measurement |
| **Start Time** | Power available < 30 seconds from cold start | — | Timed test |

### 5.2 DC Ground Power Unit

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Power Output** | 28 VDC, 1500 A continuous | ±0.5V, ±10% | Load test |
| **Voltage Regulation** | 28V ±0.25V under load | — | Load variation test |
| **Ripple Voltage** | < 0.5V peak-to-peak | — | Oscilloscope |
| **Transient Response** | < 50 ms to steady state after load change | — | Dynamic load test |
| **Current Limiting** | Adjustable 0-1500 A, trip at 110% | ±5% | Current ramp test |

## 6. Environmental Control Units

### 6.1 Air Conditioning Unit (ACU)

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Cooling Capacity** | 150 kW (43 TR) | ±10% | Calorimeter test |
| **Heating Capacity** | 100 kW | ±10% | Thermal test |
| **Airflow Rate** | 3,000-5,000 m³/h variable | ±10% | Anemometer calibration |
| **Supply Temperature Range** | +5°C to +35°C adjustable | ±2°C | Temperature sensor check |
| **Duct Connection** | 300mm (12 inch) diameter flexible duct | ±10mm | Physical fit check |
| **Duct Length** | 10m (33 ft) | ±0.5m | Measurement |
| **Noise Level** | < 80 dBA at 7m | — | Sound level meter |
| **Power Requirements** | 208 VAC 3-phase 60Hz, < 150 kVA | — | Power measurement |

### 6.2 Pre-Conditioned Air (PCA) Unit

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Airflow Rate** | 2,500 m³/h per duct (2 ducts) | ±10% | Flow measurement |
| **Temperature Range** | +10°C to +30°C | ±2°C | Temperature test |
| **Humidity** | 40-60% RH | ±5% | Hygrometer |
| **Filtration** | HEPA filter (≥99.97% at 0.3 µm) | — | Filter efficiency test |

## 7. Towing and Ground Handling Equipment

### 7.1 Aircraft Towing Tractor

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Drawbar Pull** | ≥ 250 kN (56,000 lbf) | — | Dynamometer test |
| **Towing Speed** | 0-25 km/h (0-15 mph) variable | ±2 km/h | Speed test |
| **Tow Bar Compatibility** | SAE AS25420 or BWB-specific adapter | — | Fit check with aircraft |
| **Braking Distance** | < 10m from 15 km/h | — | Brake test |
| **Turning Radius** | < 15m | — | Maneuver test |
| **Operator Visibility** | 360° visibility or camera system | — | Operational demonstration |

### 7.2 Towbarless Tractor

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Lifting Capacity** | ≥ 70 tonnes (nose gear load) | ±5% | Load test |
| **Lift Height** | Adjustable 300-800mm | ±10mm | Dimensional check |
| **Cradle Compatibility** | BWB nose gear geometry | — | Physical fit check |
| **Towing Speed** | 0-25 km/h variable | ±2 km/h | Speed test |

## 8. Lifting and Maintenance Equipment

### 8.1 Hydraulic Jack

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Lift Capacity** | 50 tonnes per jack | ±2% | Load test |
| **Lift Height Range** | 300-1,200mm | ±10mm | Dimensional check |
| **Safety Lock Intervals** | Every 50mm | ±5mm | Functional test |
| **Lift Rate** | 50-200mm/min variable | ±10% | Timed lift test |
| **Base Stability** | No tipping at 1.5× rated load offset 100mm | — | Stability test |

### 8.2 Maintenance Platform

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Platform Height Range** | 2-10m adjustable | ±50mm | Measurement |
| **Platform Size** | 5m × 2m minimum | ±100mm | Dimensional check |
| **Load Capacity** | 500 kg (2 persons + tools) | — | Load test at 1.5× |
| **Guardrail Height** | 1,100mm | ±20mm | Measurement |
| **Mobility** | Self-propelled or towable < 5 km/h | — | Mobility test |

## 9. Ground Communication and Monitoring

### 9.1 Headset and Intercom System

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Compatibility** | Standard aircraft intercom jack (U-174/U or equivalent) | — | Plug fit check |
| **Cable Length** | 10m (33 ft) | ±0.5m | Measurement |
| **Noise Cancellation** | Active noise cancellation, -25 dB | ±3 dB | Audio test |
| **Push-to-Talk** | Hands-free or handheld PTT | — | Functional test |

### 9.2 Ground Monitoring Panel

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Display Type** | 10-inch color touchscreen | — | Visual inspection |
| **Monitored Parameters** | Fuel quantity, fuel pressure, fuel temperature, electrical voltage/current, APU status | — | Interface test with aircraft |
| **Data Logging** | 1 Hz sample rate, ≥8 hours storage | — | Data extraction test |
| **Wireless Range** | 50m line-of-sight (Bluetooth or Wi-Fi) | ±10m | Range test |

## 10. Safety and Emergency Equipment

### 10.1 Fire Suppression System (for H2 GSE)

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Suppression Agent** | Dry chemical (Class D for metal fires) or inert gas (N2, Ar) | — | Agent identification |
| **Discharge Time** | Full discharge < 10 seconds | — | Timed discharge test |
| **Detection Response Time** | Alarm within 2 seconds of detection | — | Sensor test |
| **Manual Activation** | Accessible from operator position within 3 seconds | — | Ergonomic test |

### 10.2 Hydrogen Leak Detection System

| Parameter | Requirement | Tolerance | Verification |
|-----------|-------------|-----------|--------------|
| **Sensor Type** | Catalytic bead, electrochemical, or thermal conductivity | — | Sensor specification review |
| **Detection Range** | 0-4% H2 by volume (0-100% LEL) | — | Calibration test |
| **Detection Threshold** | Alarm at 10% LEL (0.4% H2) | ±5% LEL | Calibrated gas test |
| **Response Time** | < 5 seconds (T90) | — | Response time test |
| **Sensor Locations** | Within 1m of all H2 connections and vents | ±0.2m | Inspection |
| **Alarm Type** | Visual (strobe) and audible (≥85 dBA) | — | Alarm test |

## 11. Performance Verification

### 11.1 Acceptance Testing

All new GSE shall undergo acceptance testing per the following:

| Test Category | Description | Acceptance Criteria |
|---------------|-------------|---------------------|
| **Functional Test** | Verify all functions operate per specifications | 100% functions operational |
| **Performance Test** | Measure key parameters (flow rate, power output, etc.) | Within specified tolerances |
| **Safety Test** | Verify interlocks, alarms, and emergency shutoffs | All safety features functional |
| **Environmental Test** | Operate at temperature and humidity extremes | No degradation or malfunction |
| **Electromagnetic Compatibility** | EMI/EMC per DO-160 Category M | No interference with aircraft systems |

### 11.2 Periodic Calibration

| Equipment Type | Calibration Frequency | Parameters to Calibrate |
|----------------|------------------------|-------------------------|
| **LH2 Refueling** | 6 months | Flow meters, pressure gauges, temperature sensors |
| **GPU** | 12 months | Voltage, frequency, current, power output |
| **ACU/PCU** | 12 months | Temperature sensors, airflow, humidity |
| **Lifting Equipment** | 12 months (or per regulation) | Load cells, pressure gauges |
| **Leak Detectors** | 6 months | Sensor calibration with test gas |

## 12. Documentation Requirements

Each GSE unit shall be delivered with:

- **Technical Manual** — Operation, maintenance, and troubleshooting
- **Parts Catalog** — Illustrated parts breakdown with part numbers
- **Wiring Diagrams** — Electrical schematics and connection diagrams
- **Calibration Certificate** — Initial calibration data and due date
- **Test Reports** — Acceptance test results
- **Safety Data Sheets** — For all consumables (fuels, fluids, gases)

## 13. Cross-References

- **Parent Document**: [03-00-06_Engineering](../00_INDEX.md)
- **Related GSE Design Standards**: [03-00-06-01-01A_GSE_Design_Standards](./03-00-06-01-01A_GSE_Design_Standards.md)
- **H2 GSE Engineering**: [03-00-06-02_H2_GSE_Engineering](../03-00-06-02_H2_GSE_Engineering/)
- **GSE Interfaces**: [03-00-05_Interfaces](../../03-00-05_Interfaces/)
- **GSE Operations**: [03-10_Operations](../../../03-10_Operations/)

## 14. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-06-01-02A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Engineering & Certification WG

---
