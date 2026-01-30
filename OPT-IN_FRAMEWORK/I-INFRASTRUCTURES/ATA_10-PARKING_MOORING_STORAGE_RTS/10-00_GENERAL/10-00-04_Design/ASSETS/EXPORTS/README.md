# EXPORTS — Design Export Management

## Purpose

This directory manages **professional design export packages** for:
- **Handover** to manufacturing partners
- **Release** to suppliers and vendors
- **Certification submission** to authorities (EASA, FAA)
- **Archival** for long-term retention and compliance

All exports follow ATA Chapter 10 (Parking, Mooring, Storage & Return To Service) standards and include complete traceability, validation, and cryptographic verification.

---

## Directory Structure

```
EXPORTS/
├── README.md                      # This file
├── access-control.md              # Security policies and authorized recipients
│
├── manifests/                     # Export manifest definitions
│   ├── exports-manifest.schema.json
│   └── .gitkeep
│
├── packages/                      # Export packages by type
│   ├── drawings/                  # Engineering drawings (SVG, PDF, DXF)
│   ├── assemblies/                # Assembly packages with BOMs
│   ├── 3d-models/                 # 3D CAD models (STEP, IGES)
│   ├── boms/                      # Bill of Materials exports
│   ├── specs/                     # Specifications and data sheets
│   └── full-release/              # Complete release bundles
│
├── checksums/                     # SHA256 checksums for all packages
├── signatures/                    # Cryptographic signatures
│   └── public-keys/               # Public keys for verification
│
├── validation-reports/            # Automated validation results
├── release-notes/                 # Version history and changelogs
│   └── CHANGELOG.md
│
├── tooling/                       # Scripts for export management
│   ├── export-pack.sh             # Build and package exports
│   ├── generate-manifest.py       # Generate JSON manifests
│   ├── sign-package.sh            # Sign packages with GPG
│   └── verify-package.sh          # Verify signatures and checksums
│
├── ci/                            # CI/CD automation
│   ├── .github/workflows/
│   │   └── export-publish.yml     # GitHub Actions workflow
│   └── ci-scripts/
│       └── upload-to-artifactory.sh
│
└── archives/                      # Historical exports by year
    ├── 2024/
    └── 2025/
```

---

## Naming Conventions

### Package Filenames
```
<MODEL>-<ATA>-<SERIES>_<SHORT_DESC>_<YYYYMMDD>_v<MAJOR>[.MIN].<ext>
```

**Examples:**
- `Q100-10-800_H2System_20251201_v1.tar.gz`
- `Q100-10-00_GeneralDesign_20251215_v2.1.zip`

### Manifest Filenames
```
exports-manifest-<YYYYMMDD>-<HHMMSS>.json
```

**Example:**
- `exports-manifest-20251201-143022.json`

### Release Bundles
```
<MODEL>-ATA<CHAPTER>_EXPORT_<YYYYMMDD>_v<MAJOR>.<ext>
```

**Examples:**
- `Q100-ATA10_EXPORT_20251201_v1.tar.gz`
- `Q100-ATA10_EXPORT_20251201_v1.tar.gz.sig` (detached signature)
- `Q100-ATA10_EXPORT_20251201_v1.tar.gz.sha256` (checksum)

---

## Export Manifest

Each export package must include a **manifest** that describes:

### Required Fields
- `manifest_id` (UUID v4)
- `created_at` (ISO8601 timestamp)
- `created_by` (user email or system identifier)
- `model` (e.g., "Q100")
- `ata_chapter` (e.g., "10")
- `version` (semantic version or date-based)
- `packages` (array of package objects)
- `validators` (list of validation checks performed)
- `approvals` (list of approver records)
- `notes` (free-text comments)

### Package Object Fields
- `filename` (package file name)
- `package_type` (drawings, assemblies, 3d-models, boms, specs, full-release)
- `size_bytes` (file size)
- `sha256` (checksum hash)
- `signed` (boolean, whether package is cryptographically signed)
- `included_files_count` (number of files in package)
- `related_requirements` (array of requirement IDs)
- `related_assemblies` (array of assembly IDs)

### Example Manifest Snippet

```json
{
  "manifest_id": "550e8400-e29b-41d4-a716-446655440000",
  "created_at": "2025-12-01T14:30:22Z",
  "created_by": "release-automation@ampel360.aero",
  "model": "Q100",
  "ata_chapter": "10",
  "release_tag": "v1.0.0-ATA10",
  "version": "1.0.0",
  "packages": [
    {
      "filename": "Q100-10-800_H2System_20251201_v1.tar.gz",
      "package_type": "full-release",
      "size_bytes": 52428800,
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "signed": true,
      "included_files_count": 247,
      "related_requirements": ["REQ-10-800-001", "REQ-10-800-015"],
      "related_assemblies": ["ASM-10-800-001"]
    }
  ],
  "validators": [
    {
      "validator": "schema-validator",
      "version": "1.0",
      "result": "PASS",
      "timestamp": "2025-12-01T14:25:10Z"
    },
    {
      "validator": "drawing-metadata-checker",
      "version": "2.1",
      "result": "PASS",
      "timestamp": "2025-12-01T14:25:45Z"
    }
  ],
  "approvals": [
    {
      "approver": "john.doe@ampel360.aero",
      "role": "Lead Design Engineer",
      "timestamp": "2025-12-01T14:28:00Z",
      "signature": "gpg-signature-hash"
    }
  ],
  "notes": "Initial release for H2 system design export. Includes all drawings, assemblies, and BOMs for ATA 10-800 series."
}
```

---

## Package Contents Requirements

Every export package **must** contain:

1. **package-metadata.json** — Package-level metadata
2. **All asset files** — SVG, STEP, PDF, XLSX, MD files as applicable
3. **checksums/** — Per-file SHA256 checksums
4. **signatures/** — Detached signatures (if signed)
5. **index.csv** or **index.json** — File inventory
6. **readme.md** — Package scope, effectivity, and usage notes

### Package Metadata Example

```json
{
  "package_id": "PKG-10-800-20251201",
  "package_type": "full-release",
  "ata_series": "10-800",
  "effectivity": "Q100 BWB-H2",
  "created_at": "2025-12-01T14:30:22Z",
  "created_by": "release-automation@ampel360.aero",
  "version": "1.0.0",
  "file_count": 247,
  "total_size_bytes": 52428800
}
```

---

## Metadata & Schemas

All manifests must validate against:
- **exports-manifest.schema.json** (located in `manifests/`)

Supporting schemas:
- **AMPEL360_ASSETS_STANDARD.md** — Asset naming conventions
- **AMPEL360_DOCUMENTATION_STANDARD.md** — Documentation standards
- **ATA_03_NUMBERING_GUIDE.md** — ATA numbering guidelines

---

## CI/CD Automation

### GitHub Actions Workflow

The `ci/.github/workflows/export-publish.yml` workflow automates:
1. **Validation** — Schema checks, drawing metadata, BOM consistency
2. **Packaging** — Build per-series packages
3. **Manifest generation** — Create JSON manifests
4. **Checksum computation** — Generate SHA256 hashes
5. **Signing** — Cryptographically sign packages (GPG)
6. **Publishing** — Upload to artifact repository

### Triggering Exports

```bash
# Manual trigger via GitHub Actions UI
# Or via command line:
gh workflow run export-publish.yml \
  --ref main \
  -f series="10-800" \
  -f version="v1.0.0"
```

---

## Verification & Evidence

All exports undergo automated validation:

### Pre-Export Checks
- **Schema validation** — Manifests match schema
- **Drawing metadata** — All drawings have valid metadata
- **BOM completeness** — All parts referenced in BOMs exist
- **File integrity** — No corrupted or missing files
- **Naming compliance** — All files follow naming conventions

### Post-Export Verification
- **Checksum verification** — SHA256 hashes match
- **Signature verification** — GPG signatures valid
- **Manifest completeness** — All required fields present

Validation reports are stored in `validation-reports/` directory.

---

## Security & Signing

### Signing Process

All release packages are cryptographically signed using **GPG**:

1. **Generate key pair** (if not exists):
   ```bash
   gpg --full-generate-key
   ```

2. **Export public key**:
   ```bash
   gpg --armor --export release@ampel360.aero > signatures/public-keys/release-key.asc
   ```

3. **Sign package**:
   ```bash
   bash tooling/sign-package.sh Q100-ATA10_EXPORT_20251201_v1.tar.gz
   ```

4. **Verify signature**:
   ```bash
   bash tooling/verify-package.sh Q100-ATA10_EXPORT_20251201_v1.tar.gz
   ```

### Access Control

See **access-control.md** for:
- Authorized recipients
- Distribution rules
- Access levels (read, write, sign, release)
- Security classification

---

## Archive & Retention Policy

### Retention Requirements
- **Keep all release exports** for certification lifecycle + **10 years**
- **Archives organized by year** in `archives/YYYY/`
- **Quarterly reviews** to ensure archive integrity

### Archive Structure
```
archives/
├── 2024/
│   ├── Q100-ATA10_EXPORT_20240301_v0.9.tar.gz
│   └── Q100-ATA10_EXPORT_20240615_v1.0.tar.gz
└── 2025/
    ├── Q100-ATA10_EXPORT_20250115_v1.1.tar.gz
    └── Q100-ATA10_EXPORT_20250401_v1.2.tar.gz
```

---

## Tooling Usage Examples

### Package Creation
```bash
# Create a release package for ATA 10-800 series
bash tooling/export-pack.sh \
  --series 10-800 \
  --date 20251201 \
  --version v1
```

### Manifest Generation
```bash
# Generate manifest from packages
python tooling/generate-manifest.py \
  --dir packages/full-release \
  --out manifests/exports-manifest-20251201-143022.json
```

### Package Signing
```bash
# Sign a package
bash tooling/sign-package.sh Q100-ATA10_EXPORT_20251201_v1.tar.gz
```

### Package Verification
```bash
# Verify signature and checksums
bash tooling/verify-package.sh Q100-ATA10_EXPORT_20251201_v1.tar.gz
```

### Upload to Artifact Repository
```bash
# Upload to Artifactory or S3
bash ci/ci-scripts/upload-to-artifactory.sh \
  Q100-ATA10_EXPORT_20251201_v1.tar.gz \
  releases/ATA10/v1.0.0/
```

---

## Related Documentation

- [AMPEL360_ASSETS_STANDARD.md](../../../../../../../AMPEL360_ASSETS_STANDARD.md)
- [AMPEL360_DOCUMENTATION_STANDARD.md](../../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md)
- [ATA_03_NUMBERING_GUIDE.md](../../../../../../../ATA_03_NUMBERING_GUIDE.md)
- [EXPORTS/access-control.md](./access-control.md)
- [EXPORTS/release-notes/CHANGELOG.md](./release-notes/CHANGELOG.md)

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status**: DRAFT – Subject to human review and approval
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-09
- **Owner**: AMPEL360 Design Release WG
- **Version**: 1.0.0
