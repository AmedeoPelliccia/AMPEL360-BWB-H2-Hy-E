# 10-00-12-05A - Cryo System Maintenance

## 1. Purpose

This document defines specialized maintenance procedures for cryogenic liquid hydrogen (LH2) systems on the AMPEL360-BWB-H2 aircraft, addressing unique challenges of maintaining systems operating at -253°C.

## 2. Scope

- Cryogenic system component maintenance
- Vacuum jacket integrity testing
- Thermal insulation inspection and repair
- Cryogenic valve maintenance
- Boil-off management system maintenance
- Cold hazard safety protocols

## 3. Applicable Standards

- [ISO 13984](https://www.iso.org/standard/71440.html) - Liquid Hydrogen - Land Vehicle Fueling System Interface
- [ISO 21013](https://www.iso.org/standard/69791.html) - Cryogenic Vessels - Pressure Relief Accessories
- [NASA Safety Standard 1740.16](https://standards.nasa.gov/) - Safety Standard for Hydrogen and Hydrogen Systems
- [CGA P-12](https://www.cganet.com/) - Safe Handling of Cryogenic Liquids

## 4. Cryogenic System Components

### 4.1 LH2 Storage Tanks

**Maintenance Tasks**:
- External visual inspection (every A-Check)
- Vacuum jacket integrity test (every C-Check)
- Boil-off rate verification (every B-Check)
- Thermal imaging survey (every C-Check)
- Multi-layer insulation (MLI) inspection (every D-Check)

**Vacuum Jacket Integrity Test**:
1. Monitor vacuum pressure (target: <10⁻⁴ mbar)
2. Perform helium leak test if vacuum degraded
3. Document vacuum pressure trends over time
4. Schedule re-vacuum if pressure >10⁻³ mbar

### 4.2 Cryogenic Transfer Lines

**Maintenance Tasks**:
- Visual inspection for frost/ice formation (every A-Check)
- Thermal protection integrity (every B-Check)
- Flexible line inspection (every C-Check)
- Thermal imaging for cold spots (every C-Check)
- Line replacement (every 15,000 FH or 10 years)

**Inspection Criteria**:
- No visible frost on outer surface (indicates insulation failure)
- No mechanical damage to thermal protection
- Flexible sections free of cracks or kinks
- Support brackets secure and undamaged

### 4.3 Cryogenic Valves

**Maintenance Tasks**:
- External inspection (every A-Check)
- Valve cycling test (every B-Check)
- Seat leak test (every C-Check)
- Valve overhaul (every 8,000 FH or 72 months)

**Cold Valve Inspection**:
- Extended stem design allows operation without warming
- Inspect stem packing for leaks (frost indicates leak)
- Verify valve position indication accuracy
- Check for valve freeze-up during cycling test

### 4.4 Boil-Off Management System

**Components**:
- Pressure build-up coil (heat exchanger for pressure control)
- Vent system and relief valves
- Boil-off gas (BOG) utilization system (if equipped)
- Pressure control system

**Maintenance Tasks**:
- Relief valve function test (every 12 months)
- BOG flow measurement (every B-Check)
- Pressure control accuracy (every B-Check)
- Vent system inspection (every A-Check)

## 5. Cryogenic Safety Protocols

### 5.1 Cold Burn Hazards

LH2 at -253°C can cause severe cold burns on contact:

**Safety Measures**:
- Never touch cryogenic components or piping
- Use cryo-rated gloves (rated to -273°C)
- Wear face shield when working near potential spray sources
- Have warm water available for cold burn first aid

### 5.2 Oxygen Deficiency Hazard

LH2 venting can displace oxygen in confined spaces:

**Safety Measures**:
- Continuous oxygen monitoring in work area (maintain >19.5% O₂)
- Adequate ventilation at ground level (H2 rises, but cold gas may settle)
- Respiratory protection if O₂ <19.5%
- Never enter confined space without confined space permit

### 5.3 Brittle Fracture Hazard

Many materials become brittle at cryogenic temperatures:

**Safety Measures**:
- Use only cryo-rated materials for repairs
- Do not strike or impact cold surfaces
- Allow gradual warming before disassembly (never force)
- Inspect for cracks after any thermal cycling

## 6. Thermal Insulation Maintenance

### 6.1 Multi-Layer Insulation (MLI)

MLI consists of multiple reflective layers in vacuum:

**Inspection**:
- Can only be fully inspected during vacuum loss investigation
- External signs: frost formation, increased boil-off rate
- Thermal imaging can detect cold spots indicating MLI damage

**Repair**:
- Requires tank removal and vacuum chamber access
- MLI replacement is major overhaul task (D-Check level)
- Specialist contractor may be required

### 6.2 Foam Insulation

Some areas may use cryogenic foam insulation:

**Inspection**:
- Visual inspection for cracking or detachment
- Density check (foam should be uniform, not crushed)
- Moisture intrusion check (ice formation indicates moisture)

**Repair**:
- Remove damaged foam sections
- Surface must be clean and dry before foam application
- Use only cryo-rated foam materials
- Allow proper cure time before cooling system

## 7. Boil-Off Rate Verification

Normal boil-off rate for AMPEL360-BWB-H2: TBD% per day (typical 0.3-1.5%)

### 7.1 Measurement Procedure

1. Fill tank to known level (e.g., 90% full)
2. Seal tank and record pressure and temperature
3. Monitor over 24-hour period
4. Calculate LH2 loss from pressure rise or mass change
5. Calculate boil-off rate as percentage per day

### 7.2 Acceptance Criteria

- Boil-off rate <2% per day: Normal
- Boil-off rate 2-3% per day: Monitor, investigate if trending up
- Boil-off rate >3% per day: Investigate for insulation failure

## 8. Special Tooling for Cryogenic Work

### 8.1 Cryo-Rated Tools

- **Wrenches and Sockets**: Austenitic stainless steel or aluminum bronze
- **Gaskets and Seals**: PTFE or specialized cryo materials
- **Lubricants**: Cryo-compatible (no petroleum-based)
- **Fasteners**: Stainless steel or other cryo-rated materials

### 8.2 Test Equipment

- **Vacuum Gauge**: For vacuum jacket pressure measurement
- **Thermal Imaging Camera**: For insulation integrity surveys
- **Level Sensors**: Capacitance or other non-contact methods
- **Mass Flow Meters**: For boil-off rate measurement

## 9. Personnel Qualification

### 9.1 Minimum Certifications

All personnel performing cryo maintenance must have:

1. **EASA Part 66 License** (or equivalent)
2. **Cryogenic Safety Training** (ISO 21013 compliant)
3. **AMPEL360-BWB-H2 Type Rating**
4. **Confined Space Entry** (if applicable)

### 9.2 Cryo-Specific Training

Required training modules:
- Cryogenic properties and hazards (4 hours)
- Cold burn prevention and first aid (2 hours)
- Cryogenic system maintenance procedures (8 hours)
- Vacuum technology fundamentals (4 hours)
- Annual refresher training (4 hours)

See [10-00-12-34A - Cryo Handling Training](../training-services/10-00-12-34A_Cryo_Handling_Training.md) for details.

## 10. Warm-Up and Cool-Down Procedures

### 10.1 System Warm-Up (for maintenance)

1. Vent all LH2 from system (or transfer to another tank)
2. Purge with warm GN2 (gaseous nitrogen)
3. Continue purging until temperature >0°C
4. Verify no ice formation
5. Final purge with dry air or GN2
6. System ready for maintenance

**Caution**: Never use compressed air on cold components (moisture will freeze)

### 10.2 System Cool-Down (after maintenance)

1. Verify all work complete and inspected
2. Close all access ports and connections
3. Perform leak test at ambient temperature
4. Purge system with GN2
5. Begin slow cool-down with small LH2 quantities
6. Monitor for leaks during cool-down (contraction may open leaks)
7. Gradually increase fill rate
8. Verify vacuum jacket integrity during cool-down

## 11. Documentation Requirements

All cryogenic system maintenance must be documented with:

- Cryo safety work permit (signed)
- Pre-work system purge/warm-up verification
- Vacuum jacket pressure readings (if applicable)
- Boil-off rate measurements
- Thermal imaging results (if performed)
- Leak test results
- Component serial numbers
- Post-maintenance functional test results
- Airworthiness release

## 12. Cross-References

- [10-00-12-01A - Maintenance Services Overview](./10-00-12-01A_Maintenance_Services_Overview.md)
- [10-00-12-04A - H2 System Maintenance](./10-00-12-04A_H2_System_Maintenance.md)
- [10-00-12-24A - Cryo Technical Support](../technical-support/10-00-12-24A_Cryo_Technical_Support.md)
- [10-00-12-34A - Cryo Handling Training](../training-services/10-00-12-34A_Cryo_Handling_Training.md)

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-11 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-12-11*.

---
