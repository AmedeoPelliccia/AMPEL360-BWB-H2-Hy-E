# ICD-02-00-24-003: Emergency Power Modes
**Version:** 1.0.0 | **Status:** Active

## Interface Description
Emergency electrical power modes for degraded or emergency operations.

## Power Modes
### Normal Mode
- All 4 fuel cell stacks operating
- Full 10 MW power available
- All systems powered

### Degraded Mode
- 1 fuel cell stack failed
- 7.5 MW available (3 stacks)
- Non-essential loads limited

### Emergency Mode
- 2+ fuel cell stacks failed
- Battery backup activated
- Critical systems only
- 30-minute battery endurance

**RQ-ICD-02-24-020:** Emergency mode activation automatic  
**RQ-ICD-02-24-021:** Battery backup 30 min minimum  
**RQ-ICD-02-24-022:** Mode transitions seamless (<100 ms)

---
**Document Status:** ✅ Active | **Last Updated:** 2025-11-04
