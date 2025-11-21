# 02-60-09 – Edge Storage

## Purpose

On-board and edge device storage for aircraft systems, EFB applications, and IMA partitions, designed for aviation environmental conditions per [DO-160](https://standards.rtca.org/).

---

## Scope

- **IMA Storage**: Integrated Modular Avionics partitioned storage
- **EFB Local Storage**: Electronic Flight Bag offline data and cache
- **Offline Sync**: Delta synchronization with ground systems
- **Flash Management**: Wear leveling and lifetime optimization

---

## Key Documents

- **[02-60-09-001_IMA_Storage_Architecture.md](./02-60-09-001_IMA_Storage_Architecture.md)** – IMA storage partitioning
- **[02-60-09-002_EFB_Local_Storage.md](./02-60-09-002_EFB_Local_Storage.md)** – EFB storage design
- **[02-60-09-003_Offline_Data_Sync.md](./02-60-09-003_Offline_Data_Sync.md)** – Sync patterns
- **[02-60-09-004_Flash_Memory_Management.md](./02-60-09-004_Flash_Memory_Management.md)** – Flash lifetime management

---

## Environmental Requirements

Per [DO-160](https://standards.rtca.org/):
- **Temperature Range**: -40°C to +85°C
- **Altitude**: Up to 55,000 ft
- **Vibration**: Category S (severe)
- **EMI/EMC**: Category M (most stringent)

---

## Document Control

- **Directory**: 02-60-09_Edge_Storage
- **Version**: 1.0
- **Status**: DRAFT
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.
