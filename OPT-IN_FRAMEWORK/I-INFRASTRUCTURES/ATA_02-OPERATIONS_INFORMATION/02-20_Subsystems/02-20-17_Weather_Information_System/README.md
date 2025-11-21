# 02-20-17 — Weather Information System (WIS)

**Subsystem ID:** 02-20-17_Weather_Information_System  
**Parent Group:** [02-20-00 SYSTEMS](../README.md)  
**Axis:** I — Infrastructures  
**Status:** PROTOTYPE  
**Owner:** Flight Operations / Env. Sciences Domain  

---

## 1. Purpose

The **Weather Information System (WIS)** provides the **4D Atmospheric Context** (Latitude, Longitude, Altitude, Time) required for CAOS operations.

Unlike legacy systems that focus primarily on *Hazard Avoidance* (Turbulence, Hail), the AMPEL360 WIS focuses on **Environmental Optimization**:
*   **Thermal Management:** Predicting ground temperatures to calculate H₂ venting risks (Boil-off).
*   **Chemical Scavenging:** Identifying atmospheric regions with high CO₂ concentration for maximizing capture.
*   **Contrail Mitigation:** Predicting Ice Super-Saturated Regions (ISSR) to avoid forming persistent contrails.

---

## 2. Scope

### 2.1 Included
*   **Multi-Source Ingestion:** Fusing global models ([ECMWF](https://www.ecmwf.int/)/[NOAA](https://www.noaa.gov/)) with local sensors (Lidar/OAT).
*   **Nowcasting:** AI-driven short-term prediction (0-2 hours) for terminal operations.
*   **Chemical Weather:** Mapping atmospheric constituents (CO₂, H₂O, O₃).
*   **Integration:** Feeding data to [Dispatch (02-20-16)](../02-20-16_Dispatch_System_Integration/) and [Flight Planning (02-20-15)](../02-20-15_Flight_Planning_Integration/).

### 2.2 Excluded
*   **Onboard Weather Radar Hardware:** The physical antenna is defined in *ATA 34 (Navigation)*.
*   **Standard Met Reports:** The generation of standard METAR syntax is an external service; WIS *consumes* it.

---

## 3. Key Interfaces

| Interface ID | Target System | Description |
|:---|:---|:---|
| **IF-WIS-001** | [02-20-16 Dispatch](../02-20-16_Dispatch_System_Integration/) | Thermal data for H₂ boil-off calculations. |
| **IF-WIS-002** | [02-40-50 Predictive Ops](../../02-40_Software/02-40-50_Predictive_Analytics/) | Features for Neural Network training. |
| **IF-WIS-003** | ATA 21-80 CO2 Capture | CO₂ PPM density maps for capture optimization. |

---

## 4. Document Map

*   **[02-20-17-001: System Overview](02-20-17-001_Weather_System_Overview.md)** - The "Atmospheric Digital Twin".
*   **[02-20-17-002: Data Sources](02-20-17-002_Meteo_Data_Sources_and_Ingestion.md)** - Satellite, Ground, and Aircraft telemetry.
*   **[02-20-17-003: Data Fusion & QC](02-20-17-003_Weather_Data_Fusion_and_Quality_Control.md)** - Sensor fusion and quality control.
*   **[02-20-17-004: Operational Products](02-20-17-004_Operational_Weather_Products_for_Ops.md)** - Weather products for operations.
*   **[02-20-17-005: Neural Network Integration](02-20-17-005_Weather_Prediction_NN_Integration.md)** - AI models for contrail and CO₂ prediction.
*   **[02-20-17-006: Interfaces](02-20-17-006_Interfaces_with_Other_02-20_Subsystems.md)** - Integration with other 02-20 subsystems.

### Architecture Documents

*   **[02-20-17-A-001: System Architecture](02-20-17-A-001_Weather_System_Architecture.md)** - Technical architecture and data flows.
*   **[02-20-17-A-002: Display & Alert Layouts](02-20-17-A-002_Weather_Display_and_Alert_Layouts.md)** - User interface specifications.
*   **[02-20-17-A-501: Requirements Traceability](02-20-17-A-501_Requirements_Traceability.md)** - Traceability matrix.

### Test Data

*   [TEST_DATA/02-20-17-T-001_Meteo_Ingestion_Streams.json](TEST_DATA/02-20-17-T-001_Meteo_Ingestion_Streams.json)
*   [TEST_DATA/02-20-17-T-002_Fused_Weather_Grid_Cases.json](TEST_DATA/02-20-17-T-002_Fused_Weather_Grid_Cases.json)
*   [TEST_DATA/02-20-17-T-003_Weather_Products_Ops_Scenarios.json](TEST_DATA/02-20-17-T-003_Weather_Products_Ops_Scenarios.json)
*   [TEST_DATA/02-20-17-T-004_Weather_NN_Features_Labels.json](TEST_DATA/02-20-17-T-004_Weather_NN_Features_Labels.json)

---

## 5. CAOS Integration

The WIS is a **critical input** to the CAOS decision-making framework:

*   **Strategic Planning:** Global weather models feed into route optimization (24h-2h before departure).
*   **Tactical Operations:** Real-time atmospheric data enables dynamic altitude selection for contrail avoidance.
*   **Post-Flight Analysis:** Recorded weather conditions validate environmental claims for carbon credit certification.

See: [CAOS Operations Framework](../../../../CAOS/CAOS_OPERATIONS_FRAMEWORK.md)

---

## 6. Regulatory & Standards References

*   **[CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)** - Equipment, systems, and installations (EASA)
*   **[DO-178C](https://en.wikipedia.org/wiki/DO-178C)** - Software considerations in airborne systems
*   **[DO-200A](https://www.rtca.org/)** - Standards for processing aeronautical data
*   **WXXM (Weather Information Exchange Model)** - Standard protocol for weather data exchange

---

## 7. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
