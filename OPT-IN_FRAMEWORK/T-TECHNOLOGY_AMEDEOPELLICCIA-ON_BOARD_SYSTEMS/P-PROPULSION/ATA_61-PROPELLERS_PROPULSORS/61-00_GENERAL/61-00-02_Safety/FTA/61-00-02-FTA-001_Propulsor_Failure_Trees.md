# 61-00-02-FTA-001 — Propulsor Failure Trees

## Document Information

- **Document ID**: 61-00-02-FTA-001
- **Title**: Fault Tree Analysis — Propulsor Failure Trees
- **Version**: 1.0
- **Date**: 2025-12-03
- **Status**: Draft
- **Category**: Safety / FTA
- **ATA Chapter**: 61 — Propellers/Propulsors

---

## 1. Purpose

This document presents the **Fault Tree Analysis (FTA)** for the ATA 61 Propellers/Propulsors domain within the AMPEL360 Q100 BWB H2/Hybrid-Electric aircraft.

The FTA:

- Develops logical models for top-level propulsor failure events
- Identifies cut sets and minimal cut sets
- Calculates failure probabilities for comparison with safety objectives
- Supports validation of the PSSA safety requirements

The analysis follows [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) methodology.

---

## 2. Scope

### 2.1 Top Events Analyzed

The following top events are analyzed based on the SFHA hazards:

| Top Event ID | Top Event Description | Source Hazard | Probability Objective |
|--------------|----------------------|---------------|----------------------|
| TE-61-001 | Loss of all propulsor thrust | H-61-001 | < 1×10⁻⁹ |
| TE-61-002 | Asymmetric thrust — uncontrollable | H-61-002 | < 1×10⁻⁷ |
| TE-61-003 | Propulsor overspeed (uncontained) | H-61-004, H-61-006 | < 1×10⁻⁷ |

### 2.2 Analysis Boundaries

- System boundaries per [61-00-01-001 Domain Description](../../61-00-01_Overview/61-00-01-001_ATA_61_Domain_Description.md)
- Failure data sources: Industry standards, supplier data, assumed values (noted)
- Exposure time: Per flight hour unless otherwise stated

---

## 3. Fault Tree Symbology

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         Fault Tree Symbols                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌─────┐                                                               │
│   │     │  Rectangle: Event (intermediate or top)                       │
│   └─────┘                                                               │
│                                                                         │
│   ○         Circle: Basic event (component failure)                     │
│                                                                         │
│   ◇         Diamond: Undeveloped event                                  │
│                                                                         │
│   △         House: External event (normally TRUE or FALSE)              │
│                                                                         │
│    ╱╲                                                                   │
│   ╱  ╲      AND gate: All inputs must occur                             │
│  ╱____╲                                                                 │
│                                                                         │
│    ╱╲                                                                   │
│   ╱  ╲      OR gate: Any input causes output                            │
│  ╱≥1__╲                                                                 │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 4. TE-61-001: Loss of All Propulsor Thrust

### 4.1 Fault Tree Structure

```
                    ┌─────────────────────────┐
                    │    TE-61-001            │
                    │ Loss of All Propulsor   │
                    │       Thrust            │
                    └───────────┬─────────────┘
                                │
                           ╱────┴────╲
                          ╱    OR     ╲
                         ╱_____≥1_____╲
                    ┌────────┼────────┐
                    │        │        │
            ┌───────┴───┐ ┌──┴───┐ ┌──┴──────────┐
            │ G-61-001  │ │G-002 │ │   G-003     │
            │ All 4     │ │Common│ │  Common     │
            │ Propulsor │ │Power │ │  Control    │
            │ Failures  │ │Loss  │ │  Failure    │
            └─────┬─────┘ └──┬───┘ └──────┬──────┘
                  │          │            │
             ╱────┴────╲     │       ╱────┴────╲
            ╱   AND     ╲    │      ╱    OR     ╲
           ╱_____________╲   │     ╱_____≥1_____╲
       ┌───┬───┬───┬───┐     │         ┌────┴────┐
       │   │   │   │   │     │         │         │
       ○   ○   ○   ○   │     ○         ○         ○
      P1  P2  P3  P4  │  Complete   Common    Common
     Fail Fail Fail Fail  Power     Software  Hardware
                       │   Loss       Fault     Fault
                       │
                  ╱────┴────╲
                 ╱   AND     ╲
                ╱_____________╲
                    │     │
                    ○     ○
                FC1+FC2  Battery
                 Loss    Loss
```

### 4.2 Event Descriptions

| Event ID | Description | Failure Rate/Probability |
|----------|-------------|-------------------------|
| P1 Fail | Propulsor 1 complete failure | 1×10⁻⁴ /FH (assumed) |
| P2 Fail | Propulsor 2 complete failure | 1×10⁻⁴ /FH (assumed) |
| P3 Fail | Propulsor 3 complete failure | 1×10⁻⁴ /FH (assumed) |
| P4 Fail | Propulsor 4 complete failure | 1×10⁻⁴ /FH (assumed) |
| Complete Power Loss | Loss of all electrical power sources | TBD (from ATA 24 FTA) |
| Common Software Fault | CCF in PCU software affecting all units | 1×10⁻¹⁰ /FH (target) |
| Common Hardware Fault | CCF in PCU hardware affecting all units | 1×10⁻¹⁰ /FH (target) |
| FC1+FC2 Loss | Both fuel cell systems fail | TBD |
| Battery Loss | Battery system fails | TBD |

### 4.3 Minimal Cut Sets

| MCS | Events | Order | Probability |
|-----|--------|-------|-------------|
| MCS-1 | P1 Fail AND P2 Fail AND P3 Fail AND P4 Fail | 4 | 1×10⁻¹⁶ |
| MCS-2 | Complete Power Loss | 1 | TBD |
| MCS-3 | Common Software Fault | 1 | 1×10⁻¹⁰ (target) |
| MCS-4 | Common Hardware Fault | 1 | 1×10⁻¹⁰ (target) |

### 4.4 Probability Calculation

**Target**: < 1×10⁻⁹ per flight hour

**Current estimate**:

P(TE-61-001) = P(MCS-1) + P(MCS-2) + P(MCS-3) + P(MCS-4)

= (1×10⁻⁴)⁴ + P(Power Loss) + 1×10⁻¹⁰ + 1×10⁻¹⁰

= 1×10⁻¹⁶ + TBD + 2×10⁻¹⁰

**Notes**:

- Independent propulsor failures (MCS-1) contribute negligibly
- Common cause failures (MCS-3, MCS-4) require mitigation to meet target
- Power loss contribution to be obtained from ATA 24 analysis

---

## 5. TE-61-002: Asymmetric Thrust — Uncontrollable

### 5.1 Fault Tree Structure

```
                    ┌─────────────────────────┐
                    │    TE-61-002            │
                    │ Uncontrollable          │
                    │ Asymmetric Thrust       │
                    └───────────┬─────────────┘
                                │
                           ╱────┴────╲
                          ╱    OR     ╲
                         ╱_____≥1_____╲
                    ┌────────┼────────┐
                    │        │        │
            ┌───────┴───┐ ┌──┴───┐ ┌──┴──────────┐
            │ G-61-010  │ │G-011 │ │   G-012     │
            │ Both Port │ │Both  │ │  Zonal      │
            │ Propulsor │ │Stbd  │ │  Event      │
            │ Fail + CTL│ │Fail  │ │  + CTL Fail │
            └─────┬─────┘ └──┬───┘ └──────┬──────┘
                  │          │            │
             ╱────┴────╲     │       ╱────┴────╲
            ╱   AND     ╲    │      ╱   AND     ╲
           ╱_____________╲   │     ╱_____________╲
               │     │       │         │      │
               │     │       │         │      │
            ┌──┴──┐  │       │      ┌──┴──┐   │
            │P1+P2│  ○       │      │Zone │   ○
            │Fail │ Control  │      │Event│ Control
            └──┬──┘ Limit    │      └──┬──┘ Limit
               │   Exceeded  │         │   Exceeded
          ╱────┴────╲        │         ○
         ╱   AND     ╲       │    Fire/Impact
        ╱_____________╲      │    affecting
            │     │          │    2+ propulsors
            ○     ○          │
           P1    P2          │
          Fail  Fail         │
                             │
                        [Similar structure
                         for G-011]
```

### 5.2 Event Descriptions

| Event ID | Description | Failure Rate/Probability |
|----------|-------------|-------------------------|
| P1 Fail | Propulsor 1 (Port) failure | 1×10⁻⁴ /FH |
| P2 Fail | Propulsor 2 (Port Inboard) failure | 1×10⁻⁴ /FH |
| P3 Fail | Propulsor 3 (Stbd Inboard) failure | 1×10⁻⁴ /FH |
| P4 Fail | Propulsor 4 (Starboard) failure | 1×10⁻⁴ /FH |
| Control Limit Exceeded | Asymmetric thrust exceeds control authority | Conditional |
| Zone Event | Fire, impact, or explosion affecting zone | TBD |

### 5.3 Probability Calculation

**Target**: < 1×10⁻⁷ per flight hour

**Notes**:

- Probability depends on control authority assumptions
- If N-2 controllability is achieved, this top event requires 3+ propulsor losses
- Zonal safety analysis required to quantify zone event probability

---

## 6. TE-61-003: Propulsor Overspeed (Uncontained)

### 6.1 Fault Tree Structure

```
                    ┌─────────────────────────┐
                    │    TE-61-003            │
                    │ Propulsor Overspeed     │
                    │    (Uncontained)        │
                    └───────────┬─────────────┘
                                │
                           ╱────┴────╲
                          ╱   AND     ╲
                         ╱_____________╲
                    ┌────────┴────────┐
                    │                 │
            ┌───────┴───────┐ ┌───────┴───────┐
            │  G-61-020     │ │   G-61-021    │
            │  Overspeed    │ │  Containment  │
            │  Occurs       │ │  Failure      │
            └───────┬───────┘ └───────┬───────┘
                    │                 │
               ╱────┴────╲            │
              ╱    OR     ╲           │
             ╱_____≥1_____╲           │
         ┌───────┼───────┐            │
         │       │       │            │
         ○       ○       ○            ○
      Control  Speed   Protection  Containment
       Loss   Sensor   System      Structural
              CCF     Failure      Failure
```

### 6.2 Event Descriptions

| Event ID | Description | Failure Rate/Probability |
|----------|-------------|-------------------------|
| Control Loss | Loss of motor control causing runaway | TBD |
| Speed Sensor CCF | Common cause failure of all 3 speed sensors | 1×10⁻⁸ (target) |
| Protection System Failure | Both HW and SW overspeed protection fail | TBD |
| Containment Structural Failure | Nacelle cannot contain released blade | 1×10⁻⁴ (design target) |

### 6.3 Probability Calculation

**Target**: < 1×10⁻⁷ per flight hour

P(TE-61-003) = P(Overspeed Occurs) × P(Containment Fails)

**Notes**:

- Overspeed protection targets: HW < 1×10⁻⁴, SW < 1×10⁻⁴
- Combined protection failure (AND): 1×10⁻⁸
- Containment design target: 1×10⁻⁴ at overspeed
- Result: 1×10⁻⁸ × 1×10⁻⁴ = 1×10⁻¹² (meets target)

---

## 7. Common Cause Failure Analysis

### 7.1 Beta Factor Method

For common cause failures between identical components:

| Component Type | Beta Factor | Basis |
|----------------|-------------|-------|
| Speed sensors (triplicated) | 0.1 | Industry standard |
| PCU channels (dual) | 0.05 | Dissimilar design assumed |
| Propulsor units (4×) | 0.01 | Physical separation |

### 7.2 Common Cause Defenses

| CCF Type | Defense | Effectiveness |
|----------|---------|--------------|
| Software CCF | Dissimilar software in channels | High |
| Hardware CCF | Different component suppliers | Medium |
| Design CCF | Independent design teams | Medium |
| Environmental CCF | Physical separation, different locations | High |
| Manufacturing CCF | Different manufacturing processes | Medium |

---

## 8. Sensitivity Analysis

### 8.1 Key Parameters

| Parameter | Baseline | +10× | -10× | Impact on TE-61-001 |
|-----------|----------|------|------|---------------------|
| Propulsor failure rate | 1×10⁻⁴ | 1×10⁻³ | 1×10⁻⁵ | Negligible (4th order) |
| CCF beta factor | 0.01 | 0.1 | 0.001 | Significant |
| Power loss rate | TBD | - | - | Potentially significant |

### 8.2 Uncertainty Assessment

| Source | Uncertainty Range | Mitigation |
|--------|-------------------|------------|
| Assumed failure rates | ±1 order of magnitude | Obtain supplier data |
| CCF modeling | Factor of 10 | Conservative beta factors used |
| Exposure time | Mission profile dependent | Use conservative profile |

---

## 9. Conclusions and Recommendations

### 9.1 Conclusions

1. **TE-61-001 (Loss of all thrust)**: Preliminary analysis indicates target of 1×10⁻⁹ is achievable with:
   - 4-propulsor architecture
   - Independent power sources
   - Common cause failure mitigations (dissimilar software, physical separation)

2. **TE-61-002 (Uncontrollable asymmetric thrust)**: Target of 1×10⁻⁷ achievable if:
   - N-2 controllability is designed
   - Zonal separation prevents multi-propulsor damage

3. **TE-61-003 (Uncontained overspeed)**: Target of 1×10⁻⁷ achievable with:
   - Dual independent overspeed protection
   - Robust containment design

### 9.2 Recommendations

1. Complete power system FTA (ATA 24) to quantify power loss contribution
2. Perform detailed CCF analysis using supplier data
3. Validate blade containment through testing
4. Conduct zonal safety analysis for multi-propulsor damage scenarios

---

## 10. References

### Internal References

- [61-00-02-SFHA-001 Propulsor System Hazards](../SFHA/61-00-02-SFHA-001_Propulsor_System_Hazards.md)
- [61-00-02-PSSA-001 Preliminary Safety Assessment](../PSSA/61-00-02-PSSA-001_Preliminary_Safety_Assessment.md)
- [61-00-02-CCA-001 Common Cause Analysis](../CCA/61-00-02-CCA-001_Common_Cause_Analysis.md)

### External Standards

- [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) — Guidelines and Methods for Conducting the Safety Assessment Process
- [NUREG-0492](https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr0492/) — Fault Tree Handbook (reference for FTA methodology)
- [IEC 61025](https://www.iso.org/standard/38041.html) — Fault Tree Analysis

---

## 11. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-03_.

---
