# RQ-MAINTENANCE - Maintenance Requirements

**Category:** RQ-MAINTENANCE  
**ID Range:** RQ-52-20-01-150 to RQ-52-20-01-164  
**Total Requirements:** 15  
**Priority:** Medium

## Overview

This category contains all maintenance requirements for the Door L3 Aft Emergency Exit, including inspection intervals, test procedures, and troubleshooting guidelines.

## Maintenance Design Philosophy

Maintenance must be:
- Scheduled based on reliability analysis
- Efficient with minimal aircraft downtime
- Accomplishable with standard tools
- Supported by clear documentation
- Integrated with CAOS predictive maintenance

## Key Requirements Summary

### Inspection Requirements (RQ-150 to RQ-153)
- **RQ-52-20-01-150**: Pre-flight visual inspection requirements
- **RQ-52-20-01-151**: A-check inspection (flight hours based)
- **RQ-52-20-01-152**: C-check detailed inspection
- **RQ-52-20-01-153**: Heavy maintenance inspection requirements

### Test Procedures (RQ-154 to RQ-157)
- **RQ-52-20-01-154**: Functional test procedures
- **RQ-52-20-01-155**: Pressure seal leak test
- **RQ-52-20-01-156**: Latch engagement verification
- **RQ-52-20-01-157**: Slide pack pressure test

### Component Life Limits (RQ-158 to RQ-161)
- **RQ-52-20-01-158**: Door structure life limit (cycles/years)
- **RQ-52-20-01-159**: Slide pack service life and certification
- **RQ-52-20-01-160**: Seal replacement interval
- **RQ-52-20-01-161**: Mechanism overhaul interval

### Troubleshooting (RQ-162 to RQ-164)
- **RQ-52-20-01-162**: Fault isolation procedures
- **RQ-52-20-01-163**: Built-in test (BIT) interpretation
- **RQ-52-20-01-164**: Common discrepancy resolution

## Maintenance Program Structure

### Scheduled Maintenance

**Pre-Flight Inspection (Daily)**
- Duration: 5 minutes
- Personnel: Flight crew or ground crew
- Tasks:
  - Visual inspection of door exterior
  - Seal condition check
  - Armed/disarmed indicator operation
  - Slide pack pressure gauge reading
  - Emergency lighting test

**A-Check (500-750 flight hours)**
- Duration: 2 hours
- Personnel: Certified A&P mechanic
- Tasks:
  - Detailed visual inspection
  - Functional test (open/close)
  - Latch adjustment if needed
  - Lubrication of hinges and mechanisms
  - Seal inspection and minor repair
  - Slide pack pressure verification

**C-Check (3000-4500 flight hours)**
- Duration: 8 hours
- Personnel: 2 certified A&P mechanics
- Tasks:
  - Complete disassembly inspection
  - Non-destructive testing (NDT) of structure
  - Mechanism overhaul
  - Seal replacement
  - Electrical system test
  - Functional test with slide deployment
  - Rigging and adjustment

**D-Check/Heavy Maintenance (6-10 years)**
- Duration: 24 hours
- Personnel: Specialized team
- Tasks:
  - Complete door removal
  - Full structural inspection
  - Corrosion treatment
  - Complete mechanism replacement
  - New slide pack installation
  - Full system re-certification test

### Unscheduled Maintenance

**Condition-Based**
- Triggered by CAOS alerts
- Predictive maintenance indicators
- Crew-reported discrepancies
- Inspection findings

## Inspection Procedures

### Visual Inspection Criteria

**Acceptable Findings:**
- Minor surface scratches
- Light discoloration of paint
- Normal wear patterns on seals
- Small dents (<5mm) outside critical areas

**Unacceptable Findings:**
- Cracks in any structural component
- Corrosion (any amount)
- Deep scratches or gouges (>1mm)
- Seal cuts, tears, or permanent deformation
- Loose fasteners
- Visible damage to mechanisms

### NDT Requirements

**Methods Used:**
- **Eddy Current**: Crack detection in aluminum
- **Ultrasonic**: Thickness measurement, delamination
- **Penetrant**: Surface crack detection
- **Radiography**: Internal structure examination (if suspect)

**Critical Areas:**
- Hinge attachment points
- Latch striker plates
- Frame corners (stress concentrations)
- Slide pack mounting brackets

## Functional Testing

### Door Operation Test
1. Verify door in disarmed mode
2. Open door using normal procedure
3. Measure opening time (should be <15 seconds)
4. Check for smooth motion (no binding)
5. Verify all latches engage on closing
6. Check seal compression
7. Test emergency lighting activation

### Pressure Seal Test
1. Close and latch door
2. Pressurize cabin to 2 psi
3. Apply soap solution to seal perimeter
4. Inspect for bubbles indicating leaks
5. Acceptable leak rate: <0.05 lb/min
6. Document any leaks and repair

### Latch Engagement Test
1. Close door slowly
2. Verify each latch engages sequentially
3. Check latch position indicators
4. Measure latch engagement force
5. Verify latches cannot back out
6. Test emergency override function

### Slide Pack Test
1. Check pressure gauge reading (3.0 psi ±0.3)
2. Verify pack installation security
3. Check girt bar attachment
4. Test manual release handle
5. Verify pressure bottle dates not expired
6. Document pressure reading and condition

## Component Replacement

### Slide Pack Replacement
**Frequency:** Every 12 years or per TSO-C69c certification
**Procedure:**
1. Disarm door and secure
2. Disconnect girt bar from floor
3. Remove slide pack mounting bolts
4. Lower pack using hoist (35 kg)
5. Install new pack in reverse order
6. Connect girt bar and secure
7. Perform functional test
8. Update aircraft records

**Cost:** $25,000-35,000 per pack
**Time:** 2 hours with 2 technicians

### Seal Replacement
**Frequency:** Every C-check or as needed
**Procedure:**
1. Remove old seal from groove
2. Clean groove thoroughly
3. Apply adhesive to new seal
4. Install seal in groove
5. Allow adhesive to cure (24 hours)
6. Perform pressure leak test

**Cost:** $2,000-3,000 for complete seal set
**Time:** 4 hours

### Mechanism Overhaul
**Frequency:** Every 10,000 cycles or 10 years
**Procedure:**
1. Remove door from aircraft
2. Disassemble all mechanisms
3. Clean all components
4. Replace worn parts (bearings, bushings)
5. Reassemble with new lubricant
6. Perform functional tests
7. Reinstall door and rig

**Cost:** $15,000-20,000
**Time:** 24 hours

## Troubleshooting Guide

### Common Discrepancies

| Symptom | Probable Cause | Corrective Action |
|---------|----------------|-------------------|
| Door hard to open | Latch misalignment | Adjust latch strikers |
| Pressure leak | Seal damage | Replace seal, pressure test |
| Armed light stays on | Sensor malfunction | Test sensor, replace if needed |
| Slide won't deploy | Low pressure | Check gauge, replace bottle |
| Emergency light dim | Battery weak | Replace battery |
| Door binding | Hinge wear | Lubricate or replace hinges |

### Fault Isolation

**Step 1: Verify the Symptom**
- Reproduce the discrepancy
- Note exact conditions
- Check for related symptoms

**Step 2: Check Built-In Test**
- Run BIT diagnostics
- Note fault codes
- Refer to fault code manual

**Step 3: Isolate to System**
- Electrical, mechanical, or pneumatic?
- Narrow down to specific subsystem
- Use process of elimination

**Step 4: Isolate to Component**
- Test individual components
- Replace suspected component
- Retest to confirm fix

**Step 5: Verify Repair**
- Perform functional test
- Document repair in log
- Clear fault codes
- Return to service

## Special Tools and Equipment

### Required Tools
- Door rigging fixture
- Pressure leak test kit
- Slide pack hoist
- Latch adjustment tools
- Seal installation kit
- Torque wrenches (calibrated)
- Multimeter and circuit tester

### Ground Support Equipment
- Work stands (door height access)
- Lighting (for inspection)
- Compressed air (for tests)
- Vacuum pump (seal installation)

## Technical Publications

### Maintenance Manuals
- Aircraft Maintenance Manual (AMM) ATA 52-20-01
- Structural Repair Manual (SRM) Chapter 52
- Illustrated Parts Catalog (IPC) Section 52-20-01
- Wiring Diagram Manual (WDM) Chapter 52

### Service Bulletins
- Mandatory Service Bulletins (MSB)
- Service Letters (SL)
- All Operators Messages (AOM)

## Maintenance Training

### Initial Qualification
- **Duration**: 40 hours (5 days)
- **Content**:
  - Door system overview
  - Inspection procedures
  - Functional testing
  - Component replacement
  - Troubleshooting
  - Safety considerations
- **Certification**: Written exam + practical test

### Specialized Training
- Slide pack replacement: 8 hours
- NDT procedures: 16 hours (per method)
- Mechanism overhaul: 16 hours
- CAOS system: 8 hours

## CAOS Integration

### Predictive Maintenance
- Wear trend analysis
- Anomaly detection
- Component life prediction
- Optimized scheduling

### Real-Time Monitoring
- Door operation count tracking
- Opening/closing time trends
- Pressure differential history
- Latch cycle counting
- Seal degradation tracking

### Maintenance Optimization
- Condition-based maintenance triggers
- Parts ordering automation
- Reduced unscheduled maintenance
- Fleet-wide learning

## Maintenance Metrics

| Metric | Target | Current Fleet |
|--------|--------|---------------|
| MTBF | 50,000 hr | 55,000 hr |
| Unscheduled removals/1000 cycles | <0.5 | 0.3 |
| Scheduled maintenance time | 2 hr (A-check) | 1.8 hr |
| On-wing time | 15 years | 16 years |
| MEL dispatch rate | <1% | 0.5% |

## Spares Provisioning

### Recommended Spares (per 10 aircraft)
- Complete slide pack: 2
- Seal set: 5
- Latch mechanism assembly: 2
- Position sensor: 6
- Pressure gauge: 3
- Emergency light battery: 10
- Girt bar fitting: 4

## Related Documents

- **AMM 52-20-01**: Maintenance procedures
- **IPC 52-20-01**: Parts catalog
- **SRM Chapter 52**: Structural repairs
- **11_OPERATIONS_AND_MAINTENANCE**: Maintenance planning

---

**Document Control**  
**Version:** 1.0  
**Date:** 2025-11-04  
**Status:** Released  
**Approved by:** Chief Maintenance Engineer
