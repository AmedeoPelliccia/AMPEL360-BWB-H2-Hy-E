# Open Source Policy

## Purpose

This document defines the policy for selecting, using, and contributing open source software (OSS) within the AMPEL360 BWB H₂ Hy-E aircraft project.

## Scope

This policy applies to:
- All open source dependencies used in the project
- Tools and libraries integrated into the codebase
- CI/CD automation dependencies
- Development tools and utilities

## License Preferences

### Preferred Licenses (Permissive)

The following licenses are preferred for new dependencies:

1. **Apache License 2.0** ⭐ *Preferred*
   - Patent grant protection
   - Compatible with most commercial use cases
   - Clear attribution requirements

2. **MIT License** ✅ *Approved*
   - Simple and permissive
   - Minimal restrictions
   - Wide adoption

3. **BSD Licenses (2-Clause, 3-Clause)** ✅ *Approved*
   - Permissive terms
   - Well-understood requirements
   - Industry standard

4. **Python Software Foundation License** ✅ *Approved*
   - Standard for Python ecosystem
   - Compatible with Apache 2.0

### Acceptable Licenses (With Review)

These licenses require review before adoption:

- **Mozilla Public License 2.0 (MPL-2.0)** ⚠️ *Review Required*
  - Copyleft at file level
  - Patent grant included
  - Commercial use allowed

- **Eclipse Public License 2.0 (EPL-2.0)** ⚠️ *Review Required*
  - Weak copyleft
  - Patent provisions
  - Must evaluate impact

### Restricted Licenses

These licenses are generally **not permitted** without executive approval:

- **GNU GPL (v2, v3)** ❌ *Restricted*
  - Strong copyleft requirements
  - May require source disclosure
  - Incompatible with proprietary components

- **GNU AGPL (v3)** ❌ *Restricted*
  - Network copyleft
  - Service distribution triggers obligations
  - High compliance risk

- **SSPL (Server Side Public License)** ❌ *Restricted*
  - Non-OSI approved
  - Cloud service restrictions
  - Unclear legal implications

- **Proprietary/Closed Source** ❌ *Prohibited*
  - No source code access
  - Vendor lock-in risk
  - Licensing costs

## Dependency Selection Criteria

When evaluating a new open source dependency, consider:

### 1. License Compatibility ⚖️
- ✅ License is permissive (Apache, MIT, BSD)
- ✅ Compatible with Apache 2.0 project license
- ✅ No copyleft obligations that conflict with project goals
- ✅ Patent grants are clear

### 2. Project Health 💪
- ✅ Active maintenance (commits within last 6 months)
- ✅ Responsive maintainers (issues/PRs addressed)
- ✅ Regular releases
- ✅ Security vulnerability response process

### 3. Community & Support 👥
- ✅ Substantial user base (GitHub stars, downloads)
- ✅ Active community (contributors, discussions)
- ✅ Good documentation
- ✅ Available support channels

### 4. Security & Quality 🔒
- ✅ No known critical vulnerabilities
- ✅ Security advisories published when needed
- ✅ Code quality (tests, CI, code coverage)
- ✅ Dependency hygiene (minimal transitive dependencies)

### 5. Functionality & Fit 🎯
- ✅ Solves specific project need
- ✅ No unnecessary features (avoid bloat)
- ✅ Performance acceptable
- ✅ Compatible with project architecture

### 6. Long-term Viability 📈
- ✅ Stable API (not rapidly changing)
- ✅ Backward compatibility commitment
- ✅ Established project (not experimental)
- ✅ Alternative options available (no lock-in)

## Approval Process

### Automatic Approval
Dependencies meeting all criteria with preferred licenses can be added by any team member with documentation.

### Review Required
Dependencies with:
- Restricted licenses → Legal/Compliance review
- High security risk → Security team review
- Major architectural impact → Architecture review
- Cost implications → Budget approval

### Documentation Required
For each new dependency, document:
1. Purpose and justification
2. License type
3. Version pinned
4. Security scan results
5. Alternative evaluation

## Compliance Requirements

### SPDX Headers
All source files must include SPDX license identifier:

```python
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) AMPEL360 Project Contributors
```

### Attribution
Maintain `THIRD_PARTY_NOTICES.md` with:
- Dependency name and version
- License type
- Copyright holder
- Link to project

### SBOM Generation
- Automated SBOM (Software Bill of Materials) in CI
- Format: SPDX JSON
- Updated on every release
- Retained for audit trail

### License Scanning
- Automated license compliance checks in CI
- SkyWalking Eyes for header verification
- Syft/Anchore for SBOM generation
- pip-licenses for Python dependencies

## Security & Vulnerability Management

### Dependency Updates
- Regular updates (at least quarterly)
- Security patches applied immediately
- Breaking changes evaluated before update
- Changelog reviewed for each update

### Vulnerability Scanning
- GitHub Dependabot alerts enabled
- Regular vulnerability scans (e.g., Snyk, Safety)
- Critical vulnerabilities addressed within 7 days
- High vulnerabilities addressed within 30 days

### Response Process
1. Receive vulnerability notification
2. Assess impact and severity
3. Identify fix (update, patch, workaround)
4. Test fix in isolation
5. Deploy to staging, then production
6. Document resolution

## Prohibited Practices

❌ **Do NOT:**
- Use dependencies without license review
- Copy code from Stack Overflow without attribution
- Include proprietary libraries in open source components
- Ignore license incompatibilities
- Use outdated, unmaintained dependencies
- Add dependencies without scanning for vulnerabilities
- Commit credentials or secrets
- Use AI-generated code without review and attribution

## Contributing to Open Source

When contributing to upstream projects:

✅ **Do:**
- Follow project contribution guidelines
- Sign required CLAs (Contributor License Agreements)
- Ensure contributions align with project goals
- Document work time appropriately
- Use corporate email for contributions
- Respect project maintainer decisions

❌ **Don't:**
- Contribute proprietary code or algorithms
- Share confidential project information
- Commit to contributions without manager approval
- Violate project's code of conduct

## Exceptions & Waivers

Exceptions to this policy require written approval from:
- Technical Lead (for technical decisions)
- Legal/Compliance (for license exceptions)
- Project Manager (for budget/resource impact)

Document all exceptions with:
- Justification
- Risk assessment
- Mitigation plan
- Approval signatures
- Review date

## Review & Updates

This policy should be reviewed:
- Annually (minimum)
- When major dependencies change
- When license landscape evolves
- After security incidents
- Before major project milestones

## Resources

- **SPDX License List:** https://spdx.org/licenses/
- **Choose a License:** https://choosealicense.com/
- **OSI Approved Licenses:** https://opensource.org/licenses
- **Apache License 2.0:** https://www.apache.org/licenses/LICENSE-2.0

## Contact

For questions about this policy:
- Technical questions → Technical Lead
- License questions → Legal/Compliance team
- Security questions → Security team

---

**Policy Version:** 1.0  
**Effective Date:** 2025-11-13  
**Last Review:** 2025-11-13  
**Next Review:** 2026-11-13  

*This policy is subject to change. All team members are responsible for staying informed of updates.*
