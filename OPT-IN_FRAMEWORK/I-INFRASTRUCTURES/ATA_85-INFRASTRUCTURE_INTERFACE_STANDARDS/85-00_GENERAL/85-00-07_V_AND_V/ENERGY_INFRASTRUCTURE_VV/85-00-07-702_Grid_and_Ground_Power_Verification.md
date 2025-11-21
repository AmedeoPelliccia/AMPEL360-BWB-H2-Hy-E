# 85-00-07-702: Grid and Ground Power Verification

## 1. Purpose
Verify that grid-connected and ground power systems provide clean, stable electrical power to aircraft per [ISO 6858](https://www.iso.org/standard/13368.html).

## 2. Power Requirements
### 2.1 Voltage
- **Single-Phase 115 VAC**: ±3% (111.55 - 118.45 VAC)
- **Three-Phase 200 VAC**: ±3% (194.0 - 206.0 VAC line-to-line)
- **Frequency**: 400 Hz ±1% (396 - 404 Hz)

### 2.2 Load Capacity
- **Peak Load**: Sufficient for all aircraft systems (e.g., 90 kVA for wide-body)
- **Continuous Load**: Sustained power for extended ground time
- **Inrush Current**: Capable of handling motor start transients

### 2.3 Power Quality
- **Total Harmonic Distortion (THD)**: < 5% (voltage), < 10% (current)
- **Power Factor**: > 0.9
- **Voltage Imbalance**: < 2% (three-phase)

## 3. Verification Methods
### 3.1 Steady-State Testing
- **Load Steps**: Incrementally increase load, measure voltage/frequency stability
- **Sustained Load**: Full load for 4 hours (typical turnaround + ground hold)
- **No-Load to Full-Load**: Voltage sag/swell measurement

### 3.2 Transient Testing
- **Motor Start**: Large compressor or pump start, measure voltage dip
- **Load Rejection**: Sudden load drop, measure overvoltage
- **Phase Loss**: Simulate single-phase failure (three-phase system)

### 3.3 Harmonic Analysis
- **Spectrum Analyzer**: Measure individual harmonics up to 50th order
- **THD Calculation**: Per IEEE 519
- **Filter Effectiveness**: Verify harmonic filters reduce THD

## 4. Test Configurations
### 4.1 Fixed Ground Power (FGP)
- Permanent installation at gate (underground or overhead)
- 400 Hz rotary or solid-state converter
- Cable run: ≤ 30 m (voltage drop consideration)

### 4.2 Mobile Ground Power Unit (GPU)
- Trailer-mounted generator or converter
- Diesel generator (rotary converter) or solid-state (inverter)
- Cable: Standard ISO 6858 connector

### 4.3 Grid-Connected Inverter
- Renewable energy (solar/wind) via grid-tie inverter
- Battery energy storage system (BESS) for grid buffering
- Seamless transfer between grid and backup

## 5. Acceptance Criteria
### 5.1 Steady-State
- **Voltage**: Within ±3% for 99.9% of test duration
- **Frequency**: Within ±1% for 100% of test duration
- **THD**: < 5% voltage, < 10% current

### 5.2 Transient
- **Voltage Sag**: ≤ 10% for motor start (< 1 second duration)
- **Recovery Time**: Return to ±3% within 1 second
- **No Nuisance Trips**: Aircraft circuit breakers remain closed

## 6. Environmental Testing
- **Temperature**: -40°C to +50°C ambient
- **Humidity**: Up to 95% relative humidity
- **Altitude**: Airport elevation effects (reduced cooling)

## 7. Documentation
- **Power Quality Reports**: Harmonic spectrum, voltage/frequency stability
- **Compliance Certificates**: ISO 6858, MIL-STD-704F
- Test reports: [85-00-07-A-702](./ASSETS/85-00-07-A-702_Energy_Interface_Test_Reports.xlsx)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
