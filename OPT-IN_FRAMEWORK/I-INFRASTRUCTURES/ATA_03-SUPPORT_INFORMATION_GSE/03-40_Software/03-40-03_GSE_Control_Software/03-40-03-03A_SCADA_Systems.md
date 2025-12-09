# 03-40-03-03A - SCADA Systems

**Document ID:** 03-40-03-03A  
**Title:** SCADA Systems for GSE  
**ATA Chapter:** 03 — Support Information/GSE  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

Defines SCADA (Supervisory Control and Data Acquisition) system architecture and requirements for GSE fleet management.

---

## 2. Scope

Covers centralized monitoring and control of distributed GSE assets, data acquisition, and enterprise integration.

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| [IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) | Industrial Cybersecurity | Security framework |
| [IEEE 1815](https://standards.ieee.org/standard/1815-2012.html) | DNP3 Protocol | SCADA communication |
| OPC UA Specification | OPC Foundation | Industrial interoperability |

---

## 4. Software Description

### 4.1 SCADA Architecture

```
┌─────────────────────────────────────┐
│     Enterprise Layer                 │
│  (MES, ERP Integration)              │
└──────────────┬──────────────────────┘
               ↕
┌─────────────────────────────────────┐
│     SCADA Server Layer               │
│  - Data Historian                    │
│  - Alarm Management                  │
│  - Trending and Analytics            │
└──────────────┬──────────────────────┘
               ↕
┌─────────────────────────────────────┐
│     Communication Layer              │
│  (OPC UA, Modbus TCP, DNP3)          │
└──────────────┬──────────────────────┘
               ↕
┌─────────────────────────────────────┐
│     Field Device Layer               │
│  (PLCs, RTUs, Smart Sensors)         │
└─────────────────────────────────────┘
```

### 4.2 Data Historian

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Platform | OSIsoft PI, Historian by GE | Industry-standard |
| Sample Rate | 1 Hz typical, 10 Hz for critical | Configurable |
| Compression | Swinging door algorithm | Reduce storage |
| Retention | 5 years online, 10 years archive | Regulatory |
| Query Performance | <1 sec for 1M points | Optimized |

### 4.3 Key SCADA Functions

1. **Real-Time Monitoring**: Fleet-wide status
2. **Remote Control**: Authorized setpoint changes
3. **Trend Analysis**: Historical data visualization
4. **Report Generation**: Automated daily/weekly reports
5. **KPI Dashboard**: Utilization, efficiency metrics
6. **Integration**: Connect to MRO, ERP systems

### 4.4 Interfaces

- Field PLCs/RTUs (OPC UA, Modbus TCP)
- Enterprise systems (REST APIs, database)
- Mobile devices (web-based interface)
- Email/SMS alerts
- GIS (Geographic Information System)

---

## 5. Safety and Security Requirements

| Requirement ID | Requirement | Standard |
|----------------|-------------|----------|
| SCADA-SEC-001 | Network segmentation (DMZ for SCADA) | IEC 62443-3-2 |
| SCADA-SEC-002 | Encrypted communication (TLS 1.3) | IEC 62443-3-3 |
| SCADA-SEC-003 | Intrusion detection system (IDS) | IEC 62443-2-4 |
| SCADA-SEC-004 | Regular security audits | IEC 62443-2-4 |

---

## 6. Cross-References

- 03-40-03-01A — PLC Programming
- 03-40-03-02A — HMI Software
- 03-40-04-01A — Fleet Tracking SW

---

## 7. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
