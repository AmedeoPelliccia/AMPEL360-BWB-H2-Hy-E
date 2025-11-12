# ReFuelEU Aviation — Regulatory Scope & Article Breakdown

**Document ID:** 02-90-01-001A  
**Version:** 1.0  
**Date:** 2025-11-12  
**Status:** ACTIVE

---

## 1. Introduction

This document provides a detailed article-by-article breakdown of **EU Regulation 2023/2405** (ReFuelEU Aviation) as it applies to AMPEL360 aircraft operations. It serves as the authoritative reference for understanding operator obligations, timelines, and compliance requirements.

---

## 2. Regulation Overview

### Full Citation
**Regulation (EU) 2023/2405 of the European Parliament and of the Council** of 18 October 2023 on ensuring a level playing field for sustainable air transport.

### Entry into Force
- **Published:** 31 October 2023
- **Entry into Force:** 20 November 2023
- **Application Start:** 1 January 2025

### Objectives
1. Ensure minimum shares of sustainable aviation fuels (SAF) at Union airports
2. Prevent fuel tankering that undermines environmental benefits
3. Establish transparent environmental labelling for passengers
4. Support hydrogen and electricity infrastructure development
5. Create harmonized reporting and verification framework

---

## 3. Article-by-Article Analysis

### Article 1 — Subject Matter and Scope

**Scope:** Applies to:
- Aircraft operators with >700 tonne fuel annual consumption at Union airports
- Union airports with >1 million passengers or >100,000 tonnes cargo annually
- Fuel suppliers operating at Union airports

**AMPEL360 Impact:**
- As a commercial aircraft program, AMPEL360 operators fall within scope
- Hydrogen propulsion adds specific considerations under Article 7
- SAF requirements apply to any conventional fuel backup systems

---

### Article 2 — Definitions

Key terms for AMPEL360 operations:

| Term | Definition | AMPEL360 Context |
|------|------------|------------------|
| **Aviation fuel** | Kerosene, sustainable aviation fuel, synthetic aviation fuel, or hydrogen | Primarily H₂; SAF for backup/hybrid modes |
| **Sustainable aviation fuel (SAF)** | Drop-in fuel from renewable sources per RED II | Required for any conventional fuel component |
| **Union airport** | Airport in EU Member State or associated country | All AMPEL360 EU routes |
| **Yearly aviation fuel required** | Total fuel needed for all flights from Union airport | Calculated per airport annually |
| **Tanking** | Refuelling beyond immediate flight needs | Prohibited except safety cases |

**Note:** Hydrogen is explicitly recognized as aviation fuel, making AMPEL360's H₂ propulsion fully compliant.

---

### Article 3 — Minimum Shares of SAF

**Requirement:** Fuel suppliers must ensure SAF availability at minimum percentages:

| Year | Min. SAF % | Min. Synthetic % | AMPEL360 Notes |
|------|------------|------------------|----------------|
| 2025 | 2% | — | Backup systems only |
| 2030 | 6% | 1.2% | |
| 2035 | 20% | 5% | Synthetic SAF mandatory |
| 2040 | 34% | 10% | |
| 2045 | 42% | 15% | |
| 2050 | 70% | 35% | Full decarbonization target |

**AMPEL360 Strategy:**
- Primary propulsion: 100% hydrogen (zero carbon at point of use)
- Backup/auxiliary systems: Comply with SAF minimums if conventional fuel used
- Lifecycle emissions advantage: H₂ production pathway optimized

---

### Article 4 — Exemptions for SAF Obligations

**Applicability:** Limited exemptions for:
- Regional connectivity (< 270,000 movements annually)
- Force majeure situations
- Technical supply impossibilities

**AMPEL360 Application:**
- Main operations: No exemptions expected (H₂ primary)
- Backup fuel: Standard SAF requirements apply
- Remote airports: May request exemptions for backup fuel access

---

### Article 5 — Refuelling Obligations (Tanking Prevention)

#### Article 5(1) — General Rule

**Requirement:**  
Operators must uplift ≥90% of yearly aviation fuel required at each Union airport where they operate.

**Purpose:**  
Prevent fuel tankering (carrying extra fuel to avoid refuelling at higher-cost airports), which increases emissions and undermines SAF adoption.

**AMPEL360 Implementation:**
- H₂ refuelling planned at each operational airport
- No tankering incentive due to weight penalties (H₂ volume-constrained)
- Compliance tracking via Article 8 reporting

#### Article 5(2) — Safety Exceptions

**Permitted:**  
Refuelling away from destination airport if justified by:
- Safety considerations
- Operational constraints

**Documentation Required:**
- Routes and reasons for non-standard refuelling
- Included in Article 8 annual report

**AMPEL360 Procedure:**
- Safety cases documented in operations manual
- Pre-approved scenarios (e.g., inadequate H₂ infrastructure, emergency diversion)
- Reported in `notes_routes_impacted_article5_2` field

#### Article 5(3) — Temporary Exemptions

**Process:**
1. Operator applies to competent authority
2. Justification: Short routes where 90% rule creates undue operational burden
3. Commission guidelines (09 Oct 2024) specify acceptable evidence
4. Limited duration; subject to renewal

**AMPEL360 Workflow:**  
See [02-90-01-003A_Exemption_Workflow_Art5-3.md](02-90-01-003A_Exemption_Workflow_Art5-3.md)

---

### Article 6 — Access to SAF (Difficulties Reporting)

**Requirement:**  
Operators must report difficulties in accessing sufficient SAF quantities or qualities to competent authority.

**Authority Response:**
1. Investigate airport fuel supply arrangements
2. Request evidence from airport/fuel suppliers
3. Mandate corrective actions if supply deficiency confirmed

**AMPEL360 Application:**
- Monitor H₂ availability (Article 7 related but distinct)
- Report SAF access issues for any backup fuel systems
- Coordinate with airport partners for green H₂ supply

**Workflow:**  
See [02-90-01-004A_SAF_Access_Difficulties_Art6.md](02-90-01-004A_SAF_Access_Difficulties_Art6.md)

---

### Article 7 — Hydrogen and Electricity Infrastructure

#### Article 7(1) — Airport Reporting Obligation

**Requirement:**  
Union airports shall report to competent authority (first by **31 Mar 2025**, then biennially):
- Ongoing or planned H₂/electric infrastructure projects
- Estimated annual hydrogen/electricity supply capacity
- Expected commissioning dates

**Purpose:**  
Enable operators and authorities to plan hydrogen aircraft deployment.

#### Article 7(2) — Information Sharing

**Requirement:**  
Competent authorities provide airport reports to:
- European Commission
- EASA
- Interested aircraft operators

**AMPEL360 Impact:**
- **CRITICAL INPUT** for operations planning and route network design
- Identifies airports ready for AMPEL360 H₂ operations
- Informs partnership and infrastructure investment decisions

**Integration:**  
See [02-90-01-005A_H2_Electricity_Report_Art7.md](02-90-01-005A_H2_Electricity_Report_Art7.md)  
Cross-reference: **T-TECHNOLOGY / E2-ENERGY** (ATA 24, 28, 47) and **C2-CRYOGENICS** (ATA 28)

---

### Article 8 — Reporting by Aircraft Operators

#### Article 8(1) — Annual Report Content (Annex II)

**Deadline:** **31 March** each year (covering previous calendar year)

**Required Data:**

##### (a) Per Union Airport
- ICAO/IATA airport codes
- Total fuel uplifted (tonnes)
- Yearly fuel required (tonnes)
- Fuel not uplifted (tonnes) — tanking prevention tracking
- Fuel tanked for safety reasons (tonnes)

##### (b) Flight Operations
- Total number of flights departing from Union airports
- Total flight hours

##### (c) SAF Purchases
For each SAF purchase batch:
- Supplier name and contact
- Quantity purchased (tonnes)
- Conversion process (HEFA, FT, AtJ, etc.)
- Feedstock type(s)
- Country of feedstock origin
- Lifecycle greenhouse gas emissions (gCO₂e/MJ)

##### (d) SAF Batch Composition
- Aromatics content (vol %)
- Naphthalenes content (vol %)
- Sulphur content (mass %)

##### (e) Additional Information
- Routes impacted by safety tanking (Art. 5(2))
- Any other relevant operational notes

#### Article 8(2) — Verification

**Requirement:**  
Report must be verified by accredited verifier in accordance with **EU ETS Articles 14-15**.

**AMPEL360 Process:**
1. Compile data using template ([02-90-01-002A_Data_Model_Article8.csv](02-90-01-002A_Data_Model_Article8.csv))
2. Submit to accredited verifier
3. Obtain verification statement
4. Submit verified report + statement to competent authority by 31 March
5. Attach verification URI: `verification_statement_uri`

#### Article 8(3) — Penalties for Non-Compliance

**Consequences:**
- Administrative fines
- Operating restrictions
- Potential loss of slots at Union airports

**AMPEL360 Mitigation:**
- Automated CI/CD validation ([02-90-01-007A_CI_Validation_Rules.md](02-90-01-007A_CI_Validation_Rules.md))
- Early warning system for missing data
- Quarterly internal compliance reviews

---

### Article 9 — Use of SAF for Compliance

#### Article 9(1) — SAF Eligibility

**Requirement:**  
SAF counted toward compliance must:
- Comply with sustainability criteria (RED II)
- Meet aviation fuel quality standards
- Be physically delivered and used

**No book-and-claim:** SAF must be uplifted at the airport where counted (unlike some carbon markets).

#### Article 9(2) — Supplier Information Deadline

**Requirement:**  
Fuel suppliers must provide SAF characteristics to operators by **14 February** annually.

**Content:**
- Conversion process
- Feedstock
- Origin
- Lifecycle emissions
- Batch quality data

**AMPEL360 Coordination:**
- Contractual requirement for suppliers
- Data ingestion into DPP/CAOS (ATA 95)
- Validation against Article 8 report

#### Article 9(3) — No Double-Claiming

**Prohibition:**  
SAF used for ReFuelEU compliance cannot be simultaneously claimed under:
- EU ETS
- CORSIA
- Other national/international GHG reduction schemes

**Enforcement:**
- Unique `saf_purchase_id` in Article 8 data model
- Cross-scheme registry checks
- Verification body audits

**AMPEL360 Validation:**  
CI/CD checks for duplicate SAF purchase IDs across schemes (see [02-90-01-007A_CI_Validation_Rules.md](02-90-01-007A_CI_Validation_Rules.md))

---

### Article 10 — Information Provided by Fuel Suppliers

**Requirement:**  
Fuel suppliers must disclose to authorities (first by **28 Feb 2025**, then annually):
- Total aviation fuel supplied per Union airport
- SAF quantities and characteristics
- Synthetic SAF quantities
- Batch-level sustainability and quality data

**AMPEL360 Relevance:**
- Cross-validation with operator Article 8 reports
- Ensures supplier accountability
- Supports audit trail for SAF claims

---

### Article 11 — Accreditation of Voluntary Schemes

**Purpose:**  
Establish recognition process for voluntary SAF certification schemes (similar to RED II).

**AMPEL360 Impact:**
- Accept only EU-recognized SAF certification
- Due diligence on supplier certifications
- Audit trail for lifecycle emissions claims

---

### Article 12 — Assistance to Aircraft Operators

**Provision:**  
Member States may provide support to aircraft operators for:
- SAF cost premiums
- Hydrogen infrastructure investments
- Training and capacity building

**AMPEL360 Opportunities:**
- Apply for national/EU funding programs
- Public-private partnerships for H₂ infrastructure
- Innovation grants for first-of-kind aircraft

---

### Article 13 — Penalties

**Member State Obligation:**  
Establish penalties for non-compliance that are:
- Effective
- Proportionate
- Dissuasive

**Typical Penalties:**
- Administrative fines (€ per tonne non-compliant fuel)
- Operating restrictions
- Reputational damage

**AMPEL360 Risk Mitigation:**
- Proactive compliance culture
- Automated validation systems
- Internal audits ahead of external verification

---

### Article 14 — Environmental Labelling Scheme (FEL)

#### Article 14(1) — Label Issuance

**Authority:** EASA issues voluntary Flight Emissions Labels (FEL) at operator request.

**Validity:** ≤1 year per route-period.

**Content:**
- Expected CO₂ emissions per passenger
- CO₂ efficiency per passenger-kilometer
- Based on fleet, route, load factors, fuel type, SAF share

#### Article 14(2) — Methodology

**Commission Implementing Acts:** Define calculation methodology, data requirements, and label format.

**AMPEL360 Advantage:**
- Hydrogen propulsion: near-zero direct CO₂ emissions
- SAF share in backup systems: further reduces label values
- Blended Wing Body efficiency: lower per-pax energy consumption

**Strong marketing tool:** AMPEL360 FEL will show dramatically lower emissions vs. conventional aircraft.

#### Article 14(3) — Display Requirements

**Obligation:** Operators displaying FEL must:
- Use consistent templates
- Show label in booking channels
- Provide machine-readable access for aggregators
- Update annually or when operations change materially

**AMPEL360 Implementation:**  
See [02-90-01-006A_FEL_Method_Art14.md](02-90-01-006A_FEL_Method_Art14.md)

---

### Article 15 — Collection and Exchange of Information

**EASA Role:**
- Centralize ReFuelEU data from Member States
- Publish aggregated statistics
- Monitor compliance trends
- Inform policy review

**Data Sources:**
- Operator Article 8 reports
- Supplier Article 10 disclosures
- Airport Article 7 H₂/electricity reports
- Competent authority enforcement actions

**AMPEL360 Transparency:**
- Contribute to industry benchmarking
- Demonstrate hydrogen aircraft viability
- Support policy advocacy for H₂ infrastructure

---

### Article 16 — Competent Authorities

**Designation:**  
Each Member State designates competent authority(ies) for:
- Operator reporting oversight
- Verification approval
- Exemption decisions (Art. 5(3))
- Penalty enforcement

**AMPEL360 Coordination:**
- Identify relevant authority per operating base
- Establish reporting workflows
- Maintain authority contact registry

---

### Article 17 — Delegated Acts

**Commission Powers:**  
Adopt delegated acts to:
- Adjust SAF minimum shares (Art. 3)
- Update Annexes (e.g., reporting templates)
- Respond to technological developments

**AMPEL360 Monitoring:**
- Track Commission delegated act proposals
- Participate in stakeholder consultations
- Update compliance procedures accordingly

---

### Article 18 — Review and Reporting

**Commission Obligation:**  
Review Regulation by **1 Jan 2028** and every 5 years thereafter.

**Review Scope:**
- SAF availability and pricing
- Hydrogen infrastructure readiness
- Tanking prevention effectiveness
- Labelling scheme uptake

**AMPEL360 Input:**
- Provide operational data for hydrogen aircraft category
- Advocate for H₂-specific provisions
- Share lessons learned from first-of-kind operations

---

## 4. Annexes

### Annex I — Eligible SAF Feedstocks

List of renewable feedstocks and conversion processes qualifying as SAF (aligned with RED II Annex IX):

**Part A — Feedstocks:**
- Used cooking oil
- Animal fats (categories 1, 2, 3)
- Municipal solid waste (non-recyclable)
- Agricultural residues
- Forestry residues

**Part B — Advanced Feedstocks:**
- Algae
- Waste biomass
- CO₂ captured from atmosphere/industrial processes (for synthetic fuels)

**AMPEL360 Note:**  
Synthetic SAF from green H₂ + captured CO₂ (Power-to-Liquid) is eligible and increasingly relevant.

---

### Annex II — Operator Reporting Template

**Full data model implemented in:**  
[02-90-01-002A_Data_Model_Article8.csv](02-90-01-002A_Data_Model_Article8.csv)

**Template fields align with Article 8(1) requirements:**
- Airport-level fuel data
- Flight operations
- SAF purchases and batch characteristics
- Verification statement reference

---

## 5. Implementation Timeline

| Date | Milestone | AMPEL360 Action |
|------|-----------|-----------------|
| **1 Jan 2025** | Regulation application begins | Establish reporting workflows |
| **14 Feb 2025** | First supplier SAF data deadline | Coordinate with fuel suppliers |
| **31 Mar 2025** | First operator report due (2024 data) | Submit Article 8 report + verification |
| **31 Mar 2025** | First airport H₂/electricity reports | Review for ops planning |
| **1 Jan 2026** | 2% SAF minimum (backup systems) | Ensure backup fuel compliance |
| **1 Jan 2030** | 6% SAF minimum; 1.2% synthetic | Adjust procurement strategies |
| **1 Jan 2028** | First Commission review | Provide H₂ aircraft operational data |

---

## 6. AMPEL360-Specific Considerations

### Hydrogen Propulsion Advantage

**Article 7 Alignment:**  
AMPEL360's H₂ propulsion makes it a **showcase case** for Article 7 infrastructure reporting. Operators will actively use airport H₂ readiness data to plan route network.

**Tanking Prevention (Art. 5):**  
H₂ volume constraints naturally discourage tankering; compliance straightforward.

**SAF Obligations (Art. 3):**  
Apply only to backup/auxiliary conventional fuel systems, if any. Primary propulsion exempt (zero fossil fuel).

### Flight Emissions Label (Art. 14)

**Marketing Advantage:**  
AMPEL360 FEL will show:
- **Near-zero direct CO₂ per passenger** (H₂ combustion → H₂O)
- **Superior efficiency** (BWB aerodynamics + fuel cell efficiency)
- **Positive differentiation** vs. conventional aircraft

**Booking Channel Integration:**  
Prominently display FEL in GDS, airline websites, and meta-search engines to attract environmentally conscious travelers.

### Data Integration

**CAOS / ATA 95 DPP Linkage:**
- Automate Article 8 data collection from operational systems
- Integrate supplier SAF packets (Art. 9) into digital twin
- Real-time compliance dashboards
- Predictive analytics for fuel procurement optimization

---

## 7. Compliance Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Late Article 8 submission | Low | High | Automated CI/CD, early internal deadlines |
| SAF supplier data delay | Medium | Medium | Contractual deadlines; backup suppliers |
| H₂ infrastructure gaps | Medium | High | Article 7 monitoring; contingency plans |
| Verification rejection | Low | High | Quarterly pre-audits; accredited verifier early engagement |
| Double-claiming SAF | Very Low | Very High | Unique IDs; cross-scheme validation |
| Exemption denial | Low | Medium | Strong evidence per Commission guidelines |

---

## 8. References

### Primary Legislation
- **Regulation (EU) 2023/2405** — ReFuelEU Aviation  
  [EUR-Lex Link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2405)

### Related Directives
- **Directive (EU) 2018/2001** (RED II) — Renewable Energy Directive  
- **EU ETS Directive 2003/87/EC** (as amended) — Emissions Trading System

### Implementing Acts
- Commission Delegated Regulation (forthcoming) — FEL methodology
- Commission Implementing Regulation (forthcoming) — Reporting templates
- Article 5(3) Exemption Guidelines (09 Oct 2024)

### EASA Guidance
- EASA ReFuelEU MRV Portal User Guide
- Verifier Accreditation Requirements
- FEL Application Procedures

### Industry Resources
- IATA ReFuelEU Aviation Toolkit
- ICAO CAEP SAF Framework
- Airline operators' best practices (IATA, A4E, etc.)

---

## 9. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-12 | AMPEL360 Compliance Team | Initial regulatory scope document |

---

**End of Regulatory Scope Document**

For operational workflows and data models, refer to:
- [02-90-01-000A_README.md](02-90-01-000A_README.md) — Overview
- [02-90-01-002A_Data_Model_Article8.csv](02-90-01-002A_Data_Model_Article8.csv) — Article 8 schema
- [02-90-01-003A to 007A] — Detailed procedures
