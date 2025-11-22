# 85-60-01-A-004 — Capacity Planning for H2 Storage

## Document Metadata

```yaml
asset_id: "85-60-01-A-004"
title: "Capacity Planning for H2 Storage"
parent_system: "85-60-01 H2 Storage Systems"
category: "Planning and Sizing"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-22"
```

## Purpose

This asset document provides methodology and worked examples for sizing hydrogen storage, vaporization, and compression systems to meet aircraft refueling demand for the AMPEL360 BWB-H2-Hy-E program.

## Aircraft H2 Demand Characteristics

### AMPEL360 BWB-H2-Hy-E Aircraft Assumptions

**H2 Fuel Capacity:** 500 kg (estimated for BWB configuration with on-board storage at 350 bar)

**Refueling Frequency:** Once per flight cycle (departure refueling)

**Refueling Time Target:** 10-15 minutes (comparable to conventional jet fuel)

**Typical Flight Profile:**
- Short-haul: 2-4 flights per day (1,000-2,000 kg H2 per aircraft per day)
- Medium-haul: 1-2 flights per day (500-1,000 kg H2 per aircraft per day)

## Sizing Methodology

### Step 1: Define Fleet and Operations

**Example Scenario:**
- Airport: Medium hub (10 AMPEL360 aircraft based, plus 5 visiting daily)
- Total aircraft movements: 15 departures per day
- H2 demand per refueling: 500 kg (assume full refueling each departure for simplicity)
- **Total daily H2 demand:** 15 × 500 kg = **7,500 kg H2/day**

**Peak Hour Demand:**
- Assume 30% of daily demand in peak 2-hour morning departure window
- Peak hour demand: 7,500 kg × 0.30 ÷ 2 hours = **1,125 kg H2/hour**

**Simultaneous Refuelings:**
- Assume 3 aircraft refueling simultaneously during peak
- Refueling rate per aircraft: 1,125 kg/hour ÷ 3 aircraft = **375 kg H2/hour per aircraft**
- Per minute: 375 kg/h ÷ 60 min/h = **6.25 kg/min ≈ 2 kg/min** (conservative, allows for contingency)

### Step 2: Size LH2 Storage

**Storage Capacity = Daily Demand × Days Reserve + Contingency**

**Example:**
- Daily demand: 7,500 kg H2
- Days reserve: 5 days (account for delivery frequency, weather delays, supply chain disruptions)
- Contingency: 20% (for boil-off losses and operational flexibility)

**Required LH2 Storage Capacity:**
- 7,500 kg/day × 5 days × 1.20 = **45,000 kg H2**
- LH2 density: ~71 kg/m³
- Volume: 45,000 kg ÷ 71 kg/m³ = **634 m³ = 634,000 liters**

**Selected Tank Configuration:**
- One 500,000 L tank + One 150,000 L tank = **650,000 L total** (meets requirement)
- Alternatively: Two 500,000 L tanks (1,000,000 L total) for redundancy and future growth

**Boil-Off Losses:**
- Assume 0.25% per day average (well-designed tanks)
- Boil-off: 45,000 kg × 0.0025 = **113 kg H2/day**
- Annual boil-off: 113 kg/day × 365 days = **41 metric tons H2/year**
- Cost impact (if H2 = $5/kg): 41,000 kg × $5/kg = **$205,000/year** (justifies investment in high-quality insulation)

### Step 3: Size Vaporization Capacity

**Vaporization Capacity = Peak Hour Demand + Margin**

**Example:**
- Peak hour demand: 1,125 kg H2/hour
- Margin: 25% (for redundancy, maintenance, contingency)
- Required capacity: 1,125 kg/h × 1.25 = **1,406 kg H2/hour**

**Heat Required for Vaporization and Warming:**
- Latent heat (LH2 to GH2): 446 kJ/kg
- Sensible heat (warm GH2 from -253°C to +15°C): 14.3 kJ/kg·K × 268 K = 3,832 kJ/kg
- Total heat: 446 + 3,832 = **4,278 kJ/kg = 1.19 kWh/kg**

**Vaporizer Power (Thermal):**
- 1,406 kg/h × 1.19 kWh/kg = **1,673 kW (thermal)**

**Vaporizer Configuration:**
- Two 1,000 kW AAVs (ambient air vaporizers) in parallel = **2,000 kW total capacity** (meets requirement)
- One 500 kW electric vaporizer (backup for cold weather or AAV defrost) = **500 kW electric power required**

**AAV Sizing:**
- At 10 kW/m² frontal area (typical for 15°C ambient):
- Required area per AAV: 1,000 kW ÷ 10 kW/m² = **100 m² per AAV**
- Approximate dimensions: 10m wide × 10m tall × 2m deep (each AAV)

### Step 4: Size Compression Capacity

**Compression Capacity = Peak Refueling Rate + Margin**

**Example:**
- Peak refueling rate: 3 aircraft × 2 kg/min = **6 kg/min = 360 kg/hour**
- Margin: 33% (for efficiency, maintenance, future demand)
- Required capacity: 360 kg/h × 1.33 = **480 kg H2/hour**

**Compression Energy:**
- Compress from 5 bar (vaporizer outlet) to 500 bar (cascade high bank)
- Compression energy (including losses): ~3.7 kWh/kg H2 (see [85-60-01-005](../85-60-01-005_Pressure_Management.md))

**Compressor Power (Electric):**
- 480 kg/h × 3.7 kWh/kg = **1,776 kW = 1.8 MW**
- Motor size (peak): 1.8 MW × 1.5 (safety factor) = **2.7 MW motor**

**Compressor Configuration:**
- One 500 kg/h reciprocating compressor (4-stage, oil-free or with oil separator)
- **Electrical supply required:** 3 MW (including ancillary systems)

See: [85-80_Energy](../../85-80_Energy/README.md) for electrical infrastructure

### Step 5: Size GH2 Cascade Storage

**Cascade Storage Capacity = Refuelings Between Recharge × Aircraft Capacity × Cascade Factor**

**Example:**
- Refuelings between recharge: 5 aircraft (allows compressor to recharge cascade every 5 refuelings)
- Aircraft capacity: 500 kg H2
- Cascade factor: 4 (accounts for pressure equalization inefficiencies in cascade dispensing)

**Required GH2 Storage:**
- 5 aircraft × 500 kg/aircraft × 4 = **10,000 kg H2**

**At 350 bar Average Pressure:**
- H2 density at 350 bar, 15°C: ~28 kg/m³
- Volume: 10,000 kg ÷ 28 kg/m³ = **357 m³ = 357,000 liters**

**Cascade Bank Configuration:**
- Low bank: 30% of total = 107,000 L at 250 bar average
- Medium bank: 40% of total = 143,000 L at 350 bar average
- High bank: 30% of total = 107,000 L at 500 bar average

**Vessel Selection (Type III COPV, 1,000 L each):**
- Low bank: 107 vessels × 1,000 L = **107,000 L**
- Medium bank: 143 vessels × 1,000 L = **143,000 L**
- High bank: 107 vessels × 1,000 L = **107,000 L**
- **Total: 357 vessels, 357,000 L capacity**

**Physical Layout:**
- Arrange vessels in racks (e.g., 6 vessels per rack, 60 racks total)
- Space requirements: ~500 m² footprint for vessel racks + manifolds + spacing

## Refueling Cycle Analysis

### Cascade Dispensing Efficiency

**Cascade Principle:** Use lowest pressure bank first, then medium, then high to minimize compression cycles.

**Example Refueling (Aircraft tank 0 to 350 bar, 500 kg H2):**

1. **Low Bank Dispense** (Start 250 bar → End 200 bar):
   - Pressure equalization: Aircraft tank 0 → 200 bar
   - H2 transferred: ~285 kg (calculated from pressure equilibrium)
   - Time: ~8 minutes at 35 kg/min flow rate

2. **Medium Bank Dispense** (Start 350 bar → End 300 bar):
   - Pressure equalization: Aircraft tank 200 → 300 bar
   - H2 transferred: ~143 kg
   - Time: ~4 minutes

3. **High Bank Dispense** (Start 500 bar → End 350 bar):
   - Pressure equalization: Aircraft tank 300 → 350 bar
   - H2 transferred: ~72 kg
   - Time: ~2 minutes

**Total Refueling Time:** 8 + 4 + 2 = **14 minutes** (meets target <15 minutes)

**Total H2 Transferred:** 285 + 143 + 72 = **500 kg** ✓

### Compressor Recharge Cycle

After 5 aircraft refuelings (2,500 kg H2 dispensed), recharge cascade banks:

**Recharge Time:**
- Compressor capacity: 480 kg/h
- H2 to recharge: 2,500 kg
- Time: 2,500 kg ÷ 480 kg/h = **5.2 hours**

**Operational Strategy:**
- Recharge overnight (during low demand period)
- Size cascade to support daytime peak without recharge (5+ aircraft)

## Delivery and Supply Chain

### LH2 Tanker Delivery

**Tanker Capacity:** Typical 40,000 L (2,840 kg H2)

**Deliveries Per Week:**
- Weekly demand: 7,500 kg/day × 7 days = **52,500 kg H2**
- Deliveries required: 52,500 kg ÷ 2,840 kg/tanker = **18.5 deliveries per week** (~3 per day)

**Delivery Frequency:**
- Daily deliveries preferred (minimize on-site storage requirement)
- Coordinate with supplier for scheduled deliveries (e.g., 3 deliveries per day at 8am, 12pm, 4pm)

**Transfer Time:**
- Flow rate: ~200 kg/min (limited by tanker pump and transfer line size)
- Transfer time per tanker: 2,840 kg ÷ 200 kg/min = **14 minutes**
- Total time (including connect/disconnect): ~30 minutes per delivery

### H2 Production On-Site (Alternative)

**Electrolysis Capacity:**
- Daily demand: 7,500 kg H2
- Electrolyzer efficiency: 60 kWh/kg H2 (including compression and liquefaction)
- Power required: 7,500 kg × 60 kWh/kg = **450,000 kWh/day = 18.75 MW continuous**

**Feasibility:**
- Large electrical power requirement (equivalent to small power plant)
- High capital cost for electrolyzer and liquefaction
- May be justified for long-term, high-volume operations or renewable energy integration

**Recommendation:** LH2 delivery preferred for initial operations (lower capital cost, operational flexibility)

## Cost Estimation (Order of Magnitude)

### Capital Costs

- **LH2 Storage Tanks:** $500/L installed → 650,000 L × $500/L = **$325 million**
- **GH2 Cascade Vessels:** $1,000/L installed → 357,000 L × $1,000/L = **$357 million**
- **Vaporizers (AAV + Electric):** $500,000 each × 3 = **$1.5 million**
- **Compressor:** $3,000,000 for 500 kg/h system = **$3 million**
- **Safety Systems (H2 detection, fire protection, ESD):** **$2 million**
- **Site Development (foundations, piping, electrical, buildings):** **$10 million**

**Total Capital Cost Estimate:** **$700 million** (±30% at this early stage)

### Annual Operating Costs

- **H2 Purchase:** 7,500 kg/day × 365 days × $5/kg = **$13.7 million/year**
- **Electricity (compression, vaporization):** 2,500 kWh/day × 365 days × $0.10/kWh = **$91,250/year**
- **Maintenance (5% of capital per year):** $700M × 0.05 = **$35 million/year**
- **Personnel (operations, maintenance):** 10 FTE × $100,000/year = **$1 million/year**

**Total Annual Operating Cost:** **$50 million/year** (approximate)

**Cost Per kg H2 Delivered to Aircraft:** $50M/year ÷ (7,500 kg/day × 365 days) = **$18/kg**

(Compare to conventional Jet-A: ~$2-3/gallon = ~$3-4/kg)

## Scalability and Future Growth

### Capacity Expansion

**Modular Design:**
- Add LH2 storage tanks as demand increases
- Add vaporizers and compressors in parallel
- Expand cascade storage (add vessel racks)

**Example 2x Capacity Growth:**
- Add second 500,000 L LH2 tank: **+$250 million**
- Add second vaporizer and compressor: **+$4 million**
- Add 357 GH2 cascade vessels: **+$357 million**

**Total for 2x Capacity:** **+$611 million** (similar to initial investment)

### Technology Improvements

**Emerging Technologies:**
- Solid-state H2 storage (metal hydrides, chemical hydrides) — potential for higher density and safety
- Ionic liquid compressors — potential for lower cost and higher efficiency
- Cryo-compressed H2 (350 bar at -253°C) — combines LH2 density with GH2 convenience

**Timeline:** 5-10 years for commercial maturity

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-22

---

*Reference: [85-60-01 H2 Storage Systems README](../README.md)*
