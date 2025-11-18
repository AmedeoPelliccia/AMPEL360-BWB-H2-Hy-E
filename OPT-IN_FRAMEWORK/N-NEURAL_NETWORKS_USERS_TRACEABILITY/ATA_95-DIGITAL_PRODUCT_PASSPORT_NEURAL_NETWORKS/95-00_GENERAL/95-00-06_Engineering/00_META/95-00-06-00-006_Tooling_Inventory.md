# 95-00-06-00-006: Tooling Inventory

## Document Information
- **Document ID**: 95-00-06-00-006
- **Title**: Engineering Tooling Inventory
- **Version**: 1.0
- **Date**: 2025-11-17
- **Status**: Active

## Purpose

This document provides a comprehensive inventory of all software tools, platforms, and frameworks used in ATA 95 engineering activities.

## ML/AI Engineering Tools

### Model Development Frameworks

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **PyTorch** | 2.1.0 | Deep learning framework | BSD | ML Team | ✅ Active |
| **TensorFlow** | 2.14.0 | Deep learning framework | Apache 2.0 | ML Team | ✅ Active |
| **JAX** | 0.4.20 | High-performance ML | Apache 2.0 | ML Team | 🟡 Evaluation |
| **Keras** | 2.14.0 | High-level API | Apache 2.0 | ML Team | ✅ Active |
| **scikit-learn** | 1.3.2 | Classical ML | BSD | Data Team | ✅ Active |
| **XGBoost** | 2.0.1 | Gradient boosting | Apache 2.0 | Data Team | ✅ Active |

### Training & Orchestration

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **Kubeflow** | 1.8.0 | ML pipeline orchestration | Apache 2.0 | MLOps Team | ✅ Active |
| **Apache Airflow** | 2.7.3 | Workflow orchestration | Apache 2.0 | DevOps Team | ✅ Active |
| **Ray** | 2.8.0 | Distributed computing | Apache 2.0 | ML Team | ✅ Active |
| **Horovod** | 0.28.1 | Distributed training | Apache 2.0 | ML Team | ✅ Active |
| **DeepSpeed** | 0.12.0 | Training optimization | MIT | ML Team | 🟡 Evaluation |

### Experiment Tracking

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **MLflow** | 2.8.1 | Experiment tracking | Apache 2.0 | ML Team | ✅ Active |
| **Weights & Biases** | 0.16.0 | Experiment tracking | Commercial | ML Team | ✅ Active |
| **TensorBoard** | 2.14.0 | Visualization | Apache 2.0 | ML Team | ✅ Active |
| **Neptune.ai** | 1.8.5 | Metadata store | Commercial | ML Team | 🟡 Evaluation |

### Data Engineering

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **DVC** | 3.30.0 | Data version control | Apache 2.0 | Data Team | ✅ Active |
| **Pandas** | 2.1.3 | Data manipulation | BSD | Data Team | ✅ Active |
| **Polars** | 0.19.19 | Fast dataframes | MIT | Data Team | 🟡 Evaluation |
| **Dask** | 2023.11.0 | Parallel computing | BSD | Data Team | ✅ Active |
| **Apache Spark** | 3.5.0 | Big data processing | Apache 2.0 | Data Team | ✅ Active |
| **Great Expectations** | 0.18.3 | Data quality | Apache 2.0 | Data Team | ✅ Active |

### Model Deployment & Serving

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **ONNX Runtime** | 1.16.3 | Model inference | MIT | MLOps Team | ✅ Active |
| **TensorRT** | 8.6.1 | GPU inference | Proprietary | MLOps Team | ✅ Active |
| **OpenVINO** | 2023.2 | Intel optimization | Apache 2.0 | MLOps Team | 🟡 Evaluation |
| **TorchServe** | 0.9.0 | PyTorch serving | Apache 2.0 | MLOps Team | ✅ Active |
| **Triton Inference Server** | 2.40.0 | Multi-framework serving | BSD | MLOps Team | ✅ Active |
| **BentoML** | 1.1.9 | Model serving | Apache 2.0 | MLOps Team | 🟡 Evaluation |

### Containerization & Orchestration

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **Docker** | 24.0.7 | Containerization | Apache 2.0 | DevOps Team | ✅ Active |
| **Kubernetes** | 1.28.4 | Container orchestration | Apache 2.0 | DevOps Team | ✅ Active |
| **Helm** | 3.13.2 | K8s package manager | Apache 2.0 | DevOps Team | ✅ Active |
| **Podman** | 4.7.2 | Container runtime | Apache 2.0 | DevOps Team | 🟡 Evaluation |

## High-Fidelity Engineering Tools

### CFD (Computational Fluid Dynamics)

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **ANSYS Fluent** | 2024R1 | Commercial CFD | Commercial | Aero Team | ✅ Active |
| **ANSYS CFX** | 2024R1 | Turbomachinery CFD | Commercial | Propulsion Team | ✅ Active |
| **OpenFOAM** | v2312 | Open-source CFD | GPL | Aero Team | ✅ Active |
| **SU2** | 7.5.1 | Open-source CFD/adjoint | LGPL | Aero Team | 🟡 Evaluation |
| **STAR-CCM+** | 2023.1 | Commercial CFD | Commercial | Aero Team | 🔴 Not Used |

### Meshing

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **ANSYS ICEM CFD** | 2024R1 | Structured/hybrid meshing | Commercial | Aero Team | ✅ Active |
| **ANSYS Meshing** | 2024R1 | Unstructured meshing | Commercial | Aero Team | ✅ Active |
| **Pointwise** | V18.5R2 | Mesh generation | Commercial | Aero Team | ✅ Active |
| **snappyHexMesh** | OF v2312 | Hex-dominant meshing | GPL | Aero Team | ✅ Active |
| **Gmsh** | 4.12.0 | Open-source mesher | GPL | Aero Team | 🟡 Evaluation |

### FEM (Finite Element Method)

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **ANSYS Mechanical** | 2024R1 | Structural analysis | Commercial | Structures Team | ✅ Active |
| **MSC Nastran** | 2023.3 | FEA solver | Commercial | Structures Team | ✅ Active |
| **Abaqus** | 2023 | Nonlinear FEA | Commercial | Structures Team | 🟡 Available |
| **LS-DYNA** | R13.1 | Explicit dynamics | Commercial | Structures Team | 🟡 Available |
| **Code_Aster** | 16.2.0 | Open-source FEA | GPL | Structures Team | 🟡 Evaluation |

### Multiphysics

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **ANSYS Workbench** | 2024R1 | Multiphysics platform | Commercial | Multiphysics Team | ✅ Active |
| **COMSOL Multiphysics** | 6.2 | Multiphysics modeling | Commercial | Multiphysics Team | 🟡 Available |
| **OpenFOAM + FEniCS** | Custom | FSI coupling | GPL | Multiphysics Team | 🟡 Development |

### Aeroelasticity

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **MSC Nastran Aeroelastic** | 2023.3 | Flutter analysis | Commercial | Aeroelastic Team | ✅ Active |
| **ZAERO** | 9.5 | Unsteady aero | Commercial | Aeroelastic Team | ✅ Active |
| **FFAST** | 3.3 | Flutter testing | Commercial | Flight Test Team | 🟡 Available |

### Pre/Post Processing

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **ParaView** | 5.12.0 | Visualization | BSD | All Teams | ✅ Active |
| **Tecplot 360** | 2023R1 | CFD visualization | Commercial | Aero Team | ✅ Active |
| **EnSight** | 2023.2 | Visualization | Commercial | All Teams | 🟡 Available |
| **PyVista** | 0.43.0 | Python visualization | MIT | All Teams | ✅ Active |

## Development & Collaboration Tools

### Version Control

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **Git** | 2.43.0 | Version control | GPL | All Teams | ✅ Active |
| **GitHub** | Enterprise | Code hosting | Commercial | All Teams | ✅ Active |
| **Git LFS** | 3.4.1 | Large file storage | MIT | All Teams | ✅ Active |

### Code Quality

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **Black** | 23.11.0 | Python formatting | MIT | Dev Team | ✅ Active |
| **Pylint** | 3.0.3 | Python linting | GPL | Dev Team | ✅ Active |
| **Mypy** | 1.7.1 | Python type checking | MIT | Dev Team | ✅ Active |
| **isort** | 5.12.0 | Import sorting | MIT | Dev Team | ✅ Active |
| **Ruff** | 0.1.6 | Fast Python linter | MIT | Dev Team | 🟡 Evaluation |
| **SonarQube** | 10.3 | Code quality platform | LGPL | Dev Team | ✅ Active |

### Testing

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **pytest** | 7.4.3 | Python testing | MIT | Dev Team | ✅ Active |
| **pytest-cov** | 4.1.0 | Coverage reporting | MIT | Dev Team | ✅ Active |
| **Hypothesis** | 6.92.1 | Property-based testing | MPL 2.0 | Dev Team | ✅ Active |
| **unittest** | (stdlib) | Unit testing | PSF | Dev Team | ✅ Active |

### CI/CD

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **GitHub Actions** | - | CI/CD automation | Commercial | DevOps Team | ✅ Active |
| **Jenkins** | 2.426.2 | CI/CD server | MIT | DevOps Team | 🟡 Available |
| **ArgoCD** | 2.9.3 | GitOps CD | Apache 2.0 | DevOps Team | ✅ Active |

### Documentation

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **Sphinx** | 7.2.6 | Documentation generator | BSD | Doc Team | ✅ Active |
| **MkDocs** | 1.5.3 | Markdown docs | BSD | Doc Team | ✅ Active |
| **Doxygen** | 1.9.8 | Code documentation | GPL | Doc Team | 🟡 Available |
| **Pandoc** | 3.1.11 | Document conversion | GPL | Doc Team | ✅ Active |

## CAD/PLM Tools

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **CATIA V6** | R2023x | CAD/CAM/CAE | Commercial | Design Team | ✅ Active |
| **Siemens NX** | 2306 | CAD/CAM/CAE | Commercial | Design Team | 🟡 Available |
| **SolidWorks** | 2024 | 3D CAD | Commercial | Design Team | 🟡 Available |
| **FreeCAD** | 0.21.2 | Open-source CAD | LGPL | Design Team | 🟡 Evaluation |

## Cloud & Infrastructure

### Cloud Platforms

| Platform | Services Used | Owner | Status |
|----------|---------------|-------|--------|
| **AWS** | EC2, S3, SageMaker, Lambda | DevOps Team | ✅ Active |
| **Azure** | VMs, Blob Storage, ML | DevOps Team | 🟡 Available |
| **Google Cloud** | Compute, Storage, Vertex AI | DevOps Team | 🟡 Evaluation |

### HPC Resources

| Resource | Specs | Purpose | Owner | Status |
|----------|-------|---------|-------|--------|
| **On-Prem HPC Cluster** | 128 nodes, 256 GPUs (A100) | Training, CFD, FEM | IT Team | ✅ Active |
| **AWS ParallelCluster** | Scalable HPC | Burst capacity | DevOps Team | ✅ Active |

## Monitoring & Observability

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **Prometheus** | 2.48.0 | Metrics collection | Apache 2.0 | Ops Team | ✅ Active |
| **Grafana** | 10.2.2 | Metrics visualization | AGPL | Ops Team | ✅ Active |
| **ELK Stack** | 8.11.1 | Log aggregation | Elastic License | Ops Team | ✅ Active |
| **Jaeger** | 1.52.0 | Distributed tracing | Apache 2.0 | Ops Team | 🟡 Evaluation |

## Security & Compliance

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **Snyk** | - | Vulnerability scanning | Commercial | Security Team | ✅ Active |
| **Trivy** | 0.48.0 | Container scanning | Apache 2.0 | Security Team | ✅ Active |
| **Vault** | 1.15.4 | Secrets management | MPL 2.0 | Security Team | ✅ Active |
| **detect-secrets** | 1.4.0 | Secret scanning | Apache 2.0 | Security Team | ✅ Active |

## CAOS Integration Tools

| Tool | Version | Purpose | License | Owner | Status |
|------|---------|---------|---------|-------|--------|
| **MCP Server** | 1.2.0 | Model Context Protocol | Proprietary | CAOS Team | ✅ Active |
| **CAOS SDK** | 2.3.0 | Integration library | Proprietary | CAOS Team | ✅ Active |
| **CAOS Dashboard** | 3.1.0 | Operations interface | Proprietary | CAOS Team | ✅ Active |

## Tool Evaluation Process

### Criteria for Tool Selection

1. **Functionality**: Meets technical requirements
2. **Performance**: Acceptable speed and resource usage
3. **Reliability**: Stable, well-maintained
4. **Integration**: Works with existing tools
5. **Cost**: Affordable (capex & opex)
6. **Support**: Adequate documentation and community
7. **Compliance**: Meets regulatory requirements
8. **Security**: No known vulnerabilities

### Evaluation Stages

```
Request → Technical Review → Pilot Testing → Stakeholder Approval → Procurement → Deployment → Training
```

### Status Definitions

- ✅ **Active**: Currently in production use
- 🟡 **Evaluation**: Under assessment or pilot testing
- 🟡 **Available**: Licensed but not actively used
- 🔴 **Not Used**: Evaluated and rejected or deprecated
- 🔵 **Planned**: Identified for future adoption

## License Management

### Commercial Licenses

| Software | Licenses | Cost/Year | Renewal | Contact |
|----------|----------|-----------|---------|---------|
| ANSYS Suite | 20 concurrent | $500k | 2026-06 | IT Team |
| MSC Nastran | 10 concurrent | $200k | 2026-03 | IT Team |
| Weights & Biases | Team plan | $24k | 2026-01 | ML Team |
| GitHub Enterprise | Unlimited | $36k | 2026-12 | DevOps Team |

### Open-Source Compliance

All open-source software must:
- Have approved licenses (Apache, MIT, BSD, GPL)
- Be tracked in software BOM
- Comply with license terms (attribution, copyleft)
- Be scanned for vulnerabilities

## Tool Updates & Maintenance

### Update Policy

- **Security patches**: Apply within 7 days
- **Minor updates**: Quarterly review
- **Major upgrades**: Annual planning cycle
- **Deprecation notice**: 6 months minimum

### Maintenance Windows

- **Monthly**: First Saturday, 02:00-06:00 UTC
- **Emergency**: As needed, with notification

## Training & Documentation

Each tool must have:
- Getting started guide
- API/user documentation
- Best practices document
- Contact for support

Training provided:
- New user onboarding
- Quarterly workshops
- Advanced topics (on request)

## References

1. Software Tool Evaluation Checklist (AMPEL360-IT-001)
2. Open Source Software Policy (AMPEL360-LEGAL-002)
3. License Management Procedures (AMPEL360-IT-003)

## Document Control

- **Author**: AMPEL360 IT & Engineering Teams
- **Reviewer**: [To be assigned]
- **Approver**: [To be assigned]
- **Next Review**: 2026-02-17
- **Change History**: Version 1.0 - Initial release

---

**END OF DOCUMENT**
