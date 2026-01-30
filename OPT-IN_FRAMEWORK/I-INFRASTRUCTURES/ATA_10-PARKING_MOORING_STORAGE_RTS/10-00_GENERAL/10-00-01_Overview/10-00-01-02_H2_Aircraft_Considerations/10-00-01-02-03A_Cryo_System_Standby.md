# 10-00-01-02-03A - Cryogenic System Standby

## 1. Purpose

This document defines the requirements and procedures for maintaining AMPEL360-BWB-H2 cryogenic systems in standby mode during parking and storage operations, ensuring system preservation and safety.

## 2. Scope

This document covers:

- Cryogenic system configurations during parking
- Active vs. passive thermal management strategies
- System monitoring requirements in standby mode
- Transition procedures between operational and standby states

## 3. Applicable Documents

- [ATA iSpec 2200](https://www.atastandards.org/) - Information Standards for Aviation Maintenance
- [ATA 100 Chapter 10](https://www.atastandards.org/) - Parking, Mooring, Storage and Return to Service
- [ATA 28 - Fuel System](../../../../ATA_28-FUEL/)
- [ISO 21013](https://www.iso.org/) - Cryogenic vessels
- [NFPA 2 - Hydrogen Technologies Code](https://www.nfpa.org/)

## 4. Description

### 4.1 Overview

The AMPEL360-BWB-H2 cryogenic system includes:

- Liquid hydrogen (LH2) storage tanks with vacuum insulation
- Cryogenic transfer lines and valves
- Boil-off management system
- Thermal conditioning equipment
- Instrumentation and monitoring systems

During parking and storage, these systems must be maintained to:
- Preserve insulation vacuum integrity
- Minimize boil-off losses
- Prevent ice formation and moisture ingress
- Maintain safe operating conditions
- Enable rapid return to service

### 4.2 H2/LH2Considerations

#### 4.2.1 Standby Mode Classifications

**Active Standby (Short-Term Parking: < 24 hours)**
- LH2 remains in tanks
- Full system monitoring active
- Normal boil-off venting
- Electrical power from aircraft or external source
- Ready for service within 30 minutes

**Passive Standby (Medium-Term Parking: 24 hours - 7 days)**
- LH2 level maintained or reduced per fuel plan
- Reduced monitoring frequency
- Automatic vent system remains active
- External power required for monitoring systems
- Ready for service within 2-4 hours

**Preservation Mode (Long-Term Storage: > 7 days)**
- Tanks drained and purged
- Vacuum insulation maintained
- Periodic monitoring only
- Systems preserved per maintenance manual
- Ready for service after inspection and reactivation (8-24 hours)

#### 4.2.2 Thermal Management

**Vacuum Insulation System:**
- Vacuum level monitoring: Maintain < 10^-3 mbar
- Vacuum pump accessibility for maintenance
- Multi-layer insulation (MLI) integrity verification
- Thermal radiation shields monitoring

**Heat Ingress Management:**
- Parasitic heat load: Typical 0.5-2.0 W per m² of tank surface
- Solar radiation shielding for extended parking
- Ambient temperature compensation
- Boil-off rate correlation with heat ingress

### 4.3 BWB Configuration Considerations

#### 4.3.1 Integrated Tank Configuration

BWB-specific cryogenic system features:
- Multiple interconnected LH2 tanks within BWB structure
- Distributed thermal management system
- BWB structure thermal coupling considerations
- Access limitations for maintenance in standby mode

#### 4.3.2 Ground Support Integration

- External power connection for cryogenic system monitoring
- Ground-based boil-off capture system compatibility (where available)
- BWB-specific ground equipment positioning
- Thermal conditioning ground cart interfaces

## 5. Requirements

| Requirement | Specification | Notes |
|-------------|---------------|-------|
| RQ-10-02-03-001 | Vacuum insulation pressure < 10^-3 mbar | Continuous monitoring in active/passive standby |
| RQ-10-02-03-002 | Tank temperature monitoring interval: Active: 1 min, Passive: 15 min | Preservation: Daily |
| RQ-10-02-03-003 | Boil-off rate not to exceed 0.5% per day | Active/Passive standby |
| RQ-10-02-03-004 | External power for monitoring: 28VDC, 5A maximum | Aircraft or ground power |
| RQ-10-02-03-005 | Automatic transition to safe mode on power loss | Battery backup for critical functions |
| RQ-10-02-03-006 | Cryogenic valve position verified before standby entry | All isolation valves closed |
| RQ-10-02-03-007 | LH2 level monitoring accuracy: ±2% | Active and passive standby |
| RQ-10-02-03-008 | System data logging for standby period | Retain for 90 days minimum |

## 6. Safety Considerations

### 6.1 Standby Entry Procedures

**Pre-Standby Checklist:**
1. Verify LH2 quantity and distribution
2. Check vacuum insulation system status
3. Confirm vent system operational
4. Verify monitoring system function
5. Connect external power (if applicable)
6. Set standby mode configuration
7. Document entry time and conditions
8. Brief ground personnel on standby status

### 6.2 Standby Monitoring

**Active Standby Monitoring:**
- Tank pressure: Continuous
- Tank temperature: Every 1 minute
- Vacuum pressure: Every 5 minutes
- Boil-off rate: Calculated hourly
- System anomalies: Immediate alert

**Passive Standby Monitoring:**
- Tank pressure: Every 15 minutes
- Tank temperature: Every 15 minutes
- Vacuum pressure: Every hour
- Boil-off rate: Calculated every 4 hours
- System anomalies: Alert within 30 minutes

**Preservation Mode Monitoring:**
- Visual inspection: Daily
- Vacuum pressure check: Daily
- Comprehensive system check: Weekly
- Documentation review: Weekly

### 6.3 Standby Exit Procedures

**Return to Service from Standby:**
1. Review standby period data logs
2. Verify no system anomalies occurred
3. Check vacuum insulation integrity
4. Verify LH2 quantity and condition
5. Perform system leak checks
6. Restore normal monitoring configuration
7. Conduct functional checks per AMM
8. Document return to service

### 6.4 Emergency Procedures in Standby

**Loss of Monitoring:**
- Automatic safe mode activation
- Visual inspection by qualified personnel
- Restore monitoring capability
- Verify system integrity before resuming standby

**Abnormal Boil-Off Rate:**
- Investigate heat ingress sources
- Check vacuum insulation system
- Consider LH2 transfer to ground storage (if available)
- Evaluate for immediate maintenance action

**Overpressure Event:**
- Emergency vent activation (automatic)
- Personnel evacuation per safety zones
- Notify emergency services
- Investigation before return to service

## 7. Cross-References

- Related ATA Chapters:
  - [ATA 28 - Fuel](../../../../ATA_28-FUEL/) - LH2 system detailed design
  - [ATA 49 - Airborne Auxiliary Power](../../../../ATA_49-APU/) - Power for cryogenic systems
  - [ATA 31 - Instruments](../../../../ATA_31-INSTRUMENTS/) - Cryogenic instrumentation
- Parent Document: [10-00-01_Overview](../../)
- Related H2 Documents:
  - [10-00-01-02-01A_H2_Parking_Requirements.md](./10-00-01-02-01A_H2_Parking_Requirements.md)
  - [10-00-01-02-02A_LH2_Venting_Procedures.md](./10-00-01-02-02A_LH2_Venting_Procedures.md)
  - [10-00-01-02-04A_H2_Safety_Zones.md](./10-00-01-02-04A_H2_Safety_Zones.md)

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-12-08*.

---
