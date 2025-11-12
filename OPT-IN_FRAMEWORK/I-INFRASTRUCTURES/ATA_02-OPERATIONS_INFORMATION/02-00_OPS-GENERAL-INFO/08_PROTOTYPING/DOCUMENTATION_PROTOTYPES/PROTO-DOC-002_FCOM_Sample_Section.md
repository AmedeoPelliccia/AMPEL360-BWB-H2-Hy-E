# PROTO-DOC-002 - FCOM Sample Section

**Prototype ID:** PROTO-DOC-002  
**Document Type:** Flight Crew Operating Manual (FCOM) Sample  
**Section:** Normal Procedures - Startup  
**Version:** 1.0  
**Date:** 2025-10-12  
**Status:** Review

## NORMAL PROCEDURES - FUEL CELL STARTUP

### GENERAL

The AMPEL360 BWB H2 Hy-E utilizes dual PEM fuel cell stacks for primary propulsion power. This section describes the normal startup procedure for the fuel cell system.

**Prerequisites:**
- Aircraft electrical power established (Battery or GPU)
- H₂ tank pressure verified (350-700 bar, green range)
- CAOS system initialized
- Pre-start checks completed

### FUEL CELL STARTUP PROCEDURE

#### STEP 1: SYSTEM PREPARATION

**PF (Pilot Flying) Actions:**
- Parking Brake: **SET**
- Fuel Cell Master Switch: **ON**

**PM (Pilot Monitoring) Actions:**
- Verify Fuel Cell Display: **READY**
- Confirm H₂ Tank Pressure: **GREEN RANGE**
- Check Fuel Cell Temperature: **40-90°C**

**CAOS Advisory:**
- Monitor CAOS startup advisory panel
- Verify "System Ready for Startup" indication

#### STEP 2: H₂ SYSTEM ACTIVATION

**PF Actions:**
1. H₂ Main Valve Switch: **OPEN**
   - Verify valve position indicator: **OPEN**
   - Monitor H₂ flow indication: **Increasing**

**PM Actions:**
- Call out: **"H₂ FLOW ESTABLISHED"**
- Monitor pressure: **Should remain stable**
- Check for leak indications: **NONE**

**Normal Indications:**
- H₂ valve open in 2-3 seconds
- Pressure stable or slight decrease (normal consumption)
- No leak warnings
- CAOS shows "H₂ System Normal"

**Abnormal Indications:**
- Valve fails to open: **See QRH**
- Pressure drop rapid: **CLOSE VALVE, See QRH**
- Leak detected: **CLOSE VALVE, Abort startup**

#### STEP 3: FUEL CELL STACK 1 STARTUP

**PF Actions:**
1. Fuel Cell Stack 1 Switch: **START**
   - Monitor temperature increase
   - Observe power output rise

**PM Actions:**
- Call out: **"STACK 1 STARTING"**
- Monitor Stack 1 parameters:
  - Temperature: **Rising to 60-80°C**
  - Voltage: **Rising to nominal**
  - Current: **Increasing with load**
  - Efficiency: **Should reach 90%+ within 2 min**

**Normal Startup Sequence:**
- Stack 1 switch to START position
- Initial power output: ~30% (within 10 seconds)
- Temperature rise: 60°C within 30 seconds
- Full power available: within 60 seconds
- CAOS indication: "Stack 1 Normal"

**Typical Timing:**
- 0:00 - Start initiated
- 0:10 - 30% power output
- 0:30 - 60°C temperature reached
- 0:60 - 95% power available
- 1:00 - Full operational

**PM Calls:**
- At 30% power: **"STACK 1 THIRTY PERCENT"**
- At 60°C: **"STACK 1 TEMPERATURE NORMAL"**
- At full operation: **"STACK 1 NORMAL"**

#### STEP 4: FUEL CELL STACK 2 STARTUP

**PF Actions:**
1. Wait for Stack 1 stabilization (minimum 60 seconds)
2. Fuel Cell Stack 2 Switch: **START**
   - Monitor same parameters as Stack 1

**PM Actions:**
- Call out: **"STACK 2 STARTING"**
- Monitor Stack 2 parameters (same as Stack 1)
- Compare Stack 1 and Stack 2 performance

**Normal Indications:**
- Stack 2 startup similar to Stack 1
- Both stacks showing similar parameters
- Combined power output available
- Load automatically distributed by system

**PM Calls:**
- At 30% power: **"STACK 2 THIRTY PERCENT"**
- At full operation: **"STACK 2 NORMAL, BOTH STACKS OPERATIONAL"**

#### STEP 5: SYSTEM VERIFICATION

**PF Actions:**
- Verify both stacks: **NORMAL OPERATION**
- Check electrical load distribution: **BALANCED**
- Confirm CAOS status: **GREEN**

**PM Actions:**
- Fuel Cell Display review:
  - Stack 1: Temp, voltage, current, efficiency
  - Stack 2: Temp, voltage, current, efficiency
  - H₂ flow rate: **Normal range**
  - Battery status: **Charging or ready**

**Completion Callout:**
- PM: **"FUEL CELL STARTUP COMPLETE, BOTH STACKS NORMAL"**
- PF: **"CHECKED"**

### NORMAL PARAMETERS POST-STARTUP

| Parameter | Normal Range | Typical Value |
|-----------|--------------|---------------|
| Stack 1 Temperature | 60-80°C | 70°C |
| Stack 2 Temperature | 60-80°C | 70°C |
| Stack 1 Efficiency | 90-98% | 95% |
| Stack 2 Efficiency | 90-98% | 95% |
| Total Power Output | 0.5-5.5 MW | Varies with load |
| H₂ Flow Rate | Variable | 0.2-4.5 kg/min |
| Battery SOC | >50% | 70-90% |

### CAOS SYSTEM INTEGRATION

During startup, CAOS provides:
- Startup sequencing guidance
- Parameter monitoring
- Anomaly detection
- Optimal warm-up recommendations
- Predictive diagnostics

**CAOS Advisories:**
- Green: Normal startup progression
- Amber: Parameter outside optimal (but within limits)
- Red: Abnormal condition - refer to QRH

### COLD WEATHER CONSIDERATIONS

**Temperature < -20°C:**
- Extended warm-up time required (add 30 seconds per stack)
- Fuel cell heater operation (automatic)
- Monitor temperature rise more carefully
- Battery may have reduced capacity

### HOT WEATHER CONSIDERATIONS

**Temperature > +30°C:**
- Ensure cooling system operating
- Monitor stack temperatures closely
- Cooling fans may run at high speed (normal)
- H₂ tank pressure may be higher (monitor)

### TIME REQUIRED

- Normal conditions: 3-4 minutes total
- Cold weather: 4-5 minutes total
- Hot weather: 3-4 minutes total

### NOTES

1. Stack startup can be performed individually if needed
2. Single stack operation is permitted (reduced power)
3. CAOS monitors startup progression automatically
4. Ground power can remain connected during startup
5. APU not required for fuel cell startup

---

**Document Format Evaluation:**
- Standard FCOM two-column format (this is simplified)
- Clear step-by-step procedures
- Normal indications provided
- Callouts specified
- CAOS integration explained
- Tables for quick reference
- Notes section for special considerations

**Pilot Feedback:**
- Clear and easy to follow
- Good integration of CAOS callouts
- Adequate normal indications
- Ready for production format
