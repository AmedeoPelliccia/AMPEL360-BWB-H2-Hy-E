# ICD-02-00-28-002: Tank Sequencing Control

**Version:** 1.0.0  
**Status:** Active

## Interface Description

Control interface for H2 fuel tank sequencing during flight operations to maintain optimal weight distribution and center of gravity.

## Purpose

Manage fuel consumption from multiple tanks to:
- Maintain center of gravity within limits
- Optimize fuel cell feed pressure
- Balance tank pressures
- Minimize boil-off losses
- Ensure proper fuel distribution

## Tank Configuration

### AMPEL360 H2 Tank Layout
- **CTR-1**: Forward center tank (2,500 kg capacity)
- **CTR-2**: Aft center tank (2,500 kg capacity)
- **WING-L**: Left wing tank (1,500 kg capacity)
- **WING-R**: Right wing tank (1,500 kg capacity)
- **Total Capacity**: 8,000 kg LH2

## Sequencing Logic

### Normal Operations Sequence

**Phase 1: Takeoff & Climb (0-30 min)**
- Feed from center tanks (CTR-1 and CTR-2 equally)
- Maintains neutral CG
- High feed pressure for fuel cells

**Phase 2: Cruise (30 min - Top of Descent)**
- Primary: CTR-1 (forward center)
- Secondary: WING-L and WING-R (balanced)
- Maintains forward CG for optimal cruise efficiency

**Phase 3: Descent & Landing**
- Feed from CTR-2 (aft center)
- Shift CG aft for landing configuration
- Reserve fuel management

### Emergency Sequence
- Isolate leaking tank immediately
- Feed from remaining tanks with CG compensation
- CAOS automatic rebalancing

## Control Commands

### Operations → Tank Control System

**Tank Selection:**
```
TANK_SELECT:
  primary_tank: CTR-1
  secondary_tank: CTR-2
  mode: AUTO | MANUAL
```

**Fuel Transfer:**
```
TRANSFER_COMMAND:
  from_tank: WING-L
  to_tank: CTR-1
  rate_kgh: 50.0
```

**Emergency Isolation:**
```
ISOLATE_TANK:
  tank_id: CTR-1
  reason: LEAK_DETECTED
  timestamp: ISO8601
```

## Monitoring Parameters

| Parameter | Normal Range | Caution | Warning |
|-----------|--------------|---------|---------|
| CG Position | 20-35% MAC | <18% or >37% | <15% or >40% |
| Tank Imbalance | <200 kg | 200-500 kg | >500 kg |
| Feed Pressure | 2.5-3.0 bar | 2.0-2.5 bar | <2.0 bar |
| Transfer Rate | 0-100 kg/h | - | >120 kg/h |

## Interface Requirements

**RQ-ICD-02-28-010:** Automatic sequencing enabled by default  
**RQ-ICD-02-28-011:** Manual override available to flight crew  
**RQ-ICD-02-28-012:** CG limits enforced in all modes  
**RQ-ICD-02-28-013:** Tank imbalance alert within 30 seconds

## CAOS Integration

### Predictive Sequencing
- AI-optimized tank sequence for route
- Weather-adaptive fuel planning
- Real-time CG optimization
- Boil-off minimization

### Automatic Rebalancing
- Continuous CG monitoring
- Automatic transfer commands
- Predictive trim adjustment
- Fleet learning applied

## Crew Procedures

### Normal Operation
1. Verify AUTO mode selected
2. Monitor fuel quantity and CG display
3. CAOS provides optimal sequence
4. Manual intervention only if required

### Abnormal Operation
1. Select MANUAL mode if AUTO fails
2. Follow tank sequence checklist
3. Monitor CG limits continuously
4. Coordinate with ground support

## Safety Features

### CG Protection
- Hard limits enforced by flight control system
- Cannot command transfer that violates CG limits
- Automatic transfer if approaching limits

### Leak Protection
- Automatic isolation of leaking tank
- Crew notification immediate
- Alternate tank sequence activated

### Redundancy
- Dual tank control channels
- Independent CG calculation
- Manual backup procedures

---

**Document Status:** ✅ Active  
**Last Updated:** 2025-11-04
