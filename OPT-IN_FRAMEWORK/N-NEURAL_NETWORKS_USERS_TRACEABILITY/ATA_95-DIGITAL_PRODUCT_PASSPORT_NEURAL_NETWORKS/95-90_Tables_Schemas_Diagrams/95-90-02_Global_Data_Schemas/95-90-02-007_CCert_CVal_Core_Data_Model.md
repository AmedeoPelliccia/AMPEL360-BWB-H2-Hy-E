# 95-90-02-007_CCert_CVal_Core_Data_Model

**Document ID**: 95-90-02-007  
**Title**: CCert / CVal Core Data Model — AM–DPP–OM–OAV–DT  
**Version**: 1.0  
**Status**: WORKING  
**Owner**: AMPEL360 / ATA 95 Data Architecture  
**Related ATA**: 95-00, 95-20, 95-30, 95-40, 95-90  

---

## 1. Propósito

Este documento define el **esquema de datos central** para el ciclo:

> **AM → DV → DPP → OM → OAV → DT → AM'**

y su uso como:

- **esqueleto de base de datos** para  
  - Continuous Certification (**CCert**)  
  - Continuous Validation (**CVal**)  
- soporte a DPP, NN, OM (Ontological Missions) y Digital Twin ontogenético.

El objetivo es:

- estructurar los datos clave,  
- asegurar trazabilidad completa,  
- permitir consultas sobre predicción vs realidad,  
- habilitar el loop de certificación continua a nivel de datos.

---

## 2. Alcance

Incluye:

- Modelo relacional mínimo (RDBMS, p.ej. PostgreSQL)  
- Entidades maestras: `SYSTEM_PRODUCT`, `AM`, `DV`, `DPP`, `OM_EVENT`, `OAV`, `DT_SNAPSHOT`  
- Puntos de anclaje para UTCS, ATA 95 y DPP  
- Vistas lógicas para explotación (BI, analítica, certificación)

No incluye:

- Detalle de tablas auxiliares por ATA específico  
- Esquemas físicos de particionado, índices o tuning  
- Especificación de pipelines ETL

---

## 3. Entidades Principales

### 3.1 SYSTEM_PRODUCT

**Rol:** Representa *"qué soy"* a nivel de sistema / producto.

Campos clave (lógicos):

- `id` (UUID) — Identificador interno  
- `code` — Código humano legible (`Q100`, `WTCU01`, `FCC01`, `FC_PitchStab_NN`)  
- `name` — Nombre descriptivo  
- `type` — `aircraft`, `lru`, `nn_model`, `dataset`, `subsystem`, etc.  
- `primary_ata` — Capítulo ATA principal  
- `created_at`, `updated_at`

Ancla:

- Es el nodo raíz para AM, DPP, OM y DT.

---

### 3.2 AM_BASELINE

**Rol:** Modelo / manual del sistema **at rest** (ontología estática).

Campos clave:

- `id` (UUID)  
- `system_id` → FK a `SYSTEM_PRODUCT`  
- `version` — Versión de AM (p.ej. `AM_Q100_R01`)  
- `status` — `Draft`, `Approved`, `Retired`  
- `document_ref` — Ruta a repositorio (Git, S1000D, etc.)  
- `metadata` (JSONB) — Campos adicionales (autor, fecha, LC, etc.)

Ancla:

- Punto de partida para **DV (Design Validation)**.  

---

### 3.3 DESIGN_VALIDATION (DV)

**Rol:** Capa de **validación por diseño** que convierte AM en DPP confiable.

Campos clave:

- `id` (UUID)  
- `am_id` → FK a `AM_BASELINE`  
- `dv_status` — `Passed`, `ConditionallyPassed`, `Failed`  
- `dv_report_ref` — Informe DV  
- `dv_metrics` (JSONB) — Cobertura, completitud, checks, ratios  
- `performed_at`, `performed_by`

Ancla:

- `DV` es el **filtro** entre AM y DPP.

---

### 3.4 DPP_RECORD

**Rol:** Registro de **Digital Product Passport soberano** (ontología predictiva).

Campos clave:

- `id` (UUID)  
- `dpp_id` (STRING) — ID humano (`DPP_95-20_FC_PitchStability_v1.2`)  
- `system_id` → `SYSTEM_PRODUCT`  
- `am_id` → `AM_BASELINE`  
- `dv_id` → `DESIGN_VALIDATION`  
- `primary_ata`  
- `related_ata_chapters` (array) — Otros ATA relevantes  
- `status` — `Draft`, `Certified`, `InService`, `Retired`  
- `lifecycle_stage` — `Design`, `In-Service`, `Deprecated`, etc.  
- `dpp_json` (JSONB) — Payload completo del DPP  
- `created_at`, `updated_at`

Ancla:

- **DPP predice el OM**.  
- Punto de entrada para CCert/CVal.

---

### 3.5 OM_EVENT

**Rol:** Instancia de **Ontological Mission**: operación real del sistema en contexto único.

Campos clave:

- `id` (UUID)  
- `system_id` → `SYSTEM_PRODUCT`  
- `dpp_id` → `DPP_RECORD` (qué predicción le aplica)  
- `context_id` (opcional) — FK a una tabla de contexto operacional (aeropuerto, meteo, flight phase…)  
- `flight_id` — Identificador de vuelo / misión / campaña  
- `timestamp_start`, `timestamp_end`  
- `om_data` (JSONB) — KPI resumidos: latencias, errores, estados, eventos  
- `created_at`

Ancla:

- Cada `OM_EVENT` es **una realización concreta del OM**.  
- Es donde la predicción se confronta con la realidad.

---

### 3.6 OAV_CAMPAIGN

**Rol:** **On-Aircraft Validation** — campañas que agrupan múltiples OM_EVENT para validar el DPP en aeronave.

Campos clave:

- `id` (UUID)  
- `dpp_id` → `DPP_RECORD`  
- `name` — Nombre de campaña (`OAV_FC_Pitch_Q100_Phase2`)  
- `status` — `Planned`, `Running`, `Completed`, `Closed`  
- `objectives` — Texto libre  
- `criteria` (JSONB) — Qué significa "validado" (umbrales, KPIs, escenarios)  
- `result` (JSONB) — Resultado agregado: `passed`, `partial`, `failed`, findings  
- `created_at`, `completed_at`

Vínculo:

- Tabla intermedia `OAV_EVENT_LINK` asocia campaña ↔ eventos OM.

---

### 3.7 DT_SNAPSHOT

**Rol:** **Gemelo digital ontogenético** en un instante dado.

Campos clave:

- `id` (UUID)  
- `system_id` → `SYSTEM_PRODUCT`  
- `dpp_id` → `DPP_RECORD`  
- `source_oav_id` → `OAV_CAMPAIGN`  
- `version_tag` — Versión/tag del DT  
- `dt_state` (JSONB) — Estado condensado (modelos, parámetros, curvas, anomalías, historial)  
- `created_at`

Ancla:

- El DT es el **resultado acumulado** de OM + OAV.  
- Alimenta la actualización hacia **AM'** y el siguiente ciclo.

---

## 4. Relación con el Loop CCert / CVal

El modelo de datos soporta explícitamente el loop:

```text
SYSTEM_PRODUCT
   ↓
AM_BASELINE
   ↓ DV (Design Validation)
DPP_RECORD
   ↓ predice
OM_EVENT
   ↓ agrupa / evalúa
OAV_CAMPAIGN
   ↓ sintetiza
DT_SNAPSHOT
   ↓ actualiza
( AM_BASELINE' / nuevo ciclo DV → DPP' → ... )
```

* **CCert** = capacidad de reconstruir y demostrar este ciclo
* **CVal** = capacidad de generar evidencia continua a partir de OM_EVENT + OAV_CAMPAIGN

---

## 5. Vistas recomendadas

Para explotación práctica, se sugieren vistas lógicas:

1. **vw_dpp_status**

   * DPP + estado + última campaña OAV + último DT asociado.

2. **vw_system_cert_status**

   * Por `system_product`, resumen de:

     * AM vigente
     * DPP vigente
     * campañas OAV completadas
     * DT actual

3. **vw_om_vs_dpp**

   * Comparación de predicciones DPP vs métricas reales OM (latencias, accuracies, envelopes violados).

---

## 6. Assets asociados (95-90-02 / ASSETS)

Los siguientes ficheros se proponen como artefactos de soporte en `ASSETS/`:

* **95-90-02-007-A-001_CCert_CVal_Core_Tables.csv**

  * Lista tabular de entidades, campos, tipos lógicos, notas.

* **95-90-02-007-A-002_CCert_CVal_ER_Diagram.drawio**

  * Diagrama entidad–relación (SYSTEM_PRODUCT, AM, DV, DPP, OM, OAV, DT).

* **95-90-02-007-A-003_CCert_CVal_Graph_Model.drawio**

  * Modelo grafo (nodos y relaciones) para Neo4j / grafo UTCS.

* **95-90-02-007-A-004_CCert_CVal_JSON_Schema_Examples.json**

  * Ejemplos de payload JSONB (`dpp_json`, `om_data`, `dt_state`).

Estos assets complementan el presente documento como **referencia global de esquema de datos**.

---

## 7. Referencias internas

* [95-00-01-007_DPP_Data_Model_and_Identifiers.md](../../95-00_GENERAL/95-00-01_Overview/)
* [95-00-03_Requirements/](../../95-00_GENERAL/95-00-03_Requirements/)
* [95-00-07_V_AND_V/](../../95-00_GENERAL/95-00-07_V_AND_V/)
* [95-10_Operations/](../../95-10_Operations/)
* [95-90-01_Global_Reference_Taxonomies/](../95-90-01_Global_Reference_Taxonomies/)
* [95-90-02-006_CCert_CVal_Database_Schema.md](./95-90-02-006_CCert_CVal_Database_Schema.md) — Detailed PostgreSQL/Neo4j implementation

---

## 8. Control de cambios

| Versión | Fecha      | Autor                | Descripción                       |
| ------- | ---------- | -------------------- | --------------------------------- |
| 1.0     | 2025-12-13 | AMPEL360 / ATA 95 WG | Versión inicial — Core Data Model |

---

## 9. Document Control

- Generated by: AI (prompted by Amedeo Pelliccia); pending approval by [Approver]
- **Status**: WORKING – Subject to review and approval
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
- **Sub-bucket**: 02_Global_Data_Schemas
- **Document ID**: 95-90-02-007
- **Last AI update**: 2025-12-13

---

**End of Document**
