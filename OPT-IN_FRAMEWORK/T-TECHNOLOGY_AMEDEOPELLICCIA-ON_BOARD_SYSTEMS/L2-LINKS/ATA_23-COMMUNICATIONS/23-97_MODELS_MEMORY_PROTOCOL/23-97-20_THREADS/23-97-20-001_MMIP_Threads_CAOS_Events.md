# 23-97-20-001 — MMIP Threads ⇄ CAOS Events

**Document ID:** 23-97-20-001_MMIP_Threads_CAOS_Events  
**Chapter:** ATA 23-97-20 THREADS  
**Version:** 0.1  
**Status:** DRAFT  

---

## 1. Purpose

Define how **MMIP Memory Threads** map to **CAOS event chains** and mission/operation storylines.

---

## 2. Thread-to-Event Mapping

| MMIP Concept | CAOS Equivalent |
|--------------|-----------------|
| Thread | Event chain / mission storyline |
| Thread ID | Mission ID or operation ID |
| Capsule ordering | Event sequence |
| Thread fork | Alternative hypothesis branch |
| Thread merge | Investigation conclusion |

---

## 3. Recommended Thread Patterns

### 3.1 Mission Thread

```
thr_MISSION_<aircraft_id>_<date>_<seq>
```

Contains all capsules related to a single mission/flight.

### 3.2 Investigation Thread

```
thr_ICA_CASE_<case_id>
```

Forked from mission thread when investigation begins.

### 3.3 Maintenance Thread

```
thr_MRO_ACTION_<action_id>
```

Continues from investigation with maintenance actions.

---

## 4. Thread Lifecycle

1. **INIT_THREAD** — Create on mission start
2. **ATTACH_MEMORY** — Add capsules as events occur
3. **FORK_THREAD** — Branch for investigations
4. **MERGE_THREADS** — Consolidate findings
5. **SNAPSHOT_THREAD** — Archive as Context Package

---

## 5. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
