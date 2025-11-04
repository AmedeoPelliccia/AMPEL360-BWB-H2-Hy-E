# Interface Control Document
## Door L1 Forward Ice Protection Interface

**ICD Number:** ICD-52-30-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 30 (Ice and Rain Protection)

---

## 1. INTERFACE OVERVIEW

This ICD defines ice and rain protection requirements for Door L1 Forward to ensure operation in all weather conditions.

---

## 2. ICE PROTECTION REQUIREMENTS

### 2.1 Ice Formation Areas
- Door seal area: Primary concern for ice bridging
- Drain holes: Can freeze in cold weather
- Latches: Ice can prevent engagement
- Hinges: Ice buildup affects operation

### 2.2 Ice Protection Methods
- Seal area: Heating elements (optional)
- Drains: Heat tracing (optional)
- Latches: Deicing fluid application (ground)
- Hinges: Covered design, minimal exposure

---

## 3. SEAL HEATING SYSTEM

### 3.1 Heated Seal Concept (Optional)
- Type: Electric heating elements in seal groove
- Power: 28 VDC, 5W/meter
- Total power: 30W for full perimeter
- Control: Automatic based on OAT <5°C
- Purpose: Prevent ice bridging across seal

### 3.2 Temperature Control
- Set point: Maintain >0°C at seal interface
- Sensor: RTD in seal groove
- Controller: PWM control to maintain temperature
- Safety: Over-temperature cutout at 50°C

---

## 4. DRAIN SYSTEM PROTECTION

### 4.1 Drain Tube Heating
- Type: Self-regulating heat trace cable
- Power: 5W/meter
- Length: 4 drains × 2 meters = 8 meters total
- Activation: Automatic when OAT <0°C
- Purpose: Prevent drain blockage

### 4.2 Drainage Path
- Slope: Minimum 1:100 for gravity drainage
- Trap prevention: No low points where water pools
- Discharge: Overboard below door sill
- Inspection: Regular check for blockage

---

## 5. OPERATIONAL PROCEDURES

### 5.1 Pre-Flight in Cold Weather
- Visual inspection: Check for ice on door seal
- Deicing: Apply Type I fluid if ice present
- Function test: Verify door operation
- Heating: Activate seal heating if installed

### 5.2 Ground Operations in Snow
- Snow removal: Clear door area before operation
- Deicing: Aircraft deicing includes door area
- Hand cleaning: Remove snow from handle and latches
- Inspection: Check seal compression after deicing

---

## 6. RAIN PROTECTION

### 6.1 Water Sealing
- Primary seal: Prevents water ingress
- Secondary seal: Blade seal for weather protection
- Drain system: Removes any water accumulation
- Testing: Water spray test per DO-160G

### 6.2 Heavy Rain Operations
- Normal operation: Door functions in heavy rain
- Seal effectiveness: No leakage in 100mm/hr rain
- Drainage capacity: 200 ml/min per drain
- Inspection: Check drains for debris

---

## 7. SYSTEM INTERFACES

### 7.1 Ice Detection System (Optional)
- Ice detector: Wing-mounted (aircraft level)
- Door activation: Based on aircraft ice detection
- Automatic: Seal heating on when icing conditions
- Manual override: Crew can activate heating

### 7.2 Anti-Ice Control
- Control panel: Flight deck ice protection panel
- Circuit breaker: 5A for seal heating
- Indication: Annunciator when heating active
- Monitoring: Current draw monitored by CAOS

---

## 8. ENVIRONMENTAL CONDITIONS

### 8.1 Icing Conditions
- Supercooled water: 0°C to -40°C, LWC 0-3 g/m³
- Freezing rain: Continuous maximum
- Snow: Heavy snow accumulation
- Mixed conditions: Rain and snow transitions

### 8.2 Temperature Extremes
- Cold: -55°C continuous operation
- Hot: +85°C exterior surface
- Thermal shock: Rapid transitions (deicing)
- Freeze-thaw cycles: 1000+ design life

---

## 9. VERIFICATION

- [ ] Cold weather testing (-40°C)
- [ ] Ice accumulation testing
- [ ] Heated seal system validation
- [ ] Rain ingress testing
- [ ] Freeze-thaw cycling

---

## 10. RESPONSIBILITIES

| Item | ATA 52 (Door) | ATA 30 (Ice Protection) |
|------|---------------|-------------------------|
| Door design | Provide | Requirements |
| Seal heating | Provide system | Power source |
| Drain heating | Provide system | Integration |
| Control system | Interface | Provide control |
| Testing | Support | Responsible |

---

## 11. IMPLEMENTATION STATUS

This interface is in conceptual phase. Seal heating system is optional based on operational requirements and route analysis.

**Decision factors:**
- Aircraft operating regions (cold weather exposure)
- Cost-benefit analysis
- Weight impact
- Power budget availability
- Maintenance complexity

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | TBD | Initial conceptual draft |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
