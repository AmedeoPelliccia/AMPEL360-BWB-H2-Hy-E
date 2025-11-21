# 02-60-04 – Cache Storage

## Purpose

This directory defines the in-memory caching infrastructure using Redis and Memcached for high-performance data access, session management, and computed data caching.

---

## Scope

- **Session Storage**: User sessions and authentication tokens
- **Hot Keys**: Frequently accessed reference data
- **Computed Views**: Pre-calculated performance data and analytics
- **API Response Caching**: Reduce backend load and improve response times

---

## Key Documents

- **[02-60-04-001_Redis_Cluster_Architecture.md](./02-60-04-001_Redis_Cluster_Architecture.md)** – Redis cluster design and sharding
- **[02-60-04-002_Cache_Strategies.md](./02-60-04-002_Cache_Strategies.md)** – Cache patterns (write-through, write-back, read-through)
- **[02-60-04-003_Eviction_Policies.md](./02-60-04-003_Eviction_Policies.md)** – Eviction policies and settings
- **[02-60-04-004_Session_Storage.md](./02-60-04-004_Session_Storage.md)** – Session management approach

---

## ASSETS

- **02-60-04-A-001_Redis_Cluster_Config.conf** – Redis cluster configuration
- **02-60-04-A-002_Sentinel_Setup.conf** – Sentinel HA configuration
- **02-60-04-A-003_Eviction_Policy.conf** – Eviction policy settings
- **02-60-04-A-101_Hit_Rate_Analysis.xlsx** – Cache hit/miss metrics
- **02-60-04-A-102_Latency_Benchmarks.pdf** – Cache latency benchmarks

---

## Technology Stack

- **Redis 7.x** (primary cache, cluster mode)
- **Redis Sentinel** (high availability)
- **Memcached 1.6+** (specific use cases)

---

## Performance Targets

- **Hit Rate**: > 90%
- **Latency**: < 1ms (p95)
- **Availability**: 99.9%
- **Capacity**: 100-500 GB per cluster

---

## Document Control

- **Directory**: 02-60-04_Cache_Storage
- **Version**: 1.0
- **Status**: DRAFT
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.
