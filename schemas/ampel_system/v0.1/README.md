# AMPELSystem Schema (v0.1)

This directory contains the canonical schema definition for the **AMPELSystem**
data model used to describe an AMPEL programme instance: project information,
mapping, detection, capture capsules, technologies, metrics, financial benefits,
stakeholders and potential clients.

## Files

| File | Purpose |
|------|---------|
| [`ampel_system.schema.json`](./ampel_system.schema.json) | JSON Schema (draft-07) – authoritative machine-readable definition. |
| [`ampel_system.xsd`](./ampel_system.xsd) | XML Schema mirror for XML interoperability. |
| [`example.ampel_system.json`](./example.ampel_system.json) | Minimal valid example instance. |

## Structure

```
AMPELSystem
├── ProjectInfo              { ProjectName, Description, StartDate, EndDate }
├── Mapping                  { MapID, MapName, Industry,
│                              MapProperties[ Property{ PropertyName, PropertyValue } ],
│                              MappingAlgorithms[ Algorithm{ AlgorithmName, AlgorithmDescription } ] }
├── Detection                { DetectionID, DetectionName,
│                              DetectionProperties[ Property ],
│                              DetectionAlgorithms[ Algorithm ] }
├── CaptureCapsules[ Capsule { CapsuleID, CapsuleName,
│                              CapsuleProperties[ Property ],
│                              CaptureMechanisms[ Mechanism{ MechanismName, MechanismDescription } ] } ]
├── Technologies[ Technology { TechnologyName, Description, IntegrationLevel } ]
├── Metrics[ Metric { MetricName, MetricValue } ]
├── FinancialBenefits[ Benefit { BenefitName, BenefitValue, StakeholderID, ClientID } ]
├── Stakeholders[ Stakeholder { StakeholderID, StakeholderName, StakeholderType, Contribution } ]
└── PotentialClients[ Client { ClientID, ClientName } ]
```

The hierarchy maps 1:1 to both the JSON Schema and the XSD; arrays in JSON
correspond to repeated child elements in XML (`Capsule`, `Technology`, etc.).

## Validation

JSON instances can be validated against the JSON Schema with any draft-07
validator, for example:

```bash
# Python (pip install jsonschema)
python -c "import json, jsonschema; \
  s=json.load(open('schemas/ampel_system/v0.1/ampel_system.schema.json')); \
  d=json.load(open('schemas/ampel_system/v0.1/example.ampel_system.json')); \
  jsonschema.validate(d, s); print('OK')"
```

XML instances can be validated against the XSD with any XML Schema 1.0
validator (e.g. `xmllint --schema ampel_system.xsd instance.xml --noout`).

## Versioning

This is version **v0.1** of the schema. Breaking changes will be published
under a new version directory (`v0.2`, `v1.0`, …) so existing consumers remain
stable.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2026-04-24_.

---
