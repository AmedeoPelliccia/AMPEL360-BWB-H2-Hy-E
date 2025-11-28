# MMIP Architecture Diagrams (Annex D)
## Mermaid Edition

| Field               | Value                                                      |
|---------------------|------------------------------------------------------------|
| **Document ID**     | MMIP-ANNEX-D-DIAGRAMS-001                                  |
| **Version**         | 1.1                                                        |
| **Date**            | 2025-11-28                                                 |
| **Status**          | DRAFT                                                      |
| **Format**          | Mermaid                                                    |

---

## Diagram 1: MMIP Layered Architecture

The MMIP architecture is composed of five abstraction layers as defined in Section 3 of the specification.

```mermaid
flowchart TB
    subgraph L5["Layer 5: APPLICATION LAYER"]
        IDE[IDEs]
        AGT[Agents]
        LLM[LLMs]
        VLM[VLMs]
        TOOL[Tools]
    end

    subgraph L4["Layer 4: OPERATIONS LAYER"]
        direction LR
        subgraph OPS1[" "]
            INIT[INIT_THREAD]
            ATTACH[ATTACH_MEMORY]
            LIST[LIST_CAPSULES]
        end
        subgraph OPS2[" "]
            INHERIT[INHERIT_CONTEXT]
            FORK[FORK_THREAD]
            MERGE[MERGE_THREADS]
        end
        subgraph OPS3[" "]
            SNAP[SNAPSHOT]
            EXPORT[EXPORT_PACKAGE]
            SEARCH[SEARCH_MEMORY]
        end
    end

    subgraph L3["Layer 3: INHERITANCE LAYER"]
        subgraph CC["Context Compositor"]
            FILTER[Filter Engine]
            SUMM[Summarizer Engine]
            POLICY_E[Policy Enforcer<br/>Redaction/Scope]
        end
    end

    subgraph L2["Layer 2: POLICY LAYER"]
        VIS[Visibility Rules]
        EXP[Export Rules]
        RET[Retention Rules]
        RED[Redaction Rules]
    end

    subgraph L1["Layer 1: DATA LAYER"]
        subgraph DATA["Data Structures"]
            CAP[Capsules]
            THR[Threads]
            PKG[Packages]
        end
        subgraph STORE["Blob/Vector Storage"]
            EMB[Embeddings]
            FILES[Files]
            REFS[External References]
        end
    end

    L5 --> L4
    L4 --> L3
    L3 --> L2
    L2 --> L1

    style L5 fill:#e1f5fe,stroke:#01579b
    style L4 fill:#fff3e0,stroke:#e65100
    style L3 fill:#f3e5f5,stroke:#7b1fa2
    style L2 fill:#e8f5e9,stroke:#2e7d32
    style L1 fill:#fce4ec,stroke:#c2185b
```

---

## Diagram 2: INHERIT_CONTEXT Flow

This diagram illustrates the `INHERIT_CONTEXT` operation as defined in Section 6.

```mermaid
flowchart TB
    subgraph REQUEST["1. REQUEST"]
        REQ_DATA["thread_id<br/>filters<br/>max_tokens<br/>policies"]
    end

    subgraph RETRIEVAL["2. RETRIEVAL"]
        ENGINE["MMIP Engine pulls Thread<br/>from Data Layer"]
        subgraph THREAD["Thread: thr_12345"]
            CAP1[cap1] --> CAP2[cap2] --> CAP3[cap3]
        end
    end

    subgraph POLICY_CHECK["3. POLICY CHECK"]
        CHECK1["✓ Check visibility scopes"]
        CHECK2["✓ Check export permissions"]
        CHECK3["✓ Enforce retention rules"]
        ACCESS["User A ✓ → cap1, cap2<br/>User B ✗ → no access"]
    end

    subgraph TRANSFORM["4. TRANSFORMATION"]
        T1["• Apply redaction rules"]
        T2["• Summarize if over limit"]
        T3["• Mark derived capsules"]
        TOKENS["tokens: 5000 → 2000<br/>(summarized older caps)"]
    end

    subgraph OUTPUT["5. OUTPUT"]
        subgraph ENVELOPE["Signed Memory Envelope"]
            ENV_DATA["mmip_version: '0.1'<br/>context_id: 'ctx_9876'<br/>capsules: [...]<br/>integrity: {hash: ...}"]
        end
    end

    AGENT_IN[/"Agent / LLM"/] --> REQUEST
    REQUEST --> RETRIEVAL
    RETRIEVAL --> POLICY_CHECK
    POLICY_CHECK --> TRANSFORM
    TRANSFORM --> OUTPUT
    OUTPUT --> AGENT_OUT[/"Agent / LLM"/]

    style REQUEST fill:#e3f2fd,stroke:#1565c0
    style RETRIEVAL fill:#fff8e1,stroke:#f57f17
    style POLICY_CHECK fill:#e8f5e9,stroke:#2e7d32
    style TRANSFORM fill:#fce4ec,stroke:#c2185b
    style OUTPUT fill:#f3e5f5,stroke:#7b1fa2
    style ENVELOPE fill:#ede7f6,stroke:#512da8
```

---

## Diagram 3: Multi-Model Context Flow

This diagram shows how MMIP enables context continuity across model switches.

```mermaid
flowchart TB
    USER[/"User Request"/]
    
    subgraph MODELS["Model Pipeline"]
        direction LR
        M1["🧠 Reasoning Model<br/>(GPT-5.1)"]
        M2["💻 Code Model<br/>(Codex)"]
        M3["🎨 Image Model<br/>(DALL-E)"]
        
        M1 -->|"output"| M2
        M2 -->|"output"| M3
    end

    subgraph MMIP["MMIP Memory Layer"]
        subgraph THREAD["Thread: thr_project_001"]
            C1["cap_001<br/>user request"]
            C2["cap_002<br/>reason output"]
            C3["cap_003<br/>code output"]
            C1 --> C2 --> C3
        end
        POLICIES["Policies:<br/>visibility=all_models<br/>retention=session"]
    end

    USER --> M1
    M1 -->|"INHERIT_CONTEXT"| MMIP
    M2 -->|"INHERIT_CONTEXT"| MMIP
    M3 -->|"INHERIT_CONTEXT"| MMIP
    
    MMIP -->|"Memory Envelope"| M1
    MMIP -->|"Memory Envelope"| M2
    MMIP -->|"Memory Envelope"| M3

    RESULT[/"Result: Each model receives full context<br/>from previous steps without user re-entering"/]
    M3 --> RESULT

    style MODELS fill:#e1f5fe,stroke:#01579b
    style MMIP fill:#fff3e0,stroke:#e65100
    style THREAD fill:#fffde7,stroke:#f9a825
```

---

## Diagram 4: MMIP Data Model (Entity Relationship)

```mermaid
erDiagram
    CAPSULE {
        string capsule_id PK
        enum type
        enum scope
        object content
        object metadata
        object provenance
        object policies
    }
    
    THREAD {
        string thread_id PK
        string title
        string domain
        list participants
        enum retention
    }
    
    PACKAGE {
        string package_id PK
        string owner
        string name
        string description
        object policies
    }
    
    ENVELOPE {
        string context_id PK
        string mmip_version
        string thread_id FK
        object producer
        object policies
        object integrity
    }
    
    THREAD ||--|{ CAPSULE : "contains"
    PACKAGE ||--|{ CAPSULE : "references"
    ENVELOPE ||--|{ CAPSULE : "delivers"
    THREAD ||--o| ENVELOPE : "generates"
    PACKAGE ||--o| ENVELOPE : "generates"
    CAPSULE ||--o{ CAPSULE : "links_to"
```

---

## Diagram 5: Policy Decision Matrix

```mermaid
flowchart LR
    subgraph INPUT["Input Capsule"]
        CAP["Capsule<br/>scope: session<br/>policies: {...}"]
    end

    subgraph VISIBILITY["Visibility Check"]
        V1{"owner_only?"}
        V2{"all_models?"}
        V3{"no_external?"}
    end

    subgraph EXPORT["Export Check"]
        E1{"allow?"}
        E2{"redact?"}
        E3{"forbid?"}
    end

    subgraph RETENTION["Retention Check"]
        R1{"ephemeral?"}
        R2{"session?"}
        R3{"long_term?"}
    end

    subgraph OUTPUT["Output"]
        PASS["✓ Include in Envelope"]
        REDACT["⚠ Include Redacted"]
        DENY["✗ Exclude"]
    end

    CAP --> V1
    V1 -->|"no"| V2
    V1 -->|"yes + owner"| E1
    V2 -->|"yes"| E1
    V2 -->|"no"| V3
    V3 -->|"yes + internal"| E1
    V3 -->|"no"| DENY

    E1 -->|"yes"| R1
    E1 -->|"no"| E2
    E2 -->|"yes"| REDACT
    E2 -->|"no"| E3
    E3 -->|"yes"| DENY

    R1 -->|"expired"| DENY
    R1 -->|"active"| PASS
    R2 -->|"in session"| PASS
    R3 --> PASS

    style PASS fill:#c8e6c9,stroke:#2e7d32
    style REDACT fill:#fff9c4,stroke:#f57f17
    style DENY fill:#ffcdd2,stroke:#c62828
```

---

## Diagram 6: Thread Fork/Merge Operations

```mermaid
gitGraph
    commit id: "cap_001" tag: "user_msg"
    commit id: "cap_002" tag: "model_response"
    commit id: "cap_003" tag: "analysis"
    branch exploration
    checkout exploration
    commit id: "cap_004" tag: "option_A"
    commit id: "cap_005" tag: "expand_A"
    checkout main
    commit id: "cap_006" tag: "option_B"
    commit id: "cap_007" tag: "expand_B"
    merge exploration id: "cap_008" tag: "merged_result"
    commit id: "cap_009" tag: "final_summary"
```

---

## Diagram 7: Capsule Lifecycle State Machine

```mermaid
stateDiagram-v2
    [*] --> Created: ATTACH_MEMORY
    
    Created --> Active: validate
    Created --> Rejected: invalid
    
    Active --> Summarized: SUMMARIZE
    Active --> Redacted: REDACT
    Active --> Tagged: TAG_CAPSULE
    Active --> Archived: retention_expired
    Active --> Deleted: DELETE_CAPSULE
    
    Summarized --> Active: restore
    Summarized --> Archived: retention_expired
    
    Redacted --> Archived: retention_expired
    
    Tagged --> Active: untag
    Tagged --> Summarized: SUMMARIZE
    
    Archived --> [*]: purge
    Deleted --> [*]: hard_delete
    Rejected --> [*]

    note right of Active
        Primary state for
        capsules in use
    end note
    
    note right of Redacted
        PII/secrets removed
        Tombstone preserved
    end note
```

---

## Diagram 8: MMIP Operations Sequence

```mermaid
sequenceDiagram
    autonumber
    participant U as User/Agent
    participant O as Operations Layer
    participant I as Inheritance Layer
    participant P as Policy Layer
    participant D as Data Layer

    Note over U,D: Thread Creation Flow
    U->>O: INIT_THREAD(metadata)
    O->>D: create_thread()
    D-->>O: thread_id
    O-->>U: thread_id

    Note over U,D: Attach Memory Flow
    U->>O: ATTACH_MEMORY(thread_id, capsule)
    O->>P: validate_policies(capsule)
    P-->>O: ✓ valid
    O->>D: store_capsule(capsule)
    D-->>O: capsule_id
    O-->>U: success

    Note over U,D: Inherit Context Flow
    U->>O: INHERIT_CONTEXT(request)
    O->>D: fetch_thread(thread_id)
    D-->>O: thread + capsules
    O->>P: check_policies(capsules)
    P-->>O: filtered_capsules
    O->>I: compose_context(capsules)
    I->>I: filter + summarize + redact
    I-->>O: transformed_capsules
    O->>O: sign_envelope()
    O-->>U: Memory Envelope

    Note over U,D: Export Package Flow
    U->>O: EXPORT_PACKAGE(package_id)
    O->>D: fetch_package(package_id)
    D-->>O: package
    O->>P: enforce_export_policies()
    P->>I: apply_redactions()
    I-->>P: redacted_content
    P-->>O: exportable_package
    O-->>U: exported_package
```

---

## Diagram 9: MMIP Compliance Levels

```mermaid
flowchart TB
    subgraph L1["Level 1: Basic"]
        L1_CAP["Capsules"]
        L1_THR["Threads"]
        L1_ENV["Envelopes"]
        L1_OPS["INIT_THREAD<br/>ATTACH_MEMORY<br/>INHERIT_CONTEXT<br/>LIST_CAPSULES<br/>GET_CAPSULE<br/>GENERATE_ENVELOPE<br/>VALIDATE_ENVELOPE"]
    end

    subgraph L2["Level 2: User-Controlled"]
        L2_PKG["Context Packages"]
        L2_EXP["Export"]
        L2_RED["Redaction"]
        L2_OPS["CREATE_PACKAGE<br/>GET_PACKAGE<br/>LIST_PACKAGES<br/>EXPORT_PACKAGE<br/>REDACT_CAPSULE<br/>DELETE_CAPSULE"]
    end

    subgraph L3["Level 3: Full Agentic"]
        L3_INH["Inheritance"]
        L3_SUM["Summarization"]
        L3_LIN["Lineage"]
        L3_INT["Integrity"]
        L3_OPS["FORK_THREAD<br/>MERGE_THREADS<br/>SNAPSHOT_THREAD<br/>APPLY_PACKAGE<br/>SEARCH_MEMORY<br/>SEARCH_PACKAGES<br/>TAG_CAPSULES"]
    end

    L1 --> L2
    L2 --> L3

    style L1 fill:#c8e6c9,stroke:#2e7d32
    style L2 fill:#fff9c4,stroke:#f57f17
    style L3 fill:#e1bee7,stroke:#7b1fa2
```

---

## Diagram 10: MMIP ↔ AMPEL360 Integration

```mermaid
flowchart TB
    subgraph AMPEL["AMPEL360 Intelligent Aircraft"]
        subgraph L23["ATA 23 - Communications (L2-LINKS)"]
            direction TB
            MMIP["23-97 MMIP<br/>Memory Protocol"]
            ASTL["23-96 AST-L<br/>Technical Language"]
            FAIRCCC["23-95 COMM_NN<br/>FAirCCC Transport"]
        end

        subgraph CAOS_AGENTS["CAOS Agent Ecosystem"]
            SHM["SHM Agent"]
            ICA["ICA Agent"]
            MRO["MRO Agent"]
            OCC["OCC Agent"]
        end

        subgraph N_AXIS["N-Axis: Neural Networks"]
            FL["97-40-20<br/>Federated Learning"]
            MD["97-40-30<br/>Model Deployment"]
        end

        subgraph SYSTEMS["Core Systems"]
            DPP["DPP<br/>Traceability"]
            ANCHORS["ANCHORS<br/>Circularity"]
        end
    end

    SHM -->|"ATTACH_MEMORY"| MMIP
    MMIP -->|"INHERIT_CONTEXT"| ICA
    ICA -->|"ATTACH_MEMORY"| MMIP
    MMIP -->|"INHERIT_CONTEXT"| MRO
    MRO -->|"ATTACH_MEMORY"| MMIP
    MMIP -->|"INHERIT_CONTEXT"| OCC

    MMIP <-->|"expresses"| ASTL
    MMIP <-->|"transports"| FAIRCCC
    
    MMIP -->|"provenance"| DPP
    MMIP -->|"context"| FL
    MMIP -->|"packages"| MD
    MMIP -->|"resources"| ANCHORS

    style L23 fill:#e3f2fd,stroke:#1565c0
    style CAOS_AGENTS fill:#fff3e0,stroke:#e65100
    style N_AXIS fill:#f3e5f5,stroke:#7b1fa2
    style SYSTEMS fill:#e8f5e9,stroke:#2e7d32
```

---

## Diagram 11: CAOS Agent Pipeline with MMIP

```mermaid
sequenceDiagram
    autonumber
    participant SHM as SHM Agent
    participant MMIP as MMIP Engine
    participant ICA as ICA Agent
    participant MRO as MRO Agent
    participant DPP as DPP System

    Note over SHM,DPP: Anomaly Detection → Task Generation → Repair Scheduling

    SHM->>SHM: Detect anomaly in Stringer F2
    
    SHM->>MMIP: ATTACH_MEMORY(thread, capsule_shm_anomaly)
    Note right of MMIP: Capsule contains:<br/>AST-L: CAOS.Event.SHMA.RivetF12 : severity : HIGH @INFLIGHT

    SHM->>MMIP: ATTACH_MEMORY(thread, capsule_shm_analysis)
    
    ICA->>MMIP: INHERIT_CONTEXT(thread, max_tokens=2000)
    MMIP-->>ICA: Memory Envelope (SHM context)
    
    ICA->>ICA: Generate inspection task
    ICA->>MMIP: ATTACH_MEMORY(thread, capsule_ica_task)
    ICA->>DPP: Log task to DPP
    
    MRO->>MMIP: INHERIT_CONTEXT(thread, max_tokens=3000)
    MMIP-->>MRO: Memory Envelope (SHM + ICA context)
    
    MRO->>MRO: Schedule repair
    MRO->>MMIP: ATTACH_MEMORY(thread, capsule_mro_schedule)
    MRO->>DPP: Log repair to DPP

    Note over SHM,DPP: Complete traceability maintained via MMIP + DPP
```

---

## Diagram 12: MMIP Capsule ↔ AST-L Statement Mapping

```mermaid
flowchart LR
    subgraph MMIP_CAP["MMIP Capsule"]
        CAP_ID["capsule_id: cap_shm_001"]
        CAP_TYPE["type: annotation"]
        CAP_SCOPE["scope: session"]
        CAP_CONTENT["content: {...}"]
        CAP_PROV["provenance:<br/>creator: SHM_Agent<br/>timestamp: 2025-11-28T10:00:00Z"]
        CAP_META["metadata:<br/>tags: [shm, anomaly]<br/>domain: structural"]
    end

    subgraph ASTL_STMT["AST-L Statement"]
        ENTITY["entity:<br/>CAOS.Event.SHMA.RivetF12"]
        PRED["predicate:<br/>severity"]
        VALUE["value:<br/>HIGH"]
        CTX["context:<br/>@INFLIGHT"]
        LIFE["lifecycle:<br/>#L07_VV"]
    end

    CAP_CONTENT -->|"encodes"| ENTITY
    CAP_CONTENT -->|"encodes"| PRED
    CAP_CONTENT -->|"encodes"| VALUE
    CAP_SCOPE -->|"maps to"| CTX
    CAP_META -->|"maps to"| LIFE

    style MMIP_CAP fill:#e3f2fd,stroke:#1565c0
    style ASTL_STMT fill:#fff3e0,stroke:#e65100
```

---

## Diagram 13: Memory Package ↔ CUC Bundle Mapping

```mermaid
flowchart TB
    subgraph MMIP_PKG["MMIP Context Package"]
        PKG_ID["package_id"]
        PKG_CAPS["capsule_refs: [cap1, cap2, ...]"]
        PKG_POL["policies: {visibility, export, retention}"]
        PKG_SUM["summary_capsule"]
    end

    subgraph CUC["CUC Update Bundle"]
        CUC_ID["bundle_id"]
        CUC_MODEL["model_meta"]
        CUC_WEIGHTS["weights"]
        CUC_EVAL["eval_report"]
        CUC_SAFETY["safety_case"]
        CUC_SIG["signature"]
    end

    PKG_ID <-->|"≈"| CUC_ID
    PKG_CAPS <-->|"≈"| CUC_MODEL
    PKG_POL <-->|"≈"| CUC_SAFETY
    PKG_SUM <-->|"≈"| CUC_EVAL

    style MMIP_PKG fill:#e8f5e9,stroke:#2e7d32
    style CUC fill:#fce4ec,stroke:#c2185b
```

---

## Diagram 14: Complete ATA 23 Communications Stack

```mermaid
flowchart TB
    subgraph ATA23["ATA 23 - COMMUNICATIONS"]
        direction TB
        
        subgraph MMIP_LAYER["23-97: MMIP — Memory Protocol"]
            MMIP_WHAT["What to Remember"]
            CAPS["Capsules"]
            THREADS["Threads"]
            PACKAGES["Packages"]
            ENVELOPES["Envelopes"]
        end

        subgraph ASTL_LAYER["23-96: AST-L — Technical Language"]
            ASTL_HOW["How to Express"]
            SEM["Semantics"]
            SYN["Syntax"]
            SYNOP["Synopsis"]
            TECH["Technology"]
        end

        subgraph FAIRCCC_LAYER["23-95: COMM_NN — Transport"]
            FAIR_TRANS["How to Transmit"]
            GRAD["CFLF-GRAD"]
            MODEL["CFLF-MODEL"]
            TELEM["CFLF-TELEM"]
            SAFETY["CFLF-SAFETY"]
            CUC["CUC"]
        end
    end

    MMIP_LAYER -->|"content expressed via"| ASTL_LAYER
    ASTL_LAYER -->|"transported via"| FAIRCCC_LAYER

    style MMIP_LAYER fill:#e1f5fe,stroke:#0277bd
    style ASTL_LAYER fill:#fff8e1,stroke:#ff8f00
    style FAIRCCC_LAYER fill:#f3e5f5,stroke:#7b1fa2
```

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | MMIP-ANNEX-D-DIAGRAMS-001 |
| **Version** | 1.1 |
| **Date** | 2025-11-28 |
| **Status** | DRAFT |

### AI Disclosure

- **Generated with assistance of:** AI (Claude, Anthropic)
- **Prompted by:** Amedeo Pelliccia
- **Status:** DRAFT — Subject to human review
- **Last AI update:** 2025-11-28

---

*END OF DOCUMENT*
