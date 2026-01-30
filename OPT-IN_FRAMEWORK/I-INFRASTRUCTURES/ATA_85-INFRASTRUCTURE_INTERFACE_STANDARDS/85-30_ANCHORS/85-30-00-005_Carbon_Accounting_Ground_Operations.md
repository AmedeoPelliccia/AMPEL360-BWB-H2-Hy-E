# 85-30-00-005 Carbon Accounting Ground Operations

## Document Information

- **Document ID**: 85-30-00-005
- **Title**: Carbon Accounting for Ground Operations
- **Version**: 1.0
- **Date**: 2025-11-21
- **Status**: Draft
- **Category**: Technical Specification
- **ATA Chapter**: 85 - Infrastructure Interface Standards
- **Bucket**: 30 - Circularity

## Purpose

This document establishes the methodology, scope, and procedures for comprehensive carbon accounting of all ground operations supporting the AMPEL360 BWB aircraft. It ensures accurate measurement, transparent reporting, and continuous reduction of greenhouse gas (GHG) emissions from infrastructure systems throughout the aircraft turnaround cycle.

## Scope

Carbon accounting covers all GHG emissions from:

- **Ground Support Equipment (GSE)**: Tugs, loaders, GPUs, baggage handling, de-icing
- **Hydrogen Infrastructure**: Production, storage, distribution, refueling operations
- **CO₂ Battery Systems**: Charging, thermal management, swap operations
- **Airport Interface Equipment**: Passenger boarding bridges, stands, environmental control units
- **Facilities**: Terminal buildings, hangars, workshops supporting BWB operations
- **Ground Transportation**: Employee shuttles, cargo vehicles, service vehicles

**Temporal Scope**: Cradle-to-grave lifecycle including embodied emissions (manufacturing, transport) and operational emissions.

**Geographic Scope**: Initially AMPEL360 launch airports, expanding to full operational network.

## Regulatory and Standards Context

### GHG Accounting Standards

This framework complies with:

**[GHG Protocol Corporate Standard](https://ghgprotocol.org/corporate-standard)**:
- Globally recognized framework for corporate GHG inventories
- Defines Scope 1, 2, 3 emission categories
- Establishes principles: relevance, completeness, consistency, transparency, accuracy

**[GHG Protocol Scope 3 Standard](https://ghgprotocol.org/standards/scope-3-standard)**:
- Detailed guidance on value chain (Scope 3) emissions
- Applies to upstream (equipment manufacturing, H₂ production) and downstream (waste processing) activities

**[ISO 14064-1:2018](https://www.iso.org/standard/66453.html)**: Specification with guidance at the organization level for quantification and reporting of GHG emissions and removals

**[PAS 2060:2014](https://www.bsigroup.com/en-GB/PAS-2060-Carbon-Neutrality/)**: Specification for the demonstration of carbon neutrality

### Aviation-Specific Guidance

**[ICAO Carbon Offsetting and Reduction Scheme for International Aviation (CORSIA)](https://www.icao.int/environmental-protection/CORSIA/Pages/default.aspx)**:
- Requires monitoring, reporting, verification (MRV) of CO₂ emissions
- Ground operations emissions may be in scope depending on boundary definition

**[ACI Airport Carbon Accreditation](https://www.aci.aero/about-aci/priorities/environment/airport-carbon-accreditation/)**:
- Airport-specific carbon management program with 4+ certification levels
- Level 3+ requires Scope 3 emissions management (including airline GSE at airport)

**[SAF GHG Accounting](https://www.icao.int/environmental-protection/CORSIA/Pages/CORSIA-Eligible-Fuels.aspx)**:
- Lifecycle assessment methodology for sustainable aviation fuels (SAF)
- Analogous approach applied to green hydrogen assessment

## Emission Scopes and Boundaries

### Scope 1: Direct Emissions

**Definition**: GHG emissions from sources owned or controlled by AMPEL360 or airport operator.

**Infrastructure Sources**:
- **Fossil Fuel Combustion**:
  - Diesel GSE (tugs, loaders, de-icers not yet electrified)
  - Natural gas heating (hangars, workshops, terminal areas)
  - Backup generators (emergency power)
  - Refrigerant leakage (air conditioning, cold storage)

**Emission Factors**:
- Diesel combustion: 2.68 kgCO₂e/liter (includes CO₂, CH₄, N₂O per [DEFRA 2024](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2024))
- Natural gas: 0.184 kgCO₂e/kWh (regional grid-specific factors)
- Refrigerants: GWP-weighted per [IPCC AR6](https://www.ipcc.ch/assessment-report/ar6/) (e.g., R-134a: GWP = 1430)

**Measurement Methods**:
- **Direct Metering**: Fuel consumption from invoices, tank fill records
- **Equipment-Level Monitoring**: Telematics on diesel GSE (liters consumed per hour)
- **Refrigerant Tracking**: Annual leak tests, top-up quantities logged

**Reduction Targets**:
- **2030**: -80% vs. 2025 baseline (primarily via [GSE electrification](85-30-03_Energy_Efficiency_and_Electrification/85-30-03-001_GSE_Electrification_Strategy.md))
- **2035**: Net zero Scope 1 (residual emissions offset with carbon removals)

### Scope 2: Indirect Emissions from Purchased Energy

**Definition**: Emissions from generation of purchased electricity, steam, heating, and cooling consumed by infrastructure.

**Infrastructure Sources**:
- **Electricity**:
  - Electric GSE charging (tugs, baggage handlers, ground power units)
  - H₂ production via electrolysis (significant load)
  - CO₂ battery charging
  - Passenger boarding bridges (HVAC, lighting, docking systems)
  - Fixed infrastructure (hangars, terminals, offices, lighting)

**Accounting Methods**:

**Location-Based Method**:
- Uses average emission intensity of regional electricity grid
- Example: European grid ~350 gCO₂e/kWh (2024), but varies widely by country
- Data source: [IEA Emissions Factors](https://www.iea.org/data-and-statistics/data-product/emissions-factors-2024) or national grid operators

**Market-Based Method** (preferred for AMPEL360):
- Uses emission factor of contractually procured electricity
- **Renewable Contracts**: 0 gCO₂e/kWh (with valid Guarantees of Origin or RECs)
- **Green Tariffs**: Utility-specific emission factor
- **Default**: Residual mix emission factor (grid average minus renewable claims)

**AMPEL360 Strategy**:
- [100% renewable electricity by 2030](85-30-03_Energy_Efficiency_and_Electrification/85-30-03-002_Renewable_Energy_Integration.md) (market-based)
- Priority: On-site solar PV (30% target) + Power Purchase Agreements (PPAs) for remainder
- Residual location-based emissions used for transparency (dual reporting)

**Measurement Methods**:
- **Utility Meters**: Monthly consumption from invoices
- **Submeter Network**: Real-time monitoring of major loads (H₂ electrolyzers, charging stations, buildings)
- **Equipment-Level**: [DPP-integrated energy meters](85-30-00-004_DPP_Integration_for_Infrastructure.md) for granular allocation

**Reduction Targets**:
- **2027**: 50% renewable electricity (market-based)
- **2030**: 100% renewable electricity (market-based)
- **Absolute Reduction**: -30% location-based emissions via efficiency improvements (independent of renewable sourcing)

### Scope 3: Value Chain Emissions

**Definition**: All other indirect emissions occurring in the value chain (upstream and downstream).

#### Scope 3 Categories (per GHG Protocol)

**Upstream Categories**:

**Category 1: Purchased Goods and Services**:
- **Infrastructure Equipment Manufacturing**:
  - Embodied carbon in GSE, H₂ systems, CO₂ battery containers
  - Methodology: Lifecycle assessment per [ISO 14040/14044](https://www.iso.org/standard/37456.html), supplier EPDs
  - Allocation: Amortize embodied emissions over equipment lifetime
  - Example: Electric tug 20 tonnes CO₂e embodied / 15 years service life = 1.33 tCO₂e/year allocated
- **Spare Parts and Consumables**:
  - Filters, lubricants, hydraulic fluids, tires
  - Methodology: Supplier-specific emission factors or [Ecoinvent](https://ecoinvent.org/) database
- **Services**: Maintenance contracts, consulting, IT services (usually <2% of total, may be excluded if below materiality threshold)

**Category 2: Capital Goods**:
- Buildings, hangars, fixed infrastructure (airport-owned, amortized over 40-50 year life)
- H₂ production plants, pipelines (amortized over 25-30 year life)
- Methodology: Construction LCA or [RICS Whole Life Carbon Assessment](https://www.rics.org/profession-standards/rics-standards-and-guidance/sector-standards/construction-standards/whole-life-carbon-assessment)

**Category 3: Fuel and Energy-Related Activities (not in Scope 1 or 2)**:
- **Upstream Emissions of Fuels**:
  - Diesel: Extraction, refining, transport (~0.6 kgCO₂e/liter upstream, adding to 2.68 combustion)
  - Natural gas: Extraction, processing, transport (~0.05 kgCO₂e/kWh upstream)
- **Upstream Emissions of Electricity (T&D Losses)**:
  - Transmission and distribution losses (~7% global average)
  - Calculated as: Scope 2 location-based emissions × 7%
- **Green Hydrogen Production Emissions** (if sourced externally):
  - Electrolysis energy source (must be renewable to qualify as "green")
  - Compression, storage, transport (typically 0.5-1.5 kgCO₂e/kg H₂ for green hydrogen)
  - Verification via supplier [certificates of origin](85-30-04_H2_Value_Chain_Circularity/85-30-04-001_Green_H2_Production_Integration.md)

**Category 4: Upstream Transportation and Distribution**:
- Transport of equipment, spare parts, consumables to airport
- H₂ delivery via truck/pipeline (if not produced on-site)
- Methodology: Distance × mass × [emission factor](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2024) (e.g., road freight 0.1 kgCO₂e/tonne-km)

**Category 5: Waste Generated in Operations**:
- Disposal/recycling of equipment at end-of-life
- Hazardous waste transport and treatment
- Wastewater treatment
- Methodology: Waste mass × treatment-specific emission factor
  - Landfill: ~500 kgCO₂e/tonne (methane emissions)
  - Incineration: ~50 kgCO₂e/tonne (energy recovery credit)
  - Recycling: Typically net negative (avoided primary production emissions)
- AMPEL360 Target: >90% [diversion from landfill](85-30-07_Waste_Management_and_Recovery/85-30-07-004_Zero_Waste_Ground_Operations.md)

**Category 6: Business Travel**:
- Employee travel for infrastructure management (site visits, training, conferences)
- Methodology: Air km + rail km + car km × mode-specific emission factors
- Usually <1% of infrastructure carbon footprint (may be excluded if immaterial)

**Category 7: Employee Commuting**:
- Infrastructure operations and maintenance staff commuting to airport
- Methodology: # employees × average commute distance × commute mode split × emission factors
- Typically 1-3% of infrastructure footprint; important for social sustainability but low carbon impact

**Downstream Categories**:

**Category 9: Downstream Transportation and Distribution**:
- Not directly applicable (infrastructure is stationary)
- May include transport of waste/recyclables from airport to processors

**Category 10: Processing of Sold Products**:
- Not applicable (infrastructure provides services, not products)

**Category 11: Use of Sold Products**:
- Not applicable for infrastructure

**Category 12: End-of-Life Treatment of Sold Products**:
- Recycling, refurbishment, disposal of decommissioned infrastructure equipment
- Covered under Category 5 (waste) from operator perspective
- Methodology: [Material recovery rates](85-30-00-003_Materials_and_Recyclability.md) × emission credits for avoided primary production
  - Aluminum recycling credit: -8 to -10 kgCO₂e/kg (vs. primary production ~12 kgCO₂e/kg)
  - Steel recycling credit: -1.5 to -2 kgCO₂e/kg (vs. primary ~2.5 kgCO₂e/kg)
  - Plastics recycling credit: -1 to -2 kgCO₂e/kg (vs. primary ~2-3 kgCO₂e/kg)

**Category 15: Investments**:
- Emissions from airport or AMPEL360 equity investments in H₂ infrastructure companies, renewable energy projects
- Methodology: Proportional share of investee company emissions
- Usually managed at corporate level, not infrastructure-specific

#### Scope 3 Prioritization

Given the breadth of Scope 3, AMPEL360 prioritizes:

**High Priority** (>5% of total, high influence):
- Cat 1: Equipment manufacturing (embodied carbon) → Influence via [material selection](85-30-00-003_Materials_and_Recyclability.md), [lifecycle extension](85-30-00-002_Lifecycle_Management_Strategy.md)
- Cat 3: H₂ production emissions → Ensure [green H₂ certification](85-30-04_H2_Value_Chain_Circularity/85-30-04-001_Green_H2_Production_Integration.md)
- Cat 12: Equipment end-of-life → Maximize [recycling and reuse](85-30-02_Materials_and_Reuse/)

**Medium Priority** (1-5%, moderate influence):
- Cat 2: Capital goods → Engage airport authorities on infrastructure carbon intensity
- Cat 4: Transportation → Optimize logistics, local sourcing
- Cat 5: Waste → Achieve [zero-waste targets](85-30-07_Waste_Management_and_Recovery/)

**Lower Priority** (<1%, low influence or data availability):
- Cat 6: Business travel → Manage at corporate level
- Cat 7: Commuting → Encourage sustainable transport, but low infrastructure-specific lever

## Carbon Accounting Methodology

### Data Collection and Management

**Data Sources**:

| Emission Source | Primary Data | Secondary Data (if primary unavailable) | Update Frequency |
|-----------------|--------------|----------------------------------------|------------------|
| Diesel GSE | Fuel invoices, telematics | Fuel consumption rates × operating hours | Monthly |
| Natural gas heating | Utility meters, invoices | Heat demand models × heating degree days | Monthly |
| Electricity | Utility meters, submeters | Load profiles × time-of-use data | Monthly (real-time where feasible) |
| H₂ production (on-site) | Electrolyzer energy meters | H₂ mass × specific energy (55 kWh/kg) | Real-time |
| H₂ sourcing (external) | Supplier certificates | Industry average (grey H₂ ~10 kgCO₂e/kg) | Per delivery |
| Equipment embodied carbon | Supplier EPDs | [Ecoinvent](https://ecoinvent.org/) LCA database | Per procurement |
| Waste | Waste hauler reports, scales | Waste audits × facility size | Quarterly |
| Employee commuting | Survey (annual) | Regional modal split × distance estimates | Annually |

**Data Quality Tiers** (per GHG Protocol):
- **Tier 1**: Supplier-specific, primary data (highest quality) - Target >70% of Scope 1+2
- **Tier 2**: Industry-average data from reputable sources - Acceptable for Scope 3 upstream
- **Tier 3**: Proxy or estimated data - Use only where Tier 1/2 unavailable, document limitations

**Data Management Platform**:
- [Digital Product Passport (DPP)](85-30-00-004_DPP_Integration_for_Infrastructure.md) integration: Equipment-level energy and emissions data
- Central GHG accounting software (e.g., Watershed, Persefoni, or custom ERP module)
- Automated data feeds from utility meters, telematics, invoices (minimize manual entry)
- Blockchain integration for H₂ provenance and carbon credit tracking (future state)

### Calculation Methodology

**Basic Formula**:
```
Emissions (tCO₂e) = Activity Data × Emission Factor × Global Warming Potential (GWP)

Where:
Activity Data   = Quantity of activity (liters fuel, kWh electricity, kg material)
Emission Factor = GHG emitted per unit activity (kgCO₂e/unit)
GWP             = Relative warming impact (CO₂=1, CH₄=28, N₂O=265 per IPCC AR6)
```

**Example: Diesel GSE**:
```
Annual diesel consumption: 50,000 liters
Emission factor (DEFRA 2024): 2.68 kgCO₂e/liter
Emissions = 50,000 L × 2.68 kgCO₂e/L = 134 tCO₂e
```

**Example: Electric GSE (Scope 2, market-based)**:
```
Annual electricity consumption: 200,000 kWh
Renewable electricity contract: 0 gCO₂e/kWh (market-based)
Emissions (market-based) = 200,000 kWh × 0 = 0 tCO₂e

Grid average (location-based, for transparency): 350 gCO₂e/kWh
Emissions (location-based) = 200,000 kWh × 0.35 kgCO₂e/kWh = 70 tCO₂e
```

**Example: Equipment Embodied Carbon (Scope 3 Cat 1)**:
```
Equipment cost: EUR 100,000
Embodied carbon intensity: 0.5 kgCO₂e/EUR (from supplier EPD or database)
Total embodied carbon: 50 tCO₂e
Service life: 15 years
Annual allocated emissions: 50 tCO₂e / 15 years = 3.33 tCO₂e/year
```

### Allocation and Boundary Setting

**Operational Control Approach** (preferred):
- AMPEL360 accounts for 100% of emissions from infrastructure it operates, regardless of ownership
- Example: Leased GSE emissions fully accounted by AMPEL360 as operator

**Equity Share Approach** (alternative):
- Account for share of emissions proportional to ownership stake
- Example: If airport owns jetway (AMPEL360 50% user), allocate 50% of emissions
- Not preferred for infrastructure due to complexity; operational control is clearer

**Functional Allocation**:
- For shared infrastructure (e.g., terminal building supporting multiple airlines), allocate based on usage:
  - Turnaround count, passenger count, or aircraft movements
  - Example: AMPEL360 = 10% of airport movements → 10% of terminal electricity emissions

### Uncertainty and Data Gaps

**Uncertainty Management**:
- Primary data (Tier 1): ±5-10% uncertainty (meter accuracy, invoice timing)
- Secondary data (Tier 2): ±20-30% uncertainty (industry averages)
- Estimated data (Tier 3): ±50%+ uncertainty (must be clearly disclosed)

**Handling Data Gaps**:
- **Conservative Estimation**: Use higher end of uncertainty range (avoid underreporting)
- **Proxy Data**: Use similar equipment or facilities as proxy (e.g., same GSE model at different airport)
- **Disclosure**: Clearly state assumptions, data gaps, and materiality in reporting
- **Improvement Plan**: Prioritize closing gaps in high-impact categories (target: <10% estimated data by 2027)

## Integration with ATA 99 Carbon Accounting

The infrastructure carbon accounting (ATA 85-30) feeds into the aircraft-level carbon accounting framework (ATA 99):

**Data Flows**:

**ATA 85 → ATA 99** (Scope 3 for aircraft):
- Ground operations emissions per turnaround → Aircraft Scope 3 Category 9 (downstream transportation and distribution)
- H₂ carbon intensity (gCO₂e/kg) → Aircraft fuel lifecycle emissions (well-to-wake)
- CO₂ battery charging emissions → Aircraft energy system lifecycle impact

**Shared Metrics**:
- **Carbon Intensity per Turnaround**: gCO₂e/turnaround (standardized for aircraft size, ground time)
- **H₂ Carbon Intensity**: gCO₂e/MJ (lifecycle, from production through refueling)
- **Electricity Carbon Intensity**: gCO₂e/kWh (market-based and location-based)

**Reporting Alignment**:
- Both frameworks report annually per [GRI 305](https://www.globalreporting.org/standards/media/1012/gri-305-emissions-2016.pdf) (Emissions) and [CDP Climate](https://www.cdp.net/en/climate) questionnaire
- Consolidated in AMPEL360 Sustainability Report and [CSRD](https://ec.europa.eu/info/business-economy-euro/company-reporting-and-auditing/company-reporting/corporate-sustainability-reporting_en) disclosures

See [ATA 99 Carbon Accounting Framework](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_99-CARBON_ACCOUNTING/) for aircraft-level integration details.

## Carbon Reduction Strategy

### Hierarchy of Mitigation

1. **Avoid**: Eliminate emission sources (e.g., phase out fossil fuel GSE entirely)
2. **Reduce**: Improve efficiency (e.g., [energy optimization](85-30-03_Energy_Efficiency_and_Electrification/85-30-03-004_Energy_Efficiency_Optimization.md), lightweight materials)
3. **Replace**: Switch to low-carbon alternatives (e.g., [GSE electrification](85-30-03_Energy_Efficiency_and_Electrification/85-30-03-001_GSE_Electrification_Strategy.md), [green H₂](85-30-04_H2_Value_Chain_Circularity/85-30-04-001_Green_H2_Production_Integration.md))
4. **Offset**: Compensate residual emissions with verified carbon removals (last resort, <10% of total)

### Emissions Reduction Targets

**Scope 1+2 (Direct Control)**:
- **2027**: -50% vs. 2025 baseline (absolute emissions)
- **2030**: -80% vs. 2025 baseline
- **2035**: Net zero (≤5% residual emissions offset with carbon removals)

**Scope 3 (Value Chain Influence)**:
- **2030**: -40% vs. 2025 baseline (Categories 1, 3, 12 prioritized)
- **2035**: -60% vs. 2025 baseline

**Carbon Intensity (per Turnaround)**:
- **2025 Baseline**: ~500 kgCO₂e/turnaround (conventional fossil fuel GSE)
- **2027**: 250 kgCO₂e/turnaround (50% GSE electrified, 50% renewable electricity)
- **2030**: 100 kgCO₂e/turnaround (80% GSE electrified, 100% renewable electricity, green H₂)
- **2035**: <50 kgCO₂e/turnaround (100% GSE electrified, circular infrastructure, residual offsets)

### Key Decarbonization Initiatives

| Initiative | Emission Scope | Reduction Potential | Timeline | Reference |
|------------|----------------|---------------------|----------|-----------|
| [GSE Electrification](85-30-03_Energy_Efficiency_and_Electrification/85-30-03-001_GSE_Electrification_Strategy.md) | Scope 1 | -60% Scope 1 | 2025-2030 | 85-30-03-001 |
| [100% Renewable Electricity](85-30-03_Energy_Efficiency_and_Electrification/85-30-03-002_Renewable_Energy_Integration.md) | Scope 2 | -100% Scope 2 (market-based) | 2027-2030 | 85-30-03-002 |
| [Green H₂ Production](85-30-04_H2_Value_Chain_Circularity/85-30-04-001_Green_H2_Production_Integration.md) | Scope 3 Cat 3 | -90% H₂ emissions | 2026-2030 | 85-30-04-001 |
| [Lifecycle Extension](85-30-00-002_Lifecycle_Management_Strategy.md) | Scope 3 Cat 1 | -20% embodied carbon | Ongoing | 85-30-00-002 |
| [Material Circularity](85-30-00-003_Materials_and_Recyclability.md) | Scope 3 Cat 1, 12 | -30% materials footprint | 2025-2035 | 85-30-00-003 |
| [Zero Waste Operations](85-30-07_Waste_Management_and_Recovery/85-30-07-004_Zero_Waste_Ground_Operations.md) | Scope 3 Cat 5 | -95% waste emissions | 2027-2030 | 85-30-07-004 |

## Monitoring, Reporting, and Verification (MRV)

### Monitoring

**Real-Time Monitoring** (where feasible):
- Electricity consumption (submeters, 15-minute intervals)
- H₂ production and refueling (electrolyzer energy, mass delivered)
- GSE telematics (fuel/energy consumption, operating hours)

**Periodic Monitoring**:
- Diesel fuel (monthly invoices, tank fills)
- Natural gas (monthly utility bills)
- Waste generation (quarterly hauler reports)
- Equipment procurement (per transaction, EPD data)

**Annual Monitoring**:
- Employee commuting (survey-based)
- Comprehensive Scope 3 assessment (all categories)
- Uncertainty analysis and data quality review

**Dashboard and KPIs**:
- Public-facing dashboard: Real-time carbon intensity per turnaround, renewable % electricity
- Internal dashboard: All scopes, categories, trends, targets, alerts for anomalies
- KPIs tracked monthly, reported quarterly, verified annually

### Reporting

**Internal Reporting**:
- **Monthly**: KPI dashboard for operations and management
- **Quarterly**: Detailed Scope 1+2 results, progress vs. targets, variance analysis
- **Annually**: Comprehensive Scope 1+2+3 inventory, including Scope 3 screening and prioritization

**External Reporting**:
- **Annual Sustainability Report**: Public disclosure per [GRI 305](https://www.globalreporting.org/standards/media/1012/gri-305-emissions-2016.pdf)
- **CDP Climate Questionnaire**: Annual submission for investor transparency
- **CSRD Sustainability Statement**: Comprehensive ESG reporting per [EU CSRD](https://ec.europa.eu/info/business-economy-euro/company-reporting-and-auditing/company-reporting/corporate-sustainability-reporting_en)
- **Airport Carbon Accreditation**: Annual submission for [ACI accreditation](https://www.aci.aero/about-aci/priorities/environment/airport-carbon-accreditation/)
- **CORSIA**: If applicable, annual reporting per [ICAO CORSIA MRV](https://www.icao.int/environmental-protection/CORSIA/Pages/CORSIA-MRV.aspx)

**Reporting Boundaries and Consistency**:
- Clearly define organizational and operational boundaries (consistent year-over-year)
- Report both market-based and location-based Scope 2 (dual reporting)
- Disclose methodology changes, restatements, data quality issues
- Use consistent base year (2025) for progress tracking

### Verification

**Internal Verification**:
- **Monthly**: Automated data quality checks (outlier detection, mass balance, consistency)
- **Quarterly**: Management review of KPIs and anomalies
- **Annually**: Internal audit of data collection processes, calculations, documentation

**External Verification**:
- **Third-Party Assurance** (required for CSRD, recommended for CDP):
  - Limited assurance (ISAE 3410, ISO 14064-3): 2026-2028
  - Reasonable assurance: 2029 onwards (target)
  - Verifier: Accredited environmental auditor (e.g., Big Four accounting firms, specialized consultancies)
- **Scope**: Scope 1+2 emissions (full verification), Scope 3 Categories 1, 3, 12 (limited verification)

**Verification Criteria**:
- Accuracy: ±5% for Scope 1+2 (primary data), ±10-15% for Scope 3 (secondary data acceptable)
- Completeness: >95% of expected emissions sources captured
- Consistency: Methodology applied consistently across reporting periods
- Transparency: Clear documentation of assumptions, data sources, calculations

## Key Performance Indicators (KPIs)

### Absolute Emissions KPIs
- **Total GHG Emissions**: tCO₂e/year (Scope 1+2+3)
- **Scope 1 Emissions**: tCO₂e/year (target: -80% by 2030)
- **Scope 2 Emissions (market-based)**: tCO₂e/year (target: 0 by 2030)
- **Scope 2 Emissions (location-based)**: tCO₂e/year (transparency metric)
- **Scope 3 Emissions**: tCO₂e/year (target: -40% by 2030)

### Carbon Intensity KPIs
- **Emissions per Turnaround**: kgCO₂e/turnaround (target: <100 by 2030)
- **Emissions per Passenger**: kgCO₂e/passenger (turnaround emissions / passenger count)
- **H₂ Carbon Intensity**: gCO₂e/kg H₂ (lifecycle, target: <1000 for "green" H₂)
- **Electricity Carbon Intensity**: gCO₂e/kWh (location-based, target: <100 by 2030)

### Decarbonization Progress KPIs
- **GSE Electrification**: % GSE fleet electrified by energy consumption (target: 100% by 2030)
- **Renewable Energy**: % electricity from renewable sources (market-based, target: 100% by 2030)
- **Green H₂**: % H₂ from verified green sources (target: 100% by 2030)
- **Carbon Removals**: tCO₂e removed via nature-based or technological solutions (target: <5% of gross emissions)

### Data Quality KPIs
- **Primary Data Coverage**: % Scope 1+2 emissions from metered/invoiced data (target: >95%)
- **EPD Coverage**: % equipment procurement value with supplier EPD (target: >80%)
- **Data Completeness**: % expected data points collected on time (target: >98%)

Detailed tracking in [ASSETS/Metrics_and_KPIs/](ASSETS/Metrics_and_KPIs/).

## Related Documents

### Framework Documents
- [85-30-00-001 Circularity Framework Overview](85-30-00-001_Circularity_Framework_Overview.md)
- [85-30-00-004 DPP Integration for Infrastructure](85-30-00-004_DPP_Integration_for_Infrastructure.md)

### Implementation Guides
- [85-30-06-001 Ground Operations Carbon Footprint](85-30-06_Emissions_and_Carbon_Accounting/85-30-06-001_Ground_Operations_Carbon_Footprint.md)
- [85-30-06-002 Scope 1, 2, 3 Emissions Infrastructure](85-30-06_Emissions_and_Carbon_Accounting/85-30-06-002_Scope_1_2_3_Emissions_Infrastructure.md)
- [85-30-06-003 Carbon Reduction Targets and Tracking](85-30-06_Emissions_and_Carbon_Accounting/85-30-06-003_Carbon_Reduction_Targets_and_Tracking.md)
- [85-30-06-004 Integration with ATA 99 Carbon Accounting](85-30-06_Emissions_and_Carbon_Accounting/85-30-06-004_Integration_with_ATA_99_Carbon_Accounting.md)

### Cross-References
- [ATA 99 Carbon Accounting Framework](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_99-CARBON_ACCOUNTING/)
- [85-30-03 Energy Efficiency and Electrification](85-30-03_Energy_Efficiency_and_Electrification/)
- [85-30-04 H₂ Value Chain Circularity](85-30-04_H2_Value_Chain_Circularity/)

## References and Standards

- [GHG Protocol Corporate Standard](https://ghgprotocol.org/corporate-standard)
- [GHG Protocol Scope 3 Standard](https://ghgprotocol.org/standards/scope-3-standard)
- [ISO 14064-1:2018 GHG Quantification and Reporting](https://www.iso.org/standard/66453.html)
- [GRI 305: Emissions 2016](https://www.globalreporting.org/standards/media/1012/gri-305-emissions-2016.pdf)
- [CDP Climate Change Questionnaire](https://www.cdp.net/en/climate)
- [ICAO CORSIA](https://www.icao.int/environmental-protection/CORSIA/Pages/default.aspx)
- [ACI Airport Carbon Accreditation](https://www.aci.aero/about-aci/priorities/environment/airport-carbon-accreditation/)
- [EU CSRD](https://ec.europa.eu/info/business-economy-euro/company-reporting-and-auditing/company-reporting/corporate-sustainability-reporting_en)
- [DEFRA GHG Conversion Factors 2024](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2024)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---
