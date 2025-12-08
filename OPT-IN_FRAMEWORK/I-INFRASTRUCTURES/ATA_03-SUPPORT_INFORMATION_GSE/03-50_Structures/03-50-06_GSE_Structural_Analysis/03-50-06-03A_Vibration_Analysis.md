# 03-50-06-03A - Vibration Analysis

## 1. Purpose
Specification for vibration analysis of Ground Support Equipment (GSE) structures to avoid resonance, reduce fatigue, minimize noise, and ensure operational comfort and reliability.

## 2. Scope
- Modal analysis (natural frequencies and mode shapes)
- Harmonic response analysis
- Random vibration analysis
- Vibration isolation design
- Measurement and testing

## 3. Applicable Documents
- ISO 2041 (Vibration and Shock - Vocabulary)
- ISO 10816 (Mechanical Vibration - Evaluation of Machine Vibration by Measurements on Non-Rotating Parts)
- ISO 5348 (Mechanical Vibration and Shock - Mounting of Accelerometers)
- MIL-STD-810 (Environmental Engineering Considerations)
- VDI 2056 (Criteria for Evaluating Vibrations on Machinery)

## 4. Structural Description

### 4.1 Sources of Vibration
| Source | Frequency Range | Typical Magnitude |
|--------|----------------|-------------------|
| Rotating Machinery (pumps, motors) | 10-100 Hz | 0.1-10 mm/s RMS |
| Piston Engines | 20-200 Hz | 1-20 mm/s RMS |
| Hydraulic Pumps | 100-1000 Hz | 0.5-5 mm/s RMS |
| Road Excitation (mobile GSE) | 1-20 Hz | 0.5-5 g peak |
| Flow-Induced (piping) | 5-100 Hz | Variable |
| Seismic | 0.5-10 Hz | Site-specific |

### 4.2 Analysis Types
| Analysis | Purpose | Output |
|----------|---------|--------|
| Modal Analysis | Identify natural frequencies and mode shapes | f_n (Hz), mode shapes |
| Harmonic Response | Steady-state response to sinusoidal excitation | Amplitude vs frequency |
| Transient Dynamic | Time-domain response to impulse/shock | Displacement, acceleration vs time |
| Random Vibration | Response to stochastic excitation | PSD (power spectral density) |
| Fatigue (vibration) | High-cycle fatigue from vibration | Damage accumulation |

### 4.3 Resonance Avoidance
**Design Rule**: Ensure structural natural frequencies are separated from excitation frequencies
- **Separation Margin**: f_structure < 0.5×f_excitation or f_structure > 1.5×f_excitation
- **Typical GSE f_n**: 10-50 Hz for structures, 1-10 Hz for suspension systems

### 4.4 Vibration Isolation
| Isolator Type | Frequency Range | Transmissibility | Application |
|---------------|----------------|------------------|-------------|
| Rubber Mounts | 10-100 Hz | 10-30% at 2×f_n | General machinery |
| Spring Isolators | 5-50 Hz | 5-15% at 2×f_n | Heavy equipment |
| Air Springs | 1-10 Hz | 1-10% at 2×f_n | Sensitive equipment, operator isolation |
| Active Isolation | 1-100 Hz | <1% | Precision equipment (expensive) |

## 5. Structural Requirements

### 5.1 Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Natural Frequency (structures) | > 20 Hz or < 0.5×f_excitation | Design practice |
| Vibration Severity (machinery) | < 4.5 mm/s RMS (ISO Zone B) | ISO 10816-3 |
| Operator Exposure | < 0.5 m/s² RMS (8 hr) | ISO 2631 |
| Resonance Amplification | <5× static response | Damping or tuning required |
| Fatigue from Vibration | Life > 10⁸ cycles | High-cycle fatigue analysis |

### 5.2 Modal Analysis Procedure
1. Create FEA model with accurate mass and stiffness
2. Apply boundary conditions (fixed, pinned, free-free)
3. Extract modes using eigenvalue solver (Block Lanczos, PCG)
4. Review mode shapes and frequencies
5. Verify against excitation frequencies (avoid resonance)

### 5.3 Vibration Measurement
- **Sensors**: Accelerometers (piezoelectric or MEMS)
- **Locations**: Near excitation sources, at supports, on critical structures
- **Frequency Range**: DC-1000 Hz typical
- **Sampling Rate**: > 2.5× maximum frequency of interest (Nyquist)
- **Duration**: 1-10 minutes for steady-state, longer for random

### 5.4 Acceptance Criteria (ISO 10816-3)
| Vibration Severity (mm/s RMS) | Condition | Action |
|-------------------------------|-----------|--------|
| < 2.3 | Good | Normal operation |
| 2.3-7.1 | Acceptable | Monitor |
| 7.1-11.2 | Just Tolerable | Schedule maintenance |
| > 11.2 | Unacceptable | Immediate action required |

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-06-01A (FEA Structural Analysis), 03-50-06-02A (Fatigue Analysis)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-06-03A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
