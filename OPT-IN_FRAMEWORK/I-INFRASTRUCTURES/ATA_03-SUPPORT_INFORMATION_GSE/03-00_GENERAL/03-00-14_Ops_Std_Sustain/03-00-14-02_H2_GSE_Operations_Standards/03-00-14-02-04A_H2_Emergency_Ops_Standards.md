---
Title: "H2 Emergency Operations Standards"
Identifier: "AMPEL360-03-00-14-02-04A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Emergency Response Team"
ResponsibleOrg: "I-INFRASTRUCTURES H2 Emergency Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Emergency response procedures for hydrogen incidents in ground operations."
Keywords: ["ATA 03","GSE","H2","Hydrogen","Emergency","Response","Safety","Incident"]
Compliance:
  - "NFPA 2"
  - "ISO 19880-8"
  - "ICAO Annex 14"
  - "ATA iSpec 2200"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentGeneral: "../../"
  Siblings:
    - "./03-00-14-02-01A_LH2_Fueling_Ops_Standards.md"
    - "./03-00-14-02-02A_Cryogenic_Ops_Standards.md"
    - "./03-00-14-02-03A_H2_Safety_Ops_Standards.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Emergency Team", change: "Initial release" }
---

# 03-00-14-02-04A — H2 Emergency Operations Standards

## 1. Purpose

This document establishes **emergency response procedures and standards** for hydrogen-related incidents during AMPEL360 aircraft ground operations. It defines emergency scenarios, response protocols, roles and responsibilities, and coordination requirements to ensure rapid, effective, and safe emergency response to hydrogen incidents.

## 2. Scope

### 2.1 Coverage

Emergency response standards for:

1. **H₂ Leak Scenarios**
   - Small leaks (<1 kg/s)
   - Large leaks (>1 kg/s)
   - Liquid H₂ spills
   - Gaseous H₂ releases

2. **H₂ Fire Scenarios**
   - Small H₂ fires (controllable)
   - Large H₂ fires (uncontrollable)
   - Aircraft-involved H₂ fires
   - Equipment fires with H₂ present

3. **Personnel Emergencies**
   - Cryogenic burns and frostbite
   - H₂ inhalation/asphyxiation
   - Personnel trapped in H₂ hazard area
   - Mass casualty scenarios

4. **Emergency Coordination**
   - Internal emergency response
   - Fire department coordination
   - Airport emergency services
   - Regulatory notification

## 3. Applicable Documents

### 3.1 Emergency Response Standards

| Standard | Title | Application |
|----------|-------|-------------|
| **[NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2)** | Hydrogen Technologies Code | Emergency procedures |
| **[ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx)** | Aerodromes | Airport emergency planning |
| **[NFPA 403](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=403)** | Standard for Aircraft Rescue and Fire-Fighting Services | Aircraft fire response |
| **[ISO 19880-8](https://www.iso.org/standard/71940.html)** | Gaseous Hydrogen — Fueling Stations | Emergency shutdown |

### 3.2 Internal References

- [03-00-14-02-01A_LH2_Fueling_Ops_Standards.md](./03-00-14-02-01A_LH2_Fueling_Ops_Standards.md)
- [03-00-14-02-02A_Cryogenic_Ops_Standards.md](./03-00-14-02-02A_Cryogenic_Ops_Standards.md)
- [03-00-14-02-03A_H2_Safety_Ops_Standards.md](./03-00-14-02-03A_H2_Safety_Ops_Standards.md)
- [03-00-02_Safety](../../03-00-02_Safety/)

## 4. Operations/Sustainment Requirements

### 4.1 Emergency Classification

#### 4.1.1 Emergency Levels

| Level | Description | Response | Notification |
|-------|-------------|----------|--------------|
| **Level 1 — Minor** | H₂ detector alarm <25% LEL, no fire, contained | Site response team | Site supervisor |
| **Level 2 — Moderate** | H₂ alarm >25% LEL OR small fire OR minor injury | Site response + fire dept standby | Airport ops, fire dept |
| **Level 3 — Major** | Large H₂ release OR fire OR serious injury | Full emergency response | Fire dept, airport ops, regulatory authorities |
| **Level 4 — Catastrophic** | Aircraft fire with H₂ OR mass casualty OR explosion | Full emergency + mutual aid | All authorities, emergency services, NTSB/EASA |

### 4.2 Emergency Response Organization

#### 4.2.1 Roles and Responsibilities

| Role | Primary Responsibility | Authority |
|------|----------------------|-----------|
| **Incident Commander** | Overall incident management | Full authority at scene |
| **Operations Lead** | Tactical operations | Direct field operations |
| **Safety Officer** | Personnel and operational safety | Stop unsafe actions |
| **H₂ Specialist** | Technical H₂ guidance | Advise incident commander |
| **Communications Coordinator** | Internal/external communications | Manage information flow |
| **Medical Coordinator** | Medical response coordination | Direct medical resources |
| **Liaison Officer** | Interface with external agencies | Coordinate external support |

#### 4.2.2 Emergency Response Team

**Minimum Staffing During H₂ Operations:**

| Position | Number | Location | Qualification |
|----------|--------|----------|---------------|
| **H₂ Operations Supervisor** | 1 | On-site | H₂ Supervisor certification |
| **Safety Observer** | 1 | Visual contact with operations | H₂ Safety training |
| **Fire Watch** | 1 | Within 15 meters | Fire extinguisher trained |
| **Communication Operator** | 1 | Operations base | Radio operator |

**Fire Department Notification:**
- Fire department notified before H₂ operations begin
- Standby status for all H₂ fueling operations
- Response time <5 minutes to H₂ operations area

### 4.3 Emergency Shutdown Systems

#### 4.3.1 Emergency Shutdown (ESD) Sequence

**Automatic ESD Triggers:**
- H₂ detector >50% LEL
- Fire detection activation
- Emergency stop button pressed
- Loss of grounding continuity
- Communication system failure

**Manual ESD Activation:**
- E-stop buttons at fueling vehicle (2 locations minimum)
- Remote E-stop at safe distance (50 meters)
- Aircraft crew emergency shutdown
- Fire department emergency shutdown

**ESD Actions (automatic, <1 second):**
1. Close main LH₂ transfer valve
2. Close all fuel supply valves
3. Activate pressure relief / venting
4. De-energize non-essential electrical systems
5. Activate emergency lighting
6. Sound evacuation alarm
7. Notify emergency services automatically

#### 4.3.2 Emergency Disconnect

**Breakaway Coupling:**
- Installed in fueling hose (mid-point)
- Activates if hose pulled with >200 N force
- Self-sealing on both sides (<5 seconds)
- Minimizes LH₂ release (<1 liter)

### 4.4 Emergency Response Procedures

#### 4.4.1 H₂ Leak Response

**SMALL LEAK (<10% LEL at 1 meter from source):**

```markdown
IMMEDIATE ACTIONS (0-2 minutes):
☐ Alert all personnel in area (verbal + radio)
☐ Activate safety observer
☐ Eliminate ignition sources within 50 meters
☐ Increase ventilation if applicable
☐ Monitor H₂ levels continuously
☐ Do NOT evacuate unless levels increase

INVESTIGATION (2-10 minutes):
☐ Use portable H₂ detector to locate source
☐ Approach leak from upwind if outdoors
☐ Check all connections visually (DO NOT TOUCH — may be -253°C)
☐ If leak at connection: attempt to tighten if safe to do so
☐ If leak at equipment: shutdown operations and repair

RESOLUTION:
☐ If leak stopped: monitor for 15 minutes, ensure <10% LEL
☐ If leak continues: escalate to LARGE LEAK procedure
☐ Document incident details
☐ Investigate root cause before resuming operations
```

**LARGE LEAK (>25% LEL OR visible vapor plume):**

```markdown
IMMEDIATE ACTIONS (<30 seconds):
☐ ACTIVATE EMERGENCY SHUTDOWN (E-stop)
☐ SOUND EVACUATION ALARM
☐ EVACUATE all personnel to 50 meters MINIMUM
☐ NOTIFY fire department immediately (CODE: "HYDROGEN LEAK - LARGE")
☐ ELIMINATE ignition sources (no vehicles, equipment startups)

RESPONSE (1-5 minutes):
☐ Incident Commander assumes command at safe distance
☐ Establish inner perimeter (50 m) and outer perimeter (100 m)
☐ H₂ Specialist evaluates situation:
   - Source of leak?
   - Can source be shut remotely?
   - Fire risk assessment
   - Dispersion modeling (wind direction)
☐ Fire department arrives and briefs
☐ Coordinate shutdown of H₂ source if not already done

MONITORING (continuous):
☐ H₂ levels at multiple locations (upwind, downwind, perimeter)
☐ Wind speed and direction
☐ Leak dispersion (is leak decreasing?)
☐ Ignition source control (strict enforcement)

RESOLUTION:
☐ Allow LH₂ to evaporate naturally (850:1 expansion — ventilates quickly)
☐ Do NOT approach leak until H₂ levels <10% LEL at source
☐ Verify entire area <10% LEL before re-entry
☐ Full incident investigation before resuming H₂ operations
```

#### 4.4.2 LH₂ Spill Response

**SMALL SPILL (<10 liters):**

```markdown
IMMEDIATE ACTIONS:
☐ Evacuate immediate area (5-meter radius)
☐ Alert personnel
☐ Eliminate ignition sources
☐ Allow natural evaporation (DO NOT approach for 5 minutes)

AFTER EVAPORATION (5+ minutes):
☐ Verify H₂ levels <10% LEL before approaching
☐ Inspect for ice or cold-damaged surfaces
☐ Inspect for oxygen enrichment (liquid air condensation on cold spots)
☐ Allow surfaces to warm naturally
☐ Document spill location and circumstances
```

**LARGE SPILL (>10 liters):**

```markdown
IMMEDIATE ACTIONS:
☐ ACTIVATE EMERGENCY SHUTDOWN
☐ EVACUATE to 100 meters MINIMUM
☐ NOTIFY fire department immediately (CODE: "LARGE LH2 SPILL")
☐ DO NOT ATTEMPT TO CLEAN OR STOP SPILL
☐ ELIMINATE all ignition sources within 100 meters

FIRE DEPARTMENT RESPONSE:
☐ Fire department assumes incident command
☐ Establish exclusion zone (typically 150-200 meters)
☐ Monitor H₂ levels continuously
☐ Allow evaporation and dispersion
☐ Protect exposures with water spray if needed
☐ Re-entry only after full area survey shows <10% LEL
```

#### 4.4.3 H₂ Fire Response

**SMALL H₂ FIRE (leak fire, <1 kg/s):**

```markdown
IMMEDIATE ACTIONS:
☐ Evacuate to 30 meters
☐ Notify fire department (CODE: "HYDROGEN FIRE - SMALL")
☐ DO NOT extinguish if fire is at leak point (prevents gas accumulation)
☐ Shut off H₂ source if possible:
   - Remote shutdown valve
   - Emergency stop button
   - Close manual valves if SAFE to approach

FIRE DEPARTMENT ACTIONS:
☐ Protect exposures with water spray
☐ Cool surrounding equipment
☐ Shut H₂ source if not already done
☐ Allow fire to burn out after source secured
☐ Monitor for re-ignition (H₂ can auto-ignite)

POST-FIRE:
☐ Verify all H₂ sources secured
☐ Monitor H₂ levels (ensure no continued leak)
☐ Inspect equipment for fire damage
☐ Full investigation before resuming operations
```

**LARGE H₂ FIRE OR AIRCRAFT-INVOLVED FIRE:**

```markdown
IMMEDIATE ACTIONS (<30 seconds):
☐ ACTIVATE ALL EMERGENCY ALARMS
☐ EVACUATE to 100 meters MINIMUM
☐ NOTIFY fire department immediately (CODE: "AIRCRAFT FIRE - HYDROGEN")
☐ Activate emergency shutdown (all H₂ systems)
☐ EVACUATE aircraft immediately if passengers aboard

FIRE DEPARTMENT RESPONSE (FULL AIRPORT EMERGENCY):
☐ Full foam and water application per ICAO Annex 14
☐ Incident Commander (Fire Chief) assumes command
☐ Protect aircraft and personnel
☐ Approach with EXTREME CAUTION (invisible flames, explosion risk)
☐ Use thermal imaging cameras to detect flames
☐ Evacuate aircraft via emergency egress if not already done
☐ Shut all H₂ sources

EXTENDED OPERATIONS:
☐ Post-fire watch (4 hours minimum — H₂ can re-ignite)
☐ H₂ level monitoring throughout post-fire period
☐ Incident investigation (NTSB/EASA notification if aircraft damage)
☐ Equipment inspection and testing before return to service
```

### 4.5 Medical Emergencies

#### 4.5.1 Cryogenic Burn Response

**First Aid (see [03-00-14-02-02A](./03-00-14-02-02A_Cryogenic_Ops_Standards.md) for details):**
- Remove victim from hazard
- Remove contaminated clothing (cut, don't pull)
- Warm with lukewarm water (37-40°C) — NOT hot water
- Do NOT rub affected area
- Cover with sterile dressing
- Emergency medical care required (all cases)

#### 4.5.2 Asphyxiation / Oxygen Deficiency Response

**Symptoms:**
- Rapid breathing
- Dizziness, confusion
- Headache
- Loss of consciousness

**Response:**
1. Do NOT enter low-oxygen area without breathing apparatus
2. Alert fire department / rescue team immediately
3. If victim in accessible location with adequate oxygen:
   - Move victim to fresh air
   - Administer oxygen if trained and available
   - CPR if not breathing
4. Emergency medical care required

### 4.6 Communication Protocols

#### 4.6.1 Internal Communications

**Emergency Radio Protocol:**

- **Channel**: Dedicated emergency frequency
- **Priority**: Emergency calls override all other traffic
- **Format**: "EMERGENCY - EMERGENCY - EMERGENCY - [location] - [incident type] - [action required]"

**Example:**
> "EMERGENCY - EMERGENCY - EMERGENCY - Gate 15 - LARGE HYDROGEN LEAK - EVACUATE 100 METERS - FIRE DEPARTMENT RESPONDING"

#### 4.6.2 External Notifications

| Recipient | When to Notify | Information to Provide |
|-----------|---------------|------------------------|
| **Fire Department** | Any H₂ fire or leak >25% LEL | Location, incident type, wind direction, personnel status |
| **Airport Operations** | Any Level 2+ emergency | Same as fire department + aircraft status |
| **Medical Services** | Any injury | Number of casualties, injury types, access route |
| **Regulatory Authorities** | Any fire, spill, or serious injury | Preliminary notification within 2 hours, full report within 24 hours |
| **Company Management** | All H₂ incidents | Immediate notification (within 30 minutes) |
| **NTSB/EASA** | Aircraft damage or serious injury | Immediate notification |

### 4.7 Post-Emergency Procedures

#### 4.7.1 Scene Securement

- Maintain exclusion zone until full investigation
- Post guards to prevent unauthorized entry
- Preserve evidence (photos, samples if safe)
- H₂ monitoring until confirmed <10% LEL for 1 hour

#### 4.7.2 Investigation

**Mandatory Investigation for:**
- Any H₂ fire
- Any H₂ leak >25% LEL
- Any H₂ spill >10 liters
- Any injury
- Any emergency shutdown activation

**Investigation Team:**
- Safety Manager (lead)
- H₂ Specialist
- Operations Manager
- Maintenance representative
- Union/employee representative (if applicable)

**Investigation Report Elements:**
- Incident timeline
- Root cause analysis
- Contributing factors
- Immediate corrective actions
- Long-term preventive actions
- Lessons learned

#### 4.7.3 Return to Service

**Requirements Before Resuming H₂ Operations:**
- Full investigation completed
- Root cause identified and corrective actions implemented
- All equipment inspected and tested
- Personnel debriefed
- Regulatory clearance obtained (if required)
- Management approval

## 5. Performance Metrics

### 5.1 Emergency Preparedness KPIs

| Metric | Target | Frequency | Owner |
|--------|--------|-----------|-------|
| **Emergency Response Time** | <5 minutes fire dept arrival | Per incident | Airport Operations |
| **Emergency Drill Completion** | 4 drills/year (1 per quarter) | Quarterly | Safety Manager |
| **Emergency Equipment Readiness** | 100% functional | Weekly inspection | Maintenance Manager |
| **Emergency Training Current** | 100% personnel | Continuous | Training Manager |
| **Incident Investigation Closure** | 100% within 30 days | Per incident | Safety Manager |
| **Corrective Action Implementation** | 100% within timeline | Per action | Responsible Manager |

### 5.2 Drill Requirements

| Drill Type | Frequency | Participants | Duration |
|------------|-----------|--------------|----------|
| **Tabletop Exercise** | Quarterly | Management + safety team | 2 hours |
| **Functional Drill** | Bi-annual | Operations + fire dept | 4 hours |
| **Full-Scale Exercise** | Annual | All responders + airport | 8 hours |
| **Evacuation Drill** | Quarterly | All site personnel | 30 minutes |

## 6. Training and Competency

### 6.1 Emergency Response Training

| Training Module | Audience | Duration | Recurrency |
|----------------|----------|----------|------------|
| **H₂ Emergency Awareness** | All H₂ personnel | 2 hours | Annual |
| **H₂ Emergency Response** | H₂ operators + safety team | 8 hours | Semi-annual |
| **Incident Command (H₂)** | Supervisors, managers | 16 hours | Annual |
| **Fire Department H₂ Response** | Airport fire department | 24 hours | Annual |

### 6.2 Competency Demonstration

Personnel must demonstrate:
- Recognition of emergency scenarios
- Correct emergency procedures
- Proper use of emergency equipment
- Effective communication during emergencies
- Decision-making under stress

## 7. Cross-References

### 7.1 Related Documents

- **Parent Document**: [03-00-14_Ops_Std_Sustain](../)
- **LH2 Fueling**: [03-00-14-02-01A_LH2_Fueling_Ops_Standards.md](./03-00-14-02-01A_LH2_Fueling_Ops_Standards.md)
- **Cryogenic Ops**: [03-00-14-02-02A_Cryogenic_Ops_Standards.md](./03-00-14-02-02A_Cryogenic_Ops_Standards.md)
- **H2 Safety**: [03-00-14-02-03A_H2_Safety_Ops_Standards.md](./03-00-14-02-03A_H2_Safety_Ops_Standards.md)

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Emergency Response Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-14-02-04A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use — Safety Critical
- **Owner**: AMPEL360 Emergency Response WG

---
