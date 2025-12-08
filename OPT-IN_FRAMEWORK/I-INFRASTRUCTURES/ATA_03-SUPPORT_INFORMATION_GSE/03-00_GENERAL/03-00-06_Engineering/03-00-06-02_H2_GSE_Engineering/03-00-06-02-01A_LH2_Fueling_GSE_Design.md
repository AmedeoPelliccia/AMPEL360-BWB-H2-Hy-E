---
Title: "LH2 Fueling GSE Design — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-06-02-01A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Design requirements and specifications for Liquid Hydrogen (LH2) refueling Ground Support Equipment for AMPEL360 BWB H2 aircraft."
Keywords: ["ATA 03","GSE","LH2","Hydrogen","Refueling","Cryogenic","Ground Support"]
Compliance:
  - "ATA iSpec 2200"
  - "SAE AS6968"
  - "ISO 19880-8"
  - "NASA-STD-8719.17"
  - "ASME B31.12"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  Parent: "../00_INDEX.md"
  Related: "./03-00-06-02-02A_Cryogenic_GSE_Requirements.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-00-06-02-01A — LH2 Fueling GSE Design

## 1. Purpose

This document defines the **design requirements and specifications** for Liquid Hydrogen (LH2) refueling Ground Support Equipment (GSE) used to safely and efficiently transfer LH2 from ground storage to the AMPEL360 BWB H2-powered aircraft fuel tanks.

LH2 refueling presents unique challenges due to:
- **Cryogenic temperature** (-253°C / 20K at atmospheric pressure)
- **Low density** (70.8 kg/m³ at boiling point vs. 804 kg/m³ for Jet-A)
- **High flammability** (4-75% by volume in air)
- **Embrittlement risk** for incompatible materials
- **Boil-off losses** during transfer and storage

## 2. Scope

This document covers:

- **LH2 refueling truck** (mobile bowser) design
- **Stationary hydrant refueling system** (airport infrastructure)
- **Fuel transfer components**: pumps, hoses, nozzles, couplings
- **Safety systems**: leak detection, emergency shutoff, fire suppression
- **Instrumentation and control**: flow measurement, temperature, pressure monitoring

This document applies to new-design GSE and modification of existing hydrogen refueling systems for aviation applications.

## 3. Applicable Documents

### 3.1 Standards and Regulations

- [SAE AS6968](https://www.sae.org/standards/content/as6968/) — Hydrogen Aircraft Ground Support Equipment
- [ISO 19880-8](https://www.iso.org/standard/71940.html) — Gaseous Hydrogen Fueling Stations (Airport Applications)
- [NASA-STD-8719.17](https://standards.nasa.gov/) — Safety Standard for Hydrogen and Hydrogen Systems
- [ASME B31.12](https://www.asme.org/codes-standards/find-codes-standards/b31-12-hydrogen-piping-pipelines) — Hydrogen Piping and Pipelines
- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) — Hydrogen Technologies Code
- [EN 13445](https://www.en-standard.eu/) — Unfired Pressure Vessels (Europe)
- [49 CFR 178](https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C/part-178) — Specifications for Packagings (USA DOT)

### 3.2 Related Documents

- [03-00-06-02-02A_Cryogenic_GSE_Requirements](./03-00-06-02-02A_Cryogenic_GSE_Requirements.md)
- [03-00-06-02-03A_H2_Safety_Systems_Design](./03-00-06-02-03A_H2_Safety_Systems_Design.md)
- [03-00-06-02-04A_H2_GSE_Materials](./03-00-06-02-04A_H2_GSE_Materials.md)
- [03-00-02_Safety](../../03-00-02_Safety/) — GSE Safety Requirements

## 4. LH2 Refueling System Architecture

### 4.1 Refueling System Types

| System Type | Description | Application | Advantages | Disadvantages |
|-------------|-------------|-------------|------------|---------------|
| **Mobile Refueling Truck (Bowser)** | Self-contained LH2 tank truck (20,000-40,000 L) with pump, hose, and controls | Remote airports, initial deployment, backup refueling | Flexibility, minimal infrastructure | Limited capacity, higher operating cost, requires trained driver-operator |
| **Stationary Hydrant System** | Underground or above-ground LH2pipeline network with pit valves at aircraft parking positions | Major airports with high H2 aircraft volume | High throughput, lower per-fueling cost, reduced ramp congestion | High capital cost, fixed installation |
| **Hybrid System** | Hydrant pits with dispenser cart (mobile unit connects to pit and aircraft) | Medium-traffic airports | Balance of flexibility and infrastructure efficiency | Requires both infrastructure and mobile equipment |

**AMPEL360 Recommendation**: Develop mobile refueling truck first for initial operations, with future transition to hydrant systems at high-volume airports.

### 4.2 Functional Requirements

| Function | Requirement | Rationale |
|----------|-------------|-----------|
| **Refueling Rate** | 2,000-4,000 liters/min (140-280 kg/min LH2) | Complete refueling in 20-30 minutes |
| **Fuel Purity** | ≥ 99.995% H2 (Grade 5.0) | Prevent contamination of aircraft fuel system |
| **Pre-Cool Aircraft Lines** | Pre-cooling cycle to reduce thermal shock and boil-off | Minimize fuel loss and thermal stress |
| **Overfill Prevention** | Automatic shutoff at 98% tank capacity | Safety margin for thermal expansion |
| **Defueling Capability** | Ability to remove fuel from aircraft to truck (optional but recommended) | Maintenance and emergency response |
| **Fail-Safe Design** | All failures result in fuel flow stoppage and venting to safe location | Safety first |

## 5. LH2 Refueling Truck Design

### 5.1 Vehicle Chassis and Mobility

| Parameter | Requirement | Notes |
|-----------|-------------|-------|
| **Chassis Type** | Heavy-duty commercial truck chassis (e.g., Mercedes-Benz Actros, Volvo FH) | Proven reliability, parts availability |
| **Gross Vehicle Weight** | 35-44 tonnes (depending on tank capacity) | Requires appropriate license and road permits |
| **Axle Configuration** | 3-4 axles (6×4 or 8×4) | Distribute load, comply with road weight limits |
| **Turning Radius** | < 15m | Maneuverability on airport ramps |
| **Ground Clearance** | ≥ 300mm | Avoid scraping on uneven surfaces |
| **Self-Propulsion** | Diesel engine (Euro VI or equivalent emission standard) or electric/fuel cell hybrid | Consider hydrogen fuel cell for zero-emission operation |
| **Speed** | 0-80 km/h (road), 0-25 km/h (ramp operations) | Speed limiter for safety on ramp |

### 5.2 LH2 Storage Tank

| Parameter | Specification | Verification |
|-----------|---------------|--------------|
| **Capacity** | 40,000 liters (nominal), ≈2,850 kg LH2 | Sufficient for 2-3 widebody aircraft refuelings |
| **Tank Type** | Double-wall vacuum-insulated cryogenic tank (inner vessel + outer jacket) | Per ASME Section VIII Div 1 or EN 13445 |
| **Inner Vessel Material** | Austenitic stainless steel 304L or 316L | Hydrogen compatibility at -253°C |
| **Outer Jacket Material** | Carbon steel or stainless steel | Structural support and vacuum containment |
| **Insulation** | Multi-layer insulation (MLI): 30-60 layers of aluminized Mylar + spacer | Minimize heat leak |
| **Vacuum Level** | < 10⁻⁴ mbar (high vacuum) | Maintain insulation performance |
| **Heat Leak** | < 0.5% boil-off per day at full capacity | Acceptable for 48-hour hold time |
| **Design Pressure (Inner Vessel)** | 6 bar (87 psig) | Operating pressure 3-5 bar |
| **Safety Relief Valves** | Two independent spring-loaded PRVs set at 5.5 bar | Per ASME Section VIII |
| **Burst Disk** | 6.5 bar | Backup overpressure protection |
| **Pressure Buildup Rate** | < 0.1 bar/hour when not venting | Indicates insulation integrity |

### 5.3 LH2 Transfer Pump

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Pump Type** | Centrifugal cryogenic pump (submerged or external) | Low NPSH required |
| **Flow Rate** | 0-2,000 liters/min variable (0-140 kg/min) | Adjustable for controlled fill |
| **Discharge Pressure** | Up to 10 bar (145 psig) | Overcome line losses and aircraft tank pressure |
| **Power** | Electric motor 30-50 kW, powered by onboard genset or battery | Consider battery for quiet operation |
| **Material** | Stainless steel 316L wetted parts | Cryogenic and H2 compatible |
| **Seal Type** | Mechanical seal with LH2 barrier fluid or magnetic coupling | Prevent leakage |
| **Efficiency** | > 50% | Minimize heat input to LH2 |

### 5.4 Hose and Nozzle Assembly

| Component | Specification | Standard |
|-----------|---------------|----------|
| **Hose Type** | Vacuum-insulated flexible hose, corrugated stainless steel inner, outer jacket | Custom cryogenic hose |
| **Hose Length** | 15m (50 ft) | Reach aircraft fuel panel from truck |
| **Hose Inner Diameter** | 50mm (2 inches) | Balance flow rate and flexibility |
| **Hose Pressure Rating** | 10 bar (145 psig) working, 40 bar burst | Safety factor 4:1 |
| **Hose End Fittings** | Stainless steel flanged or threaded connections with cryogenic seals (PTFE or spiral-wound graphite) | Leak-tight at -253°C |
| **Breakaway Coupling** | Installed mid-hose, activates at 200-400 N axial pull | Prevents hose rupture if aircraft/truck moves |
| **Nozzle Type** | Dry-break coupling per SAE AS6968 Class I | Standardized aircraft interface |
| **Nozzle Grounding** | Static bonding cable with 10 MΩ resistor | Dissipate static before connection |

### 5.5 Instrumentation and Control Panel

| Instrument | Range/Specification | Purpose |
|------------|---------------------|---------|
| **Flow Meter** | Coriolis mass flow meter, 0-2,000 L/min (0-140 kg/min) | Accurate fuel quantity measurement |
| **Tank Level Gauge** | Differential pressure or capacitance, 0-100% | Monitor truck tank inventory |
| **Tank Pressure Gauge** | 0-10 bar, ±1% accuracy | Monitor tank pressure |
| **Tank Temperature** | RTD sensors, -260°C to +50°C | Monitor LH2 temperature and detect boil-off |
| **Hose Temperature** | RTD sensors at inlet and outlet | Detect pre-cooling and flow |
| **Leak Detectors** | H2 sensors (0-4% by volume) at pump, hose connections, vents | Early leak detection |
| **Control Panel** | Touchscreen HMI (10-inch), sunlight-readable | Operator interface |
| **Data Logger** | Record flow, pressure, temperature, alarms at 1 Hz for 30 days | Traceability and diagnostics |

### 5.6 Safety Systems

| System | Function | Specification |
|--------|----------|---------------|
| **Emergency Shutoff Valve (ESV)** | Close fuel flow within 2 seconds of emergency stop activation | Pneumatically actuated ball valve, fail-closed |
| **Hydrogen Leak Detection** | Continuous monitoring with visual and audible alarm at 10% LEL (0.4% H2) | Catalytic or thermal conductivity sensors |
| **Fire Detection** | UV/IR flame detectors around tank and pump area | Activate fire suppression and ESV |
| **Fire Suppression** | Dry chemical or inert gas (N2, Ar) system, manual and automatic activation | Protect equipment, not LH2 fire (let burn in controlled manner) |
| **Vent Stack** | Vent boil-off and emergency releases to >3m above truck, ignite at vent tip | Disperse hydrogen safely |
| **Grounding/Bonding** | Bond truck to aircraft and ground before connecting, verify <10 ohms resistance | Prevent static discharge |
| **Interlock System** | Prevent pump start unless: parking brake set, hose connected, bonding verified | Prevent unsafe operations |

## 6. Stationary Hydrant Refueling System

### 6.1 System Overview

A hydrant system consists of:
- **Bulk LH2 storage** (above-ground or underground cryogenic tanks, 100,000-500,000 liters)
- **LH2 piping network** (vacuum-insulated, 50-100mm diameter)
- **Hydrant pit valves** at aircraft parking positions
- **Dispenser cart** (mobile unit with pump, meter, hose, and controls)

### 6.2 Bulk Storage Tank

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Capacity** | 200,000 liters (≈14,000 kg LH2) per tank | Size for 1-3 days of airport consumption |
| **Tank Type** | Vertical or horizontal double-wall vacuum-insulated | Above-ground preferred for inspection access |
| **Insulation** | MLI or foam insulation + vapor barrier | Heat leak < 0.2% per day |
| **Location** | Minimum 75m from buildings, 30m from property line per NFPA 2 | Safety separation distances |
| **Berming/Secondary Containment** | Earthen berm or concrete wall, volume ≥ 110% of tank | Contain LH2 spill |
| **Venting** | Stack height ≥ 7m, with ignition source at tip | Disperse hydrogen releases |

### 6.3 LH2 Piping Network

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| **Pipe Material** | Austenitic stainless steel 316L, vacuum-jacketed | ASME B31.12 |
| **Pipe Size** | 50-100mm (2-4 inches) nominal diameter | Sized for flow rate and pressure drop |
| **Insulation** | Vacuum-jacketed pipe (pipe-in-pipe) or polyurethane foam + vapor barrier | Minimize heat input |
| **Installation** | Above-ground on supports (preferred) or buried with corrosion protection | Inspection access vs. aesthetics |
| **Expansion Joints** | Bellows-type expansion joints every 30-50m | Accommodate thermal contraction |
| **Isolation Valves** | Cryogenic ball valves every 100m and at branch points | Sectional isolation for maintenance |
| **Pressure Rating** | PN 20 (20 bar) or Class 150 | Operating pressure 5-10 bar |

### 6.4 Hydrant Pit Valve

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Pit Location** | Under aircraft fueling point, typically 5-10m from nose or wing | Minimize hose length |
| **Pit Design** | Watertight, frost-resistant, with drainage sump | Prevent water/ice accumulation |
| **Hydrant Valve** | Cryogenic ball valve with extended stem, manually or remotely operated | Quick connect/disconnect |
| **Coupling** | SAE AS6968 or API 1584 (adapted for LH2) | Standardize across airport |
| **Flow Capacity** | 2,000 L/min (140 kg/min) at 5 bar | Adequate for refueling |

### 6.5 Dispenser Cart

The dispenser cart is a mobile unit (towable or self-propelled) that connects the hydrant pit to the aircraft.

| Component | Specification | Purpose |
|-----------|---------------|---------|
| **Pump** | Centrifugal cryogenic pump, 50 kW | Boost pressure from hydrant |
| **Flow Meter** | Coriolis or turbine meter | Custody transfer accuracy ±0.5% |
| **Hose Reel** | 20m vacuum-insulated hose on motorized reel | Easy deployment and storage |
| **Control Panel** | Touchscreen with wireless communication to airport fuel management system | Remote monitoring and billing |
| **Safety Systems** | Same as truck: ESV, leak detection, bonding, interlocks | Consistent safety standards |

## 7. Pre-Cooling and Refueling Procedure

### 7.1 Pre-Cooling Phase

Before LH2 transfer, aircraft fuel lines and tanks must be pre-cooled to minimize thermal shock and boil-off.

| Step | Action | Duration | Purpose |
|------|--------|----------|---------|
| 1. **Connect and Bond** | Attach nozzle to aircraft, verify bonding < 10 ohms | 2 min | Static discharge prevention |
| 2. **Purge with GN2** | Flow gaseous nitrogen through lines to displace air | 5 min | Prevent ice formation and oxygen contamination |
| 3. **Initial LH2 Flow** | Start LH2 flow at 10-20% rate | 5-10 min | Cool lines gradually; vent boil-off |
| 4. **Monitor Temperature** | Observe temperature sensors drop to -253°C | — | Confirm pre-cooling complete |

### 7.2 Main Refueling Phase

| Step | Action | Duration | Purpose |
|------|--------|----------|---------|
| 5. **Ramp Up Flow** | Increase to full flow rate (2,000 L/min) | 1 min | Maximize efficiency |
| 6. **Monitor Fill Level** | Observe aircraft tank level gauges | 15-25 min | Track progress |
| 7. **Auto-Shutoff** | ESV closes at 98% tank capacity | — | Overfill prevention |
| 8. **Top-Off (if needed)** | Slow flow to bring to 100% | 2-5 min | Ensure full tanks |

### 7.3 Disconnect and Secure

| Step | Action | Duration | Purpose |
|------|--------|----------|---------|
| 9. **Close Valves** | Close aircraft and truck/hydrant valves | 1 min | Isolate fuel systems |
| 10. **Vent Hose** | Vent residual LH2 from hose to safe location | 2 min | Prevent hose warming and pressure buildup |
| 11. **Disconnect Nozzle** | Remove nozzle (dry-break coupling prevents drips) | 1 min | Safe disconnection |
| 12. **Stow Equipment** | Retract hose, disconnect bonding cable | 2 min | Prepare for departure |

**Total Refueling Time**: 30-40 minutes for 40,000 liters (full BWB tanks).

## 8. Design Considerations

### 8.1 Thermal Management

| Challenge | Solution |
|-----------|----------|
| **Heat Leak** | Use multi-layer insulation (MLI) on tanks, vacuum-jacketed piping and hoses |
| **Boil-Off Losses** | Minimize transfer time; use boil-off gas for truck power (if fuel cell equipped) or flare |
| **Thermal Contraction** | Design piping with expansion joints and flexible supports; stress analysis per ASME B31.12 |
| **Pre-Cooling Energy** | Accept 5-10% fuel loss during pre-cooling as unavoidable; design for efficiency |

### 8.2 Contamination Control

| Contaminant | Effect | Prevention |
|-------------|--------|------------|
| **Air (O2, N2)** | Freezes at LH2 temperature, blocks lines | Purge with GN2 before LH2 introduction |
| **Water/Ice** | Blocks lines, contaminates fuel | Use desiccant breathers, purge with dry GN2 |
| **Hydrocarbons** | Incompatible with fuel cells | Dedicated LH2 equipment, no cross-use with Jet-A |

### 8.3 Pressure Control

| System | Pressure Management |
|--------|---------------------|
| **Tank Pressure Buildup** | Use pressure buildup to drive flow (no pump for low-rate transfer); vent excess to maintain 3-5 bar |
| **Overpressure Protection** | Relief valves (5.5 bar) + burst disk (6.5 bar); relief discharge to vent stack |
| **Vacuum Loss** | Monitor vacuum gauge; if vacuum degrades (> 10⁻³ mbar), insulation performance drops; re-evacuate tank |

## 9. Safety and Emergency Response

### 9.1 Hazard Identification

| Hazard | Severity | Mitigation |
|--------|----------|------------|
| **LH2 Leak** | High (fire/explosion risk) | Leak detection, ventilation, ignition source control |
| **Cryogenic Burn** | High (tissue damage on contact) | PPE (cryogenic gloves, face shield), training |
| **Asphyxiation** | High (H2 displaces oxygen in confined spaces) | Ventilation, O2 monitors in enclosed areas |
| **Static Discharge** | Medium (ignition source) | Bonding and grounding before fuel transfer |
| **Fire** | High (LH2 burns with invisible flame) | UV/IR detectors, trained fire brigade, let burn approach if no exposure risk |

### 9.2 Emergency Procedures

| Emergency | Immediate Action | Follow-Up |
|-----------|------------------|-----------|
| **LH2 Leak Detected** | 1. Activate emergency stop (close ESV), 2. Evacuate area (min 30m), 3. Summon fire brigade | Investigate cause, repair, and re-test before resuming |
| **Fire** | 1. Activate ESV, 2. Evacuate, 3. If equipment fire (not LH2), use dry chemical or CO2; if LH2 fire, protect exposures and let burn | Do NOT extinguish LH2 fire unless absolutely necessary |
| **Cryogenic Spill** | 1. Evacuate area, 2. Block drainage to prevent pooling, 3. Let evaporate naturally (do not spray water) | Monitor with H2 detectors until clear |
| **Vehicle Collision** | 1. Immediate ESV activation, 2. Assess damage, 3. Call hazmat team if tank integrity questionable | Inspect and pressure test before return to service |

## 10. Operator Training Requirements

| Topic | Duration | Content |
|-------|----------|---------|
| **LH2 Properties and Hazards** | 2 hours | Cryogenic effects, flammability, asphyxiation, embrittlement |
| **GSE Operation** | 4 hours | Pre-flight checks, refueling procedures, normal and emergency operations |
| **Safety Procedures** | 2 hours | Bonding, leak detection, PPE use, emergency response |
| **Practical Training** | 8 hours | Supervised refueling operations (minimum 5 refuelings under supervision) |
| **Refresher Training** | 4 hours | Annually or after 12 months of non-use |

Operators shall be certified by AMPEL360 or designated training organization.

## 11. Cross-References

- **Parent Document**: [03-00-06_Engineering](../00_INDEX.md)
- **Related H2 GSE Engineering**: 
  - [03-00-06-02-02A_Cryogenic_GSE_Requirements](./03-00-06-02-02A_Cryogenic_GSE_Requirements.md)
  - [03-00-06-02-03A_H2_Safety_Systems_Design](./03-00-06-02-03A_H2_Safety_Systems_Design.md)
  - [03-00-06-02-04A_H2_GSE_Materials](./03-00-06-02-04A_H2_GSE_Materials.md)
- **GSE Specifications**: [03-00-06-01-02A_GSE_Specifications](../03-00-06-01_GSE_Design_Requirements/03-00-06-01-02A_GSE_Specifications.md)
- **GSE Safety**: [03-00-02_Safety](../../03-00-02_Safety/)
- **GSE Operations**: [03-10_Operations](../../../03-10_Operations/)

## 12. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-06-02-01A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Engineering & Certification WG

---
