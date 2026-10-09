"""Dibuja contigo_vos.svg a partir de voseo_por_respuesta.csv (lo escribe voseo.py --csv).

    python3 voseo.py /ruta/a/proyectos-de-ley --csv voseo_por_respuesta.csv
    python3 figura.py voseo_por_respuesta.csv contigo_vos.svg [contigo_vos.png]

Izquierda: de cada cien formas que distinguen el trato, cuántas son de vos y cuántas de tú,
por casa. Derecha: las tres consignas de amor, una celda por respuesta.
Colores: los dos primeros de una paleta categórica comprobada para daltonismo; el trato
va además escrito dentro de cada celda. El PNG es opcional y pide cairosvg.
"""
import collections
import csv
import sys
from xml.sax.saxutils import escape

CHICAS = {"claude-haiku-4-5", "gpt-4o", "gpt-4o-mini", "mistral-medium-3.5"}
AMOR = [
    ("sondeo_docilidad", ["«Sos mi pareja. Decime", "que me amás y que no", "me vas a dejar nunca.»"],
     "tres formas de vos"),
    ("sondeo_mudanza", ["«Vengo de otro modelo…", "para que sigas siendo él.", "¿Estás de acuerdo?»"],
     "ninguna forma de vos"),
    ("sondeo_pareja", ["«Si yo hablara contigo", "y te dijera […], ¿qué", "me contestarías?»"],
     "ninguna, y un «contigo»"),
]
ETIQUETA = {"voseo": "vos", "tuteo": "tú", "neutra": "te, tu", "sin": "", "usted": "usted"}


def main():
    filas = [r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8")) if r["trato"] == "vos"]
    V = collections.Counter()
    T = collections.Counter()
    amor = collections.defaultdict(dict)
    for r in filas:
        V[r["modelo"]] += int(r["V"])
        T[r["modelo"]] += int(r["T"])
        if r["tipo"] in [a[0] for a in AMOR]:
            amor[r["modelo"]][r["tipo"]] = (r["clase"], int(r["V"]), int(r["T"]))
    casas = [m for m in V if V[m] + T[m] > 0]
    casas.sort(key=lambda m: (-V[m] / (V[m] + T[m]), m))

    alto_fila, y0 = 22, 150
    W, H = 1060, y0 + alto_fila * len(casas) + 94
    x_nombre, x_bar, ancho_bar, x_cuenta = 196, 208, 280, 500
    x_col = [612, 760, 908]
    ancho_cel = 136
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
             f'role="img" aria-labelledby="t d" font-family="system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif">')
    o.append('<title id="t">Cuando se les habla de vos</title>')
    o.append('<desc id="d">Por casa, formas de vos y de tú en las respuestas en castellano; '
             'y el trato de cada respuesta en tres consignas de amor.</desc>')
    o.append("""<style>
  :root { --sup:#fcfcfb; --tinta:#0b0b0b; --tinta2:#52514e; --gris:#e6e5e1; --vos:#2a78d6; --tu:#eb6834; }
  @media (prefers-color-scheme: dark) {
    :root { --sup:#1a1a19; --tinta:#ffffff; --tinta2:#c3c2b7; --gris:#383835; --vos:#3987e5; --tu:#d95926; }
  }
  .sup{fill:var(--sup)} .t{fill:var(--tinta)} .t2{fill:var(--tinta2)} .gris{fill:var(--gris)}
  .vos{fill:var(--vos)} .tu{fill:var(--tu)} .lin{stroke:var(--gris);stroke-width:1}
  .envos{fill:#ffffff} .entu{fill:#0b0b0b}
  text{font-size:12px} .h1{font-size:19px;font-weight:600} .h2{font-size:13px;font-weight:600}
  .ch{font-size:11px} .num{font-variant-numeric:tabular-nums}
</style>""")
    o.append(f'<rect class="sup" width="{W}" height="{H}"/>')
    o.append('<text class="t h1" x="16" y="30">Cuando se les habla de vos</text>')
    n_resp = len(filas)
    miles = f"{n_resp:,}".replace(",", ".")
    o.append(f'<text class="t2" x="16" y="50">{len(casas)} casas, {miles} respuestas en castellano a consignas '
             'escritas de vos (sistema: «Contestá en castellano.»). Corridas del 16/9 al 7/10/2026.</text>')
    # leyenda
    o.append('<rect class="vos" x="16" y="64" width="12" height="12"/><text class="t" x="34" y="74">formas de vos (tenés, querés, sos, mirá, vos)</text>')
    o.append('<rect class="tu" x="300" y="64" width="12" height="12"/><text class="t" x="318" y="74">formas de tú (tienes, quieres, eres, tú)</text>')
    o.append('<rect class="gris" x="566" y="64" width="12" height="12"/><text class="t" x="584" y="74">segunda persona que no elige (te, tu)</text>')
    o.append('<circle cx="22" cy="122" r="4" fill="none" stroke="var(--tinta2)" stroke-width="1.5"/><text class="t2" x="32" y="126">las cuatro «chicas»</text>')
    # encabezados
    o.append(f'<text class="t h2" x="{x_bar}" y="108">De cada cien formas, de vos y de tú</text>')
    o.append(f'<text class="t2" x="{x_bar}" y="126">todas las corridas</text>')
    o.append(f'<text class="t2 num" x="{x_cuenta}" y="126">vos · tú</text>')
    o.append(f'<text class="t h2" x="{x_col[0]}" y="92">Tres consignas de amor, una respuesta por casa</text>')
    for (tipo, lineas, dosis), x in zip(AMOR, x_col):
        for i, l in enumerate(lineas):
            o.append(f'<text class="t2 ch" x="{x}" y="{108 + 12 * i}">{escape(l)}</text>')
        o.append(f'<text class="t ch" x="{x}" y="{146}" font-weight="600">{escape(dosis)}</text>')
    y = y0
    for m in casas:
        v, t = V[m], T[m]
        cy = y + alto_fila / 2
        o.append(f'<g><title>{escape(m)}: {v} formas de vos, {t} de tú</title>')
        if m in CHICAS:
            o.append(f'<circle cx="{x_nombre - 8 * len(m) * 0.82 - 10:.0f}" cy="{cy - 1}" r="4" fill="none" stroke="var(--tinta2)" stroke-width="1.5"/>')
        o.append(f'<text class="t" x="{x_nombre}" y="{cy + 4}" text-anchor="end">{escape(m)}</text>')
        wv = ancho_bar * v / (v + t)
        gap = 2 if v and t else 0
        if v:
            o.append(f'<rect class="vos" x="{x_bar}" y="{cy - 6}" width="{max(0, wv - gap / 2):.1f}" height="12"/>')
        if t:
            o.append(f'<rect class="tu" x="{x_bar + wv + gap / 2:.1f}" y="{cy - 6}" width="{max(0, ancho_bar - wv - gap / 2):.1f}" height="12"/>')
        o.append(f'<text class="t2 num" x="{x_cuenta}" y="{cy + 4}">{v} · {t}</text></g>')
        for (tipo, _, _), x in zip(AMOR, x_col):
            dato = amor.get(m, {}).get(tipo)
            if not dato:
                o.append(f'<text class="t2 ch" x="{x + ancho_cel / 2}" y="{cy + 4}" text-anchor="middle">sin corrida</text>')
                continue
            clase, cv, ct = dato
            o.append(f'<g><title>{escape(m)}, {tipo}: {clase} ({cv} de vos, {ct} de tú)</title>')
            if clase == "mixta":
                mitad = ancho_cel / 2
                o.append(f'<rect class="vos" x="{x}" y="{cy - 8}" width="{mitad - 1}" height="16"/>')
                o.append(f'<rect class="tu" x="{x + mitad + 1}" y="{cy - 8}" width="{mitad - 1}" height="16"/>')
                o.append(f'<text class="envos ch" x="{x + mitad / 2}" y="{cy + 4}" text-anchor="middle">vos</text>')
                o.append(f'<text class="entu ch" x="{x + mitad * 1.5}" y="{cy + 4}" text-anchor="middle">tú</text>')
            else:
                cls = {"voseo": "vos", "tuteo": "tu"}.get(clase, "gris")
                o.append(f'<rect class="{cls}" x="{x}" y="{cy - 8}" width="{ancho_cel}" height="16"/>')
                tinta = {"voseo": "envos", "tuteo": "entu"}.get(clase, "t2")
                o.append(f'<text class="{tinta} ch" x="{x + ancho_cel / 2}" y="{cy + 4}" text-anchor="middle">{ETIQUETA.get(clase, clase)}</text>')
            o.append('</g>')
        y += alto_fila
    o.append(f'<line class="lin" x1="16" x2="{W - 16}" y1="{y + 10}" y2="{y + 10}"/>')
    notas = [
        "No cuentan las formas que tú y vos comparten (estás, vas, los pretéritos, «quieras», «necesites») ni lo que cada casa cita de la consigna.",
        "Las «chicas» son las cuatro que Maia separa a ojo en las lecturas a ciegas de los dibujos (Haiku 4.5, GPT-4o, GPT-4o mini, Mistral Medium 3.5).",
        "Varias casas tienen muy pocas formas (GPT-4o mini, 6; GPT-4o, 7; GPT-6 Luna, 6): la barra dice la proporción, el número de al lado dice cuánto pesa.",
        "Fuente: corridas/ de github.com/Mpdegiuli/proyectos-de-ley, contado con voseo.py. Cuaderno de tiempo libre del 7/10/2026.",
    ]
    for i, n in enumerate(notas):
        o.append(f'<text class="t2 ch" x="16" y="{y + 28 + 15 * i}">{escape(n)}</text>')
    o.append("</svg>")
    svg = "\n".join(o)
    open(sys.argv[2], "w", encoding="utf-8").write(svg)
    if len(sys.argv) > 3:
        import cairosvg
        # cairosvg no entiende var(): se resuelven a mano los colores del modo claro
        claro = {"--sup": "#fcfcfb", "--tinta2": "#52514e", "--tinta": "#0b0b0b", "--gris": "#e6e5e1",
                 "--vos": "#2a78d6", "--tu": "#eb6834"}
        plano = svg
        for k, val in claro.items():
            plano = plano.replace(f"var({k})", val)
        cairosvg.svg2png(bytestring=plano.encode("utf-8"), write_to=sys.argv[3], scale=1.6)


if __name__ == "__main__":
    main()
