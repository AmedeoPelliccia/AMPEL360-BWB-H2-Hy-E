# Temporary Exemption Workflow — Article 5(3)

**Document ID:** 02-90-01-003A  
**Version:** 1.0  
**Date:** 2025-11-12  
**Status:** ACTIVE

---

## 1. Purpose

This document defines the workflow for requesting temporary exemptions from the 90% refuelling obligation under **Article 5(3) of EU Regulation 2023/2405** (ReFuelEU Aviation). It provides step-by-step procedures, evidence requirements, and timelines for AMPEL360 operators.

---

## 2. Regulatory Basis

### Article 5(3) Provision

> "By way of derogation from paragraph 1, the competent authority may, upon request by an aircraft operator, grant a temporary exemption from the obligation referred to in that paragraph for routes operated by that aircraft operator where compliance with that obligation would create an undue operational burden."

### Commission Guidelines (09 October 2024)

The European Commission issued guidelines specifying:
- Acceptable justifications for "undue operational burden"
- Evidence standards for exemption requests
- Maximum exemption durations
- Renewal conditions

---

## 3. When to Request an Exemption

### Qualifying Scenarios

Exemptions may be appropriate for:

#### Short Routes (Primary Use Case)
- **Distance:** Typically < 500 km
- **Issue:** Frequent refuelling creates disproportionate turnaround time
- **Example:** AMPEL360 shuttle service between regional airports

#### Infrastructure Constraints
- **Issue:** Union airport lacks adequate H₂ refuelling capacity
- **Temporary:** Until Article 7 infrastructure operational
- **Alternative:** Refuel at nearby hub airport

#### Operational Patterns
- **Issue:** Route structure (multiple short legs) makes 90% rule impractical
- **Example:** Multi-stop service with optimized fuel load for entire day

#### Safety Margins
- **Issue:** Specific route requires larger fuel reserves due to weather/terrain
- **Note:** Distinct from Article 5(2) safety tanking; this is systematic route characteristic

### When NOT to Request

**Do NOT use Article 5(3) for:**
- Economic savings (fuel price arbitrage) — this is prohibited tanking
- Convenience without operational justification
- Permanent operational patterns — these require fleet/network redesign
- Weather-specific events — use Article 5(2) safety tanking instead

---

## 4. Exemption Request Process

### Step 1: Internal Assessment (Weeks 1-2)

**Responsible:** AMPEL360 Operations Planning Team

**Actions:**
1. **Identify Route:** Specify ICAO codes, distance, frequency
2. **Document Burden:** Quantify operational impact
   - Additional turnaround time
   - Reduced aircraft utilization
   - Passenger impact (delays, connections)
3. **Evaluate Alternatives:** Demonstrate why operational adjustment insufficient
   - Larger fuel capacity?
   - Route consolidation?
   - Schedule optimization?
4. **Projected Impact:** Estimate fuel uplifted if exemption granted

**Output:** Internal justification memo

### Step 2: Evidence Preparation (Weeks 3-4)

**Responsible:** AMPEL360 Compliance & Operations

**Required Evidence (per Commission Guidelines):**

#### A. Route Characteristics
- ICAO origin/destination
- Great circle distance (km)
- Block time (minutes)
- Frequency (flights per week/month)
- Load factor (historical average)

#### B. Fuel Analysis
- Typical fuel uplift per leg (tonnes)
- Fuel required for route (tonnes)
- Current uplift percentage at Union airport
- Projected uplift if 90% rule applied

#### C. Operational Burden Quantification
- Additional turnaround time per flight (minutes)
- Annual lost aircraft utilization (hours)
- Passenger schedule impact
- Cost impact (quantified in €, but NOT primary justification)

#### D. Infrastructure Constraints (if applicable)
- H₂ refuelling capacity at Union airport (reference Article 7 report)
- Current availability vs. required capacity
- Expected commissioning date of adequate infrastructure

#### E. Alternatives Considered
- Larger fuel tanks: technical feasibility, certification timeline
- Route restructuring: commercial viability, network impact
- Schedule changes: passenger demand constraints

#### F. Mitigation Measures
- Commitment to resume 90% compliance when burden removed
- Plans to increase refuelling percentage during exemption
- Participation in infrastructure development (partnerships, funding)

**Output:** Exemption request dossier

### Step 3: Formal Application (Week 5)

**Responsible:** AMPEL360 Legal & Compliance

**Submission:**
1. Complete **Exemption Request Form** (Template: [02-90-01-A001_Templates/Exemption_Request_Form_Art5-3.docx](02-90-01-A001_Templates/Exemption_Request_Form_Art5-3.docx))
2. Attach evidence dossier
3. Submit to competent authority via official portal/email

**Form Core Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| `operator_icao` | ICAO operator designator | AMP360 |
| `operator_name` | Legal entity name | AMPEL360 Aviation GmbH |
| `route_id` | Origin-Destination pair | EDDF-EDDH |
| `union_airport_icao` | Union airport seeking relief | EDDF |
| `distance_km` | Great circle distance | 389 |
| `schedule_code` | Flight numbers | AMP101-AMP108 (daily) |
| `justification_type` | Primary reason | Short route turnaround |
| `evidence_refs` | Attachment list | Annex A: Fuel data; Annex B: Utilization |
| `projected_impact` | Estimated non-compliance % | 75% uplift (vs. 90% required) |
| `requested_period` | Duration | 12 months from approval |
| `contact_point` | Authority liaison | compliance@ampel360.aero |

**Submission Channels:**
- **Primary:** National CAA ReFuelEU portal
- **Backup:** Email to designated authority contact
- **Confirmation:** Request acknowledgment receipt

### Step 4: Authority Review (Weeks 6-10)

**Authority Actions:**
1. **Completeness Check:** Verify all evidence provided
2. **Substantive Review:** Assess operational burden claim
3. **Stakeholder Consultation (optional):** EASA, Commission, other operators
4. **Site Visit (optional):** Inspect airport infrastructure
5. **Decision:** Approve, approve with conditions, or deny

**Expected Timeline:** 4-6 weeks (regulatory guidance)

**Possible Outcomes:**

#### Approval
- Exemption granted for specified period (typically 6-12 months)
- Conditions may apply (e.g., minimum 75% uplift, quarterly reporting)
- Renewable upon demonstration continued burden

#### Conditional Approval
- Exemption granted with enhanced monitoring
- Additional reporting requirements
- Review trigger if circumstances change

#### Denial
- Justification insufficient
- Alternatives not adequately explored
- Right to appeal within 30 days

### Step 5: Implementation (Upon Approval)

**Responsible:** AMPEL360 Operations

**Actions:**
1. **Update OM (Operations Manual):** Document approved exemption
2. **Dispatch Instructions:** Brief flight planning and dispatch teams
3. **Fuel Planning:** Adjust uplift targets for exempt route
4. **Compliance Tracking:** Monitor actual uplift percentages
5. **Article 8 Reporting:** Include exemption status in annual report

**Monitoring:**
- Monthly review of uplift percentages vs. exemption conditions
- Quarterly internal reports to senior management
- Prepare for renewal application if burden persists

### Step 6: Renewal or Termination

**Renewal (if needed):**
- Apply 90 days before expiration
- Demonstrate continued operational burden
- Update evidence (current fuel data, infrastructure status)
- Reference prior approval and compliance with conditions

**Termination:**
- If operational burden removed (e.g., infrastructure upgraded, route discontinued)
- Notify authority of return to 90% compliance
- Update Article 8 reporting accordingly

---

## 5. Evidence Standards (Commission Guidelines)

### Quantitative Thresholds

While no absolute thresholds specified, Commission guidelines suggest:

| Metric | Indicative Threshold | AMPEL360 Interpretation |
|--------|---------------------|-------------------------|
| Route distance | < 500 km | Strong case for short routes |
| Turnaround time increase | > 20% increase | Significant operational impact |
| Aircraft utilization loss | > 5% annually | Material business impact |
| Infrastructure gap | < 50% capacity available | Clear supply constraint |

### Qualitative Factors

**Strengthens Case:**
- Limited alternatives (small airports, remote locations)
- Commitment to infrastructure development
- Passenger welfare impacts (missed connections)
- Safety margin considerations (not just economic)

**Weakens Case:**
- Economic savings as primary motivation
- Large network operator with flexibility
- Adequate infrastructure available
- Alternative routes or modes feasible

---

## 6. AMPEL360-Specific Considerations

### Hydrogen Infrastructure Gaps

**Scenario:** Union airport lacks H₂ refuelling capacity.

**Strategy:**
1. Reference **Article 7 airport reports** to demonstrate infrastructure unavailability
2. Show AMPEL360 participation in H₂ infrastructure partnerships
3. Request temporary exemption until commissioning date
4. Commit to immediate 90% compliance upon infrastructure availability

**Unique Advantage:**  
Hydrogen-specific exemptions likely viewed favorably by authorities (supporting emerging technology).

### Backup Fuel Systems

**Scenario:** AMPEL360 operates with backup conventional fuel system; Article 5(3) exemption requested for backup fuel uplift.

**Considerations:**
- Backup fuel is small percentage of total energy
- Primary H₂ always uplifted locally (no tankering incentive)
- Exemption scope limited to backup fuel component

**Documentation:** Clearly distinguish H₂ (compliant) vs. backup fuel (exemption requested).

### Route Network Design

**Proactive Approach:**
- Plan route network around Article 7 H₂-ready airports
- Minimize reliance on exemptions
- Use exemptions only during infrastructure ramp-up phase

**Temporary Nature:** Emphasize exemptions as bridge, not permanent solution.

---

## 7. Compliance Tracking

### Exemption Registry

**Maintain Internal Registry:**

| Route | Exemption ID | Granted Date | Expiry Date | Conditions | Status | Renewal Due |
|-------|--------------|--------------|-------------|------------|--------|-------------|
| EDDF-EDDH | EX-2025-001 | 2025-04-15 | 2026-04-14 | Min 75% uplift | Active | 2026-01-15 |

**Integration:**
- Link to Article 8 reporting system
- Flag exempt routes in fuel planning software
- Automated reminders for renewal applications

### Quarterly Compliance Reports

**Internal Monitoring:**
- Actual uplift % vs. exemption conditions
- Infrastructure development progress
- Renewal/termination triggers

**Escalation:**
- Breach of exemption conditions → immediate corrective action
- Risk of denial at renewal → senior management review

---

## 8. Appeals and Disputes

### Appeal Process

**If Exemption Denied:**
1. **Review Decision:** Obtain detailed written reasons from authority
2. **Legal Assessment:** Determine grounds for appeal (procedural error, misinterpretation)
3. **Appeal Submission:** Within 30 days to authority or designated appeal body
4. **Supporting Evidence:** Address specific deficiencies cited in denial
5. **Hearing (if applicable):** Present case to appeal panel

**Alternative:**
- Resubmit application with strengthened evidence
- Adjust operational plans to achieve 90% compliance

### Dispute Resolution

**Authority Discretion:**  
Article 5(3) grants competent authority discretion; judicial review available under national administrative law.

**AMPEL360 Approach:**
- Engage constructively with authority
- Provide supplemental information upon request
- Escalate only if clear regulatory error

---

## 9. Template: Exemption Request Core Fields

**Minimal dataset for exemption application:**

```csv
route_id,origin_icao,destination_icao,distance_km,schedule_code,justification_type,evidence_refs,projected_impact,requested_period,contact_point
EDDF-EDDH,EDDF,EDDH,389,AMP101-AMP108 daily,Short route turnaround impact,"Annex A: Fuel analysis, Annex B: Turnaround study",75% uplift at EDDF (vs 90% required),12 months from approval,compliance@ampel360.aero
```

**Evidence Annexes:**
- Annex A: Historical fuel uplift data (12 months)
- Annex B: Turnaround time analysis
- Annex C: Infrastructure gap assessment (Article 7 reference)
- Annex D: Alternatives considered and rejected
- Annex E: Mitigation commitments

---

## 10. Key Deadlines

| Action | Timing | Responsibility |
|--------|--------|----------------|
| Internal route assessment | Quarterly | Ops Planning |
| Exemption application (if needed) | 90 days before route launch or compliance deadline | Compliance Team |
| Authority response (expected) | 4-6 weeks | N/A |
| Renewal application | 90 days before expiry | Compliance Team |
| Appeal (if denied) | Within 30 days of denial | Legal Counsel |

---

## 11. Related Documents

- **[02-90-01-000A_README.md](02-90-01-000A_README.md):** Overall compliance framework
- **[02-90-01-001A_Regulatory_Scope.md](02-90-01-001A_Regulatory_Scope.md):** Article 5 detailed analysis
- **[02-90-01-002A_Data_Model_Article8.csv](02-90-01-002A_Data_Model_Article8.csv):** Include exemption status in annual report
- **[02-90-01-005A_H2_Electricity_Report_Art7.md](02-90-01-005A_H2_Electricity_Report_Art7.md):** Infrastructure readiness (exemption justification)
- **Template:** [Exemption_Request_Form_Art5-3.docx](02-90-01-A001_Templates/Exemption_Request_Form_Art5-3.docx)

---

## 12. References

- **Regulation (EU) 2023/2405**, Article 5(3)
- **Commission Guidelines on Article 5(3) Exemptions** (09 October 2024)
- **EASA ReFuelEU Aviation Portal** — Exemption application module
- **National CAA Guidance** — Member State-specific procedures

---

## 13. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-12 | AMPEL360 Compliance Team | Initial exemption workflow document |

---

**End of Exemption Workflow Document**

For template form, see: [02-90-01-A001_Templates/Exemption_Request_Form_Art5-3.docx](02-90-01-A001_Templates/Exemption_Request_Form_Art5-3.docx)
