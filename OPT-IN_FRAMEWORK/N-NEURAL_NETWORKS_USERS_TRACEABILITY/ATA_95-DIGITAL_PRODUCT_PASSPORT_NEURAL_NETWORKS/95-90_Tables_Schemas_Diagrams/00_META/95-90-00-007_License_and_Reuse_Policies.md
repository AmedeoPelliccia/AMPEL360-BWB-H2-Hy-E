# 95-90-00-007 — License and Reuse Policies

## 1. Purpose

This document defines the **licensing terms and reuse policies** for all tables, schemas, and diagrams in the 95-90 bucket, ensuring proper attribution and compliant usage.

## 2. License Framework

### 2.1 Primary License

All artifacts in the 95-90 bucket are licensed under:

**Apache License 2.0**

See: [LICENSE](../../../../../LICENSE) in repository root

Key provisions:
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Patent grant included
- ⚠️ Attribution required
- ⚠️ License notice required
- ⚠️ State changes required

### 2.2 Additional Terms

For AMPEL360-specific artifacts:
- Must maintain traceability to source
- Must preserve document control metadata
- Must not misrepresent as official without approval
- Derived works should reference original version

## 3. Artifact Categories

### 3.1 Public Artifacts

**Available for external use with attribution:**

| Category | Examples | Use Cases |
|----------|----------|-----------|
| Reference Schemas | Aircraft, Flight entities | Building compatible systems |
| Interface Specs | REST APIs, Message schemas | Integration implementations |
| Taxonomies | ATA mappings, Classifications | Cross-referencing |
| Diagram Templates | Style guides, Symbol libraries | Creating compatible diagrams |

**Requirements:**
- Include license notice
- Provide attribution
- Note modifications

### 3.2 Internal Artifacts

**Restricted to AMPEL360 program:**

| Category | Examples | Restrictions |
|----------|----------|--------------|
| Proprietary Designs | H₂ system specifics | Confidential, no external use |
| Certification Data | V&V results, Compliance tables | Program-internal only |
| Trade Secrets | Performance parameters | Protected information |
| Confidential Info | Partner data, Supplier specs | NDA-protected |

**Requirements:**
- Mark as CONFIDENTIAL or PROPRIETARY
- Follow data classification policies
- Restrict access to authorized personnel

### 3.3 Hybrid Artifacts

**Contain both public and internal elements:**

Example: Generic IMA partition schema (public) with AMPEL360-specific configurations (internal)

**Requirements:**
- Clearly separate public from internal sections
- Mark internal sections explicitly
- Provide public-only versions when possible

## 4. Reuse Guidelines

### 4.1 Within AMPEL360 Program

**Full reuse permitted:**
- All teams may use schemas and tables
- Modifications should be proposed via change control
- Derived artifacts should reference originals
- Update registry when creating derivatives

### 4.2 Academic Use

**Permitted with attribution:**
- Research and education
- Publications and presentations
- Must cite AMPEL360 as source
- Note: "Based on AMPEL360 BWB H₂ Hy-E schemas"

### 4.3 Commercial Use

**Requires assessment:**
- Public artifacts: Permitted with Apache 2.0 compliance
- Internal artifacts: Requires license agreement
- Integration use: Permitted for compatible systems
- Competitive use: Subject to legal review

### 4.4 Open Source Projects

**Encouraged with proper licensing:**
- Public schemas may be used in OSS projects
- Must maintain Apache 2.0 license
- Attribution required
- Contributions back to AMPEL360 welcomed

## 5. Attribution Requirements

### 5.1 Minimum Attribution

When using AMPEL360 schemas or tables:

```
Based on AMPEL360 BWB H₂ Hy-E Aircraft Schema v1.2.0
Copyright 2025 AMPEL360 Project
Licensed under Apache License 2.0
Source: https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E
```

### 5.2 Schema Metadata

Include in schema files:
```json
{
  "metadata": {
    "source": "AMPEL360 BWB H₂ Hy-E",
    "original_file": "95-90-02-A-001_Aircraft_and_Flight_Schema.json",
    "original_version": "1.2.0",
    "license": "Apache-2.0",
    "copyright": "2025 AMPEL360 Project"
  }
}
```

### 5.3 Documentation Attribution

In documentation:
> **Source:** AMPEL360 Digital Product Passport Schema v1.0  
> **License:** Apache License 2.0  
> **Repository:** github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E

## 6. Contribution Policy

### 6.1 Contributing Improvements

**Process:**
1. Fork repository (if external)
2. Create feature branch
3. Make improvements
4. Submit pull request
5. Sign Contributor License Agreement (CLA)
6. Review and merge

**Rights:**
- Contributors retain copyright
- Grant Apache 2.0 license to project
- Attribution in changelog and contributors list

### 6.2 Third-Party Schemas

When incorporating external schemas:
- Verify compatible license (Apache, MIT, BSD, etc.)
- Document source and license
- Maintain original attribution
- Add to THIRD_PARTY_NOTICES.md

### 6.3 Standards-Based Schemas

For schemas based on industry standards (ATA, ARINC, etc.):
- Reference standard specification
- Note any adaptations or extensions
- Comply with standard's terms of use
- Mark proprietary extensions clearly

## 7. Data Classification

### 7.1 Classification Levels

| Level | Description | Examples | Sharing |
|-------|-------------|----------|---------|
| PUBLIC | No restrictions | Generic schemas, API specs | Unrestricted |
| INTERNAL | AMPEL360 only | Design parameters, Calculations | Program team |
| CONFIDENTIAL | Restricted access | Performance data, Costs | Need-to-know |
| SECRET | Highly restricted | Trade secrets, IP | Authorized only |

### 7.2 Marking Requirements

Mark documents with classification:
```markdown
---
Classification: CONFIDENTIAL
Export Control: ITAR/EAR Not Applicable
Distribution: AMPEL360 Program Team Only
---
```

## 8. Export Control

### 8.1 Assessment

Technical data may be subject to:
- **ITAR** (International Traffic in Arms Regulations)
- **EAR** (Export Administration Regulations)
- **EU Dual-Use** Regulations

### 8.2 Current Status

AMPEL360 schemas (as of 2025-11-17):
- ✅ Generally not export-controlled
- ✅ Civilian aircraft technology
- ⚠️ Some propulsion data may require review
- ⚠️ Consult legal before international sharing

### 8.3 Marking

If export-controlled:
```markdown
---
Export Control: ITAR-Controlled
ECCN: 9E991
Distribution: U.S. Persons Only
---
```

## 9. Patent and IP Rights

### 9.1 Patent Rights

- AMPEL360 Project retains patent rights on innovations
- Apache 2.0 grants patent license for licensed use
- Contributors grant patent license on contributions
- Defensive termination clause applies

### 9.2 Trademark

"AMPEL360" and related marks:
- ® Registered trademark of AMPEL360 Project
- Use in attribution: Permitted
- Use in product names: Requires permission
- Descriptive use: Permitted ("compatible with AMPEL360 schemas")

### 9.3 Copyright

Copyright notices must be maintained:
```
Copyright 2025 AMPEL360 Project Contributors
SPDX-License-Identifier: Apache-2.0
```

## 10. Compliance and Enforcement

### 10.1 Monitoring

- Periodic review of external usage
- Community contributions tracked
- License compliance audits
- Proper attribution verification

### 10.2 Violations

If license violations occur:
1. Document violation
2. Contact violator (friendly notice first)
3. Request compliance
4. Legal action if necessary (last resort)

### 10.3 Good Faith

We prefer collaboration over enforcement:
- Honest mistakes: Help fix attribution
- Accidental violations: Work together to resolve
- Good faith users: Provide guidance
- Malicious actors: Protect project rights

## 11. Contact

### 11.1 License Questions

For licensing questions:
- **Email**: legal@ampel360.aero
- **Issue**: Open GitHub issue with `license` label

### 11.2 Permission Requests

For special permissions:
- **Email**: licensing@ampel360.aero
- **Include**: Intended use, scope, distribution

## 12. Updates

This policy may be updated. Check:
- **Version**: In document header
- **Last Updated**: 2025-11-17
- **Changelog**: In document control

## 13. Status

- **Document ID**: 95-90-00-007
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-11-17
- **Owner**: AMPEL360 Legal / Data Architecture WG

---

## Document Control

- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
- **License**: Apache License 2.0
