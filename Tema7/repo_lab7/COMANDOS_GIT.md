# Comandos Git — Laboratorio 7 (ejecutar en la carpeta del repositorio clonado)

> Estado del remoto al preparar este laboratorio: solo rama `main` y 4 archivos
> (README.md, laboratorio 6.docx, Prueba 1.png, Prueba 2.png); **no hay tags**.

```bash
git clone https://github.com/nickwilliamfranciscogola-tech/PolleriaDonPollo.git
cd PolleriaDonPollo
git config user.name "Nick William Francisco Gola"
git config user.email "TU_CORREO_DE_GITHUB"
```

## 1) Línea base v1.0 (Paso 2)
Copia al repo las carpetas `docs/` y `scripts/` de este paquete y luego **borra** de `docs/` lo que es de v1.1:
`docs/v1.1`, `docs/cambios`, `docs/revision` (se agregan después, en la rama del CR).
Deja `docs/v1.0`, `docs/gestion-cambios` y `docs/glosario.md` sin las filas marcadas v1.1 si quieres una línea base «pura».

```bash
git add docs/v1.0 docs/gestion-cambios docs/glosario.md scripts
git commit -m "docs(baseline): linea base v1.0 con SRS, clases, pruebas y matriz [RF-01..RF-09]"
git tag -a v1.0 -m "Linea base v1.0 (Lab 6: Vision, SRS breve, UML)"
git push origin main --tags
```

## 2) Registrar el CR en GitHub (Paso 4)
En GitHub → *Issues* → *New issue*: título `CR-001 Pago con billetera digital (Yape/Plin)`, pega el contenido de `docs/cambios/CR-001.md`.
Crea otro issue `CR-002 ...` y ciérralo con la etiqueta *wontfix* (rechazado).

## 3) Rama del cambio (Pasos 5 y 6)
```bash
git switch -c cr/CR-001-pago-billetera
git add docs/cambios
git commit -m "docs(cambios): registra CR-001 aprobado y CR-002 rechazado, con analisis de impacto [CR-001]"
git add docs/v1.1/srs-breve.md docs/v1.1/casos-uso.md docs/glosario.md
git commit -m "docs(srs): agrega RF-10, CU-10, HU-15/16 y modifica RF-07/RF-08 [CR-001]"
git add docs/v1.1/clases.md docs/v1.1/clases.csv docs/v1.1/pruebas.md docs/v1.1/pruebas.csv
git commit -m "model(clases): agrega CLS-10/11 y pruebas PR-11..PR-14 [CR-001]"
git add docs/v1.1/trazabilidad.csv docs/v1.1/reporte-cobertura.md
git commit -m "docs(trazabilidad): matriz v1.1 y reporte de cobertura 100% [CR-001]"
git push -u origin cr/CR-001-pago-billetera
```

## 4) Reporte semiautomatizado (Paso 7)
```bash
python scripts/reporte_trazabilidad.py docs/v1.1 docs/v1.0
```

## 5) Pull Request y revisión por pares (Paso 8)
En GitHub: *Compare & pull request* → título `CR-001 ...`, descripción `Closes #1`, asigna a tu compañero como *Reviewer*.
Cuando apruebe, agrega `docs/revision/revision-pares-v1.1.md` (con su nombre) y haz *Merge*.

## 6) Publicar v1.1 (Paso 9)
```bash
git switch main && git pull
git tag -a v1.1 -m "v1.1: CR-001 pago con billetera digital (RF-10, CU-10, CLS-10/11, PR-11..PR-14)"
git push origin v1.1
git log --oneline --decorate -8
```
