# AMPEL360 SBOM Snapshot (SPDX)

## 0. Applicability & Context

- **Applicability:** [LC-04 Data, AI & DPP], [LC-06 Resources & Finance], [ATA_96_Digital_Product_Passport], [ATA_98_Traceability_and_Audit]  
- **Document Type:** Software Bill of Materials (SBOM) — SPDX 2.3 snapshot  
- **Scope:** `com.github.AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E@MAIN`  
- **Declared Project License:** `Apache-2.0`

This page summarizes the automatically generated SPDX SBOM for the AMPEL360 repository and links it into the OPT-IN / DPP / AI governance views.

---

## 1. SPDX Document Metadata

| Field               | Value                                                                 |
|---------------------|-----------------------------------------------------------------------|
| `spdxVersion`       | `SPDX-2.3`                                                            |
| `dataLicense`       | `CC0-1.0`                                                             |
| `SPDXID`            | `SPDXRef-DOCUMENT`                                                    |
| `name`              | `com.github.AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E`                     |
| `documentNamespace` | `https://spdx.org/spdxdocs/protobom/c01605a5-4cd3-4fd2-98ad-6d17a12b475e` |
| `created`           | `2025-12-03T11:48:52Z`                                                |
| `creators`          | `protobom`, `GitHub Dependency Graph`, `Automatic Dependency Submission` |

**Described project package**

| Field          | Value                                                                 |
|----------------|-----------------------------------------------------------------------|
| `SPDXID`       | `SPDXRef-github-AmedeoPelliccia-AMPEL360-BWB-H2-Hy-E-MAIN-32d827`     |
| `versionInfo`  | `MAIN` (branch)                                                       |
| `downloadLocation` | `git+https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E`     |
| `licenseDeclared`  | `Apache-2.0`                                                      |
| `relationship` | `SPDXRef-DOCUMENT DESCRIBES this package`                             |

---

## 2. Runtime Dependency Overview

### 2.1 Python Runtime Stack (key packages)

| Package          | Version   | License (concluded)                      | Notes                           |
|------------------|-----------|------------------------------------------|---------------------------------|
| `fastapi`        | 0.123.5   | (not declared in snippet → typical: MIT/BSD-3) | API server framework            |
| `pydantic`       | 2.12.5    | (not declared; core under MIT)          | Data models & validation        |
| `pydantic-core`  | 2.41.5    | —                                      | Pydantic engine                 |
| `annotated-types`| 0.7.0     | MIT                                     | Type annotations support        |
| `anyio`          | 4.12.0    | MIT                                     | Async I/O                       |
| `uvicorn`        | 0.38.0    | BSD-3-Clause                            | ASGI server                     |
| `uvloop`         | 0.22.1    | Apache-2.0 AND MIT                      | High-performance event loop     |
| `httpx`          | 0.28.1    | BSD-3-Clause                            | HTTP client                     |
| `httpcore`       | 1.0.9     | BSD-2-Clause AND BSD-3-Clause           | HTTP transport for `httpx`      |
| `requests`       | 2.32.5    | Apache-2.0                              | HTTP client (classic)           |
| `urllib3`        | 2.5.0     | MIT                                     | HTTP plumbing                   |
| `websockets`     | 15.0.1    | BSD-3-Clause                            | WebSocket support               |
| `pytest`         | 9.0.1     | MIT                                     | Test framework                  |
| `markdown`       | 3.10      | BSD-3-Clause                            | Markdown processing             |
| `pyyaml`         | 6.0.3     | MIT                                     | YAML parsing                    |
| `starlette`      | 0.50.0    | BSD-3-Clause                            | ASGI toolkit (FastAPI base)     |
| `click`          | 8.3.1     | BSD-3-Clause                            | CLI utilities                   |
| `watchfiles`     | 1.1.1     | MIT                                     | File watching                   |
| `python-dotenv`  | 1.2.1     | BSD-3-Clause                            | Env config                      |
| `certifi`        | 2025.11.12| MPL-2.0                                 | CA bundle                       |
| `idna`           | 3.11      | BSD-3-Clause                            | IDNA handling                   |
| `charset-normalizer` | 3.4.4 | MIT                                     | Encoding detection              |
| `typing-extensions` | 4.15.0 | Python-2.0 / BSD-3-Clause / 0BSD combo  | Typing backports                |
| `pluggy`         | 1.6.0     | MIT                                     | Plugin manager (pytest core)    |
| `packaging`      | 25.0      | Apache-2.0 AND BSD-2-Clause             | Version/marker parsing          |
| `iniconfig`      | 2.3.0     | MIT                                     | INI config helper               |
| `pygments`       | 2.19.2    | BSD-2-Clause                            | Syntax highlighting             |
| `h11`            | 0.16.0    | MIT                                     | HTTP/1.1 protocol               |

*(All appear as `DEPENDS_ON` of the main package in the SPDX relationships.)*

---

### 2.2 Node / TypeScript Tooling

| Package                      | Version       | Notes                                          |
|------------------------------|---------------|-----------------------------------------------|
| `typescript`                 | ^5.6.0        | TS compiler, likely for tools/agents          |
| `zod`                        | ^4.1.12       | Runtime schema validation                      |
| `@types/node`                | ^24.10.1      | Type definitions for Node                      |
| `@modelcontextprotocol/sdk`  | ^1.0.0        | MCP SDK for cross-LLM / tool integration       |

These packages indicate a **TypeScript-based MCP / agent tooling layer** coexisting with the Python service stack.

---

## 3. CI/CD & GitHub Actions as Supply-Chain Components

The SBOM explicitly includes **GitHub Actions** as packages the repo depends on (via `DEPENDS_ON`):

- `anchore/sbom-action@0.*.*` — SBOM generation  
- `apache/skywalking-eyes/header@0.6.0` — license/header enforcement  
- `apisec-inc/apisec-run-scan@…` — API security scans  
- `github/codeql-action/{init,analyze,upload-sarif}@3.* / 4.*` — CodeQL analysis  
- `actions/{checkout,upload-artifact,setup-python,setup-node}@4.*.*` — core actions  
- `softprops/action-gh-release@2.*.*` — GitHub Releases  
- `peter-evans/create-pull-request@6.*.*, 7.*.*` — PR automation  
- `actions/github-script@7.*.*` — scripted automation

This confirms that **security, license compliance and SBOM generation** are already integrated into the CI/CD chain and are now fully traceable from the SPDX document.

---

## 4. Governance Hooks (for LC-04 / ATA 96 / ATA 98)

Recommended front-matter when storing this SPDX file and its wiki summary inside OPT-IN:

```yaml
applicability: [LC-04, LC-06]
axis: N
linked_ata:
  - ATA_95
  - ATA_96
  - ATA_97
  - ATA_98
artefact_type: SBOM
spdx_version: "SPDX-2.3"
source_tooling:
  - protobom
  - github_dependency_graph
  - automatic_dependency_submission
license_declared_project: "Apache-2.0"
sbom_created: "2025-12-03T11:48:52Z"
````

---

## 5. Navigation

* Back to Data/AI/DPP: [[LC-04_Data_AI_DPP_Home]]
* DPP / SBOM integration: [[ATA_96_Digital_Product_Passport]]
* Traceability & audit: [[ATA_98_Traceability_and_Audit]]
* Security & scans: [[AI_ML_Safety_and_Lifecycle_ATA_95-98]]

```
::contentReference[oaicite:0]{index=0}
```
