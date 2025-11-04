# Capacity Analysis - Door L1 Forward Production

**Document:** AMPEL360-52-10-01-CAPACITY  
**Date:** 2025-11-03  
**Status:** DRAFT

---

## Executive Summary

This document analyzes the production capacity requirements and constraints for the Door L1 Forward manufacturing at the target rate of 8 units per month. The analysis identifies the **autoclave cure process** as the primary capacity constraint and provides recommendations for achieving and maintaining target production rates.

---

## 1. PROCESS CAPACITY ANALYSIS

### 1.1 Process Step Capacity

| Process Step | Cycle Time | Setup Time | Daily Capacity | Monthly Capacity* | Utilization @ 8/mo |
|--------------|------------|------------|----------------|-------------------|-------------------|
| Material Kitting | 8 hrs | 1 hr | 1.0 units | 22 units | 36% |
| Composite Layup | 16 hrs | 2 hrs | 0.5 units | 11 units | 73% |
| Vacuum Bagging | 4 hrs | 0.5 hrs | 2.0 units | 44 units | 18% |
| **Autoclave Cure** | **8 hrs** | **2 hrs** | **0.8 units** | **17 units** | **47%** |
| NDT Inspection | 6 hrs | 1 hr | 1.3 units | 29 units | 28% |
| Trim & Drill | 8 hrs | 1 hr | 1.0 units | 22 units | 36% |
| Assembly | 12 hrs | 2 hrs | 0.6 units | 13 units | 62% |
| Painting | 8 hrs | 2 hrs | 0.8 units | 18 units | 44% |
| Final Test | 6 hrs | 1 hr | 1.3 units | 29 units | 28% |

*Monthly capacity based on 22 working days, 2 shifts, 85% availability

### 1.2 Bottleneck Identification

**Primary Bottleneck: Autoclave Cure**
- **Theoretical capacity:** 17 units/month (2 shifts)
- **Target rate:** 8 units/month
- **Buffer:** 113% (adequate for current rate)
- **Constraint:** External service provider dependency

**Secondary Bottleneck: Composite Layup**
- **Capacity:** 11 units/month
- **Buffer:** 38% (requires attention at higher rates)
- **Constraint:** Clean room space, skilled labor

---

## 2. AUTOCLAVE CAPACITY DEEP DIVE

### 2.1 Autoclave Specifications
- **Internal dimensions:** 2.5m diameter × 6m length
- **Door capacity:** 2 complete assemblies OR 4 panels per run
- **Temperature range:** Up to 200°C
- **Pressure range:** Up to 10 bar
- **Service provider:** ACT Aerospace (primary)

### 2.2 Cure Cycle Analysis

**Standard Cycle SC-001:**
```
Phase 1: Ramp-up
  - Rate: 2°C/min
  - Duration: 90 minutes (to 180°C)
  - Pressure: Ramp to 7 bar

Phase 2: Dwell
  - Temperature: 180±5°C
  - Pressure: 7.0±0.3 bar
  - Duration: 120 minutes

Phase 3: Cooldown
  - Rate: 3°C/min (max)
  - Duration: 60 minutes (to 100°C)
  - Pressure: Hold until 100°C

Total cycle time: 4.25 hours (255 minutes)
```

**Full Cycle Including Setup:**
- Pre-heat autoclave: 30 minutes
- Load parts: 45 minutes
- Connect instrumentation: 15 minutes
- Cure cycle: 255 minutes
- Unload parts: 30 minutes
- **Total: 6.25 hours per run**

### 2.3 Monthly Autoclave Capacity

**Two-Shift Operation:**
- Operating hours: 16 hrs/day × 22 days = 352 hours/month
- Availability factor: 85% (maintenance, breakdowns)
- Available hours: 352 × 0.85 = 299 hours/month
- Runs per month: 299 ÷ 6.25 = 48 runs
- **Doors per month: 48 × 2 = 96 doors** (theoretical maximum)

**Current Utilization:**
- Required runs for 8 doors/month: 4 runs
- Actual utilization: 4 ÷ 48 = **8.3%**
- **Significant excess capacity available**

### 2.4 Capacity Constraints

**Physical Constraints:**
- Autoclave internal volume: 29.5 m³
- Door envelope: ~6 m³ per assembly
- **Maximum 2 doors per run** (adequate clearance required)

**Operational Constraints:**
- Service provider availability
- Transportation to/from facility (30 km)
- Scheduling coordination
- Emergency/priority work conflicts

---

## 3. LABOR CAPACITY ANALYSIS

### 3.1 Workforce Requirements

**Steady State (8 units/month):**

| Role | Headcount | Utilization | Notes |
|------|-----------|-------------|-------|
| Composite Technician | 4 | 73% | Layup operations |
| Assembly Mechanic | 3 | 62% | Final assembly |
| Inspector/QC | 2 | 40% | All inspections |
| Material Handler | 1 | 36% | Kitting, shipping |
| Paint Technician | 1 | 44% | Finishing |
| NDT Technician | 1 | 28% | Part-time/contract |
| **Total** | **12** | **54% avg** | 2-shift operation |

### 3.2 Skill Level Mix

| Skill Level | Required | Available | Gap |
|-------------|----------|-----------|-----|
| Advanced (Level 3) | 5 | 0 | -5 |
| Intermediate (Level 2) | 5 | 0 | -5 |
| Basic (Level 1) | 2 | 0 | -2 |
| **Total** | **12** | **0** | **-12** |

**Critical Skills:**
- Composite layup (advanced)
- Vacuum bagging (intermediate)
- Composite trimming (advanced)
- Mechanical assembly (intermediate)
- NDT Level II (certified)

---

## 4. FACILITY CAPACITY

### 4.1 Space Requirements

| Area | Required (m²) | Available | Status |
|------|---------------|-----------|--------|
| Clean Room | 200 | TBD | Not identified |
| Trim/Drill | 150 | TBD | Not identified |
| Assembly | 200 | TBD | Not identified |
| Storage | 300 | TBD | Not identified |
| Quality Lab | 50 | TBD | Not identified |
| Office | 100 | TBD | Not identified |
| **Total** | **1,000** | **0** | **Gap** |

### 4.2 Environmental Controls

**Clean Room Requirements:**
- Class: ISO 8 (100,000 particles/ft³)
- Temperature: 23±2°C
- Humidity: 50±10% RH
- Air changes: 10-15 per hour
- Positive pressure: +5 Pa

**Material Storage:**
- Freezer capacity: 100 ft³ (-18±2°C)
- Climate-controlled: 50 m² (23°C, 50% RH)
- Shelf life tracking system required

---

## 5. EQUIPMENT CAPACITY

### 5.1 Critical Equipment

| Equipment | Qty | Capacity | Utilization |
|-----------|-----|----------|-------------|
| Cure mold | 1 | 1 at a time | 47% |
| Trim fixture | 1 | 1 at a time | 36% |
| Assembly fixture | 1 | 1 at a time | 62% |
| CMM (coordinate measuring) | 1 | 3/day | 27% |
| Paint booth | 1 | 2/day | 44% |
| Freezer | 1 | 100 ft³ | 60% |

**No equipment bottlenecks identified at 8 units/month**

---

## 6. CAPACITY RAMP SCENARIOS

### 6.1 Rate Ramp Analysis

| Target Rate | Primary Constraint | Action Required |
|-------------|-------------------|------------------|
| 2 units/month | None | Within all capacities |
| 4 units/month | None | Within all capacities |
| 8 units/month | Layup labor | Add 1-2 technicians |
| 12 units/month | Layup space | Additional clean room |
| 16 units/month | Autoclave | Dedicated internal autoclave |
| 20+ units/month | Multiple | Facility expansion, automation |

### 6.2 Rate Increase Triggers

**From 8 to 12 units/month:**
- Requires: +2 composite technicians
- Clean room expansion: +100 m²
- Additional cure mold: $250k
- Lead time: 6 months

**From 12 to 16 units/month:**
- Requires: Internal autoclave ($2M)
- Facility expansion: +500 m²
- Staff increase: +8 personnel
- Lead time: 18 months

---

## 7. CAPACITY RISKS

| Risk | Impact | Mitigation |
|------|--------|------------|
| Autoclave provider unavailable | HIGH | Backup service contract |
| Skilled labor shortage | HIGH | Training program, recruitment |
| Clean room contamination | MEDIUM | Strict protocols, monitoring |
| Equipment breakdown | MEDIUM | Preventive maintenance, spares |
| Material supply disruption | HIGH | Safety stock, dual sourcing |
| Facility access loss | HIGH | Business continuity plan |

---

## 8. RECOMMENDATIONS

### 8.1 Immediate Actions (0-6 months)
1. **Secure autoclave service contract** with ACT Aerospace
2. **Establish backup autoclave provider** for risk mitigation
3. **Begin recruitment** of composite technicians (4 positions)
4. **Identify facility** meeting clean room requirements
5. **Procure long-lead tooling** (cure mold, fixtures)

### 8.2 Short-term Actions (6-12 months)
1. **Complete facility setup** and environmental certification
2. **Hire and train workforce** to full complement
3. **Validate processes** with prototype builds
4. **Establish quality system** with supplier partnerships

### 8.3 Long-term Strategy (1-3 years)
1. **Monitor capacity utilization** against targets
2. **Plan for rate increases** beyond 8 units/month
3. **Evaluate automation opportunities** (AFP, robotic drilling)
4. **Consider internal autoclave** at 16+ units/month
5. **Implement continuous improvement** to increase throughput

---

## 9. CAPACITY INVESTMENT SUMMARY

| Investment Area | Cost ($k) | Impact on Capacity |
|-----------------|-----------|-------------------|
| Cure mold (primary) | 250 | Enables production |
| Trim/drill fixtures | 50 | Enables production |
| Assembly fixtures | 75 | Enables production |
| Clean room setup | 100 | Enables production |
| Inspection equipment | 45 | Enables production |
| Material handling | 50 | Efficiency improvement |
| IT/MES system | 30 | Efficiency improvement |
| **Phase 1 Total** | **600** | **Enable 0-8 units/month** |
| | | |
| Second cure mold | 250 | Enable 8-12 units/month |
| Clean room expansion | 150 | Enable 8-12 units/month |
| Additional tooling | 100 | Enable 8-12 units/month |
| **Phase 2 Total** | **500** | **Enable 8-12 units/month** |
| | | |
| Internal autoclave | 2000 | Enable 16+ units/month |
| Facility expansion | 500 | Enable 16+ units/month |
| Automation (AFP) | 1000 | Reduce labor, increase quality |
| **Phase 3 Total** | **3500** | **Enable 16+ units/month** |

---

**Document Control:**
- **Version:** Draft 1.0
- **Author:** AMPEL360 Production Planning
- **Review Date:** 2026-Q1
