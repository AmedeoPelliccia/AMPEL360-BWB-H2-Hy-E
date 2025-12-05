# Interface Specification

<!-- TEMPLATE INSTRUCTIONS (Remove this section when using)
Template ID: Q100-61-TPL-SPEC-INTERFACE
Version: 1.0

This template defines interface requirements between systems or components.
Fill in all sections marked with [REQUIRED].
-->

---

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | [REQUIRED: e.g., 61-00-04-ICD-001] |
| **Title** | [REQUIRED: Interface Specification Title] |
| **Systems** | [REQUIRED: System A ↔ System B] |
| **Version** | 1.0 |
| **Status** | Draft |
| **Author** | [REQUIRED] |
| **Date** | [REQUIRED: YYYY-MM-DD] |

---

## 1. Scope

### 1.1 Purpose

[REQUIRED: Describe the interface and its purpose]

### 1.2 Interface Parties

| Party | System/Component | Owner |
|-------|------------------|-------|
| Provider | [REQUIRED] | [Name] |
| Consumer | [REQUIRED] | [Name] |

---

## 2. Physical Interface

### 2.1 Mechanical Interface

| Parameter | Requirement | Tolerance |
|-----------|-------------|-----------|
| Mounting Pattern | [REQUIRED] | [±Tol] |
| Envelope | [L × W × H mm] | [±Tol] |
| Mass | [kg] | [±Tol] |
| CG Location | [x, y, z mm] | [±Tol] |

### 2.2 Connection Points

| ID | Type | Location | Torque |
|----|------|----------|--------|
| [CP-001] | [Bolt/Pin/Latch] | [Coordinates] | [N·m] |

---

## 3. Electrical Interface

### 3.1 Power Interface

| Signal | Voltage | Current | Connector | Pin |
|--------|---------|---------|-----------|-----|
| [+28V DC] | [28 VDC] | [10 A max] | [Type] | [#] |

### 3.2 Signal Interface

| Signal Name | Type | Range | Rate | Connector | Pin |
|-------------|------|-------|------|-----------|-----|
| [Signal] | [Analog/Digital] | [0-5V] | [Hz] | [Type] | [#] |

---

## 4. Data Interface

### 4.1 Protocol

| Parameter | Value |
|-----------|-------|
| Protocol | [ARINC 429 / CAN / Ethernet] |
| Baud Rate | [REQUIRED] |
| Word Size | [bits] |
| Parity | [Odd/Even/None] |

### 4.2 Message Definition

| Label/ID | Name | Rate | Content |
|----------|------|------|---------|
| [0x123] | [Message Name] | [Hz] | [Description] |

---

## 5. Thermal Interface

| Parameter | Requirement |
|-----------|-------------|
| Heat Dissipation | [REQUIRED: W] |
| Interface Temperature | [REQUIRED: °C range] |
| Thermal Resistance | [°C/W if applicable] |

---

## 6. Fluid Interface

| Port | Fluid | Pressure | Flow Rate | Connection |
|------|-------|----------|-----------|------------|
| [P1] | [Fluid] | [bar] | [L/min] | [Type/Size] |

---

## 7. Verification

| Requirement | Method | Criteria |
|-------------|--------|----------|
| [IF-001] | [Inspection/Test] | [Acceptance] |

---

## 8. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
