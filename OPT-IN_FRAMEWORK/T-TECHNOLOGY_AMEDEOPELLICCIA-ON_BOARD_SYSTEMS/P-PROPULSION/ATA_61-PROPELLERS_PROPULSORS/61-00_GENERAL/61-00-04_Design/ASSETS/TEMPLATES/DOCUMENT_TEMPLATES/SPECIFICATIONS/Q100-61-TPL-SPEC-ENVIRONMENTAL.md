# Environmental Specification

<!-- TEMPLATE INSTRUCTIONS (Remove this section when using)
Template ID: Q100-61-TPL-SPEC-ENVIRONMENTAL
Version: 1.0

This template defines environmental requirements and test conditions.
Fill in all sections marked with [REQUIRED].
-->

---

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | [REQUIRED: e.g., 61-00-04-SPEC-003] |
| **Title** | [REQUIRED: Environmental Specification Title] |
| **Subject** | [REQUIRED: Component/System Name] |
| **Version** | 1.0 |
| **Status** | Draft |
| **Author** | [REQUIRED] |
| **Date** | [REQUIRED: YYYY-MM-DD] |

---

## 1. Scope

### 1.1 Purpose

[REQUIRED: Describe the environmental requirements covered]

### 1.2 Equipment Category

[REQUIRED: Define equipment category per DO-160 or applicable standard]

---

## 2. Reference Standards

| Standard | Title | Sections |
|----------|-------|----------|
| RTCA DO-160G | Environmental Conditions and Test Procedures | [Sections] |
| MIL-STD-810G | Environmental Engineering Considerations | [Methods] |

---

## 3. Temperature

### 3.1 Ground Operating

| Condition | Temperature | Duration |
|-----------|-------------|----------|
| Low | [REQUIRED: °C] | [hours] |
| High | [REQUIRED: °C] | [hours] |

### 3.2 Flight Operating

| Condition | Temperature | Altitude |
|-----------|-------------|----------|
| Cruise | [REQUIRED: °C] | [m/ft] |
| Climb | [REQUIRED: °C] | [m/ft] |

### 3.3 Storage/Transport

| Condition | Temperature | Duration |
|-----------|-------------|----------|
| Low | [°C] | [hours] |
| High | [°C] | [hours] |

---

## 4. Altitude

| Condition | Altitude | Pressure |
|-----------|----------|----------|
| Maximum Operating | [REQUIRED: m/ft] | [kPa] |
| Maximum Survival | [m/ft] | [kPa] |
| Rapid Decompression | [m/ft to m/ft] | [Rate] |

---

## 5. Humidity

| Condition | Requirement |
|-----------|-------------|
| Operating Range | [REQUIRED: %RH] |
| Condensing | [Yes/No] |
| Test Method | [DO-160 Section X] |

---

## 6. Vibration

### 6.1 Random Vibration

| Axis | Frequency Range | PSD Level | Duration |
|------|-----------------|-----------|----------|
| [X/Y/Z] | [Hz-Hz] | [g²/Hz] | [min] |

### 6.2 Sinusoidal Vibration

| Axis | Frequency | Amplitude | Sweep Rate |
|------|-----------|-----------|------------|
| [X/Y/Z] | [Hz] | [g] | [oct/min] |

---

## 7. Shock

| Condition | Peak | Duration | Waveform |
|-----------|------|----------|----------|
| Operational | [g] | [ms] | [Half-sine] |
| Crash Safety | [g] | [ms] | [Triangular] |

---

## 8. Other Environmental Conditions

### 8.1 Salt Fog

[Requirements if applicable]

### 8.2 Fungus

[Requirements if applicable]

### 8.3 Sand and Dust

[Requirements if applicable]

### 8.4 Fluids Susceptibility

[List fluids and exposure requirements]

---

## 9. EMI/EMC

| Requirement | Standard | Category |
|-------------|----------|----------|
| Conducted Emissions | DO-160 Section 21 | [Category] |
| Radiated Emissions | DO-160 Section 21 | [Category] |
| Conducted Susceptibility | DO-160 Section 22 | [Category] |
| Radiated Susceptibility | DO-160 Section 20 | [Category] |

---

## 10. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
