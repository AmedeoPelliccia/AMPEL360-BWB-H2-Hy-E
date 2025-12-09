---
Title: "LH₂ Transfer Subsystem — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-13-02-02A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Detailed specifications for the Liquid Hydrogen (LH₂) Transfer Subsystem for transferring LH₂ from storage to the AMPEL360 BWB H₂ Hy-E aircraft."
Keywords: ["ATA 03","GSE","LH2 Transfer","Hydrogen","Cryogenic","Refueling"]
Compliance:
  - "ATA iSpec 2200"
  - "SAE AS6968"
  - "ISO 19880-8"
  - "ASME B31.12"
Links:
  Parent: "../"
  Siblings:
    - "03-00-13-02-01A_LH2_Storage_Subsystem.md"
    - "03-00-13-02-03A_H2_Safety_Subsystem.md"
    - "03-00-13-02-04A_Cryogenic_Control_Subsystem.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial LH₂ transfer subsystem specification" }
---

# LH₂ Transfer Subsystem — ATA 03 Support Information GSE

## 1. Purpose

This document specifies the **Liquid Hydrogen (LH₂) Transfer Subsystem** for ground support equipment serving the AMPEL360 BWB H₂ Hy-E aircraft. The subsystem enables safe, efficient transfer of cryogenic liquid hydrogen from storage tanks to aircraft fuel tanks at a rate of 500 kg/hour nominal, with peak capability of 750 kg/hour.

## 2. Scope

### 2.1 Coverage

The LH₂ Transfer Subsystem encompasses:

1. **Transfer Pump Assembly**
   - Cryogenic centrifugal pump
   - Variable frequency drive (VFD)
   - Motor cooling system
   - Vibration monitoring

2. **Cryogenic Transfer Hoses**
   - Vacuum-insulated flexible hoses
   - DN 50 (2-inch) nominal diameter
   - Length: 25 meters
   - Breakaway coupling for emergency disconnect

3. **Quick-Connect Couplings**
   - Self-sealing aircraft interface
   - Ground-side connection to hose
   - Dead-man switch integration
   - Leak-proof design

4. **Flow Control Valves**
   - Automated control valves (pneumatic/electric actuated)
   - Manual isolation valves (ball valves)
   - Check valves (non-return)
   - Emergency shut-off valves (fail-closed)

5. **Flow Metering System**
   - Coriolis mass flow meter
   - Totalizer function
   - High accuracy (±0.5% of reading)
   - Data logging capability

### 2.2 Out of Scope

- LH₂ storage tanks (see [03-00-13-02-01A](./03-00-13-02-01A_LH2_Storage_Subsystem.md))
- H₂ safety detection systems (see [03-00-13-02-03A](./03-00-13-02-03A_H2_Safety_Subsystem.md))
- Cryogenic control algorithms (see [03-00-13-02-04A](./03-00-13-02-04A_Cryogenic_Control_Subsystem.md))

## 3. Applicable Documents

| Standard | Application | Link |
|----------|-------------|------|
| **[SAE AS6968](https://www.sae.org/standards/content/as6968/)** | Hydrogen Aircraft Refueling | Transfer system requirements |
| **[ISO 19880-8](https://www.iso.org/standard/71940.html)** | Gaseous Hydrogen Fueling Stations | Transfer safety protocols |
| **[ASME B31.12](https://www.asme.org/codes-standards/find-codes-standards/b31-12-hydrogen-piping-pipelines)** | Hydrogen Piping and Pipelines | Transfer line design |
| **[EN 1594](https://standards.cen.eu/)** | Gas Supply Systems — Pipelines | Operational requirements |

## 4. Subsystem Description

### 4.1 Overview

The LH₂ Transfer Subsystem consists of a cryogenic pump, vacuum-insulated transfer hoses, automated valves, and flow metering equipment. The system transfers LH₂ from ground storage to aircraft tanks under controlled conditions, maintaining liquid state throughout the transfer process.

```
┌──────────────────────────────────────────────────────────────┐
│            LH₂ Transfer Subsystem Architecture                │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  From Storage Tank                                            │
│         │                                                      │
│         ▼                                                      │
│  ┌─────────────┐                                              │
│  │  Isolation  │                                              │
│  │    Valve    │ (Manual Ball Valve)                          │
│  │  (V-201)    │                                              │
│  └──────┬──────┘                                              │
│         │                                                      │
│         ▼                                                      │
│  ┌─────────────┐                                              │
│  │  Cryogenic  │                                              │
│  │  Transfer   │ 500 kg/hr nom., 750 kg/hr max               │
│  │    Pump     │ VFD controlled                               │
│  │  (P-201)    │                                              │
│  └──────┬──────┘                                              │
│         │                                                      │
│         ▼                                                      │
│  ┌─────────────┐                                              │
│  │   Check     │                                              │
│  │   Valve     │ (Prevent backflow)                           │
│  │  (CV-201)   │                                              │
│  └──────┬──────┘                                              │
│         │                                                      │
│         ▼                                                      │
│  ┌─────────────┐                                              │
│  │  Control    │                                              │
│  │   Valve     │ (Automated, Fail-Closed)                     │
│  │  (CV-202)   │                                              │
│  └──────┬──────┘                                              │
│         │                                                      │
│         ▼                                                      │
│  ┌─────────────┐                                              │
│  │ Flow Meter  │ Coriolis, ±0.5% accuracy                    │
│  │  (FM-201)   │ Totalizer, data logging                      │
│  └──────┬──────┘                                              │
│         │                                                      │
│         ▼                                                      │
│  ┌─────────────┐                                              │
│  │ Emergency   │                                              │
│  │  Shut-Off   │ (Fail-Closed, <1 sec closure)                │
│  │  (ESV-201)  │                                              │
│  └──────┬──────┘                                              │
│         │                                                      │
│         ▼                                                      │
│  ═════════════  Vacuum-Insulated Flexible Hose               │
│  ═════════════  DN 50, 25m length                             │
│         │                                                      │
│         ▼                                                      │
│  ┌─────────────┐                                              │
│  │ Quick-      │                                              │
│  │ Connect     │ Self-sealing, dead-man switch                │
│  │ Coupling    │                                              │
│  │ (QC-201)    │                                              │
│  └──────┬──────┘                                              │
│         │                                                      │
│         ▼                                                      │
│   To Aircraft H₂ Tank                                         │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

### 4.2 Specifications

#### 4.2.1 Transfer Pump Assembly

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Type** | Cryogenic centrifugal pump | Submerged motor design |
| **Flow Rate (Nominal)** | 500 kg/hour | 7.0 m³/hour @ 71 kg/m³ |
| **Flow Rate (Maximum)** | 750 kg/hour | 10.5 m³/hour |
| **Discharge Pressure** | 6 bar (max) | Adjustable via VFD |
| **Suction Pressure** | 1-5 bar | From storage tank |
| **Motor Power** | 15 kW | Electric, explosion-proof |
| **Motor Cooling** | LH₂ liquid cooling | Internal circulation |
| **Control** | VFD (Variable Frequency Drive) | 0-60 Hz, PLC-controlled |
| **Material (Wetted Parts)** | Stainless Steel 316L | Cryogenic compatible |
| **Temperature Range** | -253°C to +50°C | Operating range |
| **Vibration Monitoring** | Accelerometer on bearing housing | Predictive maintenance |

#### 4.2.2 Cryogenic Transfer Hoses

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Type** | Vacuum-insulated flexible hose | Double-wall construction |
| **Nominal Diameter** | DN 50 (2 inches) | Internal flow diameter |
| **Length** | 25 meters | Standard length |
| **Inner Hose Material** | Stainless Steel 316L corrugated | Flexibility + cryogenic |
| **Outer Jacket Material** | Stainless Steel 304 | Protective outer layer |
| **Insulation** | Vacuum + MLI | Multi-layer insulation |
| **Vacuum Level** | < 10⁻⁴ mbar | Maintained during service |
| **Design Pressure** | 10 bar | ASME B31.12 |
| **Operating Pressure** | 1-6 bar | Normal range |
| **Bend Radius (Min)** | 1.5 meters | Prevent hose damage |
| **Weight** | ~15 kg/meter | Requires support system |
| **End Fittings** | Flanged, ANSI 150# | Compatible with valves/couplings |

#### 4.2.3 Quick-Connect Coupling (Aircraft Interface)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Type** | Self-sealing quick-disconnect | SAE AS6968 compliant |
| **Nominal Size** | DN 50 (2 inches) | Matches hose |
| **Material** | Stainless Steel 316L | Cryogenic-rated |
| **Temperature Range** | -253°C to +50°C | Full LH₂ range |
| **Pressure Rating** | 10 bar | Design pressure |
| **Leak Rate** | < 1×10⁻⁶ mbar·L/s | Helium leak test |
| **Connection Force** | < 50 N | Manual, ergonomic |
| **Disconnection Force** | < 30 N | Manual, ergonomic |
| **Dead-Man Switch** | Integrated | Requires operator presence |
| **Safety Features** | Pressure relief, breakaway protection | Built-in |

#### 4.2.4 Flow Control Valves

| Valve ID | Type | Size | Actuation | Function |
|----------|------|------|-----------|----------|
| **V-201** | Ball valve (isolation) | DN 50 | Manual | Isolate pump from storage |
| **CV-201** | Check valve | DN 50 | Passive | Prevent backflow |
| **CV-202** | Control valve | DN 50 | Pneumatic/electric | Flow rate control |
| **ESV-201** | Emergency shut-off | DN 50 | Pneumatic (fail-closed) | Emergency isolation |

All valves:
- **Material**: Stainless Steel 316L body, PTFE or graphite seals
- **Temperature Range**: -253°C to +50°C
- **Pressure Rating**: 10 bar (ASME B31.12)
- **Actuation Time**: < 1 second (ESV-201), < 5 seconds (CV-202)

#### 4.2.5 Flow Metering System

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Type** | Coriolis mass flow meter | Direct mass measurement |
| **Flow Range** | 0-1000 kg/hour | Covers max flow + margin |
| **Accuracy** | ±0.5% of reading | Typical ±0.2% achievable |
| **Repeatability** | ±0.1% | Excellent repeatability |
| **Pressure Drop** | < 0.2 bar @ 500 kg/hr | Minimal impact |
| **Totalizer Function** | Yes | Cumulative mass transferred |
| **Output Signals** | 4-20 mA, HART, Modbus TCP | Multiple options |
| **Data Logging** | Local + remote (SCADA) | Real-time and historical |
| **Calibration Interval** | Annually | Factory or in-situ |

### 4.3 Part Number Information

| Component | Part Number | Description | Supplier | Interchangeability |
|-----------|-------------|-------------|----------|-------------------|
| Transfer Pump Assembly | GSE-H2-02-001-A | 15 kW cryogenic centrifugal pump | Barber-Nichols | None (custom) |
| VFD Controller | GSE-H2-02-002-A | 15 kW VFD, explosion-proof | ABB | ACS580 series |
| Transfer Hose (25m) | GSE-H2-02-003-A | DN 50 vacuum-insulated hose | Cryofab | None (custom) |
| Quick-Connect Coupling | GSE-H2-02-004-A | DN 50 self-sealing coupling | WEH Technologies | Model TK17 LH2 |
| Ball Valve V-201 | GSE-H2-02-005-A | DN 50 manual ball valve | Worcester Controls | Cryogenic series |
| Check Valve CV-201 | GSE-H2-02-006-A | DN 50 cryogenic check valve | Velan | Model 1060 series |
| Control Valve CV-202 | GSE-H2-02-007-A | DN 50 automated control valve | Samson AG | Type 3241 cryogenic |
| Emergency Shut-Off ESV-201 | GSE-H2-02-008-A | DN 50 fail-closed ESV | Habonim | H40 series cryogenic |
| Flow Meter FM-201 | GSE-H2-02-009-A | Coriolis mass flow meter | Endress+Hauser | Promass F 200 |

See [03-00-13-03_GSE_Part_Number_Registry](../03-00-13-03_GSE_Part_Number_Registry/) for complete PNR.

## 5. Spare Parts Information

### 5.1 Critical Spare Parts

| Part Number | Description | Criticality | Lead Time | Min Stock |
|-------------|-------------|-------------|-----------|-----------|
| GSE-H2-02-001-A | Transfer Pump Assembly | **Critical** | 16 weeks | 1 unit |
| GSE-H2-02-003-A | Transfer Hose (25m) | **Critical** | 12 weeks | 1 hose |
| GSE-H2-02-004-A | Quick-Connect Coupling | **Critical** | 8 weeks | 2 units |
| GSE-H2-02-008-A | Emergency Shut-Off ESV-201 | **Critical** | 10 weeks | 1 unit |
| GSE-H2-02-009-A | Flow Meter | **Essential** | 8 weeks | 1 unit |
| GSE-H2-02-010-A | Pump Seal Kit | **Essential** | 6 weeks | 2 kits |
| GSE-H2-02-011-A | Valve Seal Kit (CV-202) | **Standard** | 4 weeks | 2 kits |
| GSE-H2-02-012-A | Hose End Fitting Gasket Set | **Standard** | 2 weeks | 5 sets |

See [03-00-13-04_GSE_Spare_Parts_Management](../03-00-13-04_GSE_Spare_Parts_Management/) for complete spare parts strategy.

## 6. Safety Features

### 6.1 Emergency Shutdown

The transfer subsystem can be shut down by multiple methods:

| Trigger | Response Time | Action |
|---------|---------------|--------|
| **E-Stop Button** | < 1 second | Close ESV-201, stop pump, close CV-202 |
| **Leak Detection** | < 1 second | Immediate shutdown sequence |
| **High Pressure** | < 1 second | Close CV-202, stop pump |
| **Low Pressure (Suction)** | < 2 seconds | Stop pump, prevent cavitation |
| **Dead-Man Switch Release** | < 0.5 seconds | Close ESV-201 |
| **Breakaway Coupling Separation** | Immediate | Self-sealing, no leak |

### 6.2 Interlocks

| Interlock Condition | Prevents | Override |
|---------------------|----------|----------|
| Storage tank pressure < 1.2 bar | Pump start | No |
| Aircraft not connected | H₂ flow | No |
| Personnel in exclusion zone | Refueling start | No |
| Fire alarm active | All transfer operations | No |
| Aircraft tank > 98% full | Continued flow | Automatic cutoff |

## 7. Operational Parameters

### 7.1 Normal Operation

| Parameter | Operating Range | Alarm Threshold | Trip Threshold |
|-----------|-----------------|-----------------|----------------|
| Pump Discharge Pressure | 2-6 bar | < 1.5 or > 7 bar | < 1.0 or > 8 bar |
| Flow Rate | 0-750 kg/hour | > 800 kg/hour | > 850 kg/hour |
| Pump Motor Current | 5-12 A | > 14 A | > 16 A |
| Hose Vacuum Pressure | < 10⁻⁴ mbar | > 10⁻² mbar | > 10⁻¹ mbar |
| Pump Vibration | < 5 mm/s RMS | > 7 mm/s RMS | > 10 mm/s RMS |

### 7.2 Transfer Procedures

#### 7.2.1 Pre-Transfer Checklist

1. Verify all personnel clear of exclusion zone
2. Confirm aircraft ready for refueling (electrical bonding, APU off, etc.)
3. Inspect hose and couplings for damage
4. Connect hose to aircraft receptacle (hear audible click)
5. Verify "CONNECTED" signal on HMI
6. Pre-cool transfer line (circulate small amount of LH₂)
7. Verify all interlocks satisfied
8. Obtain operator confirmation to start transfer

#### 7.2.2 Transfer Sequence

1. Start transfer pump at low speed (10% VFD)
2. Gradually ramp up flow rate to desired setpoint (typically 500 kg/hr)
3. Monitor flow rate, pressure, and aircraft tank level
4. Maintain flow rate until aircraft tank reaches 95% full
5. Automatic flow reduction when tank > 95%
6. Automatic cutoff when tank = 98% (or pilot command)

#### 7.2.3 Post-Transfer Procedure

1. Close isolation valve V-201
2. Depressurize and drain transfer line (blow-back with GN₂)
3. Wait for pressure < 0.5 bar before disconnecting
4. Press coupling release button, disconnect from aircraft
5. Verify coupling self-sealed (no venting)
6. Stow hose on reel
7. Document transfer quantity and any anomalies

## 8. Maintenance Requirements

### 8.1 Routine Inspections

| Inspection | Frequency | Procedure |
|------------|-----------|-----------|
| Visual inspection (hoses, fittings) | Daily | Check for frost, damage, leaks |
| Pump vibration check | Weekly | Record vibration levels |
| Valve operation test | Monthly | Manual valves: full stroke; auto valves: stroke test |
| Flow meter verification | Quarterly | Compare with reference meter (if available) |
| Pump seal inspection | Annually | Disassemble and inspect |
| Hose vacuum integrity test | Annually | Measure vacuum level, compare to baseline |

### 8.2 Preventive Maintenance

| Task | Frequency | Estimated Duration |
|------|-----------|-------------------|
| Pump seal replacement | 2 years or 5000 hours | 16 hours |
| Valve seal replacement | 3 years | 4 hours per valve |
| Hose vacuum re-pumping | 5 years | 24 hours (if needed) |
| Flow meter calibration | Annually | 4 hours (send to OEM or in-situ) |
| VFD inspection and cleaning | 2 years | 4 hours |

## 9. Cross-References

### 9.1 Related ATA Chapters

- [ATA 02 — Operations Information](../../../../../ATA_02-OPERATIONS_INFORMATION/) — Refueling procedures
- [ATA 85 — Infrastructure Interface Standards](../../../../../ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/) — H₂ infrastructure

### 9.2 Related Documents

- [03-00-13-01-01A_GSE_Subsystem_Overview](../03-00-13-01_GSE_Subsystem_Architecture/03-00-13-01-01A_GSE_Subsystem_Overview.md)
- [03-00-13-02-01A_LH2_Storage_Subsystem](./03-00-13-02-01A_LH2_Storage_Subsystem.md)
- [03-00-13-02-03A_H2_Safety_Subsystem](./03-00-13-02-03A_H2_Safety_Subsystem.md)
- [03-00-13-02-04A_Cryogenic_Control_Subsystem](./03-00-13-02-04A_Cryogenic_Control_Subsystem.md)
- [03-00-02_Safety](../../03-00-02_Safety/) — Safety assessments
- [03-00-06_Engineering](../../03-00-06_Engineering/) — Engineering standards

### 9.3 Parent Document

- [03-00-13_Subsystems_Components](../) — Top-level subsystems directory

## 10. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-13-02-02A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 Ground Support Equipment WG

---
