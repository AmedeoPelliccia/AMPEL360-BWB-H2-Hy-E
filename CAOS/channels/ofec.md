# OFEC OPT-IN Framework Integration

## Operational Flight Envelope Channel — Directory Mapping

| Field               | Value                                                      |
|---------------------|------------------------------------------------------------|
| **Document ID**     | AMPEL360-OFEC-OPTIN-MAP-001                                |
| **Version**         | 1.0                                                        |
| **Date**            | 2025-11-27                                                 |
| **Status**          | DRAFT                                                      |
| **Classification**  | ARCHITECTURE / TELEMETRY CHANNEL                           |

---

## 1. Channel Overview

| Aspect | Value |
|--------|-------|
| **Channel Name** | OFEC — Operational Flight Envelope Channel |
| **Direction** | A→G/R (Aircraft to Ground/Regional) |
| **Data Type** | Flight envelope margins, advisory state |
| **Safety** | Read-only advisory (non-safety-critical) |
| **Update Rate** | Real-time, 1-10 Hz |
| **Standard** | AMPEL360-FAirCCC-ARCH-001 §4.1 |

---

## 2. Dual-Location Architecture

OFEC follows the OPT-IN separation of concerns:

| Aspect | N-Axis Location | L2-LINKS Location |
|--------|-----------------|-------------------|
| **Purpose** | What envelope data means | How to transmit it |
| **Content** | Margin calculations, advisory logic | Transport protocol, security |
| **ATA** | 97-40-40 (Envelope Analytics) | 23-95-60-60 (OFEC Protocol) |

### 2.1 N-Axis: Envelope Analytics (97-40-40)

```
OPT-IN_FRAMEWORK/
└── N-NEURAL_NETWORKS_USERS_TRACEABILITY/
    └── ATA_97-NEURAL_NETWORK_MODELS/
        └── 97-40_SOFTWARE/
            └── 97-40-40_ENVELOPE_ANALYTICS/     ← NEW
                ├── 97-40-40-00_GENERAL/
                ├── 97-40-40-10_MARGIN_CALCULATION/
                ├── 97-40-40-20_ADVISORY_LOGIC/
                ├── 97-40-40-30_ENVELOPE_MODELS/
                ├── 97-40-40-40_PERFORMANCE_ANALYSIS/
                ├── 97-40-40-50_PREDICTIVE_DYNAMICS/
                └── 97-40-40-90_SCHEMAS/
```

### 2.2 L2-LINKS: OFEC Protocol (23-95-60-60)

```
OPT-IN_FRAMEWORK/
└── T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/
    └── L2-LINKS/
        └── ATA_23-COMMUNICATIONS/
            └── 23-95_COMM_NN/
                └── 23-95-60_PROTOCOLS/
                    └── 60-60_OFEC/               ← NEW
                        ├── 60-60-00_GENERAL/
                        ├── 60-60-10_AIRCRAFT_PUBLISHER/
                        ├── 60-60-20_GROUND_RECEIVER/
                        ├── 60-60-30_REGIONAL_AGGREGATOR/
                        ├── 60-60-40_SECURITY/
                        └── 60-60-90_SCHEMAS/
```

---

## 3. N-Axis Structure (97-40-40 Envelope Analytics)

```
97-40-40_ENVELOPE_ANALYTICS/
│
├── 97-40-40-00_GENERAL/
│   ├── 00-01_Overview/
│   │   ├── ENVELOPE-ANALYTICS-OVERVIEW.md
│   │   └── ENVELOPE-GLOSSARY.md
│   ├── 00-02_Safety/
│   │   └── ENVELOPE-SAFETY-ASSESSMENT.md
│   ├── 00-03_Requirements/
│   │   ├── ENVELOPE-SRS.md
│   │   └── TRACEABILITY-MATRIX.md
│   ├── 00-04_Design/
│   │   ├── ENVELOPE-ARCHITECTURE.md
│   │   └── diagrams/
│   │       ├── envelope_dataflow.mermaid
│   │       └── margin_calculation.mermaid
│   ├── 00-05_Interfaces/
│   │   ├── ENVELOPE-ICD.md
│   │   ├── ATA22-INTERFACE.md      # Auto Flight
│   │   ├── ATA27-INTERFACE.md      # Flight Controls
│   │   └── ATA34-INTERFACE.md      # Navigation
│   ├── 00-06_Engineering/
│   ├── 00-07_V_AND_V/
│   │   └── ENVELOPE-VERIFICATION-PLAN.md
│   ├── 00-08_Prototyping/
│   ├── 00-09_Production_Planning/
│   ├── 00-10_Certification/
│   │   └── ENVELOPE-CERTIFICATION-PLAN.md
│   ├── 00-11_EIS_Versions_Tags/
│   ├── 00-12_Services/
│   ├── 00-13_Subsystems_Components/
│   └── 00-14_Ops_Std_Sustain/
│
├── 97-40-40-10_MARGIN_CALCULATION/
│   ├── MARGIN-CALCULATION-SPEC.md
│   ├── MARGIN-ALGORITHMS.md
│   ├── MARGIN-THRESHOLDS.yaml
│   └── src/
│       ├── margin_calculator.py
│       ├── alpha_margin.py           # Angle of attack margin
│       ├── speed_margin.py           # Vmin/Vmax margins
│       ├── load_factor_margin.py     # G-load margins
│       ├── altitude_margin.py        # Ceiling margins
│       └── bank_angle_margin.py      # Roll limits
│
├── 97-40-40-20_ADVISORY_LOGIC/
│   ├── ADVISORY-LOGIC-SPEC.md
│   ├── ADVISORY-RULES.yaml
│   ├── ALERT-THRESHOLDS.yaml
│   └── src/
│       ├── advisory_engine.py
│       ├── trend_analyzer.py
│       ├── exceedance_detector.py
│       └── recovery_advisor.py
│
├── 97-40-40-30_ENVELOPE_MODELS/
│   ├── ENVELOPE-MODELS-SPEC.md
│   ├── 30-10_Aerodynamic_Model/
│   │   ├── AERO-MODEL-SPEC.md
│   │   ├── AERO-COEFFICIENTS.yaml
│   │   └── src/
│   │       └── aero_model.py
│   ├── 30-20_Structural_Model/
│   │   ├── STRUCTURAL-MODEL-SPEC.md
│   │   ├── LOAD-LIMITS.yaml
│   │   └── src/
│   │       └── structural_model.py
│   ├── 30-30_Propulsion_Model/
│   │   ├── PROPULSION-MODEL-SPEC.md
│   │   ├── THRUST-LIMITS.yaml
│   │   └── src/
│   │       └── propulsion_model.py
│   └── 30-40_H2_Specific_Model/
│       ├── H2-ENVELOPE-SPEC.md
│       ├── H2-CONSTRAINTS.yaml
│       └── src/
│           └── h2_envelope_model.py
│
├── 97-40-40-40_PERFORMANCE_ANALYSIS/
│   ├── PERFORMANCE-ANALYSIS-SPEC.md
│   ├── 40-10_Real_Time/
│   │   ├── REALTIME-ANALYSIS-SPEC.md
│   │   └── src/
│   │       ├── realtime_analyzer.py
│   │       └── streaming_processor.py
│   ├── 40-20_Post_Flight/
│   │   ├── POST-FLIGHT-SPEC.md
│   │   └── src/
│   │       ├── post_flight_analyzer.py
│   │       └── report_generator.py
│   └── 40-30_Fleet_Aggregation/
│       ├── FLEET-AGGREGATION-SPEC.md
│       └── src/
│           └── fleet_aggregator.py
│
├── 97-40-40-50_PREDICTIVE_DYNAMICS/
│   ├── PREDICTIVE-DYNAMICS-SPEC.md
│   ├── 50-10_Short_Term/
│   │   ├── SHORT-TERM-PREDICTION.md
│   │   └── src/
│   │       └── short_term_predictor.py
│   ├── 50-20_Trend_Analysis/
│   │   ├── TREND-ANALYSIS.md
│   │   └── src/
│   │       └── trend_analyzer.py
│   └── 50-30_Anomaly_Detection/
│       ├── ANOMALY-DETECTION.md
│       └── src/
│           └── anomaly_detector.py
│
└── 97-40-40-90_SCHEMAS/
    ├── SCHEMAS-INDEX.md
    ├── envelope_state.schema.json
    ├── margin_data.schema.json
    ├── advisory_event.schema.json
    ├── performance_report.schema.json
    └── prediction.schema.json
```

---

## 4. L2-LINKS Structure (23-95-60-60 OFEC Protocol)

```
23-95-60_PROTOCOLS/
└── 60-60_OFEC/
    │
    ├── 60-60-00_GENERAL/
    │   ├── OFEC-PROTOCOL-OVERVIEW.md
    │   ├── OFEC-CHANNEL-SPEC.md
    │   └── diagrams/
    │       ├── ofec_dataflow.mermaid
    │       └── ofec_node_topology.mermaid
    │
    ├── 60-60-10_AIRCRAFT_PUBLISHER/
    │   ├── A-OFEC-SPEC.md
    │   ├── 10-10_Envelope_Sampler/
    │   │   ├── ENVELOPE-SAMPLER-SPEC.md
    │   │   ├── SAMPLE-RATE-CONFIG.yaml
    │   │   └── src/
    │   │       ├── envelope_sampler.py
    │   │       └── rate_controller.py
    │   ├── 10-20_Message_Builder/
    │   │   ├── MESSAGE-BUILDER-SPEC.md
    │   │   └── src/
    │   │       ├── message_builder.py
    │   │       └── cbor_encoder.py
    │   ├── 10-30_Phase_Aware_Publisher/
    │   │   ├── PHASE-AWARE-SPEC.md
    │   │   ├── PHASE-RATES.yaml
    │   │   └── src/
    │   │       └── phase_aware_publisher.py
    │   └── 10-90_Schemas/
    │       └── aircraft_ofec_message.schema.json
    │
    ├── 60-60-20_GROUND_RECEIVER/
    │   ├── G-OFEC-SPEC.md
    │   ├── 20-10_Message_Decoder/
    │   │   ├── DECODER-SPEC.md
    │   │   └── src/
    │   │       └── message_decoder.py
    │   ├── 20-20_Validation/
    │   │   ├── VALIDATION-SPEC.md
    │   │   └── src/
    │   │       └── envelope_validator.py
    │   ├── 20-30_Storage/
    │   │   ├── STORAGE-SPEC.md
    │   │   └── src/
    │   │       └── telemetry_store.py
    │   ├── 20-40_Alerting/
    │   │   ├── ALERTING-SPEC.md
    │   │   ├── ALERT-RULES.yaml
    │   │   └── src/
    │   │       └── alert_processor.py
    │   └── 20-90_Schemas/
    │       └── ground_ofec_record.schema.json
    │
    ├── 60-60-30_REGIONAL_AGGREGATOR/
    │   ├── R-OFEC-SPEC.md
    │   ├── 30-10_Multi_Aircraft_Aggregation/
    │   │   ├── AGGREGATION-SPEC.md
    │   │   └── src/
    │   │       └── multi_aircraft_aggregator.py
    │   ├── 30-20_Fleet_Analytics/
    │   │   ├── FLEET-ANALYTICS-SPEC.md
    │   │   └── src/
    │   │       └── fleet_analytics.py
    │   ├── 30-30_Uplink_To_Fleet_Core/
    │   │   ├── UPLINK-SPEC.md
    │   │   └── src/
    │   │       └── fleet_uplink.py
    │   └── 30-90_Schemas/
    │       └── regional_ofec_summary.schema.json
    │
    ├── 60-60-40_SECURITY/
    │   ├── OFEC-SECURITY-OVERVIEW.md
    │   ├── 40-10_Authentication/
    │   │   ├── AUTH-SPEC.md
    │   │   ├── MTLS-CONFIG.yaml
    │   │   └── src/
    │   │       └── ofec_auth.py
    │   ├── 40-20_Encryption/
    │   │   ├── ENCRYPTION-SPEC.md
    │   │   └── src/
    │   │       └── ofec_encryption.py
    │   ├── 40-30_Integrity/
    │   │   ├── INTEGRITY-SPEC.md
    │   │   └── src/
    │   │       └── integrity_checker.py
    │   └── 40-90_Schemas/
    │       └── ofec_security.schema.json
    │
    └── 60-60-90_SCHEMAS/
        ├── SCHEMAS-INDEX.md
        ├── ofec_envelope.schema.json
        ├── ofec_margin.schema.json
        ├── ofec_advisory.schema.json
        └── ofec_telemetry.schema.json
```

---

## 5. Data Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           OFEC DATA FLOW                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                    N-AXIS (97-40-40)                                │  │
│   │                  ENVELOPE ANALYTICS                                 │  │
│   │                                                                     │  │
│   │  ┌──────────────┐   ┌──────────────┐   ┌──────────────────────┐   │  │
│   │  │   Envelope   │──▶│    Margin    │──▶│    Advisory Logic    │   │  │
│   │  │    Models    │   │ Calculation  │   │                      │   │  │
│   │  │              │   │              │   │  • Trend Analysis    │   │  │
│   │  │ • Aero       │   │ • α margin   │   │  • Exceedance Det.   │   │  │
│   │  │ • Structural │   │ • Speed      │   │  • Recovery Advice   │   │  │
│   │  │ • Propulsion │   │ • Load Factor│   │                      │   │  │
│   │  │ • H₂-specific│   │ • Altitude   │   │                      │   │  │
│   │  └──────────────┘   └──────────────┘   └──────────────────────┘   │  │
│   │                                                   │                │  │
│   └───────────────────────────────────────────────────│────────────────┘  │
│                                                       │                    │
│                                                       ▼                    │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                   L2-LINKS (23-95-60-60)                            │  │
│   │                      OFEC PROTOCOL                                  │  │
│   │                                                                     │  │
│   │  ┌──────────────┐                                                  │  │
│   │  │   AIRCRAFT   │                                                  │  │
│   │  │  PUBLISHER   │                                                  │  │
│   │  │              │                                                  │  │
│   │  │ • Sampler    │                                                  │  │
│   │  │ • Encoder    │                                                  │  │
│   │  │ • Phase-aware│                                                  │  │
│   │  └──────┬───────┘                                                  │  │
│   │         │                                                          │  │
│   │         │ mTLS 1.3 / CBOR @ 1-10 Hz                                │  │
│   │         │ (preemptible during flight)                              │  │
│   │         ▼                                                          │  │
│   │  ┌──────────────┐        ┌──────────────┐                         │  │
│   │  │    GROUND    │───────▶│   REGIONAL   │                         │  │
│   │  │   RECEIVER   │        │  AGGREGATOR  │                         │  │
│   │  │              │        │              │                         │  │
│   │  │ • Decoder    │        │ • Multi-A/C  │                         │  │
│   │  │ • Validator  │        │ • Analytics  │                         │  │
│   │  │ • Storage    │        │ • Uplink     │                         │  │
│   │  │ • Alerting   │        │              │                         │  │
│   │  └──────────────┘        └──────┬───────┘                         │  │
│   │                                 │                                  │  │
│   │                                 ▼                                  │  │
│   │                          ┌──────────────┐                         │  │
│   │                          │  FLEET CORE  │                         │  │
│   │                          │              │                         │  │
│   │                          │ • Analytics  │                         │  │
│   │                          │ • DPP Log    │                         │  │
│   │                          │ • CAOS Feed  │                         │  │
│   │                          └──────────────┘                         │  │
│   │                                                                     │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Envelope Data Structure

### 6.1 Envelope State Message

```json
{
  "envelope_id": "uuid",
  "aircraft_id": "MSN-A360-001",
  "timestamp": "2025-11-27T14:30:00.123Z",
  "flight_phase": "CRUISE",
  
  "margins": {
    "alpha": {
      "current": 4.2,
      "limit": 12.5,
      "margin_deg": 8.3,
      "margin_pct": 66.4
    },
    "speed": {
      "current_ktas": 245,
      "vmin_ktas": 180,
      "vmax_ktas": 320,
      "margin_low_pct": 36.1,
      "margin_high_pct": 30.6
    },
    "load_factor": {
      "current_g": 1.02,
      "limit_positive_g": 2.5,
      "limit_negative_g": -1.0,
      "margin_positive_pct": 59.2,
      "margin_negative_pct": 102.0
    },
    "altitude": {
      "current_ft": 35000,
      "ceiling_ft": 43000,
      "margin_ft": 8000,
      "margin_pct": 18.6
    },
    "bank_angle": {
      "current_deg": 5.2,
      "limit_deg": 67,
      "margin_deg": 61.8,
      "margin_pct": 92.2
    }
  },
  
  "h2_specific": {
    "fuel_temp_margin_k": 12.5,
    "tank_pressure_margin_pct": 15.3,
    "boil_off_rate_margin_pct": 8.7
  },
  
  "advisory": {
    "level": "NORMAL",
    "active_advisories": [],
    "trend": "STABLE"
  },
  
  "metadata": {
    "sample_rate_hz": 1,
    "encoding": "CBOR",
    "schema_version": "1.0.0"
  }
}
```

---

## 7. Phase-Aware Publishing

| Flight Phase | Rate (Hz) | Priority | Preemptible |
|--------------|-----------|----------|-------------|
| GROUND | 0.1 | LOW | Yes |
| TAXI | 0.5 | LOW | Yes |
| TAKEOFF | 10 | HIGH | No |
| CLIMB | 5 | MEDIUM | Yes |
| CRUISE | 1 | LOW | Yes |
| DESCENT | 5 | MEDIUM | Yes |
| APPROACH | 10 | HIGH | No |
| LANDING | 10 | HIGH | No |

---

## 8. ATA Cross-References

| ATA | Role | OFEC Integration |
|-----|------|------------------|
| **22** | Auto Flight | Autopilot envelope protection limits |
| **27** | Flight Controls | Control surface limits, stall protection |
| **34** | Navigation | Flight dynamics, position data |
| **31** | Indicating/Recording | FDR integration |
| **45** | Central Maintenance | Exceedance logging |
| **23-95** | COMM_NN | Transport protocol |
| **23-96** | AST-L | Semantic vocabulary |

---

## 9. FAirCCC Channel Family Update

| Channel | Direction | Data Type | Safety | N-Axis | L2-Axis |
|---------|-----------|-----------|--------|--------|---------|
| CFLF-GRAD | A→G→R→F | DP-masked gradients | Non-safety | 97-40-20 | 23-95-60-10 |
| CFLF-MODEL | F→R→G→A | Trained models | Non-safety | 97-40-30 | 23-95-60-20 |
| CFLF-TELEM | A→G→R→F | Anonymized telemetry | Anonymized | 97-40-20 | 23-95-60-30 |
| CFLF-SAFETY | F→R→G→A | Safety models | [DO-178C](https://www.rtca.org/products/do-178c-software-considerations-in-airborne-systems-and-equipment-certification/)/ML | 97-40-30 | 23-95-60-40 |
| CUC | F→R→G→A | Signed bundles | Ground-only | 97-40-30 | 23-95-60-50 |
| **OFEC** | **A→G/R** | **Envelope margins** | **Advisory** | **97-40-40** | **23-95-60-60** |

---

## 10. AST-L Statements

OFEC data can be expressed in AST-L:

```astl
# Margin data
OFEC.A360-001 : alpha_margin : 8.3deg @CRUISE #L11_OPERATIONS

# Advisory state
OFEC.A360-001 : advisory_level : NORMAL @CRUISE #L11_OPERATIONS

# Trend analysis
OFEC.A360-001 : margin_trend : STABLE @10s #L11_OPERATIONS

# Exceedance event
OFEC.A360-001 : exceedance : LoadFactor(g=2.6, limit=2.5) @TURBULENCE #L07_VV
```

---

## 11. Integration Points

| System | Direction | Content |
|--------|-----------|---------|
| **CAOS** | OFEC→CAOS | Exceedance events, margin alerts |
| **DPP** | OFEC→DPP | Flight envelope history, performance records |
| **ANCHORS** | OFEC→ANCHORS | H₂-specific envelope data, efficiency metrics |
| **NN (95)** | OFEC→NN | Training data for predictive models |
| **FAirCCC-R** | OFEC→R | Regional aggregation, fleet analytics |
| **FAirCCC-F** | OFEC→F | Fleet-wide performance analysis |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | AMPEL360-OFEC-OPTIN-MAP-001 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Author** | AMPEL360 FAirCCC WG |
| **Status** | DRAFT |

---

## AI Disclosure

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---

*END OF DOCUMENT*
