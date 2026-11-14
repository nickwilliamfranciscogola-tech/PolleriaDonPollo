# Análisis de impacto — CR-001

## Alcance
- 1 RF nuevo (RF-10) y 2 modificados (RF-07, RF-08); RF-09 revisado sin cambio.
- 1 CU nuevo (CU-10) y 2 modificados (CU-07, CU-08); 2 HU nuevas (HU-15, HU-16).
- 2 clases nuevas (CLS-10, CLS-11) y 2 modificadas (CLS-07, CLS-08).
- 4 pruebas nuevas (PR-11 a PR-14) y 3 de regresión (PR-07, PR-08, PR-09).

## Tiempo (estimación del equipo)
| Actividad | Horas |
|---|---|
| Actualizar SRS, CU e HU | 3 |
| Actualizar modelos en Modelio (clases y actividad) | 3 |
| Implementar CLS-10, CLS-11 y ajustar CLS-07/08 | 8 |
| Diseñar y ejecutar PR-11 a PR-14 y regresión | 5 |
| Trazabilidad, reporte, repositorio y revisión | 3 |
| **Total** | **22** (≈ 3 días hábiles) |

## Calidad
Se mantiene 100 % de cobertura RF→CU→Clase→Prueba. Se agregan pruebas de regresión del cobro.

## Riesgos y mitigación
| ID | Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|---|
| R5 | Dependencia de medios de pago (existente) | Media | Alto | Interfaz desacoplada `PasarelaBilletera` y simulador |
| R9 | Billetera sin respuesta o con confirmación tardía | Media | Alto | Tiempo máximo de 120 s y reutilización de E2 (PR-12) |
| R10 | Comprobante inconsistente con el medio de pago | Baja | Medio | PR-14 y checklist de coherencia |
| R11 | Reembolso a billetera no definido | Media | Medio | Diferido a v1.2; reembolso manual documentado |
