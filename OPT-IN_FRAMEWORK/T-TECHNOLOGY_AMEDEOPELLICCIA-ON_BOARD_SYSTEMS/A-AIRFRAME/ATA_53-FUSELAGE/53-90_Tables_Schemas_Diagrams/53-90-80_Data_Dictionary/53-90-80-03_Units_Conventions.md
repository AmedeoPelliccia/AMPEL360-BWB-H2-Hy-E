# 53-90-80-03 Units Conventions

| Field | Value |
|-------|-------|
| **Document ID** | 53-90-80-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL / REFERENCE |
| **ATA Chapter** | 53-90-80 |

---

## 1. Purpose

This document defines the units and measurement conventions used throughout the ANCHORS system documentation and data.

## 2. General Principles

### 2.1 Unit System

The ANCHORS system uses **SI (International System of Units)** as the primary unit system, with exceptions for aviation-standard units where required for interoperability.

### 2.2 Preferred Units

| Quantity | SI Unit | Symbol | Aviation Unit |
|----------|---------|--------|---------------|
| Length | meter | m | ft, in (structural) |
| Mass | kilogram | kg | lb (weight & balance) |
| Time | second | s | — |
| Temperature | Celsius | °C | — |
| Pressure | pascal | Pa | psi, inHg (cockpit) |
| Current | ampere | A | — |
| Voltage | volt | V | — |
| Power | watt | W | — |
| Energy | joule | J | kWh (batteries) |

## 3. Quantity-Specific Conventions

### 3.1 Temperature

| Context | Unit | Precision | Range |
|---------|------|-----------|-------|
| Display | °C | 1° | -40 to +80 |
| Internal | °C × 10 | 0.1° | -400 to +800 |
| Absolute | K | 1 K | 230 to 350 |

**Conversion**: K = °C + 273.15

### 3.2 Pressure

| Context | Unit | Precision | Typical Range |
|---------|------|-----------|---------------|
| Internal | bar | 0.01 bar | 0 to 10 |
| Display | bar | 0.1 bar | 0 to 10 |
| Hydraulics | psi | 1 psi | 0 to 3000 |
| Altitude | kPa | 0.1 kPa | 20 to 110 |

**Conversions**:
- 1 bar = 100,000 Pa = 14.504 psi
- 1 psi = 6894.76 Pa

### 3.3 Flow Rate

| Fluid | Unit | Precision | Typical Range |
|-------|------|-----------|---------------|
| Coolant | L/min | 0.1 L/min | 0 to 300 |
| CO2 Gas | L/min | 1 L/min | 0 to 50 |
| Water | L/min | 0.1 L/min | 0 to 10 |
| Mass Flow | kg/s | 0.01 kg/s | 0 to 5 |

### 3.4 Electrical

| Quantity | Unit | Precision | Typical Range |
|----------|------|-----------|---------------|
| Voltage (HV) | V | 1 V | 0 to 900 |
| Voltage (LV) | V | 0.1 V | 0 to 28 |
| Current | A | 0.1 A | -500 to +500 |
| Power | kW | 0.1 kW | 0 to 1000 |
| Energy | kWh | 0.1 kWh | 0 to 50 |

### 3.5 Percentage

| Context | Unit | Precision | Range |
|---------|------|-----------|-------|
| SOC | % | 1% | 0 to 100 |
| SOH | % | 0.1% | 0 to 100 |
| Fill Level | % | 1% | 0 to 100 |
| Valve Position | % | 1% | 0 to 100 |
| Pump Speed | % | 1% | 0 to 100 |

### 3.6 Time

| Context | Unit | Precision |
|---------|------|-----------|
| Timestamps | ISO 8601 | 1 s |
| Response time | ms | 1 ms |
| Control periods | s | 0.001 s |
| Flight time | h | 0.1 h |
| Calendar | days | 1 day |

## 4. Data Encoding

### 4.1 Integer Encoding

| Type | Bytes | Range | Usage |
|------|-------|-------|-------|
| int8 | 1 | -128 to 127 | Small signed |
| uint8 | 1 | 0 to 255 | Percentage, enum |
| int16 | 2 | -32768 to 32767 | Temperature, current |
| uint16 | 2 | 0 to 65535 | Voltage, flow |
| int32 | 4 | ±2×10⁹ | Accumulated values |
| uint32 | 4 | 0 to 4×10⁹ | Counters, time |

### 4.2 Scaling Conventions

| Quantity | Raw Type | Factor | Offset | Example |
|----------|----------|--------|--------|---------|
| Temperature | int16 | ×10 | -400 | 450 = 45.0°C |
| Voltage | uint16 | ×10 | 0 | 7500 = 750.0V |
| Current | int16 | ×10 | 0 | -1000 = -100.0A |
| Pressure | uint16 | ×100 | 0 | 350 = 3.50 bar |
| Flow | uint16 | ×10 | 0 | 1500 = 150.0 L/min |
| Percentage | uint8 | ×1 | 0 | 85 = 85% |

### 4.3 Boolean Encoding

| Value | Meaning |
|-------|---------|
| 0x00 | FALSE |
| 0x01 | TRUE |
| 0xFF | INVALID/UNKNOWN |

## 5. Display Conventions

### 5.1 Numeric Formatting

| Quantity | Format | Example |
|----------|--------|---------|
| Temperature | ±XX.X °C | 45.2 °C |
| Voltage | XXX.X V | 750.0 V |
| Current | ±XXX.X A | -125.5 A |
| Power | XXX.X kW | 85.2 kW |
| Pressure | X.XX bar | 3.45 bar |
| Percentage | XXX % | 85 % |

### 5.2 Timestamp Format

**ISO 8601 Extended Format**: `YYYY-MM-DDTHH:MM:SS.sssZ`

Example: `2025-11-27T14:30:45.123Z`

- All timestamps in UTC (Zulu time)
- Millisecond precision for events
- Second precision for logs

## 6. Tolerance and Accuracy

### 6.1 Measurement Accuracy

| Sensor Type | Accuracy | Precision |
|-------------|----------|-----------|
| RTD (Temp) | ±0.5°C | 0.1°C |
| PT (Pressure) | ±1% FS | 0.01 bar |
| Flow Meter | ±2% | 0.1 L/min |
| Current Sensor | ±1% | 0.1 A |
| Voltage Sensor | ±0.5% | 0.1 V |

### 6.2 Rounding Rules

- Round half to even (banker's rounding)
- Apply after final calculation
- Preserve full precision in intermediate calculations

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---
