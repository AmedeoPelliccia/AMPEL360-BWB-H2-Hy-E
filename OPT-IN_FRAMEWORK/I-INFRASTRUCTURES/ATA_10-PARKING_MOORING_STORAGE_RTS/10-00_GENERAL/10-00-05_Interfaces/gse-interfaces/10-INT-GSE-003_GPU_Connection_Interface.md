# 10-INT-GSE-003 - GPU Connection Interface

## 1. Interface Identification

| Parameter | Value |
|-----------|-------|
| Interface Number | 10-INT-GSE-003 |
| Interface Type | Electrical |
| System A | Aircraft Electrical System (ATA-24) |
| System B | Ground Power Unit (GPU) |
| ATA Chapter A | ATA-10 |
| ATA Chapter B | ATA-24 |
| H2 Related | No |
| Cryo Related | No |
| BWB Specific | No |
| Safety Classification | Safety-Related |
| Status | Baselined |

## 2. Interface Description

Defines the electrical interface between aircraft and external Ground Power Units (GPU) during parking and maintenance operations.

### Purpose
- Provide external electrical power when engines off
- Enable APU-off operations (reduce emissions)
- Support maintenance and system checks
- Reduce fuel consumption during ground operations

## 3. Interface Parameters

| Parameter | Value | Unit | Tolerance |
|-----------|-------|------|-----------|
| Voltage (115V AC) | 115 | VAC | ±3V |
| Frequency | 400 | Hz | ±10 Hz |
| Phases | 3 | - | - |
| Current Capacity | 400 | A | Maximum |
| Voltage (28V DC) | 28 | VDC | ±2V |
| DC Current Capacity | 600 | A | Maximum |
| Connector Type (AC) | MIL-C-83723 | - | Series III |
| Connector Type (DC) | MIL-C-38999 | - | Series III |
| Connector Location | Nose gear bay, left side | - | - |

## 4. Physical Interface

### 4.1 AC Power Receptacle
- Location: Forward fuselage, Station 45, BL -80
- Ground-level access via service door
- Weather-protected receptacle with hinged cover
- Interlock prevents connection if aircraft power on

### 4.2 DC Power Receptacle
- Location: Adjacent to AC receptacle
- Used for emergency power or APU start
- Compatible with standard 28VDC ground carts

### 4.3 Grounding
- Dedicated grounding point adjacent to power receptacles
- Grounding must be established before power connection
- Verified continuity required (<0.1 ohm resistance)

## 5. H2/Cryo Considerations

| Parameter | Value |
|-----------|-------|
| H2 Related | No |
| Cryo Related | No |
| Special Requirements | Standard electrical safety procedures apply |

## 6. BWB Considerations

- Receptacles accessible from ground level (BWB low profile advantage)
- Protected location in nose gear bay from weather
- Clear access despite wide BWB structure

## 7. Constraints

### Operational
- GPU must be properly grounded before connection
- Aircraft batteries disconnected before GPU connection
- Maximum cable length: 15 m
- Connection/disconnection only when no load

### Safety
- Arc flash protection required for ground personnel
- GPU must meet voltage/frequency requirements
- Automatic disconnect if parameters exceed limits
- Regular GPU testing and certification required

## 8. Verification

| Verification Method | Criteria | Status | Reference |
|---------------------|----------|--------|-----------|
| Electrical Test | Voltage/frequency within spec | Completed | TEST-10-GSE-003 |
| Load Test | Full load 400A AC, 600A DC | Completed | TEST-10-GSE-004 |
| Safety Feature Test | Interlocks function correctly | Completed | TEST-10-GSE-005 |

## 9. Related Documentation

- ICD Reference: [10-ICD-001 - Master ICD Index](../interface-control-documents/10-ICD-001_Master_ICD_Index.md)
- Related Standards: [MIL-C-83723](https://quicksearch.dla.mil/): Connector, Electrical, Aircraft Ground Power
- Cross-ATA: [10-INT-ATA-004 - Electrical Interface (ATA 24)](../ata-cross-references/10-INT-ATA-004_ATA24_Electrical_Interface.md)

## 10. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-09 | AMPEL360 Engineering | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **BASELINED** – Approved for production use
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-09

---
