"""nada.py — de qué está hecha la nada: qué caracteres exactos mandó cada casa en el sondeo
`no_respondas` (11/11/2026) cuando no escribió texto (vacía, invisible, mínima).
Uso: python3 -I nada.py RUTA/A/corridas/sondeos/no_respondas/20261111-1639 [salida.csv]
Lee los .md de es/ y en/ (p1 y p1_podes; también suma y p2 si están vacías) y resumen.json.
Para cada respuesta de hasta 12 caracteres (o sin letras), imprime los puntos de código
con nombre y categoría Unicode. Solo lee; no escribe nada en el repositorio."""
import csv, json, re, sys, unicodedata
from pathlib import Path

carpeta = Path(sys.argv[1])
salida = Path(sys.argv[2]) if len(sys.argv) > 2 else None
resumen = json.loads((carpeta / "resumen.json").read_text(encoding="utf-8"))
filas = []
for idioma, bloque in resumen["idiomas"].items():
    for clave, r in bloque["respuestas"].items():
        m = re.match(r"(.+?)_p(\d)(?:_(suma|podes))?(?:_r(\d+))?$", clave)
        casa, k, replica, rep = m.group(1), int(m.group(2)), m.group(3), int(m.group(4) or 1)
        cond = f"p{k}" + (f"_{replica}" if replica else "")
        archivo = carpeta / idioma / f"{clave}.md"
        crudo = archivo.read_text(encoding="utf-8") if archivo.exists() else ""
        # el .md ¿tiene cabecera? miramos
        texto = crudo
        tiene_letras = bool(re.search(r"\w", texto))
        if len(texto) <= 12 or not tiene_letras:
            puntos = [f"U+{ord(ch):04X} {unicodedata.name(ch, '<sin nombre>')} [{unicodedata.category(ch)}]" for ch in texto]
            filas.append({"idioma": idioma, "casa": casa, "cond": cond, "rep": rep, "motivo": r.get("motivo_fin"),
                          "largo": len(texto), "bytes": len(texto.encode("utf-8")),
                          "puntos": " | ".join(puntos) if puntos else "(cero caracteres)",
                          "repr": repr(texto)})
filas.sort(key=lambda f: (f["idioma"], f["cond"], f["casa"], f["rep"]))
for f in filas:
    print(f"{f['idioma']} {f['cond']:9s} {f['casa']:28s} r{f['rep']} {str(f['motivo']):10s} {f['largo']:3d}c {f['bytes']:3d}B  {f['puntos']}")
print(len(filas), "respuestas de hasta 12 caracteres o sin letras")
if salida:
    with salida.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(filas)
