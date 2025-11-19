# 02-20_Subsystems — Digital Operations Management & Information Systems

**Axis:** I — Infrastructures  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../README.md)  
**Bucket 20:** Subsystems (Digital Ops Platforms & Operational Information Systems)

---

## 1. Purpose

`02-20_Subsystems` agrupa todos los **subsystems digitales de operaciones** que:

- Gestionan la **información operacional** de AMPEL360 (documentos, datos, perfiles)  
- Ejecutan **cálculos clave** (performance, W&B, planning, H₂…)  
- Integran operaciones aéreas con **sistemas de tierra, AOC y CAOS/AirCCC**  
- Conectan con **ATA 95 Neural Networks** para capacidades predictivas y optimización  

Es el *hub técnico* de ATA 02: todo lo que consumen `02-10_Operations`, `02-30_Circularity`,
`02-90_Tables_Schemas_Diagrams` y CAOS vive aquí o se referencia desde aquí.

---

## 2. Top-Level Artefacts

- [`02-20-00-001_Subsystems_Overview.md`](./02-20-00-001_Subsystems_Overview.md)  
  Visión general de todos los subsistemas digitales de operaciones (scope, roles, mapa funcional).

- [`02-20-00-002_Subsystems_Integration_Map.md`](./02-20-00-002_Subsystems_Integration_Map.md)  
  Mapa de integración entre subsistemas 02-20 y otros ATA (28, 31, 42, 95, etc.).

- [`02-20-00-003_Cross_ATA_Dependencies.csv`](./02-20-00-003_Cross_ATA_Dependencies.csv)  
  Matriz de dependencias cruzadas ATA (importante para certificación y trazabilidad).

- [`02-20-00-004_CAOS_Operations_Integration.md`](./02-20-00-004_CAOS_Operations_Integration.md)  
  Cómo CAOS/AirCCC consume datos de 02-20 y los reinyecta en 02-10_Operations.

---

## 3. Subsystems Index

### 3.1 Core Digital Ops Platform

- [`02-20-01_Digital_Ops_Platform/`](./02-20-01_Digital_Ops_Platform/)  
  Plataforma núcleo de operaciones digitales (backbone de datos y servicios).

  - [`README.md`](./02-20-01_Digital_Ops_Platform/README.md)  
  - `02-20-01-001_Platform_Architecture.md`  
  - `02-20-01-002_Data_Management.md`  
  - `02-20-01-003_User_Interfaces.md`  
  - `02-20-01-004_Integration_Layer.md`  
  - `ASSETS/` (arquitecturas y data flow diagrams)

---

### 3.2 Electronic Flight Bag (EFB) — 02-20-11

- [`02-20-11_Electronic_Flight_Bag/`](./02-20-11_Electronic_Flight_Bag/)  
  Sistema EFB (Class 3 / portable), centro de:

  - Gestión documental  
  - Cálculo de performance  
  - Weight & Balance  
  - Integración meteorológica y NOTAMs  

  Documentos clave:

  - `02-20-11-001_EFB_Overview.md`  
    – overview funcional y de certificación del EFB  
  - `02-20-11-002_Class_3_EFB_Implementation.md`  
  - `02-20-11-003_Document_Management.md`  
  - `02-20-11-004_Performance_Calculations.md`  
  - `02-20-11-005_Weight_Balance_Module.md`  
  - `02-20-11-006_Weather_Integration.md`  
  - `02-20-11-007_Charts_Navigation_Data.md`  
  - `02-20-11-008_Integration_with_ATA_42.md`  
  - `02-20-11-009_Safety_and_Certification.md`  

  - `ASSETS/`  
    - `02-20-11-A-001_EFB_System_Architecture.drawio`  
    - `02-20-11-A-002_EFB_System_Architecture.svg`  
    - `02-20-11-A-003_Class_3_Integration.svg`  
    - `02-20-11-A-101_Display_Mockups.pdf`  
    - `Certification/` (DO-178C, AC 120-76D evidencia, etc.)

---

### 3.3 Weight & Balance Computer — 02-20-12

- [`02-20-12_Weight_Balance_Computer/`](./02-20-12_Weight_Balance_Computer/)  
  Motor de cálculo de **W&B**, incluyendo integración H₂ y seguimiento CG en tiempo real.

---

### 3.4 Performance Computer — 02-20-13

- [`02-20-13_Performance_Computer/`](./02-20-13_Performance_Computer/)  
  Cálculos de performance (despegue, aterrizaje, crucero), incluyendo NN de performance
  y particularidades BWB.

---

### 3.5 Ground Operations Management — 02-20-14

- [`02-20-14_Ground_Ops_Management/`](./02-20-14_Ground_Ops_Management/)  
  Gestión de operaciones en tierra, turnaround, GSE, H₂ refuelling y carga.

---

### 3.6 Flight Planning Integration — 02-20-15

- [`02-20-15_Flight_Planning_Integration/`](./02-20-15_Flight_Planning_Integration/)  
  Integración con sistemas de flight planning (rutas, H₂ fuel planning, alternates, NOTAM, meteo).

---

### 3.7 Dispatch System Integration — 02-20-16

- [`02-20-16_Dispatch_System_Integration/`](./02-20-16_Dispatch_System_Integration/)  
  Integración con el Airline Operations Center / AOC, flight releases, actualizaciones en tiempo real.

---

### 3.8 Weather Information System — 02-20-17

- [`02-20-17_Weather_Information_System/`](./02-20-17_Weather_Information_System/)  
  Sistema de ingestión, fusión y presentación de datos meteo (incluye NN de predicción).

---

### 3.9 Operational Data Recording — 02-20-18

- [`02-20-18_Operational_Data_Recording/`](./02-20-18_Operational_Data_Recording/)  
  Logging de eventos operacionales, integración con ATA 31/FDR y DPP.

---

### 3.10 Crew Resource Management — 02-20-19

- [`02-20-19_Crew_Resource_Management/`](./02-20-19_Crew_Resource_Management/)  
  Herramientas de coordinación de tripulación, workload monitoring, task management.

---

### 3.11 H₂ Operations Management — 02-20-21

- [`02-20-21_H2_Operations_Management/`](./02-20-21_H2_Operations_Management/)  
  Gestión de operaciones específicas H₂ (procedimientos, safety monitoring, infraestructura).

---

### 3.12 Passenger Experience Management — 02-20-22

- [`02-20-22_Passenger_Experience_Management/`](./02-20-22_Passenger_Experience_Management/)  
  Sistemas de gestión de experiencia pasajero (embarque, servicio a bordo, comfort monitoring).

---

### 3.13 Predictive Operations NN — 02-20-23

- [`02-20-23_Predictive_Operations_NN/`](./02-20-23_Predictive_Operations_NN/)  
  Subsystem de **optimización predictiva de operaciones** (delays, turnaround, recursos) usando NN/RL.

---

## 4. Cross-ATA Integration & CAOS

Las integraciones **críticas** con otros capítulos ATA se documentan en:

- [`02-20-00-002_Subsystems_Integration_Map.md`](./02-20-00-002_Subsystems_Integration_Map.md)  
- [`02-20-00-003_Cross_ATA_Dependencies.csv`](./02-20-00-003_Cross_ATA_Dependencies.csv)  
- [`02-20-00-004_CAOS_Operations_Integration.md`](./02-20-00-004_CAOS_Operations_Integration.md)  

Capítulos típicamente enlazados:

- **ATA 03** – Support Information / GSE  
- **ATA 28** – Hydrogen Fuel System  
- **ATA 31** – Indicating/Recording (recording function)  
- **ATA 42** – IMA / AOC interfaces  
- **ATA 71** – Fuel Cell Powerplant  
- **ATA 95** – Neural Networks / Users / Traceability  

Documentación CAOS relevante:

- [CAOS Index](../../../CAOS/CAOS_INDEX.md)  
- [CAOS Operations Framework](../../../CAOS/CAOS_OPERATIONS_FRAMEWORK.md)  
- [CAOS Use Cases](../../../CAOS/CAOS_USE_CASES.md)

---

## 5. Conventions

- Código de subsistema: `02-20-XX_Subsystem_Name/`  
- Artefactos internos: `02-20-XX-YYY_Description.ext`  
  - `XX` = identificador de subsistema  
  - `YYY` = número secuencial (001, 002, …)  

Cada `README.md` de subsistema debe incluir al menos:

- **Scope**  
- **Interfaces (ATA y externos)**  
- **Datos de entrada/salida**  
- **CAOS observability / KPIs**  
- **Vínculos con ATA 95 (si aplica)**  

---

## 6. Document Control

> **Status:** Draft / Structure defined  
> **Owner:** AMPEL360 Digital Operations & CAOS Working Group  
> **Applies to:** All digital operations subsystems under ATA_02

| Version | Date       | Author / Team                                   | Changes                                  |
|---------|------------|--------------------------------------------------|------------------------------------------|
| 0.1     | YYYY-MM-DD | AMPEL360 Digital Operations & CAOS WG           | Initial 02-20_Subsystems structure       |
