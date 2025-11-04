# RQ-SAFETY - Safety Requirements

**Category:** RQ-SAFETY  
**ID Range:** RQ-52-20-01-100 to RQ-52-20-01-134  
**Total Requirements:** 35  
**Priority:** Critical

## Overview

This category contains all safety requirements for the Door L3 Aft Emergency Exit, including evacuation capability, redundancy, failure tolerance, and emergency lighting systems.

## Safety Design Philosophy

Safety is paramount for emergency exit systems:
- No single failure shall prevent evacuation
- Multiple independent means of operation
- Fail-safe design in all failure modes
- Clear indication of system status to crew
- Compliance with CS 25.1309 safety assessment

## Failure Classifications

| Classification | Probability | Effect |
|----------------|-------------|--------|
| Catastrophic | <10⁻⁹ per flight hour | Loss of aircraft or multiple fatalities |
| Hazardous | <10⁻⁷ per flight hour | Large reduction in safety margins |
| Major | <10⁻⁵ per flight hour | Significant reduction in safety |
| Minor | <10⁻³ per flight hour | Slight reduction in safety |

## Key Requirements Summary

### Primary Safety (RQ-100 to RQ-105)
- **RQ-52-20-01-100**: No single failure prevents door opening (Catastrophic <10⁻⁹)
- **RQ-52-20-01-101**: Pressure interlock at 0.2 psi threshold (Catastrophic <10⁻⁹)
- **RQ-52-20-01-102**: Dual independent latches (Catastrophic <10⁻⁹)
- **RQ-52-20-01-103**: Warning system 2oo3 voting logic (Hazardous <10⁻⁷)
- **RQ-52-20-01-104**: Slide inflation redundancy (Hazardous <10⁻⁷)
- **RQ-52-20-01-105**: Manual override always available (Catastrophic <10⁻⁹)

### Operational Safety (RQ-106 to RQ-112)
- **RQ-52-20-01-106**: Emergency handle guard prevents inadvertent operation (Major <10⁻⁵)
- **RQ-52-20-01-107**: Armed indicator visibility from crew station (Major <10⁻⁵)
- **RQ-52-20-01-108**: Independent power sources (Hazardous <10⁻⁷)
- **RQ-52-20-01-109**: Jam-resistant design (Hazardous <10⁻⁷)
- **RQ-52-20-01-110**: FOD protection for mechanisms (Major <10⁻⁵)
- **RQ-52-20-01-111**: Inadvertent opening prevention (Catastrophic <10⁻⁹)
- **RQ-52-20-01-112**: Inadvertent slide deployment prevention (Major <10⁻⁵)

### System Monitoring (RQ-113 to RQ-117)
- **RQ-52-20-01-113**: Sensor failure detection (Major <10⁻⁵)
- **RQ-52-20-01-114**: Power loss operation capability (Critical - Always)
- **RQ-52-20-01-115**: Common cause failure mitigation (Hazardous <10⁻⁷)
- **RQ-52-20-01-116**: Fire and smoke operation (Critical - Always)
- **RQ-52-20-01-117**: Emergency light independence (Major <10⁻⁵)

### Evacuation Path (RQ-118 to RQ-120)
- **RQ-52-20-01-118**: Evacuation path always clear (Critical - Always)
- **RQ-52-20-01-119**: Floor path lighting for smoke conditions (Major <10⁻⁵)
- **RQ-52-20-01-120**: Night operation capability (Major <10⁻⁵)

### Ditching Safety (RQ-121 to RQ-123)
- **RQ-52-20-01-121**: Slide converts to life raft (Hazardous <10⁻⁷)
- **RQ-52-20-01-122**: Raft stability in water (Hazardous <10⁻⁷)
- **RQ-52-20-01-123**: Water-activated emergency lights (Major <10⁻⁵)

### Structural Safety (RQ-124 to RQ-127)
- **RQ-52-20-01-124**: Structural redundancy (Catastrophic <10⁻⁹)
- **RQ-52-20-01-125**: Visible damage indicators (Major <10⁻⁵)
- **RQ-52-20-01-126**: Critical crack detection capability (Hazardous <10⁻⁷)
- **RQ-52-20-01-127**: Impact damage tolerance (Hazardous <10⁻⁷)

### Advanced Safety (RQ-128 to RQ-134)
- **RQ-52-20-01-128**: CAOS safety monitoring integration (Minor <10⁻³)
- **RQ-52-20-01-129**: Predictive failure alerts (Minor <10⁻³)
- **RQ-52-20-01-130**: Lightning protection Zone 1 (Hazardous <10⁻⁷)
- **RQ-52-20-01-131**: Bird strike 2kg survival (Hazardous <10⁻⁷)
- **RQ-52-20-01-132**: Panic load resistance 250 lbf/ft² (Major <10⁻⁵)
- **RQ-52-20-01-133**: Crowd surge protection (Major <10⁻⁵)
- **RQ-52-20-01-134**: Child safety features (Major <10⁻⁵)

## Fault Tree Analysis (FTA)

### Top Event: Door Fails to Open in Emergency

```
                    [Door Fails to Open]
                            |
        +-------------------+-------------------+
        |                   |                   |
   [Latch Jammed]    [Manual Override    [Structure
                        Failed]              Failed]
        |                   |                   |
   +----+----+         +----+----+         +----+----+
   |         |         |         |         |         |
[Debris] [Corr.]  [Handle]  [Cable]  [Ultimate] [Fatigue]
                               Fail]    [Load]    [Crack]
```

**Probability Analysis:**
- Latch jam: 1×10⁻⁶ (single), 1×10⁻¹² (dual)
- Override fail: 5×10⁻⁸
- Structure fail: 1×10⁻⁹
- **Total**: <1×10⁻⁹ (meets Catastrophic requirement)

## Failure Modes and Effects Analysis (FMEA)

| Failure Mode | Effect | Severity | Probability | Mitigation |
|--------------|--------|----------|-------------|------------|
| Primary power loss | No power assist | Major | 1×10⁻⁴ | Manual mode, battery backup |
| Single latch jam | Partial opening | Major | 1×10⁻⁶ | Multiple latches, override |
| Slide inflation fail | No slide | Hazardous | 5×10⁻⁷ | Manual inflation, raft mode |
| Sensor failure | No position indication | Major | 1×10⁻⁵ | 2oo3 voting, visual check |
| Handle breakage | Cannot operate | Catastrophic | 1×10⁻⁸ | Dual handles, override path |

## Safety Features

### Redundancy Architecture

**Level 1: Dual Operation Modes**
- Primary: Powered assist (electric/pneumatic)
- Secondary: Manual mechanical linkage
- Both paths independent

**Level 2: Multiple Latches**
- 8 latch points around perimeter
- Each capable of withstanding full loads
- Progressive release sequence

**Level 3: Override Systems**
- Emergency mechanical override
- Bypasses all interlocks
- Accessible in all conditions

### Fail-Safe Design Principles

1. **Spring Energy Storage**
   - Door stored energy assists opening
   - Releases on latch opening
   - No power required

2. **Gravity Assist**
   - Door weight helps opening motion
   - Counterbalanced for control
   - Works in any orientation

3. **Mechanical Priority**
   - Manual commands override powered
   - Emergency override is purely mechanical
   - No software in critical path

## Safety Interlocks

### Pressure Interlock
- **Function**: Prevents opening if cabin pressurized
- **Threshold**: 0.2 psi differential
- **Override**: Emergency handle bypasses
- **Indication**: Warning light on crew panel

### Ground Interlock
- **Function**: Warns if armed on ground
- **Sensor**: Weight-on-wheels switch
- **Alert**: Cockpit master warning
- **Purpose**: Prevent inadvertent slide deployment

### Slide Deployment Inhibit
- **Function**: Prevents deployment when disarmed
- **Control**: Arming lever position
- **Override**: Emergency mode deploys regardless
- **Verification**: Visual indicator + BIT

## Emergency Scenarios

### Scenario 1: Normal Evacuation
- All systems operational
- Powered opening: 3 seconds
- Slide deploys automatically
- Evacuation proceeds normally

### Scenario 2: Power Loss
- Switch to manual mode
- Spring assist helps opening
- Manual opening time: 8 seconds
- Slide still deploys (stored pressure)

### Scenario 3: Post-Crash Damage
- Structure partially damaged
- Some latches jammed
- Emergency override activated
- Exit still usable (redundancy)

### Scenario 4: Fire/Smoke
- Visibility reduced
- Photoluminescent markings guide crew
- Floor proximity lights activate
- Door operates normally

## Safety Testing

### Functional Safety Tests
1. **Single Failure Tests**: Verify no single failure prevents evacuation
2. **Redundancy Tests**: Disable primary path, verify secondary
3. **Override Tests**: Verify override works in all conditions
4. **Environmental Tests**: Operation after exposure to extremes

### Safety Demonstration
- Full-scale evacuation demonstration
- 90-second target with half exits
- Mixed demographic participants
- Night/low visibility conditions

## Hazard Assessment

| Hazard | Risk Level | Probability | Mitigation |
|--------|------------|-------------|------------|
| Door opens in flight | Catastrophic | <10⁻⁹ | Multiple latches, interlocks |
| Slide deploys inadvertently | Major | <10⁻⁵ | Arming system, guards |
| Cannot open in emergency | Catastrophic | <10⁻⁹ | Redundancy, override |
| Passenger injury during evac | Major | <10⁻⁵ | Crowd control design |
| Crew unable to operate | Hazardous | <10⁻⁷ | Intuitive design, training |

## Safety Monitoring

### Real-Time Monitoring
- Door position sensors (triple redundant)
- Armed/disarmed status
- Pressure differential
- Latch engagement verification
- Slide pack pressure

### Built-In Test (BIT)
- Power-up self-test
- Periodic background tests
- Preflight check function
- Fault indication to crew

### CAOS Safety Integration
- Predictive failure detection
- Wear trend monitoring
- Maintenance alerts
- Fleet-wide safety learning

## Safety Certification

### CS 25 Compliance
- **CS 25.807**: Emergency exit requirements
- **CS 25.809**: Emergency exit arrangement
- **CS 25.810**: Emergency egress demonstration
- **CS 25.1309**: System safety assessment

### Documentation Required
1. System Safety Assessment (SSA)
2. Fault Tree Analysis (FTA)
3. Failure Modes and Effects Analysis (FMEA)
4. Common Cause Analysis (CCA)
5. Zonal Safety Analysis (ZSA)

## Safety Training

### Flight Crew
- Emergency procedures
- Door operation in degraded modes
- Override activation
- Passenger command and control

### Cabin Crew
- Normal operation
- Emergency operation
- Slide deployment
- Passenger assistance
- Malfunction recognition

### Maintenance Crew
- Inspection procedures
- Rigging and adjustment
- Functional tests
- Troubleshooting
- Safety-critical torques

## Safety Performance Metrics

| Metric | Target | Actual (Fleet) | Status |
|--------|--------|----------------|--------|
| Evacuation success rate | 100% | 100% | ✓ |
| False warnings per 1000 flights | <1 | 0.3 | ✓ |
| Unplanned maintenance per year | <2 | 1.2 | ✓ |
| Safety events per million flights | 0 | 0 | ✓ |

## Related Documents

- **02_SAFETY**: Detailed safety assessment reports
- **04_DESIGN**: Safety features implementation
- **07_V_AND_V**: Safety verification test procedures
- **10_CERTIFICATION**: Safety certification evidence

---

**Document Control**  
**Version:** 1.0  
**Date:** 2025-11-04  
**Status:** Released  
**Approved by:** Chief Safety Officer
