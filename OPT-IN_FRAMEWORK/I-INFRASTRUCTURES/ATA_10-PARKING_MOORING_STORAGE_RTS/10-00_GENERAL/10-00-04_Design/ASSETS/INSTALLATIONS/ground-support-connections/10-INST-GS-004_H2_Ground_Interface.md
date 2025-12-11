# 10-INST-GS-004 - H2 Ground Interface

## 1. Purpose

Installation and operation of hydrogen fueling interface between ground storage and AMPEL360-BWB-H2 aircraft.

## 2. Scope

- LH2 transfer connection interface
- Safety systems and interlocks
- Grounding and bonding requirements
- Emergency shutdown systems

## 3. H2 Ground Interface Components

### 3.1 LH2 Transfer Connection

**Type**: Bayonet quick-connect coupling
**Size**: 2-3" diameter (transfer rate dependent)
**Material**: Stainless steel 316L
**Rating**: Cryogenic (-253°C), vacuum-insulated
**Standard**: SAE AS6968 compliant

### 3.2 Safety Systems

**Required Safety Features**:
- Emergency breakaway coupling (separates if excess force)
- Deadman switch (operator must hold to maintain flow)
- Emergency shutdown button (accessible from multiple locations)
- H2 detection interlocked to shutdown
- Automatic shutdown on coupling disconnect

### 3.3 Grounding and Bonding

**Critical for H2 Safety**:
- Ground cable from aircraft to ground grid (<0.003 ohms)
- Bonding cable from fueling equipment to aircraft
- Verify bonding before connecting LH2 coupling
- Continuous bonding monitoring during fueling

## 4. Installation Procedure

### 4.1 Fueling Interface Installation

1. Survey fueling area and mark H2 safety zones
2. Install grounding grid (copper, interconnected)
3. Install fueling pedestal or mobile equipment parking area
4. Install H2 detection sensors (per 10-INST-H2-002)
5. Install emergency shutdown stations (4 minimum around fueling area)
6. Install LH2 transfer coupling with vacuum-insulated hose
7. Install safety shower and eyewash within 25 ft
8. Install fire suppression equipment
9. Post H2 safety signage and establish exclusion zones

### 4.2 Testing and Commissioning

1. Test all safety systems (emergency shutdown, detection, alarms)
2. Leak test LH2 connections with nitrogen
3. Verify bonding and grounding (<0.003 ohms)
4. Functional test breakaway coupling
5. Train all fueling personnel
6. Conduct emergency drill
7. Commission system with authority approval

## 5. Operational Safety

**Before Each Fueling**:
- Verify H2 detection system operational
- Test emergency shutdown
- Verify safety equipment available (PPE, fire extinguishers, etc.)
- Establish exclusion zone (25 ft minimum)
- Post fueling in progress signs
- Assign safety observer

**During Fueling**:
- Continuous H2 monitoring
- Operator at fueling panel with deadman switch
- No ignition sources within 50 ft
- Safety observer monitors operations
- Wind direction monitoring (for vapor cloud drift)

**After Fueling**:
- Purge transfer line with nitrogen
- Disconnect and cap aircraft connection
- Remove bonding cables
- Verify no H2 leaks (detection sensors)
- Clear exclusion zone

## 6. Emergency Procedures

**H2 Leak During Fueling**:
1. Activate emergency shutdown immediately
2. Do not disconnect coupling (may worsen leak)
3. Evacuate area (100 ft minimum)
4. Allow H2 to disperse naturally (rises and disperses)
5. Monitor H2 concentration remotely
6. Summon emergency response
7. Re-enter only when H2 <25% LEL

**Fire at Fueling Interface**:
1. Activate emergency shutdown
2. Evacuate immediately
3. Summon fire department
4. DO NOT extinguish H2 fire (allow controlled burn)
5. Protect exposures with water (cool adjacent equipment)

## 7. BWB/H2 Considerations

- BWB fuel connection location may differ from conventional aircraft
- Multiple fuel connection points possible (distributed tanks)
- Large fuel capacity may require extended fueling time
- BWB geometry may affect fueling equipment positioning

## 8. Quality Assurance

- Daily functional test of safety systems when in use
- Weekly leak test of all connections
- Monthly calibration of H2 detection sensors
- Quarterly emergency drill
- Annual complete system inspection and recertification

## 9. Cross-References

- **10-INST-H2-001** - H2 Venting System Installation
- **10-INST-H2-002** - H2 Detection Sensors
- **10-INST-H2-003** - Cryo Safety Equipment
- **ATA 28** - Fuel System
- **SAE AS6968** - Hydrogen Aircraft GSE
- **NFPA 2** - Hydrogen Technologies Code

## 10. Revision History

| Rev | Date       | Author              | Description          |
|-----|------------|---------------------|----------------------|
| A   | 2025-12-09 | Amedeo Pelliccia    | Initial release      |

---

## Document Control

- **Document ID**: 10-INST-GS-004
- **Revision**: A
- **Status**: DRAFT - Subject to human review and approval
- **Safety Critical**: YES
- **Owner**: AMPEL360 Documentation WG
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
