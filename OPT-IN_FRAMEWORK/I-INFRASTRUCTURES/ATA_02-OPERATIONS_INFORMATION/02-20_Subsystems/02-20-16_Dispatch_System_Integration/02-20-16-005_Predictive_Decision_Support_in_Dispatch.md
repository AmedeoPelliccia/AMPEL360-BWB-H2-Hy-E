# 02-20-16-005: Predictive Decision Support Guidelines

> **ID:** 02-20-16-005  
> **Title:** AI Confidence Intervals & Decision Support Standards  
> **System:** ATA 02-20 (Operations) / ATA 95 (Neural Networks)  
> **Revision:** 1.0  
> **Status:** DEFINITION  
> **Related:** [02-40-50 Predictive Analytics](../../02-40-00_PROGRAMMING_ALGORITHMS/02-40-50_PREDICTIVE_ANALYTICS/)

---

## 1. Purpose and Philosophy
The AMPEL360 CAOS system generates *probabilistic* data (e.g., "85% chance of H₂ tank pressure exceeding limits"). However, Flight Dispatchers must make *deterministic* decisions ("Go" or "No-Go").

This document defines the **Presentation Standards** and **Operational Thresholds** used to translate AI Confidence Intervals (CI) into actionable Dispatch Release criteria. The guiding philosophy is **"Human Authority, AI Advisory."**

---

## 2. The "Uncertainty Gap"
Standard aviation systems report values like `Fuel = 5,000 kg`.
CAOS reports values like `Fuel_Req = 5,000 kg (± 200 kg @ 95% CI)`.

To prevent cognitive overload, the Dispatch System Integration (02-20-16) applies the following visualization rules:

### 2.1 Presentation Tiers

| Confidence Level (CI) | Visualization Style | Operational Implication |
|:---|:---|:---|
| **High (> 95%)** | **Solid Value** (Green) | Treated as fact. No dispatcher intervention required. |
| **Medium (80-95%)** | **Range / Band** (Amber) | Dispatcher must review the "Worst Case" scenario. |
| **Low (< 80%)** | **Warning Icon** (Red) | AI prediction is unstable. Fallback to Manual/Standard calculations. |

---

## 3. Display Standards for Specific Predictions

### 3.1 Hydrogen Boil-Off (Thermal Risk)
*   **The Prediction:** "Time to Venting" based on ambient temp and delays.
*   **Display Rule:** Always display the **Conservative Lower Bound** (P1).
    *   *Raw AI:* 45 mins ± 10 mins.
    *   *Dispatch View:* **"35 mins (Safe Limit)"**
*   **Rationale:** If the AI over-estimates operational time, safety is compromised (venting in unsafe zone).

### 3.2 CO₂ Capture Capacity (Mass/CG Risk)
*   **The Prediction:** "Projected Sorbent Saturation" based on engine load profile.
*   **Display Rule:** Display the **Median** with a **"Shadow Envelope."**
    *   *Dispatch View:* "Capture Target: 4,000 kg" (with ghosted text: *Max Risk: 4,200 kg*).
*   **Rationale:** Dispatchers need to know the likely landing weight, but must also check if the "Shadow/Max" weight exceeds MLW (Max Landing Weight).

### 3.3 Turnaround Turn Time (Schedule Risk)
*   **The Prediction:** Likelihood of completing H₂ refueling within slot.
*   **Display Rule:** **Traffic Light Probability.**
    *   🟢 >90% chance of On-Time.
    *   🟡 50-90% chance (Show "Risk Factors" tooltip, e.g., *GSE availability low*).
    *   🔴 <50% chance (System suggests: "Request New Slot").

---

## 4. The "Explainability" Requirement (XAI)

Dispatchers are legally responsible for the flight. They cannot blindly trust a "Black Box."
Every predictive alert in the Dispatch Interface must include a **"Why?"** dropdown (Traceability to ATA 95).

**Example: Re-Routing Recommendation**
> **Alert:** "Suggested Re-route: Waypoint DELTA (+5 mins flight time)."
> **XAI Explanation:** "Satellite data indicates high atmospheric CO₂ plume at FL350. Deviating allows +150kg additional carbon capture. Net benefit: +$200 in Carbon Credits vs Fuel Cost."
> **Action:** [ACCEPT] / [IGNORE]

---

## 5. Liability & Authority Protocols

### 5.1 The "Golden Rule"
**The Dispatcher's signature supersedes the AI.** 
If CAOS predicts a "No-Go" (e.g., high probability of turbulence), but the Dispatcher has validated weather data proving otherwise, they may override the system.

### 5.2 Forced Acknowledgement
For **Medium Confidence** predictions involving safety margins (e.g., CG Envelope), the UI must require an active "Acknowledge" click before a Release can be signed.
*   *UI Behavior:* "CAOS predicts 82% chance of Aft CG Limit approach. Confirm Payload restriction?" -> [I CONFIRM]

### 5.3 Data Logging (ATA 95)
All interactions are logged to the Digital Product Passport:
1.  **AI Prediction:** The raw probability vector.
2.  **Display State:** What the human actually saw (e.g., "Amber Range").
3.  **Human Action:** The decision made.

*Use Case:* If an incident occurs, investigators can determine if the AI failed to predict the risk, or if the Human ignored a correctly presented risk.

---

## 6. Degraded AI Modes

If the Neural Network Confidence drops below a safety threshold (e.g., due to sensor loss or novel weather patterns):
1.  **Mode Switch:** The interface flashes **"AI ADVISORY OFFLINE."**
2.  **Fallback:** The system reverts to **deterministic table-based lookups** (Standard ATA 28 Fuel Charts).
3.  **Buffer:** A mandatory "Uncertainty Penalty" (e.g., +5% Fuel Reserve) is applied to the flight plan automatically.

---

## 7. Training Requirements
Dispatchers for AMPEL360 must undergo specific training module **TRN-DISP-040**:
*   Interpreting Confidence Intervals.
*   Understanding "False Positives" in predictive maintenance.
*   The thermodynamics of H₂ boil-off vs. time predictions.
