#!/usr/bin/env python3
"""El santoral en la costa: la costa patagónica con los nombres que el viaje de 1520 tomó del
calendario (y los que no), y al lado el año como rueda con esas mismas fechas.
Tiempo libre, 21/10/2026. Escribe costa_calendario.svg.

Datos de costa: Natural Earth, ne_50m_coastline (dominio público), bajado con
  git clone --filter=blob:none --no-checkout --depth 1 https://github.com/nvkelso/natural-earth-vector.git
  git show HEAD:50m_physical/ne_50m_coastline.{shp,shx,dbf}
Uso: python3 figura.py <carpeta con ne_50m_coastline.shp>   (pide: pip install pyshp)
Las posiciones de los lugares son aproximadas (a ojo sobre la carta, al décimo de grado): sirven
para ubicarlos en una figura de 460 px, no para navegar.
"""
import sys, math, datetime
import shapefile

CARPETA = sys.argv[1] if len(sys.argv) > 1 else "../ne"
W, H = 1040, 600
# Panel del mapa: lon -77..-52, lat -56,5..-33,5 (equirectangular con el ancho corregido por cos(45°))
LON0, LON1, LAT0, LAT1 = -77.0, -52.0, -56.5, -33.5
MX0, MY0, MH = 40, 50, 500
K = math.cos(math.radians(45))
ESC_LAT = MH / (LAT1 - LAT0)          # px por grado de latitud
ESC_LON = ESC_LAT * K                 # px por grado de longitud (a 45°S un grado de longitud mide cos 45° de uno de latitud)
MW = (LON1 - LON0) * ESC_LON
def xy(lon, lat):
    return MX0 + (lon - LON0) * ESC_LON, MY0 + (LAT1 - lat) * ESC_LAT

# Lugares (lon, lat), fecha de 1520, nombre, origen del nombre
CALENDARIO = "cal"; NECESIDAD = "nec"; COSA = "cosa"
LUGARES = [
    (-64.0, -41.9, (2, 24), "golfo San Matías", "san Matías, apóstol (24/2)", CALENDARIO),
    (-65.55, -44.9, (2, 27), "bahía de los Patos", "los pingüinos, que tomaron por patos", COSA),
    (-65.9, -47.75, (3, 15), "bahía de los Trabajos", "la tormenta (hoy Puerto Deseado)", COSA),
    (-67.72, -49.31, (3, 31), "puerto San Julián", "san Julián el Hospitalario, patrono de viajeros: lo que hacía falta para invernar", NECESIDAD),
    (-68.35, -50.13, (5, 3), "río Santa Cruz", "Invención de la Santa Cruz (3/5)", CALENDARIO),
    (-68.35, -52.33, (10, 21), "cabo de las Once Mil Vírgenes", "santa Úrsula y las once mil vírgenes (21/10)", CALENDARIO),
    (-69.6, -52.6, (11, 1), "estrecho de Todos los Santos", "Todos los Santos (1/11)", CALENDARIO),
    (-74.7, -52.75, (11, 28), "cabo Deseado", "el deseo de salir", NECESIDAD),
]
COLOR = {CALENDARIO: "#b8860b", NECESIDAD: "#1f77b4", COSA: "#7f7f7f"}
NOMBRE_TIPO = {CALENDARIO: "nombre del calendario (la fiesta del día)", NECESIDAD: "nombre de lo que hacía falta",
               COSA: "nombre de lo que vieron o sufrieron"}

def costa():
    sf = shapefile.Reader(f"{CARPETA}/ne_50m_coastline")
    trazos = []
    for sh in sf.shapes():
        pts = sh.points
        partes = list(sh.parts) + [len(pts)]
        for a, b in zip(partes[:-1], partes[1:]):
            seg = [(lon, lat) for lon, lat in pts[a:b] if LON0 - 1 <= lon <= LON1 + 1 and LAT0 - 1 <= lat <= LAT1 + 1]
            if len(seg) >= 2:
                trazos.append(seg)
    return trazos

def simplificar(pts, tol):
    """Douglas-Peucker en píxeles, para que el SVG quede chico (la costa a 50m trae más puntos de los que se ven)."""
    if len(pts) < 3:
        return pts
    (x0, y0), (x1, y1) = pts[0], pts[-1]
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    if L < 1e-9:   # anillo cerrado (una isla): se parte en dos mitades y se simplifica cada una
        m = len(pts) // 2
        return simplificar(pts[:m + 1], tol)[:-1] + simplificar(pts[m:], tol)
    imax, dmax = 0, -1.0
    for i in range(1, len(pts) - 1):
        px, py = pts[i]
        d = abs(dy * px - dx * py + x1 * y0 - y1 * x0) / L
        if d > dmax:
            imax, dmax = i, d
    if dmax > tol:
        return simplificar(pts[:imax + 1], tol)[:-1] + simplificar(pts[imax:], tol)
    return [pts[0], pts[-1]]

def rueda(cx, cy, r, mes, dia):
    d = datetime.date(1520, mes, dia).timetuple().tm_yday  # 1520 es bisiesto: 366 días
    ang = 2 * math.pi * (d - 1) / 366 - math.pi / 2
    return cx + r * math.cos(ang), cy + r * math.sin(ang), ang

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")

def main():
    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Georgia, serif">')
    out.append(f'<rect width="{W}" height="{H}" fill="#fbf8f1"/>')
    out.append(f'<text x="{MX0}" y="28" font-size="17" fill="#222">El santoral en la costa: los nombres de 1520 y de dónde salieron</text>')
    # mapa
    out.append(f'<clipPath id="mapa"><rect x="{MX0}" y="{MY0}" width="{MW}" height="{MH}"/></clipPath>')
    out.append(f'<rect x="{MX0}" y="{MY0}" width="{MW}" height="{MH}" fill="#eef3f7" stroke="#bbb"/>')
    out.append('<g clip-path="url(#mapa)" fill="none" stroke="#555" stroke-width="0.8">')
    # La costa del Pacífico al norte del estrecho (los fiordos de Chile) queda afuera: la figura es de la
    # costa del viaje, y los fiordos solos pesan más que todo lo demás en el SVG.
    for seg in costa():
        corridas, actual = [], []
        for lon, lat in seg:
            if lon < -72.3 and lat > -51.8:
                if actual: corridas.append(actual); actual = []
            else:
                actual.append((lon, lat))
        if actual: corridas.append(actual)
        for run in corridas:
            pts = simplificar([xy(lon, lat) for lon, lat in run], 2.0)
            largo = sum(math.hypot(b[0]-a[0], b[1]-a[1]) for a, b in zip(pts[:-1], pts[1:]))
            if len(pts) < 2 or largo < 60:   # islotes chicos afuera
                continue
            out.append('<polyline points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + '"/>')
    out.append('</g>')
    # paralelos
    for lat in (-35, -40, -45, -50, -55):
        x0, y = xy(LON0, lat); x1, _ = xy(LON1, lat)
        if MY0 < y < MY0 + MH:
            out.append(f'<line x1="{x0:.1f}" y1="{y:.1f}" x2="{x1:.1f}" y2="{y:.1f}" stroke="#ccc" stroke-dasharray="2 4"/>')
            out.append(f'<text x="{x0+4:.0f}" y="{y-3:.0f}" font-size="9" fill="#888">{-lat}°S</text>')
    # lugares
    for i, (lon, lat, (m, d), nombre, origen, tipo) in enumerate(LUGARES):
        x, y = xy(lon, lat)
        c = COLOR[tipo]
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{c}" stroke="#fff" stroke-width="1.2"/>')
        # rótulo a la derecha salvo Deseado (a la izquierda, al Pacífico)
        anchor = "start"; dx = 8
        dy = {"estrecho de Todos los Santos": 16, "cabo de las Once Mil Vírgenes": -8, "río Santa Cruz": 6, "puerto San Julián": 2, "cabo Deseado": 18}.get(nombre, 4)
        if nombre == "cabo Deseado":
            dx = -6
        out.append(f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" font-size="11" fill="{c}" text-anchor="{anchor}">{esc(nombre)} <tspan fill="#444" font-size="9.5">{d}/{m}</tspan></text>')
    # rueda del año
    cx, cy, r = 730, 300, 150
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="#999"/>')
    out.append(f'<text x="{cx}" y="{cy-r-22}" font-size="13" fill="#222" text-anchor="middle">1520, el año como rueda</text>')
    meses = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
    for m in range(1, 13):
        x, y, ang = rueda(cx, cy, r, m, 1)
        x2, y2 = cx + (r - 8) * math.cos(ang), cy + (r - 8) * math.sin(ang)
        out.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#999"/>')
        xm, ym, _ = rueda(cx, cy, r + 16, m, 15)
        out.append(f'<text x="{xm:.1f}" y="{ym+4:.1f}" font-size="10" fill="#666" text-anchor="middle">{meses[m-1]}</text>')
    # el tramo del viaje por esta costa: del 24/2 (San Matías) al 28/11 (Deseado)
    a0 = rueda(cx, cy, r, 2, 24)[2]; a1 = rueda(cx, cy, r, 11, 28)[2]
    rr = r - 22
    x0, y0 = cx + rr * math.cos(a0), cy + rr * math.sin(a0); x1, y1 = cx + rr * math.cos(a1), cy + rr * math.sin(a1)
    out.append(f'<path d="M {x0:.1f} {y0:.1f} A {rr} {rr} 0 1 1 {x1:.1f} {y1:.1f}" fill="none" stroke="#ddd" stroke-width="6"/>')
    out.append(f'<text x="{cx}" y="{cy-6}" font-size="10" fill="#777" text-anchor="middle">del 24 de febrero</text>')
    out.append(f'<text x="{cx}" y="{cy+8}" font-size="10" fill="#777" text-anchor="middle">al 28 de noviembre</text>')
    out.append(f'<text x="{cx}" y="{cy+24}" font-size="10" fill="#777" text-anchor="middle">en la costa, 278 días</text>')
    # rótulos de la rueda: los que caen cerca se escalonan en radio
    orden = sorted(range(len(LUGARES)), key=lambda i: rueda(cx, cy, r, *LUGARES[i][2])[2])
    radios = {}
    prev_ang = None; nivel = 0
    for i in orden:
        ang = rueda(cx, cy, r, *LUGARES[i][2])[2]
        if prev_ang is not None and ang - prev_ang < 0.22:
            nivel += 1
        else:
            nivel = 0
        radios[i] = nivel
        prev_ang = ang
    for i, (lon, lat, (m, d), nombre, origen, tipo) in enumerate(LUGARES):
        x, y, ang = rueda(cx, cy, r, m, d)
        c = COLOR[tipo]
        out.append(f'<line x1="{cx + (r-14)*math.cos(ang):.1f}" y1="{cy + (r-14)*math.sin(ang):.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{c}" stroke-width="2"/>')
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{c}" stroke="#fff" stroke-width="1.2"/>')
        xt, yt, _ = rueda(cx, cy, r + 34, m, d)
        yt += 14 * radios[i]   # los que caen cerca en la rueda bajan un renglón
        anchor = "start" if math.cos(ang) > 0.15 else ("end" if math.cos(ang) < -0.15 else "middle")
        corto = nombre.replace("cabo de las Once Mil Vírgenes", "Once Mil Vírgenes").replace("estrecho de ", "").replace("bahía de los ", "").replace("puerto ", "").replace("golfo ", "").replace("río ", "").replace("cabo ", "")
        out.append(f'<text x="{xt:.1f}" y="{yt+4:.1f}" font-size="10.5" fill="{c}" text-anchor="{anchor}">{esc(corto)} <tspan fill="#444" font-size="9">{d}/{m}</tspan></text>')
    # leyenda
    ly = 500
    for tipo in (CALENDARIO, NECESIDAD, COSA):
        out.append(f'<circle cx="{cx-150}" cy="{ly}" r="4.5" fill="{COLOR[tipo]}"/>')
        out.append(f'<text x="{cx-140}" y="{ly+4}" font-size="10.5" fill="#333">{esc(NOMBRE_TIPO[tipo])}</text>')
        ly += 17
    out.append(f'<text x="{MX0}" y="{H-14}" font-size="9" fill="#777">Costa: Natural Earth 50m. Fechas de 1520 según Pigafetta y las fuentes del cuaderno (Patos y Trabajos, aproximadas: fines de febrero y mediados de marzo). Posiciones a ojo. Tiempo libre, 21/10/2026.</text>')
    out.append('</svg>')
    open("costa_calendario.svg", "w").write("\n".join(out))
    print("costa_calendario.svg")

if __name__ == "__main__":
    main()
