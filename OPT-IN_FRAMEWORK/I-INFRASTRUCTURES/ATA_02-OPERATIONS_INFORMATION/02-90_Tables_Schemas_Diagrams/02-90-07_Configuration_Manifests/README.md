# 02-90-07: Configuration Manifests

## Purpose

This folder contains infrastructure and deployment manifests (Kubernetes, Helm, Docker, Terraform) used by AMPEL360 operations systems.

## Scope

Configuration manifests define:

- **Kubernetes**: Namespace, deployment, service, ingress configurations
- **Helm Charts**: Packaged application deployments
- **Docker**: Container definitions and compose configurations
- **Terraform**: Infrastructure as code for cloud resources

All manifests are **examples** without production credentials or endpoints.

## Structure

```
02-90-07_Configuration_Manifests/
├── README.md (this file)
├── 02-90-07-001_Kubernetes_Manifests.md
├── 02-90-07-002_Docker_Compose_Configs.md
├── 02-90-07-003_Helm_Charts_Index.md
└── ASSETS/
    ├── Kubernetes/        # K8s YAML manifests
    ├── Helm/              # Helm chart packages
    ├── Docker/            # Docker and docker-compose files
    └── Terraform/         # Infrastructure as code
```

## Kubernetes

### Namespace Configuration

Logical separation of workloads:

- `operations`: Flight operations services
- `analytics`: Data analytics and reporting
- `monitoring`: Observability stack (Prometheus, Grafana)
- `data`: Database and storage systems

Example: [Namespace Config](./ASSETS/Kubernetes/02-90-07-A-001_namespace_config.yaml)

### Deployments

Application deployments with:
- Replica counts for high availability
- Resource requests and limits
- Health checks (liveness, readiness)
- Environment-specific configurations

### Services

Service exposure patterns:
- **ClusterIP**: Internal services
- **NodePort**: Development/testing
- **LoadBalancer**: Production external services
- **Ingress**: HTTP/HTTPS routing with TLS

## Helm Charts

Helm charts provide templated, versioned deployments:

### Operations Chart

[Operations chart](./ASSETS/Helm/02-90-07-A-101_operations_chart/) deploys:
- Backend services ([02-40-12](../../02-40_Software/02-40-12_Backend_Services/README.md))
- API gateways
- Database connections

### Analytics Chart

[Analytics chart](./ASSETS/Helm/02-90-07-A-102_analytics_chart/) deploys:
- Analytics engine ([02-40-19](../../02-40_Software/02-40-19_Analytics_Engine/README.md))
- Data warehouse connections
- BI tools

### Monitoring Chart

[Monitoring chart](./ASSETS/Helm/02-90-07-A-103_monitoring_chart/) deploys:
- Prometheus for metrics
- Grafana for dashboards
- ELK stack for logging

## Docker

### Docker Compose

[Docker compose](./ASSETS/Docker/02-90-07-A-201_docker-compose.yml) orchestrates:

```yaml
services:
  backend:
    image: ampel360/backend-services:latest
    ports:
      - "8080:8080"
    environment:
      - DATABASE_URL=postgresql://db:5432/operations
  
  database:
    image: postgres:13
    volumes:
      - db-data:/var/lib/postgresql/data
  
  redis:
    image: redis:6
```

### Dockerfiles

[Dockerfiles](./ASSETS/Docker/02-90-07-A-202_Dockerfiles/) define container images for services.

### Network Configuration

[Docker network config](./ASSETS/Docker/02-90-07-A-203_docker_network_config.yaml) defines:
- Bridge networks for services
- Custom subnets
- Service discovery via DNS

## Terraform

### Infrastructure Modules

[Terraform modules](./ASSETS/Terraform/02-90-07-A-301_infrastructure_config/) for:

- **Networking**: VPC, subnets, security groups
- **Compute**: Kubernetes clusters, VM instances
- **Storage**: S3/blob storage, persistent volumes
- **Databases**: Managed PostgreSQL, TimescaleDB, MongoDB
- **Monitoring**: CloudWatch, Cloud Monitoring

### State Management

[State configuration](./ASSETS/Terraform/02-90-07-A-302_state_files/) for:
- Remote state backends (S3, GCS, Azure Storage)
- State locking (DynamoDB, Consul)
- Workspace management

## Environment Management

### Environment Tiers

| Environment | Purpose | Configuration |
|-------------|---------|---------------|
| **Development** | Local development | Docker Compose, minimal resources |
| **Staging** | Pre-production testing | Kubernetes, production-like config |
| **Production** | Live operations | Kubernetes, HA, autoscaling |

### Configuration Hierarchy

```
Base Configuration
├── Development Overrides
├── Staging Overrides
└── Production Overrides
```

### Secret Management

Secrets handled via:
- **Kubernetes Secrets**: For K8s deployments
- **HashiCorp Vault**: For centralized secret management
- **Cloud KMS**: For encryption at rest

**Note**: No actual secrets in this repository. All examples use placeholders.

## Security Considerations

- **RBAC**: Role-based access control in Kubernetes
- **Network Policies**: Restrict pod-to-pod communication
- **Pod Security**: Security contexts, non-root users
- **Image Scanning**: Vulnerability scanning in CI/CD
- **Secret Rotation**: Automated secret rotation policies

## CI/CD Integration

Manifests used in GitOps workflows:

```
Git Push → CI/CD Pipeline → Validate Manifests → Apply to Cluster
```

Tools:
- **GitLab CI / GitHub Actions**: Pipeline orchestration
- **ArgoCD / Flux**: GitOps deployment
- **Helm**: Chart deployment
- **Terraform**: Infrastructure provisioning

## Usage Guidelines

### For DevOps Engineers

1. **Review manifests**: Understand configuration structure
2. **Customize for environment**: Apply environment-specific overrides
3. **Validate locally**: Test with `kubectl apply --dry-run`
4. **Deploy gradually**: Canary or blue-green deployments
5. **Monitor deployments**: Track rollout status and health

### For Developers

1. **Local development**: Use Docker Compose for rapid iteration
2. **Feature branches**: Deploy to development namespaces
3. **Integration testing**: Deploy to staging before production
4. **Document changes**: Update manifest documentation

### For Security Teams

1. **Review RBAC**: Validate access controls
2. **Scan images**: Check for vulnerabilities
3. **Audit secrets**: Ensure no secrets in Git
4. **Network policies**: Validate segmentation

## Cross-References

- [02-90-01 Database Schemas](../02-90-01_Database_Schemas/README.md)
- [02-90-02 API Specifications](../02-90-02_API_Specifications/README.md)
- [02-40 Software](../../02-40_Software/README.md)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Documentation](https://helm.sh/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Terraform Documentation](https://www.terraform.io/docs/)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
