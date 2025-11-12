# Flight Emissions Label (FEL) Methodology — Article 14

**Document ID:** 02-90-01-006A  
**Version:** 1.0  
**Date:** 2025-11-12  
**Status:** ACTIVE

---

## 1. Purpose

This document defines the methodology for obtaining and displaying **Flight Emissions Labels (FEL)** under **Article 14 of EU Regulation 2023/2405** (ReFuelEU Aviation). It provides AMPEL360-specific procedures for data collection, EASA application, label acquisition, and passenger-facing display.

---

## 2. Regulatory Basis

### Article 14 — Environmental Labelling Scheme

**Article 14(1) — Voluntary Label:**
EASA shall issue FEL at aircraft operator request, showing:
- Expected CO₂ emissions per passenger for a specific route
- CO₂ efficiency per passenger-kilometer
- Validity: ≤1 year per route-period

**Article 14(2) — Methodology:**
Commission implementing acts define:
- Calculation methodology
- Data requirements
- Label format and display templates
- Machine-readable access requirements

**Article 14(3) — Display Obligations:**
Operators choosing to display FEL must:
- Use consistent templates across booking channels
- Provide machine-readable access for price comparison websites
- Update labels annually or when operations change materially

**Purpose:** Empower passengers to choose lower-emission flights; reward operators investing in sustainable fuels and efficient aircraft.

---

## 3. AMPEL360 Strategic Value of FEL

### Marketing Advantage

**AMPEL360 Unique Selling Points:**

1. **Near-Zero Direct CO₂ Emissions**
   - Primary propulsion: Hydrogen fuel cells → byproduct is H₂O (water), not CO₂
   - FEL will show **dramatically lower CO₂ per passenger** vs. conventional aircraft
   
2. **Blended Wing Body Efficiency**
   - 30% lower energy consumption per seat-km (BWB aerodynamics)
   - Translates to lower lifecycle emissions even accounting for H₂ production

3. **Sustainable Backup Systems**
   - Any backup conventional fuel: 100% SAF (compliant with Article 3)
   - Further reduces FEL label values

**Passenger Appeal:**
- Environmentally conscious travelers actively seek low-emission options
- FEL provides **trusted, EASA-verified** metric (not operator marketing claim)
- Booking channel integration → competitive advantage in search/sort results

**Example FEL Display:**

```
┌─────────────────────────────────────────────┐
│  EASA Flight Emissions Label                │
│  ─────────────────────────────────────────  │
│  Route: Amsterdam (AMS) → Frankfurt (FRA)   │
│  Operator: AMPEL360 Aviation                │
│  Flight: AMP102                             │
│  ─────────────────────────────────────────  │
│  CO₂ per passenger: 2.1 kg                  │
│  CO₂ efficiency: 8 g/pax-km                 │
│  ─────────────────────────────────────────  │
│  Valid: 2025-04-01 to 2026-03-31            │
│  Verified by EASA                           │
└─────────────────────────────────────────────┘

Conventional aircraft comparable route: 45 kg CO₂/pax
AMPEL360 advantage: 95% lower emissions
```

### Regulatory Compliance Synergy

**FEL Complements Article 8 Reporting:**
- Uses same fuel/operations data
- Verification process aligned with EU ETS verifier
- Demonstrates commitment to transparency

---

## 4. FEL Calculation Methodology

### Inputs Required

#### A. Fleet Data
| Parameter | AMPEL360 Value | Source |
|-----------|----------------|--------|
| Aircraft type | BWB H₂ Hy-E Q100 | Type Certificate Data Sheet (TCDS) |
| Engine/fuel cell type | PEM fuel cell stacks | ATA 71 (Powerplant) documentation |
| Maximum takeoff weight | [MTOW per TCDS] | ATA 06 (Weight & Balance) |
| Passenger capacity | 220 (nominal config) | ATA 25 (Equipment & Furnishings) |
| Cargo capacity | [kg] | ATA 50 (Cargo Compartments) |

#### B. Route Data
| Parameter | Description | Example (AMS-FRA) |
|-----------|-------------|-------------------|
| Origin airport | ICAO/IATA | EHAM / AMS |
| Destination airport | ICAO/IATA | EDDF / FRA |
| Great circle distance | km | 358 km |
| Flight time | Minutes (block-to-block) | 65 min |
| Frequency | Flights per week | 14 (2x daily) |

#### C. Operational Data
| Parameter | Description | Calculation Basis |
|-----------|-------------|-------------------|
| Average load factor | % seats filled | Historical data (min 6 months) |
| Average cargo load | kg per flight | Historical data |
| Fuel uplift per flight | kg (H₂ + backup fuel) | Fuel logs (Article 8 data) |
| SAF share | % of backup fuel (if any) | Article 8 SAF purchases |

#### D. Fuel Emissions Factors

**Hydrogen:**
- **Direct combustion/use:** 0 gCO₂/MJ (water byproduct)
- **Lifecycle (upstream):** Depends on H₂ production pathway
  - Green H₂ (electrolysis + renewable electricity): 0-10 gCO₂e/MJ
  - Blue H₂ (SMR + CCS): 30-50 gCO₂e/MJ
  - Grey H₂ (SMR, no CCS): 90-100 gCO₂e/MJ

**AMPEL360 Target:** Green H₂ with lifecycle emissions ≤10 gCO₂e/MJ

**SAF (Backup Fuel, if any):**
- Lifecycle emissions per Article 8 data: 15-30 gCO₂e/MJ (typical HEFA SAF)
- Direct combustion: 73.4 gCO₂/MJ (same as Jet-A, but offset by lifecycle savings)

**Conventional Jet-A (Comparison):**
- Lifecycle: ~88 gCO₂e/MJ (incl. extraction, refining, transport)

#### E. Verification Data
| Parameter | Description |
|-----------|-------------|
| Verification body | EU ETS accredited verifier |
| Verification statement | URI to signed statement |
| Data period | 6-12 months of operations |

---

### Calculation Formula (Simplified)

**Per Commission Implementing Acts (methodology pending full publication):**

**Step 1: Total Energy Consumption**
```
E_total (MJ) = (H₂_uplift_kg × H₂_LHV_MJ/kg) + (SAF_uplift_kg × SAF_LHV_MJ/kg)
```
Where:
- H₂ Lower Heating Value (LHV) ≈ 120 MJ/kg
- SAF LHV ≈ 43 MJ/kg (similar to Jet-A)

**Step 2: Lifecycle CO₂ Emissions**
```
CO₂_total (kg) = (E_H₂ × LCA_H₂_gCO₂e/MJ / 1000) + (E_SAF × LCA_SAF_gCO₂e/MJ / 1000)
```

**Step 3: Passenger Allocation**
```
CO₂_per_pax (kg) = CO₂_total / (pax_count + (cargo_kg / 100))
```
Note: Cargo allocation factor adjusts for belly freight (methodology defined by Commission)

**Step 4: Efficiency Metric**
```
CO₂_efficiency (g/pax-km) = (CO₂_per_pax × 1000) / distance_km
```

---

### AMPEL360 Example Calculation

**Route:** Amsterdam (AMS) → Frankfurt (FRA)  
**Distance:** 358 km  
**Aircraft:** AMPEL360 BWB H₂ Hy-E Q100  
**Load Factor:** 85% (187 passengers)  
**Cargo:** 2,000 kg  

**Fuel:**
- H₂ uplift: 250 kg (green H₂, LCA = 8 gCO₂e/MJ)
- Backup SAF: 0 kg (primary H₂ sufficient)

**Calculation:**

```
E_total = 250 kg × 120 MJ/kg = 30,000 MJ

CO₂_total = 30,000 MJ × 8 gCO₂e/MJ / 1000 = 240 kg CO₂e (lifecycle)

pax_equivalent = 187 + (2000 / 100) = 207

CO₂_per_pax = 240 kg / 207 = 1.16 kg CO₂e/pax

CO₂_efficiency = 1.16 kg × 1000 / 358 km = 3.24 g/pax-km
```

**Comparison:**
- **Conventional aircraft (same route):** ~45 kg CO₂/pax, ~125 g/pax-km
- **AMPEL360 advantage:** 97% lower CO₂ per pax, 97% lower efficiency metric

**FEL Display Value:**
- **CO₂ per passenger:** 1.2 kg (rounded)
- **CO₂ efficiency:** 3.2 g/pax-km (rounded)

---

## 5. FEL Application Process

### Step 1: Data Collection (Months 1-3)

**Responsible:** AMPEL360 Operations & Compliance Teams

**Actions:**
1. **Compile Historical Data:** Minimum 6 months operations on target route
   - Fuel uplift logs (from Article 8 system)
   - Load factors (passenger and cargo)
   - Flight times and frequencies
2. **H₂ Lifecycle Verification:** Obtain supplier declaration on green H₂ production pathway and lifecycle emissions
3. **SAF Data (if applicable):** Pull from Article 8 SAF purchase records
4. **Fleet Technical Specs:** TCDS, fuel cell efficiency, weights

**Output:** FEL Input Dataset

**Template:** [02-90-01-A001_Templates/FEL_Input_Dataset_Template.xlsx](02-90-01-A001_Templates/FEL_Input_Dataset_Template.xlsx)

**CSV Format:**

```csv
season,route_code,origin_icao,destination_icao,aircraft_type,avg_pax,avg_cargo_kg,fuel_h2_kg,fuel_saf_kg,saf_share_pct,h2_lca_gCO2e_MJ,saf_lca_gCO2e_MJ,flights_count,data_period_start,data_period_end
Summer 2025,AMP102,EHAM,EDDF,BWB-H2-Q100,187,2000,250,0,0,8.0,0,364,2024-10-01,2025-03-31
Winter 2025,AMP102,EHAM,EDDF,BWB-H2-Q100,175,1800,245,0,0,8.0,0,182,2025-04-01,2025-09-30
```

### Step 2: Verification (Month 4)

**Responsible:** EU ETS Accredited Verifier

**Process:**
1. **Verifier Engagement:** Contract with same verifier used for Article 8 reporting (efficiency)
2. **Data Audit:** Verifier checks:
   - Fuel logs accuracy
   - Load factor calculations
   - H₂ supplier lifecycle emissions certificates
   - Calculation methodology per Commission implementing acts
3. **Verification Statement:** Verifier issues signed statement confirming data accuracy

**Deliverable:** Verification Statement (PDF) with unique ID and URI

### Step 3: EASA Application (Month 5)

**Responsible:** AMPEL360 Compliance Team

**Submission:**
1. **Portal Access:** Log in to EASA ReFuelEU Portal → FEL Module
2. **Application Form:** Complete fields:
   - Operator details (ICAO, AOC number, legal entity)
   - Route details (origin, destination, flight numbers)
   - Period covered (start/end dates, typically 12 months forward)
   - FEL dataset upload (CSV or Excel per EASA template)
   - Verification statement (PDF upload + URI)
3. **Fee Payment:** (Amount TBD by EASA; estimated €500-2000 per route-season)
4. **Submit:** Review and submit application

**Timeline:** EASA processes within **30 days** (target per draft procedures)

### Step 4: EASA Review & Label Issuance (Month 6)

**EASA Actions:**
1. **Completeness Check:** Verify all required data submitted
2. **Methodology Validation:** Confirm calculations per Commission implementing acts
3. **Verification Review:** Accept or request additional information from verifier
4. **Label Generation:** Issue FEL with:
   - CO₂ per passenger (kg)
   - CO₂ efficiency (g/pax-km)
   - Validity period (≤12 months)
   - EASA seal/authentication code

**Outcome:**
- **Approved:** Receive FEL certificate (PDF) + machine-readable data file (JSON/XML)
- **Rejected:** Receive reasons; correct data and resubmit
- **Clarification Requested:** Provide additional info within 10 days

**Deliverables:**
- FEL Certificate (PDF for display)
- Machine-readable FEL data (JSON/XML for booking systems)
- EASA authentication URI (for passenger verification)

### Step 5: Display Implementation (Month 7 onward)

**Responsible:** AMPEL360 Marketing & IT Teams

**Booking Channels:**
1. **Airline Website:** Embed FEL in flight search results and booking confirmation
2. **GDS (Amadeus, Sabre, Travelport):** Upload FEL data via GDS messaging
3. **Meta-Search Engines:** Provide machine-readable FEL via API (e.g., Skyscanner, Google Flights)
4. **Travel Agents:** Include FEL in PNR remarks and e-ticket confirmations

**Display Requirements (Article 14(3)):**

#### Consistent Template
- Must use EASA-approved display format (color scheme, layout, fonts)
- No alterations or embellishments beyond template

#### Prominent Placement
- Flight search results: Show FEL alongside price, duration
- Booking page: Display before payment confirmation
- E-ticket: Include FEL summary

#### Machine-Readable Access
- JSON/XML feed accessible via public API
- Standard schema per EASA specification
- Updated within 24 hours of FEL issuance/expiry

**Example Booking Page Display:**

```html
<div class="flight-emissions-label">
  <img src="easa-fel-logo.png" alt="EASA Flight Emissions Label" />
  <p><strong>CO₂ per passenger:</strong> 1.2 kg</p>
  <p><strong>Efficiency:</strong> 3.2 g CO₂ per pax-km</p>
  <p><small>Verified by EASA | Valid until 2026-03-31</small></p>
  <a href="https://fel.easa.europa.eu/verify/AMP102-2025">Verify Label</a>
</div>
```

---

## 6. Label Maintenance & Updates

### Annual Renewal (Standard)

**Timeline:**
- **9 months before expiry:** Begin data collection for renewal
- **6 months before expiry:** Submit renewal application to EASA
- **3 months before expiry:** Receive renewed FEL
- **Before expiry:** Update all booking channels

**Process:** Same as initial application (Steps 1-5 above)

### Material Change Triggers

**Must Update FEL If:**
- Aircraft type change (e.g., upgrade to Q200 model)
- Fuel source change (e.g., switch from green H₂ to blue H₂)
- Route characteristics change materially (>20% distance change, major load factor shift)
- SAF share changes significantly (>10 percentage points)

**Timeline:** Submit update application within **30 days** of change; cease displaying old FEL immediately upon material change.

### Expiry Handling

**Upon Expiry:**
- Remove FEL from all booking channels
- Display "Emissions data pending renewal" or equivalent
- Do not display expired FEL (regulatory non-compliance)

---

## 7. AMPEL360 Competitive Differentiation

### Marketing Strategies

#### Highlight Hydrogen Advantage
**Message:** "AMPEL360: The only widebody airliner with near-zero CO₂ emissions (EASA verified)"

**Channels:**
- Airline website homepage
- Social media campaigns
- Press releases at FEL launch
- Industry conferences (IATA, Routes Europe, etc.)

#### Passenger Education
**Content:**
- Explainer videos: "What is the Flight Emissions Label?"
- Infographics: AMPEL360 vs. conventional aircraft CO₂ comparison
- Blog posts: "How we achieve 97% lower emissions"

**Call to Action:** "Choose AMPEL360 for guilt-free flying"

#### Corporate Travel Partnerships
**Target:** Companies with net-zero commitments
- Offer corporate travel accounts with emissions tracking
- Quarterly reports: "Your company saved X tonnes CO₂ by flying AMPEL360"
- B2B marketing: FEL as differentiator in RFPs

#### Loyalty Program Integration
**Benefit:** Reward environmentally conscious passengers
- Bonus miles for FEL-labeled flights
- "Green Tier" status for frequent AMPEL360 flyers
- Carbon offset credits (even though AMPEL360 near-zero)

---

## 8. Validation & Compliance

### Internal Checks (Pre-Submission)

**Quality Assurance:**
- Cross-check FEL dataset with Article 8 reporting data (fuel, flights, airports)
- Validate H₂ lifecycle emissions against supplier certificates
- Recalculate CO₂ per pax independently (avoid arithmetic errors)
- Legal review of FEL display compliance (templates, placement)

**Responsible:** AMPEL360 IV&V (Independent Verification & Validation) Team

### CI/CD Integration

**Automated Checks:**
- FEL dataset schema validation (correct columns, data types)
- H₂ LCA value within acceptable range (0-15 gCO₂e/MJ for green H₂)
- Load factor reasonability check (50-100%)
- Fuel uplift vs. distance correlation (physics-based bounds)

**Tool:** See [02-90-01-007A_CI_Validation_Rules.md](02-90-01-007A_CI_Validation_Rules.md)

### EASA Audits

**Ongoing Compliance:**
- EASA may audit FEL data accuracy post-issuance
- Operators must retain supporting documentation for 3 years
- Penalties for intentional misrepresentation (fines, label revocation)

**AMPEL360 Preparedness:**
- Archive all FEL applications, verifier reports, fuel logs
- Maintain traceability to source systems (flight ops database, fuel management)
- Annual internal audit of FEL processes

---

## 9. Cost-Benefit Analysis

### Costs

| Item | Estimate (per route-season) | Notes |
|------|----------------------------|----|
| Data collection & compilation | €1,000 - €2,000 | Internal staff time |
| Verification (if separate from Art. 8) | €500 - €1,500 | May bundle with Article 8 |
| EASA application fee | €500 - €2,000 | TBD by EASA |
| IT implementation (one-time) | €10,000 - €50,000 | Booking system integration |
| Annual maintenance | €500/route | Updates, renewals |

**Total Initial Investment:** ~€15,000 - €60,000 (all routes)  
**Ongoing Annual:** ~€2,000 - €5,000 per route

### Benefits

| Benefit | Value | Rationale |
|---------|-------|-----------|
| **Passenger Preference** | +5-10% load factor | Studies show 10-15% willingness to pay premium for low-emission flights |
| **Premium Pricing** | +€5-10 per ticket | Environmental surcharge accepted by eco-conscious travelers |
| **Corporate Contracts** | +20-30% B2B revenue | Net-zero corporate travel mandates |
| **Brand Reputation** | Intangible | Positions AMPEL360 as sustainability leader |
| **Regulatory Goodwill** | Intangible | Demonstrates proactive compliance |

**ROI:** Likely positive within 1-2 years for high-frequency routes.

---

## 10. Related Documents

- **[02-90-01-000A_README.md](02-90-01-000A_README.md):** Overall compliance framework
- **[02-90-01-001A_Regulatory_Scope.md](02-90-01-001A_Regulatory_Scope.md):** Article 14 detailed analysis
- **[02-90-01-002A_Data_Model_Article8.csv](02-90-01-002A_Data_Model_Article8.csv):** Fuel data source for FEL
- **[02-90-01-007A_CI_Validation_Rules.md](02-90-01-007A_CI_Validation_Rules.md):** Automated FEL dataset checks
- **Template:** [FEL_Input_Dataset_Template.xlsx](02-90-01-A001_Templates/FEL_Input_Dataset_Template.xlsx)

---

## 11. References

- **Regulation (EU) 2023/2405**, Article 14
- **Commission Implementing Acts** (forthcoming) — FEL methodology, display templates
- **EASA FEL Portal** — Application procedures and technical specs
- **ICAO CORSIA** — Complementary emissions labelling schemes
- **ISO 14067** — Carbon footprint of products (lifecycle methodology principles)

---

## 12. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-12 | AMPEL360 Compliance & Marketing Teams | Initial FEL methodology document |

---

**End of FEL Methodology Document**

For FEL input dataset template, see: [02-90-01-A001_Templates/FEL_Input_Dataset_Template.xlsx](02-90-01-A001_Templates/FEL_Input_Dataset_Template.xlsx)
