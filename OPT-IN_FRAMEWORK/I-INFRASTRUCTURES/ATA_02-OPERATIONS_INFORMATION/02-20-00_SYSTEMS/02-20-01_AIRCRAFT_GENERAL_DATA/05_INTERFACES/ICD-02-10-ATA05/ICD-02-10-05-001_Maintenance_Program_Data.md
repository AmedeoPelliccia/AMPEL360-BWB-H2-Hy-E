# ICD-02-10-05-001: Maintenance Program Data Interface

**From:** ATA 02-10 Aircraft General Data  
**To:** ATA 05 Time Limits & Maintenance Checks

**ICD ID:** ICD-02-10-05-001  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## Purpose

This Interface Control Document defines the data exchange between Aircraft General Data (ATA 02-10) and the Maintenance Program (ATA 05) to ensure maintenance planning is based on accurate aircraft specifications and limitations.

## Data Exchange

### Aircraft Limitations Data

**Provided by ATA 02-10:**
- Maximum flight hours between major inspections
- Calendar time limits
- Cycle-based inspection intervals
- Component life limits
- Airworthiness limitations

**Data Format:** Structured maintenance requirements table  
**Update Frequency:** Static (updated with design changes)  
**Criticality:** Medium

### H₂ System Maintenance Requirements

**Specific to AMPEL360:**
- Cryogenic tank inspection intervals: 2,000 flight hours or 5 years
- Fuel cell stack replacement: 10,000 hours
- H₂ pressure sensor calibration: 500 flight hours
- Emergency valve testing: 1,000 cycles

## Interface Specifications

**Data Exchange Method:** Static documentation reference  
**Format:** ATA iSpec 2200 compliant tables  
**Validation:** Annual review by maintenance planning and engineering

## Dependencies

- Structural life calculations (ATA 20)
- H₂ system component specifications (ATA 28)
- Fuel cell maintenance requirements (ATA 71)

## Responsibilities

**ATA 02-10 (Provider):**
- Maintain accurate aircraft limitations
- Update maintenance intervals based on service experience
- Coordinate with engineering for limit changes

**ATA 05 (Consumer):**
- Incorporate limitations into maintenance program
- Track compliance with intervals
- Report anomalies for limit review

## Change Control

Changes to maintenance limitations require:
1. Engineering analysis and justification
2. Safety assessment
3. Regulatory authority approval
4. Update to Aircraft Maintenance Manual

## References

- EASA CS-25 Subpart D: Design and Construction
- FAA AC 120-16F: Air Carrier Maintenance Programs
- ATA iSpec 2200 Chapter 5

---

**Document Control:**
- Version: 1.0
- Status: Active
- Last Updated: 2025-11-05
- Review Cycle: Annual
