# 95-00-05-01-001 Data Sources Catalog

**Document ID:** 95-00-05-01-001
**Title:** Data Sources Catalog
**Version:** 1.0.0
**Status:** ACTIVE
**Date:** 2025-11-17

---

## Interface Attributes

| Attribute | Value |
|-----------|-------|
| **Category** | DATA |
| **Type** | Catalog / Documentation |
| **Protocol** | Multiple (AFDX, ARINC 825, Ethernet) |
| **Criticality** | DAL C |
| **Direction** | Input (to AI/ML system) |
| **Owner** | Data Engineering Team |
| **Stakeholders** | AI/ML Team, Systems Integration, Avionics |

---

## 1. Introduction

### 1.1 Purpose

This catalog provides a comprehensive inventory of all data sources that feed the AMPEL360 BWB H2-Hy-E AI/ML systems. It serves as the single source of truth for understanding what data is available, where it comes from, and how to access it.

### 1.2 Scope

**Included:**
- Aircraft sensor data (ATA 28, ATA 31, etc.)
- Avionics system data (ATA 42)
- Flight operations data (ATA 02)
- Environmental data
- Historical/training data sources

**Excluded:**
- Data processing pipelines (see 95-00-05-02-003)
- Model outputs (see 95-00-05-01-002 Data Sinks)

---

## 2. Data Source Summary

| Category | Source Count | Update Frequency | Protocol | Criticality |
|----------|-------------|------------------|----------|-------------|
| **H2 Fuel System** | 12 | 10 Hz | ARINC 825 | DAL B |
| **Flight Parameters** | 8 | 1-10 Hz | AFDX | DAL C |
| **Environmental** | 6 | 1 Hz | AFDX | DAL C |
| **Historical Data** | 3 | Batch | Ethernet | DAL E |

---

## 3. H2 Fuel System Data Sources

### 3.1 H2 Pressure Sensors

**Source ID:** `H2_PRESSURE_TANK_1`

| Attribute | Value |
|-----------|-------|
| **ATA Chapter** | 28 (Fuel) |
| **Sensor Type** | Pressure transducer |
| **Location** | H2 Tank 1 (forward fuselage) |
| **Measurement** | Hydrogen pressure |
| **Range** | 0-350 bar |
| **Accuracy** | ±1% FS |
| **Update Rate** | 10 Hz |
| **Protocol** | ARINC 825 (CAN) |
| **CAN ID** | 0x2A0 |
| **Data Format** | 32-bit float (IEEE 754) |
| **Units** | bar (absolute pressure) |
| **Criticality** | DAL B |

**Related Sensors:**
- `H2_PRESSURE_TANK_2` (CAN ID: 0x2A1)
- `H2_PRESSURE_TANK_3` (CAN ID: 0x2A2)
- `H2_PRESSURE_TANK_4` (CAN ID: 0x2A3)

### 3.2 H2 Temperature Sensors

**Source ID:** `H2_TEMP_TANK_1`

| Attribute | Value |
|-----------|-------|
| **ATA Chapter** | 28 (Fuel) |
| **Sensor Type** | Cryogenic RTD (Pt-100) |
| **Location** | H2 Tank 1 (liquid phase) |
| **Measurement** | Hydrogen temperature |
| **Range** | 20-300 K |
| **Accuracy** | ±0.5 K |
| **Update Rate** | 10 Hz |
| **Protocol** | ARINC 825 (CAN) |
| **CAN ID** | 0x2B0 |
| **Data Format** | 32-bit float (IEEE 754) |
| **Units** | Kelvin |
| **Criticality** | DAL B |

### 3.3 H2 Flow Rate Sensors

**Source ID:** `H2_FLOW_RATE_MAIN`

| Attribute | Value |
|-----------|-------|
| **ATA Chapter** | 28 (Fuel) |
| **Sensor Type** | Coriolis mass flow meter |
| **Location** | Main fuel line |
| **Measurement** | Hydrogen mass flow rate |
| **Range** | 0-50 kg/s |
| **Accuracy** | ±2% |
| **Update Rate** | 10 Hz |
| **Protocol** | ARINC 825 (CAN) |
| **CAN ID** | 0x2C0 |
| **Data Format** | 32-bit float (IEEE 754) |
| **Units** | kg/s |
| **Criticality** | DAL B |

### 3.4 H2 Tank Level Sensors

**Source ID:** `H2_LEVEL_TANK_1`

| Attribute | Value |
|-----------|-------|
| **ATA Chapter** | 28 (Fuel) |
| **Sensor Type** | Capacitive level sensor |
| **Location** | H2 Tank 1 |
| **Measurement** | Fill percentage |
| **Range** | 0-100% |
| **Accuracy** | ±1% |
| **Update Rate** | 10 Hz |
| **Protocol** | ARINC 825 (CAN) |
| **CAN ID** | 0x2D0 |
| **Data Format** | 16-bit unsigned int (scaled 0-10000) |
| **Units** | Percent (0.01% resolution) |
| **Criticality** | DAL B |

---

## 4. Flight Parameter Data Sources

### 4.1 Airspeed

**Source ID:** `AIRSPEED_IAS`

| Attribute | Value |
|-----------|-------|
| **ATA Chapter** | 34 (Navigation) |
| **Source** | Air Data Computer (ADC) |
| **Measurement** | Indicated Airspeed |
| **Range** | 0-500 knots |
| **Accuracy** | ±2 knots |
| **Update Rate** | 10 Hz |
| **Protocol** | AFDX (ARINC 664) |
| **Virtual Link** | VL_42 |
| **Data Format** | ARINC 429 label 0x206 |
| **Units** | Knots |
| **Criticality** | DAL C |

### 4.2 Altitude

**Source ID:** `ALTITUDE_PRESSURE`

| Attribute | Value |
|-----------|-------|
| **ATA Chapter** | 34 (Navigation) |
| **Source** | Air Data Computer (ADC) |
| **Measurement** | Pressure altitude |
| **Range** | -1000 to 50,000 ft |
| **Accuracy** | ±50 ft |
| **Update Rate** | 10 Hz |
| **Protocol** | AFDX (ARINC 664) |
| **Virtual Link** | VL_42 |
| **Data Format** | ARINC 429 label 0x203 |
| **Units** | Feet |
| **Criticality** | DAL C |

### 4.3 Flight Phase

**Source ID:** `FLIGHT_PHASE`

| Attribute | Value |
|-----------|-------|
| **ATA Chapter** | 02 (Operations) |
| **Source** | Flight Management System (FMS) |
| **Measurement** | Current flight phase |
| **Values** | GROUND, TAXI, TAKEOFF, CLIMB, CRUISE, DESCENT, APPROACH, LANDING |
| **Update Rate** | Event-driven |
| **Protocol** | AFDX (ARINC 664) |
| **Virtual Link** | VL_15 |
| **Data Format** | Enumerated integer (1 byte) |
| **Criticality** | DAL C |

---

## 5. Environmental Data Sources

### 5.1 Outside Air Temperature

**Source ID:** `OAT`

| Attribute | Value |
|-----------|-------|
| **ATA Chapter** | 34 (Navigation) |
| **Source** | Air Data Computer (ADC) |
| **Measurement** | Outside air temperature |
| **Range** | -70 to +50 °C |
| **Accuracy** | ±2 °C |
| **Update Rate** | 1 Hz |
| **Protocol** | AFDX (ARINC 664) |
| **Virtual Link** | VL_42 |
| **Data Format** | ARINC 429 label 0x211 |
| **Units** | Celsius |
| **Criticality** | DAL C |

---

## 6. Historical/Training Data Sources

### 6.1 Flight Data Archive

**Source ID:** `FLIGHT_DATA_ARCHIVE`

| Attribute | Value |
|-----------|-------|
| **Location** | Ground data warehouse |
| **Content** | Historical flight data (all sensors, 5 years) |
| **Size** | ~500 TB |
| **Format** | Parquet (columnar) |
| **Access** | Batch queries (SQL/Spark) |
| **Update** | Daily (post-flight sync) |
| **Protocol** | HTTPS (REST API) |
| **Criticality** | DAL E |
| **Purpose** | Model training, validation, analysis |

### 6.2 Maintenance Records

**Source ID:** `MAINTENANCE_RECORDS_DB`

| Attribute | Value |
|-----------|-------|
| **Location** | MRO database (cloud) |
| **Content** | Maintenance logs, faults, repairs |
| **Format** | SQL database (PostgreSQL) |
| **Access** | SQL queries |
| **Update** | Real-time (on-ground only) |
| **Protocol** | HTTPS (SQL over TLS) |
| **Criticality** | DAL E |
| **Purpose** | Predictive maintenance models |

---

## 7. Data Access Patterns

### 7.1 Real-Time Streaming

**Sources:** H2 sensors, flight parameters, environmental

**Access Method:**
```python
from ampel_data import StreamingDataSource

# Subscribe to real-time H2 pressure data
stream = StreamingDataSource("H2_PRESSURE_TANK_1")
for sample in stream:
    timestamp, value = sample
    # Process data
```

### 7.2 Historical Batch

**Sources:** Flight data archive, maintenance records

**Access Method:**
```python
from ampel_data import HistoricalDataSource

# Query flight data for date range
archive = HistoricalDataSource("FLIGHT_DATA_ARCHIVE")
df = archive.query(
    sensors=["H2_PRESSURE_TANK_1", "H2_TEMP_TANK_1"],
    start_date="2025-01-01",
    end_date="2025-01-31"
)
```

---

## 8. Data Quality

### 8.1 Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Availability** | > 99.9% | % of time source is accessible |
| **Completeness** | > 99% | % of expected samples received |
| **Accuracy** | Per sensor spec | Validation against calibration |
| **Latency** | < 100 ms | Time from sensor to AI/ML system |

### 8.2 Data Validation

All data sources undergo:
- **Schema validation** - Correct data types and ranges
- **Temporal validation** - Monotonic timestamps, expected frequency
- **Cross-validation** - Consistency checks across related sensors
- **Anomaly detection** - Outlier and drift detection

See [95-00-05-01-004_Data_Contracts.md](95-00-05-01-004_Data_Contracts.md) for validation rules.

---

## 9. Traceability

### 9.1 Requirements

| Requirement ID | Description | Source Reference |
|---------------|-------------|------------------|
| REQ-001 | All H2 sensor data available to AI/ML | H2_PRESSURE_TANK_* |
| REQ-002 | Flight phase detection for context | FLIGHT_PHASE |
| REQ-015 | Historical data for training | FLIGHT_DATA_ARCHIVE |

### 9.2 Data Lineage

See [95-00-05-01-005_Data_Lineage_Map.md](95-00-05-01-005_Data_Lineage_Map.md) for complete data flow.

---

## 10. Related Documents

| Document ID | Title |
|-------------|-------|
| 95-00-05-01-002 | Data Sinks Catalog |
| 95-00-05-01-003 | Feature Schemas |
| 95-00-05-01-004 | Data Contracts |
| 95-00-05-01-007 | ARINC 664 AFDX Mapping |
| 95-00-05-03-006 | ATA 28 Fuel System Interface |

---

## 11. Assets

- [95-00-05-01-A-001_Data_Flow_Diagram.svg](ASSETS/95-00-05-01-A-001_Data_Flow_Diagram.drawio) - Visual data flow
- [95-00-05-01-A-003_Data_Contracts_Table.csv](ASSETS/95-00-05-01-A-003_Data_Contracts_Table.csv) - Machine-readable contracts

---

**End of Document**

**Next Review:** 2025-12-17
**Owner:** Data Engineering Team
