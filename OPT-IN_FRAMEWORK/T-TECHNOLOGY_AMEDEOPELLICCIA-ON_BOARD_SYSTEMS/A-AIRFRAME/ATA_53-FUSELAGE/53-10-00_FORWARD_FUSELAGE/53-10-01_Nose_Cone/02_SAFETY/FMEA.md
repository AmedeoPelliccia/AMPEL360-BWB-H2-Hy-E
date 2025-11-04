# FMEA - Nose Cone (53-10-01)

## Document Information
- **Component:** 53-10-01 Nose Cone
- **Revision:** A
- **Date:** 2025-11-03

## Failure Modes

### FM-01: Radome Delamination
- **Cause:** Manufacturing defect, moisture ingress, impact damage
- **Effect:** Loss of weather radar function, potential aerodynamic degradation
- **Severity:** 3 (Major)
- **Occurrence:** 2 (Remote)
- **Detection:** 2 (Detectable via NDT, CAOS sensors)
- **RPN:** 12
- **Mitigation:** Quality control, periodic ultrasonic inspection, moisture barrier

### FM-02: Bird Strike Penetration
- **Cause:** 4 lb bird impact at 250 knots
- **Effect:** Structural damage, potential radar damage, debris ingestion
- **Severity:** 4 (Hazardous)
- **Occurrence:** 3 (Occasional - bird strikes occur)
- **Detection:** 1 (Immediate - visible damage, CAOS impact detection)
- **RPN:** 12
- **Mitigation:** Design for CS-25.631 bird strike, energy absorption, post-impact inspection

### FM-03: Lightning Strike Burn-Through
- **Cause:** 200 kA lightning strike (Zone 1A)
- **Effect:** Skin penetration, delamination, potential fire
- **Severity:** 4 (Hazardous)
- **Occurrence:** 2 (Remote with protection)
- **Detection:** 2 (Detectable post-flight)
- **RPN:** 16
- **Mitigation:** Conductive diverter strips, bonding < 2.5 milliohm, post-lightning inspection

### FM-04: Pitot Probe Blockage
- **Cause:** Ice, insects, debris, maintenance cover left on
- **Effect:** Erroneous airspeed indication
- **Severity:** 4 (Hazardous)
- **Occurrence:** 3 (Occasional)
- **Detection:** 1 (Immediate - airspeed disagree alert)
- **RPN:** 12
- **Mitigation:** Pitot heat, multiple probes (3×), disagree alert, pre-flight check

## Risk Summary
All failure modes have acceptable RPN < 25. Critical items (lightning, bird strike) have been designed to meet certification requirements.

## Revision History
| Rev | Date | Author | Changes |
|-----|------|--------|---------|
| A | 2025-11-03 | A. Pelliccia | Initial release |
