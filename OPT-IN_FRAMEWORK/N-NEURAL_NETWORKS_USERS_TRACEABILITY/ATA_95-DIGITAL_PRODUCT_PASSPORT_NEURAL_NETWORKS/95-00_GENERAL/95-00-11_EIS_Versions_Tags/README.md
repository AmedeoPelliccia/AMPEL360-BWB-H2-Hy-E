# 95-00-11: EIS Versions Tags

## Purpose

This comprehensive documentation structure defines the Entry Into Service (EIS) versioning strategy, configuration management, and lifecycle management for the AMPEL360 BWB H₂ Hy-E aircraft program. It covers all aspects of version control from development through deployment, operations, and eventual retirement.

## Scope

This folder is part of the **95-00_GENERAL** layer, which provides governance and lifecycle management for ATA Chapter 95. It specifically addresses:

- **Entry Into Service Management**: Phased rollout strategies and operator onboarding
- **Version Control**: Semantic versioning for all configuration items
- **Configuration Management**: Baseline definition, approval, and change control
- **Neural Network Versioning**: Specific CM principles for AI/ML models
- **Digital Product Passport Integration**: Blockchain-anchored traceability
- **Fleet Operations**: Multi-aircraft and multi-operator configuration management
- **Deployment Orchestration**: Automated deployment through CAOS system
- **Monitoring & Audit**: Continuous monitoring and compliance traceability

---

## 📂 Complete Structure

### Root Documents
```
95-00-11_EIS_Versions_Tags/
├── README.md (this file)
├── 95-00-11-00-001_EIS_and_Versioning_Strategy.md
└── 95-00-11-00-002_Config_Management_Principles_for_NN.md
```

### 00_META/ — Metadata and Cross-Cutting Concerns
```
00_META/
├── 95-00-11-00-003_EIS_Versioning_Taxonomy.md
├── 95-00-11-00-004_Version_Traceability_Matrix.csv
├── 95-00-11-00-005_Baseline_Registry.json
├── 95-00-11-00-006_Environment_and_Channel_Map.md
└── 95-00-11-00-007_CAOS_EIS_Hooks.md
```

### 01_VERSIONING_MODEL/ — Core Versioning Framework
```
01_VERSIONING_MODEL/
├── 95-00-11-01-001_Versioning_Model_Overview.md
├── 95-00-11-01-002_Model_Data_DPP_Version_Coupling.md
├── 95-00-11-01-003_Semantic_Versioning_Rules.md
├── 95-00-11-01-004_EIS_Baselines_and_Derivatives.md
├── 95-00-11-01-005_Version_Compatibility_Policy.md
└── ASSETS/
    ├── 95-00-11-01-A-001_Versioning_Model_Diagram.drawio
    ├── 95-00-11-01-A-002_Version_States_StateMachine.svg
    ├── 95-00-11-01-A-003_Compatibility_Matrix.csv
    └── 95-00-11-01-A-004_Versioning_Examples.md
```

### 02_TAGGING_AND_NAMING/ — Naming Conventions
```
02_TAGGING_AND_NAMING/
├── 95-00-11-02-001_Tagging_Conventions.md
├── 95-00-11-02-002_Git_Branches_Tags_and_Release_Lines.md
├── 95-00-11-02-003_DPP_and_Blockchain_Tagging.md
├── 95-00-11-02-004_Environment_Channel_Tags.md
├── 95-00-11-02-005_Operator_and_Fleet_Tags.md
└── ASSETS/
    ├── 95-00-11-02-A-001_Tagging_Rules_Table.csv
    ├── 95-00-11-02-A-002_Tag_Name_Examples.md
    ├── 95-00-11-02-A-003_Git_Flow_with_Tags.drawio
    └── 95-00-11-02-A-004_Tag_to_DPP_Reference_Map.xlsx
```

### 03_CONFIG_BASELINES/ — Configuration Baseline Management
```
03_CONFIG_BASELINES/
├── 95-00-11-03-001_Config_Baseline_Definition.md
├── 95-00-11-03-002_Config_Items_for_NN_and_DPP.md
├── 95-00-11-03-003_Baseline_Approval_Process.md
├── 95-00-11-03-004_Variant_and_Option_Management.md
├── 95-00-11-03-005_Baseline_Change_Control.md
└── ASSETS/
    ├── 95-00-11-03-A-001_Config_Baseline_Template.md
    ├── 95-00-11-03-A-002_Config_Item_Registry.xlsx
    ├── 95-00-11-03-A-003_Variant_Management_Diagram.svg
    └── 95-00-11-03-A-004_Baseline_Change_Log.json
```

### 04_EIS_PHASES_AND_ROLLOUT/ — Entry Into Service Phases
```
04_EIS_PHASES_AND_ROLLOUT/
├── 95-00-11-04-001_EIS_Phases_Definition.md
├── 95-00-11-04-002_Pilot_Operator_and_Fleet_Intro.md
├── 95-00-11-04-003_Phased_Rollout_Strategies.md
├── 95-00-11-04-004_Risk_and_Mitigation_per_EIS_Phase.md
├── 95-00-11-04-005_Relationship_to_Cert_and_Production.md
└── ASSETS/
    ├── 95-00-11-04-A-001_EIS_Phases_Timeline.svg
    ├── 95-00-11-04-A-002_Rollout_Wave_Plan_Template.md
    ├── 95-00-11-04-A-003_EIS_Risk_Matrix.xlsx
    └── 95-00-11-04-A-004_Operator_Onboarding_Checklist.md
```

### 05_FLEET_AND_AIRCRAFT_CONFIG/ — Fleet Configuration Management
```
05_FLEET_AND_AIRCRAFT_CONFIG/
├── 95-00-11-05-001_Fleet_Config_Model.md
├── 95-00-11-05-002_Aircraft_Specific_Config_and_Tail_Number_Map.md
├── 95-00-11-05-003_Operator_Specific_Configurations.md
├── 95-00-11-05-004_Fleet_Wide_Update_Strategy.md
├── 95-00-11-05-005_Config_to_EIS_Version_Mapping.md
└── ASSETS/
    ├── 95-00-11-05-A-001_Fleet_Config_Table.csv
    ├── 95-00-11-05-A-002_TailNumber_to_Version_Map.xlsx
    ├── 95-00-11-05-A-003_Operator_Config_Profiles.json
    └── 95-00-11-05-A-004_Fleet_Update_Plan_Template.md
```

### 06_CHANGE_LOGS_AND_RELEASE_NOTES/ — Change Documentation
```
06_CHANGE_LOGS_AND_RELEASE_NOTES/
├── 95-00-11-06-001_Change_Log_Policy.md
├── 95-00-11-06-002_Release_Types_and_Impact_Levels.md
├── 95-00-11-06-003_Release_Notes_Structure.md
├── 95-00-11-06-004_Change_Communication_to_Operators.md
├── 95-00-11-06-005_Links_to_Requirements_VV_and_Cert.md
└── ASSETS/
    ├── 95-00-11-06-A-001_Change_Log_Template.md
    ├── 95-00-11-06-A-002_Release_Impact_Classification_Table.csv
    ├── 95-00-11-06-A-003_Release_Notes_Example.md
    └── 95-00-11-06-A-004_Operator_Communication_Template.md
```

### 07_HOTFIXES_AND_BACKPORTS/ — Emergency Changes
```
07_HOTFIXES_AND_BACKPORTS/
├── 95-00-11-07-001_Hotfix_Strategy.md
├── 95-00-11-07-002_Backport_Policy.md
├── 95-00-11-07-003_Hotfix_to_Baseline_Integration.md
├── 95-00-11-07-004_Risk_Assessment_for_Hotfixes.md
├── 95-00-11-07-005_Emergency_Procedures_and_Rollback.md
└── ASSETS/
    ├── 95-00-11-07-A-001_Hotfix_Flowchart.drawio
    ├── 95-00-11-07-A-002_Backport_Matrix.xlsx
    ├── 95-00-11-07-A-003_Emergency_Change_Form_Template.md
    └── 95-00-11-07-A-004_Rollback_Playbook.md
```

### 08_DPP_VERSIONING_AND_ANCHORING/ — Digital Product Passport
```
08_DPP_VERSIONING_AND_ANCHORING/
├── 95-00-11-08-001_DPP_Versioning_Model.md
├── 95-00-11-08-002_DPP_Entries_per_EIS_Baseline.md
├── 95-00-11-08-003_Blockchain_Anchoring_for_Versions.md
├── 95-00-11-08-004_OnChain_Proofs_for_Configs_and_Evidence.md
├── 95-00-11-08-005_Privacy_Scope_for_OnChain_Data.md
└── ASSETS/
    ├── 95-00-11-08-A-001_DPP_Versioning_Sequence_Diagram.drawio
    ├── 95-00-11-08-A-002_DPP_Version_Record_Schema.json
    ├── 95-00-11-08-A-003_Blockchain_Anchor_Examples.md
    └── 95-00-11-08-A-004_DPP_Version_to_EIS_Map.xlsx
```

### 09_DATA_AND_MODEL_VERSION_LINKS/ — AI/ML Version Management
```
09_DATA_AND_MODEL_VERSION_LINKS/
├── 95-00-11-09-001_Data_Cuts_and_Model_Versions.md
├── 95-00-11-09-002_Experiment_to_Prod_Version_Promotion.md
├── 95-00-11-09-003_Links_to_95-00-06_Engineering_Artifacts.md
├── 95-00-11-09-004_Traceability_of_Scenarios_and_Edge_Cases.md
├── 95-00-11-09-005_Impact_of_Data_Changes_on_EIS_Versions.md
└── ASSETS/
    ├── 95-00-11-09-A-001_DataModel_Linkage_Table.csv
    ├── 95-00-11-09-A-002_Experiment_Promotion_Flow.svg
    ├── 95-00-11-09-A-003_Scenario_Coverage_Index.xlsx
    └── 95-00-11-09-A-004_Data_Change_Impact_Log.json
```

### 10_VV_CERT_AND_EIS_VERSION_LINKS/ — Certification Traceability
```
10_VV_CERT_AND_EIS_VERSION_LINKS/
├── 95-00-11-10-001_VV_Evidence_per_Version.md
├── 95-00-11-10-002_Cert_Basis_per_EIS_Baseline.md
├── 95-00-11-10-003_Doors_Between_95-00-07_and_95-00-10.md
├── 95-00-11-10-004_Limits_and_Operating_Envelopes_per_Version.md
├── 95-00-11-10-005_Audit_Trails_across_Versions.md
└── ASSETS/
    ├── 95-00-11-10-A-001_Version_to_Evidence_Matrix.xlsx
    ├── 95-00-11-10-A-002_EIS_Config_Limits_Table.csv
    ├── 95-00-11-10-A-003_Version_Audit_Trail_Diagram.drawio
    └── 95-00-11-10-A-004_Version_Specific_OML_Extract_Template.md
```

### 11_DEPLOYMENT_CHANNELS_AND_ENVIRONMENTS/ — Deployment Infrastructure
```
11_DEPLOYMENT_CHANNELS_AND_ENVIRONMENTS/
├── 95-00-11-11-001_Deployment_Channel_Model.md
├── 95-00-11-11-002_Env_Types_Dev_QA_PreProd_Prod.md
├── 95-00-11-11-003_Canary_and_Shadow_Rollouts.md
├── 95-00-11-11-004_Operator_Specific_Channels.md
├── 95-00-11-11-005_Env_Config_and_Tag_Rules.md
└── ASSETS/
    ├── 95-00-11-11-A-001_Channel_Architecture.svg
    ├── 95-00-11-11-A-002_Environment_Config_Template.yaml
    ├── 95-00-11-11-A-003_Channel_to_Version_Map.xlsx
    └── 95-00-11-11-A-004_Canary_Rollout_Playbook.md
```

### 12_MONITORING_AND_OBSERVABILITY_PER_VERSION/ — Operational Monitoring
```
12_MONITORING_AND_OBSERVABILITY_PER_VERSION/
├── 95-00-11-12-001_Observability_Strategy_per_EIS_Version.md
├── 95-00-11-12-002_Dashboards_and_KPIs_per_Version.md
├── 95-00-11-12-003_Alerts_and_Thresholds_per_Config.md
├── 95-00-11-12-004_Link_to_InService_Events_and_ADs.md
├── 95-00-11-12-005_Reporting_to_Operators_and_Authorities.md
└── ASSETS/
    ├── 95-00-11-12-A-001_Versioned_KPI_Dashboard_Sketch.svg
    ├── 95-00-11-12-A-002_Alert_Thresholds_Table.csv
    ├── 95-00-11-12-A-003_InService_Event_Report_Template.md
    └── 95-00-11-12-A-004_Versioned_Performance_Report_Template.md
```

### 13_AUDIT_AND_TRACEABILITY_QUERIES/ — Audit and Forensics
```
13_AUDIT_AND_TRACEABILITY_QUERIES/
├── 95-00-11-13-001_Audit_Questions_Supported_by_DPP.md
├── 95-00-11-13-002_Traceability_Query_Catalog.md
├── 95-00-11-13-003_Forensic_Analysis_and_Incident_Investigation.md
├── 95-00-11-13-004_Logs_and_Records_for_Version_Tracing.md
├── 95-00-11-13-005_Integration_with_CAOS_Query_Interfaces.md
└── ASSETS/
    ├── 95-00-11-13-A-001_Audit_Query_Examples.md
    ├── 95-00-11-13-A-002_Traceability_Query_Grammar.yaml
    ├── 95-00-11-13-A-003_Forensic_Timeline_Template.xlsx
    └── 95-00-11-13-A-004_Version_Log_Retention_Spec.json
```

### 14_RETIREMENT_AND_DECOMMISSIONING/ — End of Life Management
```
14_RETIREMENT_AND_DECOMMISSIONING/
├── 95-00-11-14-001_Version_Retirement_Policy.md
├── 95-00-11-14-002_Decommissioning_Procedures.md
├── 95-00-11-14-003_Marking_Obsolete_DPP_and_OnChain_Records.md
├── 95-00-11-14-004_LongTerm_Storage_and_Anonymization.md
├── 95-00-11-14-005_Operator_and_Authority_Notification_for_EoL.md
└── ASSETS/
    ├── 95-00-11-14-A-001_Retirement_Flowchart.drawio
    ├── 95-00-11-14-A-002_EoL_Version_List_Template.csv
    ├── 95-00-11-14-A-003_Anonymization_and_Retention_Spec.json
    └── 95-00-11-14-A-004_EoL_Communication_Template.md
```

---

## Key Features

### ✅ Comprehensive Coverage
- **134 files** across 30 folders
- **15 major topics** from versioning to retirement
- **82 main documents** plus 56 supporting assets
- Complete lifecycle coverage

### ✅ Regulatory Compliance
- **EASA CS-25**: Large aircraft certification
- **DO-178C/DO-254**: Software and hardware assurance
- **EU AI Act**: High-risk AI system transparency
- **EU DPP Regulation**: Digital product passport requirements
- **ISO standards**: Configuration management and quality

### ✅ CAOS Integration
- Automated deployment orchestration
- Real-time monitoring and alerting
- Blockchain-anchored DPP entries
- Fleet-wide learning and optimization
- Emergency rollback capabilities

### ✅ Neural Network Focus
- Specific CM principles for AI/ML models
- Training data versioning and lineage
- Model-data-DPP coupling
- Drift detection and monitoring
- Operational Design Domain (ODD) management

---

## Status

- **Phase**: EIS Versions Tags
- **Lifecycle Position**: 11 of 14
- **Status**: ✅ **Structure Complete** (Content: In Progress)
- **Last Updated**: 2025-11-17
- **Files Created**: 134 documents and assets
- **Folders**: 30 (including ASSETS folders)

---

## Document Maturity Levels

| Level | Count | Description |
|-------|-------|-------------|
| **Detailed** | 9 | Comprehensive content with examples |
| **Structured** | 35 | Standard structure with placeholders |
| **Placeholder** | 90 | Awaiting content development |

**Priority for development:** Core versioning documents (01-03), DPP integration (08), and CAOS hooks (00_META/007)

---

## Related Folders

Part of the canonical 14-folder lifecycle:
1. Overview → 2. Safety → 3. Requirements → 4. Design → 5. Interfaces → 6. Engineering → 7. V&V → 8. Prototyping → 9. Production Planning → 10. Certification → **11. EIS/Versions/Tags** → 12. Services → 13. Subsystems/Components → 14. Ops/Std/Sustain

---

## Cross-References

### Within ATA 95
- **95-00-01**: Overview (strategy alignment)
- **95-00-02**: Safety (NN safety considerations)
- **95-00-03**: Requirements (version-specific requirements)
- **95-00-06**: Engineering (model artifacts)
- **95-00-07**: V&V (version validation evidence)
- **95-00-10**: Certification (certification baselines)

### Other ATA Chapters
- **ATA 02**: Operations (operational configurations)
- **ATA 28**: Fuel System (H₂ configuration management)
- **ATA 40**: AI Integration (CAOS neural networks)
- **ATA 52**: Doors (hardware configuration examples)
- **ATA 92**: Model-Based Maintenance (CAOS integration)

---

## Document Control

- **Standard**: OPT-IN Framework v1.4 (ATA 95 canonical template)
- **Owner**: AMPEL360 Configuration Management Team
- **Primary Contact**: config-mgmt@ampel360.aero
- **Review Cycle**: Quarterly or upon major milestone
- **Next Review**: 2026-02-17

---

## Usage Guidelines

### For Engineers
1. Start with **95-00-11-00-001** for overall strategy
2. Refer to **95-00-11-00-003** for taxonomy and naming
3. Use **01_VERSIONING_MODEL** for semantic versioning rules
4. Follow **02_TAGGING_AND_NAMING** for Git and DPP tags

### For Operators
1. Review **04_EIS_PHASES_AND_ROLLOUT** for deployment schedule
2. Check **05_FLEET_AND_AIRCRAFT_CONFIG** for fleet-specific configs
3. Monitor **06_CHANGE_LOGS_AND_RELEASE_NOTES** for updates
4. Follow **07_HOTFIXES_AND_BACKPORTS** for emergency procedures

### For Certification Engineers
1. Reference **10_VV_CERT_AND_EIS_VERSION_LINKS** for evidence
2. Use **03_CONFIG_BASELINES** for baseline approval
3. Review **08_DPP_VERSIONING_AND_ANCHORING** for traceability
4. Check **13_AUDIT_AND_TRACEABILITY_QUERIES** for compliance

---

## Future Development

### Short Term (Q1 2026)
- [ ] Complete content for folders 01-07
- [ ] Develop detailed DPP schemas (folder 08)
- [ ] Create operator communication templates (folder 06)
- [ ] Establish monitoring dashboards (folder 12)

### Medium Term (Q2-Q3 2026)
- [ ] Populate all asset files with real examples
- [ ] Integrate with CAOS deployment system
- [ ] Validate with first EIS operator
- [ ] Complete audit query catalog (folder 13)

### Long Term (2027+)
- [ ] Continuous refinement based on operational data
- [ ] Automation of version lifecycle management
- [ ] AI-assisted configuration optimization
- [ ] Industry standardization efforts

---

**Document Classification:** Internal Use  
**Distribution:** Engineering, Operations, Quality, Certification teams  
**Feedback:** Submit via GitHub issues or config-mgmt@ampel360.aero
