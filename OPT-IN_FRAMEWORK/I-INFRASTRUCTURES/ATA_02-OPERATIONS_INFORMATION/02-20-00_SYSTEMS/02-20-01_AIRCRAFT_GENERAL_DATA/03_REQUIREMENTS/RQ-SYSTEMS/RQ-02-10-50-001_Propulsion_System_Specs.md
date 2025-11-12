# RQ-02-10-50-001: Propulsion System Specs

**Requirement ID:** RQ-02-10-50-001  
**Category:** Systems  
**Priority:** Critical  
**Status:** Approved

## Requirement

The aircraft shall be powered by hydrogen fuel cell propulsion system providing sufficient thrust and power for all flight phases with appropriate redundancy and reliability.

**Propulsion System Configuration:**
- Primary Power: PEM Fuel Cell Stacks
- Total Power Output: 12 MW (16,100 HP)
- Propulsors: 4× Boundary Layer Ingestion (BLI) ducted fans
- Thrust per Propulsor: 45 kN (10,116 lbf) at takeoff

## System Architecture

**Fuel Cell Stacks:**
- Type: Proton Exchange Membrane (PEM)
- Number of Stacks: 8 (2 per propulsor)
- Power per Stack: 1.5 MW
- Operating Temperature: 60-80°C
- Efficiency: 50-60% (higher than combustion)

**Electric Propulsors:**
- Configuration: Aft-mounted, BLI ducted fans
- Motor Type: High-density permanent magnet
- Motor Power: 3 MW per propulsor
- Fan Diameter: 2.8 m
- Design Point RPM: 4,200

## Rationale

Fuel cell propulsion provides:
- Zero emissions (only water vapor byproduct)
- High efficiency (50-60% vs 25-35% turbofan)
- Reduced noise (65 dB vs 85 dB conventional)
- Lower operating costs
- BLI benefits from BWB configuration
- Scalable and modular design

## Performance Requirements

**Takeoff Power:**
- Total Thrust: 180 kN (40,464 lbf)
- Power Required: 12 MW
- Duration: 5 minutes at maximum power

**Cruise Power:**
- Total Thrust: 45 kN (10,116 lbf)
- Power Required: 3 MW (25% of maximum)
- Efficiency: 58% at cruise conditions

**Redundancy:**
- Single fuel cell failure: Continued safe flight
- Single propulsor failure: Continued safe flight and landing
- Dual failure: Safe landing capability

## Integration with BWB

**Boundary Layer Ingestion Benefits:**
- Propulsors ingest fuselage boundary layer
- Reduced overall drag by 8-12%
- Improved propulsive efficiency
- Integrated aerodynamic design

## Verification

- **Method:** Test and Analysis
- **Procedure:**
  - Fuel cell stack testing (ground rig)
  - Propulsor performance testing
  - Integrated system testing
  - Flight test validation
- **Acceptance Criteria:**
  - Thrust and power targets achieved
  - Reliability demonstrated (MTBF > 5,000 hours)
  - Efficiency within 5% of predictions
  - Emergency procedures validated

## Hydrogen Fuel Consumption

| Flight Phase | Power (MW) | Duration | H₂ Consumption (kg) |
|--------------|-----------|----------|---------------------|
| Taxi | 0.5 | 10 min | 50 |
| Takeoff | 12 | 5 min | 150 |
| Climb | 6 | 20 min | 500 |
| Cruise | 3 | 7 hours | 5,500 |
| Descent | 2 | 25 min | 200 |
| Landing | 4 | 5 min | 100 |

## Maintenance Requirements

**Scheduled Maintenance:**
- Fuel cell stack inspection: 2,000 flight hours
- Propulsor inspection: 1,000 flight hours
- Major overhaul: 10,000 flight hours

**CAOS Predictive Maintenance:**
- Real-time health monitoring
- Performance degradation prediction
- Automated maintenance scheduling
- Parts inventory optimization

## Compliance

- CS-25.901: Installation (powerplant)
- CS-25.903: Engines
- CS-25.1305: Powerplant instruments
- SAE ARP6518: Fuel Cell Power Systems for Aircraft
- DO-160: Environmental Conditions and Test Procedures

## Related Requirements

- RQ-02-10-30-003: H2 Fuel Capacity
- RQ-02-10-50-002: H2 System Specs
- RQ-02-10-40-001: Design Range
- RQ-02-10-40-002: Cruise Speed

---

**Document Control:**
- Version: 1.0
- Status: Approved
- Last Updated: 2025-11-05
- Approved By: Propulsion Systems Engineer
