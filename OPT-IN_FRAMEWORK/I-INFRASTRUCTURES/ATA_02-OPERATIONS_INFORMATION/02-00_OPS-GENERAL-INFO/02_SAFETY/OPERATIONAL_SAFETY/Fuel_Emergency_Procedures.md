# Fuel Emergency Procedures

**Document ID:** AMPEL360-02-10-00-SAF-FEP  
**Version:** 1.0.0  
**Date:** 2025-11-05  
**Status:** Released  
**Classification:** Safety Critical

## Purpose

This document defines emergency procedures for hydrogen fuel-related emergencies on the AMPEL360 BWB H₂ Hy-E Q100 INTEGRA aircraft. These procedures are designed to be integrated into the Quick Reference Handbook (QRH) and training programs.

## Fuel Planning Requirements

### Minimum Fuel Requirements

**Pre-Flight Fuel Planning:**
- **Trip Fuel:** Calculated fuel for planned route
- **Contingency Fuel:** 5% of trip fuel or 5 minutes holding, whichever greater
- **Alternate Fuel:** Fuel to divert to alternate airport
- **Final Reserve:** 45 minutes holding at 1,500 ft above alternate
- **Additional:** Any additional fuel required by MEL, weather, etc.

**Minimum Fuel Formula:**
```
Minimum Fuel = Trip + Contingency + Alternate + Final Reserve + Additional
```

### Fuel Alerts

**Minimum Fuel (CAOS Advisory):**
- Fuel remaining = Final Reserve + Alternate fuel
- ATC notification: "Minimum Fuel"
- Commit to destination or divert to alternate

**Emergency Fuel (CAOS Warning):**
- Fuel remaining = Final Reserve only (45 minutes)
- ATC notification: "MAYDAY FUEL"
- Priority handling required
- No delay acceptable

**Critical Fuel (CAOS Red Alert):**
- Fuel remaining < 30 minutes
- Immediate landing required
- Nearest suitable airport
- Emergency services alert

## H₂ Fuel System Malfunctions

### Procedure: H₂ LEAK DETECTED (Ground or Flight)

**Conditions:**
- EICAS message: "H2 LEAK DETECTED"
- Leak detection system: ≥25% LEL
- Or visible signs of leak (frost, vapor)

**Immediate Actions (Memory Items):**
1. **Emergency Ventilation** ...................... ON
2. **Affected Zone Fuel Valve** .................. CLOSE (if identified)
3. **Notify ATC** ..................................... H₂ LEAK EMERGENCY

**Subsequent Actions (Checklist):**
4. Assess leak severity:
   - Check H₂ concentration trend (CAOS monitoring)
   - Review fuel quantity loss rate
   - Identify affected fuel zone if possible

5. If leak increasing or not controlled:
   - **Master H₂ Shutoff** ........................ CLOSE
   - **Fuel Cells** .................................. SHUTDOWN (all)
   - **APU** .......................................... START (if available)
   - **Battery Power** .............................. MONITOR

6. If leak controlled (concentration decreasing):
   - **Continue monitoring**
   - **Isolate affected zone** (if not done)
   - **Consider diversion**

7. Landing considerations:
   - **Priority landing** ........................... REQUEST
   - **CFR services** ............................... ALERT (H₂ specific)
   - **Wind direction** ............................. CONSIDER (land upwind approach if possible)
   - **Passengers** .................................. BRIEF (evacuation may be required)

8. After landing:
   - **Stop on taxiway** (if safe) or proceed to remote area
   - **Remain upwind** of leak
   - **Do not shut down** until CFR assessment
   - **Evacuate** if CFR recommends

**Notes:**
- H₂ leak is serious but not immediately catastrophic if no ignition
- Emergency ventilation reduces accumulation risk
- Fuel cells can operate on remaining H₂ in non-leaking zones
- APU provides backup electrical if fuel cells shutdown required

---

### Procedure: H₂ FIRE DETECTED

**Conditions:**
- EICAS message: "H2 FIRE DETECTED"
- Multi-spectrum fire detection confirmed
- Or crew observation of fire indications

**Immediate Actions (Memory Items):**
1. **Fire Handle** ................................... PULL (affected zone)
   - Fuel shutoff
   - Generator disconnect
2. **Fire Suppression** ............................. DISCHARGE
3. **Notify ATC** .................................... MAYDAY - H₂ FIRE

**Subsequent Actions (Checklist):**
4. Assess fire status:
   - Check fire detection (still active?)
   - Monitor thermal sensors
   - If fire continues: 2nd discharge

5. If fire suppressed:
   - **Monitor** for re-ignition
   - **Continue to nearest suitable airport**
   - **Do not restart** affected fuel cell

6. If fire NOT suppressed after 2nd discharge:
   - **All H₂ Fuel Valves** ........................ CLOSE
   - **All Fuel Cells** ............................. SHUTDOWN
   - **APU** .......................................... START (emergency power)
   - **Battery Power** .............................. MONITOR
   - **Emergency Descent** .......................... INITIATE (if at altitude)

7. Landing:
   - **Nearest suitable airport** .................. LAND IMMEDIATELY
   - **Overweight landing** ........................ ACCEPTED (if necessary)
   - **CFR services** ............................... FULL ALERT
   - **Evacuate** after landing .................... IMMEDIATE

**Notes:**
- H₂ fire is a serious emergency requiring immediate action
- Fire suppression should control fire in most scenarios
- If fire persists, fuel source must be isolated
- Emergency electrical power critical (APU or battery)

---

### Procedure: FUEL QUANTITY LOW

**Conditions:**
- CAOS advisory: "FUEL QUANTITY LOW"
- Fuel remaining ≤ Minimum Fuel
- Or earlier if concerned about reaching destination

**Actions:**
1. **Verify fuel quantity:**
   - Cross-check all fuel quantity indications
   - Compare with flight plan burn rate
   - Assess fuel remaining vs. required

2. **If fuel = Minimum Fuel:**
   - **ATC notify** .................................. "MINIMUM FUEL"
   - **Expedite** .................................... Request direct routing
   - **Holding** ..................................... Decline unless critical
   - **Alternate planning** ......................... Review and be ready to divert

3. **If fuel = Emergency Fuel (Final Reserve + 0):**
   - **ATC notify** .................................. "MAYDAY FUEL"
   - **Priority** .................................... Request
   - **Divert if necessary** ........................ Do not delay
   - **Speed** ....................................... Adjust for maximum range if required

4. **If fuel = Critical (<30 min):**
   - **ATC notify** .................................. "MAYDAY - IMMEDIATE LANDING REQUIRED"
   - **Nearest suitable airport** .................. LAND IMMEDIATELY
   - **All non-essential systems** ................. OFF (conserve fuel cell load)

5. **Landing considerations:**
   - **Overweight landing** ........................ Accepted if fuel critical
   - **CFR services** ............................... Alert if any risk of fuel exhaustion
   - **Single approach** ............................ Prepare for immediate landing

**Notes:**
- Fuel management is critical with H₂ (cannot be replenished in flight)
- "Minimum Fuel" is notification, not emergency
- "MAYDAY FUEL" is emergency, requires priority
- CAOS provides predictive fuel planning, monitor closely

---

### Procedure: FUEL CELL STACK FAILURE

**Conditions:**
- EICAS message: "FUEL CELL STACK FAIL"
- One or more fuel cell stacks inoperative
- Reduced electrical power available

**Actions:**
1. **Assess power available:**
   - 4 stacks normal: 100% power
   - 3 stacks: 75% power (adequate)
   - 2 stacks: 50% power (minimum required)
   - 1 stack or 0 stacks: Emergency power only (APU/battery)

2. **If 3 stacks operating (75% power):**
   - **Continue to destination** (if performance adequate)
   - **Load shed non-essential** ................... As required
   - **Monitor remaining stacks** .................. Closely
   - **Notify ATC** ................................. Fuel cell malfunction, continue
   - **Maintenance** ................................ Notify (post-flight)

3. **If 2 stacks operating (50% power):**
   - **Consider diversion** ........................ Nearest suitable airport
   - **Load shed non-essential** ................... Execute automatic + manual
   - **Notify ATC** ................................. Fuel cell malfunction, may divert
   - **Performance degraded** ...................... Single engine performance
   - **Climbing** ................................... Limited or not possible

4. **If 1 stack or all stacks fail:**
   - **APU** ......................................... START (immediate)
   - **Emergency electrical power** ................ Verify (APU or battery)
   - **All non-essential** ......................... OFF
   - **Notify ATC** ................................. MAYDAY - ELECTRICAL EMERGENCY
   - **Emergency descent** ......................... If at altitude
   - **Nearest suitable airport** .................. LAND IMMEDIATELY

5. **Landing considerations:**
   - **Overweight landing** ........................ Accepted
   - **Single approach** ........................... Plan for immediate landing
   - **Battery time limited** ...................... If APU also fails (30 minutes)

**Notes:**
- Aircraft designed to operate on 2 of 4 stacks (50% power)
- Loss of all stacks is extremely unlikely (redundancy)
- APU provides essential backup electrical power
- Battery provides final backup (time-limited)

---

### Procedure: FUEL TRANSFER FAILURE

**Conditions:**
- Unable to transfer fuel between tanks
- CG position approaching limits
- Or EICAS message: "FUEL TRANSFER FAIL"

**Actions:**
1. **Assess CG position:**
   - Current CG (CAOS display)
   - Predicted CG based on remaining fuel distribution
   - Time to CG limit

2. **If CG approaching caution limit (±2% MAC):**
   - **Manual fuel transfer** ....................... Attempt
   - **Cross-feed valves** .......................... Open/cycle to redistribute
   - **Fuel burn rate** ............................. Monitor per tank
   - **CAOS advisory** .............................. Follow recommendations

3. **If CG approaching warning limit (±1% MAC):**
   - **Diversion** .................................. Consider immediate
   - **Reduce weight** .............................. Land sooner to reduce fuel burn
   - **Slow speed** ................................. Reduce to extend time to limit
   - **Notify ATC** ................................. Fuel transfer malfunction

4. **If CG at limit:**
   - **Emergency** .................................. Declare
   - **Nearest suitable airport** .................. LAND IMMEDIATELY
   - **Speed** ...................................... Carefully manage (CG affects handling)
   - **Approach** ................................... Stable approach critical
   - **Pilot technique** ............................ May require adjusted control inputs

**Notes:**
- CG management critical for BWB configuration
- CAOS provides real-time CG calculation and prediction
- Fuel transfer normally automatic, manual backup available
- If CG cannot be controlled, immediate landing required

---

## Fuel Planning Tools

### CAOS Fuel Advisory

**Features:**
- Real-time fuel quantity all tanks
- Fuel burn rate (actual vs. planned)
- Predicted fuel remaining at destination
- CG position and prediction
- Alerts for minimum fuel, emergency fuel
- Alternate airport recommendations with fuel required

**Crew Actions:**
- Monitor CAOS fuel page regularly
- Cross-check with manual calculations
- Act on CAOS advisories (minimum fuel, etc.)
- Override if CAOS appears incorrect (human authority)

### Manual Fuel Calculation

**Method (Backup if CAOS unavailable):**
1. Note current fuel quantity (kg)
2. Calculate fuel burn rate (kg/hour) from recent trend
3. Calculate fuel required to destination:
   - Time remaining (hours)
   - Fuel rate (kg/hour)
   - Fuel required = Time × Rate
4. Compare fuel required to fuel available
5. Add reserves (contingency, alternate, final)

**Rule of Thumb:**
- If fuel available < fuel required + final reserve → Minimum Fuel
- If fuel available < final reserve → Emergency Fuel

## Training Requirements

### Flight Crew

**Initial:**
- H₂ fuel system overview (4 hours)
- Fuel emergency procedures (4 hours)
- Simulator scenarios (4 scenarios minimum):
  - H₂ leak in flight
  - Fuel cell failure
  - Low fuel diversion
  - CG management failure

**Recurrent (Annual):**
- Fuel emergency procedures review (2 hours)
- Simulator scenarios (2 scenarios minimum)

### Dispatch

**Initial:**
- H₂ fuel planning (4 hours)
- Fuel emergency coordination (2 hours)

**Recurrent (Annual):**
- Fuel planning review (2 hours)

## Post-Emergency Actions

### After H₂ Leak or Fire:

1. **Aircraft quarantine:** Do not move until H₂ specialist inspects
2. **No personnel approach:** Until H₂ levels confirmed safe (<10% LEL)
3. **Thorough inspection:** All H₂ systems before next flight
4. **Incident report:** Mandatory report to safety and CAA
5. **Investigation:** Determine root cause
6. **Corrective action:** Before return to service

### After Fuel Quantity Low:

1. **Flight review:** Analyze fuel planning vs. actual
2. **Fuel quantity verification:** Confirm actual fuel loaded
3. **Report:** If fuel planning error or fuel system malfunction
4. **Corrective action:** Address any procedural or system issues

---

**Document Owner:** Chief Pilot - Training & Standards  
**Next Review Date:** 2026-05-05  
**Configuration Control:** Git SHA-256: [hash]  
**Classification:** Safety Critical - Unclassified
