# 10-00-02-005-A — LH₂ Properties and Hazards

## 1. Purpose

This document describes the unique properties and hazards of liquid hydrogen (LH₂) relevant to ground operations at AMPEL360 facilities. It provides a common technical baseline for design, procedures, training, and emergency preparedness associated with LH₂ storage, transfer, conditioning, and fueling activities.

## 2. Scope

This document applies to all AMPEL360 ground operations where LH₂ is produced, delivered, stored, conditioned, transferred, or used as process/propulsion fuel, including but not limited to:

- Fixed LH₂ storage tanks and associated piping systems within AMPEL360-controlled areas.  
- Mobile LH₂ delivery units (road tankers, containerized modules) while on site.  
- LH₂ conditioning, pumping, and vaporization skids used to supply aircraft and test stands.  
- LH₂ lines, couplings, and interfaces to Ground Support Equipment (GSE) for BWB H₂ Hy-E aircraft.  
- Maintenance, inspection, and testing activities that may expose personnel to LH₂ or cold surfaces.  

The scope excludes detailed design specifications for individual components (handled in dedicated design documents) and site-specific emergency response plans (covered by local HSE documentation). However, it provides the technical hazard basis on which those documents must rely.

## 3. Overview

Liquid hydrogen is a cryogenic, flammable fluid with several characteristics that make it fundamentally different from conventional jet fuel:

- **Cryogenic temperature**: LH₂ boils at approximately −253 °C (20 K) at atmospheric pressure. Contact with uninsulated surfaces or small leaks can lead to severe cold burns, material embrittlement, and icing of ambient moisture.  
- **Low density / high expansion ratio**: LH₂ has a very low volumetric density; when vaporized, it expands by a factor of ~800. Even small quantities of liquid can generate large volumes of gas, creating over-pressure and confinement hazards.  
- **Wide flammability range**: Gaseous hydrogen has a very wide flammability range in air (approximately 4–75 % by volume) and a low minimum ignition energy, making it easy to ignite in the presence of leaks and ignition sources.  
- **Buoyancy and dispersion**: Once released and warmed, hydrogen gas becomes highly buoyant and tends to rise rapidly. However, in partially confined or low-ventilation areas, it can accumulate under roofs or canopies and form flammable pockets.  
- **Invisible flames**: Hydrogen flames can be nearly invisible in daylight, complicating detection and response. Personnel may not perceive a flame without dedicated detection equipment or thermal cues.  

In addition, LH₂ operations introduce secondary hazards such as oxygen enrichment (due to preferential condensation of nitrogen), pressure surges during rapid warm-up, and mechanical stresses on materials exposed to repeated cryogenic cycles. These effects must be considered in system design, procedural controls, and training.

## 4. Requirements

At a minimum, LH₂ ground operations within AMPEL360 shall comply with the following high-level requirements:

- **Design and containment**  
  - LH₂ storage and transfer systems shall provide double containment or equivalent protection for credible leak scenarios.  
  - Materials, gaskets, and valves in contact with LH₂ shall be qualified for cryogenic hydrogen service and documented accordingly.  

- **Detection, ventilation, and zoning**  
  - Hydrogen leak detection (fixed and/or portable) shall be installed in areas where hydrogen can accumulate, as defined by the facility hazardous area classification.  
  - Ventilation (natural and/or forced) shall be demonstrated adequate to prevent persistent flammable mixtures under normal operation.  
  - Hazardous zones around LH₂ equipment shall be defined and marked, with equipment selection aligned to the zone classification.  

- **Procedural and administrative controls**  
  - Written operating procedures shall be available, controlled, and maintained for normal, abnormal, and emergency LH₂ operations.  
  - Permit-to-work systems shall be applied for hot work, confined space activities, and intrusive maintenance near LH₂ installations.  

- **Safety instrumentation and interlocks**  
  - Critical parameters (pressure, temperature, flow, level) shall be monitored with alarms and trip functions where required by the risk assessment.  
  - Interlocks and emergency shutdown functions shall be designed to fail-safe and be periodically tested.  

- **Training and qualification**  
  - Personnel involved in LH₂ operations shall receive role-specific training (see Section 7) and be formally authorized before performing tasks independently.  

Compliance with these requirements shall be verified through design reviews, HAZOP/FMEA/Fault Tree analyses, commissioning tests, and periodic audits.

## 5. Procedures

The following procedural principles apply to LH₂ ground operations; detailed step-by-step instructions are provided in the relevant Operating Procedures:

- **Pre-operation checks**  
  - Verify system integrity, completion of maintenance, and status of permits before introducing LH₂.  
  - Confirm readiness of detection, communication, and emergency shutdown systems.  

- **Normal operations**  
  - Follow defined sequences for cool-down, pressurization, transfer, and isolation to minimize thermal shock and pressure transients.  
  - Monitor key process parameters continuously; operate within defined envelopes for pressure, temperature, and flow.  
  - Maintain clear communication between control room, field operators, and external parties (e.g., tanker drivers, aircraft crew).  

- **Abnormal conditions**  
  - In case of alarms (leak detection, over-pressure, abnormal temperature), follow predefined response trees: stabilize if safe, otherwise execute controlled shutdown.  
  - Escalate promptly to supervision and HSE when the situation deviates from expected behaviour or when multiple alarms are active.  

- **Emergency response**  
  - In the event of confirmed LH₂ leak, fire, or explosion risk, prioritize life safety: raise alarms, evacuate affected zones, and secure ignition sources.  
  - Activate emergency shutdown systems as per procedure; do not attempt to operate valves directly in hazardous atmospheres.  
  - Coordinate with site emergency services and external responders following the site-specific Emergency Response Plan.  

- **Post-event recovery**  
  - After any significant incident, maintain isolation until engineering assessment confirms structural and functional integrity.  
  - Record the event, perform root cause analysis, and implement corrective/preventive actions before resuming normal operations.  

## 6. Responsibilities

The allocation of responsibilities for LH₂ properties and hazards within AMPEL360 ground operations shall, as a minimum, reflect the following structure:

- **LH₂ Operations Supervisor**  
  - Owns the safe execution of LH₂ operations in the assigned area.  
  - Ensures procedures are available, up to date, and followed.  
  - Verifies that personnel are trained and authorized for their tasks.  

- **GSE / Field Operators**  
  - Execute LH₂ operations in accordance with approved procedures and permits.  
  - Perform pre-use inspections and report anomalies immediately.  
  - Stop work and escalate if conditions become unsafe or unclear.  

- **Maintenance Team**  
  - Plan and execute preventive and corrective maintenance on LH₂ equipment.  
  - Verify correct re-instatement of systems after maintenance and update records.  
  - Coordinate with Operations for functional tests involving LH₂.  

- **Safety / HSE Function**  
  - Maintain and update the LH₂ hazard register and supporting risk assessments.  
  - Define training requirements and support delivery of safety training.  
  - Monitor compliance, perform inspections/audits, and manage incident learning.  

- **Engineering / Design Authority**  
  - Ensure that design changes affecting LH₂ systems are reviewed and approved.  
  - Maintain configuration control of P&IDs, layout drawings, and safety studies.  

Specific RACI allocations may be detailed in separate organizational documents; this section provides the minimum role definition for this document.

## 7. Training Requirements

The following training requirements apply to personnel involved in LH₂ ground operations:

- **Core hydrogen safety training (all personnel accessing LH₂ areas)**  
  - Basic hydrogen properties and differences vs. conventional fuels.  
  - Recognition of LH₂/cryogenic hazards, hydrogen leaks, and invisible flames.  
  - Site-specific alarms, signage, and evacuation routes.  

- **Role-specific technical training (operators and maintenance)**  
  - Detailed understanding of the LH₂ system configuration (storage, transfer, conditioning).  
  - Normal operating procedures, limits, and alarms.  
  - Use of PPE, gas detectors, and communication tools.  
  - Safe maintenance practices on cryogenic and pressurized equipment.  

- **Emergency response and drills (operations, maintenance, HSE, security)**  
  - Response to LH₂ leaks, fires, and loss-of-containment scenarios.  
  - Use of emergency shutdown systems and coordination with emergency services.  
  - Participation in periodic drills and exercises, including debrief and lessons learned.  

- **Refresher training and re-authorization**  
  - Minimum periodic refresher (e.g. every 24 months) or after significant system modifications or incidents.  
  - Documented assessment of competence before (re)authorization.

## 8. Cross-References

This document shall be read in conjunction with, at least, the following:

- 10-00-02-001-A — Hydrogen Safety Fundamentals (Ground Operations)  
- 10-00-02-010-A — LH₂ Storage and Transfer System Description  
- 10-00-02-020-A — LH₂ Operating Procedures (Normal and Abnormal)  
- 10-00-02-030-A — LH₂ Emergency Response Plan (Ground Facilities)  
- 03-10-00-XXX — GSE Operations Manual (Hydrogen Ground Support Equipment)  
- 85-30-00-XXX — Circular Infrastructure: Hydrogen and Carbon Loop Interfaces  

Applicable external standards and regulations are referenced in the hydrogen safety normative index (see 10-00-00-XXX).

## 9. Document Control

| Attribute      | Value                                        |
|----------------|----------------------------------------------|
| Document ID    | 10-00-02-005-A                               |
| Version        | 1.0                                          |
| Status         | 🔄 Draft — Preliminary Design                |
| Classification | AMPEL360 Internal                            |
| Owner          | Safety Engineering                           |
| Last Updated   | 2025-12-09                                   |
| Next Review    | 2026-03-09                                   |

Generated with the assistance of AI (GitHub Copilot / CGen), prompted by Amedeo Pelliccia.
