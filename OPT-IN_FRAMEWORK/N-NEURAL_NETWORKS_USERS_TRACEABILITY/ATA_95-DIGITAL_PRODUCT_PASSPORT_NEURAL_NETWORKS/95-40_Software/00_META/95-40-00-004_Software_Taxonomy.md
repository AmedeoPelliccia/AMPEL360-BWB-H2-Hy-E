# 95-40-00-004 Software Taxonomy

**ATA Chapter:** 95 – Digital Product Passport Neural Networks  
**Section:** 95-40 – Software  
**Document ID:** 95-40-00-004  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE

---

## 1. Purpose

This document provides a comprehensive taxonomy of all software technologies, frameworks, libraries, and tools used across the AMPEL360 Neural Network and Digital Product Passport systems. It serves as the authoritative reference for technology decisions and standardization.

---

## 2. Programming Languages

### 2.1 Primary Languages

| Language | Version | Use Cases | Certification | Status |
|----------|---------|-----------|---------------|--------|
| Python | 3.11+ | ML pipelines, data processing, APIs, scripting | N/A | ADOPT |
| C | C11 | Safety-critical embedded code, drivers | DO-178C Level A/B | ADOPT |
| C++ | C++17 | High-performance embedded code, inference engines | DO-178C Level B/C | ADOPT |
| Rust | 1.70+ | Security-critical services, blockchain clients | N/A | ADOPT |
| Go | 1.21+ | Cloud services, CLI tools, orchestration | N/A | ADOPT |

### 2.2 Secondary Languages

| Language | Version | Use Cases | Status |
|----------|---------|-----------|--------|
| TypeScript | 5.0+ | Web UIs, Node.js services | ADOPT |
| JavaScript | ES2022+ | Frontend, scripting | ADOPT |
| SQL | ANSI SQL | Database queries and schemas | ADOPT |
| Bash | 4.4+ | Shell scripts, automation | ADOPT |
| YAML | 1.2 | Configuration, CI/CD pipelines | ADOPT |

---

## 3. Machine Learning and AI

### 3.1 ML Frameworks

| Framework | Version | Purpose | Environment | Status |
|-----------|---------|---------|-------------|--------|
| TensorFlow | 2.14+ | Model training, serving | Ground | ADOPT |
| PyTorch | 2.1+ | Research, model development | Ground | ADOPT |
| ONNX Runtime | 1.16+ | Cross-platform inference | Ground/Embedded | ADOPT |
| TensorRT | 8.6+ | GPU-accelerated inference | Ground/Edge | ADOPT |
| scikit-learn | 1.3+ | Classical ML, preprocessing | Ground | ADOPT |

### 3.2 ML Operations

| Tool | Version | Purpose | Status |
|------|---------|---------|--------|
| MLflow | 2.8+ | Experiment tracking, model registry | ADOPT |
| Apache Airflow | 2.7+ | Pipeline orchestration | ADOPT |
| Kubeflow | 1.8+ | ML workflows on Kubernetes | TRIAL |
| DVC | 3.30+ | Data version control | ADOPT |
| Feast | 0.35+ | Feature store | TRIAL |
| Weights & Biases | Latest | Experiment tracking (alternative) | ASSESS |

---

## 4. Cloud and Infrastructure

### 4.1 Container and Orchestration

| Technology | Version | Purpose | Status |
|------------|---------|---------|--------|
| Docker | 24+ | Container runtime | ADOPT |
| Kubernetes | 1.28+ | Container orchestration | ADOPT |
| Helm | 3.13+ | Kubernetes package management | ADOPT |
| Istio | 1.20+ | Service mesh | ADOPT |
| containerd | 1.7+ | Container runtime (alternative) | ADOPT |

### 4.2 Infrastructure as Code

| Tool | Version | Purpose | Status |
|------|---------|---------|--------|
| Terraform | 1.6+ | Multi-cloud provisioning | ADOPT |
| Ansible | 2.15+ | Configuration management | ADOPT |
| Pulumi | 3.90+ | Infrastructure as code (alternative) | ASSESS |
| ArgoCD | 2.9+ | GitOps continuous delivery | ADOPT |

### 4.3 Cloud Providers

| Provider | Services Used | Status |
|----------|---------------|--------|
| AWS | EKS, S3, RDS, Lambda, SageMaker | ADOPT |
| Azure | AKS, Blob Storage, CosmosDB, ML | TRIAL |
| GCP | GKE, Cloud Storage, BigQuery, Vertex AI | TRIAL |

---

## 5. Databases and Storage

### 5.1 Relational Databases

| Database | Version | Purpose | Status |
|----------|---------|---------|--------|
| PostgreSQL | 16+ | Primary relational DB | ADOPT |
| MySQL | 8.0+ | Legacy integrations | HOLD |
| SQLite | 3.43+ | Embedded, testing | ADOPT |

### 5.2 NoSQL Databases

| Database | Version | Purpose | Status |
|----------|---------|---------|--------|
| Redis | 7.2+ | Caching, session store | ADOPT |
| MongoDB | 7.0+ | Document store | TRIAL |
| Cassandra | 4.1+ | Distributed data | ASSESS |

### 5.3 Time-Series and Analytics

| Database | Version | Purpose | Status |
|----------|---------|---------|--------|
| InfluxDB | 2.7+ | Time-series metrics | ADOPT |
| Prometheus | 2.48+ | Metrics collection | ADOPT |
| ClickHouse | 23.10+ | Analytics queries | TRIAL |

### 5.4 Object Storage

| Storage | Purpose | Status |
|---------|---------|--------|
| S3 (AWS) | Primary object storage | ADOPT |
| MinIO | Self-hosted S3-compatible | ADOPT |
| Azure Blob | Azure deployments | TRIAL |

---

## 6. APIs and Integration

### 6.1 API Frameworks

| Framework | Language | Purpose | Status |
|-----------|----------|---------|--------|
| FastAPI | Python | REST APIs, async | ADOPT |
| Flask | Python | Simple REST APIs | ADOPT |
| gRPC | Multiple | High-performance RPC | ADOPT |
| GraphQL | Multiple | Flexible queries | TRIAL |

### 6.2 API Documentation

| Tool | Purpose | Status |
|------|---------|--------|
| OpenAPI/Swagger | REST API specs | ADOPT |
| Redoc | API documentation | ADOPT |
| Postman | API testing | ADOPT |

### 6.3 Message Brokers

| Broker | Version | Purpose | Status |
|--------|---------|---------|--------|
| Apache Kafka | 3.6+ | Event streaming | ADOPT |
| RabbitMQ | 3.12+ | Message queue | TRIAL |
| NATS | 2.10+ | Lightweight messaging | ASSESS |

---

## 7. Blockchain and DPP

### 7.1 Blockchain Platforms

| Platform | Version | Purpose | Status |
|----------|---------|---------|--------|
| Hyperledger Fabric | 2.5+ | Permissioned blockchain | ADOPT |
| Ethereum | Mainnet | Public blockchain (if needed) | ASSESS |
| Polygon | Mainnet | Layer 2 solution | ASSESS |

### 7.2 Smart Contract Languages

| Language | Platform | Status |
|----------|----------|--------|
| Chaincode (Go) | Hyperledger Fabric | ADOPT |
| Solidity | Ethereum | ASSESS |

### 7.3 Blockchain Tools

| Tool | Purpose | Status |
|------|---------|--------|
| Hyperledger Explorer | Blockchain browser | ADOPT |
| Caliper | Performance benchmarking | TRIAL |
| web3.js | Ethereum interaction | ASSESS |

---

## 8. Embedded and Real-Time

### 8.1 Real-Time Operating Systems

| RTOS | Version | Certification | Status |
|------|---------|---------------|--------|
| VxWorks 653 | 7.x | DO-178C Level A | ADOPT |
| PikeOS | 5.x | DO-178C Level A | TRIAL |
| FreeRTOS | 10.5+ | None | HOLD (non-critical only) |

### 8.2 Communication Protocols

| Protocol | Standard | Purpose | Status |
|----------|----------|---------|--------|
| ARINC 653 | APEX | Partition management | ADOPT |
| ARINC 664 | AFDX | Avionics network | ADOPT |
| ARINC 429 | Legacy | Legacy avionics | ADOPT |
| CAN Bus | ISO 11898 | Vehicle bus | ADOPT |
| Ethernet | IEEE 802.3 | General networking | ADOPT |

### 8.3 Embedded Libraries

| Library | Purpose | Status |
|---------|---------|--------|
| FlatBuffers | Efficient serialization | ADOPT |
| Protocol Buffers | Serialization (non-embedded) | ADOPT |
| Eigen | Linear algebra | ADOPT |
| CMSIS | ARM Cortex-M support | TRIAL |

---

## 9. Testing and Quality

### 9.1 Testing Frameworks

| Framework | Language | Purpose | Status |
|-----------|----------|---------|--------|
| pytest | Python | Unit/integration tests | ADOPT |
| unittest | Python | Standard library testing | ADOPT |
| Google Test | C++ | Unit tests | ADOPT |
| Robot Framework | Multiple | Acceptance testing | ADOPT |
| JUnit | Java | Unit tests | ADOPT |

### 9.2 Code Quality Tools

| Tool | Purpose | Status |
|------|---------|--------|
| pylint | Python linting | ADOPT |
| black | Python code formatting | ADOPT |
| mypy | Python type checking | ADOPT |
| clang-tidy | C/C++ linting | ADOPT |
| SonarQube | Code quality analysis | ADOPT |
| Coverity | Static analysis (DO-178C) | ADOPT |

### 9.3 Load and Performance Testing

| Tool | Purpose | Status |
|------|---------|--------|
| Locust | Load testing | ADOPT |
| JMeter | Performance testing | ADOPT |
| k6 | Modern load testing | TRIAL |

---

## 10. CI/CD and DevOps

### 10.1 CI/CD Platforms

| Platform | Purpose | Status |
|----------|---------|--------|
| GitLab CI/CD | Primary CI/CD | ADOPT |
| Jenkins | Build automation | ADOPT |
| GitHub Actions | Open source CI/CD | TRIAL |
| CircleCI | Alternative CI/CD | ASSESS |

### 10.2 Version Control

| Tool | Purpose | Status |
|------|---------|--------|
| Git | Source control | ADOPT |
| Git LFS | Large file storage | ADOPT |
| GitLab | Code hosting, CI/CD | ADOPT |
| GitHub | Open source projects | ADOPT |

---

## 11. Monitoring and Observability

### 11.1 Metrics

| Tool | Purpose | Status |
|------|---------|--------|
| Prometheus | Metrics collection | ADOPT |
| Grafana | Metrics visualization | ADOPT |
| Datadog | APM (alternative) | ASSESS |

### 11.2 Logging

| Tool | Purpose | Status |
|------|---------|--------|
| Elasticsearch | Log storage and search | ADOPT |
| Logstash | Log processing | ADOPT |
| Kibana | Log visualization | ADOPT |
| Fluentd | Log forwarding | ADOPT |

### 11.3 Tracing

| Tool | Purpose | Status |
|------|---------|--------|
| Jaeger | Distributed tracing | ADOPT |
| Zipkin | Alternative tracing | TRIAL |
| OpenTelemetry | Observability standard | ADOPT |

---

## 12. Security

### 12.1 Authentication and Authorization

| Tool | Purpose | Status |
|------|---------|--------|
| Keycloak | Identity and access mgmt | ADOPT |
| OAuth2/OIDC | Auth protocols | ADOPT |
| LDAP/AD | Enterprise identity | ADOPT |

### 12.2 Secret Management

| Tool | Purpose | Status |
|------|---------|--------|
| HashiCorp Vault | Secret storage | ADOPT |
| AWS Secrets Manager | Cloud secrets | ADOPT |
| Sealed Secrets | Kubernetes secrets | ADOPT |

### 12.3 Security Scanning

| Tool | Purpose | Status |
|------|---------|--------|
| Trivy | Container scanning | ADOPT |
| Snyk | Dependency scanning | ADOPT |
| OWASP ZAP | Web security testing | ADOPT |
| Falco | Runtime security | TRIAL |

---

## 13. Documentation

### 13.1 Documentation Tools

| Tool | Purpose | Status |
|------|---------|--------|
| Markdown | Lightweight markup | ADOPT |
| Sphinx | Python documentation | ADOPT |
| Doxygen | C/C++ documentation | ADOPT |
| MkDocs | Static site generator | ADOPT |
| Mermaid | Diagrams as code | ADOPT |

### 13.2 Diagram Tools

| Tool | Purpose | Status |
|------|---------|--------|
| Draw.io | General diagrams | ADOPT |
| PlantUML | UML diagrams as code | ADOPT |
| Lucidchart | Collaborative diagrams | TRIAL |

---

## 14. Technology Radar Status Definitions

| Status | Definition |
|--------|------------|
| **ADOPT** | Proven technology, production-ready, recommended for use |
| **TRIAL** | Promising technology, approved for pilot projects |
| **ASSESS** | Interesting technology, evaluate but don't commit yet |
| **HOLD** | Avoid for new projects, phase out if currently used |

---

## 15. References

### 15.1 Internal References

- [95-40-00-001 Software Overview](../95-40-00-001_Software_Overview.md)
- [95-40-00-002 Software Architecture and Scope](../95-40-00-002_Software_Architecture_and_Scope.md)

### 15.2 External Standards

- DO-178C (Software Considerations in Airborne Systems)
- DO-330 (Software Tool Qualification)
- ARINC 653 (Avionics Application Software Standard Interface)

---

## 16. Document Control

- **Owner:** Chief Technology Officer
- **Approver:** Technical Director
- **Review Cycle:** Quarterly
- **Next Review:** 2026-02-17

---

**END OF DOCUMENT**
