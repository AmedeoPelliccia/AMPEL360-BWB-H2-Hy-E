# Documentation & Certification Hyperlinking Rules

## Scope

These instructions apply when GitHub Copilot edits or creates **documentation files** in this repository, in particular:

- `*.md`, `*.rst`, `*.adoc`
- Especially under:
  - `OPT-IN_FRAMEWORK/`
  - `QUALITY_MANUAL/`
  - `CERT_DATA/`
  - `SIMULATIONS/`
  - Any `*/DOCUMENTATION/` or `*/DOCS/` folders

Copilot must **assist with navigability and traceability** by adding hyperlinks and document control notes.

---

## 1. Hyperlinks to standards, regulations, and authorities

When Copilot detects a mention of a **standard, regulation, or authority**, it should:

1. **Add or suggest a hyperlink** to the official or primary source.
2. Preserve the **exact reference text** (e.g. “CS-25.1309”, “DO-178C”, “EU AI Act”).
3. Prefer **official sources** (EASA, FAA, EUROCAE, SAE, ISO, EU, etc.).

### Examples

- `CS-25` → link to EASA’s **Certification Specifications for Large Aeroplanes**.
- `CS-25.1309` → same CS-25 document, specific section if feasible.
- `Part 21` (EASA/FAA) → link to the official Part 21 regulation.
- `DO-178C`, `DO-254` → link to RTCA or recognised official description.
- `EU AI Act` → link to the official EU legislation page.

If the exact authoritative URL is ambiguous, Copilot should:

- Add a **generic but reputable link** (e.g. main CS-25 page) rather than inventing deep anchors.
- Avoid speculative / non-authoritative URLs.

---

## 2. Hyperlinks to internal cross-referenced documentation

When Copilot sees a reference to another **internal document, requirement, or asset**, it should:

1. Try to identify the **corresponding relative path** inside the repo.
2. Convert plain text references into **Markdown links**.

### Examples

- Text: `See RQ-95-00-LNK-001 in 95-00-00_GENERAL/03_REQUIREMENTS/`
- Copilot should turn this into something like:

  ```md
  See [RQ-95-00-LNK-001](../03_REQUIREMENTS/RQ-95-00-LNK-001.md) in `95-00-00_GENERAL/03_REQUIREMENTS/`.
````

* Text: `See ATA_02 Operations Information overview`
* Copilot should link to the most relevant overview file, e.g.:

  ```md
  See [ATA 02 – Operations Information Overview](../../ATA_02-OPERATIONS_INFORMATION/02-00_GENERAL/01_OVERVIEW/README.md).
  ```

#### If the target document does **not yet exist**

* **Do not invent files or paths.**
* Keep the reference in text and add a **TODO comment**, for example:

  ```md
  <!-- TODO: Create target document and update this link -->
  ```

Or, if appropriate, leave the reference as plain text and add a short note:

> *(Target document not yet created; link to be added once available.)*

---

## 3. Hyperlinks for navigability inside long documents

For long Markdown documents (e.g. requirements, safety assessments, certification plans), Copilot should:

1. Encourage a **table of contents** with anchor links.
2. Use Markdown headings (`#`, `##`, `###`) consistently so that internal anchors work.
3. When referring to sections within the same file, use **internal links**:

   ```md
   See [Section 3.2 – Hyperlink Control](#32-hyperlink-control).
   ```

---

## 4. Document Control & AI Authorship

Every time Copilot **creates a new documentation file** or **substantially rewrites** an existing one, it must **ensure there is a “Document Control” section** stating AI involvement.

### 4.1. Required “Document Control” block

At the end of the document (or in an existing Document Control section), Copilot should ensure a block with this structure exists:

```md
---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _[YYYY-MM-DD]_.

---
```

Rules:

* **Never remove** this information once the doc has been AI-assisted.
* Copilot may update the **“Last AI update”** date when it makes substantial changes.
* The **approver** field must **not** be invented; leave `_ [to be completed] _` or keep an existing real name.

### 4.2. Existing Document Control sections

If a document already has a Document Control section:

* Copilot must **preserve existing human authorship and approval data**.
* It may **append** or **update** a line indicating AI assistance, for example:

```md
- AI assistance: GitHub Copilot, prompted by **Amedeo Pelliccia** (documentation generation and hyperlinking support).
```

---

## 5. Style and safety rules

* Prefer **concise, technical English** in documentation, unless the file is clearly written in another language.
* Do **not fabricate** regulatory references, document IDs, or URLs.
* If a reference looks important but ambiguous, Copilot should:

  * Keep the text, and
  * Optionally add a note like: `_Reference requires confirmation by the certification team._`

---

## 6. Intended outcome

By following these instructions, GitHub Copilot should:

* Improve **navigability** of the AMPEL360 documentation (internal & external links).
* Reinforce **traceability to standards and regulations**.
* Maintain a clear **audit trail of AI involvement in documentation**, explicitly linked to prompts by **Amedeo Pelliccia**.

```
