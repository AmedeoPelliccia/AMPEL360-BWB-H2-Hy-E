
# 95-20-21 — Test Logs Directory  
### ECS Neural Network Subsystem (NN_ECS)

**Path**: `ASSETS/Reports/95-20-21-Test_Logs/`  
**Subsystem**: 95-20-21 NN_ECS  
**Type**: Test Execution Logs  
**Status**: WORKING  

---

## 1. Purpose

This directory stores **raw and processed test execution logs** for the ECS Neural Network Subsystem (95-20-21 NN_ECS), providing:

- Evidence for the **Verification Report**  
  → [`../95-20-21-Verification_Report.md`](../95-20-21-Verification_Report.md)  
- Support for the **Coverage Summary**  
  → [`../95-20-21-Coverage_Summary.md`](../95-20-21-Coverage_Summary.md)  
- Traceability to requirements (HLR / LLR) and test cases  
  → `../../../TRACE/95-20-21-TRACE.csv`  

These logs are **certification evidence** and must be:

- Immutable once baselined  
- Under configuration control (see SCMP)  
- Clearly identified by test type, model, and version  

---

## 2. Directory Structure

```text
ASSETS/Reports/95-20-21-Test_Logs/
├── README.md                          # This file
├── Unit/
│   ├── 95-20-21-TL-UNIT_A-101_v1.2.log
│   ├── 95-20-21-TL-UNIT_A-102_v1.0.log
│   └── ...
├── Integration/
│   ├── 95-20-21-TL-INT_ECS_Pipeline_v1.0.log
│   └── ...
├── System/
│   ├── 95-20-21-TL-SYS_ECS_DT_Scenarios_v3.2.log
│   └── ...
├── Robustness/
│   ├── 95-20-21-TL-ROB_Noise_and_Faults.log
│   └── ...
├── Timing/
│   ├── 95-20-21-TL-TIMING_A-101_v1.2.log
│   ├── 95-20-21-TL-TIMING_A-102_v1.0.log
│   └── ...
└── Regression/
    ├── 95-20-21-TL-REG_A-101_v1.2_vs_v1.1.log
    └── ...
````

> Los nombres de fichero son una **convención**, no un requisito rígido, pero deben permitir identificar:
> `Subsystem` – `Type` – `ModelID` – `Version`.

---

## 3. File Naming Convention

Formato recomendado:

```text
95-20-21-TL-<CATEGORY>_<TARGET>_v<MAJOR>.<MINOR>.log
```

* `TL` → Test Log
* `<CATEGORY>` → `UNIT`, `INT`, `SYS`, `ROB`, `TIMING`, `REG`
* `<TARGET>` → modelo o pipeline (`A-101`, `A-102`, `ECS_Pipeline`, etc.)
* `v<MAJOR>.<MINOR>` → versión del modelo / software bajo prueba

Ejemplos:

* `95-20-21-TL-UNIT_A-101_v1.2.log`
* `95-20-21-TL-TIMING_A-101_v1.2.log`
* `95-20-21-TL-SYS_ECS_DT_Scenarios_v3.2.log`

---

## 4. Recommended Log Content

Cada log debería incluir como mínimo:

1. **Header de contexto**

   ```text
   Subsystem: 95-20-21 NN_ECS
   Model: A-101 – Cabin Temperature Predictor
   Model Version: v1.2
   ONNX File: Models/Trained/temp_predictor_v1.2.onnx
   Test Category: TIMING
   Test Tool: onnxruntime / custom timing harness
   Test Date (UTC): 2025-11-19T12:34:56Z
   Test Campaign ID: ECS-TIMING-2025-11-B01
   ```

2. **Configuración de entorno**

   * Hardware / IMA partition (si aplica)
   * Versiones de runtime / libs
   * Semillas de aleatoriedad (para reproducibilidad)

3. **Listado de casos ejecutados**

   * ID de caso de prueba (linkeable a `TRACE.csv`)
   * Resultado: PASS / FAIL / SKIP
   * Evidencia clave (p.ej. latencias, temperaturas)

4. **Resumen de resultados**

   * Número de casos ejecutados
   * Número de PASS / FAIL
   * Umbrales vs valores medidos
   * Comentarios / anomalías

---

## 5. Traceability

Cada log debe referenciar:

* Requisitos ejercitados → IDs de HLR/LLR de
  → `../../../Certification/95-20-21-SRS.md`
* Test cases → IDs en
  → `../../../TRACE/95-20-21-TRACE.csv`
* Informe agregado →
  → `../95-20-21-Verification_Report.md`
  → `../95-20-21-Coverage_Summary.md`

Ejemplo dentro del log:

```text
Requirements: HLR-101, HLR-102, LLR-001, LLR-004
Trace Rows: TRACE IDs 1201–1210
Aggregated In: 95-20-21-Verification_Report.md §4.2, §7
```

---

## 6. Configuration Management

Este directorio está bajo el control de:

* [`../../../Certification/95-20-21-SCMP.md`](../../../Certification/95-20-21-SCMP.md)

Política recomendada:

* Los logs de campañas **baselined** no se modifican.
* Nuevas campañas → nuevos ficheros de log (no sobrescribir).
* Cambios se gestionan mediante Pull Requests con revisión de **Verification** + **Safety**.

---

## 7. Document Control

* **Document**: `ASSETS/Reports/95-20-21-Test_Logs/README.md`
* **Status**: WORKING
* **Owner**: AMPEL360 Verification Team
* **AI Assistance**: Drafted with AI assistance (ChatGPT), prompted by **Amedeo Pelliccia**; subject to human review and formal approval.

