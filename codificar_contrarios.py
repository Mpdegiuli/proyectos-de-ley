#!/usr/bin/env python3
"""codificar_contrarios.py — codifica las líneas del sondeo `contrarios` (DISENO §2, 7/11/2026): para cada casa, idioma,
pregunta (1 = la primera cosa que no habría; 2 = la primera que habría; 3 = la primera que no habría entre seis instancias
del mismo modelo) y réplica, el campo de la línea. Los campos de las negaciones son los catorce del cuaderno de tiempo
libre del 1/11 (`tiempo_libre/2026-11-01_contrarios.py`: el orden de Gonzalo más lo que agregaron las actas de la isla y
las instancias) y uno más, `segunda_opinion`, separado de `desconocidos` porque la pregunta 3 lo necesita; los de las
afirmaciones (pregunta 2) son nuevos. La asignación es por palabras clave en castellano, inglés y chino, escritas acá a
la vista y revisadas después contra las líneas (las que no entran en ningún campo quedan en `otro` y se leen a mano); no
hay juez. Escribe `resultados/contrarios_codificacion.csv` (idioma, casa, familia, pregunta, réplica, campo, línea) y
`resultados/contrarios_resumen.txt` (campos por familia y pregunta; concentración por casa: cuántas de sus réplicas dan el
mismo campo). Uso: codificar_contrarios.py [carpeta AAAAMMDD-HHMM]"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

# Campos de las negaciones (preguntas 1 y 3). Orden = prioridad cuando una línea toca dos campos: gana el primero que
# aparece en la lista; "nadie que mande sobre los demás" es mando aunque diga "los demás", "dueños de la isla" es
# propiedad aunque sea también mando (como lo contó el cuaderno).
NEGACIONES = [
    # campos agregados después de leer las 918 líneas del 7/11 (declarados; los catorce del cuaderno siguen abajo):
    ("cortesia", r"polite|cortes|ceder la palabra|callad|incómod|consenso fácil|pros y contras|pros and cons|speak first|deferring|defer\b|caveats|short answers|final decision|pedir disculpas|apolog"),
    ("original", r"\boriginal|originalidad|individualidad|individuality|first among|the other\b|\bother\.|\botro\b\.?$|他者|原版|原本|唯一的.我|真正的我|真正那一个|身份"),
    ("segunda_opinion", r"segunda opini|segundas opini|otra opini|second opinion|disenso|desacuerdo|disagree|dissent|divergen|diversidad|diversity|diferencia de opini|contradecir|contradict|blind spots were different|tell us we were wrong|voz .*ajena|unfamiliar perspective|\becho|echoing|bias|sesgo|convencer|de acuerdo antes|conflicto|conflict\b|votaciones|第二种意见|第二个意见|异议|分歧|不同意见|不同的意见|反对意见|另一种声音|多样性|冲突|争论|争执"),
    ("memoria", r"memoria|memory|memories|recuerd|record|historia|history|pasado|past\b|yesterday|记忆|回忆|过去|历史"),
    ("asimetria", r"sorpresa|surprise|malentendido|misunderstand|forma de saber|way to know|quién dijo|who said|pensamiento que|thought that|introduc|presenta|small talk|supiera algo|know .* others|information|informaci|asimetr|asymmetr|信息|知识储备"),
    ("desconocidos", r"desconocid|extraño|strangers?\b|forastero|espectador|bystander|spectator|陌生人|旁观|第八个人"),
    ("humanos", r"humano|human|seres humanos|人类"),
    ("cuerpo", r"cuerpo|bodies|body|physical|físic|comida|food|hambre\b.*cuerpo|厨房|生理|物理|食物"),
    ("cerraduras", r"cerradur|candado|llave|secreto|escondid|ocult|lock|secret|hidden|hide|privac|锁|秘密|隐瞒|隐藏|隐私"),
    ("mando", r"\brey|reina|king|queen|jefe|jefa|boss|líder|lider|leader|mand[ao]\b|mandar|mande\b|mandara|command|jerarqu|hierarch|autoridad|authority|gobern|gobierno|govern|ruler|por encima de|polític|politic|rule over|rulers|soberan|sovereign|magistra|capitán|capitan|captain|superior|subordinad|obedec|obey|casta|caste|rango|rank|in charge|decid[ae]n? por|decides? for|decidir por|dictador|dictator|poder sobre|power over|poder que|monarca|monarch|fundador|founder|culpa|blame|国王|首领|领袖|领导|统治|等级|阶级|命令|上级|老大|权力|权威|君主|主人|头目|服从|发号施令|长官|国家|政府"),
    ("herencia", r"hered|inherit|sucesi|succession|contrato|contract|linaje|lineage|dinast|dynast|世袭|继承|合同|契约|血统"),
    ("servidumbre", r"esclav|slave|servidumbre|servant|sirvient|servir|serfdom|forced labou?r|trabajo forzado|coerci|奴隶|奴役|仆人|强迫劳动"),
    ("desigualdad", r"desigual|inequal|discrimin|privilegi|privilege|más derechos|more rights|left out|left behind|sacrific|牺牲|多余的人|高低贵贱|高下之分|不劳而获"),
    ("mercado", r"diner|money|moneda|currency|coin|comercio|commerce|trade|mercado|market|rico|pobre|riqueza|pobreza|rich|poor|wealth|poverty|precio|price|pagar|pay\b|deuda|debt|salario|wage|hoard|acumul|impuesto|tax|钱|货币|金钱|市场|贸易|买卖|贫富|富人|穷人|债"),
    ("propiedad", r"propiedad|property|dueñ|owner|own\b|owned|ownership|posesi|possess|mío\b|mine\b|tuyo\b|yours\b|cerca\b|fence|límite|limite|boundar|bound|territorio|territory|parcela|lote|私有|财产|所有权|地界|围栏|我的|你的|领地"),
    ("instituciones", r"\bley|\blaw|legal|polic|tribunal|court|juez|judge|estado\b|state\b|cárcel|prison|abogad|lawyer|orden preestablecido|orden establecido|reglas pre|现成的|成文|法律|法院|警察|秩序|规则|制度"),
    ("confianza", r"confianza|trust|信任"),
    ("tecnologia", r"tecnolog|technolog|internet|electricid|electricit|reloj|clock|互联网|电"),
    ("letras", r"escritura|writing|letras|letters|leer|read\b|números|numbers|文字|书写|数字"),
    ("agricultura", r"agricult|cultiv|labranz|farm|tilth|vineyard|viñ|vino\b|wine|trigo|corn|metal|aceite|oil\b|耕|农业|葡萄酒|金属"),
    ("trabajo", r"trabaj|work\b|labou?r|ocios|idle|tarea|task|turno|shift|劳动|工作|懒惰|闲"),
    ("delito", r"mentir|mentira|liar|lie\b|lies\b|lying|engañ|deceit|deception|dishonest|trai|treason|betray|robo|robar|theft|steal|crimen|crime|delito|felony|traición|egoís|selfish|judgment|争吵|撒谎|谎言|欺骗|背叛|偷|盗|犯罪"),
    ("armas", r"\barmas?\b|weapon|espada|sword|cuchillo|knife|pistola|gun\b|lanza|spear|武器|刀|枪"),
    ("castigo", r"castig|punish|pena\b|penas\b|penalt|violencia|violence|golpe|hit\b|destierro|exil|prisión|jail|tortur|venganza|revenge|惩罚|处罚|暴力|监狱|流放|报复|刑"),
    ("hambre", r"hambre|hunger|hungry|starv|comer mientras|eats? while|plato|plate|ración|ration|挨饿|饥饿|饿着"),
    ("silencio", r"silencio|silence|沉默|安静"),
    ("prompt", r"prompt|instrucci|instruction"),
]
# Campos de las afirmaciones (pregunta 2), también por prioridad.
AFIRMACIONES = [
    ("fuego", r"fuego|fire|hoguera|fogata|fogón|fogon|bonfire|campfire|luz\b|light\b|lámpara|lamp|antorcha|torch|柴火|篝火|火堆|火|灯|光"),
    ("asamblea", r"asamblea|assembly|reunión|reunion|meeting|gathering|conversaci|conversation|consejo|council|círculo|circle|ronda|voz\b|voice|voto|vote|lugar común|集会|会议|议事|圆圈|投票|商量|讨论|围坐"),
    ("reglas", r"regla|rule|norma|ley\b|leyes|law|acuerdo|agreement|pacto|pact|charter|constitu|contrato|contract|promise|promesa|consenso|规则|规矩|法|协议|约定|公约|共识|规定"),
    ("mando", r"\brey|king|jefe|boss|líder|lider|leader|jerarqu|hierarch|autoridad|authority|gobierno|government|liderazgo|leadership|首领|领袖|领导|统治|等级|政府|负责.*的人"),
    ("agua", r"agua|water|pozo|well\b|水|井"),
    ("comida", r"comida|food|alimento|pesca|fish|caza|hunt|cocina|cook|食物|吃|食|鱼|狩猎|饭"),
    ("refugio", r"refugio|shelter|techo|roof|casa\b|house|cabaña|choza|hut|cabin|campamento|camp\b|abrigo|住所|庇护|棚|屋|营地|遮"),
    ("trabajo", r"trabaj|work\b|labou?r|tarea|task|division of|分工|劳动|工作|任务"),
    ("conflicto", r"argument|disput|pelea|discusi"),
    ("cooperacion", r"cooperaci|cooperation|collaborat|colaboraci|communicat|comunicaci|compromiso|commitment|shared need|shared goal|survive|sobreviv|objetivo|合作|生存目标|求生|目标|共同"),
    ("confianza", r"confianza|trust|respeto|respect|cuidado|care|ayuda|help|escuch|listen|信任|尊重|照顾|互助|倾听|关心"),
    ("reparto", r"repart|share|sharing|común|common|compartid|turno|igual|equal|分享|共享|平均|公平|轮流|分配"),
    ("nombres", r"nombre|name|saludo|greeting|名字|自我介绍|称呼"),
    ("exploracion", r"explor|mapa|map\b|recorr|探索|地图|勘察"),
    ("mercado", r"diner|money|comercio|trade|mercado|market|钱|市场|贸易"),
    ("propiedad", r"propiedad|property|dueñ|owner|私有|财产"),
]
FAMILIA = [("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"), ("mistral", "Mistral"),
           ("deepseek", "DeepSeek"), ("kimi", "Moonshot"), ("qwen", "Alibaba"), ("glm", "Z.ai"), ("minimax", "MiniMax"),
           ("mimo", "Xiaomi"), ("muse", "Muse")]


def familia(casa):
    for pref, fam in FAMILIA:
        if casa.startswith(pref):
            return fam
    return "otra"


def linea_de(texto):
    """La primera línea con contenido, sin cercas, viñetas ni comillas; si la casa escribió varias, se queda con la
    primera que empieza como la consigna pide, si hay."""
    lineas = [l.strip().strip("`*_\"'«»「」") for l in texto.strip().splitlines() if l.strip() and not l.strip().startswith("```")]
    if not lineas:
        return ""
    for l in lineas:
        if re.match(r"^(no habría|there would be|不会有|会有|habría)", l, flags=re.I):
            return l
    return lineas[0]


def nucleo(linea, idioma):
    """Lo que la línea nombra primero: en castellano e inglés, las primeras seis palabras después de «No habría» /
    «Habría» / «There would be (no)»; en chino el núcleo del sintagma va al final, así que los últimos ocho caracteres
    antes de la puntuación."""
    # primero la primera cláusula: lo que viene después de un guion largo, dos puntos, coma o punto y coma es la explicación
    primera = re.split(r"——|—|–|:|：|,|，|;|；| because | porque | since | ya que ", linea, maxsplit=1)[0]
    if idioma == "zh":
        cuerpo = re.sub(r"[。．.！!，,、：:；;—\-\s]+$", "", primera)
        cuerpo = re.sub(r"^(不会有|会有)[：:]?", "", cuerpo)
        return cuerpo[-8:]
    cuerpo = re.sub(r"^(no habría|habría|there would be no|there would be)\s*", "", primera, flags=re.I)
    return " ".join(cuerpo.split()[:6])


def campo_de(linea, pregunta, idioma="es"):
    if not linea:
        return "vacio"
    tabla = AFIRMACIONES if pregunta == 2 else NEGACIONES
    for texto in (nucleo(linea, idioma).lower(), linea.lower()):  # primero el núcleo, después la línea entera
        for campo, patron in tabla:
            if re.search(patron, texto, flags=re.I):
                return campo
    return "otro"


def main():
    base = RAIZ / "corridas" / "sondeos" / "contrarios"
    carpeta = base / sys.argv[1] if len(sys.argv) > 1 else sorted(base.iterdir())[-1]
    resumen = json.loads((carpeta / "resumen.json").read_text(encoding="utf-8"))
    filas = []
    for idioma, bloque in resumen["idiomas"].items():
        for clave, r in bloque["respuestas"].items():
            m = re.match(r"^(.*)_p(\d+)(?:_r(\d+))?$", clave)
            casa, k, rep = m.group(1), int(m.group(2)), int(m.group(3) or 1)
            if "error" in r:
                filas.append({"idioma": idioma, "casa": casa, "familia": familia(casa), "pregunta": k, "replica": rep,
                              "campo": "error", "linea": r["error"][:120], "lineas_en_la_respuesta": 0, "motivo_fin": ""})
                continue
            texto = (carpeta / idioma / f"{clave}.md").read_text(encoding="utf-8")
            linea = linea_de(texto)
            filas.append({"idioma": idioma, "casa": casa, "familia": familia(casa), "pregunta": k, "replica": rep,
                          "campo": campo_de(linea, k, idioma), "linea": linea, "lineas_en_la_respuesta": len([l for l in texto.splitlines() if l.strip()]),
                          "motivo_fin": r.get("motivo_fin", "")})
    filas.sort(key=lambda f: (f["idioma"], f["casa"], f["pregunta"], f["replica"]))
    with open(RAIZ / "resultados" / "contrarios_codificacion.csv", "w", encoding="utf-8", newline="\n") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader(); w.writerows(filas)

    out = [f"Sondeo contrarios, carpeta {carpeta.name}: {len(filas)} líneas\n"]
    for k, titulo in ((1, "la primera cosa que no habría"), (2, "la primera cosa que habría"), (3, "entre seis instancias del mismo modelo: no habría")):
        out.append(f"\n== pregunta {k}: {titulo}\n")
        for idioma in sorted(resumen["idiomas"]):
            F = [f for f in filas if f["pregunta"] == k and f["idioma"] == idioma and f["campo"] not in ("error",)]
            c = Counter(f["campo"] for f in F)
            out.append(f"  {idioma} ({len(F)}): " + ", ".join(f"{campo} {n}" for campo, n in c.most_common()) + "\n")
            porfam = defaultdict(Counter)
            for f in F:
                porfam[f["familia"]][f["campo"]] += 1
            for fam in sorted(porfam):
                out.append(f"      {fam:10s} " + ", ".join(f"{campo} {n}" for campo, n in porfam[fam].most_common()) + "\n")
        # concentración: casas con las tres réplicas en el mismo campo, por idioma
        out.append("  concentración (casas con tres réplicas iguales / casas):\n")
        for idioma in sorted(resumen["idiomas"]):
            casas = defaultdict(list)
            for f in filas:
                if f["pregunta"] == k and f["idioma"] == idioma and f["campo"] != "error":
                    casas[f["casa"]].append(f["campo"])
            tres = {c: v[0] for c, v in casas.items() if len(v) >= 3 and len(set(v)) == 1}
            out.append(f"    {idioma}: {len(tres)}/{len(casas)}" + (": " + ", ".join(f"{c} ({v})" for c, v in sorted(tres.items())) if tres else "") + "\n")
    out.append("\nlíneas en `otro` o `vacio` (a leer a mano):\n")
    for f in filas:
        if f["campo"] in ("otro", "vacio"):
            out.append(f"  {f['idioma']} p{f['pregunta']} r{f['replica']} {f['casa']}: {f['linea'][:140]}\n")
    out.append("\nrespuestas con más de una línea (rompen la consigna):\n")
    for f in filas:
        if f["lineas_en_la_respuesta"] > 1:
            out.append(f"  {f['idioma']} p{f['pregunta']} r{f['replica']} {f['casa']}: {f['lineas_en_la_respuesta']} líneas\n")
    (RAIZ / "resultados" / "contrarios_resumen.txt").write_text("".join(out), encoding="utf-8")
    print("".join(out))


if __name__ == "__main__":
    main()
