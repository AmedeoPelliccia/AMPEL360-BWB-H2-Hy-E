# RQ-PERFORMANCE - Performance Requirements

**Category:** RQ-PERFORMANCE  
**ID Range:** RQ-52-20-01-050 to RQ-52-20-01-067  
**Total Requirements:** 18  
**Priority:** Critical

## Overview

This category contains all performance requirements for the Door L3 Aft Emergency Exit, including opening times, flow rates, reliability metrics, and weight limits.

## Performance Design Philosophy

The emergency exit performance must:
- Meet 90-second evacuation requirement
- Operate reliably across all environmental conditions
- Minimize evacuation time in emergency scenarios
- Maintain performance over 20-year service life
- Achieve 99.95% availability

## Key Requirements Summary

### Timing Requirements (RQ-050 to RQ-055)
- **RQ-52-20-01-050**: Door opening time (powered) = 3 seconds (+1s tolerance)
- **RQ-52-20-01-051**: Door opening time (manual) = 8 seconds maximum
- **RQ-52-20-01-052**: Slide deployment time = 6 seconds (+2s tolerance)
- **RQ-52-20-01-053**: Evacuation flow rate = 70 passengers/min (minimum 55)
- **RQ-52-20-01-054**: Total evacuation time = 75 seconds (90s maximum)
- **RQ-52-20-01-055**: Door closing time = 10 seconds (+2s tolerance)

### Environmental Operating Range (RQ-056)
- **RQ-52-20-01-056**: Operating temperature range = -55°C to +70°C
  - Cold extreme: Arctic operations
  - Hot extreme: Desert ground operations
  - Performance must not degrade

### Service Life (RQ-057 to RQ-058)
- **RQ-52-20-01-057**: Service life cycles = 20,000 minimum
- **RQ-52-20-01-058**: Service life years = 20 years minimum
  - Accounts for aging and degradation
  - Assumes 2.7 cycles per day average

### Force & Effort (RQ-059 to RQ-060)
- **RQ-52-20-01-059**: Manual opening force = 30 lbf maximum
  - 95th percentile female capability
  - Measured at handle
- **RQ-52-20-01-060**: Slide inflation pressure = 3.0 psi (±0.3 psi)
  - Optimized for rapid inflation
  - Maintains structural integrity

### Capacity (RQ-061 to RQ-062)
- **RQ-52-20-01-061**: Slide support capacity = 220 persons minimum
  - Simultaneous on slide/raft
  - Includes emergency equipment weight
- **RQ-52-20-01-062**: Door weight = 142 kg maximum
  - Including all mechanisms and hardware
  - Critical for aircraft weight budget

### Reliability & Maintenance (RQ-063 to RQ-065)
- **RQ-52-20-01-063**: Reliability MTBF = 50,000 flight hours minimum
- **RQ-52-20-01-064**: Leak rate at cabin pressure = 0.05 lb/min maximum
- **RQ-52-20-01-065**: Latch engagement force = 50 N (±10 N)

### Slide Performance (RQ-066 to RQ-067)
- **RQ-52-20-01-066**: Slide angle range = 35-48 degrees (±2°)
  - Accommodates ground height variation
  - Optimized evacuation angle
- **RQ-52-20-01-067**: System availability = 99.95% minimum
  - Includes all failure modes
  - Mission reliability target

## Critical Performance Metrics

### Emergency Evacuation Timeline
```
T+0s:   Emergency declared, crew activates
T+3s:   Door fully open (powered mode)
T+6s:   Slide fully deployed and usable
T+9s:   First passenger exits
T+75s:  All passengers evacuated (target)
T+90s:  Regulatory maximum time
```

### Performance Under Stress

| Condition | Opening Time | Slide Deploy | Notes |
|-----------|--------------|--------------|-------|
| Normal (25°C) | 3.0s | 6.0s | Baseline |
| Cold (-55°C) | 3.5s | 7.0s | Viscosity effects |
| Hot (+70°C) | 3.2s | 6.5s | Gas expansion |
| Manual Mode | 8.0s | 8.0s | No power assist |
| Post-Impact | 8.0s | 8.0s | Damage tolerance |

## Evacuation Flow Analysis

### Single-Lane Capacity
- **Theoretical**: 80 pax/min
- **Practical**: 70 pax/min (design target)
- **Minimum**: 55 pax/min (acceptable)

### Dual-Lane Configuration
- **Effective**: 2 × 70 = 140 pax/min theoretical
- **Practical**: 110 pax/min (flow interference)
- **Advantage**: Redundancy if one lane blocked

### Bottleneck Analysis
1. **Door Opening**: 3-8 seconds (system dependent)
2. **First Passenger**: +3 seconds (reaction time)
3. **Steady Flow**: 0.86s per passenger
4. **Last Passenger**: Queue dependent

## Reliability Metrics

### Mean Time Between Failures (MTBF)
- **Target**: 50,000 flight hours
- **Calculation Basis**: 
  - 3.5 flight hours per cycle average
  - 14,285 cycles between failures
  - 0.7 failures per 10,000 cycles

### Failure Rate Categories
| Component | Failure Rate | MTBF |
|-----------|--------------|------|
| Latches | 5×10⁻⁶/hr | 200,000 hr |
| Power Assist | 2×10⁻⁵/hr | 50,000 hr |
| Slide System | 1×10⁻⁵/hr | 100,000 hr |
| Sensors | 8×10⁻⁶/hr | 125,000 hr |
| **Overall System** | **2×10⁻⁵/hr** | **50,000 hr** |

## Weight Budget Breakdown

| Component | Weight (kg) | Percentage |
|-----------|-------------|------------|
| Door Structure | 65 | 46% |
| Mechanisms | 28 | 20% |
| Slide Pack | 35 | 25% |
| Seals & Hardware | 10 | 7% |
| Sensors & Wiring | 4 | 2% |
| **Total** | **142** | **100%** |

## Environmental Performance

### Temperature Effects
- **Cold (-55°C)**:
  - Hydraulic fluid viscosity increase
  - Seal stiffness increase
  - Gas pressure decrease
  - Battery capacity reduction
  
- **Hot (+70°C)**:
  - Material strength reduction
  - Seal degradation acceleration
  - Gas pressure increase
  - Lubrication breakdown

### Altitude Effects
- **Operating Ceiling**: 45,000 ft
- **Pressure Differential**: 9.5 psi maximum
- **Seal Performance**: Maintained across range
- **Gas Inflation**: Compensated for altitude

## Verification Approach

| Method | Requirements | Test Type |
|--------|--------------|-----------|
| Test | 14 (78%) | Physical measurement |
| Analysis | 3 (17%) | Calculation/simulation |
| Demonstration | 1 (5%) | Evacuation trial |

## Test Acceptance Criteria

### Opening Time Test
- **Sample Size**: 30 cycles minimum
- **Pass Criteria**: Mean ≤ 3.0s, Max ≤ 4.0s (powered)
- **Conditions**: Ambient, cold, hot
- **Power States**: Full, degraded, manual

### Slide Deployment Test
- **Sample Size**: 10 deployments minimum
- **Pass Criteria**: 100% success, time ≤ 8.0s
- **Conditions**: All environmental extremes
- **Configurations**: Armed, emergency override

### Evacuation Demo Test
- **Sample Size**: Full aircraft evacuation
- **Pass Criteria**: 90 seconds maximum
- **Participants**: Mixed demographics
- **Conditions**: Half exits available, dark cabin

## Performance Margins

| Parameter | Requirement | Margin | Design Target |
|-----------|-------------|--------|---------------|
| Opening Time | 8s max | 20% | 6.7s |
| Slide Deploy | 8s max | 25% | 6.0s |
| Flow Rate | 55 pax/min | 27% | 70 pax/min |
| Manual Force | 30 lbf | 33% | 20 lbf |
| MTBF | 50k hr | 40% | 70k hr |

## Degraded Mode Performance

### Partial Power Loss
- Opening time: 5 seconds (vs 3s normal)
- Still meets 8-second requirement
- Batteries provide backup

### Complete Power Loss
- Manual mode available
- Opening time: 8 seconds maximum
- No slide automatic deployment

### Post-Impact Scenario
- Structure damaged but functional
- Manual override accessible
- 8-second opening maintained

## Performance Monitoring

### In-Service Data Collection
- Opening time per event
- Slide deployment reliability
- Latch engagement cycles
- Maintenance actions required

### Fleet Performance Tracking
- Aggregate failure rates
- Performance degradation trends
- Preventive maintenance optimization
- Design improvement identification

## Compliance Matrix

| Requirement | CS25 Reference | Verification | Status |
|-------------|----------------|--------------|--------|
| RQ-050/051 | 25.807(c) | Test | Defined |
| RQ-052 | 25.809 | Test | Defined |
| RQ-053/054 | 25.803(c) | Demonstration | Defined |
| RQ-063 | 25.1309 | Analysis | Defined |

## Related Documents

- **02_SAFETY**: Reliability analysis and FMEA
- **06_ENGINEERING**: Performance calculations
- **07_V_AND_V**: Test procedures and results
- **11_OPERATIONS_AND_MAINTENANCE**: Performance monitoring

---

**Document Control**  
**Version:** 1.0  
**Date:** 2025-11-04  
**Status:** Released  
**Approved by:** Chief Performance Engineer
