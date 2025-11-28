# MMIP Architecture Diagrams (Annex D)

This directory contains architecture diagrams for the MMIP v0.1 specification.

---

## Diagram 1: The MMIP Layered Architecture

The MMIP architecture is composed of five abstraction layers as defined in Section 3 of the specification.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Layer 5: APPLICATION LAYER                        │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐   │
│  │  IDEs   │  │ Agents  │  │  LLMs   │  │  VLMs   │  │ Tools   │   │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘   │
└───────┼────────────┼────────────┼────────────┼────────────┼────────┘
        │            │            │            │            │
        └────────────┴─────┬──────┴────────────┴────────────┘
                           │
┌──────────────────────────┼──────────────────────────────────────────┐
│                    Layer 4: OPERATIONS LAYER                         │
│                                                                      │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐         │
│  │ INIT_THREAD    │  │ INHERIT_CONTEXT│  │ SNAPSHOT       │         │
│  │ ATTACH_MEMORY  │  │ FORK_THREAD    │  │ EXPORT_PACKAGE │         │
│  │ LIST_CAPSULES  │  │ MERGE_THREADS  │  │ SEARCH_MEMORY  │         │
│  └────────────────┘  └────────────────┘  └────────────────┘         │
│                                                                      │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
┌──────────────────────────┼──────────────────────────────────────────┐
│                    Layer 3: INHERITANCE LAYER                        │
│                                                                      │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    Context Compositor                          │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐   │  │
│  │  │   Filter    │  │ Summarizer  │  │ Policy Enforcer     │   │  │
│  │  │   Engine    │  │   Engine    │  │ (Redaction/Scope)   │   │  │
│  │  └─────────────┘  └─────────────┘  └─────────────────────┘   │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                      │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
┌──────────────────────────┼──────────────────────────────────────────┐
│                    Layer 2: POLICY LAYER                             │
│                                                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐  │
│  │ Visibility  │  │   Export    │  │ Retention   │  │ Redaction  │  │
│  │   Rules     │  │   Rules     │  │   Rules     │  │   Rules    │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  └────────────┘  │
│                                                                      │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
┌──────────────────────────┼──────────────────────────────────────────┐
│                    Layer 1: DATA LAYER                               │
│                                                                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐      │
│  │    Capsules     │  │     Threads     │  │    Packages     │      │
│  │  ┌───┐ ┌───┐    │  │  cap1→cap2→cap3 │  │  ┌───────────┐  │      │
│  │  │cap│ │cap│    │  │        ↘        │  │  │ capsules  │  │      │
│  │  └───┘ └───┘    │  │       cap4      │  │  │ +policies │  │      │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘      │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                    Blob/Vector Storage                       │    │
│  │    (Embeddings, Files, External References)                  │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Diagram 2: The Inheritance Flow

This diagram illustrates the `INHERIT_CONTEXT` operation as defined in Section 6.

```
                          INHERIT_CONTEXT Flow
┌─────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  ┌─────────┐                                                         │
│  │  Agent  │─────────────────┐                                       │
│  │  /LLM   │                 │                                       │
│  └─────────┘                 ▼                                       │
│                    ┌──────────────────┐                              │
│                    │  1. REQUEST      │                              │
│                    │  ───────────     │                              │
│                    │  thread_id       │                              │
│                    │  filters         │                              │
│                    │  max_tokens      │                              │
│                    │  policies        │                              │
│                    └────────┬─────────┘                              │
│                             │                                        │
│                             ▼                                        │
│               ┌─────────────────────────────┐                        │
│               │      2. RETRIEVAL           │                        │
│               │      ────────────           │                        │
│               │  MMIP Engine pulls Thread   │                        │
│               │  from Data Layer            │                        │
│               │                             │                        │
│               │  ┌───────────────────────┐  │                        │
│               │  │ Thread: thr_12345     │  │                        │
│               │  │ ┌────┐ ┌────┐ ┌────┐  │  │                        │
│               │  │ │cap1│→│cap2│→│cap3│  │  │                        │
│               │  │ └────┘ └────┘ └────┘  │  │                        │
│               │  └───────────────────────┘  │                        │
│               └─────────────┬───────────────┘                        │
│                             │                                        │
│                             ▼                                        │
│               ┌─────────────────────────────┐                        │
│               │      3. POLICY CHECK        │                        │
│               │      ──────────────         │                        │
│               │  ✓ Check visibility scopes  │                        │
│               │  ✓ Check export permissions │                        │
│               │  ✓ Enforce retention rules  │                        │
│               │                             │                        │
│               │  User A ✓ → cap1, cap2      │                        │
│               │  User B ✗ → (no access)     │                        │
│               └─────────────┬───────────────┘                        │
│                             │                                        │
│                             ▼                                        │
│               ┌─────────────────────────────┐                        │
│               │     4. TRANSFORMATION       │                        │
│               │     ───────────────         │                        │
│               │  • Apply redaction rules    │                        │
│               │  • Summarize if over limit  │                        │
│               │  • Mark derived capsules    │                        │
│               │                             │                        │
│               │  tokens: 5000 → 2000        │                        │
│               │  (summarized older caps)    │                        │
│               └─────────────┬───────────────┘                        │
│                             │                                        │
│                             ▼                                        │
│               ┌─────────────────────────────┐                        │
│               │      5. OUTPUT              │                        │
│               │      ──────                 │                        │
│               │  Signed Memory Envelope     │                        │
│               │  ┌───────────────────────┐  │                        │
│               │  │ mmip_version: "0.1"   │  │                        │
│               │  │ context_id: "ctx_9876"│  │                        │
│               │  │ capsules: [...]       │  │                        │
│               │  │ integrity: {hash: ...}│  │                        │
│               │  └───────────────────────┘  │                        │
│               └─────────────┬───────────────┘                        │
│                             │                                        │
│                             ▼                                        │
│                    ┌─────────┐                                       │
│                    │  Agent  │                                       │
│                    │  /LLM   │                                       │
│                    └─────────┘                                       │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Diagram 3: Multi-Model Context Flow

This diagram shows how MMIP enables context continuity across model switches.

```
┌─────────────────────────────────────────────────────────────────────┐
│                   Multi-Model Context Flow                           │
│                                                                      │
│   User Request                                                       │
│       │                                                              │
│       ▼                                                              │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐          │
│  │  Reasoning  │      │    Code     │      │   Image     │          │
│  │    Model    │─────▶│    Model    │─────▶│    Model    │          │
│  │  (GPT-5.1)  │      │  (Codex)    │      │  (DALL-E)   │          │
│  └──────┬──────┘      └──────┬──────┘      └──────┬──────┘          │
│         │                    │                    │                  │
│         │ INHERIT_CONTEXT    │ INHERIT_CONTEXT    │ INHERIT_CONTEXT │
│         │                    │                    │                  │
│         ▼                    ▼                    ▼                  │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                    MMIP Memory Layer                         │    │
│  │                                                              │    │
│  │  ┌────────────────────────────────────────────────────────┐ │    │
│  │  │ Thread: thr_project_001                                │ │    │
│  │  │                                                        │ │    │
│  │  │  ┌─────────┐    ┌─────────┐    ┌─────────┐             │ │    │
│  │  │  │ cap_001 │───▶│ cap_002 │───▶│ cap_003 │             │ │    │
│  │  │  │ user    │    │ reason  │    │ code    │             │ │    │
│  │  │  │ request │    │ output  │    │ output  │             │ │    │
│  │  │  └─────────┘    └─────────┘    └─────────┘             │ │    │
│  │  │                                                        │ │    │
│  │  └────────────────────────────────────────────────────────┘ │    │
│  │                                                              │    │
│  │  Policies: visibility=all_models, retention=session          │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  Result: Each model receives full context from previous steps        │
│          without user re-entering information                        │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Future SVG Diagrams

The following diagrams are planned for future releases:

1. **mmip-architecture-v0.1.svg** - Full architecture diagram in SVG format
2. **mmip-inheritance-flow-v0.1.svg** - Detailed inheritance flow diagram
3. **mmip-policy-matrix-v0.1.svg** - Visual policy decision matrix
4. **mmip-data-model-v0.1.svg** - Entity-relationship diagram of the data model

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
