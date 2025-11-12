# RQ-02-10-50-002: H₂ System Specs

**Requirement ID:** RQ-02-10-50-002  
**Category:** Systems  
**Priority:** Critical  
**Status:** Approved

## Requirement

The hydrogen fuel system shall safely store, manage, and deliver liquid hydrogen (LH₂) to the fuel cell stacks throughout all operational conditions while maintaining safety, reliability, and efficiency.

## System Overview

**Storage System:**
- 4× Cryogenic tanks (Type IV composite)
- Total Capacity: 8,500 kg LH₂
- Usable Fuel: 8,000 kg
- Storage Temperature: -253°C (20K)
- Operating Pressure: 5-8 bar

**Distribution System:**
- Cryogenic feed lines with vacuum insulation
- Redundant pump system (4 pumps, 1 per tank)
- Pressure regulation and control
- Vaporization and heating system
- Emergency shutoff valves

## Tank Specifications

**Tank Design:**
- Type: Type IV (carbon fiber overwrapped, aluminum liner)
- Insulation: Multi-layer insulation (MLI) + vacuum
- Boil-off Rate: < 0.5% per day
- Maximum Pressure: 12 bar (design safety factor: 2.5)
- Leak Rate: < 10⁻⁶ mbar·L/s
- Design Life: 20 years / 50,000 cycles

**Safety Features:**
- Pressure relief valves
- Burst disks
- Emergency venting system
- Fire detection and suppression
- Crash protection structure
- Lightning protection

## Fuel Management System

**Feed Sequence (CG Control):**
1. Center forward tank (Tank 2) - First
2. Center aft tank (Tank 3) - Second
3. Port and starboard tanks balanced (Tanks 1 & 4) - Third

**Capabilities:**
- Automatic tank sequencing
- CG optimization
- Cross-feed capability
- Fuel balancing
- Quantity indication (±2% accuracy)
- Temperature monitoring

## Fuel Conditioning

**Vaporization and Heating:**
- Heat exchangers utilize waste heat from fuel cells
- Gaseous H₂ delivered to fuel cells at 60°C
- Pressure regulation: 5 bar nominal
- Flow rate: 0-2.5 kg/s per stack

**Quality Control:**
- Purity monitoring (>99.97% H₂)
- Moisture detection
- Contaminant filtering

## Rationale

H₂ system specifications ensure:
- Safe storage and handling of cryogenic fuel
- Reliable fuel delivery in all flight phases
- CG management through fuel sequencing
- System redundancy and fault tolerance
- Compliance with emerging H₂ safety standards
- Integration with fuel cell propulsion

## Safety Systems

**Detection Systems:**
- H₂ leak detectors (multiple zones)
- Temperature sensors (tank and line monitoring)
- Pressure monitoring (continuous)
- Fire detection in compartments

**Protection Systems:**
- Automatic shutoff valves (crash-activated)
- Emergency venting (overboard)
- Fire suppression (Halon alternative)
- Thermal insulation and barriers
- Ventilation system (purge capability)

**Emergency Procedures:**
- Fuel system shutdown sequence
- Emergency fuel dump (if required)
- Fire fighting procedures
- Leak response procedures

## Verification

- **Method:** Test, Analysis, and Inspection
- **Procedure:**
  - Tank pressure testing and certification
  - Thermal performance testing (boil-off rate)
  - Leak testing (helium mass spectrometry)
  - Flow testing and calibration
  - Safety system validation
  - Emergency procedure testing
- **Acceptance Criteria:**
  - Tanks certified to design pressure
  - Boil-off rate < 0.5% per day
  - Leak rate within specification
  - Safety systems respond per requirements
  - Fuel delivery rate adequate for all conditions

## Maintenance Requirements

**Scheduled Inspections:**
- Visual inspection: Pre-flight
- Leak checks: 500 flight hours
- Tank internal inspection: 5,000 flight hours
- Pressure test: 10,000 flight hours

**CAOS Integration:**
- Real-time system health monitoring
- Predictive maintenance alerts
- Fuel quantity and quality tracking
- Performance trending
- Automated fault detection

## Ground Operations

**Refueling:**
- Connection: Quick-disconnect couplings
- Fill Rate: 1,000 kg/hour per connection
- Fill Time: ~4 hours for full tanks
- Safety Zone: 30m radius during refueling
- Ground crew training: H₂ safety certified

**Defueling:**
- Emergency defueling capability
- Rate: 500 kg/hour
- Vapor recovery system

## Compliance

- CS-25.954: Fuel system lightning protection
- CS-25.963: Fuel tanks: general
- CS-25.967: Fuel tank installation
- CS-25.975: Fuel tank vents and carburetor vapor vents
- CS-25.981: Fuel tank ignition prevention
- ISO 19881: Gaseous hydrogen land vehicle fuel containers
- SAE AIR7165: Hydrogen fuel system safety
- SAE ARP6418: Aerospace hydrogen safety

## Related Requirements

- RQ-02-10-30-003: H2 Fuel Capacity
- RQ-02-10-50-001: Propulsion System Specs
- RQ-02-10-20-005: CG Envelope BWB
- RQ-02-10-50-003: CAOS Integration

---

**Document Control:**
- Version: 1.0
- Status: Approved
- Last Updated: 2025-11-05
- Approved By: H₂ Systems Chief Engineer
