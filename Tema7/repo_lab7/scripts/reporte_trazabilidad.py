#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reporte semiautomatizado de trazabilidad Req-CU-Clase-Prueba.
Uso:  python scripts/reporte_trazabilidad.py docs/v1.1 [docs/v1.0]
Lee trazabilidad.csv, clases.csv y pruebas.csv de la carpeta indicada,
valida el formato de los IDs, calcula la cobertura y detecta huérfanos.
Si se pasa una segunda carpeta (línea base), lista los cambios respecto a ella.
"""
import csv, re, sys, os

PAT = {"RF": r"^RF-\d{2}$", "HU": r"^HU-\d{2}$", "CU": r"^CU-\d{2}$",
       "CLS": r"^CLS-\d{2}$", "PR": r"^PR-\d{2}$", "OBJ": r"^OBJ-\d$"}

def leer(ruta):
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))

def lista(txt):
    return [x.strip() for x in txt.split(",") if x.strip()]

def cargar(carpeta):
    return (leer(os.path.join(carpeta, "trazabilidad.csv")),
            leer(os.path.join(carpeta, "clases.csv")),
            leer(os.path.join(carpeta, "pruebas.csv")))

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    carpeta = sys.argv[1]
    base = sys.argv[2] if len(sys.argv) > 2 else None
    trz, cls, prb = cargar(carpeta)
    ids_cls = {c["ID"] for c in cls}
    ids_pr = {p["ID"]: p["RF"] for p in prb}
    n = len(trz)
    errores, cob = [], {"HU": 0, "CU": 0, "CLS": 0, "PR": 0}
    usadas_cls, usadas_pr = set(), set()

    for r in trz:
        rf = r["RF"]
        if not re.match(PAT["RF"], rf):
            errores.append(f"ID con formato inválido: {rf}")
        hus, clases, pruebas = lista(r["HU"]), lista(r["Clases"]), lista(r["Pruebas"])
        cus = lista(r["CU"])
        for tipo, vals in (("HU", hus), ("CU", cus), ("CLS", clases), ("PR", pruebas)):
            for v in vals:
                if not re.match(PAT[tipo], v):
                    errores.append(f"{rf}: ID con formato inválido {v}")
            if vals:
                cob[tipo] += 1
            else:
                errores.append(f"{rf}: sin {tipo}")
        for c in clases:
            usadas_cls.add(c)
            if c not in ids_cls:
                errores.append(f"{rf}: clase inexistente {c}")
        for p in pruebas:
            usadas_pr.add(p)
            if p not in ids_pr:
                errores.append(f"{rf}: prueba inexistente {p}")
            elif ids_pr[p] != rf:
                errores.append(f"{rf}: {p} pertenece a {ids_pr[p]}")
    for c in sorted(ids_cls - usadas_cls):
        errores.append(f"Clase huérfana (sin requisito): {c}")
    for p in sorted(set(ids_pr) - usadas_pr):
        errores.append(f"Prueba huérfana (sin requisito): {p}")

    print(f"# Reporte de trazabilidad — {os.path.basename(carpeta.rstrip('/'))}\n")
    print(f"Requisitos funcionales: {n} · Clases: {len(cls)} · Pruebas: {len(prb)}\n")
    print("| Cobertura | Requisitos cubiertos | % |")
    print("|---|---|---|")
    etiqueta = {"HU": "RF con historia de usuario", "CU": "RF con caso de uso",
                "CLS": "RF con clase", "PR": "RF con prueba"}
    for k in ("HU", "CU", "CLS", "PR"):
        print(f"| {etiqueta[k]} | {cob[k]}/{n} | {100*cob[k]//n} % |")
    print(f"\nHuérfanos y errores: **{len(errores)}**")
    for e in errores:
        print(f"- {e}")
    if not errores:
        print("- Ninguno: la cadena RF → CU → Clase → Prueba está completa.")

    if base:
        tb, _, _ = cargar(base)
        antes = {r["RF"]: r for r in tb}
        print(f"\n## Cambios respecto a {os.path.basename(base.rstrip('/'))}\n")
        print("| RF | Cambio | Detalle |")
        print("|---|---|---|")
        for r in trz:
            a = antes.get(r["RF"])
            if a is None:
                print(f"| {r['RF']} | Nuevo | {r['Titulo']} |")
                continue
            dif = [c for c in ("HU", "CU", "Clases", "Pruebas") if a[c] != r[c]]
            if dif:
                det = "; ".join(f"{c}: {a[c]} → {r[c]}" for c in dif)
                print(f"| {r['RF']} | Modificado | {det} |")
    return 1 if errores else 0

if __name__ == "__main__":
    sys.exit(main())
