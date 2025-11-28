# MMIP v0.1 — Models Memory Inheritance Protocol

**A Standard for Portable, Policy-Aware Memory Across Generative AI Systems**

| Field | Value |
|-------|-------|
| Status | Draft Standard |
| Version | 0.1 |
| Date | 2025-11-28 |
| Editors | _(Placeholder)_ |
| Contributors | _(Placeholder)_ |

---

## Table of Contents

- [0. Abstract](#0-abstract)
- [1. Scope](#1-scope)
- [2. Terminology](#2-terminology)
- [3. Architecture Overview](#3-architecture-overview)
- [4. Data Model](#4-data-model)
  - [4.1 Memory Capsule](#41-memory-capsule)
  - [4.2 Memory Thread](#42-memory-thread)
  - [4.3 Context Package](#43-context-package)
  - [4.4 Memory Envelope](#44-memory-envelope)
- [5. Policy Model](#5-policy-model)
- [6. Inheritance Model](#6-inheritance-model)
- [7. Standard Operations (API Verbs)](#7-standard-operations-api-verbs)
- [8. Transport Independence](#8-transport-independence)
- [9. Security & Compliance](#9-security--compliance)
- [10. Reference Behaviors](#10-reference-behaviors)
- [11. Example Envelope (Normative)](#11-example-envelope-normative)
- [12. Extensibility](#12-extensibility)
- [13. Compliance Levels](#13-compliance-levels)
- [14. Reference Implementation (Non-Normative)](#14-reference-implementation-non-normative)
- [15. Future Work](#15-future-work)
- [16. Conclusion](#16-conclusion)

---

## 0. Abstract

The **Models Memory Inheritance Protocol (MMIP)** defines a vendor-agnostic, transport-agnostic standard for representing, storing, sharing, inheriting, redacting, and exporting **memory capsules** between generative AI models, tools, and agentic workflows.

MMIP enables **automatic** continuity of context across:

- Model switches (e.g., reasoning → code → image)
- Tool calls
- Agent pipelines
- Playground or IDE sessions

...without requiring users to manually re-enter context.

**Key principle**: Model or session shifts trigger automatic inheritance of relevant memory (thread + context packages) by default, rather than starting from scratch. This ensures seamless context continuity while respecting user-defined policies.

MMIP also provides user-level control: browsing, managing, grouping, redacting, exporting, and injecting context as **Context Packages**.

---

## 1. Scope

MMIP standardizes:

- A data model for memory capsules and packages
- A protocol for inheritance, redaction, and summarization
- A set of operations for both system and user agents
- A compliance model for privacy, auditability, and lineage
- Interoperability between:
  - LLMs, VLMs, code models, tool agents
  - Playgrounds, IDEs, Copilot-like systems
  - Model context servers (e.g., MCP-based)
  - Multi-agent, multi-model AI stacks

MMIP does **not** prescribe:

- Model behavior
- Tokenization or formatting rules
- Specific storage/transport (HTTP, gRPC, WebSockets, MCP)
- UI/UX

---

## 2. Terminology

| Term | Definition |
|------|------------|
| **Memory Capsule** | Atomic unit of memory containing content, metadata, scopes, and policies. |
| **Memory Thread** | A chain or DAG of capsules representing a persistent contextual sequence. |
| **Context Package** | A named, user-definable bundle of capsules and summaries, portable across sessions and models. |
| **Memory Envelope** | The subset of memory (capsules + summaries + policies) delivered to a model/tool for a single call. |
| **Inheritance Context** | Rules guiding how a model receives, summarizes, filters, or redacts memory. |
| **Policy Set** | Rules controlling retention, privacy, exportability, visibility, and redaction. |

---

## 3. Architecture Overview

MMIP is composed of five layers:

1. **Data Layer** — Defines capsules, packages, threads.
2. **Policy Layer** — Governs access, retention, redaction, visibility.
3. **Inheritance Layer** — Governs context composition and transfer.
4. **Operations Layer** — Defines standard API verbs.
5. **Audit Layer** — Defines provenance, lineage, and compliance requirements.

See [Annex D: Architecture Diagrams](../assets/diagrams/README.md) for visual representations.

---

## 4. Data Model

### 4.1 Memory Capsule

A **Memory Capsule** MUST contain:

| Field | Type | Description |
|-------|------|-------------|
| `capsule_id` | string | Unique identifier |
| `type` | enum | `user_message`, `model_message`, `summary`, `annotation`, `upload`, `file_ref`, `metadata` |
| `scope` | enum | `user_long_term`, `session`, `task`, `agent_local` |
| `content` | object | Raw or structured content |
| `metadata` | object | Tags, domain, embeddings, size, tokens |
| `provenance` | object | Who created it, when, from what |
| `policies` | object | Export, visibility, retention |
| `links` | list | DAG relationships (`summarizes`, `derived_from`) |

Fields MAY be extended by vendor implementations via `extensions`.

**Schema**: See [`schemas/capsule.json`](../schemas/capsule.json)

---

### 4.2 Memory Thread

A **Memory Thread** MUST contain:

- `thread_id`
- Ordered or DAG-linked capsules
- Thread-level metadata (title, domain, participants)
- Retention policy
- Lineage graph

Threads MAY fork/merge.

---

### 4.3 Context Package

A **Context Package** MUST contain:

| Field | Description |
|-------|-------------|
| `package_id` | Unique ID |
| `owner` | User, org, or agent owner |
| `name`, `description` | Human-readable |
| `capsule_refs` | List of `capsule_id`s or filters |
| `policies` | Visibility, export rules, retention |
| `summary_capsule` | Optional auto-generated compression |
| `tags` | Domain grouping |
| `provenance` | Creation and modification log |

---

### 4.4 Memory Envelope

A **Memory Envelope** MUST contain:

- `mmip_version`
- `thread_id` (if applicable)
- `context_id`
- `producer` (agent/model/tool)
- `policies`
- A set of capsules (possibly summarized)
- Optional external references (vector store, file store)

Memory Envelopes MUST be **immutable**.

**Schema**: See [`schemas/envelope.json`](../schemas/envelope.json)

---

## 5. Policy Model

MMIP defines five mandatory policy classes:

### 1. Visibility

- Which models/tools/agents may access a capsule/package
- Examples: `owner_only`, `all_models`, `no_external_providers`

### 2. Export

- Governs downloadability or external transfer
- Examples: `allow_export`, `forbid_export`, `redact_on_export`

### 3. Retention

- Lifespan of capsules
- Examples: `ephemeral`, `session`, `long_term`, `never_persist`

### 4. Redaction

- Rules for PII, secrets, compliance

### 5. Transformation

- Summarization rules, compression limits, abstraction levels

---

## 6. Inheritance Model

When a model/tool is invoked, it receives context via `INHERIT_CONTEXT`.

### 6.1 Inputs

- `thread_id` (optional)
- `package_ids` (optional)
- `filters` (capsule types, scopes, recency, tags)
- `policies` (visibility/retention)
- `max_tokens` or size constraint
- `summarization_profile`

### 6.2 Output

A **Memory Envelope** containing:

1. Selected capsules
2. Summaries or compressions required to meet size limits
3. Redactions required by policies
4. A provenance log for auditability

### 6.3 Inheritance Rules

- Capsules MUST NOT violate visibility/export rules
- Ordered context MUST preserve thread order unless summarized
- Compressors/summarizers MUST mark capsules as derived
- Redactions MUST create tombstone or redaction capsules

---

## 7. Standard Operations (API Verbs)

The MMIP protocol defines the following required operations.

### 7.1 Thread Operations

| Operation | Description |
|-----------|-------------|
| `INIT_THREAD(metadata)` | Create a new thread |
| `ATTACH_MEMORY(thread_id, capsule)` | Add a capsule to a thread |
| `INHERIT_CONTEXT(thread_id, filters, policies)` | Retrieve context envelope |
| `FORK_THREAD(thread_id)` | Create a branch from existing thread |
| `MERGE_THREADS(thread_id_A, thread_id_B)` | Combine two threads |
| `SNAPSHOT_THREAD(thread_id → package_id)` | Create a package from thread |

### 7.2 Capsule Operations

| Operation | Description |
|-----------|-------------|
| `LIST_CAPSULES(thread_id, filters)` | List capsules matching criteria |
| `GET_CAPSULE(capsule_id)` | Retrieve a specific capsule |
| `TAG_CAPSULES(capsule_ids, tags)` | Add tags to capsules |
| `REDACT_CAPSULE(capsule_id, rule_set)` | Apply redaction rules |
| `DELETE_CAPSULE(capsule_id)` | Soft deletion |

### 7.3 Context Package Operations

| Operation | Description |
|-----------|-------------|
| `CREATE_CONTEXT_PACKAGE(name, capsule_refs, policies)` | Create a new package |
| `UPDATE_CONTEXT_PACKAGE(package_id, metadata, changes)` | Modify package metadata |
| `LIST_CONTEXT_PACKAGES(owner)` | List packages for an owner |
| `GET_CONTEXT_PACKAGE(package_id)` | Retrieve a package |
| `EXPORT_CONTEXT_PACKAGE(package_id, format)` | Export package in specified format |
| `APPLY_CONTEXT_PACKAGE(session_id, package_id, mode)` | Apply package to session |

**Modes**: `read_only`, `extendable`, `fork_into_new_thread`

### 7.4 Envelope Operations

| Operation | Description |
|-----------|-------------|
| `GENERATE_ENVELOPE(thread/package + filters)` | Create an envelope |
| `VALIDATE_ENVELOPE(envelope)` | Validate envelope schema |
| `STORE_ENVELOPE(envelope)` | Persist envelope (optional) |
| `AUDIT_ENVELOPE(envelope)` | Generate audit trail |

### 7.5 Search & Query Operations

| Operation | Description |
|-----------|-------------|
| `SEARCH_MEMORY(query, filters)` | Search capsules |
| `SEARCH_PACKAGES(query, tags)` | Search packages |

MUST include embeddings/vector references if supported.

---

## 8. Transport Independence

MMIP MUST operate over any transport. This specification defines generic payloads and behaviors.

**Recommended bindings**:

- JSON over HTTP
- gRPC
- WebSocket streams
- MCP (Model Context Protocol)
- Local agent bus

Future annexes MAY define formal transport schemas.

---

## 9. Security & Compliance

MMIP MUST support:

### 9.1 Privacy Guarantees

- Capsule-level visibility scopes
- Redaction before export
- Separation of user-long-term vs session-memory

### 9.2 Auditability

- Every capsule and envelope MUST contain provenance
- Every transformation MUST reference source capsules
- Tool access MUST be logged

### 9.3 Integrity

- Optionally cryptographic hash of capsule content
- Optionally signed envelopes

---

## 10. Reference Behaviors

### Default Automatic Inheritance

MMIP implementations MUST automatically inherit relevant memory on model or session shifts by default. This ensures context continuity without requiring manual re-entry of information.

**Default behavior on model/session shift**:

1. The system MUST automatically invoke `INHERIT_CONTEXT` with the current thread and applicable context packages
2. The incoming model/session MUST receive the composed Memory Envelope
3. Context MUST NOT be reset unless explicitly requested by the user or policy

This default can be overridden by:
- Explicit user action (e.g., "start fresh")
- Policy rules that restrict inheritance
- System configuration for specific use cases

### Switching Models

- MUST NOT reset context (automatic inheritance is the default)
- MUST automatically invoke `INHERIT_CONTEXT` on model switch
- MUST enforce policies of included capsules
- MAY allow user override to start without inherited context

### Session Shifts

- MUST preserve thread continuity across session boundaries by default
- MUST automatically load applicable context packages on session resume
- MUST respect retention policies when determining what to inherit

### Agent Pipelines

- Each agent MUST declare which packages it requires
- Pipelines MUST maintain thread continuity by default
- Tools MUST receive minimal-privilege summaries

### User Exports

- MUST enforce export policies
- MUST redact where required
- MUST embed full provenance

---

## 11. Example Envelope (Normative)

```json
{
  "mmip_version": "0.1",
  "context_id": "ctx_9876",
  "thread_id": "thr_12345",
  "producer": {
    "type": "model",
    "id": "gpt-5.1",
    "role": "assistant"
  },
  "policies": {
    "visibility": ["all_models"],
    "retention": "session",
    "sharing": {
      "allow_external_providers": false,
      "require_redaction": ["PII"]
    }
  },
  "capsules": [
    {
      "capsule_id": "cap_001",
      "type": "user_message",
      "scope": "session",
      "content": {
        "text": "Formalize the MMIP standard"
      },
      "provenance": {
        "source": "user",
        "timestamp": "2025-11-28T12:34:56Z"
      }
    }
  ],
  "links": [],
  "integrity": {
    "hash": "sha256:abc123..."
  }
}
```

---

## 12. Extensibility

MMIP supports extensions at:

- Capsule metadata level
- Envelope metadata level
- Additional policy types
- Custom capsule types
- Vector references / file references
- Plug-in summarization engines

Extensions MUST NOT break schema compatibility.

---

## 13. Compliance Levels

MMIP defines three compliance tiers:

### Level 1 — Basic

Supports capsules, threads, and envelopes.

### Level 2 — User-Controlled Memory

Adds packages, export, redaction, and user-facing operations.

### Level 3 — Full Agentic Interoperability

Implements inheritance, summarization, lineage, integrity, and cross-model portability.

---

## 14. Reference Implementation (Non-Normative)

A reference implementation is provided in [`reference_impl/mmip_protocol.py`](../reference_impl/mmip_protocol.py).

Future annexes will include:

- MCP binding
- Local file-backed store
- Cloud-backed store

---

## 15. Future Work

- Binary capsule formats
- Cryptographically signed capsules
- MMIP for distributed multi-agent swarms
- Differential privacy for summarization
- Capsule diff/patch operations

---

## 16. Conclusion

MMIP creates:

- A universal memory layer
- A portable context mechanism
- A user-controllable memory interface
- A standard for model independence
- A foundation for agent ecosystems

It resolves the long-standing fragmentation of memory in GenAI systems and establishes a shared backbone for interoperable, auditable, policy-aware contextual reasoning.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
