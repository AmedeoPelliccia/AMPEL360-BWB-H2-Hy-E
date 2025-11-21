# 02-90-09: Wiring and Data Network Diagrams

## Purpose

This folder contains diagrams describing physical and logical network/wiring related to AMPEL360 operations systems.

## Scope

Network and wiring documentation includes:

- **Network Topology**: Physical and logical network layouts
- **AFDX Networks**: Avionics network diagrams
- **Ground Infrastructure**: Data center and ground station networks
- **Edge Computing**: Aircraft and edge device connectivity

All diagrams are **generic, non-proprietary examples** suitable for architecture discussions.

## Structure

```
02-90-09_Wiring_Data_Network_Diagrams/
├── README.md (this file)
├── 02-90-09-001_Network_Wiring_Diagrams.md
├── 02-90-09-002_AFDX_Network_Topology.md
├── 02-90-09-003_Ground_Infrastructure_Network.md
└── ASSETS/
    ├── AFDX/              # Avionics network diagrams
    ├── Ground/            # Ground infrastructure networks
    ├── Edge/              # Edge computing connectivity
    └── Integration/       # Network integration diagrams
```

## Network Types

### AFDX (Avionics Full-Duplex Switched Ethernet)

AFDX network topology diagrams show:

- **End Systems**: Avionics computers and displays
- **Switches**: Redundant network switches (A/B network)
- **Virtual Links**: Logical communication channels
- **Physical Topology**: Cable runs and connections

Reference: [AFDX Network Topology](../02-90-03_Data_Exchange_Formats/ASSETS/AFDX/02-90-03-A-003_Network_Topology.svg)

### Ground Infrastructure

Ground network architecture:

- **Data Centers**: Cloud and on-premise infrastructure
- **Operations Centers**: AOC (Airline Operations Center) connectivity
- **Internet Gateways**: Secure internet access
- **VPN Tunnels**: Site-to-site encrypted connections

### Edge Computing

Edge device connectivity:

- **Aircraft Systems**: Onboard computing and storage
- **EFB Devices**: Electronic Flight Bag connectivity
- **Ground Stations**: Aircraft-to-ground datalink
- **Satellite Links**: SATCOM for remote operations

## Diagram Categories

### Physical Topology

Shows actual cable runs, connectors, and hardware:

- Cable types (fiber, copper, wireless)
- Connector types and pinouts
- Rack layouts and cable management
- Power distribution

### Logical Topology

Shows logical connections and data flows:

- VLANs and subnets
- Routing protocols
- Firewall rules
- Load balancing

### Integration Diagrams

Cross-system network integration:

- Aircraft-to-ground communications
- Cloud-to-edge synchronization
- External system connections (ANSP, airports)
- Redundancy and failover paths

## Network Standards

| Standard | Purpose | Reference |
|----------|---------|-----------|
| **ARINC 664 Part 7** | AFDX specification | [ARINC 664](https://en.wikipedia.org/wiki/ARINC_664) |
| **IEEE 802.3** | Ethernet | [IEEE 802.3](https://standards.ieee.org/) |
| **IEEE 802.11** | Wi-Fi | [IEEE 802.11](https://standards.ieee.org/) |
| **ARINC 781** | Aircraft-ground datalink | [ARINC Standards](https://www.arinc.com/) |

## Security Zones

Network segmentation by security zone:

### Avionics Zone

- **Criticality**: Safety-critical systems
- **Isolation**: Air-gapped or strict firewall rules
- **Access**: Limited to certified systems only

### Operations Zone

- **Criticality**: Business-critical operations
- **Isolation**: Firewall with DMZ
- **Access**: Authenticated users and systems

### Analytics Zone

- **Criticality**: Non-critical analytics
- **Isolation**: Read-only access to operational data
- **Access**: Data scientists and analysts

### DMZ (Demilitarized Zone)

- **Purpose**: External-facing services
- **Isolation**: Strict ingress/egress rules
- **Access**: Public APIs with authentication

## Network Performance

### Bandwidth Requirements

| System | Bandwidth | Latency | Reliability |
|--------|-----------|---------|-------------|
| AFDX | 10-100 Mbps per VL | <1 ms | 99.999% |
| Operations Data | 1-10 Gbps | <10 ms | 99.99% |
| Analytics | 10+ Gbps | <100 ms | 99.9% |
| Telemetry Streaming | 1-10 Gbps | <50 ms | 99.95% |

### Quality of Service (QoS)

Priority levels:

1. **Critical**: Safety-critical avionics (highest priority)
2. **Real-time**: Operations and telemetry
3. **Business**: Management and reporting
4. **Best-effort**: Analytics and non-time-sensitive data

## Redundancy and Failover

### Network Redundancy

- **AFDX**: Dual redundant networks (A/B)
- **Ground**: Multi-path routing with BGP
- **Datalink**: Primary and backup communication channels
- **Power**: Redundant power supplies and UPS

### Failover Scenarios

- **Primary link down**: Automatic failover to backup
- **Site failure**: Traffic rerouted to backup data center
- **Device failure**: Load balancer redirects to healthy nodes

## Monitoring and Management

### Network Monitoring

Tools and metrics:

- **Traffic analysis**: Bandwidth utilization, packet loss
- **Latency monitoring**: Round-trip time, jitter
- **Availability**: Uptime and SLA tracking
- **Security**: Intrusion detection, anomaly detection

### Management Interfaces

- **SNMP**: Simple Network Management Protocol
- **NetFlow**: Traffic flow analysis
- **APIs**: Programmatic network management

## Diagram Maintenance

### Update Triggers

Update diagrams when:

1. **New systems deployed**: Add to network topology
2. **Network changes**: VLAN, routing, firewall rule changes
3. **Infrastructure changes**: New data centers, links
4. **Security changes**: Zone boundary modifications

### Review Process

1. **Document change**: Update diagram source file
2. **Export formats**: Regenerate SVG, PDF
3. **Peer review**: Network engineer validation
4. **Approval**: Security and architecture review (if needed)
5. **Deployment**: Update documentation portal

## Cross-References

- [02-90-03 Data Exchange Formats](../02-90-03_Data_Exchange_Formats/README.md) – AFDX and protocol specs
- [02-90-04 System Architecture Diagrams](../02-90-04_System_Architecture_Diagrams/README.md) – System-level diagrams
- [02-90-07 Configuration Manifests](../02-90-07_Configuration_Manifests/README.md) – Network configurations
- [ARINC 664 Part 7](https://en.wikipedia.org/wiki/ARINC_664) – AFDX specification
- [IEEE 802 Standards](https://standards.ieee.org/)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
