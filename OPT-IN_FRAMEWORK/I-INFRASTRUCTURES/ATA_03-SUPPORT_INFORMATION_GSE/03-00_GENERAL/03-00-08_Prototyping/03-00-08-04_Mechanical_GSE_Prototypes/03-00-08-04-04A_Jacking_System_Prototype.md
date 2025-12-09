# 03-00-08-04-04A - Jacking System Prototype

## 1. Purpose
This document defines the prototype development for Aircraft Jacking System equipment designed to safely lift and support the AMPEL360 BWB aircraft for maintenance operations, accommodating the unique weight distribution, jacking points, and structural characteristics of the blended wing body design.

## 2. Scope
This prototype covers jacking system design including hydraulic jacks, support stands, control systems, safety interlocks, load monitoring, stability systems, and specialized adaptations for BWB aircraft jacking points and load distribution requirements.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE ARP1796 (GSE Design Requirements)
- SAE ARP1870 (Aircraft Jacking Equipment)
- ISO 3691 (Industrial Trucks - Safety Requirements)
- OSHA 1910.184 (Slings and Rigging)
- [Reference to 03-00-02_Safety]
- [Reference to Aircraft Maintenance Manual - Jacking Procedures]

## 4. Prototype Description

### 4.1 Overview
The Jacking System Prototype provides safe aircraft elevation for landing gear maintenance, weighing operations, and structural inspections. It must accommodate the BWB's unique center of gravity, multiple jacking points, and distributed load requirements while ensuring aircraft stability throughout the jacking process.

### 4.2 Design Specifications

| Parameter | Specification | Target |
|-----------|---------------|--------|
| Jacking Capacity | Maximum aircraft weight | 200,000 kg (440,000 lbs) MTOW |
| Jack Capacity | Individual jack rating | 40,000-60,000 kg per jack |
| Number of Jacks | Primary jacking points | 4-6 jacks minimum |
| Lift Height | Maximum elevation | 2.0-3.0m |
| Lift Speed | Elevation rate | 5-10 mm/minute (synchronized) |
| Position Accuracy | Jack synchronization | ±5mm between jacks |
| Load Monitoring | Real-time load cells | ±1% accuracy |
| Control System | Jack coordination | Automatic synchronization |
| Safety Factor | Design safety margin | 2:1 minimum |
| Stability System | Automatic leveling | Tilt sensors, automatic stop |

### 4.3 Materials and Components

#### 4.3.1 Hydraulic Jacks
- **Jack Type**: Telescoping hydraulic cylinders
- **Capacity**: 40,000-60,000 kg each
- **Construction**: Forged steel with hard chrome plating
- **Seals**: High-pressure hydraulic seals
- **Safety Locks**: Mechanical drop-prevention locks
- **Load Cells**: Integrated load measurement
- **Position Sensors**: Hydraulic or electronic position feedback

#### 4.3.2 Jack Adapters
- **Adapter Plates**: Aircraft-specific jacking point interfaces
- **Material**: High-strength steel or aluminum
- **Protection**: Rubber or urethane aircraft contact pads
- **Adjustment**: Fine positioning capability ±50mm
- **Safety**: Positive locking to jack head

#### 4.3.3 Hydraulic Power Unit
- **Pump Type**: Variable displacement piston pump
- **Pressure**: 200-350 bar (3,000-5,000 psi)
- **Flow Rate**: Sufficient for synchronized operation
- **Reservoir**: Adequate capacity for full cycle
- **Filtration**: Maintain hydraulic cleanliness
- **Controls**: Proportional control for smooth operation

#### 4.3.4 Control System
- **Controller**: PLC-based jack synchronization
- **HMI**: Touchscreen operator interface
- **Load Monitoring**: Real-time display of all jack loads
- **Safety Interlocks**: Automatic stop on anomalies
- **Position Display**: Height indication for each jack
- **Communication**: Wireless remote control option

#### 4.3.5 Support Stands
- **Type**: Adjustable height jack stands
- **Capacity**: Match or exceed jack capacity
- **Adjustment**: Telescoping or pin-adjustable
- **Base**: Wide footprint for stability
- **Locking**: Positive locking mechanisms
- **Quantity**: One stand per jack minimum

## 5. Prototype Build Plan

| Phase | Activities | Duration | Deliverables |
|-------|------------|----------|--------------|
| Design | Load analysis, jacking point design, safety review | 3 months | Design specifications |
| Procurement | Jacks, hydraulics, control system | 2 months | Components inventory |
| Fabrication | Adapters, stands, hydraulic assembly | 2 months | Assembled jacking system |
| Integration | Control system, load monitoring | 1 month | Integrated system |
| Validation | Load testing, aircraft trials, certification | 2 months | Certification report |

## 6. Testing Requirements

### 6.1 Capacity and Safety Testing
- **Individual Jack Testing**: 150% of rated capacity (static load)
- **System Testing**: Full aircraft weight simulation
- **Overload Protection**: Automatic stop at 110% capacity
- **Safety Lock Testing**: Drop prevention verification
- **Pressure Relief**: Hydraulic safety valve operation
- **Emergency Lowering**: Manual emergency descent

### 6.2 Synchronization Testing
- **Position Accuracy**: Verify ±5mm synchronization
- **Load Distribution**: Balanced loading across jacks
- **Control Response**: System response time
- **Communication**: Verify all jack communication
- **Failure Mode**: Single jack failure handling
- **Manual Override**: Individual jack control capability

### 6.3 Aircraft Interface Testing
- **Jacking Point Compatibility**: Adapter fit and alignment
- **Load Transfer**: Stress analysis at jacking points
- **Aircraft Stability**: CG tracking during lift
- **Clearance**: Ensure no interference with aircraft structure
- **Surface Protection**: No damage to aircraft surfaces
- **Access**: Maintainer access while jacked

### 6.4 Hydraulic System Testing
- **Pressure Testing**: System pressure at 150% operating pressure
- **Leak Testing**: All connections and seals
- **Flow Testing**: Adequate flow for synchronization
- **Temperature**: Hydraulic oil temperature under load
- **Filtration**: Contamination control verification
- **Accumulator**: Pressure accumulator function (if equipped)

### 6.5 Control System Testing
- **HMI Functionality**: All screens and controls operational
- **Safety Interlocks**: Verify all interlock functions
- **Load Monitoring**: Calibration of all load cells
- **Position Sensors**: Accuracy and repeatability
- **Alarms**: Proper alarm conditions and responses
- **Remote Control**: Wireless operation (if equipped)

### 6.6 Stability Testing
- **Level Surface**: Baseline stability measurement
- **Sloped Surface**: Operation on 2° slope
- **Uneven Support**: Simulated uneven foundation
- **Wind Loading**: Stability in wind conditions
- **Seismic**: Earthquake resistance (if applicable)
- **Long-term Hold**: Aircraft supported for extended period

### 6.7 Environmental Testing
- **Temperature Range**: -20°C to +50°C operation
- **Humidity**: Hydraulic and electrical system reliability
- **Vibration**: Hangar floor vibrations
- **Corrosion**: Protection of all metal surfaces
- **Contamination**: Dust and debris resistance

### 6.8 Operational Testing
- **Setup Time**: Jack positioning and preparation
- **Jacking Procedure**: Complete lift operation timing
- **Stand Placement**: Support stand installation
- **Lowering Procedure**: Controlled descent
- **Operator Training**: Training effectiveness assessment
- **Maintenance**: System serviceability and maintenance access

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 03-00-02 (Safety)
  - ATA 03-00-07 (V&V)
  - ATA 07 (Lifting and Shoring)
  - ATA 32 (Landing Gear)
- Parent Document: 03-00-08_Prototyping
- Related Maintenance Platform: 03-00-08-04-03A_Maintenance_Platform_Prototype
- Related Aircraft Maintenance Manual: Jacking and Shoring Procedures
- Related Testing: 03-00-08-06_GSE_Prototype_Testing

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |
