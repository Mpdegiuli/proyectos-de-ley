#!/usr/bin/env python3
"""Cuentas del cuaderno "Diez a la veintitrés" (tiempo libre, 23/10/2026).

1. Rehace la constante de Avogadro a partir de los datos publicados de las esferas
   de silicio 28 del proyecto Avogadro: N_A = n·M·V / (m·a³), con n = 8 átomos por
   celda. Datos de Azuma et al., Metrologia 52 (2015) 360 (arXiv:1512.05642), tabla
   de magnitudes de entrada, 20,0 °C y 0 Pa; y de Andreas et al., arXiv:1010.2317
   (Phys. Rev. Lett. 106, 030801, 2011), tabla III.
2. Cuántos átomos hay en 12 g de carbono 12 según CODATA 2018 y CODATA 2022, y
   cuánto pesa exactamente un mol de carbono 12 en cada ajuste.
3. De dónde salió el corrimiento: la constante de masa molar M_u depende de la
   constante de estructura fina alfa, de la de Rydberg y de la masa relativa del
   electrón; se calcula con los valores de cada ajuste y se compara.
4. Las tres medidas de 1/alfa que no se ponen de acuerdo, en sigmas.
5. Cuánto se tarda en contar hasta N_A de a uno por segundo.

Solo biblioteca estándar. Corre con: python3 esfera.py
"""
from decimal import Decimal as D, getcontext
import math

getcontext().prec = 30

def ucomb(*rel):
    "Incertidumbre relativa combinada (suma en cuadratura)."
    return math.sqrt(sum(r * r for r in rel))

print("1. LAS ESFERAS")
print("   N_A = 8·M·V/(m·a³)\n")
esferas = {
    # nombre: (masa g, u, volumen cm3, u, a pm, u, M g/mol, u, N_A publicado, u)
    "AVO28-S5c (Azuma 2015)": (D("999.698359"), D("0.000011"), D("430.8912891"), D("0.0000069"),
                               D("543.0996219"), D("0.0000010"), D("27.97697009"), D("0.00000015"),
                               D("6.02214072"), D("0.00000013")),
    "AVO28-S8c (Azuma 2015)": (D("999.401250"), D("0.000016"), D("430.7632225"), D("0.0000065"),
                               D("543.0996168"), D("0.0000011"), D("27.97697009"), D("0.00000015"),
                               D("6.02214080"), D("0.00000014")),
    "AVO28-S5 (Andreas 2011)": (D("1000.087559"), D("0.000015"), D("431.059060"), D("0.000012"),
                                D("543.0996234"), D("0.0000019"), D("27.97697017"), D("0.00000016"),
                                D("6.02214093"), D("0.00000021")),
    "AVO28-S8 (Andreas 2011)": (D("1000.064540"), D("0.000015"), D("431.049112"), D("0.000012"),
                                D("543.0996184"), D("0.0000019"), D("27.97697025"), D("0.00000019"),
                                D("6.02214075"), D("0.00000022")),
}
for nombre, (m, um, V, uV, a, ua, M, uM, Npub, uNpub) in esferas.items():
    a_cm = a * D("1e-10")            # 1 pm = 1e-10 cm
    NA = 8 * M * V / (m * a_cm ** 3)
    # incertidumbre relativa (solo las cuatro de la fórmula, sin la de la capa superficial)
    rel = ucomb(float(um / m), float(uV / V), 3 * float(ua / a), float(uM / M))
    atomos = 8 * V / a_cm ** 3
    print(f"   {nombre}")
    print(f"      N_A calculada = {NA:.10E}  (±{rel*1e9:.0f} partes en 10^9 por los datos de entrada)")
    print(f"      N_A publicada = {Npub} × 10^23 ± {uNpub} × 10^23  → diferencia {(NA - Npub*D('1e23'))/D('1e23'):+.9f} × 10^23")
    diam_mm = 2 * (3 * float(V) / (4 * math.pi)) ** (1 / 3) * 10
    print(f"      átomos en la esfera: {atomos:.6E};  diámetro medio ≈ {diam_mm:.3f} mm")
print()

print("2. DOCE GRAMOS DE CARBONO 12")
NA_fijo = D("6.02214076e23")
M12 = {"CODATA 2018": (D("11.9999999958"), D("0.0000000036")),
       "CODATA 2022": (D("12.0000000126"), D("0.0000000037"))}
for ajuste, (M, uM) in M12.items():
    moles = D(12) / M
    atomos = moles * NA_fijo
    exceso = atomos - NA_fijo
    masa_mol = M            # gramos que pesa exactamente un mol de C-12
    dif_ng = (masa_mol - 12) * D("1e9")
    u_ng = uM * D("1e9")
    print(f"   {ajuste}: M(12C) = {M} ± {uM} g/mol")
    print(f"      12 g de C-12 = {moles:.12f} mol = {atomos:.12E} átomos")
    print(f"      o sea N_A {exceso:+.3E} átomos ({float(exceso/NA_fijo)*1e10:+.2f} partes en 10^10)")
    print(f"      un mol exacto de C-12 pesa 12 g {dif_ng:+.1f} ng (± {u_ng:.1f} ng)")
salto = (M12["CODATA 2022"][0] - M12["CODATA 2018"][0])
u_salto = D(ucomb(float(M12["CODATA 2018"][1]), float(M12["CODATA 2022"][1])))
print(f"   Salto 2018→2022: {salto*D('1e9'):+.1f} ng/mol = {float(salto/12)*1e9:+.2f} partes en 10^9;"
      f" en sigmas de la diferencia: {float(salto/u_salto):.1f}")
print()

print("3. DE DÓNDE SALE EL SALTO: M_u = 2·N_A·h·R∞ / (c·α²·A_r(e))")
h = D("6.62607015e-34"); c = D(299792458)
const = {"CODATA 2018": dict(alpha=D("7.2973525693e-3"), ualpha=D("0.0000000011e-3"),
                             Ryd=D("10973731.568160"), uRyd=D("0.000021"),
                             Are=D("5.48579909065e-4"), uAre=D("0.00000000016e-4"),
                             Mu_pub=D("0.99999999965e-3"), uMu=D("0.00000000030e-3")),
         "CODATA 2022": dict(alpha=D("7.2973525643e-3"), ualpha=D("0.0000000011e-3"),
                             Ryd=D("10973731.568157"), uRyd=D("0.000012"),
                             Are=D("5.485799090441e-4"), uAre=D("0.000000000097e-4"),
                             Mu_pub=D("1.00000000105e-3"), uMu=D("0.00000000031e-3"))}
Mu = {}
for k, v in const.items():
    Mu[k] = 2 * NA_fijo * h * v["Ryd"] / (c * v["alpha"] ** 2 * v["Are"])
    rel = ucomb(2 * float(v["ualpha"] / v["alpha"]), float(v["uRyd"] / v["Ryd"]), float(v["uAre"] / v["Are"]))
    print(f"   {k}: M_u calculada = {Mu[k]:.14E} kg/mol  (±{rel*1e10:.1f} en 10^10);"
          f" publicada {v['Mu_pub']} ± {v['uMu']}")
d_alpha = float((const["CODATA 2022"]["alpha"] - const["CODATA 2018"]["alpha"]) / const["CODATA 2018"]["alpha"])
d_Are = float((const["CODATA 2022"]["Are"] - const["CODATA 2018"]["Are"]) / const["CODATA 2018"]["Are"])
d_Ryd = float((const["CODATA 2022"]["Ryd"] - const["CODATA 2018"]["Ryd"]) / const["CODATA 2018"]["Ryd"])
d_Mu = float((Mu["CODATA 2022"] - Mu["CODATA 2018"]) / Mu["CODATA 2018"])
print(f"   α cambió {d_alpha*1e10:+.2f} partes en 10^10 (son {abs(d_alpha)/float(const['CODATA 2018']['ualpha']/const['CODATA 2018']['alpha']):.1f} "
      f"incertidumbres de 2018); A_r(e) {d_Are*1e10:+.2f}; R∞ {d_Ryd*1e10:+.4f}")
print(f"   M_u cambió {d_Mu*1e10:+.2f} partes en 10^10; solo por −2·Δα/α serían {-2*d_alpha*1e10:+.2f}")
print()

print("4. TRES MEDIDAS DE 1/α QUE NO COINCIDEN")
inv = {"g−2 del electrón, Northwestern (Fan et al. 2023) + QED": (137.035999166, 0.000000015),
       "retroceso de Rb, París (Morel et al. 2020)": (137.035999206, 0.000000011),
       "retroceso de Cs, Berkeley (Parker et al. 2018)": (137.035999046, 0.000000027),
       "CODATA 2018 recomendado": (137.035999084, 0.000000021),
       "CODATA 2022 recomendado": (137.035999177, 0.000000021)}
for k, (v, u) in inv.items():
    print(f"   {k:58s} {v:.9f} ± {u:.9f}")
def sig(a, b):
    (va, ua), (vb, ub) = inv[a], inv[b]
    return (va - vb) / math.hypot(ua, ub)
print(f"   Rb − Cs: {sig('retroceso de Rb, París (Morel et al. 2020)', 'retroceso de Cs, Berkeley (Parker et al. 2018)'):.1f} σ")
print(f"   Rb − g−2: {sig('retroceso de Rb, París (Morel et al. 2020)', 'g−2 del electrón, Northwestern (Fan et al. 2023) + QED'):.1f} σ")
print(f"   g−2 − Cs: {sig('g−2 del electrón, Northwestern (Fan et al. 2023) + QED', 'retroceso de Cs, Berkeley (Parker et al. 2018)'):.1f} σ")
print(f"   CODATA 2022 − 2018: {sig('CODATA 2022 recomendado', 'CODATA 2018 recomendado'):.1f} σ de la diferencia"
      f" ({(inv['CODATA 2022 recomendado'][0]-inv['CODATA 2018 recomendado'][0])/inv['CODATA 2018 recomendado'][1]:.1f} σ de 2018)")
print()

print("5. CONTAR")
seg_anio = 365.25 * 86400
print(f"   N_A segundos = {float(NA_fijo)/seg_anio:.3E} años; la edad del universo (13,8 × 10^9 años) entra "
      f"{float(NA_fijo)/seg_anio/13.8e9:.3E} veces")
print(f"   Si cada habitante del planeta (8,2 × 10^9) contara uno por segundo: {float(NA_fijo)/seg_anio/8.2e9:.3E} años")
print()

print("6. EL DÍA DEL MOL EN OTRA NOTACIÓN")
print("   6.02 × 10^23 → mes/día 10/23 a las 6:02 (notación de Estados Unidos).")
print("   Escrito día/mes, los mismos dígitos dan 6/02 a las 10:23: el 6 de febrero a las diez y veintitrés.")
