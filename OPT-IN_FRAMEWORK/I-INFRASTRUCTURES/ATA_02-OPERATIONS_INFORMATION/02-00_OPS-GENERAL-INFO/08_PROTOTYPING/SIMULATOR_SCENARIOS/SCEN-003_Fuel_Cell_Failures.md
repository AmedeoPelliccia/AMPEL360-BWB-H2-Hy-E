# SCEN-003 - Fuel Cell Failure Scenarios

**Scenario ID:** SCEN-003  
**Version:** 1.0  
**Date:** 2025-09-25  
**Status:** Active Testing  
**Complexity:** High

## Scenario 3.1: Single Fuel Cell Stack Failure in Cruise

**Flight Profile:**
- Phase: Cruise at FL340
- 1:30 into 3:00 hour flight

**Initial Conditions:**
- Both stacks operating at 85% capacity
- Battery at 75% SOC
- Normal operations

**Event Trigger:**
- Fuel Cell Stack 1 output drops to zero
- MASTER CAUTION
- CAOS advisory: "Stack 1 failure - Stack 2 increasing load"

**Required Actions:**
1. Identify failed stack
2. Isolate Stack 1
3. Increase Stack 2 output to maximum
4. Engage battery assist
5. Shed non-essential electrical loads
6. Plan diversion to nearest suitable airport
7. Calculate revised endurance

**CAOS Support:**
- Automatic load transfer to Stack 2
- Battery discharge optimization
- Divert airport recommendations with fuel calculations
- Essential vs non-essential load advisory

**Training Objectives:**
- Single engine (stack) operations
- Load shedding procedures
- Battery management
- Diversion decision making

**Success Criteria:**
- Stack isolated within 1 minute
- Power balance maintained
- Safe diversion and landing
- Passenger comfort maintained

## Scenario 3.2: Dual Fuel Cell Failure - Full Battery Mode

**Flight Profile:**
- Phase: Cruise at FL280
- 45 minutes from destination

**Initial Conditions:**
- Normal operations
- Battery at 70% SOC

**Event Trigger:**
- Stack 1 fails
- 5 minutes later, Stack 2 fails
- MASTER WARNING
- Full battery emergency mode

**Required Actions:**
1. BOTH STACKS - SHUTDOWN (memory item)
2. BATTERY EMERGENCY MODE - ACTIVATE (memory item)
3. EMERGENCY DESCENT - INITIATE (memory item)
4. DECLARE MAYDAY
5. ALL NON-ESSENTIAL - OFF
6. Land at nearest airport IMMEDIATELY

**CAOS Support:**
- Emergency power management
- Maximum battery endurance calculation
- Nearest airport with emergency services
- Time to minimum battery critical

**Training Objectives:**
- Total propulsion failure response
- Emergency descent
- Maximum stress decision making
- Battery emergency mode operation

**Success Criteria:**
- Memory items within 15 seconds
- Emergency declared immediately
- Land before battery critical (15% SOC)
- No loss of control

## Scenario 3.3: Fuel Cell Thermal Runaway

**Flight Profile:**
- Phase: Climb at 12,000 ft

**Initial Conditions:**
- Both stacks under high load
- Normal operations

**Event Trigger:**
- Stack 2 temperature rapidly increasing
- EICAS warning: FC2 OVERHEAT
- Thermal runaway imminent
- Fire warning possible

**Required Actions:**
1. Reduce Stack 2 load immediately
2. Increase cooling flow
3. If temperature continues: SHUTDOWN Stack 2
4. Prepare for possible fire
5. Continue on Stack 1 + Battery
6. Return to departure airport or divert

**CAOS Support:**
- Temperature trend prediction
- Cooling system optimization
- Fire risk assessment
- Return vs continue decision support

**Training Objectives:**
- Thermal management
- Fire prevention
- Progressive failure management
- Quick decision making

**Success Criteria:**
- Temperature controlled or stack shut down
- Fire prevented or extinguished
- Safe return/diversion
- Proper prioritization

## Scenario 3.4: Fuel Cell Degraded Performance

**Flight Profile:**
- Phase: Throughout flight
- Multiple phases

**Initial Conditions:**
- Both stacks operating but degraded
- Stack 1: 70% efficiency
- Stack 2: 75% efficiency

**Event Trigger:**
- CAOS advisory: "Fuel cell performance degraded"
- Higher than normal H₂ consumption
- Reduced available power

**Required Actions:**
1. Acknowledge degraded performance
2. Reduce electrical loads
3. Plan more conservative fuel reserves
4. Consider reduced altitude
5. Possible diversion if performance insufficient
6. Report to maintenance after flight

**CAOS Support:**
- Performance monitoring
- Fuel endurance recalculation
- Optimal operating point recommendation
- Load management suggestions

**Training Objectives:**
- Recognize degraded performance
- Conservative fuel planning
- Long-term management
- Maintenance reporting

**Success Criteria:**
- Problem recognized early
- Appropriate conservative planning
- Safe completion of flight
- Proper documentation

## Scenario 3.5: Fuel Cell Fire Warning

**Flight Profile:**
- Phase: Any
- Surprise element

**Initial Conditions:**
- Normal or near-normal operations

**Event Trigger:**
- FIRE WARNING - FUEL CELL
- Possible smoke in cockpit/cabin
- Multiple warnings

**Required Actions:**
1. Identify affected fuel cell
2. SHUTDOWN affected fuel cell
3. H₂ SUPPLY - CLOSE
4. FIRE EXTINGUISHER - ACTIVATE
5. VENTILATION - MAXIMUM
6. Prepare for emergency landing
7. DECLARE MAYDAY

**CAOS Support:**
- Fire location identification
- Extinguisher status monitoring
- Emergency landing site selection
- Time-critical guidance

**Training Objectives:**
- Fire response
- Emergency procedures under stress
- Crew coordination
- Smoke/fire management

**Success Criteria:**
- Immediate correct identification
- Fire extinguished or contained
- Emergency landing executed safely
- Proper emergency declaration

## Debriefing Focus Areas

1. System knowledge
2. Memory item accuracy
3. CAOS interaction during stress
4. Battery management skills
5. Decision making speed and quality
6. Crew coordination
7. ATC communication
8. Passenger management

---

**Scenario Status:** Active Testing  
**Next Review:** After 10 simulator sessions  
**Complexity Rating:** 8/10
