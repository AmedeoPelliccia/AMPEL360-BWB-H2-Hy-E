# SAF Access Difficulties Reporting — Article 6

**Document ID:** 02-90-01-004A  
**Version:** 1.0  
**Date:** 2025-11-12  
**Status:** ACTIVE

---

## 1. Purpose

This document defines procedures for reporting difficulties in accessing Sustainable Aviation Fuel (SAF) under **Article 6 of EU Regulation 2023/2405** (ReFuelEU Aviation). It provides workflows for documenting supply issues, escalating to competent authorities, and triggering corrective actions.

---

## 2. Regulatory Basis

### Article 6 — Access to Sustainable Aviation Fuels

**Article 6(1):** Aircraft operators encountering difficulties in accessing sufficient quantities or appropriate qualities of SAF at Union airports shall inform the competent authority.

**Article 6(2):** Competent authority shall:
1. Contact the Union airport managing body
2. Request evidence on fuel supplier arrangements and SAF availability
3. If deficiency confirmed, require airport to take corrective action
4. Monitor remediation and report to Commission/EASA

**Purpose:** Prevent situations where operators willing to use SAF cannot obtain it due to airport-side supply constraints.

---

## 3. What Constitutes a "Difficulty"?

### Qualifying Scenarios

Report when AMPEL360 experiences:

#### Quantity Insufficiency
- **Issue:** SAF volume available < SAF volume requested
- **Example:** Operator needs 50 tonnes SAF; only 20 tonnes available
- **Threshold:** Persistent shortages (not one-off events)

#### Quality Issues
- **Issue:** SAF does not meet specifications (ASTM D7566, DEF STAN 91-091)
- **Example:** Aromatic content < 8% (seal compatibility issues)
- **Example:** Batch contamination, off-spec chemistry

#### Unreasonable Pricing
- **Issue:** SAF premium far exceeds market benchmarks
- **Caution:** Price differential alone insufficient; must impede access
- **Example:** SAF offered at 5x conventional fuel price with no commercial justification

#### Supplier Refusal
- **Issue:** Airport fuel supplier refuses to supply SAF despite availability
- **Example:** Supplier prioritizes other customers; discriminatory practices

#### Infrastructure Limitations
- **Issue:** Airport lacks SAF-compatible fuelling equipment
- **Example:** No segregated tankage; commingling prohibited by operator specs

#### Administrative Barriers
- **Issue:** Excessive paperwork, delays in contractual processes
- **Example:** Months-long approval for SAF supply agreement

### Not Qualifying as Difficulties

**Do NOT report:**
- **Global SAF scarcity:** If SAF unavailable EU-wide, this is market reality (not airport-specific)
- **Economic preference:** Operator chooses conventional fuel to save costs (no supply barrier)
- **Lack of advance booking:** Operator failed to pre-order SAF with reasonable lead time
- **Contractual disputes:** Commercial disagreement on terms (resolve bilaterally first)

---

## 4. Difficulty Reporting Process

### Step 1: Initial Symptom Detection (Day 0)

**Trigger Events:**
- Fuel order rejected or partially filled
- Quality test failure on delivered SAF batch
- Supplier notification of unavailability

**Responsible:** AMPEL360 Fuel Procurement / Operations

**Immediate Actions:**
1. **Document Incident:** Date, airport, supplier, quantity requested/received
2. **Contact Supplier:** Attempt to resolve (alternative batch, delivery schedule)
3. **Safety Assessment:** Ensure flight safety not compromised (use conventional fuel if necessary)

### Step 2: Evidence Gathering (Days 1-7)

**Responsible:** AMPEL360 Compliance Team

**Required Documentation:**

#### A. Difficulty Description
- Nature of problem (quantity, quality, price, refusal, infrastructure)
- Date(s) of occurrence
- Union airport ICAO/IATA code
- Impact on operations (flights affected, SAF targets missed)

#### B. Supplier Engagement
- Name and contact of fuel supplier
- Correspondence summary (emails, meeting notes)
- Quantities requested vs. quantities offered
- Supplier's stated reasons for shortfall

#### C. Quality Evidence (if applicable)
- Lab test results showing off-spec parameters
- ASTM D7566 certification documentation (or lack thereof)
- Batch traceability (batch number, supplier Declaration of Conformity)

#### D. Market Context
- SAF availability at comparable Union airports (benchmark)
- Industry reports on regional SAF supply
- Evidence that operator willing to pay reasonable premium

#### E. Operational Impact
- Flights where SAF could not be uplifted as planned
- Shortfall in Article 3 compliance targets
- Financial impact (if quantifiable, but not required)

**Output:** Difficulty evidence bundle

### Step 3: Formal Notification to Competent Authority (Days 8-10)

**Responsible:** AMPEL360 Legal & Compliance

**Notification Content:**

| Section | Content |
|---------|---------|
| **Subject** | SAF Access Difficulty Report — Article 6, Reg (EU) 2023/2405 |
| **Operator Details** | ICAO code, legal name, contact |
| **Airport** | ICAO/IATA, managing body name |
| **Supplier** | Name, contact (if known) |
| **Difficulty Type** | Quantity / Quality / Price / Refusal / Infrastructure / Admin |
| **Dates** | Occurrence dates and persistence (ongoing or resolved) |
| **Quantities** | Requested vs. supplied (tonnes) |
| **Evidence** | Attach documentation bundle |
| **Impact** | Flights affected, compliance risk |
| **Requested Action** | Investigation of airport/supplier arrangements; corrective measures |

**Submission Channels:**
- **Primary:** National CAA ReFuelEU portal (Article 6 module)
- **Copy:** EASA (for EU-wide monitoring)
- **Format:** Structured form + PDF evidence attachments

**Template Dataset:**

```csv
airport_icao,airport_iata,date,difficulty_type,supplier_contacted,quantity_requested_tonnes,quantity_available_tonnes,correspondence_uri,escalation_status
EDDF,FRA,2025-02-15,Quantity shortage,Lufthansa Aviation Fuel,50.0,20.0,https://docs.ampel360/correspondence/EDDF-2025-02-15,Submitted to CAA
LFPG,CDG,2025-03-08,Quality issue,TotalEnergies Aviation,30.0,30.0,https://docs.ampel360/correspondence/LFPG-2025-03-08,Under investigation
```

### Step 4: Authority Investigation (Days 11-40)

**Authority Actions:**
1. **Acknowledge Receipt:** Typically within 5 business days
2. **Contact Airport:** Request evidence from airport managing body per Article 6(2)
   - Fuel supply contracts
   - SAF procurement records
   - Fuelling infrastructure specifications
3. **Fuel Supplier Inquiry:** If airport delegates fuelling, contact supplier
4. **Site Inspection (optional):** Physical verification of infrastructure/stocks
5. **Determination:** Deficiency confirmed or operator claim unfounded

**Expected Timeline:** 30-45 days (regulatory guidance)

**Possible Outcomes:**

#### Deficiency Confirmed
- Authority orders airport to take corrective action
- Remediation plan with timeline (e.g., increase SAF orders, upgrade infrastructure)
- Follow-up monitoring by authority
- Operator informed of corrective measures

#### Operator Claim Unfounded
- Authority finds adequate SAF was available
- Operator may have failed to follow procurement procedures
- Guidance provided for future SAF procurement

#### Partial Deficiency
- Some constraints confirmed (e.g., temporary supply disruption)
- Airport takes partial corrective action
- Operator adjusts procurement strategy

### Step 5: Corrective Action Monitoring (Ongoing)

**Authority Obligations:**
- Monitor airport/supplier compliance with corrective action plan
- Report to Commission and EASA
- Update operator on progress

**AMPEL360 Actions:**
- Re-attempt SAF procurement per corrective action timeline
- Document improvements (quantity, quality, availability)
- Close difficulty ticket if resolved
- Escalate if corrective action inadequate

**Follow-Up Reporting:**
- Quarterly status updates to authority
- Include in next Article 8 annual report (difficulties encountered/resolved)

---

## 5. AMPEL360-Specific Considerations

### Hydrogen vs. SAF Difficulties

**Distinction:**
- **Article 6:** Applies to SAF (drop-in sustainable jet fuel)
- **Article 7:** Applies to hydrogen and electricity infrastructure

**AMPEL360 Context:**
- Primary propulsion: Hydrogen (report H₂ access issues under Article 7 monitoring, not Article 6)
- Backup/auxiliary fuel: SAF (Article 6 applies if difficulties encountered)

**Clear Separation:** When reporting, specify fuel type and system (primary H₂ vs. backup SAF).

### Proactive SAF Procurement

**Best Practice:**
- Establish long-term SAF supply agreements with multiple suppliers
- Pre-book SAF volumes well in advance (6-12 months)
- Diversify supply chain (different feedstocks, conversion processes)
- Participate in airport SAF infrastructure partnerships

**Reduces Likelihood of Article 6 Reports:** Strong commercial relationships minimize access difficulties.

### Quality Specifications for AMPEL360

**Unique Requirements:**
- BWB design may have specific fuel property sensitivities (e.g., thermal stability at altitude)
- Hydrogen fuel cell contamination risks from backup fuel cross-contamination

**Quality Assurance:**
- Define AMPEL360-specific SAF acceptance criteria (beyond ASTM D7566)
- Communicate to suppliers in advance
- Report quality issues under Article 6 if supplier cannot meet specs

### Green Hydrogen Access (Article 7 Linkage)

**If H₂ supply issues arise:**
- Do NOT report under Article 6 (SAF-specific)
- Reference Article 7 airport H₂ infrastructure reports
- Engage with airport managing body directly
- Inform competent authority via Article 8 reporting or direct communication

**Cross-Reference:** [02-90-01-005A_H2_Electricity_Report_Art7.md](02-90-01-005A_H2_Electricity_Report_Art7.md)

---

## 6. Evidence Standards

### Documentary Requirements

**Minimum Evidence for Credible Report:**

| Evidence Type | Required | Format | Example |
|---------------|----------|--------|---------|
| **Fuel Order** | Yes | Email, purchase order | "Request for 50T SAF, HEFA, delivery 2025-02-20" |
| **Supplier Response** | Yes | Email, letter | "Only 20T available due to supply chain disruption" |
| **Alternative Sourcing Attempts** | Yes | Correspondence | Contacted 2+ suppliers; all cite shortages |
| **Quality Test Results** | If quality issue | Lab report | ASTM D7566 parameter X = Y (out of spec) |
| **Operational Impact** | Yes | Flight schedule | AMP102-AMP115: SAF target missed, conventional fuel used |
| **Market Benchmark** | Recommended | Industry report | SAF available at EHAM, EGLL; shortage specific to EDDF |

**Avoid:**
- Hearsay without documentation
- Unsubstantiated pricing claims
- Incomplete supplier engagement records

**Strengthen Case:**
- Multiple evidence sources (emails, meeting notes, contracts)
- Third-party verification (industry associations, other operators)
- Long-term procurement history (demonstrates good faith)

---

## 7. Escalation and Remediation

### Authority Corrective Action Powers

**Article 6(2) Authority Tools:**

1. **Mandate SAF Procurement:** Require airport/supplier to source additional SAF
2. **Infrastructure Upgrades:** Order installation of SAF-compatible tankage/fuelling equipment
3. **Supply Agreement Review:** Require transparent, non-discriminatory SAF supply terms
4. **Penalties:** Impose fines on airport/supplier for non-compliance (Member State law)

### Operator Role in Remediation

**AMPEL360 Responsibilities:**
- **Cooperate:** Provide additional information upon authority request
- **Re-Test:** Attempt procurement once corrective action implemented
- **Feedback:** Inform authority if measures insufficient
- **Goodwill:** Continue commercial dialogue with airport/supplier

**Avoid:**
- Circumventing local supplier (if corrective action in progress)
- Public disputes damaging relationships
- Excessive reliance on Article 6 (commercial solutions preferred)

### Timeline Expectations

| Milestone | Expected Timing |
|-----------|----------------|
| Operator reports difficulty | Day 0 |
| Authority acknowledges | Day 5 |
| Airport responds to authority | Day 20 |
| Authority determination | Day 40 |
| Corrective action plan | Day 50 |
| Implementation start | Day 60 |
| Full resolution | Day 120-180 (varies) |

**Long-Term Infrastructure:** Some corrective actions (new tankage) may take 12-24 months.

---

## 8. Reporting Template

### SAF Access Difficulty Record (CSV Format)

**Core fields for internal tracking and authority reporting:**

```csv
difficulty_id,airport_icao,airport_iata,airport_name,date,difficulty_type,supplier_name,supplier_contact,quantity_requested_tonnes,quantity_available_tonnes,quality_issue_description,price_premium_pct,correspondence_uri,flights_impacted,escalation_date,authority_response_date,corrective_action_plan,resolution_date,status
DIFF-2025-001,EDDF,FRA,Frankfurt Airport,2025-02-15,Quantity shortage,Lufthansa Aviation Fuel,fuel@lhag.de,50.0,20.0,,N/A,https://docs.ampel360/EDDF-001,"AMP102,AMP105,AMP107",2025-02-18,2025-02-25,Airport to procure additional SAF via Neste; ETA 2025-03-15,2025-03-20,Resolved
DIFF-2025-002,LFPG,CDG,Paris Charles de Gaulle,2025-03-08,Quality issue,TotalEnergies Aviation,saf@totalenergies.fr,30.0,30.0,Aromatic content 6.8% (spec min 8%),,https://docs.ampel360/LFPG-002,"AMP201,AMP203",2025-03-10,2025-03-18,Supplier to blend batches to meet aromatics spec,2025-03-25,Resolved
DIFF-2025-003,EHAM,AMS,Amsterdam Schiphol,2025-04-12,Infrastructure,bp Aviation,bp-schiphol@bp.com,40.0,40.0,No segregated SAF tankage; commingling risk,,https://docs.ampel360/EHAM-003,"AMP301-AMP310",2025-04-15,,Airport to install dedicated SAF tank; ETA Q4 2025,,Open
```

**Field Definitions:**

- `difficulty_id`: Unique identifier (e.g., DIFF-YYYY-NNN)
- `difficulty_type`: Quantity shortage / Quality issue / Price barrier / Refusal / Infrastructure / Admin
- `quality_issue_description`: Free text (if quality type)
- `price_premium_pct`: % above conventional fuel (if price type)
- `correspondence_uri`: Link to stored evidence (emails, letters)
- `flights_impacted`: List of flight numbers affected
- `escalation_date`: Date reported to authority
- `authority_response_date`: Date authority acknowledged
- `corrective_action_plan`: Summary of mandated remediation
- `resolution_date`: Date difficulty resolved
- `status`: Open / Under investigation / Corrective action in progress / Resolved / Closed - unfounded

---

## 9. Integration with Article 8 Reporting

### Annual Report Inclusion

**Article 8(1)(e) — Additional Information:**  
Include summary of Article 6 difficulties encountered during reporting year.

**Template Section:**

```markdown
### SAF Access Difficulties (Article 6)

**Reporting Year:** 2024

**Difficulties Reported:**
- EDDF (FRA): Quantity shortage Feb 2025; resolved Mar 2025 via airport corrective action
- LFPG (CDG): Quality issue (aromatics) Mar 2025; resolved Mar 2025 via batch blending
- EHAM (AMS): Infrastructure limitation Apr 2025; corrective action in progress (Q4 2025 ETA)

**Impact on Compliance:**
- Estimated 15 tonnes SAF shortfall due to EDDF incident
- No impact on Article 3 minimum shares (compensated at other airports)
- All difficulties formally reported and tracked to resolution
```

**Benefits:**
- Demonstrates good faith effort to use SAF
- Contextualizes any compliance shortfalls
- Supports industry data on SAF supply maturity

---

## 10. Preventive Measures

### Avoid Article 6 Reports Through:

1. **Early Supplier Engagement:** Lock in SAF supply 6-12 months ahead
2. **Diversified Supply Chain:** Multiple suppliers per airport
3. **Quality Pre-Checks:** Require supplier Declaration of Conformity (DoC) and test certificates
4. **Airport Partnerships:** Co-invest in SAF infrastructure (Article 7 synergy)
5. **Industry Collaboration:** Join airline consortia for bulk SAF purchasing
6. **Continuous Monitoring:** Track SAF market availability and pricing trends

**Trade-Off:**  
Proactive measures (long-term contracts, partnerships) more effective than reactive Article 6 reports.

---

## 11. Related Documents

- **[02-90-01-000A_README.md](02-90-01-000A_README.md):** Overall compliance framework
- **[02-90-01-001A_Regulatory_Scope.md](02-90-01-001A_Regulatory_Scope.md):** Article 6 detailed analysis
- **[02-90-01-002A_Data_Model_Article8.csv](02-90-01-002A_Data_Model_Article8.csv):** Include SAF difficulties in annual report
- **[02-90-01-005A_H2_Electricity_Report_Art7.md](02-90-01-005A_H2_Electricity_Report_Art7.md):** Hydrogen access (not SAF)
- **[02-90-01-007A_CI_Validation_Rules.md](02-90-01-007A_CI_Validation_Rules.md):** Automated checks for SAF data quality

---

## 12. References

- **Regulation (EU) 2023/2405**, Article 6
- **EASA ReFuelEU Portal** — Article 6 difficulty reporting module
- **IATA SAF Registry** — Industry SAF availability tracking
- **National CAA Guidance** — Member State-specific reporting procedures
- **ASTM D7566** — Standard Specification for Aviation Turbine Fuel Containing Synthesized Hydrocarbons

---

## 13. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-12 | AMPEL360 Compliance Team | Initial SAF access difficulties document |

---

**End of SAF Access Difficulties Document**

For difficulty reporting template dataset, see CSV format in Section 8 above.
