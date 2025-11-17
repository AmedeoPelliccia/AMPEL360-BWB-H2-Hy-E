# 95-40-00-007 Software Quality and Standards

**ATA Chapter:** 95 – Digital Product Passport Neural Networks  
**Section:** 95-40 – Software  
**Document ID:** 95-40-00-007  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE

---

## 1. Purpose

This document defines the quality standards, processes, and metrics for all software development within ATA 95. It ensures that software meets the highest standards of reliability, safety, security, and maintainability required for aerospace applications.

---

## 2. Applicable Standards

### 2.1 Aviation Standards

| Standard | Title | Applicability |
|----------|-------|---------------|
| DO-178C | Software Considerations in Airborne Systems and Equipment Certification | Safety-critical embedded software |
| DO-330 | Software Tool Qualification Considerations | Development and verification tools |
| DO-200B | Standards for Processing Aeronautical Data | Data quality and integrity |
| DO-278A | Guidelines for Communication, Navigation, Surveillance and Air Traffic Management (CNS/ATM) Systems Software Integrity Assurance | Ground-based CNS systems |

### 2.2 Software Engineering Standards

| Standard | Title | Applicability |
|----------|-------|---------------|
| ISO/IEC 25010:2011 | Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models | Software quality attributes |
| ISO/IEC 27001:2022 | Information security management systems | Security controls |
| ISO/IEC 29119 | Software Testing | Test processes and documentation |
| ISO/IEC 12207 | Systems and software engineering — Software life cycle processes | Development lifecycle |

### 2.3 AI/ML Standards

| Standard | Title | Applicability |
|----------|-------|---------------|
| EASA AI Concept Paper | Guidelines for Level 1 and 2 AI systems in aviation | Neural network certification |
| ISO/IEC 23894:2023 | Information technology — Artificial intelligence — Guidance on risk management | AI risk assessment |
| IEEE P2851 | Standard for Functional Safety Data Format for Exchanging Autonomous System Information | Safety data exchange |

---

## 3. Software Development Lifecycle (SDLC)

### 3.1 Lifecycle Model

We follow a hybrid lifecycle model:
- **Agile/Scrum** for cloud-based services and tools
- **V-Model** for safety-critical embedded software
- **MLOps** for machine learning pipelines

### 3.2 Lifecycle Phases

| Phase | Activities | Deliverables | Review Gate |
|-------|-----------|--------------|-------------|
| **Planning** | Requirements analysis, feasibility, risk assessment | Software Development Plan, Software Quality Assurance Plan | Preliminary Design Review (PDR) |
| **Design** | High-level and detailed design, architecture | Software Design Description, Interface Control Documents | Critical Design Review (CDR) |
| **Implementation** | Coding, unit testing, integration | Source code, unit test reports | Code Review |
| **Verification** | System testing, validation, certification | Test reports, compliance matrices | Test Readiness Review (TRR) |
| **Deployment** | Release, installation, training | Release package, deployment documentation | Release Approval |
| **Maintenance** | Bug fixes, updates, enhancements | Change requests, patch releases | Change Control Board |

---

## 4. Quality Attributes

### 4.1 Functional Quality

| Attribute | Definition | Measurement |
|-----------|------------|-------------|
| **Correctness** | Software behaves according to specification | Requirements coverage, defect density |
| **Completeness** | All specified features implemented | Feature completeness percentage |
| **Traceability** | All requirements traced to implementation and tests | Traceability matrix coverage |

### 4.2 Non-Functional Quality

| Attribute | Target | Measurement Method |
|-----------|--------|-------------------|
| **Reliability** | MTBF > 10,000 hours (critical), > 1,000 hours (non-critical) | Operational metrics, defect tracking |
| **Availability** | 99.99% (critical), 99.9% (high), 99.5% (standard) | Uptime monitoring |
| **Performance** | See latency/throughput targets in 95-40-02-004 | Load testing, profiling |
| **Security** | Zero critical vulnerabilities, < 5 high vulnerabilities | Security scanning, penetration testing |
| **Maintainability** | Cyclomatic complexity < 10, code coverage > 80% | Static analysis, coverage reports |
| **Portability** | Support 3+ platforms (where applicable) | Cross-platform testing |

---

## 5. Code Quality Standards

### 5.1 Coding Standards

| Language | Standard | Tool Enforcement |
|----------|----------|------------------|
| C | MISRA C:2012 (safety-critical), SEI CERT C | Coverity, PC-lint |
| C++ | MISRA C++:2008 (safety-critical), C++ Core Guidelines | Clang-tidy, Coverity |
| Python | PEP 8, Google Python Style Guide | pylint, black, mypy |
| Go | Effective Go, Go Code Review Comments | gofmt, golangci-lint |
| Rust | Rust API Guidelines | rustfmt, clippy |

### 5.2 Code Metrics

| Metric | Target | Critical Threshold |
|--------|--------|-------------------|
| **Cyclomatic Complexity** | ≤ 10 per function | ≤ 15 |
| **Lines of Code per File** | ≤ 500 | ≤ 1000 |
| **Function Length** | ≤ 50 lines | ≤ 100 lines |
| **Comment Density** | 15-25% | < 10% or > 40% |
| **Code Duplication** | < 3% | < 5% |

### 5.3 Code Review

All code changes require:
- Peer review by at least one qualified developer
- Approval from code owner for critical components
- Automated checks (linting, tests, security) must pass
- Safety-critical code requires formal inspection

---

## 6. Testing Standards

### 6.1 Test Levels

| Test Level | Coverage Target | Responsibility |
|------------|----------------|----------------|
| **Unit Testing** | > 80% line coverage, > 70% branch coverage | Developer |
| **Integration Testing** | > 70% integration path coverage | Development team |
| **System Testing** | 100% requirements coverage | QA team |
| **Acceptance Testing** | 100% acceptance criteria | Product owner, stakeholders |
| **Regression Testing** | All tests from previous levels | Automated CI/CD |

### 6.2 Test Types

| Type | Purpose | Frequency |
|------|---------|-----------|
| **Functional** | Verify feature behavior | Every commit |
| **Performance** | Validate latency, throughput | Weekly, before release |
| **Security** | Identify vulnerabilities | Daily (static), weekly (dynamic) |
| **Usability** | Assess user experience | Sprint review |
| **Compatibility** | Cross-platform, cross-browser | Before release |
| **Stress/Load** | System behavior under load | Before major release |

### 6.3 DO-178C Testing (Safety-Critical)

| Software Level | Structural Coverage |
|----------------|---------------------|
| **Level A** | Modified Condition/Decision Coverage (MC/DC) |
| **Level B** | Decision Coverage (DC) |
| **Level C** | Statement Coverage (SC) |
| **Level D** | Minimal structural coverage |

---

## 7. Configuration Management

### 7.1 Version Control

- **Repository:** Git (GitLab, GitHub)
- **Branching Strategy:** GitFlow (main, develop, feature/, release/, hotfix/)
- **Commit Messages:** Conventional Commits format
- **Code Ownership:** CODEOWNERS file in each repository

### 7.2 Versioning Scheme

**Semantic Versioning (SemVer):** MAJOR.MINOR.PATCH

- **MAJOR:** Incompatible API changes
- **MINOR:** Backward-compatible functionality additions
- **PATCH:** Backward-compatible bug fixes

### 7.3 Release Management

| Release Type | Cadence | Approval Required |
|--------------|---------|-------------------|
| **Major** | Annually | Architecture Review Board, Product Owner |
| **Minor** | Quarterly | Product Owner, Tech Lead |
| **Patch** | As needed | Tech Lead |
| **Hotfix** | Emergency | Incident Commander, Product Owner |

---

## 8. Change Control

### 8.1 Change Request Process

1. **Submission:** Change request (CR) created with justification
2. **Impact Analysis:** Technical, schedule, cost, risk assessment
3. **Review:** Change Control Board (CCB) evaluates CR
4. **Approval:** CCB approves/rejects/defers CR
5. **Implementation:** Approved changes implemented and tested
6. **Verification:** Changes verified against acceptance criteria
7. **Closure:** CR closed with traceability to commits

### 8.2 Change Control Board (CCB)

**Members:**
- Chief Software Architect (Chair)
- Product Owner
- Safety Engineer (for safety-critical changes)
- Security Architect (for security changes)
- QA Lead
- Configuration Manager

**Meeting Frequency:** Bi-weekly or as needed

---

## 9. Defect Management

### 9.1 Defect Severity

| Severity | Definition | Response Time | Fix Time (Target) |
|----------|------------|---------------|-------------------|
| **Critical** | System down, safety impact, data loss | 1 hour | 24 hours |
| **High** | Major feature broken, workaround exists | 4 hours | 1 week |
| **Medium** | Minor feature broken, usability issue | 1 day | 2 weeks |
| **Low** | Cosmetic issue, enhancement request | 1 week | Next release |

### 9.2 Defect Tracking

- **Tool:** Jira, GitLab Issues
- **Workflow:** Open → In Progress → Code Review → Testing → Closed
- **Metrics:** Defect density, mean time to resolution, escaped defects

---

## 10. Documentation Standards

### 10.1 Required Documentation

| Document | Purpose | Update Frequency |
|----------|---------|------------------|
| **Software Requirements Specification (SRS)** | Functional and non-functional requirements | With each major release |
| **Software Design Description (SDD)** | Architecture and detailed design | With significant design changes |
| **Software Test Plan (STP)** | Test strategy and approach | Annually |
| **Software Test Report (STR)** | Test execution results | After each test cycle |
| **User Manual** | End-user documentation | With each release |
| **API Documentation** | Interface specifications | With each API change |

### 10.2 Documentation Format

- **Markdown** for version-controlled docs
- **OpenAPI/Swagger** for REST APIs
- **Protocol Buffers** for gRPC APIs
- **Doxygen/Sphinx** for code documentation
- **Draw.io/Mermaid** for diagrams

---

## 11. Security Standards

### 11.1 Secure Development Lifecycle (SDL)

| Phase | Security Activities |
|-------|---------------------|
| **Requirements** | Threat modeling, security requirements |
| **Design** | Security architecture review, attack surface analysis |
| **Implementation** | Secure coding practices, static analysis |
| **Verification** | Security testing, penetration testing |
| **Deployment** | Security hardening, secrets management |
| **Operations** | Monitoring, incident response, patching |

### 11.2 Security Controls

- **SAST:** Static Application Security Testing on every commit
- **DAST:** Dynamic Application Security Testing weekly
- **SCA:** Software Composition Analysis for dependencies
- **Secrets Scanning:** No secrets in code repositories
- **Penetration Testing:** Annually by third-party

---

## 12. Continuous Integration/Continuous Deployment (CI/CD)

### 12.1 CI Pipeline

| Stage | Activities | Gate Criteria |
|-------|-----------|---------------|
| **Build** | Compile, lint, format check | Zero errors |
| **Test** | Unit tests, integration tests | > 80% coverage, all tests pass |
| **Analyze** | Static analysis, code quality | No critical issues |
| **Security** | Dependency scan, SAST | No critical vulnerabilities |
| **Package** | Container build, artifact creation | Successful build |

### 12.2 CD Pipeline

| Environment | Deployment Trigger | Approval |
|-------------|-------------------|----------|
| **Development** | Every commit to develop | Automatic |
| **Staging** | Every commit to main | Automatic |
| **Production** | Release tag | Manual (Product Owner) |

---

## 13. Quality Metrics and KPIs

### 13.1 Process Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Code Review Turnaround** | < 24 hours | Median time from PR creation to approval |
| **Build Success Rate** | > 95% | Successful builds / total builds |
| **Test Pass Rate** | > 98% | Passing tests / total tests |
| **Deployment Frequency** | 1/week (non-critical), 1/month (critical) | Deployments per time period |
| **Mean Time to Restore (MTTR)** | < 4 hours | Time from incident detection to resolution |

### 13.2 Product Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Defect Density** | < 5 defects / 1K LOC | Total defects / lines of code |
| **Escaped Defect Rate** | < 2% | Production defects / total defects |
| **Technical Debt Ratio** | < 5% | Remediation cost / development cost |
| **API Response Time (p95)** | < 200ms | 95th percentile latency |
| **System Uptime** | > 99.9% | Available time / total time |

---

## 14. Audits and Compliance

### 14.1 Internal Audits

- **Frequency:** Quarterly
- **Scope:** Code quality, process adherence, documentation
- **Conducted By:** QA team, independent reviewer

### 14.2 External Audits

- **Certification Audits:** As required for DO-178C certification
- **Security Audits:** Annually by third-party
- **Compliance Audits:** As required by regulatory bodies

---

## 15. Training and Competency

### 15.1 Required Training

| Role | Training |
|------|----------|
| **All Developers** | Secure coding, Git/CI/CD, company standards |
| **Safety-Critical Developers** | DO-178C, MISRA C/C++, formal methods |
| **ML Engineers** | Responsible AI, model validation, MLOps |
| **Security Engineers** | OWASP Top 10, penetration testing, threat modeling |

### 15.2 Competency Assessment

- Annual skills assessment for all developers
- Certification required for safety-critical development (e.g., CAST-certified)
- Continuing education: 40 hours/year

---

## 16. References

### 16.1 Internal References

- [95-40-00-001 Software Overview](../95-40-00-001_Software_Overview.md)
- [95-40-00-004 Software Taxonomy](95-40-00-004_Software_Taxonomy.md)
- [95-00-07 V&V](../../95-00_GENERAL/95-00-07_V_AND_V/)

### 16.2 External Standards

- DO-178C: Software Considerations in Airborne Systems and Equipment Certification
- ISO/IEC 25010: Systems and software quality models
- MISRA C:2012 and MISRA C++:2008

---

## 17. Document Control

- **Owner:** Chief Quality Officer
- **Approver:** VP of Engineering
- **Review Cycle:** Annually
- **Next Review:** 2026-11-17

---

**END OF DOCUMENT**
