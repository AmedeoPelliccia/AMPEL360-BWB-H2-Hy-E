# CG Control Design

## Executive Summary

The AMPEL360 BWB requires active CG control due to its wide CG envelope (27% MAC usable range). This document defines the design of the integrated CG control system combining H2 fuel management, load planning, and CAOS monitoring.

## CG Control Architecture

### Three-Layer Control System

**Layer 1: Design Phase (Passive)**
- Optimal OEW CG at 27% MAC (mid-envelope)
- Distributed structural masses
- Fixed equipment strategic placement
- Emergency equipment balanced distribution

**Layer 2: Ground Operations (Active)**
- Passenger seat assignment optimization
- Cargo loading sequence planning
- H2 fuel loading distribution
- Load sheet generation and verification

**Layer 3: Flight Operations (Dynamic)**
- Real-time CG monitoring
- Automated H2 transfer between tanks
- Crew decision support
- Performance optimization

## Design Phase Controls

### Structural Mass Distribution

**Forward Masses (15-22% MAC)**
- Flight deck equipment: 2,800 kg
- Forward avionics bay: 1,500 kg
- Nose landing gear: 3,200 kg
- Forward H2 tanks (empty): 600 kg
- **Subtotal:** 8,100 kg

**Center Masses (22-32% MAC)**
- Center body structure: 28,500 kg
- Main landing gear: 8,400 kg
- Center H2 tanks (empty): 1,200 kg
- Fuel cells (2×): 4,200 kg
- Main systems: 6,500 kg
- **Subtotal:** 48,800 kg

**Aft Masses (32-40% MAC)**
- Aft cabin equipment: 1,800 kg
- Aft avionics bay: 900 kg
- Aft H2 tanks (empty): 400 kg
- Empennage: 3,200 kg
- APU: 1,500 kg
- **Subtotal:** 7,800 kg

**OEW CG Result: 27.2% MAC** ✓

## Ground Operations Controls

### Load Planning Software

**Inputs:**
- Passenger count and demographics
- Cargo weight and distribution
- H2 fuel required
- Flight performance requirements
- Weather conditions

**Optimization Algorithm:**
```
1. Calculate baseline CG with empty aircraft
2. Add passenger loads per zone assignment
3. Add cargo per compartment assignment
4. Add H2 fuel per tank loading sequence
5. Verify CG within limits (19-35% MAC)
6. If out of limits:
   - Adjust passenger seating zones
   - Redistribute cargo compartments
   - Modify H2 tank loading priority
7. Generate load sheet
8. Validate against aircraft limits
```

**Output:**
- Seat assignment map
- Cargo loading sequence
- H2 tank filling order
- Final CG position
- Takeoff performance data

### Loading Sequence

**Step 1: Cargo Loading**
- Forward cargo: 15 minutes
- Aft cargo: 15 minutes
- Verify individual compartment weights

**Step 2: H2 Refueling**
- Primary tanks (center): 25 minutes
- Trim tanks (wing): 15 minutes
- Pressure stabilization: 10 minutes

**Step 3: Passenger Boarding**
- Zone B center: 5 minutes
- Zones A & C simultaneously: 10 minutes
- Zone B outer: 5 minutes
- Final count verification: 2 minutes

**Total Ground Time:** 90 minutes (typical)

### Final Verification

- Weight and balance computer validation
- CG position: 25-29% MAC (target range)
- Takeoff performance check
- Crew review and acceptance

## Flight Operations Controls

### Real-Time CG Monitoring (CAOS)

**Sensor Inputs:**
- H2 tank quantity (8 sensors)
- H2 tank CG position calculation
- Flight control surface positions
- Airspeed and altitude
- Aircraft attitude

**CG Calculation:**
```
CG = (ΣMi × Xi) / ΣMi

Where:
Mi = Mass of component i
Xi = Longitudinal position of component i
Σ = Sum over all components
```

**Update Rate:** 1 Hz (every second)

### Automated H2 Transfer System

**Transfer Triggers:**
- CG deviation > 3% from optimal (26% MAC)
- Crew-commanded trim requirement
- Performance optimization mode
- Emergency rebalancing

**Transfer Logic:**
```
If CG < 24% MAC (too forward):
  Transfer H2 from center tanks to aft wing tanks
  Rate: 50 kg/min
  Stop when CG ≥ 26% MAC

If CG > 30% MAC (too aft):
  Transfer H2 from wing tanks to center tanks
  Rate: 50 kg/min
  Stop when CG ≤ 28% MAC

Normal cruise target: 26-28% MAC (optimal L/D)
```

**Transfer Rate:** 50 kg/min (0.5% MAC shift per 10 minutes)

### Crew Interface

**Primary Flight Display (PFD) CG Indicator**
- Current CG: Digital readout (% MAC)
- CG limits: Green arc (19-35% MAC)
- Optimal range: Yellow arc (24-32% MAC)
- Transfer status: Blue arrow when active

**Multi-Function Display (MFD) Weight & Balance Page**
- Graphical CG envelope
- Current CG position (moving dot)
- Fuel distribution bar chart
- Transfer system status
- Limit alerting

**EICAS Messages**
- `CG APPROACHING LIMIT` at ±2% from limits
- `CG XFER IN PROGRESS` during automated transfer
- `CG XFER FAIL` if system fault

### Performance Optimization

**Cruise Climb CG Management**
- As fuel depletes, maintain CG 26-28% MAC
- Automated transfer minimizes trim drag
- Improved L/D = reduced fuel consumption
- CAOS learns optimal profiles over fleet

**Descent CG Strategy**
- Transfer fuel to center tanks (stable for landing)
- Target landing CG: 27% MAC ± 2%
- Reduced elevator deflection requirement
- Improved go-around performance

## Emergency Procedures

### Fuel Transfer System Failure
- Manual transfer available via overhead panel
- Crew calculates required transfer amount
- CAOS provides guidance
- Flight within normal CG limits still possible

### Extreme CG Situations
- If CG < 19% MAC: Dump aft fuel, request priority landing
- If CG > 35% MAC: Dump forward fuel, increase speed for control
- CAOS provides recommended airspeeds and configuration

### Passenger Movement (Turbulence)
- Expected CG shift: ±0.5% MAC
- Automated H2 transfer compensates
- Crew awareness of large movements

## Design Margins

### Regulatory Compliance
- **CS-25.27:** CG limits definition
- **Forward Limit:** 15% MAC (structural)
- **Aft Limit:** 42% MAC (control authority)
- **Operational Envelope:** 19-35% MAC (16% range)
- **Usable Envelope:** 27% MAC (vs 20% conventional)

### Safety Margins
- **Structural limits:** ±4% beyond operational
- **Control authority:** ±7% beyond operational
- **Warning margins:** ±2% before operational limit

## Validation and Testing

### Ground Testing
- Static load tests with various configurations
- CG calculation system validation
- Load planning software verification
- Transfer system functional testing

### Flight Testing
- CG envelope verification
- Transfer system performance
- Extreme loading scenarios
- System failure modes

### Certification Compliance
- CS-25.27 compliance demonstration
- FCOM procedures validation
- Training program development
- Simulator validation

---

**References:**
- Weight & Balance Manual: WBM-001
- Flight Crew Operating Manual: FCOM Section 02.10
- CAOS System Description: ATA 45-00-00
- H2 Fuel Management: ATA 28-00-00
- Certification Basis: CB-WB-2025-001
