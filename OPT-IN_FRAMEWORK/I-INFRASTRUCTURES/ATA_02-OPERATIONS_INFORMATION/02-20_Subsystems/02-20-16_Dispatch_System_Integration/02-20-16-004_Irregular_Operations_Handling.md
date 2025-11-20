# 02-20-16-004: Irregular Operations (IROPS) Handling

> **ID:** 02-20-16-004  
> **Title:** Irregular Operations Handling Logic  
> **System:** ATA 02-20 (Operations / Dispatch)  
> **Revision:** 1.0  
> **Status:** CONCEPTUAL DESIGN  
> **Risk Level:** HIGH (Operational Disruption)

---

## 1. Purpose
This document outlines the CAOS automated logic and Dispatcher workflows for managing non-standard operational events. Due to the unique physics of the AMPEL360 (Cryogenic Fuel + Solid State CO₂ Capture), IROPS require specialized handling to prevent safety exceedances or "Stranded Asset" scenarios.

## 2. The "Tail Swap" Challenge (Equipment Substitution)

In conventional aviation, swapping one A320 for another is trivial. For the AMPEL360, the **thermodynamic state** of the specific airframe dictates its capability.

### 2.1 State Mismatch Logic
When a tail swap is initiated in the Flight Planning System (FPS), CAOS performs an immediate compatibility check:

| Parameter | Original Aircraft (N360A) | Replacement Aircraft (N360B) | CAOS Logic / Outcome |
|:---|:---|:---|:---|
| **H₂ Tank Temp** | -252°C (Sub-cooled) | -248°C (Saturated) | **Energy Deficit:** N360B has lower fuel density. Dispatch must reduce Payload or add a refueling stop. |
| **Sorbent State** | 100% Capacity (Fresh) | 40% Capacity (Partially Used) | **Capture Deficit:** N360B cannot complete the mission *and* remain Carbon Negative. Dispatch must authorize "Net Zero" or "Positive Carbon" mode, or trigger Sorbent Swap (45 min delay). |
| **Battery Temp** | 25°C | 45°C (Hot from previous flight) | **Turnaround Delay:** N360B requires 15 min active cooling before H₂ fueling can begin. |

### 2.2 Dispatch Alerting
*   `WARN: TAIL_SWAP_ENERGY_MISMATCH` - Replacement aircraft requires +400kg H₂ to match energy profile.
*   `ERR: TAIL_SWAP_SORBENT_INSUFFICIENT` - Replacement aircraft cannot hold projected CO₂ mass.

---

## 3. Ground Delays & Cryogenic Management (The "Ticking Clock")

Hydrogen boils off as it warms. A long ground delay can pressurize the tanks, necessitating venting (fuel loss).

### 3.1 Time-To-Vent (TTV) Calculation
CAOS continuously calculates `TTV` based on ambient temperature and tank insulation performance.

```mermaid
graph TD
    A[Ground Delay Initiated] --> B{Check Tank Pressure}
    B -->|P < 3.0 bar| C[Safe State]
    B -->|P > 3.5 bar| D[Pre-Vent Warning]
    
    D --> E{Estimated Takeoff Time < TTV?}
    E -->|Yes| F[Continue Taxi - Burn Boil-off in Engines]
    E -->|No| G[Action Required]
    
    G --> H[Option 1: Return to Stand (Sub-cool)]
    G --> I[Option 2: Vent to Atmosphere (Safety Zone)]
```

### 3.2 Dispatch Decision Matrix
1.  **If `TTV < 30 mins`:** Dispatch must coordinate with ATC for "Expedited Departure" (similar to De-icing holdover times).
2.  **If Venting Required:** Aircraft must move to a designated "Vent Zone" (cannot vent at crowded gate). Operational penalty: Fuel mass lost must be re-calculated to ensure reserves remain legal.

---

## 4. Divert & Alternate Management

The AMPEL360 cannot divert to just any airport due to fueling infrastructure requirements.

### 4.1 The "Stranded Asset" Check
During Dispatch Optimization (02-20-16-001), alternates are categorized:
*   **Tier 1 (Full Service):** LH2 Refueling + Sorbent Exchange available.
*   **Tier 2 (Recovery Only):** LH2 Refueling available; No Sorbent Exchange.
*   **Tier 3 (Emergency):** No H2 infrastructure. Aircraft becomes **AOG (Aircraft On Ground)** upon landing.

**Logic:**
*   If diverting to **Tier 3**, Dispatch must alert Maintenance immediately to deploy a "Mobile Refueler" or recovery team.
*   **Fuel Reserve Logic:** If diverting to Tier 3, the Pilot is authorized to use "Reserve Fuel" more aggressively, as the aircraft is grounded regardless.

### 4.2 Dynamic Landing Weight at Alternate
*   **Scenario:** Flight diverts early.
*   **Physics:** Less fuel burned than planned ($Weight_{High}$) + Less CO₂ captured ($Weight_{Low}$).
*   **Result:** The aircraft may be **Lighter** than a standard diversion calculation, affecting landing distance performance. CAOS updates the FMS Landing Performance Data dynamically.

---

## 5. In-Flight System Degradation

### 5.1 Loss of Carbon Capture (ATA 21-80 Failure)
If the CO₂ capture system fails mid-flight:
1.  **Mass Deviation:** The aircraft stops gaining weight.
2.  **CG Shift:** The anticipated rearward CG shift (from CO₂ accumulation) stops.
3.  **Dispatch Action:**
    *   No immediate safety threat.
    *   **Post-Flight:** Flight is flagged as "Positive Carbon Emission" in ATA 95 Ledger. Carbon credits are voided.

### 5.2 Fuel Cell Module Loss (ATA 73 Partial Failure)
The BWB has distributed propulsion (e.g., 4 pods). Loss of 1 pod:
1.  **Performance:** Altitude ceiling drops.
2.  **H₂ Consumption:** Remaining cells run at higher load (potentially lower efficiency).
3.  **Dispatch Action:** CAOS re-calculates range in real-time. If `New_Range < Distance_to_Dest + Reserves`, a diversion is triggered automatically.

---

## 6. Workflow: Managing a "Venting Event"

**Scenario:** Technical problem at the gate causes a 2-hour delay with full tanks.

1.  **T-00:00:** Delay confirmed.
2.  **T-00:05:** CAOS predicts `TTV = 90 mins`.
3.  **T-00:10:** Dispatcher receives Alert: `CRYO_LIMIT_EXCEEDANCE_PREDICTED`.
4.  **Decision:** Dispatcher selects **"Defuel/Recycle"** workflow.
5.  **Action:** Ground crew connects GSE. LH2 is pumped back to the bowser (or sub-cooled loop) to maintain state.
6.  **Resume:** When delay clears, fuel is pumped back. Dispatch must verify **Final Mass** matches Loadsheet (some loss is inevitable).

---

## 7. Integration Artifacts

| Artifact | Description | Format |
|:---|:---|:---|
| **IROPS_Checklist_H2.xml** | Digital checklist for Crew/Dispatch during Cryo events. | S1000D |
| **Tier3_Airport_Db.json** | Database of airports lacking H2 infrastructure. | JSON |
| **Vent_Zone_Map_Layer** | Geospatial overlay for EFB showing safe venting areas. | KML/GeoJSON |

```
