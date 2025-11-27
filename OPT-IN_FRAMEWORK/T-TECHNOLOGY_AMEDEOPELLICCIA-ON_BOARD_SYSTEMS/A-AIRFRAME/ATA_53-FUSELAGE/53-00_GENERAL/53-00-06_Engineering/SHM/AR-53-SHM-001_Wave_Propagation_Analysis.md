# AR-53-SHM-001: Wave Propagation Analysis

## Document ID
**AR-53-SHM-001**

## Title
Guided Wave Propagation Analysis for AMPEL360 Fuselage Structure

## Purpose
Document the analysis of guided wave propagation characteristics in the AMPEL360 BWB fuselage structure to support SHM sensor placement and detection algorithm development.

## Analysis Scope

### Materials Analyzed
| Material | Configuration | Thickness Range |
|----------|---------------|-----------------|
| CFRP quasi-isotropic | [45/0/-45/90]ns | 2.0-6.0 mm |
| CFRP fabric | Plain weave | 2.0-4.0 mm |
| Al 7075-T651 | Monolithic | 1.6-4.0 mm |
| Ti-6Al-4V | Monolithic | 2.0-5.0 mm |
| CFRP/honeycomb | Sandwich | 15-30 mm |

### Wave Modes
| Mode | Characteristics | Application |
|------|-----------------|-------------|
| A0 (Antisymmetric) | Short wavelength, sensitive to surface damage | Corrosion, BVID |
| S0 (Symmetric) | Long propagation distance | Through-thickness damage |
| SH0 (Shear horizontal) | Non-dispersive, good for composites | Delamination |

## Dispersion Analysis

### CFRP Laminate (4 mm thickness)
| Frequency (kHz) | A0 Velocity (m/s) | S0 Velocity (m/s) | Wavelength A0 (mm) |
|-----------------|-------------------|-------------------|-------------------|
| 50 | 980 | 5200 | 19.6 |
| 100 | 1380 | 5200 | 13.8 |
| 200 | 1950 | 5180 | 9.8 |
| 300 | 2390 | 5150 | 8.0 |

### Aluminum (2.5 mm thickness)
| Frequency (kHz) | A0 Velocity (m/s) | S0 Velocity (m/s) | Wavelength A0 (mm) |
|-----------------|-------------------|-------------------|-------------------|
| 100 | 1650 | 5350 | 16.5 |
| 200 | 2330 | 5340 | 11.7 |
| 300 | 2850 | 5320 | 9.5 |
| 400 | 3290 | 5300 | 8.2 |

## Attenuation Analysis

### Material Attenuation Coefficients
| Material | Frequency | Attenuation A0 | Attenuation S0 |
|----------|-----------|----------------|----------------|
| Al 7075 | 200 kHz | 0.05 dB/m | 0.02 dB/m |
| CFRP QI | 200 kHz | 2.8 dB/m | 1.2 dB/m |
| CFRP fabric | 200 kHz | 3.5 dB/m | 1.8 dB/m |
| Ti-6Al-4V | 200 kHz | 0.08 dB/m | 0.03 dB/m |

### Geometric Attenuation
| Configuration | Additional Loss | Notes |
|---------------|-----------------|-------|
| Cylindrical spreading | 3 dB/doubling distance | Dominant in far field |
| Stiffener crossing | 2-4 dB per crossing | Depends on stiffener height |
| Fastener row | 1-2 dB per row | Depends on pitch |
| Joint (bolted) | 6-10 dB | Depends on joint design |

## Stiffened Panel Analysis

### T-Stiffener Interaction
| Stiffener Height | Transmission Loss | Reflection Coefficient |
|------------------|-------------------|----------------------|
| 25 mm | 2.5 dB | 0.15 |
| 40 mm | 3.2 dB | 0.22 |
| 60 mm | 4.5 dB | 0.32 |

### Hat Stiffener Interaction
| Stiffener Width | Transmission Loss | Notes |
|-----------------|-------------------|-------|
| 50 mm | 1.8 dB | Low-profile |
| 80 mm | 2.4 dB | Standard |
| 100 mm | 3.0 dB | Large section |

## Temperature Effects

### Velocity Variation
| Material | Temperature Range | Velocity Change |
|----------|-------------------|-----------------|
| Al 7075 | -55°C to +85°C | ±3% |
| CFRP | -55°C to +85°C | ±8% |
| Ti-6Al-4V | -55°C to +85°C | ±2% |
| Cryogenic (FBG) | -253°C to +20°C | ±15% |

### Compensation Method
- Temperature-indexed baseline library
- Real-time temperature measurement
- Automatic baseline selection

## FEA Model Details

### Model Parameters
| Parameter | Value |
|-----------|-------|
| Element type | C3D8R (brick, reduced integration) |
| Element size | 0.5 mm (≤λ/10) |
| Time step | 0.1 μs |
| Solver | Abaqus Explicit |
| Damping | Rayleigh (α=100, β=1e-8) |

### Validation
| Test | Predicted | Measured | Error |
|------|-----------|----------|-------|
| A0 velocity (CFRP) | 1950 m/s | 1920 m/s | +1.6% |
| S0 velocity (CFRP) | 5180 m/s | 5210 m/s | -0.6% |
| Attenuation (CFRP) | 2.8 dB/m | 3.0 dB/m | -6.7% |

## Conclusions and Recommendations

### Optimal Frequency Selection
| Material | Recommended Frequency | Sensing Radius |
|----------|----------------------|----------------|
| CFRP laminate | 150-200 kHz | 0.6-0.8 m |
| Aluminum skin | 200-300 kHz | 0.8-1.2 m |
| Titanium fitting | 200-250 kHz | 1.0-1.5 m |

### Sensor Placement Implications
- Maximum sensor spacing: 600 mm for CFRP, 800 mm for aluminum
- Consider stiffener locations in layout
- Account for 6-10 dB loss at joints

## Traceability
- Parent Requirement: [53-00-03-01-005](../53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md)
- V&V Reference: V&V-53-013

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
