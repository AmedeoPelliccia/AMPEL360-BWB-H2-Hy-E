# 53-80-00-02 — Energy System Design Rules

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-00-02 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / DESIGN RULES |

---

## 1. Purpose

This document establishes mandatory design rules for all 53-80 Energy systems, ensuring consistency, safety, and maintainability across electrical and thermal distribution systems within the ANCHORS architecture.

## 2. General Design Principles

### 2.1 Fundamental Rules

| Rule ID | Rule | Rationale |
|---------|------|-----------|
| DR-NRG-001 | All power paths shall be redundant or fail-safe | Safety requirement |
| DR-NRG-002 | Thermal buses shall have backup circulation | Prevent thermal runaway |
| DR-NRG-003 | Protection devices shall fail to safe state | CS-25.1309 compliance |
| DR-NRG-004 | All energy flows shall be metered | Efficiency monitoring |
| DR-NRG-005 | Manual isolation shall be available | Maintenance access |

### 2.2 Separation Requirements

| Rule ID | Rule | Rationale |
|---------|------|-----------|
| DR-NRG-010 | HT and LT coolant circuits shall be physically separated | Cross-contamination prevention |
| DR-NRG-011 | HVDC and 28V circuits shall have galvanic isolation | Safety |
| DR-NRG-012 | Power and thermal control wiring shall be separated | EMI |
| DR-NRG-013 | Redundant paths shall use different routings | Common-cause protection |

## 3. Electrical Design Rules

### 3.1 HVDC Bus Rules

| Rule ID | Rule | Value/Limit | Verification |
|---------|------|-------------|--------------|
| DR-E-001 | Nominal bus voltage | 750 VDC | Analysis |
| DR-E-002 | Bus voltage range | 650-850 VDC | Test |
| DR-E-003 | Maximum ripple | < 2% peak-to-peak | Test |
| DR-E-004 | Grounding scheme | TN-S | Design review |
| DR-E-005 | Insulation resistance | > 1 MΩ | Test |
| DR-E-006 | Creepage distance | > 8 mm/kV | Inspection |
| DR-E-007 | Clearance distance | > 4 mm/kV | Inspection |

### 3.2 Conductor Sizing

| Rule ID | Rule | Details |
|---------|------|---------|
| DR-E-010 | Current derating | 80% of rated capacity in bundles |
| DR-E-011 | Voltage drop | < 3% at full load |
| DR-E-012 | Temperature rating | ≥ 150°C for HVDC |
| DR-E-013 | Shielding | 360° shield on HVDC cables |
| DR-E-014 | Termination | Crimped terminals with witness holes |

### 3.3 Protection Coordination

```
Level 1: Load SSCB (< 1 ms)
    ↓ Fails to clear
Level 2: Channel SSCB (< 10 ms)
    ↓ Fails to clear
Level 3: GFI (< 50 ms)
    ↓ Fails to clear
Level 4: Bus MCCB (< 100 ms)
    ↓ Fails to clear
Level 5: Battery Contactor (< 200 ms)
```

| Rule ID | Rule | Details |
|---------|------|---------|
| DR-E-020 | Protection selectivity | 10:1 time margin between levels |
| DR-E-021 | Let-through energy | I²t < component withstand |
| DR-E-022 | Arc flash protection | Category 2 or better |
| DR-E-023 | Fault current rating | 150% of maximum prospective |

## 4. Thermal Design Rules

### 4.1 Coolant System Rules

| Rule ID | Rule | Value/Limit | Rationale |
|---------|------|-------------|-----------|
| DR-T-001 | HT operating range | 80-90°C | Heat source matching |
| DR-T-002 | LT operating range | 45-55°C | Component limits |
| DR-T-003 | Maximum HT temperature | 100°C | Material limits |
| DR-T-004 | Maximum LT temperature | 70°C | Battery safety |
| DR-T-005 | Coolant type | 50% propylene glycol/water | Freeze protection |
| DR-T-006 | Minimum flow HT | 80 L/min | Heat transfer |
| DR-T-007 | Minimum flow LT | 120 L/min | Cooling capacity |

### 4.2 Heat Exchanger Rules

| Rule ID | Rule | Details |
|---------|------|---------|
| DR-T-010 | Approach temperature | ≥ 5°C for liquid-liquid |
| DR-T-011 | Fouling factor | 0.0002 m²·K/W minimum |
| DR-T-012 | Pressure drop | < 50 kPa per exchanger |
| DR-T-013 | Material compatibility | Aluminum alloy or SS316 |
| DR-T-014 | Leak detection | Continuous pressure monitoring |

### 4.3 Pump Design Rules

| Rule ID | Rule | Details |
|---------|------|---------|
| DR-T-020 | Pump redundancy | 100% backup capacity |
| DR-T-021 | NPSH margin | ≥ 1.5× required NPSH |
| DR-T-022 | Speed control | Variable frequency drive |
| DR-T-023 | Seal type | Magnetic coupling (leak-free) |
| DR-T-024 | Cavitation protection | Low-flow interlock |

## 5. Power Conversion Rules

### 5.1 DC-DC Converter Rules

| Rule ID | Rule | Value/Limit |
|---------|------|-------------|
| DR-C-001 | Minimum efficiency | 95% at rated load |
| DR-C-002 | Efficiency at 25% load | ≥ 90% |
| DR-C-003 | Output ripple | < 1% for all outputs |
| DR-C-004 | Transient response | < 5% overshoot |
| DR-C-005 | Parallel operation | Active current sharing |
| DR-C-006 | Soft start | Inrush current < 2× rated |

### 5.2 Bidirectional Converter Rules

| Rule ID | Rule | Details |
|---------|------|---------|
| DR-C-010 | Mode transition | Seamless, < 10 ms |
| DR-C-011 | Power reversal rate | < 100 kW/s |
| DR-C-012 | Battery precharge | Automatic, < 5 s |
| DR-C-013 | Regeneration limit | 800 kW maximum |

## 6. Control and Monitoring Rules

### 6.1 Sensor Requirements

| Rule ID | Rule | Details |
|---------|------|---------|
| DR-M-001 | Voltage measurement | ±0.5% accuracy |
| DR-M-002 | Current measurement | ±1% accuracy |
| DR-M-003 | Temperature measurement | ±0.5°C accuracy |
| DR-M-004 | Flow measurement | ±2% accuracy |
| DR-M-005 | Pressure measurement | ±1% accuracy |
| DR-M-006 | Sensor redundancy | Dual sensors for safety-critical |

### 6.2 Control Loop Rules

| Rule ID | Rule | Details |
|---------|------|---------|
| DR-M-010 | Power control rate | 10 Hz minimum |
| DR-M-011 | Thermal control rate | 1 Hz minimum |
| DR-M-012 | Protection response | < 1 ms for SSCB |
| DR-M-013 | Command acknowledgment | < 100 ms |
| DR-M-014 | Watchdog timeout | 500 ms maximum |

## 7. Environmental Design Rules

### 7.1 Operating Environment

| Rule ID | Rule | Value |
|---------|------|-------|
| DR-ENV-001 | Temperature range | -40°C to +70°C |
| DR-ENV-002 | Altitude | 0 to 45,000 ft |
| DR-ENV-003 | Humidity | 0 to 100% RH |
| DR-ENV-004 | Vibration | DO-160 Cat S2 |
| DR-ENV-005 | EMI | DO-160 Cat M |

### 7.2 Materials

| Rule ID | Rule | Details |
|---------|------|---------|
| DR-ENV-010 | Flammability | FAR 25.853 compliant |
| DR-ENV-011 | Toxicity | Low smoke, low toxicity |
| DR-ENV-012 | Corrosion protection | Salt spray 500 hrs |
| DR-ENV-013 | Fluid compatibility | Tested with all coolants |

## 8. Documentation Rules

### 8.1 Required Documentation

| Rule ID | Document Type | Requirement |
|---------|---------------|-------------|
| DR-DOC-001 | Schematic diagrams | All power/thermal circuits |
| DR-DOC-002 | Wiring diagrams | Point-to-point connections |
| DR-DOC-003 | P&ID | All thermal systems |
| DR-DOC-004 | Protection coordination study | Selectivity analysis |
| DR-DOC-005 | FMEA | All energy components |

### 8.2 Traceability

| Rule ID | Rule | Details |
|---------|------|---------|
| DR-DOC-010 | Requirements tracing | All requirements to design |
| DR-DOC-011 | Test coverage | 100% of requirements |
| DR-DOC-012 | Hazard tracking | Link to SSA |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-00-02 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Author** | AMPEL360 Energy Systems Team |
| **Reviewer** | _[To be assigned]_ |
| **Approver** | _[To be assigned]_ |

### AI Disclosure

- **Generated with assistance of:** AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT — Subject to human review and approval
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-27

---

*END OF DOCUMENT*
