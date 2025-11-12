# ICD-02-00-28-003: Quantity Indication Interface

**Version:** 1.0.0  
**Status:** Active

## Interface Description

Real-time fuel quantity indication interface providing accurate H2 fuel mass data to operations and flight crew.

## Technical Challenges

### Cryogenic Fuel Measurement
Unlike conventional jet fuel, liquid hydrogen presents unique challenges:
- **Density Variation**: LH2 density varies significantly with temperature (-253°C nominal)
- **Boil-Off**: Continuous evaporation requires compensation
- **Sloshing**: Low density amplifies tank dynamics
- **Measurement**: Capacitance probes require temperature compensation

## Measurement System

### Primary Quantity System
- **Method**: Capacitance probes with temperature compensation
- **Probes per Tank**: 6-8 redundant probes
- **Update Rate**: 1 Hz (averaged over 10 samples)
- **Accuracy**: ±50 kg or ±2%, whichever is greater

### Backup Quantity System
- **Method**: Flow integration from refuel point
- **Accuracy**: ±100 kg (degrades with time since refuel)
- **Reset**: At each refueling

### CAOS Predictive System
- **Method**: AI model using temperature, pressure, flow, flight phase
- **Accuracy**: ±75 kg
- **Availability**: Continuous (backup to backup)

## Data Flows

### Fuel System → Operations
```yaml
FUEL_QUANTITY:
  timestamp: ISO8601
  total_fuel_kg: 6543.2
  tanks:
    CTR-1:
      quantity_kg: 1843.5
      confidence: 98.2
      source: PRIMARY
    CTR-2:
      quantity_kg: 1702.8
      confidence: 98.5
      source: PRIMARY
    WING-L:
      quantity_kg: 1498.1
      confidence: 97.8
      source: PRIMARY
    WING-R:
      quantity_kg: 1498.8
      confidence: 98.1
      source: PRIMARY
  fuel_consumed_kg: 1456.8
  fuel_remaining_time_minutes: 187
  reserve_fuel_kg: 1200.0
  bingo_fuel_alert: false
```

## Display Requirements

### Primary Flight Display (PFD)
- **Total Fuel**: Large numerical display (kg)
- **Fuel Flow**: kg/hour current consumption
- **Endurance**: Time remaining at current flow

### Multi-Function Display (MFD)
- **Tank Distribution**: Graphical tank representation
- **Individual Tank Quantities**: Numerical per tank
- **CG Position**: Resulting from fuel distribution
- **Trend Arrow**: Fuel consumption trend

### EICAS Display
- **Alerts**: Low fuel, imbalance, sensor failures
- **Status Messages**: Quantity system status

## Interface Requirements

**RQ-ICD-02-28-020:** Total fuel quantity accuracy ±50 kg  
**RQ-ICD-02-28-021:** Update rate 1 Hz minimum  
**RQ-ICD-02-28-022:** Sensor failure detection within 5 seconds  
**RQ-ICD-02-28-023:** Automatic source switching on failure

## Fuel Planning Integration

### Pre-Flight
- Required fuel calculation (trip + reserve + alternate + contingency)
- Fuel order transmitted to refueling system
- Actual fuel uploaded verification

### In-Flight
- Continuous fuel remaining calculation
- Destination fuel prediction
- Alternate fuel check
- Bingo fuel monitoring

### CAOS Optimization
- Real-time fuel burn adjustment based on actual conditions
- Route optimization for fuel efficiency
- Altitude optimization
- Speed optimization

## Alert Thresholds

| Alert | Threshold | Action |
|-------|-----------|--------|
| Low Fuel | <1000 kg | Caution alert, verify fuel plan |
| Bingo Fuel | <500 kg | Warning alert, divert to nearest suitable |
| Critical Fuel | <300 kg | Emergency, immediate landing |
| Imbalance | >500 kg difference | Initiate fuel transfer |
| Sensor Fail | Loss of redundancy | Advisory, use backup system |

## Failure Modes

### Primary System Failure
- Automatic switch to backup flow integration
- Crew notification
- Increased monitoring required
- MEL Category B (3 days)

### Backup System Failure
- Use CAOS predictive model
- Manual fuel monitoring enhanced
- Land at earliest suitable airport
- MEL: No dispatch

### Both Systems Failed
- Aircraft grounded
- No dispatch allowed
- Repair required before next flight

## Calibration

### Ground Calibration
- Performed during refueling
- Known fuel quantity uploaded
- System correlation verified
- Discrepancies investigated

### In-Flight Calibration
- CAOS monitors fuel burn vs. prediction
- Adjusts models based on actual performance
- Identifies sensor drift
- Recommends calibration if needed

---

**Document Status:** ✅ Active  
**Last Updated:** 2025-11-04
