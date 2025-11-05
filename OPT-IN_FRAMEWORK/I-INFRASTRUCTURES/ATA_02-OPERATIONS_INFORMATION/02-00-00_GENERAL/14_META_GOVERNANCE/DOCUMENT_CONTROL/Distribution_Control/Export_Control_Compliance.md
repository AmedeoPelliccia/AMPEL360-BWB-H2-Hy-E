# Export Control Compliance

**Document ID:** AMPEL360-02-00-00-META-EXPORT  
**Version:** 1.0.0  
**Effective Date:** 2025-09-01  
**Classification:** INTERNAL

## Purpose

This document establishes export control compliance procedures for AMPEL360 documentation to ensure compliance with:
- U.S. International Traffic in Arms Regulations (ITAR)
- U.S. Export Administration Regulations (EAR)
- EU Dual-Use Regulation
- Relevant international export control regimes

## Scope

Applies to all documentation that may contain:
- Technical data
- Software
- Technology
- Specific information related to defense articles or dual-use items

## Export Control Classification

### Preliminary Assessment

All documents must undergo preliminary export control assessment:

**Step 1: Determine if document contains technical data**
- Does it describe design, development, production, or use of technology?
- Does it contain specifications, drawings, algorithms, or code?

**Step 2: Determine applicable regulation**
- **ITAR**: Defense-related articles (military applications)
- **EAR**: Dual-use items (commercial and potential military use)
- **EAR99**: Items not subject to ITAR or specific EAR control

**Step 3: Classify and mark**
- Assign Export Control Classification Number (ECCN) if EAR
- Assign USML category if ITAR
- Mark document appropriately

### AMPEL360 Technology Classification

| Technology Area | Typical Classification | Rationale |
|----------------|----------------------|-----------|
| **BWB Aerodynamics** | EAR (ECCN 9E610) | Advanced aerodynamic tech |
| **H₂ Fuel System** | EAR (ECCN 9E610) | Aircraft propulsion |
| **Fuel Cell Technology** | EAR (ECCN 3A991) | Energy conversion |
| **CAOS AI System** | EAR (ECCN 4D994/4E992) | Machine learning tech |
| **Composite Structures** | EAR (ECCN 1C210/1E001) | Advanced materials |
| **Flight Control Software** | EAR (ECCN 9D610/9E610) | Flight control systems |

**Note**: Classifications are preliminary and subject to formal determination by Export Control Officer.

## Document Marking

### Export Controlled Documents

**Required Markings:**
```
EXPORT CONTROLLED
This document contains technical data subject to [ITAR/EAR].
Export or disclosure to foreign persons may require an export license.
[ECCN or USML Category]
```

**Header**: On every page
**Footer**: Copyright and proprietary notice
**Cover Page**: Full export control statement

### Export Control Statement (Cover Page)

```
EXPORT CONTROL NOTICE

This document contains technical data controlled under the [U.S. International Traffic in Arms Regulations (ITAR) 22 CFR 120-130 / Export Administration Regulations (EAR) 15 CFR 730-774] and may not be exported, released, or disclosed to foreign persons inside or outside the United States without prior authorization from the U.S. Department of State / U.S. Department of Commerce and AMPEL360 Export Control Office.

Violations of export control laws are subject to civil and criminal penalties including fines up to $1,000,000 and imprisonment up to 20 years.

Classification: [ECCN / USML Category]
Export Control Officer: exportcontrol@ampel360.aero
```

## Distribution Control

### Foreign Person Definition

A "foreign person" includes:
- Any person who is NOT a U.S. citizen
- Any person who is NOT a U.S. lawful permanent resident (green card holder)
- Any foreign corporation, business, organization, or government
- Any person acting on behalf of a foreign entity

### Distribution Authorization

**Before distributing export-controlled documents:**

1. **Verify recipient status**
   - U.S. person or foreign person?
   - Nationality and employer
   - Purpose of access

2. **Determine if export license required**
   - Is recipient a foreign person?
   - Is technology controlled?
   - Is there an applicable exemption?

3. **Obtain approval**
   - Submit request to Export Control Officer
   - Provide justification and recipient details
   - Await formal authorization

4. **Document authorization**
   - Log in distribution log
   - Retain approval record
   - Brief recipient on requirements

### Electronic Transmission

**Export-controlled documents transmitted electronically must:**
- Use approved secure transmission method
- Verify recipient authorization before sending
- Mark email subject line: "[EXPORT CONTROLLED]"
- Include export control notice in email body
- Log transmission

**Prohibited Methods:**
- Unencrypted email to foreign persons
- Public cloud storage without encryption
- Unsecured file sharing services
- Social media or public forums

## Deemed Exports

### Definition

A "deemed export" occurs when:
- Technology or technical data is released to a foreign person in the United States
- This is treated as an export to that person's country

### Examples in Documentation Context

- Foreign person employee accessing export-controlled documents
- Foreign person contractor reviewing technical drawings
- Foreign person visitor attending technical presentation
- Foreign person student participating in research

### Authorization Required

Deemed exports require:
- Export license OR license exemption
- Same process as physical export
- Pre-approval before access granted

## Training and Awareness

### Required Training

All personnel handling export-controlled documentation must complete:
- **Initial Training**: Within 30 days of hiring/role assignment
- **Annual Refresher**: Every 12 months
- **Ad-hoc Training**: When regulations change

Training topics:
- Export control overview (ITAR, EAR)
- Document classification
- Marking requirements
- Distribution procedures
- Deemed export rules
- Violations and penalties

### Awareness

Regular communications:
- Monthly export control reminders
- Regulatory updates
- Case studies and lessons learned

## Violations and Reporting

### Potential Violations

Report immediately if:
- Unauthorized distribution occurs
- Markings are missing or incorrect
- Foreign person gains unauthorized access
- Export occurs without required license
- Suspicious inquiries received

### Reporting Process

1. **Immediate**: Notify Export Control Officer
2. **Document**: Record details of potential violation
3. **Investigate**: Export Control Office investigates
4. **Remediate**: Implement corrective actions
5. **Report**: File voluntary self-disclosure if required
6. **Prevent**: Update procedures to prevent recurrence

### Penalties

Violations can result in:
- **Civil Penalties**: Fines up to $1,000,000 per violation
- **Criminal Penalties**: Imprisonment up to 20 years
- **Export Privileges Denied**: Company-wide export ban
- **Reputational Damage**: Loss of business opportunities

## Compliance Verification

### Quarterly Audits

Export Control Office conducts quarterly audits:
- Random sample of documents reviewed
- Marking compliance verified
- Distribution logs checked
- Training records confirmed

### Annual Certification

All document owners must annually certify:
- Export control classifications are current
- Markings are accurate
- Distribution is authorized
- Training is up-to-date

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Export Control Officer** | Overall compliance, classifications, license applications |
| **Documentation Manager** | Ensure marking compliance, distribution control |
| **Document Owners** | Identify export-controlled content, request classifications |
| **Security Team** | Access control, audit trails, security measures |
| **All Personnel** | Follow procedures, report violations, complete training |

## References

### Regulations
- ITAR: 22 CFR Parts 120-130
- EAR: 15 CFR Parts 730-774
- EU Dual-Use Regulation: (EC) No 428/2009

### Internal
- Proprietary Marking Guide (Proprietary_Marking_Guide.md)
- Distribution Matrix (Distribution_Matrix.csv)
- Access Control List (Access_Control_List.csv)

### External Resources
- U.S. Department of State (ITAR): https://www.pmddtc.state.gov/
- U.S. Department of Commerce (EAR): https://www.bis.doc.gov/
- Export Control Officer: exportcontrol@ampel360.aero

---

**Document Control:**
- Document ID: AMPEL360-02-00-00-META-EXPORT
- Version: 1.0.0
- Status: Released
- Classification: INTERNAL
- Owner: Export Control Officer
- Approved By: Chief Legal Officer
- Next Review: 2026-03-01 (Semi-annual)
