#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2025 AMPEL360 Project Contributors

"""
ai_author_synth.py

AI-driven technical publication generator for AMPEL360 ICA documentation.
Generates compliant technical publications including:
- Data Modules (DMC) for S1000D
- Markdown documentation for OPT-IN Framework
- Interface Control Documents (ICD)
- Reliability Exchange (REX) sheets
- ICA blocks and maintenance procedures

Usage:
    python -m tools.ica.cgen.ai_author_synth --type dmc --ata 53 --subject "Wing Structure"
    python -m tools.ica.cgen.ai_author_synth --type icd --source ATA_24 --target ATA_71
    python -m tools.ica.cgen.ai_author_synth --type procedure --task "Inspection"
"""

import argparse
import hashlib
import json
import logging
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Repository root
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
OPT_IN_FRAMEWORK = REPO_ROOT / "OPT-IN_FRAMEWORK"


@dataclass
class DocumentSpec:
    """Specification for a generated document."""
    doc_type: str
    ata_chapter: str
    title: str
    subject: str
    author: str = "AI Author (prompted by Amedeo Pelliccia)"
    version: str = "1.0"
    status: str = "Draft"
    metadata: Dict = field(default_factory=dict)


@dataclass
class GeneratedDocument:
    """Represents a generated document."""
    id: str
    spec: DocumentSpec
    content: str
    output_path: Path
    created_at: str


class AIAuthorSynthesizer:
    """AI-driven technical publication generator."""
    
    # Document type templates
    TEMPLATES = {
        "dmc": "data_module",
        "icd": "interface_control",
        "rex": "reliability_exchange",
        "procedure": "maintenance_procedure",
        "ica": "ica_block",
        "overview": "system_overview",
    }
    
    # ATA chapter information
    ATA_INFO = {
        "02": ("Operations Information", "I-INFRASTRUCTURES"),
        "04": ("Airworthiness Limitations", "O-ORGANIZATION"),
        "05": ("Time Limits/Maintenance Checks", "O-ORGANIZATION"),
        "21": ("Air Conditioning", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"),
        "24": ("Electrical Power", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"),
        "25": ("Equipment/Furnishings", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"),
        "27": ("Flight Controls", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"),
        "28": ("Fuel", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"),
        "29": ("Hydraulic Power", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"),
        "32": ("Landing Gear", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"),
        "34": ("Navigation", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"),
        "53": ("Fuselage", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"),
        "71": ("Powerplant", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"),
        "72": ("Engine", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"),
        "85": ("Infrastructure Interface Standards", "I-INFRASTRUCTURES"),
        "95": ("Digital Product Passport", "N-NEURAL_NETWORKS_USERS_TRACEABILITY"),
    }
    
    def __init__(self, repo_root: Path = REPO_ROOT):
        self.repo_root = repo_root
        self.opt_in_root = repo_root / "OPT-IN_FRAMEWORK"
    
    def generate_doc_id(self, doc_type: str, ata: str) -> str:
        """Generate a unique document ID."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        content = f"{doc_type}-{ata}-{timestamp}"
        hash_suffix = hashlib.sha256(content.encode()).hexdigest()[:8].upper()
        return f"DOC-{ata}-{doc_type.upper()}-{hash_suffix}"
    
    def get_output_path(self, spec: DocumentSpec) -> Path:
        """Determine output path based on document spec."""
        ata_num = spec.ata_chapter.zfill(2)
        ata_info = self.ATA_INFO.get(ata_num, ("Unknown", "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS"))
        ata_name, framework_area = ata_info
        
        # Build path based on document type
        if spec.doc_type == "dmc":
            folder = "04_Design"
        elif spec.doc_type == "icd":
            folder = "05_Interfaces"
        elif spec.doc_type == "procedure":
            folder = "14_Ops_Std_Sustain"
        elif spec.doc_type == "ica":
            folder = "10_Certification"
        else:
            folder = "01_Overview"
        
        # Sanitize filename
        safe_subject = spec.subject.replace(" ", "_").replace("/", "-")[:50]
        filename = f"{ata_num}-00-00-{spec.doc_type.upper()}_{safe_subject}.md"
        
        # Build full path
        ata_dir = f"ATA_{ata_num}-{ata_name.upper().replace(' ', '_').replace('/', '_')}"
        path = self.opt_in_root / framework_area / ata_dir / f"{ata_num}-00_GENERAL" / f"{ata_num}-00-{folder.split('_')[0]}_{folder.split('_', 1)[1]}"
        
        return path / filename
    
    def generate_dmc(self, spec: DocumentSpec) -> str:
        """Generate a Data Module Content (S1000D-style)."""
        ata = spec.ata_chapter.zfill(2)
        ata_name = self.ATA_INFO.get(ata, ("Unknown",))[0]
        
        content = f"""# {spec.title}

**Data Module Code:** DMC-AMPEL360-{ata}-00-00-00AA-{spec.doc_type.upper()}  
**ATA Chapter:** {ata} - {ata_name}  
**Issue Date:** {datetime.now().strftime("%Y-%m-%d")}  
**Version:** {spec.version}  
**Status:** {spec.status}

---

## 1. Purpose and Scope

This data module provides technical documentation for {spec.subject} as part of the 
AMPEL360-BWB-H₂-Hy-E aircraft program. It is designed to support maintenance, repair, 
and overhaul (MRO) operations while ensuring continued airworthiness compliance.

### 1.1 Applicability

- **Aircraft Type:** AMPEL360-BWB-H₂-Hy-E
- **ATA Chapter:** {ata} - {ata_name}
- **Effectivity:** All aircraft unless otherwise specified

### 1.2 References

| Document ID | Title | Version |
|-------------|-------|---------|
| CS-25 | Certification Specifications for Large Aeroplanes | Current |
| ATA iSpec 2200 | Information Standards for Aviation Maintenance | Current |
| S1000D | International Specification for Technical Publications | Issue 5.0 |

---

## 2. Description

### 2.1 General

{spec.subject} description and technical details.

> **Note:** This section should be completed with specific technical content 
> by domain experts.

### 2.2 System Architecture

```
┌─────────────────────────────────────────────┐
│            {spec.subject}                   │
├─────────────────────────────────────────────┤
│  Component A  │  Component B  │  Component C │
├───────────────┼───────────────┼──────────────┤
│   Interface   │   Interface   │   Interface  │
└───────────────┴───────────────┴──────────────┘
```

### 2.3 Key Parameters

| Parameter | Value | Unit | Tolerance |
|-----------|-------|------|-----------|
| TBD | TBD | TBD | TBD |

---

## 3. Operation

### 3.1 Normal Operation

Description of normal operating procedures.

### 3.2 Abnormal Operation

Description of abnormal conditions and responses.

---

## 4. Maintenance

### 4.1 Scheduled Maintenance

| Task | Interval | Reference |
|------|----------|-----------|
| Inspection | Per MPD | TBD |
| Lubrication | Per MPD | TBD |

### 4.2 Unscheduled Maintenance

Troubleshooting and corrective action procedures.

---

## 5. Illustrated Parts Data

Reference to Illustrated Parts Catalog (IPC) for {spec.subject}.

---

## Document Control

- **Document ID:** DMC-AMPEL360-{ata}-00-00-00AA
- **Generated by:** {spec.author}
- **Status:** {spec.status} – Subject to human review and approval
- **CAOS Integration:** This document is managed by the CAOS ICA Enabling Toolchain
- **Last AI Update:** {datetime.now().strftime("%Y-%m-%d")}

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| {spec.version} | {datetime.now().strftime("%Y-%m-%d")} | {spec.author} | Initial generation |

"""
        return content
    
    def generate_icd(self, spec: DocumentSpec) -> str:
        """Generate an Interface Control Document."""
        ata = spec.ata_chapter.zfill(2)
        ata_name = self.ATA_INFO.get(ata, ("Unknown",))[0]
        
        content = f"""# Interface Control Document: {spec.title}

**ICD ID:** ICD-AMPEL360-{ata}-{spec.metadata.get('target_ata', 'XX')}  
**ATA Chapter:** {ata} - {ata_name}  
**Interface Type:** {spec.metadata.get('interface_type', 'Data/Power/Mechanical')}  
**Issue Date:** {datetime.now().strftime("%Y-%m-%d")}  
**Version:** {spec.version}  
**Status:** {spec.status}

---

## 1. Scope

This Interface Control Document (ICD) defines the interface between:
- **Source System:** ATA {ata} - {ata_name}
- **Target System:** ATA {spec.metadata.get('target_ata', 'XX')} - {spec.metadata.get('target_name', 'TBD')}

### 1.1 Purpose

Define the physical, electrical, and data interfaces to ensure interoperability
and support continued airworthiness.

### 1.2 References

| Document | Title | Version |
|----------|-------|---------|
| ICD-AMPEL360-MASTER | Master Interface Control Document | Current |
| CS-25.1309 | Equipment, Systems, and Installations | Current |

---

## 2. Interface Definition

### 2.1 Physical Interface

| Parameter | Source | Target | Notes |
|-----------|--------|--------|-------|
| Connector Type | TBD | TBD | |
| Mounting | TBD | TBD | |
| Envelope | TBD | TBD | |

### 2.2 Electrical Interface

| Signal | Type | Range | Units | Direction |
|--------|------|-------|-------|-----------|
| TBD | Analog/Digital | TBD | TBD | In/Out |

### 2.3 Data Interface

| Parameter | Protocol | Format | Rate | Notes |
|-----------|----------|--------|------|-------|
| TBD | ARINC 429 / CAN / Ethernet | TBD | TBD | |

---

## 3. Interface Requirements

### 3.1 Performance Requirements

| Requirement ID | Description | Verification Method |
|----------------|-------------|---------------------|
| ICD-REQ-001 | TBD | Analysis/Test |

### 3.2 Environmental Requirements

Per DO-160G environmental categories.

---

## 4. Verification

### 4.1 Interface Verification Matrix

| Requirement | Test Method | Status | Evidence |
|-------------|-------------|--------|----------|
| ICD-REQ-001 | TBD | Planned | TBD |

---

## Document Control

- **Document ID:** ICD-AMPEL360-{ata}-{spec.metadata.get('target_ata', 'XX')}
- **Generated by:** {spec.author}
- **Status:** {spec.status} – Subject to human review and approval
- **CAOS Integration:** This document is managed by the CAOS ICA Enabling Toolchain
- **Last AI Update:** {datetime.now().strftime("%Y-%m-%d")}

"""
        return content
    
    def generate_procedure(self, spec: DocumentSpec) -> str:
        """Generate a maintenance procedure document."""
        ata = spec.ata_chapter.zfill(2)
        ata_name = self.ATA_INFO.get(ata, ("Unknown",))[0]
        
        content = f"""# Maintenance Procedure: {spec.title}

**Procedure ID:** PROC-AMPEL360-{ata}-{spec.metadata.get('task_code', '001')}  
**ATA Chapter:** {ata} - {ata_name}  
**Task Type:** {spec.metadata.get('task_type', 'Inspection/Repair/Replacement')}  
**Issue Date:** {datetime.now().strftime("%Y-%m-%d")}  
**Version:** {spec.version}  
**Status:** {spec.status}

---

## 1. General

### 1.1 Purpose

This procedure provides instructions for {spec.subject} on the AMPEL360-BWB-H₂-Hy-E aircraft.

### 1.2 Applicability

- **Aircraft Type:** AMPEL360-BWB-H₂-Hy-E
- **Effectivity:** All applicable aircraft
- **Task Interval:** Per Maintenance Planning Document (MPD)

### 1.3 References

| Document | Title |
|----------|-------|
| AMM-{ata}-00 | Aircraft Maintenance Manual - {ata_name} |
| IPC-{ata}-00 | Illustrated Parts Catalog - {ata_name} |
| MPD-AMPEL360 | Maintenance Planning Document |

---

## 2. Safety Precautions

### 2.1 Warnings

> ⚠️ **WARNING:** [Safety-critical warnings go here]

### 2.2 Cautions

> ⚡ **CAUTION:** [Equipment protection cautions go here]

### 2.3 Personal Protective Equipment

| PPE Item | Required |
|----------|----------|
| Safety glasses | Yes |
| Gloves | As required |
| Hearing protection | As required |

---

## 3. Tools and Equipment

| Item | Part Number | Quantity |
|------|-------------|----------|
| TBD | TBD | TBD |

---

## 4. Materials and Consumables

| Item | Specification | Quantity |
|------|---------------|----------|
| TBD | TBD | As required |

---

## 5. Procedure

### 5.1 Preparation

1. Ensure aircraft is properly grounded
2. Obtain necessary tools and materials
3. Review safety precautions

### 5.2 {spec.subject}

1. **Step 1:** [Procedure step description]
   - Sub-step a
   - Sub-step b

2. **Step 2:** [Procedure step description]

3. **Step 3:** [Procedure step description]

### 5.3 Post-Task Actions

1. Inspect completed work
2. Document task completion in maintenance records
3. Return tools and materials

---

## 6. Inspection Criteria

| Check Point | Acceptance Criteria | Method |
|-------------|---------------------|--------|
| TBD | TBD | Visual/Measurement |

---

## 7. Troubleshooting

| Symptom | Probable Cause | Corrective Action |
|---------|----------------|-------------------|
| TBD | TBD | TBD |

---

## Document Control

- **Procedure ID:** PROC-AMPEL360-{ata}-{spec.metadata.get('task_code', '001')}
- **Generated by:** {spec.author}
- **Status:** {spec.status} – Subject to human review and approval
- **CAOS Integration:** This document is managed by the CAOS ICA Enabling Toolchain
- **Last AI Update:** {datetime.now().strftime("%Y-%m-%d")}

"""
        return content
    
    def generate_document(self, spec: DocumentSpec) -> GeneratedDocument:
        """Generate a document based on specification."""
        logger.info(f"Generating {spec.doc_type} document for ATA {spec.ata_chapter}")
        
        # Select generator based on type
        generators = {
            "dmc": self.generate_dmc,
            "icd": self.generate_icd,
            "procedure": self.generate_procedure,
        }
        
        generator = generators.get(spec.doc_type, self.generate_dmc)
        content = generator(spec)
        
        doc_id = self.generate_doc_id(spec.doc_type, spec.ata_chapter)
        output_path = self.get_output_path(spec)
        
        return GeneratedDocument(
            id=doc_id,
            spec=spec,
            content=content,
            output_path=output_path,
            created_at=datetime.now().isoformat()
        )
    
    def save_document(self, doc: GeneratedDocument, output_path: Optional[Path] = None) -> Path:
        """Save generated document to file."""
        path = output_path or doc.output_path
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(doc.content)
        
        logger.info(f"Saved document: {path}")
        return path


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="AI-driven technical publication generator"
    )
    parser.add_argument(
        "--type",
        choices=["dmc", "icd", "rex", "procedure", "ica", "overview"],
        default="dmc",
        help="Document type to generate"
    )
    parser.add_argument(
        "--ata",
        required=True,
        help="ATA chapter number (e.g., 53)"
    )
    parser.add_argument(
        "--subject",
        required=True,
        help="Subject/topic of the document"
    )
    parser.add_argument(
        "--title",
        help="Document title (auto-generated if not provided)"
    )
    parser.add_argument(
        "--target-ata",
        help="Target ATA chapter for ICD documents"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Custom output path"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Generate but don't save document"
    )
    
    args = parser.parse_args()
    
    # Build spec
    metadata = {}
    if args.target_ata:
        metadata["target_ata"] = args.target_ata
    
    spec = DocumentSpec(
        doc_type=args.type,
        ata_chapter=args.ata,
        title=args.title or f"{args.type.upper()}: {args.subject}",
        subject=args.subject,
        metadata=metadata
    )
    
    # Generate document
    synthesizer = AIAuthorSynthesizer()
    doc = synthesizer.generate_document(spec)
    
    print(f"\n{'='*60}")
    print(f"Document Generated: {doc.id}")
    print(f"{'='*60}")
    print(f"Type: {spec.doc_type}")
    print(f"ATA Chapter: {spec.ata_chapter}")
    print(f"Subject: {spec.subject}")
    print(f"Output Path: {doc.output_path}")
    
    if args.dry_run:
        print("\n[Dry run - document not saved]")
        print("\nPreview (first 50 lines):")
        print("-" * 40)
        for line in doc.content.split("\n")[:50]:
            print(line)
    else:
        output_path = args.output or doc.output_path
        saved_path = synthesizer.save_document(doc, output_path)
        print(f"\n✅ Document saved: {saved_path}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
