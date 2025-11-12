# ATA 02 - Operations Information
## Units of Measurement

**Document ID:** AMPEL360-02-00-00-OVR-UM  
**Version:** 1.0.0  
**Date:** 2025-11-04  
**Classification:** Operations Critical

---

## 1. PRIMARY UNITS

AMPEL360 documentation uses **SI (International System) units** as primary, with conversions provided where needed.

---

## 2. LENGTH / DISTANCE

### Primary Units
- **Meter (m)** - Short distances
- **Kilometer (km)** - Ground distances
- **Nautical Mile (NM)** - Aviation distances

### Conversions
| From | To | Multiply by |
|------|-----------|-------------|
| m | ft | 3.2808 |
| ft | m | 0.3048 |
| km | NM | 0.5400 |
| NM | km | 1.852 |
| m | in | 39.370 |
| in | m | 0.0254 |

### Examples
- Wingspan: 80.0 m (262 ft)
- Range: 3,500 NM (6,482 km)
- Height: 18.2 m (60 ft)

---

## 3. MASS / WEIGHT

### Primary Unit
- **Kilogram (kg)**

### Conversions
| From | To | Multiply by |
|------|-----------|-------------|
| kg | lb | 2.2046 |
| lb | kg | 0.4536 |
| tonne | kg | 1,000 |

### Examples
- MTOW: 80,000 kg (176,370 lb)
- H2 Fuel: 8,000 kg (17,637 lb)
- OEW: 42,000 kg (92,594 lb)

---

## 4. TEMPERATURE

### Primary Unit
- **Celsius (°C)**

### Conversions
| From | To | Formula |
|------|-----------|---------|
| °C | K | K = °C + 273.15 |
| K | °C | °C = K - 273.15 |
| °C | °F | °F = (°C × 9/5) + 32 |
| °F | °C | °C = (°F - 32) × 5/9 |

### Examples
- ISA Sea Level: +15°C (59°F, 288K)
- LH2 Storage: -253°C (-423°F, 20K)
- FC Operating: 60-80°C (140-176°F)

---

## 5. SPEED

### Primary Units
- **Knot (kt)** - Airspeed, wind
- **Mach (M)** - High-speed flight

### Conversions
| From | To | Multiply by |
|------|-----------|-------------|
| kt | km/h | 1.852 |
| km/h | kt | 0.5400 |
| kt | m/s | 0.5144 |
| m/s | kt | 1.944 |

### Mach Number
- M = TAS / Speed of sound
- Speed of sound (ISA, SL): 661 kt (340 m/s)

### Examples
- Cruise Speed: M0.82 (470 kt TAS)
- Vmo: 350 KIAS
- Crosswind Limit: 35 kt

---

## 6. PRESSURE

### Primary Units
- **Hectopascal (hPa)** - Atmospheric pressure
- **Bar** - System pressures
- **PSI (lb/in²)** - Some system pressures

### Conversions
| From | To | Multiply by |
|------|-----------|-------------|
| hPa | inHg | 0.02953 |
| inHg | hPa | 33.864 |
| bar | PSI | 14.504 |
| PSI | bar | 0.06895 |
| hPa | mb | 1.0 (identical) |

### Standard Values
- ISA Sea Level: 1013.25 hPa (29.92 inHg)
- Cabin Pressure (FL390): 2,450 m cabin alt (8,000 ft)
- H2 Tank Pressure: 3-5 bar

---

## 7. VOLUME / CAPACITY

### Primary Unit
- **Liter (L)** - Fluid volumes
- **Cubic meter (m³)** - Large volumes

### Conversions
| From | To | Multiply by |
|------|-----------|-------------|
| L | US gal | 0.2642 |
| US gal | L | 3.785 |
| L | Imp gal | 0.2200 |
| Imp gal | L | 4.546 |
| m³ | L | 1,000 |

### H2 Fuel
- Mass: kg (primary measure for H2)
- LH2 Density: 70.8 kg/m³
- 8,000 kg = 113 m³ (29,859 US gal)

---

## 8. POWER / ENERGY

### Primary Units
- **Megawatt (MW)** - Power
- **Kilowatt (kW)** - Power
- **Megajoule (MJ)** - Energy

### Conversions
| From | To | Multiply by |
|------|-----------|-------------|
| MW | HP | 1,341 |
| HP | kW | 0.7457 |
| kW | HP | 1.341 |
| MJ/kg | Wh/kg | 277.8 |

### Examples
- Fuel Cell Power: 4 × 2.5 MW = 10 MW
- H2 Energy Content: 120 MJ/kg
- Total FC Output: 10 MW (13,410 HP)

---

## 9. FUEL CONSUMPTION

### Primary Unit
- **Kilograms per hour (kg/h)** - H2 fuel flow

### Traditional Aviation
- Jet-A: typically kg/h or lb/h
- AMPEL360 H2: 50-80 kg/h cruise

### Energy Equivalence
- 1 kg H2 ≈ 3.5 kg Jet-A (energy)
- 50 kg/h H2 ≈ 175 kg/h Jet-A (energy)

---

## 10. ALTITUDE

### Primary Unit
- **Meter (m)**
- **Flight Level (FL)** - Altitude in hundreds of feet

### Conversions
| From | To | Multiply by |
|------|-----------|-------------|
| m | ft | 3.2808 |
| ft | m | 0.3048 |

### Flight Levels
- FL390 = 39,000 ft = 11,887 m
- FL450 = 45,000 ft = 13,716 m (service ceiling)

---

## 11. AREA

### Primary Unit
- **Square meter (m²)**

### Conversions
| From | To | Multiply by |
|------|-----------|-------------|
| m² | ft² | 10.764 |
| ft² | m² | 0.09290 |

### Examples
- Wing Area: 750 m² (8,073 ft²)
- Cargo Door: 7.5 m² (81 ft²)

---

## 12. ANGULAR MEASUREMENT

### Primary Unit
- **Degree (°)**

### Common Angles
- Takeoff Rotation: 5°/second
- Approach Angle: 3° (typical ILS)
- Bank Angle Limit: 30° (normal), 45° (max)

---

## 13. TIME

### Standard Units
- **Hour (h, hr)** - Flight time, endurance
- **Minute (min)** - Procedures, reserves
- **Second (s, sec)** - System response

### Examples
- H2 Refuel Time: 45 min
- FC Response Time: 3 sec
- Final Reserve: 45 min (675 kg H2)

---

## 14. CONVERSION TABLES

### Quick Reference: Length
| Meters | Feet | NM |
|--------|------|----|
| 1,000 | 3,281 | 0.54 |
| 1,852 | 6,076 | 1.00 |
| 10,000 | 32,808 | 5.40 |

### Quick Reference: Mass
| kg | lb |
|----|-----|
| 1 | 2.20 |
| 100 | 220 |
| 1,000 | 2,205 |
| 10,000 | 22,046 |

### Quick Reference: Speed
| Knots | km/h | Mach (ISA SL) |
|-------|------|---------------|
| 100 | 185 | 0.15 |
| 200 | 370 | 0.30 |
| 350 | 648 | 0.53 |
| 470 | 870 | 0.71 |

---

## 15. SPECIAL NOTES

### Hydrogen-Specific
- **Density (LH2):** 70.8 kg/m³ at -253°C
- **Energy Density:** 120 MJ/kg (33.3 kWh/kg)
- **Boil-Off Rate:** 0.3% per hour on ground

### ISA Standard Atmosphere
- **Sea Level:**
  - Pressure: 1013.25 hPa
  - Temperature: 15°C (59°F)
  - Density: 1.225 kg/m³
- **Temperature Lapse:** -6.5°C per 1,000 m (-1.98°C per 1,000 ft)
- **Tropopause:** 11,000 m (36,089 ft), -56.5°C

---

## 16. ROUNDING CONVENTIONS

### Operational Use
- **Fuel:** Round up to nearest 10 kg
- **Weight:** Round up to nearest 100 kg
- **CG:** Round to nearest 0.1% MAC
- **Speeds:** Round to nearest knot
- **Altitudes:** Round to nearest 100 ft (or FL)

### Performance Calculations
- Use full precision during calculation
- Round final result per above conventions
- Always round conservatively (safe direction)

---

**Document Status:** ✅ RELEASED  
**Effective Date:** 2029-01-01 (Entry Into Service)  
**Next Review:** 2026-11-04 (Annual)  
**Configuration Control:** Git SHA-256: [hash]
