# ICD-02-00-24-002: Load Management Interface
**Version:** 1.0.0 | **Status:** Active

## Interface Description
Electrical load management system coordinating power distribution based on flight phase and priorities.

## Load Prioritization
1. **Critical**: Flight controls, avionics, fuel pumps
2. **Essential**: Navigation, communications, lighting
3. **Non-Essential**: Passenger services, galley, IFE

## Load Shedding
Automatic load shedding if power generation capacity reduced:
- Non-essential loads shed first
- Essential loads maintained
- Critical loads never shed

**RQ-ICD-02-24-010:** Load shed response <1 second  
**RQ-ICD-02-24-011:** Critical loads 100% protected  
**RQ-ICD-02-24-012:** Crew notification of load shed status

---
**Document Status:** ✅ Active | **Last Updated:** 2025-11-04
