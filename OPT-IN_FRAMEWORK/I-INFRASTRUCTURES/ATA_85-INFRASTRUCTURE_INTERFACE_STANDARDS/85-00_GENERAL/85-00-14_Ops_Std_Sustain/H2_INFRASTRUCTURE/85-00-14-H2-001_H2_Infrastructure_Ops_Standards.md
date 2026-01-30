# 85-00-14-H2-001 — H₂ Infrastructure Ops Standards

## 1. Purpose

This document defines the **operational standards and standard operating procedures (SOPs)** for **hydrogen (H₂) infrastructure interfaces** supporting AMPEL360 BWB H₂ Hy-E aircraft operations.

It provides detailed procedures for H₂ refuelling, safety protocols, and coordination with ground operations.

---

## 2. Scope

### 2.1 H₂ Operations Covered

- **Ground H₂ refuelling** — 350 bar and 700 bar systems
- **H₂ storage and distribution** — Airport-side infrastructure
- **Safety systems** — Leak detection, automatic shutoff, fire suppression
- **Emergency response** — H₂ leak and fire scenarios
- **Personnel training** — Certification and competency requirements

### 2.2 Applicable Interfaces

- H₂ refuelling connectors (aircraft-side and ground-side)
- H₂ storage tanks and distribution pipelines
- Safety monitoring and control systems
- Communication systems (ground crew ↔ flight crew ↔ H₂ facility)

---

## 3. H₂ Refuelling Standard Operating Procedure

### 3.1 Pre-Refuelling Checks

#### Aircraft Side
- **H₂ system status**: Verify aircraft H₂ tanks depressurized and ready for refuelling
- **Tank temperature**: Within acceptable range for H₂ loading
- **Vent system**: Operational and clear
- **Aircraft power**: APU or ground power available for monitoring systems
- **Flight crew notification**: Crew aware of refuelling operation

#### Ground Infrastructure Side
- **H₂ supply**: Available and pressure verified (350 or 700 bar as required)
- **Refuelling equipment**: Inspected, no visible damage, certified for use
- **Leak detectors**: Functional and calibrated
- **Safety perimeter**: Established per [ISO/TR 15916](https://www.iso.org/standard/29316.html)
- **Weather conditions**: Wind speed/direction acceptable, no lightning within 10 km
- **Communication**: Ground crew ↔ flight crew ↔ H₂ facility control

### 3.2 Connection Sequence

1. **Safety Briefing** — All personnel review emergency procedures
2. **Equipment Positioning** — H₂ refuelling vehicle/unit positioned at designated location
3. **Bonding and Grounding** — Establish electrical bonding before connector mating
4. **Visual Inspection** — Inspect connector, hose, and aircraft interface for damage
5. **Connector Mating** — Connect H₂ coupler per [ISO 13985](https://www.iso.org/standard/54560.html) interface standard
6. **Verification** — Confirm secure connection (visual and sensor feedback)
7. **Leak Check** — Pressurize with N₂, confirm no leaks (H₂ sensors)
8. **System Activation** — Enable H₂ flow control, confirm readiness

### 3.3 Refuelling Process

1. **Initiate H₂ Flow** — Start refuelling sequence per automated protocol
2. **Monitor Flow Rate** — Target rate: 60-80 kg H₂/min (depending on system capacity)
3. **Pressure Management** — Ramp pressure to target (350 or 700 bar)
4. **Temperature Monitoring** — Ensure tank temperature within limits (avoid overheating)
5. **Continuous Leak Monitoring** — H₂ sensors active throughout operation
6. **Flow Termination** — Automatic stop at target mass or manual stop if needed
7. **Pressure Equalization** — Allow system to stabilize

Typical refuelling time: **10-15 minutes** for 1,000 kg H₂ (see KPI-010 in [85-00-14-003](../85-00-14-003_Service_Levels_and_KPIs.md))

### 3.4 Disconnection Sequence

1. **H₂ Flow Stop** — Confirm flow terminated
2. **Depressurization** — Safely vent hose pressure (to atmosphere or recovery system)
3. **Leak Verification** — Final H₂ sensor check around connector
4. **Connector Unmating** — Disconnect coupler per standard procedure
5. **Post-Disconnect Inspection** — Check for leaks, damage, or ice formation
6. **Equipment Stowage** — Return refuelling equipment to safe storage
7. **Documentation** — Log refuelling operation (mass loaded, time, any anomalies)
8. **Flight Crew Notification** — Confirm refuelling complete, aircraft ready

### 3.5 Post-Refuelling Checks

- **Aircraft H₂ tank status**: Pressure and mass verified via aircraft systems
- **No leaks detected**: H₂ sensors confirm no residual leaks
- **Safety perimeter clear**: Personnel and equipment clear of aircraft
- **Documentation complete**: Refuelling log signed off by ground crew and flight crew

---

## 4. Safety Protocols

### 4.1 Safety Perimeters

#### Hot Zone (0-3 meters from H₂ connection point)
- **Access**: Only essential personnel in flame-resistant PPE
- **No ignition sources**: No electronics, no smoking, no hot work
- **Continuous monitoring**: H₂ sensors, visual observation

#### Warm Zone (3-10 meters)
- **Limited access**: Support personnel only
- **PPE required**: Safety glasses, flame-resistant clothing
- **Emergency equipment**: Fire extinguishers, emergency shutoff stations

#### Cold Zone (>10 meters)
- **Unrestricted access**: Standard airport operations
- **Awareness**: Personnel briefed on H₂ operations and alarms

Reference: [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) Hydrogen Technologies Code

### 4.2 Leak Detection and Response

#### Detection Layers
1. **Sensor network**: Distributed H₂ sensors (catalytic, electrochemical, optical)
2. **Alarm thresholds**: 
   - 25% LEL (Lower Explosive Limit) → **Caution** (investigate)
   - 50% LEL → **Warning** (prepare to evacuate)
   - 75% LEL → **Danger** (immediate evacuation and shutoff)
3. **Visual/auditory**: Hissing sound, visible gas dispersion

#### Response Actions
- **Isolate H₂ source**: Automatic or manual shutoff at source and aircraft interface
- **Evacuate personnel**: Clear hot and warm zones immediately
- **Notify emergency services**: Airport fire and rescue on standby
- **Monitor dispersion**: H₂ disperses rapidly upward (lighter than air)
- **Investigate after safe**: Determine leak source and corrective actions
- **No re-entry until clear**: H₂ levels < 25% LEL confirmed

### 4.3 Fire Response

#### H₂ Fire Characteristics
- **Nearly invisible flame**: Difficult to see in daylight
- **Detection**: Thermal imaging, flame detectors
- **Approach**: Extreme caution, assume fire present if H₂ leak confirmed

#### Fire Response Procedure
1. **Immediate notification**: Activate airport emergency response
2. **Do NOT extinguish** if H₂ source not isolated (risk of vapor cloud explosion)
3. **Isolate H₂ source**: Shut off flow at source if safe to approach
4. **Cool surroundings**: Apply water spray to adjacent structures and aircraft
5. **Let burn in controlled manner**: If source isolated, allow remaining H₂ to burn off
6. **Extinguish only after**: H₂ source confirmed isolated
7. **Post-fire inspection**: Comprehensive damage assessment before resuming operations

Reference: [ISO/TR 15916](https://www.iso.org/standard/29316.html) Section on H₂ fire response

---

## 5. Training and Competency

### 5.1 Personnel Qualifications

#### Ground Crew (H₂ Refuelling Technicians)
- **Initial training**: 40 hours classroom + 20 hours hands-on
- **Topics**: H₂ properties, safety, refuelling procedures, emergency response
- **Certification**: Written exam (≥ 80%) and practical assessment
- **Recurrent training**: Annual refresher (8 hours) plus competency check

#### H₂ Facility Operators
- **Initial training**: 60 hours including H₂ systems, safety, operations
- **Certification**: National/international H₂ safety certification
- **Recurrent training**: Annual refresher plus incident scenario drills

#### Flight Crew
- **Awareness training**: H₂ system basics, refuelling coordination, emergencies
- **Duration**: 4 hours as part of aircraft type rating
- **Recurrent**: Included in annual flight crew training

### 5.2 Training Materials

Available in `ASSETS/` folder (to be developed):
- Classroom training slides and manuals
- Hands-on training procedures
- E-learning modules
- Emergency scenario simulations

See [85-00-14-007_Knowledge_Management](../85-00-14-007_Knowledge_Management_and_Lessons_Learned.md) for training content development.

---

## 6. Coordination and Communication

### 6.1 Pre-Arrival Coordination

- **30 minutes before arrival**: Airport ops confirms H₂ infrastructure ready
- **Flight crew notification**: H₂ refuelling planned, aircraft systems configured
- **Weather check**: Conditions acceptable for H₂ operations

### 6.2 During Refuelling

- **Continuous communication**: Ground crew ↔ flight crew via intercom/radio
- **Status updates**: Refuelling progress, any anomalies
- **Emergency communication**: Direct line to airport emergency services

### 6.3 Post-Refuelling

- **Completion confirmation**: Ground crew → flight crew (mass loaded, ready)
- **Aircraft systems check**: Flight crew verifies H₂ tank status
- **Documentation**: Refuelling log completed and filed

---

## 7. Equipment Maintenance and Inspection

### 7.1 Daily Inspections

Before each operational period:
- **Visual inspection**: Hoses, connectors, fittings for damage
- **Leak check**: Pressurize system with N₂, verify no leaks
- **Sensor check**: H₂ sensors functional and calibrated
- **Communication check**: Radio and intercom systems operational

### 7.2 Periodic Maintenance

- **Weekly**: Detailed inspection of refuelling equipment, sensor calibration
- **Monthly**: H₂ system pressure test, valve and seal inspection
- **Quarterly**: Full system audit, safety equipment certification
- **Annually**: Major overhaul, replacement of wear items per manufacturer schedule

See [85-00-14-H2-002_H2_Infrastructure_Sustainment_Plan](./85-00-14-H2-002_H2_Infrastructure_Sustainment_Plan.md).

---

## 8. Integration with Service Levels and KPIs

H₂ operations monitored per [85-00-14-003_Service_Levels_and_KPIs](../85-00-14-003_Service_Levels_and_KPIs.md):

- **KPI-002**: H₂ Refuelling System Uptime (target ≥ 99.0%)
- **KPI-010**: H₂ Refuelling Time (target ≤ 15 minutes)
- **KPI-020**: Interface-Related Safety Incidents (target zero per 10,000 ops)
- **KPI-021**: H₂ Leak Detection Response Time (target ≤ 30 seconds automated)
- **KPI-031**: H₂ Transfer Efficiency (target ≥ 98%, ≤ 2% loss)

---

## 9. Related Documentation

### Internal ATA 85 References

- [85-00-03_Requirements/85-00-03-H2](../../85-00-03_Requirements/85-00-03-H2_Hydrogen_Refuelling_Infrastructure) — H₂ requirements
- [85-00-02_Safety](../../85-00-02_Safety) — H₂ safety assessments
- [85-00-14_Ops_Std_Sustain Parent](../) — Global operational standards
- [85-00-14-H2-002](./85-00-14-H2-002_H2_Infrastructure_Sustainment_Plan.md) — H₂ sustainment plan

### External Standards

- [ISO 13985](https://www.iso.org/standard/54560.html) — Liquid hydrogen fuelling interface
- [ISO/TR 15916](https://www.iso.org/standard/29316.html) — H₂ system safety
- [SAE J2601](https://www.sae.org/standards/content/j2601_201612/) — H₂ fuelling protocols
- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) — Hydrogen Technologies Code

---

## 10. Status

- **Phase**: H₂ Ops Standards Development (A-LIVE-GP Stage 14)
- **Maturity**: `DRAFT` — To be validated with ground operations trials
- **Last Updated**: 2025-11-21

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---

**End of Document**
