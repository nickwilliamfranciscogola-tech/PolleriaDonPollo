# Convención de identificadores (formato único)

| Artefacto | Formato | Ejemplo | Regla |
|---|---|---|---|
| Objetivo | `OBJ-n` | OBJ-3 | Definido en la Visión |
| Requisito funcional | `RF-nn` | RF-07 | Un RF nunca cambia de número; si se elimina, queda «Retirado» |
| Historia de usuario | `HU-nn` | HU-15 | Se asocia a uno o más RF |
| Caso de uso | `CU-nn` | CU-10 | Mismo número que el RF que lo origina cuando es 1:1 |
| Clase | `CLS-nn` | CLS-10 | Nombre en PascalCase en el modelo (Modelio) |
| Prueba | `PR-nn` | PR-11 | Cada PR referencia exactamente un RF |
| Solicitud de cambio | `CR-nnn` | CR-001 | Una por Issue de GitHub |
| Riesgo | `Rn` | R9 | Continúa la numeración del plan de riesgos |
| Hallazgo de revisión | `Hn` | H6 | Continúa la numeración del Lab 6 |
| Evidencia | `E-nn` | E-07 | Se cita en el PDF con sus IDs |
| Etiqueta (tag) | `vX.Y` | v1.1 | v1.0 = línea base; v1.1 = cambios aprobados |

## Convenciones de Git
- Ramas: `main` (estable) · `cr/CR-nnn-descripcion` (una por solicitud de cambio).
- Commits: `tipo(alcance): mensaje [ID]`, por ejemplo `docs(srs): agrega RF-10 [CR-001]`.
- Tipos: `docs`, `feat`, `test`, `model`, `chore`.
- Etiquetas anotadas: `git tag -a v1.1 -m "..."`.
