# 23-97-70-010 — MMIP ⇄ CAOS Agent Memory Binding

**Document ID:** 23-97-70-010_MMIP_CAOS_Agent_Memory  
**Chapter:** ATA 23-97-70 OPERATIONS  
**Version:** 0.1  
**Status:** DRAFT  

---

## 1. Purpose

Define how **CAOS agents** (SHM, ICA, MRO, etc.) use MMIP for:

- Attaching their observations and decisions as **capsules**.
- Inheriting context from previous agents via `INHERIT_CONTEXT`.
- Exposing their memory as **Context Packages** for reuse and audit.

---

## 2. Agent Roles and Threads

Each CAOS agent operates over one or more **MMIP threads**:

- **SHM Agent** — monitoring thread(s) per aircraft/mission.
- **ICA Agent** — investigation / case threads.
- **MRO Agent** — maintenance action threads.

Recommended pattern:

- One **mission thread** per flight/mission: `thr_MISSION_<id>`.
- Sub-threads via `FORK_THREAD` for experiments, alternative hypotheses, etc.

---

## 3. Standard Agent Behaviour

### 3.1 SHM Agent

- On anomaly detection:
  - Create capsule `cap_SHM_x` with AST-L anomaly statements.
  - `ATTACH_MEMORY(thr_MISSION, cap_SHM_x)`.
- When escalating to ICA:
  - Call `INHERIT_CONTEXT(thread_id=thr_MISSION, filters={scopes:[session,task]})`.
  - Wrap result in envelope and send to ICA agent (via FAirCCC or local bus).

### 3.2 ICA Agent

- On case creation:
  - Derive or reuse mission thread (`FORK_THREAD` if investigation branch).
- Uses `INHERIT_CONTEXT` to:
  - Pull all relevant anomaly capsules.
  - Attach investigation steps (hypotheses, test results).
- May create a **Context Package**:
  - `pkg_ICA_CASE_<id>` to summarise the case for MRO / regulators.

### 3.3 MRO Agent

- On receiving ICA output:
  - Attach maintenance plan capsules to the same or derived thread.
  - Optionally lift relevant context into a **long-term package**:
    - e.g., "Known Issue: STRINGER F2 Overload".

---

## 4. Context Packages in CAOS

Example Context Packages:

| Package ID | Content | Scope |
|------------|---------|-------|
| `pkg_AIRCRAFT_ARCH` | High-level architecture, limitations | user_long_term |
| `pkg_MISSION_<id>` | Mission-specific capsules | session/task |
| `pkg_ICA_CASE_<case_id>` | Investigation summaries, key evidence | long_term |
| `pkg_KNOWN_ISSUE_<code>` | Known problem patterns and mitigations | long_term |

Agents:

- Attach packages to sessions via `APPLY_CONTEXT_PACKAGE(session_id, package_id)`.
- Inherit automatically on agent/model shifts (MMIP default behaviour).

---

## 5. Example Flow: SHM → ICA → MRO

```text
1. SHM detects anomaly
   - ATTACH_MEMORY(thr_MISSION, cap_SHM_01)

2. ICA starts investigation
   - INHERIT_CONTEXT(thr_MISSION, filters=...)
   - Receives envelope with cap_SHM_01..N
   - ATTACH_MEMORY(thr_MISSION, cap_ICA_01)  # root cause hypothesis

3. ICA finalises case
   - CREATE_CONTEXT_PACKAGE("ICA_CASE_123", capsule_refs=[...])
   - EXPORT_CONTEXT_PACKAGE for audit if allowed by policy

4. MRO schedules action
   - INHERIT_CONTEXT(thr_MISSION, package_ids=[pkg_ICA_CASE_123])
   - ATTACH_MEMORY(thr_MISSION, cap_MRO_01) # maintenance task
```

---

## 6. Policy Alignment

- **Visibility**:
  - Some capsules (e.g., internal deliberations) may be `agent_local`.
  - Packages exposed to regulators must follow 97-40-20 data protection rules.
- **Retention**:
  - Mission threads: at least `session` retention.
  - Known issue packages: `long_term`.
  - Agent scratchpads: `ephemeral` or `agent_local`.
- **Export**:
  - Export to external stakeholders governed by package-level `export` policies.

---

## 7. Compliance Levels in CAOS

- **Level 1**: CAOS agents use MMIP capsules and threads internally.
- **Level 2**: Agents expose user-manageable packages (ICA, MRO cases).
- **Level 3**: Full multi-agent interoperability with auditable inheritance and
  cross-surface reuse (IETP, training, post-event analysis).

---

## 8. References

- [MMIP v0.1 Specification](../../../../../../mmip-standard/spec/mmip-v0.1.md)
- [23-97-00-001 MMIP Overview](../23-97-00_GENERAL/23-97-00-001_MMIP_Overview.md)
- [23-97-60-010 MMIP ⇄ FAirCCC Integration](../23-97-60_INHERITANCE/23-97-60-010_MMIP_FAIRCCC_Integration.md)
- [CAOS Architecture](../../../../../../CAOS/)

---

## 9. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
