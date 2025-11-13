# 28-60_Storages

## Purpose

Tanks, reservoirs, accumulators, cryo vessels

## Scope

This is a **cross-ATA root bucket** present in every ATA chapter. It provides a consistent location for tanks, reservoirs, accumulators, cryo vessels.

## Internal Structure

The internal structure of this bucket is **design-driven** and flexible:
- Organize contents based on how systems are conceived, designed, and implemented
- No mandatory 01-14 lifecycle duplication within buckets
- Maintain traceability to lifecycle phases via metadata or index files

## Naming Convention

Items within this bucket follow the pattern:
- **28-60-XX_DESCRIPTION**
  - 28 = ATA chapter
  - 60 = Bucket number
  - XX = Sequential number (00, 01, 02, etc.)
  - DESCRIPTION = Descriptive name

## Status

- **Bucket**: 60_Storages
- **Status**: Active
- **Applicability**: Universal (all ATA chapters)
- **Last Updated**: 2025-11-13

## Document Control

- **Standard**: OPT-IN Framework v1.1
- **Owner**: AMPEL360 Documentation WG

---

**Note**: If this bucket is not applicable to ATA 28, document the reason here. Do not remove the bucket.
