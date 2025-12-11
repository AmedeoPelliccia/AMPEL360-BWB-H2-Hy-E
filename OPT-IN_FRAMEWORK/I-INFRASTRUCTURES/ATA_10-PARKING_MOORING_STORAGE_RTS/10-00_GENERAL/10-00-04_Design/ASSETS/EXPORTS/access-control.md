# Access Control — EXPORTS

## Purpose

This document defines the **access control policies** for design export packages under ATA Chapter 10. It specifies who can access, modify, sign, and release export packages, as well as distribution rules and security classifications.

---

## Security Classification

All export packages are classified according to the following levels:

### Classification Levels

| Level | Description | Examples |
|-------|-------------|----------|
| **PUBLIC** | Publicly available information | Marketing brochures, general specifications |
| **INTERNAL** | For AMPEL360 internal use only | Work-in-progress designs, draft documents |
| **CONFIDENTIAL** | Shared with authorized partners | Detailed drawings, assembly BOMs |
| **RESTRICTED** | Limited to specific recipients | Proprietary systems, trade secrets |
| **CERTIFICATION** | For regulatory authorities only | Compliance evidence, test reports |

**Default classification**: **CONFIDENTIAL**

---

## Authorized Recipients

### Internal Recipients

| Role | Access Level | Permissions |
|------|--------------|-------------|
| **Design Engineers** | READ, WRITE | Create and modify design packages |
| **Lead Design Engineer** | READ, WRITE, APPROVE | Approve packages for release |
| **Configuration Manager** | READ, WRITE, SIGN | Sign and release packages |
| **Chief Engineer** | READ, APPROVE, SIGN | Final approval authority |
| **Quality Assurance** | READ | Verify package compliance |
| **Certification Team** | READ | Access certification submissions |

### External Recipients

| Recipient Type | Classification | Access Level | Approval Required |
|----------------|----------------|--------------|-------------------|
| **Manufacturing Partners** | CONFIDENTIAL | READ | Lead Engineer |
| **Suppliers/Vendors** | CONFIDENTIAL | READ | Configuration Manager |
| **Certification Authorities** | CERTIFICATION | READ | Chief Engineer |
| **Regulatory Bodies (EASA, FAA)** | CERTIFICATION | READ | Chief Engineer |
| **Strategic Partners** | CONFIDENTIAL | READ | Chief Engineer |

---

## Access Levels

### READ
- View and download export packages
- Access manifests and checksums
- Verify signatures
- Generate reports

### WRITE
- Create new export packages
- Modify package contents
- Update manifests
- Generate checksums

### APPROVE
- Review packages for release
- Approve manifest completeness
- Authorize distribution

### SIGN
- Cryptographically sign packages
- Generate detached signatures
- Manage signing keys

### RELEASE
- Publish packages to external repositories
- Distribute to authorized recipients
- Archive final releases

---

## Distribution Rules

### Internal Distribution

1. **Work-in-Progress (WIP)**
   - Classification: INTERNAL
   - Distribution: Design team only
   - Location: `packages/` subdirectories
   - Retention: Until superseded

2. **Review Packages**
   - Classification: INTERNAL
   - Distribution: Design team + QA + Lead Engineer
   - Location: `packages/` subdirectories
   - Retention: Until approved or rejected

3. **Approved Packages**
   - Classification: CONFIDENTIAL
   - Distribution: All internal authorized recipients
   - Location: `packages/full-release/`
   - Retention: Per retention policy (10+ years)

### External Distribution

1. **Partner Releases**
   - Classification: CONFIDENTIAL
   - Approval: Lead Design Engineer
   - Medium: Secure file transfer (SFTP, HTTPS)
   - Retention: Permanent archive

2. **Supplier Packages**
   - Classification: CONFIDENTIAL
   - Approval: Configuration Manager
   - Medium: Secure portal or encrypted email
   - Retention: Contract lifecycle + 5 years

3. **Certification Submissions**
   - Classification: CERTIFICATION
   - Approval: Chief Engineer
   - Medium: Direct submission to authority portal
   - Retention: Certification lifecycle + 10 years

---

## Security Requirements

### Package Signing

All packages intended for external distribution **must** be:
- Cryptographically signed using GPG
- Verified before distribution
- Signed by authorized personnel only

**Authorized Signers:**
- Configuration Manager
- Chief Engineer
- Designated Release Engineer

### Checksum Verification

All packages **must** include:
- SHA256 checksums for all files
- Package-level checksum
- Verification script

### Encryption

Packages containing **RESTRICTED** or **CERTIFICATION** content **must** be:
- Encrypted using AES-256
- Transmitted over secure channels only
- Decryption keys managed separately

### Audit Trail

All access and distribution events **must** be logged:
- User identity
- Action performed (read, write, sign, release)
- Timestamp
- Package identifier
- Recipient (for distributions)

---

## Key Management

### GPG Keys

#### Internal Keys
- **Release Key**: Used for signing official releases
  - Location: `signatures/public-keys/release-key.asc`
  - Owner: Configuration Manager
  - Expiry: 2 years, renewable

- **Backup Key**: Emergency signing authority
  - Owner: Chief Engineer
  - Expiry: 2 years, renewable

#### External Keys
- **Partner Keys**: Public keys from external recipients
  - Location: `signatures/public-keys/partners/`
  - Used for: Verifying incoming packages, encrypting sensitive exports

### Key Rotation
- Keys rotated every **2 years**
- Old keys retained for **10 years** for verification of historical packages
- Key rotation announced **90 days** in advance

---

## Approval Workflow

### Package Release Approval

1. **Design Complete**
   - Design Engineers create package
   - Self-review and validation

2. **QA Review**
   - Quality Assurance verifies compliance
   - Validation reports generated

3. **Lead Engineer Approval**
   - Review package completeness
   - Approve for release or request changes

4. **Configuration Manager Sign**
   - Cryptographically sign package
   - Generate manifest

5. **Chief Engineer Release** (for external distribution)
   - Final approval for external release
   - Authorize distribution

### Emergency Releases

For time-critical releases:
- Chief Engineer can expedite approval
- QA review may be performed post-release
- Emergency release noted in manifest

---

## Non-Disclosure Agreements (NDAs)

All external recipients **must** have:
- Current NDA on file
- Specified access scope
- Expiration date tracked

**NDA Types:**
- **Mutual NDA**: For strategic partners
- **One-way NDA**: For suppliers and vendors
- **Authority Agreement**: For certification bodies (if required)

---

## Revocation & Incident Response

### Access Revocation

Access is immediately revoked when:
- Employment/contract termination
- Role change removing authorization
- Security policy violation
- Suspected compromise

### Incident Response

In case of unauthorized access or distribution:
1. **Immediate**: Revoke compromised credentials
2. **1 hour**: Notify Chief Engineer and Security Officer
3. **4 hours**: Assess impact and affected packages
4. **24 hours**: Issue incident report
5. **7 days**: Implement corrective actions

---

## Compliance & Audits

### Internal Audits
- **Quarterly**: Access log review
- **Annually**: Full security audit

### External Audits
- Certification authorities may audit access controls
- Partner audits per contract requirements

### Compliance Checks
- ITAR/EAR compliance (if applicable)
- GDPR compliance for personal data
- ISO 27001 alignment

---

## Contact

For access control questions or incidents:
- **Configuration Manager**: config-mgr@ampel360.aero
- **Chief Engineer**: chief-engineer@ampel360.aero
- **Security Officer**: security@ampel360.aero

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status**: DRAFT – Subject to human review and approval
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-09
- **Owner**: AMPEL360 Security & Configuration Management WG
- **Version**: 1.0.0
