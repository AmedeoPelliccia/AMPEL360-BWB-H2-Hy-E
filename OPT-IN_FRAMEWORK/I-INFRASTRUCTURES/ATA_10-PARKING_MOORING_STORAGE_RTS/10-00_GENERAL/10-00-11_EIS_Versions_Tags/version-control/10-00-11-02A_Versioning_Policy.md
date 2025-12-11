# 10-00-11-02A: Versioning Policy

## Document Information
- **Document ID**: 10-00-11-02A
- **Title**: Versioning Policy
- **Version**: 1.0.0
- **Date**: 2025-12-11
- **Status**: DRAFT
- **Document Type**: policy

## Purpose

This policy establishes the versioning rules and governance for all AMPEL360-BWB-H2 aircraft program deliverables, ensuring consistent version management across documentation, software, hardware, and configuration items.

## Scope

This policy applies to:
- Technical documentation
- Software components
- Hardware assemblies
- Configuration items
- Test artifacts
- Certification deliverables
- H2 system configurations
- BWB-specific configurations

## Policy Statements

### 1. Mandatory Versioning

**POLICY 1.1**: All deliverables MUST be versioned using an approved versioning scheme.

**POLICY 1.2**: Version identifiers MUST be unique and non-reusable.

**POLICY 1.3**: Versions MUST be traceable to their source and change history.

### 2. Semantic Versioning

**POLICY 2.1**: Software and system configurations SHALL use Semantic Versioning 2.0.0 (MAJOR.MINOR.PATCH).

**POLICY 2.2**: Documentation SHALL use document-specific versioning (10-00-11-NNA format).

**POLICY 2.3**: Hardware assemblies SHALL use part number versioning with dash numbers.

### 3. Version Increment Rules

**POLICY 3.1 - MAJOR Version Increments**:
- Breaking changes to interfaces or compatibility
- Major system redesign
- Certification milestone achievement
- Entry Into Service (EIS)

**POLICY 3.2 - MINOR Version Increments**:
- New features or capabilities (backward-compatible)
- Design enhancements
- Additional functionality
- Non-breaking interface changes

**POLICY 3.3 - PATCH Version Increments**:
- Bug fixes (backward-compatible)
- Documentation corrections
- Non-functional improvements
- Clarifications without design impact

### 4. Pre-release Versioning

**POLICY 4.1**: Pre-release versions SHALL use suffixes: `-alpha`, `-beta`, `-rc` (release candidate).

**POLICY 4.2**: Alpha versions are for internal development only.

**POLICY 4.3**: Beta versions may be shared with selected partners.

**POLICY 4.4**: Release candidates are feature-complete and undergoing final verification.

**Example**: `0.5.0-beta.2` (Beta version 2 of the 0.5.0 release)

### 5. Document Revision Letters

**POLICY 5.1**: Document revisions SHALL use alphabetic suffixes (A, B, C, ..., Z).

**POLICY 5.2**: Revision A is the first official release.

**POLICY 5.3**: After revision Z, a new document number SHALL be assigned.

**POLICY 5.4**: Minor corrections without technical impact MAY use decimal notation (A.1, A.2).

### 6. Version Synchronization

**POLICY 6.1**: Related deliverables SHALL maintain version compatibility matrices.

**POLICY 6.2**: System integration points SHALL document minimum compatible versions.

**POLICY 6.3**: H2 system components SHALL maintain compatibility with aircraft baseline versions.

**POLICY 6.4**: BWB configurations SHALL track compatibility with standard configurations.

## Version Governance

### 7. Version Authority

**POLICY 7.1**: Configuration Manager has authority over version numbering scheme.

**POLICY 7.2**: Document Controller assigns document revision letters.

**POLICY 7.3**: System engineers determine software/system version increments.

**POLICY 7.4**: Configuration Control Board (CCB) approves MAJOR version releases.

### 8. Version Approval

**POLICY 8.1**: DRAFT versions do not require formal approval.

**POLICY 8.2**: IN_REVIEW versions require technical review before approval.

**POLICY 8.3**: APPROVED versions require CCB approval for release.

**POLICY 8.4**: RELEASED versions are under full configuration control.

### 9. Version Lifecycle

**POLICY 9.1**: Version states SHALL be one of:
- DRAFT - Under development
- IN_REVIEW - Under review
- APPROVED - Approved but not released
- RELEASED - Official release
- SUPERSEDED - Replaced by newer version
- OBSOLETE - No longer valid

**POLICY 9.2**: Transition between states requires documented approval.

**POLICY 9.3**: SUPERSEDED and OBSOLETE versions SHALL be archived.

## Special Versioning Rules

### 10. H2 System Versioning

**POLICY 10.1**: H2 safety-critical components require independent version tracking.

**POLICY 10.2**: Cryo system configurations maintain separate version lineage.

**POLICY 10.3**: H2 vent system changes increment independently from aircraft versions.

**POLICY 10.4**: H2 detection systems follow DO-178C software versioning if software-based.

### 11. BWB Configuration Versioning

**POLICY 11.1**: BWB structural configurations track separately from conventional variants.

**POLICY 11.2**: Ground handling equipment versions align with BWB configuration versions.

**POLICY 11.3**: BWB clearance requirements version with airframe changes.

### 12. Baseline Versioning

**POLICY 12.1**: Baselines SHALL be tagged with milestone identifiers (PDR, CDR, TRR, FAI, EIS).

**POLICY 12.2**: Baseline changes after establishment require CCB approval.

**POLICY 12.3**: Emergency baseline changes are permitted for safety issues with post-approval.

## Version Metadata

### 13. Required Metadata

**POLICY 13.1**: All versioned items SHALL include:
- Version identifier
- Release date
- Author/owner
- Approval status
- Change summary

**POLICY 13.2**: Metadata SHALL conform to `eis-metadata.schema.json`.

**POLICY 13.3**: Version history SHALL be maintained in revision_history field.

## Version Communication

### 14. Version Notifications

**POLICY 14.1**: MAJOR version releases require stakeholder notification.

**POLICY 14.2**: Release notes SHALL accompany all RELEASED versions.

**POLICY 14.3**: Breaking changes SHALL be highlighted in release communications.

**POLICY 14.4**: Deprecation notices SHALL precede OBSOLETE status by at least one MINOR version.

## Compliance and Enforcement

### 15. Compliance Requirements

**POLICY 15.1**: All project members SHALL comply with this versioning policy.

**POLICY 15.2**: Non-compliance SHALL be reported to Configuration Manager.

**POLICY 15.3**: Repeated non-compliance may result in access restrictions.

### 16. Policy Exceptions

**POLICY 16.1**: Exceptions require written approval from Configuration Manager.

**POLICY 16.2**: Safety-critical changes may override versioning rules with CCB approval.

**POLICY 16.3**: All exceptions SHALL be documented with justification.

## Standards and References

This policy aligns with:
- **Semantic Versioning 2.0.0**: https://semver.org/
- **ATA iSpec 2200**: Configuration Management
- **ISO 10007**: Quality Management - Configuration Management
- **SAE AS9100**: Quality Management Systems for Aviation
- **EASA Part 21**: Certification Procedures

## Related Documents

- 10-00-11-01A: Version Control Plan
- 10-00-11-03A: Semantic Versioning
- 10-00-11-04A: Change Log Policy

## Review and Updates

This policy is reviewed:
- Annually
- At each major milestone
- When standards or regulations change

## Document Control

- **Author**: AMPEL360 Configuration Management Team
- **Reviewer**: [To be assigned]
- **Approver**: [To be assigned]
- **Next Review**: 2026-12-11
- **Revision History**:
  - Rev A (v1.0.0) - 2025-12-11 - Initial release

---

**END OF DOCUMENT**
