# 02-20-16 — Dispatch System Integration

**Subsystem ID:** 02-20-16_Dispatch_System_Integration  
**Parent Group:** 02-20 Turnaround & Ground Ops Coordination *(TBD doc link)*  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / WORKING  
**Owner:** Digital Operations & OCC / Dispatch Domain  

---

## 1. Purpose

02-20-16 defines how the **AMPEL360 CAOS layer** integrates with:

- Airline **Dispatch / OCC systems** (flight watch, control, irregular ops handling)  
- The **02-20-14 Ground Ops Management** subsystem (turnaround, GSE, H₂ constraints)  
- The **02-20-15 Flight Planning Integration** subsystem (FPL, ATFM/slots, TOBT/EOBT)  
- The **Predictive Ops NN (02-20-23)** decision-support services  

The objective is to provide a **coherent, traceable, human-in-the-loop decision hub** where:

- Ground reality (turnaround, GSE, H₂ safety constraints)  
- Flight plan and slot commitments (EOBT, CTOT, TSAT)  
- Predictive risk assessments and recommendations  

are aggregated and exposed to **dispatchers and OCC operators** through well-defined CAOS interfaces and workflows.

02-20-16 focuses on the **Dispatch-side integration**, not on the internal design of OCC tools or NN models.

---

## 2. Scope

### 2.1 Included

- Logical integration between CAOS and **Dispatch / OCC platforms**, including:

  - Consumption of events from 02-20-14 and 02-20-15  
  - Consolidation of ground / FPL / ATFM / predictive signals into **dispatch views**  
  - Interfaces to push **operational decisions** back into CAOS (e.g. accept/reject TOBT proposals, re-slotting requests, prioritisation instructions)

- Definition of **Dispatch-facing abstractions**, such as:

  - Flight-level **operational status** (plan vs actual vs risk)  
  - **Decision tickets / action items** triggered by events and predictive alerts  
  - **Irregular Operations (IROPS)** patterns (e.g. missed slot, extended H₂ fueling, tail swap) at the integration level  

- **Human-in-the-loop** workflows, including:

  - How dispatchers review and approve **FPI.TOBT_PROPOSAL** and re-slot advisories  
  - How OCC acknowledges and documents **FPI.SLOT_RISK_ALERT** and Predictive Ops recommendations  
  - Logging of decisions for **traceability, training data, and post-event analysis**  

### 2.2 Excluded

- Detailed UI/UX design of airline OCC tools or dashboards  
- Airline-specific **business policies** (e.g. commercial rules for cancelling/maintaining flights, passenger re-accommodation logic)  
- Internal algorithms of third-party dispatch systems or crew rostering solutions  
- NN model internals, certification and governance (handled under ATA 95 / 02-20-23)  

---

## 3. Position in CAOS & Relationships

02-20-16 sits at the intersection between **CAOS integration** and **airline operational control**:

- **Upstream / Inputs:**

  - 02-20-14 Ground Ops Management  
    - Turnaround phases, task progress, GSE/H₂ constraints, disruptions  
  - 02-20-15 Flight Planning Integration  
    - FPL plan snapshots, schedule/slot changes, TOBT/EOBT proposals  
    - Slot/ATFM integration (CTOT/TSAT windows, feasibility)  
  - Predictive Ops NN (02-20-23)  
    - Risk scores (`p_departure_delay_X`, `p_slot_infringement`)  
    - Recommended buffers, stand/GSE strategies, escalation hints  

- **Downstream / Outputs:**

  - **Decision confirmations** and instructions back into CAOS, e.g.:  
    - Accept / modify / reject **TOBT/EOBT proposals**  
    - Confirm **mitigation actions** (prioritise H₂ fueling, re-slot, change stand)  
    - Trigger IROPS workflows (e.g. “protect this connection”, “re-time departure”)  
  - **Audit trail** of dispatch decisions and rationale for:  
    - Post-event operational reviews  
    - Predictive model training/validation  

02-20-16 is therefore the **OCC/Dispatch integration layer** of 02-20 and must align tightly with:

- [../02-20-14_Ground_Ops_Management/](../02-20-14_Ground_Ops_Management/README.md)  
- [../02-20-15_Flight_Planning_Integration/](../02-20-15_Flight_Planning_Integration/README.md)  
- Future 02-20-23 Predictive Ops NN subtree (ATA 95 compliant)  

---

## 4. Subsystem Responsibilities

02-20-16 is responsible for:

1. **Dispatch-Centric Flight View Aggregation**

   - Build a flight-centric “single pane of glass” from:

     - Ground state (turnaround / GSE / H₂ constraints)  
     - FPL / slot state (EOBT/TOBT, CTOT/TSAT, regulations)  
     - Predictive risk and recommendations  

   - Provide a stable **integration contract** to OCC tools, independent of internal CAOS structures.

2. **Decision & Action Integration**

   - Capture dispatcher/OCC actions related to:

     - Accepting / modifying TOBT/EOBT and slot strategy  
     - Prioritising flights or ground resources  
     - Triggering flight cancellations/diversions at integration level  

   - Translate these decisions into:

     - Events and payloads usable by 02-20-14 / 02-20-15  
     - Traceable records for 02-20-23 training and governance.

3. **Irregular Operations (IROPS) Integration Patterns**

   - Define IROPS patterns at the integration level, e.g.:

     - Threatened slot / high delay risk event  
     - Turnaround infeasibility due to H₂ or GSE constraints  
     - Tail swap / aircraft change impacting ground configuration  

   - Specify how such patterns are **exposed to Dispatch** and how resulting actions flow back into CAOS.

4. **Traceability & NN Governance Hooks**

   - Maintain identifiers linking:

     - Predictive inputs/outputs  
     - Dispatch decisions  
     - Resulting operational outcomes  

   - Support ATA 95 traceability by ensuring **decision trails** are recoverable.

---

## 5. Document Map

Planned / existing documents under this subsystem:

- **Overview & Responsibilities**

  - `02-20-16-001_Dispatch_Integration_Overview.md`  
    - High-level concept of Dispatch System Integration within CAOS.  
    - Relationships to 02-20-14, 02-20-15, 02-20-23 and external OCC systems.  

- **Use Cases & Workflows**

  - `02-20-16-002_Dispatch_Use_Cases_and_Workflows.md`  
    - Canonical scenarios: slot at risk, H₂ fueling conflict, GSE shortage, tail swap, cancellation.  
    - Swimlane diagrams (Ground Ops, FPL, OCC, NN).  

- **Interfaces & Payloads**

  - `02-20-16-003_CAOS_Dispatch_Interfaces.md`  
    - Logical data contracts for Dispatch-facing APIs/events.  
    - Decision ticket structures, acknowledgements, audit records.  

- **Irregular Operations Handling**

  - `02-20-16-004_Irregular_Operations_Handling.md`  
    - Integration patterns for IROPS flows through CAOS to Dispatch and back.  
    - Link to test data for disruption scenarios.  

- **Predictive Decision Support**

  - `02-20-16-005_Predictive_Decision_Support_in_Dispatch.md`  
    - How Predictive Ops NN outputs are rendered and actioned in OCC.  
    - Rules for using vs ignoring NN outputs, escalation thresholds.  

- **Architecture & Assets**

  - `02-20-16-A-001_Dispatch_Integration_Architecture.md`  
    - Logical/physical views of Dispatch integration within CAOS.  
  - `ASSETS/02-20-16-A-001_Dispatch_Integration_Architecture.svg` *(planned)*  

- **Test Data & RTM (future)**

  - `TEST_DATA/02-20-16-T-001_Dispatch_IROPS_Scenarios.json`  
  - `02-20-16-A-501_Requirements_Traceability.md`  

---

## 6. Integration with Test Data & Predictive Ops

02-20-16 does not directly define predictive models but:

- **Consumes**:

  - Predictive risk and recommendations produced per-flight by 02-20-23 (via 02-20-15 hooks).  

- **Produces**:

  - Rich, labelled **decision and outcome logs** (e.g. “OCC accepted NN suggestion and protected slot; delay reduced from predicted 30+ to 10 min”).  

These artefacts are intended to:

- Complement 02-20-14 and 02-20-15 `TEST_DATA` sets (turnaround, allocation, FPL/slot scenarios).  
- Provide realistic **dispatch-centric labels** for evaluation of Predictive Ops NN in operational context.  

---

## 7. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia  
> **Subsystem:** 02-20-16 Dispatch System Integration  
> **Asset:** Subsystem README  
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework  

| Version | Date       | Author / Team                             | Notes                                             |
| ------- | ---------- | ----------------------------------------- | ------------------------------------------------- |
| 0.1.0   | 2025-11-21 | AMPEL360 Digital Ops & OCC / Dispatch WG | Initial subsystem skeleton and integration intent |
```
