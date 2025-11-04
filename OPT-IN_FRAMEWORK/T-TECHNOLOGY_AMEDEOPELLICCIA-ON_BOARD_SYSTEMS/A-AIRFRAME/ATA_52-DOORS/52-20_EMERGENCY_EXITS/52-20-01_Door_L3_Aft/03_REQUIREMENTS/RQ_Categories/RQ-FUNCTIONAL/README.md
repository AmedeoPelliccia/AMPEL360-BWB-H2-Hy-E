# RQ-FUNCTIONAL - Functional Requirements

**Category:** RQ-FUNCTIONAL  
**ID Range:** RQ-52-20-01-020 to RQ-52-20-01-047  
**Total Requirements:** 28  
**Priority:** Critical

## Overview

This category contains all functional requirements for the Door L3 Aft Emergency Exit, including emergency opening, slide deployment, arming/disarming, and manual override capabilities.

## Functional Design Philosophy

The emergency exit must:
- Open reliably in all emergency scenarios
- Deploy evacuation slide automatically when armed
- Provide manual override capability under all conditions
- Indicate armed/disarmed status clearly to crew
- Operate with power loss or system failures

## Key Requirements Summary

### Emergency Opening (RQ-020 to RQ-024)
- **RQ-52-20-01-020**: Emergency door opening capability in all modes
- **RQ-52-20-01-021**: Dual activation modes (powered and manual)
- **RQ-52-20-01-022**: Manual opening force maximum 30 lbf
- **RQ-52-20-01-023**: Automatic slide deployment when armed
- **RQ-52-20-01-024**: Slide arming/disarming system functionality

### Door Sealing & Pressure (RQ-025 to RQ-027)
- **RQ-52-20-01-025**: Door pressure seal function maintains cabin pressure
- **RQ-52-20-01-026**: Pressure interlock prevents opening > 0.2 psi differential
- **RQ-52-20-01-027**: Emergency override function bypasses interlocks

### Power Assist & Sensing (RQ-028 to RQ-030)
- **RQ-52-20-01-028**: Power assist opening reduces cycle time
- **RQ-52-20-01-029**: Triple redundant position sensing (open/closed/armed)
- **RQ-52-20-01-030**: Slide pack opening mechanism releases bustle

### Slide Configuration (RQ-031 to RQ-037)
- **RQ-52-20-01-031**: Dual-lane slide configuration for Type A exit
- **RQ-52-20-01-032**: Visual status indicators (armed, pressure, faults)
- **RQ-52-20-01-033**: Cockpit warning integration (EICAS/ECAM)
- **RQ-52-20-01-034**: Girt bar attachment system to floor
- **RQ-52-20-01-035**: Slide inflation system (compressed gas)
- **RQ-52-20-01-036**: Manual inflation backup system
- **RQ-52-20-01-037**: Slide detachment for ditching scenario

### Operation & Control (RQ-038 to RQ-047)
- **RQ-52-20-01-038**: Interior handle operation by cabin crew
- **RQ-52-20-01-039**: Exterior handle access for ground operations
- **RQ-52-20-01-040**: Door motion sequencing (unlatch, swing, clear)
- **RQ-52-20-01-041**: Fail-safe latch design (cannot fail to unsafe state)
- **RQ-52-20-01-042**: Spring assist mechanism for manual mode
- **RQ-52-20-01-043**: Mechanical advantage system reduces effort
- **RQ-52-20-01-044**: Emergency lighting interface activation
- **RQ-52-20-01-045**: Floor proximity lighting in smoke conditions
- **RQ-52-20-01-046**: Photoluminescent marking for power loss
- **RQ-52-20-01-047**: Slide angle adjustment for ground height variation

## Operational Modes

### Mode 1: Normal Operation (Disarmed)
- Door can be opened normally for servicing
- Slide remains stowed
- No automatic deployment
- Pressure interlock active
- Used during ground operations

### Mode 2: Armed for Flight
- Automatic slide deployment enabled
- Opening triggers slide inflation
- Visual armed indicators illuminated
- Cockpit warning if armed on ground
- Required for takeoff and landing

### Mode 3: Emergency Operation
- Override all interlocks
- Maximum opening speed
- Automatic slide deployment
- Emergency lighting activation
- Operable with all power sources failed

## Functional States

```
[CLOSED & LOCKED] ←→ [OPEN]
        ↓                ↓
   [DISARMED]      [DISARMED]
        ↓                ↓
    [ARMED]  ←→    [SLIDE DEPLOYED]
```

## Critical Functional Sequences

### Sequence 1: Normal Opening (Disarmed)
1. Crew moves disarm lever to DISARMED position
2. Crew unlocks and opens door
3. Door swings outward
4. Slide remains stowed

### Sequence 2: Emergency Evacuation (Armed)
1. Door already in ARMED mode for flight
2. Crew pulls emergency handle
3. Latches release immediately
4. Door swings open (power or manual)
5. Girt bar releases slide pack
6. Slide inflates automatically (6 seconds)
7. Emergency lighting activates

### Sequence 3: Manual Override (Emergency)
1. All power systems failed
2. Crew activates emergency override
3. Mechanical unlocking bypasses all interlocks
4. Manual effort opens door (≤30 lbf)
5. Slide deploys via manual inflation if needed

## Verification Methods

| Method | Requirements | Percentage |
|--------|--------------|------------|
| Test | 17 | 61% |
| Demonstration | 8 | 29% |
| Inspection | 2 | 7% |
| Analysis | 1 | 3% |

## Critical Performance Metrics

- **Opening Time (Powered)**: 3 seconds target, 4 seconds maximum
- **Opening Time (Manual)**: 8 seconds maximum
- **Slide Deployment**: 6 seconds target, 8 seconds maximum
- **Manual Force**: 30 lbf maximum (95th percentile capability)
- **Reliability**: No single failure prevents evacuation

## Human Factors Integration

### Crew Interface
- Intuitive handle design (RED = EMERGENCY)
- Clear armed/disarmed indicators
- Tactile feedback on latch engagement
- Operable with winter gloves

### Passenger Protection
- Crowd surge resistant design
- No pinch points or sharp edges
- Clear evacuation path markings
- Photoluminescent guidance

## Safety Interlocks

1. **Pressure Interlock**: Prevents opening if ΔP > 0.2 psi
2. **Ground Safety**: Warning if armed with weight-on-wheels
3. **Slide Deploy Inhibit**: Prevents deployment in disarmed mode
4. **Emergency Override**: Bypasses all interlocks for safety

## Failure Modes & Mitigations

| Failure | Effect | Mitigation |
|---------|--------|------------|
| Power loss | No powered assist | Manual mode always available |
| Sensor failure | No position indication | 2oo3 voting, visual check |
| Latch jam | Cannot open | Emergency override mechanism |
| Slide failure | No slide | Manual inflation, raft mode |

## Test Requirements

- **Functional Test 1**: 50 opening cycles, all modes
- **Functional Test 2**: Cold soak (-55°C) + operation
- **Functional Test 3**: Hot soak (+70°C) + operation
- **Functional Test 4**: Slide deployment in all conditions
- **Functional Test 5**: Emergency override verification

## Interface Requirements

### Electrical
- 28 VDC power (primary and backup)
- ARINC 429 data bus for status
- Discrete signals for warnings

### Mechanical
- Girt bar attachment to floor structure
- Slide pack mounting provisions
- Handle mechanism integration

### Pneumatic
- Compressed gas bottles for slide inflation
- Manual backup aspiration system

## Compliance Matrix

| Requirement | CS25 Reference | TSO Reference | Status |
|-------------|----------------|---------------|--------|
| RQ-020 | 25.807(c) | - | Defined |
| RQ-023 | 25.809 | TSO-C69c | Defined |
| RQ-026 | 25.783(d) | - | Defined |
| RQ-027 | 25.807(e) | - | Defined |

## Related Documents

- **02_SAFETY**: FMEA and safety analysis
- **04_DESIGN**: Mechanism design and kinematics
- **07_V_AND_V**: Functional test procedures
- **11_OPERATIONS_AND_MAINTENANCE**: Crew procedures manual

---

**Document Control**  
**Version:** 1.0  
**Date:** 2025-11-04  
**Status:** Released  
**Approved by:** Chief Systems Engineer
