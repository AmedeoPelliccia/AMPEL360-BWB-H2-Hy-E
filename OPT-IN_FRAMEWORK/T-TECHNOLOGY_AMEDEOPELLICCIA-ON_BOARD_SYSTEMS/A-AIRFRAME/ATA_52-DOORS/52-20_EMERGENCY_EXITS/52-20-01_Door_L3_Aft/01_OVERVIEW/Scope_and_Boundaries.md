# Scope and Boundaries - Door L3 Aft Emergency Exit

**Document ID:** AMPEL360-52-20-01-SCOPE  
**Version:** 0.1  
**Date:** 2025-11-04

## 1. IN SCOPE

### 1.1 Physical Components
✅ Door structure and mechanisms
✅ Slide system and pack
✅ Actuation systems (primary & backup)
✅ Local control electronics
✅ Sensors and monitoring
✅ Manual release mechanisms
✅ Arming/disarming system
✅ Visual indicators and placards
✅ Girt bar and floor attachments
✅ Emergency lighting integration

### 1.2 Functional Capabilities
✅ Normal and emergency operation
✅ Power assist opening
✅ Manual override operation
✅ Automatic slide deployment
✅ CAOS health monitoring
✅ Predictive maintenance
✅ Digital twin integration
✅ Fleet learning capability

### 1.3 Documentation Coverage
✅ All 14 SKELETON folders
✅ Design justification
✅ Safety analysis (FMEA, FHA)
✅ Certification compliance
✅ Test procedures
✅ Maintenance procedures
✅ Training materials
✅ Digital passport data

## 2. OUT OF SCOPE

### 2.1 Not Included
❌ Fuselage structure (covered in ATA 53)
❌ Cabin interior finish (ATA 25)
❌ Emergency lighting system details (ATA 33)
❌ Oxygen system integration (ATA 35)
❌ Passenger seating (ATA 25)
❌ Flight attendant seats (ATA 25)
❌ Galley/lavatory doors (ATA 25/38)

### 2.2 External Dependencies
- Frame reinforcement (ATA 53)
- Electrical power supply (ATA 24)
- Environmental control (ATA 21)
- IMA integration (ATA 42)
- Ground support equipment (ATA 03)

## 3. BOUNDARY DEFINITIONS

### 3.1 Physical Boundaries
```
Forward: Frame Station 42 (BWB coordinates)
Aft: Frame Station 44
Upper: Ceiling rail interface
Lower: Floor beam interface
Lateral: ±200mm from door centerline
```

### 3.2 System Boundaries

#### Mechanical
- **Starts:** Door frame interface
- **Ends:** Floor/ceiling attachments

#### Electrical
- **Starts:** Aircraft power bus connector
- **Ends:** DCU outputs

#### Data
- **Starts:** CAOS data concentrator
- **Ends:** Door sensors/actuators

#### Pneumatic
- **Starts:** Slide inflation bottle
- **Ends:** Slide chambers

## 4. INTERFACE RESPONSIBILITIES

### 4.1 Our Responsibility (52-20-01)
- Door structure integrity
- Opening/closing mechanisms
- Slide deployment system
- Local control logic
- Sensor integration
- Manual backup systems

### 4.2 Other Systems' Responsibility

#### ATA 53 (Fuselage)
- Cutout reinforcement
- Primary load path
- Pressure vessel integrity

#### ATA 24 (Electrical)
- Power generation
- Bus protection
- Emergency power transfer

#### ATA 42 (IMA)
- System-level logic
- Cockpit indications
- CAOS server processing

## 5. TECHNICAL BOUNDARIES

### 5.1 Performance Envelope
- **Altitude:** 0 to 45,000 ft
- **Temperature:** -55°C to +70°C
- **Pressure Differential:** 0 to 9.5 psi
- **Wind Load:** Up to 40 knots
- **Opening Time:** 3-8 seconds
- **Cycles:** 20,000 minimum

### 5.2 Certification Limits
- **Compliance:** EASA CS-25 Amendment 27
- **Special Conditions:** BWB configuration
- **Environmental:** DO-160G
- **Software:** DO-178C Level B
- **Hardware:** DO-254 Level C

## 6. PROJECT BOUNDARIES

### 6.1 Development Phases

#### Phase 1 (Current)
- Conceptual design
- AI-based analysis
- Documentation framework

#### Phase 2 (2026)
- Detailed design
- FEA validation
- Prototype planning

#### Phase 3 (2027)
- Manufacturing
- Testing
- Certification

#### Phase 4 (2028+)
- Production
- In-service support
- Continuous improvement

### 6.2 Organizational Boundaries

#### Internal Team
- Design engineering
- Safety analysis
- CAOS integration
- Documentation

#### External Support Needed
- FEA services
- Slide supplier
- Actuator supplier
- Test facilities
- Certification (DER)

## 7. ASSUMPTIONS

### 7.1 Technical Assumptions
- BWB frame design frozen
- 100 passenger configuration
- All-electric aircraft systems
- CAOS v2.0 available
- Composite manufacturing capability

### 7.2 Program Assumptions
- Funding available Q1 2026
- Test facilities accessible
- Certification path agreed
- Suppliers qualified
- Team scaled appropriately

## 8. CONSTRAINTS

### 8.1 Regulatory Constraints
- Must meet CS 25.807-813
- 90-second evacuation demo
- TSO authorization required
- ETSO-C69c for slides

### 8.2 Technical Constraints
- Maximum weight: 150 kg
- Door must fit in existing cutout
- Power limited to 400W
- Must work unpowered
- No hydraulics available

### 8.3 Program Constraints
- Budget: €500k development
- Timeline: 24 months to cert
- Team: Max 5 engineers
- Testing: Limited to available facilities

## 9. SUCCESS CRITERIA

### 9.1 Technical Success
- ✓ Opens in <8 seconds (all modes)
- ✓ Slide deploys in <10 seconds
- ✓ 20,000 cycle capability
- ✓ Weight <150 kg
- ✓ CAOS fully integrated

### 9.2 Program Success
- ✓ On schedule (2028 cert)
- ✓ Within budget (€500k)
- ✓ Zero safety incidents
- ✓ Certification achieved
- ✓ Production ready
