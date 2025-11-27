# 97-40-20-20_PRIVACY_BUDGET — Privacy Budget Governance

**Global privacy accounting and governance for CFLF-GRAD Federated Learning**

---

## Document Control

| Field              | Value                                                           |
|--------------------|-----------------------------------------------------------------|
| **Document ID**    | 97-40-20-20-001_Privacy_Budget_Governance                      |
| **ATA Chapter**    | 97 — Neural Network Models / Digital Artifacts                  |
| **Bucket**         | 97-40-20 — FEDERATED_LEARNING                                   |
| **Sub-Bucket**     | 97-40-20-20 — PRIVACY_BUDGET                                   |
| **Version**        | 1.0                                                             |
| **Date**           | 2025-11-27                                                      |
| **Status**         | DRAFT                                                           |
| **Classification** | PRIVACY / GOVERNANCE / ACCOUNTING                               |
| **Owner**          | N — Neural Networks Users Traceability WG (ATA 95/97)           |
| **Programme**      | AMPEL360-BWB-H₂-Hy-E Q100                                       |

---

## 1. Purpose

This document defines the **privacy budget model, governance rules and accounting mechanisms**  
used by AMPEL360 for **federated learning** within the **CFLF-GRAD fabric**.

It establishes:

- How **privacy budgets (ε, δ)** are defined, allocated and consumed.
- How DP mechanisms (e.g. **DP-SGD**) report their effective privacy cost.
- How privacy budgets are **traced across aircraft, nodes and federated runs**.
- How privacy status is exposed to **CAOS, DPP and regulators**.

---

## 2. Scope

The scope of this document and bucket includes:

1. **Conceptual Definition of Privacy Budget**
   - Global ε, δ semantics for AMPEL360 federated learning.
   - Per-model, per-aircraft, per-fleet and per-time-window budgets.

2. **Accounting Mechanisms**
   - Supported privacy accountants (e.g. RDP, Moments, Gaussian).
   - How training runs report their cumulative ε, δ.

3. **Governance & Policies**
   - Allowed ranges for ε, δ per use case / data category.
   - Quotas per aircraft, fleet, region and time frame.
   - Kill switches and enforcement behaviors.

4. **Integration with CFLF-GRAD**
   - How **97-40-20-10_DP_SGD** reports consumption.
   - How nodes A/G/R/F synchronize privacy state.

5. **Integration with CAOS, DPP and AST-L**
   - How privacy budget state is:
     - Logged into **DPP**.
     - Exposed to **CAOS** for operational awareness.
     - Described in **AST-L (AirSynTech Language)** metadata.

Implementation details (code, accountants, libraries) are referenced in sub-documents and schemas within this bucket.

---

## 3. Position in OPT-IN & ATA

### 3.1 OPT-IN Axes

The **PRIVACY_BUDGET** bucket belongs to the **N — NEURAL_NETWORKS_USERS_TRACEABILITY** axis:

- Governs **what level of privacy** is guaranteed for data used in learning.
- Acts as the **policy and accounting layer** for mechanisms like **DP-SGD (97-40-20-10)**.
- Feeds **traceability and compliance views** into:
  - **CAOS** (Continuous Airworthiness operations intelligence).
  - **DPP** (Digital Product Passport).

It interacts with:

- **T / L2-LINKS (ATA 23)** — for propagating privacy metadata along CFLF channels.
- **I / CAOS & AirCCC** — for orchestration, reporting and alarms when budgets are exhausted.

### 3.2 Relevant ATA Chapters

- **ATA 97** – Home of model artifacts, DPP linkage, and federated learning metadata.
- **ATA 95** – AI/NN safety & governance, where privacy forms part of the assurance case.
- **ATA 23** – Communications channels (CFLF-GRAD, CFLF-MODEL, CFLF-TELEM).
- **ATA 02 / 42** – Operational and computing context (where training occurs).

---

## 4. Concept of Privacy Budget in AMPEL360

### 4.1 Definition

In AMPEL360, a **privacy budget** is the **maximum allowed cumulative privacy loss** (ε, δ)  
associated with the usage of **real-world, sensitive or personal data** in federated learning.

It is defined at several levels:

- **Per Model** — budget per model family (e.g. H₂ Management, PredMaint, ANCHORS).
- **Per Asset** — budget per physical aircraft or component group.
- **Per Time Window** — budget per rolling period (e.g. per year, per Type Certificate phase).
- **Per Region / Regulatory Domain** — budgets aligned with local privacy regulations.

### 4.2 Units

- **ε (epsilon)** — privacy loss parameter; smaller is more private.
- **δ (delta)** — failure probability bound; usually set very small (e.g. 1e-6 or lower).

The combination (ε, δ) is recorded and tracked **per federated run** and **per cumulative view**.

---

## 5. Accounting Model

### 5.1 Inputs to the Accountant

Each DP-protected learning mechanism (e.g. **DP-SGD**) must report at least:

- Mechanism type (e.g. DP-SGD).
- `noise_multiplier` and `clip_norm`.
- Sampling rate or batch size vs dataset size.
- Number of training steps (`num_steps`) or rounds.
- Composition strategy (e.g. Poisson subsampling).

These parameters are used to compute or approximate the effective (ε, δ).

### 5.2 Accounting Approaches

This bucket supports one or more standardized accountants, such as:

- **RDP (Rényi Differential Privacy)** accountants.
- **Moments / Gaussian** accountants.

The selected accountant and parameters must be:

- Defined in configuration profiles under this bucket.
- Attached as metadata to each run (see SCHEMAS section).

### 5.3 Accumulation

For each **scope** (model, aircraft, fleet…):

- **Initial Budget**: (ε_max, δ_max) defined by policy.
- **Cumulative Usage**: sum / composition of ε, δ contributions from all runs.
- **Remaining Budget**: ε_rem = ε_max − ε_used (with domain-specific composition rules).

When remaining budget falls below defined thresholds, **CAOS** and **MRO/ICA** may:

- Trigger **alerts**.
- Restrict further training.
- Require **governance review** before continuing.

---

## 6. Governance and Policies

### 6.1 Policy Profiles

Privacy budgets are defined via **profiles** (e.g. YAML) such as:

- `HIGH_PRIVACY` — low ε_max, strict bounds, sensitive data.
- `BALANCED_PRIVACY` — moderate ε_max, non-critical performance.
- `SIMULATED_DATA` — relaxed or no strict budget (synthetic or non-sensitive).

Each profile defines:

- Allowed ranges for ε, δ.
- Allowed mechanisms (e.g. required DP-SGD).
- Approved accountant type.
- Reporting obligations.

### 6.2 Enforcement

If a run would exceed budget:

- The **orchestrator must abort or downgrade** the learning operation.
- A **policy violation event** is generated and logged to:
  - **CAOS Event Bus**.
  - **DPP** (as part of lifecycle history).
- A human review is required to reconfigure budgets or training plans.

---

## 7. Integration with CFLF-GRAD and AST-L

### 7.1 CFLF-GRAD Channels

Every gradient or model update transmitted through CFLF channels must carry **AST-L descriptors** containing:

- `privacy_profile_id`
- Accountant type and version.
- Estimated cumulative (ε, δ) at the time of transmission.
- Scope identifiers (model_id, aircraft_id, fleet_id, region_id).

For example, the **`gradient_envelope`** schema (in 23-95-90_SCHEMAS) includes a nested  
`privacy_budget` object referencing this bucket’s schemas.

### 7.2 Node Roles (A/G/R/F)

Across the node architecture:

- **A (Aircraft)**:
  - Reports local consumption.
  - Cannot override global privacy policy; uses pre-approved profiles.

- **G (Ground)** and **R (Regional)**:
  - Aggregate per-A runs and update regional/fleet budgets.

- **F (Fleet Core)**:
  - Maintains authoritative global budget state.
  - Exposes budget dashboards and APIs to CAOS / DPP / regulators.

---

## 8. CAOS and DPP Integration

### 8.1 CAOS Awareness

CAOS must be able to:

- Query or receive events about **privacy budget states**.
- Include privacy budget status in **fleet intelligence** and **risk views**.
- Ensure that training actions never compromise:
  - Safety envelopes.
  - Regulatory privacy limits.

### 8.2 DPP Traceability (ATA 97)

For each model variant and federated learning campaign, DPP records:

- Privacy profile applied.
- Accountant type and parameters.
- Final cumulative (ε, δ).
- Budget remaining at closure of the campaign.
- Any exceptions or policy overrides (with approvals).

This enables **auditable, regulator-facing evidence** of privacy-aware learning.

---

## 9. Directory Structure (97-40-20-20_PRIVACY_BUDGET)

Recommended internal structure:

```text
97-40-20-20_PRIVACY_BUDGET/
├── README.md                          # This file
├── SPEC/
│   └── Privacy_Budget_Model.md        # Formal definition of budgets and scopes
├── POLICIES/
│   ├── privacy_profiles.yaml          # HIGH/BALANCED/OTHER profiles
│   └── regional_overlays.yaml         # Region/regulator-specific rules
├── ACCOUNTANTS/
│   ├── rdp_accountant_notes.md        # RDP configuration notes
│   └── accountant_selection.md        # Criteria and rationale
├── REPORTS/
│   └── budget_usage_examples.md       # Example scenarios and budget traces
└── SCHEMAS/
    └── privacy_budget_run.schema.json # Schema for logging privacy usage per run
````

As the program evolves, additional artifacts (dashboards, scripts, configs) may be added under these folders.

---

## 10. Related Documents

* `97-40-20-00_GENERAL/README.md` — Federated Learning General (CFLF-GRAD overview).
* `97-40-20-10_DP_SGD/README.md` — DP-SGD algorithm and parameters.
* `97-40-20-80_MODELS/` — Models that consume privacy budgets.
* `T-.../ATA_23-COMMUNICATIONS/23-95_COMM_NN/` — Federated learning communication channels.
* `CAOS/CAOS_CROSS_ATA_MAP.md` — CAOS awareness and autonomy spine context.
* `DPP/` (ATA 97) — Lifecycle and regulator-facing traceability.

---

## Authorship & Review

* **Authorship:** Content generated through prompt engineering methods using AI assistants and agent tools, prompted and partially reviewed by **Amedeo Pelliccia**, with automated checking tools for validation.
* **Status:** **DRAFT** – Subject to human review and approval.
* **Human approver:** *[to be completed]*.
* **Repository:** `AMPEL360-BWB-H2-Hy-E`
* **Last AI update:** *2025-11-27*.



