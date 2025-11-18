# 95-00-09-01-003: Change Control in Production

**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE  
**Document ID:** 95-00-09-01-003

## 1. Purpose
Defines the change control process for frozen models in production planning and deployment phases.

## 2. Change Control Board (CCB)
- **Chair**: Chief Engineer
- **Members**: Safety Engineer, V&V Lead, Quality Assurance, Model Owner
- **Meeting Frequency**: Weekly or as needed

## 3. Change Request Process
1. Submit Change Request Form with justification
2. Impact assessment (safety, performance, schedule, cost)
3. CCB review and decision
4. If approved: implement, test, new baseline
5. Update documentation and traceability

## 4. Change Categories
- **Emergency**: Safety-critical, immediate action, 24h CCB decision
- **Urgent**: High impact, 3-day CCB decision
- **Normal**: Standard process, next scheduled CCB
- **Deferred**: Low priority, batched changes

## 5. Version Impact
- Emergency/Critical: PATCH version increment
- Significant changes: MINOR version increment  
- Architecture changes: MAJOR version increment

## 6. Document Control
- **Owner**: Change Control Board
- **Review Cycle**: Annually
