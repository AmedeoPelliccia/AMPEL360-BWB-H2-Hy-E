# ATA 28-10-10-04: Liquid Level Sensor (8-digit Level)

**Parent Assembly:** 28-10-10 - Primary H₂ Storage Tank  
**ATA Code:** 28-10-10-04  
**Level:** Component (8-digit)  
**Classification:** Safety Critical - DAL B

---

## Component Description

The Liquid Level Sensor is a capacitive probe-type sensor that measures the quantity of liquid hydrogen in the primary storage tank. The sensor operates on the principle that liquid hydrogen has a different dielectric constant than gaseous hydrogen, enabling accurate level measurement throughout the 0-100% range.

### Technical Specifications

| Parameter | Specification |
|-----------|---------------|
| **Measurement Principle** | Capacitive (dielectric constant sensing) |
| **Measurement Range** | 0-100% tank height |
| **Probe Length** | [TBD] mm (matches tank internal height) |
| **Accuracy** | ±2% of full scale |
| **Repeatability** | ±0.5% of full scale |
| **Resolution** | 0.1% of full scale |
| **Response Time** | < 1 second |
| **Operating Temperature** | -270°C to +85°C |
| **Pressure Rating** | 0 to [TBD] bar |
| **Output Signal** | 4-20mA analog + ARINC 429 digital |
| **Power Supply** | 28 VDC ±4V |
| **Power Consumption** | < 5W |
| **Weight** | 0.5 kg (approx) |
| **MTBF** | > 50,000 hours |

---

## 9-Digit Part Number Variants

### 28-10-10-041: Standard Production Unit
- **Full P/N:** AMPEL-28-LLS-041-A
- **Probe Length:** [TBD] mm (nominal for primary tank)
- **Configuration:** Standard calibration, primary tank
- **Quantity per Aircraft:** 1
- **Unit Cost:** $[TBD]
- **Manufacturer:** [Sensor Tech Inc.]
- **Lead Time:** 12 weeks ARO

### 28-10-10-042: Extended Range Variant
- **Full P/N:** AMPEL-28-LLS-042-A
- **Probe Length:** [TBD] mm +10% (dimensional tolerance accommodation)
- **Configuration:** Extended range calibration
- **Use Case:** Replacement unit when dimensional variation requires
- **Interchangeability:** Yes, with software calibration update
- **Unit Cost:** $[TBD]

### 28-10-10-043: Universal Service Unit
- **Full P/N:** AMPEL-28-LLS-043-A
- **Probe Length:** [TBD] mm (field-trimmable design)
- **Configuration:** Universal calibration, adjustable mounting
- **Use Case:** Spare parts inventory (reduces SKU count)
- **Field Trimming:** Can be cut to length with recalibration
- **Includes:** Calibration certificate, installation tools
- **Unit Cost:** $[TBD]

---

## Component Architecture

### Sensing Element
- **Capacitor Plates:** Concentric tubes (inner probe, outer reference)
- **Dielectric:** LH₂ (ε_r ≈ 1.23) vs. GH₂ (ε_r ≈ 1.00)
- **Capacitance Range:** [TBD] pF (empty) to [TBD] pF (full)
- **Frequency:** High-frequency AC excitation (~MHz range)

### Probe Structure
- **Inner Electrode:** Stainless steel 316L tube, [TBD] mm diameter
- **Outer Electrode:** Coaxial tube, [TBD] mm diameter
- **Insulator:** PTFE or ceramic spacers (cryogenic compatible)
- **Sealing:** Hermetically sealed, helium leak tested

### Electronics Housing
- **Material:** Aluminum alloy, anodized
- **Mounting:** Flange mount to tank boss penetration
- **Connector:** MIL-DTL-38999 Series III (environmental sealed)
- **Protection:** IP67 rating minimum
- **EMI Shielding:** Per DO-160 requirements

### Signal Processing
- **Capacitance-to-Digital Converter:** High-resolution (> 16-bit)
- **Temperature Compensation:** Internal temp sensor, lookup table correction
- **Linearization:** Software linearization for tank geometry
- **Output Drivers:** 4-20mA (galvanically isolated) + ARINC 429 (dual redundant)

---

## Principle of Operation

### Physical Principle
Capacitive Sensing: C = ε₀ · ε_r · A / d
- ε₀: Permittivity of free space
- ε_r: Relative permittivity (LH₂ ≈ 1.23, GH₂ ≈ 1.00)
- A: Electrode area
- d: Electrode spacing

### Signal Flow
```
LH₂ Level → Capacitance Change → AC Bridge → Demodulator → 
ADC → Microcontroller → Linearization + Temp Compensation → 
4-20mA Output + ARINC 429 Output → ATA 31 (Instrumentation)
```

---

## CAOS Integration (Component Level)

### Real-Time Monitoring
- **Signal Quality:** Monitor signal-to-noise ratio, detect degradation
- **Calibration Drift:** Compare sensor reading to calculated quantity
- **Cross-Sensor Validation:** If redundant sensor exists, cross-check values

### Predictive Maintenance
- **Drift Prediction:** ML model forecasts when sensor will exceed tolerance
- **Failure Precursors:** Identify patterns before complete failure
- **Maintenance Scheduling:** Optimal replacement window (minimize downtime)

### Digital Twin
- **Virtual Sensor:** Physics-based model of tank level vs. mass
- **Comparison:** Real sensor vs. virtual sensor (detects discrepancies)
- **Calibration Validation:** Digital twin confirms sensor accuracy

---

## Digital Product Passport (9-Digit Level)

Each individual sensor has a complete DPP entry:

```json
{
  "ata_code": "28-10-10-04",
  "part_number": "AMPEL-28-LLS-041-A",
  "serial_number": "LLS-25110101234",
  "manufacturing": {
    "manufacturer": "Sensor Tech Inc.",
    "manufacture_date": "2025-09-15",
    "factory_calibration_date": "2025-09-20",
    "calibration_certificate": "STC-CAL-2025-09-001234"
  },
  "installation": {
    "aircraft_msn": "AMPEL-BWB-001",
    "ata_location": "28-10-10 (Primary Tank)",
    "installed_date": "2025-10-01",
    "installed_by": "Tech ID 4567",
    "work_order": "WO-2025-10-001"
  },
  "operational_data": {
    "total_operating_hours": 456.3,
    "power_on_cycles": 89,
    "last_calibration_check": "2025-11-10",
    "calibration_error": "+0.3% (within spec)",
    "next_check_due": "2026-05-10"
  },
  "caos_health": {
    "health_score": 97.5,
    "predicted_time_to_failure": "12,400 hours",
    "recommended_action": "Continue monitoring",
    "anomalies_detected": 0
  }
}
```

---

## ATA Numbering Hierarchy Summary

This component demonstrates the complete hierarchy:

- **2-digit:** 28 = Fuel/Hydrogen Systems
- **4-digit:** 28-10-00 = H₂ Storage Tanks (subsystem)
- **6-digit:** 28-10-10 = Primary Storage Tank (assembly)
- **8-digit:** 28-10-10-04 = Liquid Level Sensor (component)
- **9-digit:** 28-10-10-041/042/043 = Part number variants

---

**Component Owner:** Instrumentation Engineering  
**Safety Classification:** DAL B  
**Last Update:** 2025-11-12  
**Generated by:** AMPEL360 Documentation Expert Agent
