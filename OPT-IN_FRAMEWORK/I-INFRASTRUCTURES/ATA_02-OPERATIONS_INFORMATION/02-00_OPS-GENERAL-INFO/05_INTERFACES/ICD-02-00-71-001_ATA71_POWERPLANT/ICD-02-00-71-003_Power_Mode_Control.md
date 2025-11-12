# ICD-02-00-71-003: Power Mode Control
**Version:** 1.0.0 | **Status:** Active

## Interface Description
Fuel cell power mode selection and control based on flight phase and operational requirements.

## Power Modes

### Takeoff Mode
- All 4 stacks at maximum power
- 10 MW available
- Maximum 5-minute duration

### Climb Mode
- 3-4 stacks at 80-90% power
- 7-9 MW typical
- Efficiency optimized

### Cruise Mode
- 2-3 stacks at 60-70% power
- 4-5 MW typical
- Maximum efficiency (58-60%)

### Descent Mode
- 1-2 stacks at 30-50% power
- 1-2 MW typical
- Idle power mode

### Emergency Mode
- Minimum stacks for essential power
- Battery backup available
- Reduced performance accepted

**RQ-ICD-02-71-020:** Mode transitions automatic  
**RQ-ICD-02-71-021:** Power available within 3 seconds  
**RQ-ICD-02-71-022:** Efficiency optimization enabled

---
**Document Status:** ✅ Active | **Last Updated:** 2025-11-04
