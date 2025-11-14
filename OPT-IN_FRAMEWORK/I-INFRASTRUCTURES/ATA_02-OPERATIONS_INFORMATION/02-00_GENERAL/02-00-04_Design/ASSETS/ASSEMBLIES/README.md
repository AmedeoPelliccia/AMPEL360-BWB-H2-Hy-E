# ASSEMBLIES — ATA 02 / Design

**Rule:** Keep **source models and BOMs here**. Put **renders/exports** (PNG/PDF/JT snapshots) only in `../EXPORTS/`.

## Naming
`<XX>-<YY>-<ZZ>-A<nnn>_ASSY_<ShortName>.<ext>`
- Example: `02-00-04-A310_ASSY_GSE_Power_Cart.step`

BOM files live in `ASSEMBLIES/BOM/`:
`<AssetID>_BOM.csv` → `02-00-04-A310_ASSY_GSE_Power_Cart_BOM.csv`

## Minimal DET (append to BOM or as `<AssetID>.det.yaml`)
```yaml
det_version: 1
asset_id: 02-00-04-A310
category: ASSY
mass_properties:
  mass_kg: null
  cg: [null, null, null]   # x,y,z (m)
  inertia_tensor: [null, null, null, null, null, null]
trace:
  reqs: ["REQ-02-001"]
  odd:  ["ODD-01"]
  safety: ["HZ-02-0007"]
checksum: "<filled-by-CI>"
status: Draft
```

## Don'ts

* ❌ Do **not** store `…_EXPT_*.pdf/png` here (use `../EXPORTS/`).
* ❌ Do **not** duplicate lifecycle docs inside `ASSEMBLIES/`.
