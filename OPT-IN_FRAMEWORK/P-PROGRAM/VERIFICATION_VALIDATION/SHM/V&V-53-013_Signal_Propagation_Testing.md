# V&V-53-013: Signal Propagation Testing

## Activity ID
**V&V-53-013**

## Title
SHM Signal Propagation Testing Program

## Objective
Characterize and validate guided wave signal propagation through aircraft structural materials and joints to verify SHM system detection capability.

## Scope
- Material-specific wave velocity characterization
- Attenuation measurement across material types
- Joint transmission loss quantification
- Temperature effect characterization

## Test Matrix

### Material Characterization
| Material | Thickness Range | Frequency Range | Specimens |
|----------|-----------------|-----------------|-----------|
| Al 7075-T651 | 1.6-4.0 mm | 100-500 kHz | 10 |
| CFRP (UD) | 2.0-6.0 mm | 50-300 kHz | 15 |
| CFRP (fabric) | 3.0-8.0 mm | 50-300 kHz | 10 |
| Ti-6Al-4V | 2.0-5.0 mm | 100-400 kHz | 8 |
| Sandwich (CFRP/HC) | 15-30 mm | 25-150 kHz | 8 |

### Joint Transmission Testing
| Joint Type | Configuration | Target Loss | Specimens |
|------------|---------------|-------------|-----------|
| Bolted metallic | Hi-lok, titanium | ≤6 dB | 12 |
| Bolted composite | Countersunk | ≤10 dB | 12 |
| Bonded composite | Secondary bond | ≤3 dB | 10 |
| Hybrid joint | Ti-CFRP | ≤8 dB | 10 |

### Temperature Testing
| Condition | Range | Soak Time | Specimens |
|-----------|-------|-----------|-----------|
| Standard | +20°C | 2 hours | All |
| Cold | -55°C | 4 hours | 20 |
| Hot | +85°C | 4 hours | 20 |
| Cryogenic | -253°C | 4 hours | 10 (cryo zone) |

## Test Procedures

### Velocity Measurement
1. Install reference sensor pair at known separation
2. Execute pitch-catch acquisition
3. Calculate group velocity from ToF
4. Repeat for multiple frequencies and modes

### Attenuation Measurement
1. Configure sensor array at multiple distances
2. Acquire signals at each position
3. Calculate amplitude decay curve
4. Determine attenuation coefficient (dB/m)

### Joint Transmission
1. Install sensors on each side of joint
2. Measure transmitted signal amplitude
3. Calculate transmission loss
4. Document frequency dependence

## Pass Criteria

| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Velocity accuracy | ±5% of predicted | Per SAFE analysis |
| Attenuation (Al) | ≤15 dB/m | Per 53-00-03-01-005 |
| Attenuation (CFRP) | ≤20 dB/0.75m | Per 53-00-03-01-005 |
| Joint loss (bolted) | ≤10 dB | Per 53-00-03-01-005 |
| Temperature stability | ≤10% velocity change | -55°C to +85°C |

## Traceability

### Requirements Verified
| Requirement | Criteria | Method |
|-------------|----------|--------|
| [53-00-03-01-005](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md) | Signal attenuation | Test |
| 53-00-03-07-002 | Signal quality | Test |

## Deliverables
- Signal Propagation Test Report (TR-53-013)
- Material Characterization Database
- Temperature Compensation Algorithm Validation
- Joint Transmission Loss Atlas

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **DRAFT** |
| Repository | `AMPEL360-BWB-H2-Hy-E` |
| Last AI Update | 2025-11-27 |

---
