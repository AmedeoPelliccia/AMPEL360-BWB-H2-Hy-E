# 10-INT-GSE-001 - Towing Interface

## 1. Interface Identification

| Parameter | Value |
|-----------|-------|
| Interface Number | 10-INT-GSE-001 |
| Interface Type | Mechanical |
| System A | Aircraft Nose Structure |
| System B | Tow Tractor / Towbar |
| ATA Chapter A | ATA-10 |
| ATA Chapter B | ATA-03 (GSE) |
| H2 Related | No |
| Cryo Related | No |
| BWB Specific | Yes |
| Safety Classification | Safety-Critical |
| Status | Baselined |

## 2. Interface Description

Defines the towing interface for pushback and ground movement of the AMPEL360-BWB-H2-Hy-E aircraft. The BWB configuration requires special consideration due to its wide wingspan, high mass, and unique center of gravity characteristics.

### Purpose
- Enable safe pushback from parking stand
- Facilitate aircraft positioning and ground movements
- Provide positive attachment to tow vehicle
- Ensure load transfer without aircraft damage

## 3. Interface Parameters

| Parameter | Value | Unit | Tolerance |
|-----------|-------|------|-----------|
| Tow Fitting Location | Station 10, CL, WL 8 | - | - |
| Tow Fitting Type | NATO Standard Tow Fitting | - | MIL-DTL-24638 |
| Ultimate Tow Load | 300 | kN | - |
| Maximum Tow Speed | 8 | km/h | - |
| Maximum Turning Angle | ±60 | degrees | ±2° |
| Aircraft Mass (Maximum) | 365,000 | kg | Ramp weight |
| Towbar Length (Typical) | 6-8 | m | Variable |
| Ground Clearance | 300 | mm | Minimum |

## 4. Physical Interface

### 4.1 Mechanical

**Tow Fitting:**
- Forged steel NATO standard fitting per MIL-DTL-24638
- Location: Nose landing gear region, accessible from ground
- Shear pin capacity: 350 kN (safety feature)
- Attachment: 4× M24 bolts to primary structure
- Load path: Tow fitting → nose gear bulkhead → center keel

**Towbar Interface:**
- Standard NATO towbar head compatible
- Vertical travel: ±100 mm to accommodate aircraft pitch
- Lateral angular range: ±60° for maneuvering
- Quick-connect mechanism with safety lock

**BWB-Specific Considerations:**
- Wide turning radius due to 88m wingspan
- High mass requires heavy-duty tow vehicle (>40 tons capacity)
- Center of gravity range affects towing characteristics
- Special procedures for asymmetric loading conditions

## 5. H2/Cryo Considerations

| Parameter | Value |
|-----------|-------|
| H2 Related | No |
| Cryo Related | No |
| Special H2 Procedures | Verify H2 tank secure before towing |

## 6. BWB Considerations

- Wide track main gear (42m) provides stability but limits maneuverability
- Tow vehicle must have sufficient capacity for 365,000 kg aircraft
- Turning radius calculation accounts for BWB planform
- Ground crew positioning critical due to wide structure
- Minimum apron width: 65m for 180° turn

## 7. Constraints

### Operational
- Maximum tow speed: 8 km/h on straight sections, 4 km/h in turns
- Parking brake must be released before towing
- Minimum 2 wing walkers required for BWB
- Not approved for towing on slopes >3%

### Safety
- Shear pin inspection before each tow
- Towbar certified for aircraft weight class
- Communication system between cockpit and tow vehicle mandatory
- Emergency stop capability required

## 8. Verification

| Verification Method | Criteria | Status | Reference |
|---------------------|----------|--------|-----------|
| Load Test | Ultimate load 300 kN, no failure | Completed | TEST-10-GSE-001 |
| Towing Demonstration | 360° turn completed successfully | Completed | DEMO-10-GSE-001 |
| Clearance Check | No contact with aircraft during full range motion | Completed | INSP-10-GSE-001 |

## 9. Related Documentation

- ICD Reference: [10-ICD-003 - BWB Ground Handling ICD](../interface-control-documents/10-ICD-003_BWB_Ground_Handling_ICD.md)
- Related Standards: [MIL-DTL-24638](https://quicksearch.dla.mil/): Tow Fitting, Aircraft
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
