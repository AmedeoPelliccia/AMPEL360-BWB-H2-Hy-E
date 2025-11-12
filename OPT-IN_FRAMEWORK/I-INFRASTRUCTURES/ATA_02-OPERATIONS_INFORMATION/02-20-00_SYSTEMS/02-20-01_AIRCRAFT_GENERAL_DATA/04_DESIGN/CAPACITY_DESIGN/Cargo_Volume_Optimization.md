# Cargo Volume Optimization

## Executive Summary

The AMPEL360 BWB configuration provides exceptional cargo volume capability through its wide center body design, enabling up to 15,000 kg (120 m³) of containerized cargo while maintaining passenger capacity and CG control.

## Cargo Compartment Design

### Forward Cargo Compartment
**Location:** Stations 6-12m, below passenger floor  
**Volume:** 45 m³  
**Capacity:** 5,000 kg  
**CG Position:** 18% MAC

**Container Compatibility:**
- LD-3: 6 containers
- LD-8: 3 containers
- Pallets: 88" × 125" (4 units)

**Access:**
- Forward cargo door: 1.68m × 2.44m (66" × 96")
- Powered loader system
- Environmental control: Yes

**Features:**
- Fire suppression: Halon alternative
- Smoke detection: Dual redundant
- Temperature control: 5-25°C range
- Lighting: LED, automatic

### Center Cargo Compartment
**Location:** Stations 12-18m, below passenger floor  
**Volume:** 50 m³  
**Capacity:** 6,000 kg  
**CG Position:** 25% MAC

**Container Compatibility:**
- LD-3: 8 containers
- LD-8: 4 containers
- Pallets: 88" × 125" (5 units)

**Access:**
- Center cargo door (both sides): 1.68m × 2.44m
- Powered loader system
- Environmental control: Yes

**Features:**
- Fire suppression: Halon alternative
- Smoke detection: Dual redundant
- Temperature control: 5-25°C range
- Bulk cargo capability: 10 m³ bulk area

### Aft Cargo Compartment
**Location:** Stations 18-24m, below passenger floor  
**Volume:** 25 m³  
**Capacity:** 4,000 kg  
**CG Position:** 32% MAC

**Container Compatibility:**
- LD-3: 4 containers
- LD-8: 2 containers
- Pallets: 88" × 125" (2 units)

**Access:**
- Aft cargo door: 1.68m × 2.44m
- Powered loader system
- Environmental control: Optional

**Features:**
- Fire suppression: Halon alternative
- Smoke detection: Dual redundant
- Bulk cargo capability: Full compartment option
- Pet transport: Dedicated area with climate control

## Total Cargo Capability

### Standard Configuration
- **Total Volume:** 120 m³
- **Total Weight:** 15,000 kg
- **Containers:** 18× LD-3 or 9× LD-8
- **Pallets:** 11× 88"×125"

### Revenue Potential
- **Per Flight:** 15,000 kg @ $1.50/kg = $22,500
- **Annual (500 flights):** $11.25M cargo revenue
- **Cargo-only Conversion:** Potential 45,000 kg capacity

## Cargo Loading Strategy

### CG Balance Principles

**Forward Heavy Configuration**
- Load forward compartment first
- Used when aft passengers or aft H2 fuel
- Target: CG 20-24% MAC

**Balanced Configuration**
- Load all compartments proportionally
- Standard loading pattern
- Target: CG 24-28% MAC

**Aft Heavy Configuration**
- Load aft compartment first
- Used when forward passengers or forward H2 fuel
- Target: CG 28-32% MAC

### Loading Sequence Integration

**Typical Turnaround (45 minutes):**
1. Unload arriving cargo: 15 minutes
2. Load departing cargo: 20 minutes
3. Verification and securing: 5 minutes
4. Documentation: 5 minutes (parallel)

### CAOS Integration
- Pre-calculates optimal cargo distribution
- Generates load plan for ground crew
- Real-time weight and balance monitoring
- Alerts for CG deviations

## Cargo System Design

### Loading Equipment

**Power Drive Units (PDU)**
- Roller bed system: Full length of compartments
- Drive speed: 0.3 m/s
- Control: Automated with manual override
- Power: Aircraft electrical (115V AC)

**Container Locks**
- Type: Automatic
- Quantity: 36 positions
- Load rating: 1,000 kg vertical, 500 kg horizontal
- Status indication: Electronic to CAOS

**Net Systems**
- Cargo nets: Certified to CS-25.787
- Capacity: 1,500 kg per net
- Quick-release: Emergency egress

### Safety Systems

**Fire Detection and Suppression**
- Smoke detectors: Ionization type, redundant
- Fire suppression: Halon 1301 alternative (HFC-125)
- Discharge time: < 2 minutes full compartment
- Crew alerting: EICAS warnings

**Temperature Control**
- Forward compartment: Heated/cooled (5-25°C)
- Center compartment: Heated/cooled (5-25°C)
- Aft compartment: Heated only (10-25°C)
- Pet area: Dedicated climate control (15-25°C)

**Structural Design**
- Floor loading: 1,000 kg/m² uniform
- Point loads: 2,000 kg over 0.25m²
- Crash loads: 9g forward, 3g aft, 4g lateral
- Fire resistance: Class C materials

## Special Cargo Capabilities

### Dangerous Goods (DG)
- **Approved Classes:** 1-9 per IATA DGR
- **Segregation:** Dedicated zones in forward compartment
- **Quantity Limits:** Per passenger aircraft restrictions
- **Crew Training:** Required for operations

### Temperature-Controlled Cargo
- **Refrigerated:** Active cooling containers (LD-3 cool)
- **Temperature Range:** -20°C to +25°C
- **Monitoring:** CAOS real-time tracking
- **Autonomy:** 24 hours with battery backup

### Live Animals
- **Pet Transport:** Dedicated aft compartment area
- **Capacity:** 12 pet carriers (IATA CR-82 compliant)
- **Climate Control:** 15-25°C, fresh air supply
- **Monitoring:** Video surveillance, CAOS alerts

### Valuable Cargo
- **Security:** Lockable containers, sealed doors
- **Tracking:** RFID tags, CAOS integration
- **Insurance:** Coverage up to $1M per flight
- **Handling:** Dedicated secure procedures

## Optimization Analysis

### Volume Utilization

**Current Design:**
- Usable volume: 120 m³
- Container volume: 95 m³ (79% utilization)
- Bulk volume: 25 m³ (21% flexibility)

**Optimization Opportunities:**
- Contour matching containers: +10% utilization
- Overhead cargo bins: +5 m³ (crew bags, mail)
- Underfloor voids: Minimized by BWB design

### Weight vs Volume Trade
- **Standard cargo:** 125 kg/m³ average density
- **Current capacity:** 15,000 kg / 120 m³ = 125 kg/m³ ✓
- **Volume-limited:** Mail, low-density goods
- **Weight-limited:** Dense cargo, machinery

### Revenue Optimization

**Cargo Priority Algorithm (CAOS):**
```
For each flight:
  1. Calculate available capacity (weight and volume)
  2. Price cargo by kg and m³ factors
  3. Maximize revenue within constraints:
     - CG envelope (19-35% MAC)
     - Weight limits (MTOW, MZFW)
     - Volume limits (120 m³)
  4. Generate load plan
  5. Communicate to ground systems
```

**Expected Results:**
- Revenue increase: 15% over manual planning
- Load factor improvement: 8%
- CG optimization: Improved fuel efficiency 2%

## Cargo Conversion Option

### Full Cargo Configuration
- **Remove:** All passenger seats and monuments
- **Add:** Reinforced floor, additional nets
- **Capacity:** 45,000 kg / 340 m³
- **CG Range:** 18-35% MAC (wider envelope)

**Market Opportunity:**
- Quick-change capability (8 hours conversion)
- Passenger-to-cargo as needed
- Night cargo, day passenger operations
- Addresses peak cargo demand periods

### Combi Configuration
- **Forward:** Cargo (30 m³, 4,000 kg)
- **Center/Aft:** Passengers (120 pax)
- **Barrier:** Class B partition
- **Use Case:** Mixed passenger/cargo routes

## Certification Compliance

### CS-25 Requirements
- **CS-25.787:** Cargo compartment classification (Class C)
- **CS-25.855:** Cargo compartment fire protection
- **CS-25.857:** Cargo compartment ventilation
- **CS-25.1309:** Equipment, systems, installations

### Operational Standards
- **IATA ULD Regulations:** Container compatibility
- **IATA DGR:** Dangerous goods handling
- **TSA Cargo Security:** Known shipper program
- **FAA/EASA:** Cargo handling procedures

---

**References:**
- Cargo Compartment Design: DWG-CAR-001
- Loading System Specification: SPC-LOAD-001
- Fire Suppression Analysis: FSA-2025-001
- Cargo Operations Manual: COM-001
- CS-25.787 Compliance Report: CRT-CAR-2025-001
