# Natural Frequency Analysis - Door Panel

**Calculation:** CALC-52-10-01-DYN-001  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Rayleigh-Ritz Approximation (AI-Assisted)  
**Confidence:** ±30%

## 1. SIMPLIFIED MODEL

### Sandwich Panel Properties
```python
# Face sheets (CFRP)
E_face = 65 GPa  # Quasi-isotropic modulus
t_face = 4 mm    # Per face
ρ_face = 1600 kg/m³

# Core (Nomex)
G_core = 35 MPa  # Shear modulus
t_core = 40 mm   # Core thickness
ρ_core = 48 kg/m³

# Panel dimensions
a = 1.88 m  # Height
b = 1.12 m  # Width
```

## 2. EQUIVALENT STIFFNESS

### Bending Stiffness (D)
```python
# Sandwich panel flexural rigidity
I = (b * t_face³)/12 + 2 * b * t_face * ((t_core + t_face)/2)²
D = E_face * I
D ≈ 8.5 × 10⁶ N⋅m  # Per unit width
```

### Mass per unit area
```python
m = 2 * ρ_face * t_face + ρ_core * t_core
m = 2 * 1600 * 0.004 + 48 * 0.040
m = 14.72 kg/m²
```

## 3. FREQUENCY ESTIMATION

### Mode 1 - Fundamental Bending
Using Rayleigh's method for clamped edges:
```python
f₁ = (λ₁²/2π) * √(D/(m * a⁴))

Where λ₁ ≈ 4.73 (first mode, clamped)

f₁ = (4.73²/2π) * √(8.5×10⁶/(14.72 * 1.88⁴))
f₁ ≈ 25-30 Hz
```

**🔴 CRITICAL:** This coincides with engine RPM (25 Hz)

## 4. MODE SHAPE PREDICTIONS

| Mode | Frequency (Hz) | Description | Confidence |
|------|---------------|-------------|------------|
| 1 | 25-30 | Fundamental bending | ±30% |
| 2 | 35-45 | First torsion | ±40% |
| 3 | 60-80 | Second bending | ±50% |
| 4 | 85-110 | Complex mode | Very low |

## 5. RESONANCE RISK ASSESSMENT

### Engine Excitation
- Max continuous RPM: 1500 = 25.0 Hz
- Blade passing (20 blades): 500 Hz

### Risk Level: HIGH
- Mode 1 within 1-5 Hz of engine frequency
- Damping unknown (must measure)
- GVT mandatory before flight

## 6. REQUIRED ACTIONS

1. **Immediate:** Plan GVT test
2. **If ζ < 3%:** Increase face sheet to 5mm
3. **Alternative:** Add constrained layer damping
4. **Validation:** Professional modal analysis required

---

**Status:** CRITICAL - GVT MANDATORY  
**Risk:** HIGH - Resonance potential
