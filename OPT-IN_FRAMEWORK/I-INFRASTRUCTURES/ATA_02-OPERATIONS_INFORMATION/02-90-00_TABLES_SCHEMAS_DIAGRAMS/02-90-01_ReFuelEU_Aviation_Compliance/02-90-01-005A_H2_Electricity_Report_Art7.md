# Hydrogen & Electricity Infrastructure Readiness — Article 7

**Document ID:** 02-90-01-005A  
**Version:** 1.0  
**Date:** 2025-11-12  
**Status:** ACTIVE

---

## 1. Purpose

This document provides guidance on monitoring and utilizing **Article 7 hydrogen and electricity infrastructure reports** from Union airports. It integrates airport readiness data into AMPEL360 operations planning, route network design, and infrastructure partnership strategies.

---

## 2. Regulatory Basis

### Article 7 — Hydrogen and Electricity Infrastructure at Union Airports

**Article 7(1) — Airport Reporting Obligation:**

Union airports shall report to their competent authority (first by **31 March 2025**, then **biennially**):

1. **Infrastructure projects:** Ongoing or planned hydrogen and electricity supply infrastructure for aircraft operations
2. **Supply capacity:** Estimated annual capacity for hydrogen and/or electricity supply
3. **Commissioning timelines:** Expected dates when infrastructure becomes operational

**Article 7(2) — Information Sharing:**

Competent authorities shall make reports available to:
- European Commission
- EASA
- Aircraft operators (upon request)

**Purpose:** Enable hydrogen and electric aircraft operators to plan deployment, identify ready airports, and coordinate infrastructure investments.

---

## 3. AMPEL360 Strategic Importance

### Why Article 7 Matters for AMPEL360

**Primary Propulsion:** AMPEL360 BWB H₂ Hy-E Q100 relies on hydrogen fuel cells as primary propulsion system.

**Operational Requirement:**  
Route network **must** align with airports possessing or developing:
- Liquid hydrogen (LH₂) refuelling infrastructure
- Cryogenic storage and handling capabilities
- Safety systems for H₂ operations
- Trained ground crew

**Article 7 as Planning Input:**
- **Route Network Design:** Prioritize airports with H₂ readiness
- **Launch Customer Selection:** Target airlines operating from H₂-ready airports
- **Infrastructure Partnerships:** Co-invest with airports showing Article 7 commitments
- **EIS Timing:** Align Entry Into Service with critical mass of H₂ airports

**Competitive Advantage:**  
Early AMPEL360 operations at Article 7-compliant airports demonstrate technological leadership and regulatory alignment.

---

## 4. Article 7 Report Structure

### Expected Report Content (Airport)

| Section | Information | AMPEL360 Use |
|---------|-------------|--------------|
| **Airport Identity** | ICAO, IATA, legal name, managing body | Route planning database |
| **H₂ Projects** | Project names, descriptions, partners | Partnership opportunities |
| **H₂ Supply Capacity** | Tonnes/year (LH₂), purity specifications | Refuelling feasibility |
| **Commissioning Dates** | Expected operational dates (phases) | EIS and network rollout timing |
| **Electricity Projects** | High-power charging infrastructure (if applicable) | Future electric propulsion synergy |
| **Electricity Capacity** | MWh/year, connection points | Ground operations electrification |
| **Contact Information** | Airport H₂ infrastructure project lead | Direct engagement |

### Reporting Timeline

| Milestone | Date | AMPEL360 Action |
|-----------|------|-----------------|
| **First Report** | 31 Mar 2025 | Review all Union airport submissions |
| **Biennial Updates** | 31 Mar 2027, 2029, … | Monitor infrastructure progress |
| **Ad-hoc Updates** | As infrastructure commissioned | Update route feasibility |

---

## 5. AMPEL360 Monitoring Process

### Step 1: Report Acquisition (April - May, biennial)

**Source Channels:**
1. **EASA Portal:** Centralized repository of Article 7 reports (primary)
2. **National CAAs:** Member State competent authority websites
3. **Direct from Airports:** Request reports from target airports
4. **Industry Associations:** ACI Europe summaries

**Responsible:** AMPEL360 Infrastructure Planning Team

**Actions:**
- Download all Union airport Article 7 reports
- Ingest into structured database
- Flag updates vs. prior reporting cycle

### Step 2: Data Structuring (May - June)

**Database Schema:**

```csv
airport_icao,airport_iata,airport_name,country,reporting_year,h2_project_name,h2_project_status,h2_capacity_tonnes_per_year,h2_commissioning_date,h2_purity_spec,electricity_capacity_mwh_per_year,electricity_commissioning_date,contact_name,contact_email,notes
EDDF,FRA,Frankfurt Airport,DE,2025,H2FLY Frankfurt Hub,Under construction,5000,2026-Q3,99.97%,1200,2026-Q1,Dr. Hans Mueller,h2@fraport.de,Phase 1: Regional aircraft; Phase 2: 2027 widebody
LFPG,CDG,Paris Charles de Gaulle,FR,2025,CDG Hydrogen Valley,Planning,8000,2027-Q2,99.95%,1500,2027-Q1,Marie Dubois,h2@adp.fr,Joint project with Air Liquide
EHAM,AMS,Amsterdam Schiphol,NL,2025,Schiphol H2 Gateway,Operational,3000,2025-Q4,99.99%,800,2025-Q4,Jan de Vries,hydrogen@schiphol.nl,Early adopter program available
EGLL,LHR,London Heathrow,UK,2025,Heathrow Hydrogen Hub,Feasibility,0,2028-Q1,TBD,0,2028-Q1,Sarah Johnson,hydrogen@heathrow.com,Study phase; capacity TBD
```

**Key Fields for AMPEL360:**

- `h2_project_status`: Planning / Feasibility / Under construction / Operational / Delayed
- `h2_capacity_tonnes_per_year`: Annual LH₂ refuelling capacity
- `h2_commissioning_date`: When infrastructure ready (critical for route launch)
- `h2_purity_spec`: Fuel cell contamination tolerance (AMPEL360 requires ≥99.95%)

**Tool Integration:**
- Import into **ATA 95 DPP/CAOS** for analytics
- Link to route network optimizer
- Dashboard for management visibility

### Step 3: Readiness Assessment (June - July)

**Classify Airports by H₂ Readiness:**

#### Tier 1: Operational (Ready for AMPEL360)
- H₂ infrastructure commissioned and operational
- Capacity ≥ AMPEL360 route needs
- Safety certifications complete
- **Action:** Include in initial route network

#### Tier 2: Near-Term (0-18 months)
- Infrastructure under construction
- Commissioning date < 18 months
- High confidence in delivery
- **Action:** Plan routes for post-commissioning; secure slots

#### Tier 3: Mid-Term (18-36 months)
- Planning or early construction phase
- Commissioning 18-36 months out
- **Action:** Engage for partnership; monitor progress

#### Tier 4: Long-Term (>36 months)
- Feasibility studies or distant commissioning
- **Action:** Track for future network expansion

#### Tier 5: No Plan
- Airport has not reported H₂ infrastructure plans
- **Action:** Advocate for investment; consider Article 6-style difficulty reporting (if applicable)

**Example Assessment:**

| Airport | Tier | Commissioning | AMPEL360 Routes | Notes |
|---------|------|---------------|-----------------|-------|
| EHAM (AMS) | 1 | Q4 2025 | AMP100 series | Launch airport candidate |
| EDDF (FRA) | 2 | Q3 2026 | AMP200 series | Reserve slots now |
| LFPG (CDG) | 2 | Q2 2027 | AMP300 series | Partnership with Air Liquide |
| EGLL (LHR) | 3 | Q1 2028 | Future expansion | Monitor study outcomes |
| LEMD (MAD) | 5 | None reported | Not feasible | Advocate for infrastructure |

### Step 4: Partnership Development (Ongoing)

**Proactive Engagement:**

For Tier 1-3 airports:
1. **Direct Outreach:** Contact airport H₂ project leads (Article 7 reports include contact info)
2. **MoU Negotiations:** Memoranda of Understanding for:
   - H₂ supply agreements (volume, quality, pricing)
   - Infrastructure use rights (refuelling positions, equipment access)
   - Safety protocol alignment
   - Marketing cooperation (airport as sustainability showcase)
3. **Co-Investment:** Joint ventures or cost-sharing for AMPEL360-specific infrastructure (e.g., dedicated widebody H₂ fuelling positions)
4. **Regulatory Coordination:** Ensure airport H₂ operations certified for AMPEL360 aircraft type

**Responsible:** AMPEL360 Business Development & Infrastructure Team

**Deliverables:**
- Signed MoUs with Tier 1-2 airports (prior to EIS)
- Infrastructure Service Level Agreements (SLAs)
- Integration into airport operations manuals

### Step 5: Cross-Link to AMPEL360 Technical Systems (Continuous)

**Integration Points:**

#### T-TECHNOLOGY / E2-ENERGY (ATA 24, 28, 47, 49)
- **Interface Control:** Airport H₂ supply pressure, temperature, flow rate
- **Fuel Cell Specs:** AMPEL360 H₂ purity requirements (≥99.95%)
- **Electrical Ground Power:** Backup systems during H₂ refuelling
- **Safety Systems:** Leak detection, emergency shutdown coordination

**Action:** Maintain **Interface Control Documents (ICDs)** linking Article 7 airport infrastructure specs to AMPEL360 aircraft systems.

**Example ICD Reference:**  
`ICD-02-00-28-001_ATA28_H2_FUEL` (already exists in OPT-IN structure)

#### T-TECHNOLOGY / C2-CRYOGENICS (ATA 28)
- **LH₂ Handling:** Cryogenic transfer procedures (−253°C)
- **Boil-Off Management:** Airport vs. aircraft responsibilities
- **Insulation Standards:** Tank compatibility

**Action:** Validate airport cryogenic systems against AMPEL360 ATA 28 specifications.

#### N-NEURAL NETWORKS / ATA 95 (DPP/CAOS)
- **Predictive Analytics:** Forecast H₂ demand vs. airport supply capacity
- **Route Optimization:** Real-time airport H₂ availability feed
- **Digital Twin:** Model ground operations including H₂ refuelling

**Action:** Ingest Article 7 data into CAOS for automated network planning.

---

## 6. Article 7 Data as Compliance Evidence

### Supporting Other ReFuelEU Articles

#### Article 5(3) Exemptions
**Use Case:** If requesting temporary exemption from 90% refuelling rule due to H₂ infrastructure gaps:
- **Evidence:** Reference airport's Article 7 report showing no H₂ capacity
- **Justification:** Operator willing to refuel locally, but infrastructure unavailable
- **Timeline:** Commit to compliance upon commissioning date per Article 7 report

**See:** [02-90-01-003A_Exemption_Workflow_Art5-3.md](02-90-01-003A_Exemption_Workflow_Art5-3.md)

#### Article 6 Difficulties (Adapted for H₂)
**Use Case:** Airport Article 7 report indicates H₂ project, but infrastructure not delivered on schedule.
- **Action:** Engage with airport and competent authority
- **Evidence:** Article 7 commissioning date vs. actual status
- **Remediation:** Request authority oversight of infrastructure delivery

**Note:** Article 6 strictly applies to SAF; H₂ access issues handled informally via Article 7 monitoring and direct airport engagement.

#### Article 8 Reporting
**Use Case:** Explain operational context in annual report.
- **Example:** "AMPEL360 operations at EHAM benefited from Article 7 H₂ infrastructure operational since Q4 2025. Routes to EDDF delayed pending Article 7 reported commissioning in Q3 2026."

**Benefit:** Demonstrates proactive H₂ infrastructure planning aligned with regulatory framework.

---

## 7. AMPEL360 Infrastructure Requirements

### Technical Specifications for H₂ Airports

**Minimum Airport Capabilities for AMPEL360 Operations:**

| Parameter | Specification | Rationale |
|-----------|---------------|-----------|
| **LH₂ Storage Capacity** | ≥10 tonnes on-site | Support daily operations (multiple refuellings) |
| **Refuelling Flow Rate** | ≥500 kg/hour | Minimize turnaround time |
| **H₂ Purity** | ≥99.95% | Fuel cell contamination tolerance |
| **Pressure** | 3-10 bar (liquid transfer) | AMPEL360 tank inlet specification |
| **Temperature** | −253°C (±2°C) | LH₂ boiling point maintenance |
| **Safety Zone** | 25m exclusion radius | Regulatory safety standard (ICAO, EASA) |
| **Trained Personnel** | Min 4 certified H₂ handlers per shift | 24/7 operations |
| **Emergency Response** | H₂ fire suppression, leak detection | Airport fire/rescue H₂-qualified |

**Verify Against Article 7 Reports:**
- Contact airport to confirm technical details
- Conduct site survey before committing to operations
- Test refuelling procedures during commissioning phase

### Electrical Ground Support (Secondary)

**For Hybrid/Electric Ground Operations:**
- **High-Power Charging:** 350+ kW for ground service equipment (GSE)
- **APU Replacement:** Electric ground power units
- **Synergy:** Article 7 electricity infrastructure supports AMPEL360 ground ops electrification

---

## 8. Advocacy and Policy Engagement

### Industry Representation

**AMPEL360 Role:**
- **Pioneer Operator:** First widebody H₂ commercial aircraft → showcase for Article 7 success
- **Data Provider:** Share operational data with Commission/EASA for Article 18 reviews
- **Standards Development:** Participate in ICAO/EASA H₂ infrastructure standards

**Advocacy Priorities:**
1. **Accelerate Airport Investments:** Advocate for EU funding (CEF, Innovation Fund) for H₂ infrastructure
2. **Standardization:** Harmonize H₂ refuelling interfaces, safety protocols across Union airports
3. **Regulatory Clarity:** Define H₂ aircraft operator obligations analogous to SAF (Articles 3-9)
4. **Article 7 Enhancements:** Request more detailed reporting (e.g., refuelling position counts, redundancy)

**Channels:**
- **IATA:** Airline industry representation
- **A4E (Airlines for Europe):** EU-specific airline advocacy
- **Hydrogen Europe:** Cross-sector H₂ advocacy
- **Direct Commission Engagement:** DG MOVE, DG CLIMA

---

## 9. Risk Mitigation

### Infrastructure Delivery Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Delayed Commissioning** | Route launch postponed | Diversify launch airports; contingency network |
| **Insufficient Capacity** | Limited flight frequency | Secure priority access agreements; demand management |
| **Safety Certification Delays** | Operational restrictions | Engage early with airport & authorities; pre-certify procedures |
| **Cost Overruns → High Pricing** | Uneconomic operations | Lock in pricing via long-term agreements; cost-sharing partnerships |
| **Airport Withdraws Project** | Network disruption | Monitor Article 7 biennial updates; diversify dependencies |

**Contingency Planning:**
- **Backup Airports:** For each Tier 1 airport, identify Tier 2 alternative
- **Fuel Type Flexibility:** If H₂ unavailable, AMPEL360 backup SAF system (requires SAF compliance)
- **Network Flexibility:** Design route network resilient to 1-2 airport H₂ unavailability

---

## 10. Reporting Template

### Article 7 Airport Readiness Tracker (CSV)

**Internal AMPEL360 tracking database:**

```csv
airport_icao,airport_iata,airport_name,country,article7_report_year,h2_project_status,h2_capacity_tonnes_per_year,h2_commissioning_date_planned,h2_commissioning_date_actual,h2_purity_spec,ampel360_tier,ampel360_routes_planned,mou_signed,mou_date,contact_name,contact_email,last_update,notes
EHAM,AMS,Amsterdam Schiphol,NL,2025,Operational,3000,2025-Q4,2025-12-01,99.99%,Tier 1,AMP100-AMP120,Yes,2025-03-15,Jan de Vries,hydrogen@schiphol.nl,2025-12-01,Launch airport; 24/7 refuelling available
EDDF,FRA,Frankfurt Airport,DE,2025,Under construction,5000,2026-Q3,2026-Q3,99.97%,Tier 2,AMP200-AMP230,In negotiation,,Dr. Hans Mueller,h2@fraport.de,2025-11-01,Phase 1 regional; Phase 2 widebody Q3 2026
LFPG,CDG,Paris Charles de Gaulle,FR,2025,Planning,8000,2027-Q2,TBD,99.95%,Tier 2,AMP300-AMP330,No,,Marie Dubois,h2@adp.fr,2025-10-15,Air Liquide partnership; high confidence
EGLL,LHR,London Heathrow,UK,2025,Feasibility,0,2028-Q1,TBD,TBD,Tier 3,Future,No,,Sarah Johnson,hydrogen@heathrow.com,2025-09-20,Study phase; monitor biennial update 2027
LEMD,MAD,Madrid-Barajas,ES,2025,None reported,0,N/A,N/A,N/A,Tier 5,Advocacy target,No,,,,2025-08-10,No H2 plans; advocate for investment
```

**Update Frequency:**
- **Biennial:** Upon new Article 7 reports (Mar 2025, Mar 2027, …)
- **Quarterly:** Operational status checks with Tier 1-2 airports
- **Ad-hoc:** Significant infrastructure milestones (commissioning, capacity expansions)

---

## 11. Integration with EIS and Network Rollout

### Entry Into Service (EIS) Dependency

**AMPEL360 EIS Target:** 2029 (per roadmap)

**Critical Path:**
1. **2025:** Article 7 reports identify H₂-ready airports
2. **2026-2027:** Secure MoUs with Tier 1-2 airports; validate infrastructure
3. **2028:** Certification campaign at launch airports; crew/ground staff training
4. **2029 Q1:** EIS at 2-3 Tier 1 airports (e.g., EHAM, EDDF, LFPG)
5. **2029-2030:** Expand network to additional Article 7-compliant airports

**Risk:** If insufficient Article 7 airports ready by 2029, EIS may delay.

**Mitigation:** Start infrastructure advocacy NOW (2025-2026) to influence airport investment decisions.

### Route Network Phasing

**Phase 1 (2029):** Tier 1 Airports Only
- Amsterdam (EHAM)
- Frankfurt (EDDF) — if Q3 2026 commissioning successful
- 2-3 additional early adopters

**Phase 2 (2030-2031):** Tier 2 Airports
- Paris CDG (LFPG)
- Copenhagen (EKCH)
- Munich (EDDM)

**Phase 3 (2032+):** Tier 3 Airports + New Investments
- London Heathrow (EGLL)
- Madrid (LEMD) — if infrastructure developed
- Vienna, Brussels, etc.

**Strategy:** Align route launches with Article 7 commissioning dates; avoid premature commitments.

---

## 12. Related Documents

- **[02-90-01-000A_README.md](02-90-01-000A_README.md):** Overall compliance framework
- **[02-90-01-001A_Regulatory_Scope.md](02-90-01-001A_Regulatory_Scope.md):** Article 7 detailed analysis
- **[02-90-01-003A_Exemption_Workflow_Art5-3.md](02-90-01-003A_Exemption_Workflow_Art5-3.md):** Use Article 7 data for exemption justifications
- **[02-90-01-002A_Data_Model_Article8.csv](02-90-01-002A_Data_Model_Article8.csv):** Reference H₂ infrastructure in annual report

### Technical Cross-References (T-TECHNOLOGY)
- **ATA 28 (Fuel Systems):** H₂ refuelling interface specs
- **ATA 24 (Electrical Power):** Ground power integration
- **ATA 47 (Inerting):** H₂ safety systems
- **ICD-02-00-28-001:** Airport H₂ infrastructure interface control

### CAOS Integration (N-NEURAL NETWORKS)
- **ATA 95 (DPP):** Ingest Article 7 data for predictive analytics

---

## 13. References

- **Regulation (EU) 2023/2405**, Article 7
- **EASA Article 7 Report Repository** (forthcoming)
- **ICAO Doc 10083** — Guidance on Hydrogen Aviation
- **ISO 21087** — Gas analysis — Analytical methods for hydrogen fuel
- **Hydrogen Europe Aviation Reports** — Industry H₂ infrastructure studies
- **ACI Europe Hydrogen Roadmap** — Airport H₂ deployment strategies

---

## 14. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-12 | AMPEL360 Infrastructure Team | Initial H₂/electricity infrastructure document |

---

**End of H₂ Infrastructure Readiness Document**

For airport readiness tracking template, see CSV format in Section 10 above.
