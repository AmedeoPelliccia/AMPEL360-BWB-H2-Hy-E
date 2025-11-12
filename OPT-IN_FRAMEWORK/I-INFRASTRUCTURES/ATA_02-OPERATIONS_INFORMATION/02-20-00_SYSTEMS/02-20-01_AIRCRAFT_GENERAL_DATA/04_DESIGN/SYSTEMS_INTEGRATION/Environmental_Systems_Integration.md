# Environmental Systems Integration

## Executive Summary

The AMPEL360 environmental control and life support systems are integrated to provide passenger comfort, safety, and novel H2-related requirements while leveraging BWB advantages and fuel cell technology.

## Environmental Control System (ECS)

### Air Conditioning and Pressurization

**BWB Advantages:**
- Large cabin volume: 650 m³ (vs 400 m³ narrow-body)
- Wide cross-section: Better air distribution
- Lower cabin altitude: 6,500 ft at FL390 (vs 8,000 ft)
- Structural efficiency: Allows lower cabin altitude

**System Design:**
- Air source: Bleed from fuel cell compressors
- Conditioning: Electric heat pumps (fuel cell powered)
- Distribution: 6 independent zones
- Recirculation: 50% (HEPA filtered)

**Performance:**
- Temperature control: ±2°C in each zone
- Humidity: 20% maintained (vs 10% conventional)
- Air changes: 20 per hour
- Pressurization rate: < 500 fpm (comfortable)

### H2 Fuel Cell Waste Heat Recovery

**Available Heat:**
- Fuel cell rejection: 1.4 MW per stack at cruise
- Temperature: 75-80°C (ideal for cabin heating)
- Year-round: Excess heat available

**Heat Integration:**
```
Fuel Cell → Heat Exchanger → Cabin Heating → Overboard
                           ↓
                      Hot Water → Galley, Lavatories
```

**Benefits:**
- "Free" cabin heating (no electrical load)
- Reduced environmental system weight
- Improved overall efficiency
- Hot water for passenger service

### Thermal Management Integration

**Integrated Cooling:**
- Fuel cells: Primary heat source
- Electric motors: 13 kW each
- Avionics: 25 kW
- Environmental system: Integrated radiators

**Ram Air System:**
- Inlets: Wing leading edge
- Radiators: Fuel cell coolant, motor coolant
- Modulating doors: Temperature control
- Drag penalty: Minimized by efficient design

## Oxygen System

### Passenger Oxygen

**Type:** Chemical generators
- Drop-down masks: All passenger seats
- Duration: 15 minutes (regulatory minimum)
- Activation: Automatic or manual
- Pressure: Continuous flow above 14,000 ft cabin

**BWB Advantage:**
- Lower normal cabin altitude: Less frequent deployment need
- Large cabin volume: Slower depressurization
- Emergency descent: Adequate time to reach 10,000 ft

### Crew Oxygen

**Type:** Gaseous oxygen (high-pressure cylinders)
- Flight crew: Full-face masks, 100% O₂
- Duration: 2 hours per crew member
- Pressure demand: Prevents hypoxia in emergency
- Backup: Portable bottles for cabin crew

### H2 Safety Consideration

**Oxygen/Hydrogen Separation:**
- Oxygen storage: Far from H2 tanks
- Piping: No crossover zones
- Fire triangle prevention: O₂ + H₂ + ignition = explosion
- Safety analysis: Extensive FHA/SHA

## Fire Protection

### Detection

**Smoke Detection:**
- Lavatories: Mandatory (CS-25)
- Cargo compartments: Dual redundant
- Avionics bays: Optical sensors
- H2 compartments: Smoke + H2 sensors

**Heat Detection:**
- Fuel cell compartments: Rate-of-rise
- Motor compartments: Fixed temperature
- Baggage areas: Combination detectors

### Suppression

**Class C Cargo Compartments:**
- Agent: Halon 1301 alternative (HFC-125)
- Distribution: Full compartment flooding
- Discharge time: < 2 minutes
- Control: Automatic or manual

**H2 Fire Protection:**
- Prevention: Inert gas purging (nitrogen)
- Detection: H2 sensors (4 ppm)
- Suppression: Halon alternative
- Ventilation: Maximum flow, containment

**Portable Extinguishers:**
- Cabin: Halon 1211 or equivalent
- Flight deck: CO₂ for electrical fires
- Quantity: Per CS-25 requirements

## Water and Waste System

### Water System

**Potable Water:**
- Capacity: 300 liters
- Heating: Fuel cell waste heat
- Distribution: Galleys, lavatories
- Pressure: 50 psi

**Fuel Cell Product Water:**
- Production: 5.8 kg H₂O per kg H₂
- Use: Partial cabin humidification
- Quality: Distilled (high purity)
- Excess: Overboard dump (steam)

### Waste System

**Vacuum Toilets:**
- Type: Vacuum flush (water-efficient)
- Capacity: 300 liters (14 lavatories)
- Power: Electric vacuum pump
- Disposal: Ground servicing

## Ice and Rain Protection

### Anti-Ice System

**Leading Edge:**
- Type: Electro-thermal (powered by fuel cells)
- Coverage: Wings, empennage
- Power: 50 kW total
- Control: Automatic based on icing conditions

**Engine Inlets (Fuel Cells):**
- Heating: Electrical or hot air
- Protection: Ensures air flow to fuel cells
- Critical: Icing can starve fuel cell of air

**Sensors:**
- Ice detectors: Vibrating probe type
- Temperature: TAT and SAT
- Control: CAOS-integrated icing protection

### Rain Removal

**Windshield:**
- Wipers: Dual redundant
- Rain repellent: Optional
- Heating: Electric de-fog/de-ice
- Design: Unobstructed view in all conditions

## Pneumatic System

### Minimal Pneumatic Requirements

**BWB/H2 Advantage:**
- No engine bleed air (fuel cells don't have bleed)
- Electric systems: Replace traditional pneumatic
- Weight savings: No heavy bleed air ducting

**Remaining Pneumatic Functions:**
- Water tank pressurization: Electric pump
- Landing gear extension: Gravity backup (no pneumatic)
- Air conditioning: Electric compressors

### Inert Gas System

**Nitrogen Generation:**
- Purpose: H2 tank inerting (safety)
- Generation: Electric air separation module
- Purity: 95% N₂ minimum
- Storage: Low-pressure accumulators

**Uses:**
- H2 tank purging before maintenance
- H2 compartment inerting
- Fire suppression assist

## Cabin Systems Integration

### Lighting

**LED System:**
- Cabin: Circadian rhythm lighting (adjustable color temperature)
- Emergency: Battery-powered, photoluminescent
- Exterior: LED landing, taxi, navigation lights
- Power: Efficient (total lighting < 5 kW)

**Controls:**
- Crew panel: Master control
- Zone control: Cabin crew
- Automatic: Dim during cruise, bright for service
- Emergency: Independent power

### In-Flight Entertainment (IFE)

**System:**
- Streaming IFE: Centralized servers
- Seat displays: All classes (size varies)
- Connectivity: Satellite Wi-Fi (100 Mbps)
- Power: AC and USB-C at every seat

**Integration:**
- Power distribution: From fuel cell DC/AC inverters
- CAOS monitoring: System health
- Passenger amenity: Competitive with conventional

### Galley Equipment

**Electric Galleys:**
- Ovens: Electric (no gas)
- Coffee makers: Electric
- Refrigeration: Electric compressors
- Power: 30 kW total (managed by load controller)

**Load Management:**
- Non-simultaneous use: Ovens interlocked
- CAOS optimization: Minimizes peak power
- Battery buffering: Smooths load spikes

## Environmental Monitoring

### CAOS Integration

**Parameters Monitored:**
- Cabin temperature (6 zones)
- Cabin pressure and altitude
- Air quality (CO₂, humidity)
- H2 concentration (safety)
- Smoke detection status
- Fire suppression status

**Crew Alerting:**
- EICAS messages: Prioritized alerts
- Trend data: Predictive warnings
- Maintenance: Log exceedances

### Air Quality

**Monitoring:**
- CO₂: Target < 1,000 ppm (comfort)
- Humidity: 20% (better than conventional 10%)
- Temperature: Per passenger preferences
- Particulates: HEPA filtered (99.97% > 0.3 μm)

**Benefits:**
- Enhanced comfort: Higher humidity, lower cabin altitude
- Health: Better air quality
- Passenger satisfaction: Measurable improvement

## Certification Compliance

### CS-25 Requirements

**CS-25.831:** Ventilation
- 10 lb/min fresh air per occupant ✓
- Recirculation: Permitted if filtered ✓

**CS-25.841:** Pressurization
- Limit cabin altitude: 8,000 ft (AMPEL360: 6,500 ft) ✓
- Emergency descent: 10 minutes to 10,000 ft ✓

**CS-25.851-869:** Fire Protection
- Detection, suppression, extinguishing ✓
- Smoke evacuation capability ✓

**CS-25.1309:** Systems Safety
- Environmental systems: Single failure tolerant ✓
- H2 integration: Special conditions addressed ✓

### H2-Specific Safety Conditions

**Novel Aspects:**
- H2/O₂ separation: Demonstrated
- H2 fire protection: Validated by testing
- Ventilation: Prevents combustible concentrations
- Emergency procedures: Crew training required

---

**References:**
- Environmental Control: ATA 21-00-00
- Fire Protection: ATA 26-00-00
- Ice & Rain Protection: ATA 30-00-00
- Oxygen System: ATA 35-00-00
- Safety Analysis: SHA-ENV-2025-001
