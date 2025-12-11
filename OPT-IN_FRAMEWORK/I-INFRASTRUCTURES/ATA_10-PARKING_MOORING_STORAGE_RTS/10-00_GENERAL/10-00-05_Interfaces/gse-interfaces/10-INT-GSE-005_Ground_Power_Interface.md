# 10-INT-GSE-005 - Ground Power Interface

## 1. Interface Identification

| Parameter | Value |
|-----------|-------|
| Interface Number | 10-INT-GSE-005 |
| Interface Type | Electrical |
| System A | Aircraft Power Distribution |
| System B | Ground Power Sources |
| ATA Chapter A | ATA-10 |
| ATA Chapter B | ATA-24 |
| H2 Related | No |
| Cryo Related | No |
| BWB Specific | No |
| Safety Classification | Safety-Related |
| Status | Baselined |

## 2. Interface Description

Comprehensive interface for all ground electrical power connections, consolidating AC and DC power requirements for parking and maintenance operations. This interface ensures safe and efficient power supply from external sources.

### Purpose
- Centralize ground power interface specification
- Define power quality requirements
- Establish connection procedures
- Enable various ground power scenarios

## 3. Interface Parameters

### AC Power
| Parameter | Value | Unit |
|-----------|-------|------|
| Voltage | 115/200 | VAC |
| Frequency | 400 | Hz |
| Phases | 3-phase | - |
| Capacity | 400 | A |

### DC Power
| Parameter | Value | Unit |
|-----------|-------|------|
| Voltage | 28 | VDC |
| Capacity | 600 | A |

### Power Quality
- Voltage regulation: ±3% for AC, ±5% for DC
- Frequency stability: ±10 Hz
- Total harmonic distortion: <5%
- Transient voltage: <150% of nominal

## 4. Physical Interface

### 4.1 Connection Points
- Primary AC: Nose gear bay, left side (10-INT-GSE-003)
- DC: Adjacent to AC connection
- Emergency: Additional DC port, right side

### 4.2 Safety Features
- Reverse polarity protection
- Over-voltage/under-voltage protection
- Over-current protection (circuit breakers)
- Ground fault detection
- Arc flash protection

## 5. H2/Cryo Considerations

| Parameter | Value |
|-----------|-------|
| H2 Related | No |
| Cryo Related | No |
| Special Requirements | Electrical bonding verified before H2 operations |

## 6. BWB Considerations

- Multiple connection points may be added for BWB maintenance
- Power distribution across wide BWB structure
- Redundant grounding points for large metallic structure

## 7. Constraints

### Operational
- Power factor: >0.9
- GPU must be stabilized before connection
- Load management system prevents overload
- Maximum simultaneous loads defined in aircraft manual

### Safety
- Personnel training required for connection/disconnection
- PPE required: insulated gloves, face shield
- Lockout/tagout procedures for maintenance
- Ground power disconnect before aircraft power-up

## 8. Verification

| Verification Method | Criteria | Status | Reference |
|---------------------|----------|--------|-----------|
| Power Quality Test | All parameters within specification | Completed | TEST-10-GSE-008 |
| Safety System Test | All protections function correctly | Completed | TEST-10-GSE-009 |
| Load Test | Full load sustainable for 8 hours | Completed | TEST-10-GSE-010 |

## 9. Related Documentation

- ICD Reference: [10-ICD-001 - Master ICD Index](../interface-control-documents/10-ICD-001_Master_ICD_Index.md)
- Related: [10-INT-GSE-003 - GPU Connection Interface](./10-INT-GSE-003_GPU_Connection_Interface.md)
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
