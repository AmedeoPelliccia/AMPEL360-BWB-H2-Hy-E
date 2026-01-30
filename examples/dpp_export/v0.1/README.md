# DPP Export v0.1 — Example Documents

This directory contains example JSON documents that demonstrate the Aircraft Baseline DPP Export v0.1 format.

## Files

### manifest.json
Complete export package manifest for the AMPEL360 Q100 aircraft, including:
- Export metadata and identification
- File inventory with SHA-256 checksums
- Regulatory basis and validation status
- References to baseline, effectivity, software BOM, and SPDX SBOM

### baseline.json
Baseline configuration defining all major components for the Q100 aircraft:
- Fuselage structure (ATA 53)
- Hydrogen fuel cell propulsion system (ATA 61)
- Avionics and flight control computers (ATA 31)
- Cryogenic hydrogen storage (ATA 28)
- Component hierarchy, weights, and certification basis

### effectivity.json
Effectivity matrix showing component applicability:
- MSN (Manufacturer Serial Number) range rules
- Tail number (registration) specific configurations
- Production batch applicability
- Exclusion rules for test and prototype aircraft
- Modification and service bulletin references

### software_bom.json
Software Bill of Materials for all aircraft software:
- Flight Control Computer software (DO-178C DAL-A)
- Energy Management System (fuel cell/battery control)
- Flight Management System (navigation)
- In-Flight Entertainment System
- Cryogenic Tank Monitor
- Binary files, checksums, and load addresses
- Configuration files and dependencies

## Validation

All example files have been validated against their JSON Schema draft-07 definitions.

To validate:

```bash
cd /path/to/AMPEL360-BWB-H2-Hy-E
python3 tools/validate_dpp_export.py
```

## Integration Notes

These examples integrate with:
- **OPT-IN Framework**: ATA chapter structure aligns with `OPT-IN_FRAMEWORK/`
- **SBOM**: References to SPDX 2.3 format aircraft SBOM
- **Configuration Management**: Baseline IDs reference configuration control system

## Related Documentation

- [DPP Export v0.1 README](../../schemas/dpp_export/v0.1/README.md) — Complete specification
- [JSON Schema Draft-07](https://json-schema.org/draft-07/schema)
- [SPDX 2.3 Specification](https://spdx.github.io/spdx-spec/v2.3/)

---

**Note:** These are example documents with placeholder checksums and data. For production use, replace with actual component data, compute real checksums, and validate against certification requirements.
