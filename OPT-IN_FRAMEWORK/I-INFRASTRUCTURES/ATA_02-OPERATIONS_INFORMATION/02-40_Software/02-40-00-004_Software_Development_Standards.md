# 02-40-00-004 – Software Development Standards

## Purpose

This document establishes the coding standards, branching model, code review rules, and general Software Development Life Cycle (SDLC) guidelines for all software development activities within the 02-40 Software scope of the AMPEL360 project.

---

## 1. Scope and Applicability

These standards apply to all software developed, maintained, or integrated within:

- **02-40-01** Core Applications
- **02-40-11** EFB Software  
- **02-40-12** Backend Services
- **02-40-13** Performance Calculator
- **02-40-14** Weight & Balance System
- **02-40-15** Flight Planning Software
- **02-40-16** Dispatch Interface
- **02-40-17** Weather Data Processor
- **02-40-18** Data Recording Service
- **02-40-19** Analytics Engine
- **02-40-21** H₂ Operations Software
- **02-40-23** Predictive Ops Software

---

## 2. Programming Languages and Frameworks

### 2.1 Language-Specific Standards

#### Swift/SwiftUI (iOS EFB Applications)
- **Standard**: [Swift API Design Guidelines](https://swift.org/documentation/api-design-guidelines/)
- **Style Guide**: [Ray Wenderlich Swift Style Guide](https://github.com/raywenderlich/swift-style-guide)
- **Version**: Swift 5.9+, SwiftUI 5.0+
- **Minimum iOS Target**: iOS 16.0
- **Key Principles**:
  - Use `struct` for value types, `class` for reference types
  - Leverage SwiftUI's declarative syntax
  - Implement offline-first data persistence
  - Use Combine for reactive programming

#### Python (ML/Data Processing/Analytics)
- **Standard**: [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- **Docstrings**: [PEP 257 – Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- **Type Hints**: [PEP 484 – Type Hints](https://www.python.org/dev/peps/pep-0484/)
- **Version**: Python 3.11+
- **Key Tools**:
  - `black` for code formatting
  - `pylint` and `flake8` for linting
  - `mypy` for static type checking
  - `pytest` for testing

#### Go (High-Performance Backend Services)
- **Standard**: [Effective Go](https://golang.org/doc/effective_go.html)
- **Style Guide**: [Uber Go Style Guide](https://github.com/uber-go/guide/blob/master/style.md)
- **Version**: Go 1.21+
- **Key Principles**:
  - Prefer simplicity and readability
  - Use interfaces for abstraction
  - Handle errors explicitly
  - Leverage goroutines and channels for concurrency

#### TypeScript/Node.js (Web Applications, Integration Services)
- **Standard**: [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- **Style Guide**: [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- **Version**: TypeScript 5.0+, Node.js 20 LTS
- **Key Tools**:
  - `eslint` with TypeScript plugin
  - `prettier` for code formatting
  - `jest` for testing

#### C++ (Performance-Critical Calculations)
- **Standard**: C++17 or C++20
- **Style Guide**: [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)
- **Key Principles**:
  - Use modern C++ features (smart pointers, lambdas, `constexpr`)
  - RAII for resource management
  - Minimize use of raw pointers
  - Extensive unit testing for numerical accuracy

---

## 3. Code Quality Standards

### 3.1 Code Coverage

| Component Type | Minimum Coverage | Target Coverage |
|----------------|------------------|-----------------|
| Safety-critical (DO-178C Level C) | 100% (MC/DC) | 100% (MC/DC) |
| Business-critical | 80% | 90% |
| Non-critical utilities | 60% | 75% |

**Note**: Safety-critical software must achieve 100% Modified Condition/Decision Coverage (MC/DC) as required by [DO-178C](https://www.rtca.org/content/standards-guidance-materials).

### 3.2 Code Complexity

- **Cyclomatic Complexity**: Maximum 10 per function/method
- **Function Length**: Maximum 50 lines (excluding comments/whitespace)
- **File Length**: Maximum 500 lines (consider refactoring into multiple files)
- **Parameter Count**: Maximum 5 parameters per function

### 3.3 Documentation

#### Code Comments
- Use comments to explain **why**, not **what** (code should be self-explanatory)
- Update comments when code changes
- Avoid obvious comments (e.g., `i++; // increment i`)

#### API Documentation
- All public APIs must have complete documentation
- Use language-native doc formats:
  - Swift: DocC comments
  - Python: Docstrings (Google/NumPy style)
  - Go: GoDoc comments
  - TypeScript: JSDoc/TSDoc comments
  - C++: Doxygen comments

#### Architecture Documentation
- Maintain up-to-date architecture diagrams (see [AMPEL360_ASSETS_STANDARD.md](../../../../AMPEL360_ASSETS_STANDARD.md))
- Document design decisions in Architecture Decision Records (ADRs)
- Keep README files current in each module/service directory

---

## 4. Version Control and Branching Strategy

### 4.1 Git Workflow

We use a **trunk-based development** approach with short-lived feature branches.

```
main (protected)
  ├── feature/EFB-123-performance-calc
  ├── feature/EFB-456-weather-display
  ├── hotfix/PROD-789-acars-timeout
  └── release/v2.3.0
```

### 4.2 Branch Naming Convention

- **Feature branches**: `feature/<TICKET-ID>-<short-description>`
- **Bug fix branches**: `bugfix/<TICKET-ID>-<short-description>`
- **Hotfix branches**: `hotfix/<TICKET-ID>-<short-description>`
- **Release branches**: `release/v<MAJOR>.<MINOR>.<PATCH>`

**Examples**:
- `feature/EFB-123-add-h2-fuel-gauge`
- `bugfix/API-456-fix-token-refresh`
- `hotfix/PROD-789-acars-connection-leak`
- `release/v2.3.0`

### 4.3 Commit Message Convention

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring (no functional change)
- `perf`: Performance improvement
- `test`: Adding or updating tests
- `chore`: Build process, tooling, dependencies

**Example**:
```
feat(efb): add H2 fuel quantity display

Implement real-time H2 fuel quantity gauge in EFB performance page.
Integrates with ATA 28 fuel system via AFDX data bus.

Closes EFB-123
```

### 4.4 Branch Protection Rules

For `main` branch:
- Require pull request reviews (minimum 2 approvals for safety-critical code)
- Require status checks to pass:
  - Unit tests
  - Integration tests
  - Code coverage (must meet minimums)
  - Security scanning
  - Linting
- Prohibit force push
- Require signed commits (GPG)

---

## 5. Code Review Process

### 5.1 Review Requirements

All code changes must be reviewed before merging to `main`.

| Code Type | Required Reviewers | Approval Count |
|-----------|-------------------|----------------|
| Safety-critical (DO-178C) | Certified reviewers + QA | 3 |
| Business-critical | Senior engineers | 2 |
| Non-critical | Any team member | 1 |

### 5.2 Review Checklist

Reviewers must verify:

- [ ] **Functionality**: Code achieves stated objectives
- [ ] **Tests**: Adequate test coverage, tests pass
- [ ] **Code Quality**: Follows coding standards, complexity limits
- [ ] **Security**: No security vulnerabilities introduced
- [ ] **Performance**: No performance regressions
- [ ] **Documentation**: Code and API documentation updated
- [ ] **Error Handling**: Proper error handling and logging
- [ ] **Dependencies**: No unnecessary dependencies added
- [ ] **Traceability**: Linked to requirements/issues

### 5.3 Review Turnaround Time

- **Target**: Within 24 hours for non-urgent changes
- **Hotfixes**: Within 4 hours
- **Safety-critical**: Within 48 hours (due to additional scrutiny)

### 5.4 Addressing Review Comments

- Author must respond to all review comments
- Use "resolved" threads to indicate addressed comments
- Request re-review after addressing significant comments

---

## 6. Testing Strategy

### 6.1 Test Pyramid

```
        /\
       /  \      E2E Tests (10%)
      /    \
     /------\    Integration Tests (20%)
    /        \
   /----------\  Unit Tests (70%)
```

### 6.2 Unit Testing

- **Framework**: 
  - Swift: XCTest
  - Python: pytest
  - Go: testing package + testify
  - TypeScript: Jest
  - C++: Google Test

- **Principles**:
  - Fast (<1s per test)
  - Isolated (no external dependencies)
  - Deterministic (same result every time)
  - Use mocks/stubs for dependencies

### 6.3 Integration Testing

- Test interactions between modules/services
- Use test containers for databases and message queues
- Verify API contracts (e.g., with Pact)

### 6.4 End-to-End Testing

- Automate critical user journeys
- Run in staging environment
- Include performance/load testing

### 6.5 Test Data Management

- Use synthetic test data (never production data)
- Maintain test data fixtures in version control
- Use data factories/builders for test setup

---

## 7. Continuous Integration/Continuous Deployment (CI/CD)

### 7.1 CI Pipeline

Every pull request triggers:

1. **Linting**: Check code style compliance
2. **Unit Tests**: Run all unit tests
3. **Security Scan**: Dependency vulnerability scan (Snyk, GitHub Advanced Security)
4. **Code Coverage**: Verify coverage thresholds met
5. **Integration Tests**: Test service integrations
6. **Build**: Compile/package application
7. **Artifact Upload**: Upload build artifacts

### 7.2 CD Pipeline

Merges to `main` branch trigger:

1. **Full Test Suite**: Run all tests (unit, integration, E2E)
2. **Security Scan**: Deep security analysis (SAST, DAST)
3. **Build & Package**: Create deployable artifacts
4. **Deploy to Dev**: Automatic deployment to development environment
5. **Smoke Tests**: Run basic health checks
6. **Deploy to Staging**: Automatic deployment to staging (for release branches)
7. **Deploy to Production**: Manual approval + deployment (blue-green/canary)

### 7.3 Deployment Strategies

- **Development**: Continuous deployment on every merge
- **Staging**: Continuous deployment from release branches
- **Production**: 
  - Blue-Green deployment for zero downtime
  - Canary releases (5% → 25% → 50% → 100%)
  - Automated rollback on error rate threshold

---

## 8. Security Standards

### 8.1 Secure Coding Practices

- **Input Validation**: Validate all external inputs
- **Output Encoding**: Encode data before rendering (prevent XSS)
- **SQL Injection Prevention**: Use parameterized queries/ORMs
- **Authentication**: Use OAuth2 + JWT, never store passwords in plain text
- **Authorization**: Implement least privilege principle
- **Secrets Management**: Use secret management tools (AWS Secrets Manager, HashiCorp Vault)
- **Cryptography**: Use well-established libraries (do not roll your own crypto)

### 8.2 Dependency Management

- Keep dependencies up to date
- Use dependency scanning tools (Dependabot, Renovate)
- Review security advisories for critical dependencies
- Pin dependency versions in production

### 8.3 Security Testing

- **Static Analysis (SAST)**: Integrated into CI pipeline (SonarQube, Semgrep)
- **Dynamic Analysis (DAST)**: Scan running applications (OWASP ZAP)
- **Dependency Scanning**: Check for known vulnerabilities (Snyk, GitHub Advanced Security)
- **Penetration Testing**: Annual third-party penetration testing

---

## 9. Performance Standards

### 9.1 Performance Targets

| Metric | Target | Critical Threshold |
|--------|--------|-------------------|
| API Response Time (P95) | <200ms | <500ms |
| API Response Time (P99) | <500ms | <1s |
| Database Query Time | <50ms | <100ms |
| Page Load Time | <2s | <3s |
| EFB Calculation Time | <100ms | <200ms |

### 9.2 Performance Testing

- **Load Testing**: Simulate expected traffic (JMeter, Gatling)
- **Stress Testing**: Find breaking points
- **Spike Testing**: Sudden traffic increases
- **Endurance Testing**: Sustained load over time

### 9.3 Profiling and Optimization

- Profile code before optimizing (don't guess)
- Focus on hot paths and bottlenecks
- Use language-specific profiling tools:
  - Swift: Instruments
  - Python: cProfile, py-spy
  - Go: pprof
  - TypeScript/Node: Node.js Inspector

---

## 10. Certification and Compliance

### 10.1 DO-178C Compliance (EFB, Performance Calculator, W&B)

Safety-critical software follows [DO-178C](https://www.rtca.org/content/standards-guidance-materials) processes:

- **Planning**: Software Development Plan, Software Verification Plan, Software Configuration Management Plan, Software Quality Assurance Plan
- **Development**: Requirements, design, coding, integration per DO-178C standards
- **Verification**: Reviews, analysis, testing to achieve MC/DC coverage
- **Configuration Management**: Traceability, change control, version control
- **Quality Assurance**: Independent verification, audits, process compliance

**Certification Levels**:
- EFB Software: Level C or D (depending on functionality)
- Performance Calculator: Level C
- Weight & Balance: Level C

### 10.2 EU AI Act Compliance

For AI/ML components (see [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)):

- Risk assessment and classification
- Data governance and quality
- Model transparency and explainability
- Human oversight requirements
- Robustness and accuracy testing

---

## 11. Documentation Requirements

### 11.1 Required Documentation

Every software component must include:

1. **README.md**: Overview, setup instructions, usage examples
2. **ARCHITECTURE.md**: High-level design, key components, data flows
3. **API.md** or **OpenAPI spec**: API documentation
4. **CHANGELOG.md**: Version history, changes per release
5. **CONTRIBUTING.md**: How to contribute, development setup
6. **LICENSE**: Software license (if open source or shared)

### 11.2 Architecture Decision Records (ADRs)

Document significant architectural decisions:

```markdown
# ADR-001: Use GraphQL for Data Service API

## Status
Accepted

## Context
Need flexible query capability for EFB and web clients with varying data needs.

## Decision
Implement GraphQL API alongside REST endpoints.

## Consequences
- Positive: Clients can request exactly the data they need
- Negative: Additional complexity in backend implementation
- Mitigation: Provide REST fallback for simple queries
```

Store ADRs in `/docs/adr/` directory.

---

## 12. Monitoring and Observability

### 12.1 Logging Standards

- Use structured logging (JSON format)
- Include contextual information (request ID, user ID, trace ID)
- Log levels:
  - DEBUG: Detailed diagnostic information
  - INFO: General operational information
  - WARN: Warning messages (potential issues)
  - ERROR: Error events (need attention)
  - FATAL: Critical errors (system failure)

### 12.2 Metrics

Collect RED metrics for all services:
- **Rate**: Requests per second
- **Errors**: Error rate (%)
- **Duration**: Latency (P50, P95, P99)

### 12.3 Tracing

- Implement distributed tracing (OpenTelemetry)
- Propagate trace context across service boundaries
- Sample 1% in production, 100% in dev/staging

---

## 13. Dependency and License Management

### 13.1 Approved Licenses

Software dependencies must use approved open-source licenses:
- **Permissive**: MIT, Apache 2.0, BSD
- **Copyleft** (case-by-case): GPL, LGPL (requires legal review)
- **Prohibited**: AGPL, proprietary without commercial license

### 13.2 Dependency Approval Process

1. Developer identifies need for new dependency
2. Check license compatibility
3. Evaluate security posture (known vulnerabilities, maintenance activity)
4. Get approval from tech lead
5. Document in `THIRD_PARTY_NOTICES.md`

---

## 14. Configuration Management

### 14.1 Configuration-as-Code

- Store configuration in version control
- Use environment variables for secrets (injected at runtime)
- Separate configuration per environment (dev, staging, prod)

### 14.2 Feature Flags

- Use feature flags for gradual rollout
- Decouple deployment from release
- Tools: LaunchDarkly, Unleash, or custom solution

---

## 15. Incident Response

### 15.1 Severity Levels

| Severity | Description | Response Time |
|----------|-------------|---------------|
| P0 (Critical) | Complete service outage, safety impact | Immediate |
| P1 (High) | Major functionality broken, multiple users affected | <1 hour |
| P2 (Medium) | Significant functionality degraded, workaround exists | <4 hours |
| P3 (Low) | Minor issues, few users affected | <1 business day |

### 15.2 Post-Incident Review

After P0/P1 incidents:
- Conduct blameless post-mortem
- Document root cause, timeline, impact
- Identify action items to prevent recurrence
- Share learnings with team

---

## 16. Training and Onboarding

### 16.1 Developer Onboarding

New developers must complete:
- Code of Conduct training
- Security awareness training
- Language-specific coding standards training
- DO-178C training (for safety-critical work)

### 16.2 Continuous Learning

- Encourage participation in conferences, workshops
- Provide access to online learning platforms
- Host internal knowledge-sharing sessions (lunch & learn)

---

## 17. References

### Standards and Guidelines

- [Swift API Design Guidelines](https://swift.org/documentation/api-design-guidelines/)
- [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Effective Go](https://golang.org/doc/effective_go.html)
- [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [DO-178C](https://www.rtca.org/content/standards-guidance-materials) – Software Considerations in Airborne Systems
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)

### Internal Documentation

- [02-40-00-001 Software Architecture Overview](02-40-00-001_Software_Architecture_Overview.md)
- [02-40-00-002 Software Integration Map](02-40-00-002_Software_Integration_Map.md)
- [02-40-00-003 API Catalog](02-40-00-003_API_Catalog.yaml)
- [AMPEL360_DOCUMENTATION_STANDARD.md](../../../../AMPEL360_DOCUMENTATION_STANDARD.md)

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: _2025-11-21_.

---

**End of Document**
