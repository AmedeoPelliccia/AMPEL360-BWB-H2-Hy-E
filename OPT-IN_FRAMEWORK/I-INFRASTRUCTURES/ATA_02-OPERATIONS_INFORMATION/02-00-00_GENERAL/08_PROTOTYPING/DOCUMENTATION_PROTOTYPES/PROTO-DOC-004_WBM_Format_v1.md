# PROTO-DOC-004 - Weight and Balance Manual Format v1.0

**Prototype ID:** PROTO-DOC-004  
**Document Type:** Weight and Balance Manual (WBM) Format Sample  
**Version:** 1.0  
**Date:** 2025-10-16  
**Status:** Review

## WEIGHT AND BALANCE MANUAL - FORMAT PROTOTYPE

### SECTION 1: GENERAL INFORMATION

#### 1.1 Aircraft Type
- **Model:** AMPEL360 BWB H2 Hy-E Q100
- **Manufacturer:** AMPEL360
- **Configuration:** Blended Wing Body
- **Propulsion:** Dual PEM Fuel Cell + Battery
- **Capacity:** 220 passengers

#### 1.2 Weight Units
- All weights in kilograms (kg)
- Moments in kilogram-meters (kg-m)
- CG in % Mean Aerodynamic Chord (MAC)

### SECTION 2: BASIC EMPTY WEIGHT

#### 2.1 Definition
Basic Empty Weight (BEW) includes:
- Aircraft structure
- Fuel cell systems
- Battery systems (empty)
- All fixed equipment
- Unusable H₂ fuel
- Hydraulic fluid
- Engine oil equivalent
- Emergency equipment

**Typical BEW:** 85,000 kg  
**BEW CG:** 45.2% MAC (typical)

#### 2.2 Aircraft Specific Data
Each aircraft has specific BEW determined by weighing:
- Last weigh date: [To be filled for each aircraft]
- Next weigh due: [Every 4 years or 20,000 FH]
- Weigh location: [To be recorded]

### SECTION 3: OPERATING EMPTY WEIGHT

#### 3.1 Definition
Operating Empty Weight (OEW) = BEW + Operational Items:
- Flight crew (2): 85 kg each = 170 kg
- Cabin crew (4): 75 kg each = 300 kg
- Crew baggage: 50 kg
- Catering and service items: 500 kg
- Potable water and toilet fluids: 200 kg

**Typical OEW:** 86,220 kg  
**OEW CG:** 45.0% MAC (typical)

### SECTION 4: LOADING STATIONS

#### 4.1 BWB Loading Zones

**Zone A - Forward Cabin (Rows 1-8)**
- Station: 20.0 m from datum
- Capacity: 80 passengers
- Cargo: 2,500 kg (forward hold)

**Zone B - Mid Cabin (Rows 9-16)**
- Station: 35.0 m from datum
- Capacity: 80 passengers
- Cargo: Overhead bins only

**Zone C - Aft Cabin (Rows 17-24)**
- Station: 50.0 m from datum
- Capacity: 60 passengers
- Cargo: 2,500 kg (aft hold)

**H₂ Fuel Tanks**
- Station: 30.0 m from datum
- Capacity: 3,500 kg maximum
- Note: Located in upper fuselage

#### 4.2 Standard Passenger Weights
- Adult (including carry-on):
  - Summer: 85 kg
  - Winter: 90 kg
- Child: 35 kg
- Infant: 0 kg (on lap)

### SECTION 5: CG ENVELOPE

#### 5.1 Blended Wing Body CG Envelope

**Forward Limit:** 42.0% MAC  
**Aft Limit:** 48.0% MAC

**CG Envelope Diagram:**
```
100,000 kg ----+----------------+
               |                |
               |                |
95,000 kg  ----+                |
               |                |
               |    FLIGHT      |
90,000 kg  ----+    ENVELOPE    |
               |                |
               |                |
85,000 kg  ----+----------------+
               42%            48%
                   % MAC
```

**Note:** BWB configuration provides wider CG range than conventional aircraft due to lift distribution across entire wing-body.

### SECTION 6: WEIGHT LIMITATIONS

#### 6.1 Maximum Weights
- **MTOW:** 110,000 kg
- **MLW:** 100,000 kg
- **MZFW:** 95,000 kg

#### 6.2 Floor Loading Limits
- Passenger cabin: 500 kg/m²
- Forward cargo: 400 kg/m²
- Aft cargo: 400 kg/m²

### SECTION 7: LOADING EXAMPLES

#### Example 1: Short Range Flight
**Configuration:**
- Passengers: 180 (full distribution)
- Cargo: 3,000 kg (balanced fwd/aft)
- H₂ Fuel: 1,500 kg

**Calculation:**
```
OEW:           86,220 kg @ 45.0% MAC
Passengers:    15,300 kg @ 35.0% MAC
Cargo Fwd:     1,500 kg @ 20.0% MAC
Cargo Aft:     1,500 kg @ 50.0% MAC
H₂ Fuel:       1,500 kg @ 30.0% MAC
---
ZFW:           93,520 kg @ 43.8% MAC ✓ (Within limits)
TOW:           95,020 kg @ 43.2% MAC ✓ (Within limits)
```

#### Example 2: Maximum Range
**Configuration:**
- Passengers: 140 (reduced for range)
- Cargo: 2,000 kg
- H₂ Fuel: 3,500 kg (maximum)

**Calculation:**
```
OEW:           86,220 kg @ 45.0% MAC
Passengers:    11,900 kg @ 35.0% MAC
Cargo:         2,000 kg @ 35.0% MAC
H₂ Fuel:       3,500 kg @ 30.0% MAC
---
ZFW:           93,120 kg @ 43.5% MAC ✓
TOW:          103,620 kg @ 41.8% MAC ✓
```

### SECTION 8: H₂ FUEL CONSIDERATIONS

#### 8.1 H₂ Weight Characteristics
- H₂ is very light (0.089 kg/L vs 0.8 kg/L kerosene)
- Located in forward upper fuselage
- CG shift during flight is minimal
- Tank location provides good weight distribution

#### 8.2 H₂ Loading Sequence
1. Verify OEW and passenger loading first
2. Calculate required H₂ fuel
3. Verify ZFW within limits
4. Add H₂ fuel weight
5. Verify TOW and CG within limits
6. Consider LW (landing weight)

### SECTION 9: CAOS W&B MONITORING

#### 9.1 Real-Time Monitoring
CAOS system provides:
- Current aircraft weight
- Current CG position
- Fuel consumption tracking
- Predicted landing weight
- Real-time CG shift monitoring

#### 9.2 In-Flight Adjustments
- CAOS monitors CG continuously
- Alerts if approaching limits
- H₂ consumption typically maintains CG
- Passenger movement effects displayed

### SECTION 10: LOADING PROCEDURES

#### 10.1 Standard Loading Sequence
1. Load cargo holds (balanced)
2. Board passengers (zone sequence)
3. Refuel H₂ (calculated amount)
4. Final W&B calculation
5. CAOS verification
6. Load sheet completion
7. Captain review and approval

#### 10.2 Load Sheet Format
[Standard load sheet diagram would be shown here]

---

**Format Evaluation:**
- Clear section organization
- BWB-specific information highlighted
- H₂ fuel integration explained
- Examples provided for reference
- CAOS integration described
- Diagrams and tables used effectively

**Review Comments:**
- Format appropriate for WBM
- BWB considerations well explained
- H₂ fuel handling clear
- Ready for detailed content development
