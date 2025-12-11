# 10-INT-GSE-002 - Jacking Points Interface

## 1. Interface Identification

| Parameter | Value |
|-----------|-------|
| Interface Number | 10-INT-GSE-002 |
| Interface Type | Mechanical, Structural |
| System A | Aircraft Structure (BWB) |
| System B | Aircraft Jacks |
| ATA Chapter A | ATA-10 |
| ATA Chapter B | ATA-03 (GSE) |
| H2 Related | No |
| Cryo Related | No |
| BWB Specific | Yes |
| Safety Classification | Safety-Critical |
| Status | Baselined |

## 2. Interface Description

Defines jacking point locations and specifications for lifting the AMPEL360-BWB-H2-Hy-E aircraft during maintenance operations. The BWB configuration requires 6 jacking points (3 forward, 3 aft) to safely support the aircraft weight and maintain structural integrity.

### Purpose
- Enable wheel/brake maintenance and tire changes
- Provide access to landing gear systems
- Support structural inspections and repairs
- Ensure safe lifting operations

## 3. Interface Parameters

| Parameter | Value | Unit | Tolerance |
|-----------|-------|------|-----------|
| Number of Jacking Points | 6 | - | - |
| Jack Capacity (each) | 120,000 | kg | - |
| Jack Pad Size | 150 × 150 | mm | - |
| Maximum Jacking Height | 800 | mm | Above ground |
| Jack Positioning Tolerance | ±25 | mm | Horizontal |
| Leveling Tolerance | ±0.5 | degrees | - |

### Forward Jacking Points (3)
- Location: Station 60, BL 0 and ±180
- Integrated into front spar bulkhead structure
- Titanium reinforcement plates

### Aft Jacking Points (3)
- Location: Station 380, BL 0 and ±200
- Integrated into rear spar bulkhead structure
- Titanium reinforcement plates

## 4. Physical Interface

### 4.1 Jack Pad Interface
- Hardened steel pad surface, 150 × 150 mm
- Anti-slip serrated surface pattern
- Recessed 10 mm below OML with protective cover
- High-visibility markings and placards

### 4.2 Load Requirements
- Ultimate load per jack point: 180,000 kg (1.5 × limit)
- Combined capacity exceeds MTOW by 100%
- Load distribution: Forward jacks 45%, Aft jacks 55%

## 5. H2/Cryo Considerations

| Parameter | Value |
|-----------|-------|
| H2 Related | No |
| Cryo Related | No |
| Special Requirements | All fuel (H2) must be removed before jacking |

## 6. BWB Considerations

- 6-point jacking system optimized for BWB load distribution
- Wide stance provides excellent stability when jacked
- Lower ground clearance than conventional aircraft
- Jacking procedure accounts for BWB CG range

**Jacking Sequence:**
1. Position jacks at all 6 points
2. Raise all jacks to contact (no load)
3. Raise forward jacks simultaneously to design height
4. Raise aft jacks simultaneously to design height
5. Verify level within tolerance

## 7. Constraints

### Operational
- Aircraft must be on level surface (±1%)
- Maximum wind speed during jacking: 20 knots
- All jacks must be hydraulically synchronized
- Minimum 3 personnel required for jacking operations

### Safety
- No personnel under aircraft during jacking
- Safety stands deployed immediately after jacking
- Daily stability check when aircraft remains jacked
- Maximum jacked duration: 7 days

## 8. Verification

| Verification Method | Criteria | Status | Reference |
|---------------------|----------|--------|-----------|
| Load Test | 1.5 × limit load per point | Completed | TEST-10-GSE-002 |
| Structural Analysis | Stress analysis verification | Completed | ANA-10-GSE-001 |
| Jacking Demonstration | Full jacking procedure | Completed | DEMO-10-GSE-002 |

## 9. Related Documentation

- ICD Reference: [10-ICD-003 - BWB Ground Handling ICD](../interface-control-documents/10-ICD-003_BWB_Ground_Handling_ICD.md)
- Related Standards: [SAE AS1893](https://www.sae.org/standards/content/as1893/): Aircraft Jacks
- Cross-ATA: [10-INT-AC-005 - BWB Structural Interface](../aircraft-interfaces/10-INT-AC-005_BWB_Structural_Interface.md)

## 10. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-09 | AMPEL360 Engineering | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **BASELINED** – Approved for production use
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-09

---
