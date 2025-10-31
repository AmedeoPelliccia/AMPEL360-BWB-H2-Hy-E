# Overview: 18-40-01 - Open-Fan Propulsor Acoustics

## 1.0 Purpose
This component establishes the noise analysis, prediction, and mitigation framework for the AMPEL360's unducted open-fan propulsors—the primary noise source on the aircraft and a critical certification challenge.

## 2.0 Propulsor Configuration

### 2.1 Physical Description
- **Type:** Counter-rotating open rotor (CROR) / unducted fan
- **Location:** Upper surface BWB mounting (twin nacelles)
- **Blade Count:** 12 blades (front rotor) + 10 blades (aft rotor)
- **Diameter:** 5.2 meters
- **Tip Speed:** Mach 0.78 at takeoff power
- **Rotational Speed:** Variable (1,200-1,800 RPM)
- **Blade Design:** Swept scimitar profile with composite construction

### 2.2 Acoustic Characteristics
**Primary Noise Sources:**
1. **Blade Passage Frequency (BPF) Tones:** Discrete frequency components at N×RPM×blade_count
2. **Tip Vortex Noise:** Broadband noise from blade tip aerodynamics
3. **Interaction Noise:** Front rotor wake impinging on aft rotor blades
4. **Installation Effects:** Noise reflection/diffraction from BWB upper surface
5. **Haystacking:** Multiple discrete tones creating comb-like spectrum

**Noise Levels (Preliminary):**
- **Maximum Takeoff:** 105 EPNdB (sideline), 98 EPNdB (flyover), 95 EPNdB (approach)
- **Cruise:** 85 dBA (in cabin with treatment), 110 dB SPL (far-field)
- **Ground Operations:** 95 dBA @ 100m (regulatory limit: 100 dBA)

## 3.0 Regulatory Requirements

### 3.1 ICAO Annex 16 Compliance
**Target:** Stage 5 certification with ≥12 EPNdB cumulative margin

| Measurement Point | ICAO Stage 5 Limit | AMPEL360 Target | Margin |
|-------------------|--------------------|-----------------|--------|
| Lateral (Sideline) | 94.0 EPNdB | 90.0 EPNdB | 4.0 EPNdB |
| Flyover (Approach) | 89.0 EPNdB | 85.0 EPNdB | 4.0 EPNdB |
| Approach | 98.0 EPNdB | 94.0 EPNdB | 4.0 EPNdB |
| **Cumulative** | **281.0 EPNdB** | **269.0 EPNdB** | **12.0 EPNdB** |

### 3.2 Community Noise Limits
- **Airport Noise Zoning:** Comply with 55 dBA DNL at airport boundary (FAA Part 150)
- **EU Night Restrictions:** <65 dB Lmax for night operations (23:00-06:00 local)
- **ICAO Balanced Approach:** Demonstrate best available noise reduction technology

## 4.0 Noise Prediction Methods

### 4.1 Computational Aeroacoustics (CAA)
**Software:** PowerFLOW (Lattice-Boltzmann method) + Ffowcs Williams-Hawkings (FW-H) acoustic analogy

**Modeling Approach:**
1. High-fidelity geometry: Full propulsor + pylon + BWB upper surface (1 billion voxels)
2. Transient simulation: 10 rotor revolutions at 0.2ms timestep
3. Acoustic surface: Permeable FW-H surface enclosing propulsor
4. Far-field projection: Free-field Green's function to observer locations
5. Validation: Compare to wind tunnel data (correlation >95%)

**Predicted Noise Spectrum:**
- **BPF Fundamental (Front):** 240 Hz @ 1,200 RPM (12 blades × 20 Hz rotation)
- **BPF Fundamental (Aft):** 200 Hz @ 1,200 RPM (10 blades × 20 Hz)
- **Interaction Tone:** 440 Hz (12×20 + 10×20 beat frequency)
- **Harmonics:** Up to 10th harmonic (4.4 kHz) above background

**Uncertainty:** ±2 dB SPL (validated against wind tunnel data)

### 4.2 Empirical Methods
**NASA Glenn Propeller Noise Model:**
- Based on legacy propeller test data (1980s-1990s)
- Correction factors for modern blade designs (-3 dB)
- Installation correction for BWB mounting (+2 dB reflection)

**ANOPP (Aircraft Noise Prediction Program):**
- Semi-empirical model for certification compliance prediction
- Uses blade element theory + acoustic mapping
- Conservative approach: adds 3 dB margin to CAA results

### 4.3 Wind Tunnel Testing
**Facility:** NASA Ames 40×80 ft Wind Tunnel (largest in North America)

**Test Configuration:**
- 1/7-scale propulsor model (0.74m diameter)
- Tip speed matched to flight (M_tip = 0.78)
- 48-microphone phased array for source localization
- Anechoic foam treatment for free-field conditions

**Test Matrix:**
- **Mach Numbers:** 0.2 (approach), 0.25 (takeoff), 0.78 (cruise)
- **Blade Angles:** 15°, 30°, 45° (propulsor pitch settings)
- **Installation Effects:** With/without BWB upper surface simulator

**Results:**
- BPF tone levels: ±1 dB agreement with CAA
- Broadband noise: ±3 dB agreement (higher uncertainty)
- Directivity patterns: Excellent agreement (<5° error in peak direction)

## 5.0 Noise Mitigation Strategies

### 5.1 Aeroacoustic Blade Design
**Blade Sweep:**
- 35° sweep angle at tip reduces tip vortex strength
- Delays transonic effects (keeps flow attached at M_tip = 0.78)
- **Benefit:** -2 dB BPF tone reduction vs. unswept baseline

**Scimitar Profile:**
- Curved blade planform (forward sweep near tip, aft sweep at root)
- Reduces spanwise pressure gradient (weaker tip vortex)
- **Benefit:** -1.5 dB broadband noise reduction

**Blade Clipping:**
- Truncated blade tips (5% diameter reduction)
- Eliminates strongest tip vortex formation
- **Trade-off:** +0.5% thrust loss, -3 dB tip vortex noise

**Low-Noise Airfoil Sections:**
- Proprietary NASA-developed airfoils (NLF-series)
- Maximize laminar flow extent (reduces turbulent boundary layer noise)
- **Benefit:** -1 dB broadband noise reduction

**Cumulative Design Benefit:** -7 to -8 dB vs. unoptimized open rotor

### 5.2 Operational Noise Reduction Procedures

**Variable Speed Operation:**
- Avoid resonant frequencies (BPF ≠ structural modes)
- Lower RPM during approach/departure (noise-power trade study)
- **Approach:** 1,200 RPM (vs. 1,500 RPM max), -4 dB noise, +2% fuel burn

**Blade Pitch Scheduling:**
- Lower blade angles during community-sensitive operations
- Digital control optimizes thrust-noise trade in real-time
- **Benefit:** -2 dB during approach with <5% thrust loss

**Noise Abatement Procedures (NAP):**
- Steep climb gradient (6° vs. standard 4°) to gain altitude quickly
- Delayed acceleration to reduce ground-level noise footprint
- **Benefit:** -5 dB perceived noise at sensitive receptors

### 5.3 Installation Effects Mitigation

**Acoustic Liner:**
- Porous acoustic treatment on BWB upper surface (around propulsor)
- Honeycomb core + perforated face sheet (tuned to BPF)
- **Benefit:** -2 dB reflected noise component

**Propulsor Mounting Height:**
- 1.8m above BWB surface (optimized for shielding vs. performance)
- Ground effect: Reduces perceived noise by -3 dB vs. wing-mounted config
- **Trade-off:** +1% drag penalty, structural complexity

**Differential Blade Count:**
- Front/aft rotors have different blade counts (12/10) to minimize interaction tones
- Prevents coincidence of BPF harmonics (no additive reinforcement)
- **Benefit:** -2 dB interaction tone reduction

## 6.0 Certification Test Plan

### 6.1 Noise Certification Testing
**Location:** Edwards Air Force Base, CA (FAA-approved noise certification range)

**Procedure per FAA AC 36-4C:**
1. **Pre-Test:**
   - Microphone calibration (±0.5 dB)
   - Weather monitoring (wind <6 m/s, temp 15-35°C)
   - Aircraft weight verification (must be at max takeoff weight ±1%)

2. **Takeoff Test (6 runs minimum):**
   - Full thrust on runway, accelerate to V2+10 kts
   - Maintain V2+10 to 10,000 ft AGL
   - Microphones: Sideline (450m), Flyover (6,500m from brake release)
   - Record: Time history, 1/3-octave spectra, EPNdB

3. **Approach Test (6 runs minimum):**
   - Stabilized 3° glide slope, Vref + 5 kts
   - Constant power from 10,000 ft to 600 ft AGL
   - Microphone: 2,000m from runway threshold, centerline
   - Record: Same as takeoff

4. **Data Processing:**
   - Apply atmospheric corrections (absorption, temperature gradient)
   - Calculate tone-corrected perceived noise level (PNLT)
   - Integrate to effective perceived noise level (EPNL)
   - Apply 10s averaging per ICAO Annex 16

**Acceptance Criteria:**
- All 3 measurement points ≤ Stage 5 limits
- Cumulative margin ≥ 10 EPNdB (with 2 dB test uncertainty)

### 6.2 Flight Test Instrumentation
**Onboard Sensors:**
- 12× cabin microphones (ICP Type 377B10, ±1 dB, 10 Hz - 20 kHz)
- 8× external microphones (flush-mounted on fuselage/nacelle)
- 24× accelerometers (structural vibration correlation)
- GPS/INS (position/velocity for flight path reconstruction)

**Data Acquisition:**
- National Instruments PXI system (200 channels, 48 kHz sampling)
- Synchronized with aircraft ACMS (time-code generator)
- Redundant recording (onboard + telemetry)

**Test Points:**
- Steady-state cruise: Various Mach numbers (0.70, 0.75, 0.78, 0.80)
- Transient maneuvers: Climb, descent, level acceleration
- Propulsor power sweeps: 50%, 75%, 100% thrust

## 7.0 Operational Monitoring

### 7.1 In-Service Noise Monitoring
**ACMS Parameters:**
- `PROP_RPM_FWD`, `PROP_RPM_AFT`: Blade passage frequency calculation
- `CABIN_NOISE_LEVEL`: Averaged cabin microphone (A-weighted dBA)
- `EXTERNAL_NOISE_EVENT`: Exceedance flag (>threshold during takeoff/landing)

**Trending Analysis:**
- Plot cabin noise vs. flight hours (detect acoustic treatment degradation)
- Compare fleet-wide noise levels (identify outlier aircraft)
- Correlate with maintenance events (e.g., blade replacement, liner damage)

### 7.2 Community Noise Monitoring
**Airport Permanent Monitors:**
- Collaborate with airport authorities for permanent noise monitoring stations
- Correlate AMPEL360 operations with community noise measurements
- Validate compliance with 55 dBA DNL limits

**Complaint Tracking:**
- Database of noise complaints associated with AMPEL360 operations
- Investigate complaints >65 dBA Lmax (typical threshold for annoyance)
- Implement corrective actions if complaint rate >1 per 10,000 operations

## 8.0 Interfaces
- **ATA 00-50:** Operational limitations (noise abatement procedures)
- **ATA 02-20:** Flight Operations (NAP procedures in FCOM)
- **ATA 44-30:** Active noise cancellation system (cabin ANC)
- **ATA 45-31:** ACMS monitoring (noise/vibration data)
- **ATA 61-10:** Propulsor design (blade aeroacoustics)
- **ATA 71-20:** Engine control (variable speed for noise reduction)
- **ATA 92-30:** Predictive maintenance (noise signature analysis)
