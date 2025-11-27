# 53-90-00-03 Naming Conventions

| Field | Value |
|-------|-------|
| **Document ID** | 53-90-00-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL / DATA |
| **ATA Chapter** | 53-90-00 |

---

## 1. Purpose

This document defines the naming conventions for all data elements within the ANCHORS system (ATA 53) to ensure consistency, traceability, and machine-readability.

## 2. Signal Naming Convention

### 2.1 Signal ID Structure

```
<System>_<Subsystem>_<Type>_<Name>_<Qualifier>

Example: ANCH_BAT_T_CELL_MAX
         │    │   │ │    │
         │    │   │ │    └── Qualifier (MAX, MIN, AVG, etc.)
         │    │   │ └─────── Descriptive name
         │    │   └───────── Signal type code
         │    └───────────── Subsystem identifier
         └────────────────── System prefix (ANCH = ANCHORS)
```

### 2.2 System Prefixes

| Prefix | System | Description |
|--------|--------|-------------|
| ANCH | ANCHORS | Main system prefix for ATA 53 |
| EMS | Energy Management | Energy distribution subsystem |
| TMS | Thermal Management | Thermal control subsystem |
| BMS | Battery Management | Battery monitoring subsystem |

### 2.3 Subsystem Identifiers

| ID | Subsystem | Description |
|----|-----------|-------------|
| BAT | Battery | Battery pack and cells |
| CO2 | Carbon Capture | CO2 capture and storage |
| H2O | Water | Water treatment system |
| TH | Thermal | Thermal buses (HT/LT) |
| SS | Safety Supervisor | Safety monitoring |
| MM | Mode Manager | Operating mode control |
| EMS | Energy Management | Power distribution |

### 2.4 Signal Type Codes

| Code | Type | Description | Typical Units |
|------|------|-------------|---------------|
| T | Temperature | Thermal measurement | °C, K |
| P | Pressure | Pressure measurement | bar, kPa |
| F | Flow | Flow rate | L/min, kg/s |
| L | Level | Fill level or percentage | %, L |
| V | Voltage | Electrical potential | V, mV |
| I | Current | Electrical current | A, mA |
| W | Power | Electrical power | W, kW |
| S | Speed | Rotational or linear speed | RPM, m/s |
| D | Discrete | Boolean or enumerated | 0/1, enum |
| A | Analog | Generic analog value | varies |
| C | Command | Control command output | varies |
| X | Status | System status | enum |

### 2.5 Qualifier Codes

| Qualifier | Meaning | Usage |
|-----------|---------|-------|
| MAX | Maximum | Highest value |
| MIN | Minimum | Lowest value |
| AVG | Average | Mean value |
| RAW | Raw | Unprocessed sensor data |
| FLT | Filtered | Processed/filtered value |
| CMD | Command | Commanded value |
| ACT | Actual | Measured actual value |
| LIM | Limit | Threshold limit |
| SET | Setpoint | Target setpoint |

## 3. Parameter Naming Convention

### 3.1 Parameter ID Structure

```
P_<System>_<Subsystem>_<Name>_<Type>

Example: P_BAT_TMS_T_HIGH_LIM
         │ │   │   │ │    │
         │ │   │   │ │    └── Type (LIM, SET, GAIN, etc.)
         │ │   │   │ └─────── Descriptive name
         │ │   │   └───────── Parameter category
         │ │   └───────────── Subsystem
         │ └───────────────── System
         └─────────────────── Parameter prefix
```

### 3.2 Parameter Categories

| Category | Description | Modification Rights |
|----------|-------------|---------------------|
| Fixed | Hardware-defined, not modifiable | Factory only |
| Tunable | Adjustable during development | Engineering |
| Configurable | Adjustable per aircraft | Maintenance |
| Adaptive | Self-adjusting during operation | Automatic |

### 3.3 Parameter Type Suffixes

| Suffix | Meaning | Example |
|--------|---------|---------|
| _LIM | Limit threshold | P_BAT_T_HIGH_LIM |
| _SET | Setpoint | P_TH_HT_T_SET |
| _GAIN | Control gain | P_TMS_COOL_GAIN |
| _TI | Integral time | P_TMS_COOL_TI |
| _TD | Derivative time | P_PID_TD |
| _MIN | Minimum value | P_PUMP_SPD_MIN |
| _MAX | Maximum value | P_PUMP_SPD_MAX |
| _NOM | Nominal value | P_CO2_FLOW_NOM |

## 4. Message Naming Convention

### 4.1 AFDX Virtual Link Naming

```
VL_<ATA><Sequence>

Example: VL_5301
         │  │  │
         │  │  └── Sequence number (01-99)
         │  └───── ATA chapter (53)
         └──────── Virtual Link prefix
```

### 4.2 CAN Message Naming

```
<SUBSYSTEM>_<FUNCTION>_<QUALIFIER>

Example: BAT_CELL_TEMP_1
         │   │    │    │
         │   │    │    └── Instance number
         │   │    └─────── Measurement type
         │   └──────────── Function
         └──────────────── Subsystem
```

## 5. Document Naming Convention

### 5.1 Document ID Structure

```
<ATA>-<Bucket>-<Band>-<Sequence>_<Title>.md

Example: 53-90-10-01_Signal_Catalog.csv
         │  │  │  │   │
         │  │  │  │   └── Descriptive title
         │  │  │  └────── Sequence (01-99)
         │  │  └───────── Band (00-90)
         │  └──────────── Bucket (00-90)
         └─────────────── ATA chapter
```

### 5.2 Figure Naming

```
FIG-<ATA>-<Bucket>-<Sequence>_<Title>.<ext>

Example: FIG-53-40-001_SW_Context.mermaid
```

### 5.3 Drawing Naming

```
DWG-<ATA>-<Bucket>-<Sequence>_<Title>.<ext>

Example: DWG-53-60-001_Battery_Housing.step
```

## 6. Data File Naming

### 6.1 CSV Files

| Pattern | Usage | Example |
|---------|-------|---------|
| `*_Catalog.csv` | Catalog listings | `Signal_Catalog.csv` |
| `*_Matrix.csv` | Traceability matrices | `Req_Design_Matrix.csv` |
| `*_Definitions.csv` | Definition tables | `AFDX_VL_Definitions.csv` |

### 6.2 JSON Schema Files

| Pattern | Usage | Example |
|---------|-------|---------|
| `*_Schema.json` | Schema definitions | `Signal_Schema.json` |
| `*_Record.json` | Record templates | `Component_Record.json` |

### 6.3 Reserved Characters

| Character | Usage | Replacement |
|-----------|-------|-------------|
| Space | Not allowed | Use underscore `_` |
| Hyphen `-` | Segment separator | Use for IDs only |
| Underscore `_` | Word separator | Use in names |
| Period `.` | Extension separator | File extension only |

## 7. Examples

### 7.1 Signal Examples

| Signal ID | Description |
|-----------|-------------|
| `ANCH_BAT_T_CELL_MAX` | Battery cell maximum temperature |
| `ANCH_BAT_V_PACK` | Battery pack voltage |
| `ANCH_CO2_P_INLET` | CO2 system inlet pressure |
| `ANCH_TH_F_HT_BUS` | High-temp thermal bus flow |
| `ANCH_SS_D_ISO_CMD` | Safety supervisor isolation command |

### 7.2 Parameter Examples

| Parameter ID | Description |
|--------------|-------------|
| `P_BAT_TMS_T_HIGH_LIM` | Battery high temperature limit |
| `P_CO2_CTRL_FLOW_SET` | CO2 control flow setpoint |
| `P_TH_HT_PUMP_SPD_MIN` | HT pump minimum speed |
| `P_EMS_BAT_SOC_MIN` | Minimum battery state of charge |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---
