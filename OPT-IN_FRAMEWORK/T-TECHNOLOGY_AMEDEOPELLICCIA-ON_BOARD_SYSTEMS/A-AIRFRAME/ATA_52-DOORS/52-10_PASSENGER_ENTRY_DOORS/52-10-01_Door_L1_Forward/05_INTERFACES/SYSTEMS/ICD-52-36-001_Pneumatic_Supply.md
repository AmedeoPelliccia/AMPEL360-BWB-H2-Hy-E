# Interface Control Document
## Door L1 Forward Pneumatic Supply Interface

**ICD Number:** ICD-52-36-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 36 (Pneumatic System)

---

## 1. INTERFACE OVERVIEW

This ICD defines the pneumatic interface for door seal inflation and optional power assist.

---

## 2. PNEUMATIC REQUIREMENTS

### 2.1 Seal Inflation System
- Supply pressure: 15 psi regulated from bleed air
- Flow rate: 2 SCFM maximum
- Line size: 6mm (1/4") OD tubing
- Connection: MS33656-4 fitting at FS 105

### 2.2 Optional Power Assist
- Supply pressure: 3000 psi hydraulic or pneumatic TBD
- Reserved for future implementation

---

## 3. COMPONENTS

| Component | Specification | Location |
|-----------|---------------|----------|
| Pressure regulator | 15 psi output | Door controller |
| Solenoid valve | 28 VDC, 0.5A | Door frame |
| Tubing | MS27064-4C | Internal routing |
| Quick disconnect | MS3367-4 | Service point |

---

## 4. VERIFICATION

- [ ] Pressure regulation test
- [ ] Leak test (<0.1 SCFM @ 15 psi)
- [ ] Inflation time (<30 seconds)

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial draft |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
