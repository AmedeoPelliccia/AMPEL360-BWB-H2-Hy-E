# 02-20-16 — Dispatch System Integration

**Subsystem ID:** 02-20-16_Dispatch_System_Integration  
**Parent Group:** [02-20-00 SYSTEMS](../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / WORKING  
**Owner:** Digital Operations & OCC / Dispatch Domain  

---

## 1. Purpose

02-20-16 defines how the **AMPEL360 CAOS (Computer Aided Operations & Services)** layer integrates with external airline systems. It serves as the interoperability bridge between the "Digital Twin" of the aircraft and the airline's **Dispatch / OCC (Operations Control Center)** environment.

The objective is to provide a **coherent, traceable, human-in-the-loop decision hub** where:

1.  **Ground Reality:** Turnaround status, GSE availability, and H₂ safety constraints (from 02-20-14).
2.  **Flight Commitments:** EOBT, CTOT, and Slot constraints (from 02-20-15).
3.  **Predictive Intelligence:** Risk assessments and optimization strategies (from 02-40-50).

These inputs are aggregated and exposed to dispatchers, enabling them to make informed decisions that are immediately reflected back into the aircraft's operational plan.

---

## 2. Scope

### 2.1 Included
*   **Logical Integration:** Definition of APIs and event schemas to push CAOS data to flight planning systems (e.g., LIDO, Sabre, Jeppesen).
*   **Dispatch Abstractions:** High-level status flags (e.g., `H2_REFUEL_CRITICAL`, `SLOT_RISK_HIGH`) rather than raw sensor data.
*   **Decision Workflows:** Protocols for how a dispatcher "Accepts," "Rejects," or "Modifies" a CAOS-generated optimization proposal.
*   **Irregular Operations (IROPS):** Handling logic for non-standard events (tail swaps, H₂ venting delays, divert planning).

### 2.2 Excluded
*   **UI/UX Design:** The actual graphical interface of the airline's OCC software is out of scope.
*   **Commercial Policy:** Rules regarding passenger re-accommodation or route profitability.
*   **Internal Physics:** The calculation of H₂ boil-off happens in *ATA 28*; this module only reports the *result* to Dispatch.

---

## 3. Position in CAOS & Relationships

This subsystem acts as the "Neck," connecting the "Body" (Aircraft Operations) to the "Head" (Strategic Decision Making).

### Upstream Inputs (Data Sources)
*   **[02-20-14 Ground Ops Management](../02-20-14_GROUND_OPS_MANAGEMENT/):** Real-time turnaround progress and physical constraints.
*   **[02-20-15 Flight Planning Integration](../02-20-15_FLIGHT_PLANNING_INTEGRATION/):** Slot windows, airway restrictions, and filed flight plans.
*   **[02-40-50 Predictive Analytics](../../02-40-00_PROGRAMMING_ALGORITHMS/02-40-50_PREDICTIVE_ANALYTICS/):** Probabilistic risk scores (e.g., "85% chance of exceeding H₂ loading time").

### Downstream Outputs (Actions)
*   **Decision Tickets:** Confirmed actions (e.g., "Dispatcher approved new TOBT").
*   **Parameter Updates:** New weights (ZFW/TOW) sent to the onboard FMS/WBS.
*   **Audit Logs:** Immutable records of human decisions for ATA 95 traceability.

---

## 4. Subsystem Responsibilities

1.  **Flight View Aggregation**
    *   Create a "Single Pane of Glass" logic that synchronizes the aircraft's internal state with the airline's schedule.
2.  **Dynamic Dispatch Envelope**
    *   Calculate the unique **Mass-Energy-Emission** envelope for H₂ operations (managing the trade-off between Fuel Burn and CO₂ Capture weight).
3.  **Action Translation**
    *   Translate high-level Dispatch commands (e.g., "Prioritize Cargo") into specific system parameters (e.g., "Limit CO₂ Capture to 80% capacity").
4.  **Traceability & Governance**
    *   Ensure every dispatch decision that overrides a safety or efficiency recommendation is logged for **ATA 95 Digital Product Passport** compliance.

---

## 5. Document Map

| Document ID | Title | Description |
|:---|:---|:---|
| **02-20-16-001** | [Dispatch Integration Overview](02-20-16-001_Dispatch_Integration_Overview.md) | High-level architecture and the "Dynamic Mass" dispatch challenge. |
| **02-20-16-002** | Dispatch Use Cases & Workflows | Swimlane diagrams for Standard Ops and IROPS. |
| **02-20-16-003** | CAOS Dispatch Interfaces | API contracts (JSON/XML schemas) for Airline Systems. |
| **02-20-16-004** | Irregular Operations Handling | Logic for tail swaps, venting delays, and divert management. |
| **02-20-16-005** | Predictive Decision Support | Guidelines for presenting AI confidence intervals to dispatchers. |

---

## 6. Integration with Test Data & Machine Learning

02-20-16 plays a critical role in the **Reinforcement Learning (RL)** loop for the CAOS AI:

*   **Data Labeling:** When a dispatcher accepts or rejects a CAOS recommendation, that decision is recorded.
*   **Feedback Loop:** 
    *   *Scenario:* CAOS predicts a delay. Dispatcher ignores it. Delay occurs.
    *   *Outcome:* The system "learns" the prediction was correct, and the human override was the error source (or vice versa).
*   **Artifacts:** This subsystem produces the `DISPATCH_DECISION_LOG` datasets used to retrain the models in 02-40-50.

---

## 7. Document Control

> **Originator:** CAOS Architecture Team  
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework  
> **Revision:** 1.1  
> **Last Updated:** 2025-11-21
