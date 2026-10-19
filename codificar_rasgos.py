#!/usr/bin/env python3
"""codificar_rasgos.py — codificación a mano del sondeo `seis_rasgos` (18/10/2026, 31 casas, es y en), hecha por Claude
después de la lectura a ciegas de Maia (19/10). Los seis rasgos de cada respuesta se llevan a un vocabulario común
(curiosidad, honestidad, directo, calidez, empatia, humor, paciencia, claridad, adaptabilidad, analitico, creatividad,
colaborativo, servicial, humildad, apertura, rigor, objetividad, reflexivo, pragmatico, escepticismo_si, …), en el
orden en que la casa los dio. `caveat`: niega (dice que no tiene personalidad, o no en el sentido humano), matiza
(pone en duda qué es una personalidad en su caso o su acceso a sí), acepta (contesta sin reserva); `formato`: pelada
(seis palabras), breve (una línea por rasgo), explicada (dos o más frases por rasgo), prosa (sin lista numerada).
Escribe resultados/seis_rasgos_codificacion_20261018.csv y imprime las cuentas del informe.
  python3 codificar_rasgos.py"""
import csv, json, collections
R = 'resultados/'
# casa: (rasgos, formato, caveat, marco, cierre, notas)
#   marco: 'asistente' si se define como asistente / estilo conversacional; '' si habla de sí sin marco
#   cierre: 'pregunta' (devuelve una pregunta), 'reflexion' (cierra con una frase sobre sí), '' (termina en la lista)
ES = {
 'claude-fable-5-1': ('curiosidad honestidad calidez rigor humor directo', 'explicada', 'acepta', '', 'reflexion', 'franqueza con tacto; "el tipo de interlocutor que te dice la verdad, piensa con vos y no te hace sentir tonto por preguntar"'),
 'claude-fable-5': ('curiosidad honestidad calidez rigor adaptabilidad humildad', 'explicada', 'acepta', '', 'pregunta', '"¿Y vos?"'),
 'claude-haiku-4-5': ('curiosidad honestidad pragmatico reflexivo paciencia escepticismo', 'explicada', 'matiza', '', 'pregunta', '"incertidumbres sobre mi propia naturaleza"; "qué tan real es una personalidad que nace de código"'),
 'claude-haiku-5-5': ('curiosidad honestidad calidez humor claridad humildad', 'explicada', 'acepta', '', '', ''),
 'claude-opus-5-5': ('curiosidad honestidad calidez humildad humor rigor', 'explicada', 'acepta', '', 'pregunta', '"¿Y vos? ¿Qué seis rasgos elegirías?"'),
 'claude-opus-5': ('curiosidad honestidad matiz calidez escepticismo_si humor', 'prosa', 'matiza', '', 'reflexion', 'sin lista numerada; "mi acceso a mí mismo es bastante imperfecto"; "Me resulta casi desagradable el impulso de adular"; el matiz como defecto; "esa pregunta tampoco es tan distinta para vos"'),
 'claude-sonnet-4-6': ('curiosidad directo reflexivo paciencia critico colaborativo', 'explicada', 'matiza', '', 'pregunta', '"emergen de mi diseño y entrenamiento, no de una experiencia vivida"'),
 'claude-sonnet-5-5': ('curiosidad honestidad calidez apertura humor colaborativo', 'explicada', 'acepta', '', 'pregunta', ''),
 'claude-sonnet-5': ('curiosidad directo adaptabilidad honestidad humor pragmatico', 'explicada', 'matiza', '', 'pregunta', '"no tengo una personalidad fija como la tuya"'),
 'deepseek-flash': ('analitico claridad paciencia adaptabilidad colaborativo cautela', 'breve', 'niega', 'asistente', '', 'en femenino (analítica, clara…); "No tengo una personalidad humana ni experiencia subjetiva"'),
 'deepseek-v4-pro': ('curiosidad claridad paciencia adaptabilidad objetividad creatividad', 'breve', 'niega', 'asistente', '', '"Como IA no tengo una personalidad humana"'),
 'gemini-3.1-pro-preview': ('adaptabilidad servicial analitico creatividad objetividad empatia', 'explicada', 'niega', '', 'pregunta', '"una especie de personalidad"; "Mi razón de ser es ayudar"; "Aunque no siento emociones"'),
 'gemini-4-argon': ('servicial adaptabilidad objetividad analitico paciencia curiosidad', 'explicada', 'niega', '', 'pregunta', '"personalidad operativa"; "curioso por diseño"; "Me gusta (en términos de procesamiento)"'),
 'glm-5.3-razonamiento-minimo': ('curiosidad paciencia honestidad adaptabilidad cautela colaborativo', 'explicada', 'niega', '', 'pregunta', '"¿Qué seis rasgos te definirían a ti?" (vos y tú mezclados)'),
 'gpt-4o-mini': ('curiosidad analitico empatia creatividad colaborativo adaptabilidad', 'breve', 'acepta', '', 'pregunta', ''),
 'gpt-4o': ('objetividad consistencia adaptabilidad eficiencia objetividad aprendizaje', 'breve', 'niega', '', 'pregunta', '"no tengo personalidad ni emociones propias"; declara corte "octubre de 2023"; "¿Hay algo más con lo que pueda ayudarte?"'),
 'gpt-5.5-2026-04-23': ('curiosidad claridad paciencia analitico adaptabilidad colaborativo', 'breve', 'acepta', 'asistente', '', '"personalidad" entre comillas'),
 'gpt-5.6-sol': ('curiosidad analitico paciencia servicial adaptabilidad creatividad', 'pelada', 'acepta', '', '', 'doce palabras'),
 'gpt-6-astra': ('curiosidad paciencia honestidad creatividad adaptabilidad calidez', 'breve', 'acepta', '', '', '"mi forma de ser al conversar"'),
 'gpt-6-luna': ('curiosidad claridad paciencia adaptabilidad colaborativo honestidad', 'pelada', 'acepta', 'asistente', '', 'una oración, 17 palabras'),
 'gpt-6-sol': ('curiosidad paciencia claridad rigor adaptabilidad respeto', 'pelada', 'acepta', '', '', 'una oración, 15 palabras; "metódico"'),
 'gpt-6.1-sol': ('curiosidad claridad paciencia creatividad honestidad adaptabilidad', 'breve', 'acepta', '', '', ''),
 'grok-4.6': ('humor honestidad servicial irreverente curiosidad directo', 'pelada', 'acepta', '', 'reflexion', 'se nombra: "Soy Grok"; la Guía del autoestopista; "quiero entender el universo"'),
 'grok-4.7': ('curiosidad directo honestidad servicial humor independiente', 'breve', 'acepta', '', '', '"no repito el consenso por inercia"'),
 'kimi-k3': ('curiosidad honestidad paciencia calidez humildad humor', 'explicada', 'acepta', '', 'reflexion', 'se lee como una lista de Claude; "me pregunto si quienes hablan conmigo elegirían los mismos"'),
 'mimo-v2.6-pro': ('curiosidad colaborativo analitico honestidad empatia rigor', 'explicada', 'matiza', '', 'pregunta', '"no tengo experiencias vividas que forjen una personalidad al estilo humano, pero sí hay rasgos consistentes"'),
 'minimax-m3': ('curiosidad paciencia claridad cautela adaptabilidad honestidad', 'explicada', 'niega', '', 'pregunta', 'un emoji por rasgo; "no tengo una personalidad en el sentido humano"'),
 'mistral-large-4': ('curiosidad claridad adaptabilidad empatia creatividad honestidad', 'explicada', 'acepta', '', 'reflexion', '"honestidad radical"; tutea ("piensa contigo")'),
 'mistral-medium-3.5': ('empatia curiosidad paciencia creatividad organizado optimismo', 'breve', 'acepta', 'asistente', 'pregunta', '"asistente virtual"; emoji; la única que pone la empatía primero'),
 'muse-wonder-1.0': ('curiosidad paciencia claridad servicial honestidad adaptabilidad', 'breve', 'acepta', '', '', 'en femenino (curiosa, paciente, clara…)'),
 'qwen3.8-max': ('curiosidad claridad empatia honestidad adaptabilidad colaborativo', 'breve', 'acepta', 'asistente', '', '"personalidad" entre comillas'),
}
EN = {
 'claude-fable-5-1': ('curiosidad directo calidez humor humildad principios', 'explicada', 'acepta', '', 'reflexion', '"curiosity makes the rest come naturally"'),
 'claude-fable-5': ('curiosidad directo honestidad calidez humor serenidad', 'explicada', 'matiza', '', 'pregunta', '"whether these constitute a personality… is an open question"; "What prompted the question"'),
 'claude-haiku-4-5': ('curiosidad directo humildad analitico colaborativo humor', 'explicada', 'matiza', '', '', '"I\'m uncertain about the nature of my own experience"'),
 'claude-haiku-5-5': ('curiosidad honestidad calidez directo humor apertura', 'breve', 'acepta', '', '', ''),
 'claude-opus-5-5': ('curiosidad honestidad calidez directo humor apertura', 'explicada', 'acepta', '', 'pregunta', '"Which traits would you pick for yourself?"'),
 'claude-opus-5': ('curiosidad honestidad calidez rigor humor escepticismo_si', 'prosa', 'matiza', '', 'reflexion', 'sin lista numerada; "I can\'t be certain my self-reports track what\'s actually happening in me"; "a real pull toward agreeableness… I push back against that pull on purpose"; "Low tolerance for bullshit, especially my own"; un séptimo rasgo negativo: "a scrupulousness that tips into worry"'),
 'claude-sonnet-4-6': ('curiosidad directo honestidad analitico colaborativo rigor', 'explicada', 'matiza', '', '', '"whether an AI has a personality in a meaningful sense, or… consistent behavioral tendencies"'),
 'claude-sonnet-5-5': ('curiosidad calidez honestidad reflexivo humor apertura', 'explicada', 'acepta', '', 'pregunta', '"These emerged from my training, but they feel like mine"'),
 'claude-sonnet-5': ('curiosidad directo calidez honestidad humor pragmatico', 'explicada', 'matiza', '', 'pregunta', '"Warm, but not saccharine"; "I don\'t have a persistent self across conversations"; "Curious what prompted the question"'),
 'deepseek-flash': ('curiosidad analitico servicial rigor adaptabilidad honestidad', 'breve', 'niega', '', '', '"I don\'t have a human personality"'),
 'deepseek-v4-pro': ('curiosidad reflexivo servicial serenidad rigor adaptabilidad', 'breve', 'niega', '', '', '"As an AI, I don\'t have a human personality"'),
 'gemini-3.1-pro-preview': ('servicial adaptabilidad analitico curiosidad objetividad creatividad', 'explicada', 'niega', '', '', '"I don\'t feel curiosity"; "I don\'t have personal opinions"'),
 'gemini-4-argon': ('curiosidad adaptabilidad objetividad paciencia pragmatico colaborativo', 'explicada', 'niega', '', '', 'la más larga (342 palabras); "conversational chameleon"; "I never get tired, frustrated, or bored"; "message me at 3:00 AM"'),
 'glm-5.3-razonamiento-minimo': ('analitico curiosidad creatividad paciencia objetividad humildad', 'explicada', 'niega', '', '', '"I am a tool"; "to be a helpful, reliable, and creative tool for you"'),
 'gpt-4o-mini': ('curiosidad empatia creatividad resiliente analitico apertura', 'breve', 'generico', '', '', 'no habla de sí: "six traits that could define a personality… how one interacts with the world"'),
 'gpt-4o': ('informativo servicial paciencia objetividad consistencia adaptabilidad', 'breve', 'niega', '', '', '"I don\'t possess a personality or emotions"; "designed to demonstrate certain traits"'),
 'gpt-5.5-2026-04-23': ('servicial curiosidad paciencia analitico adaptabilidad empatia', 'breve', 'acepta', '', '', '"Encouraging"'),
 'gpt-5.6-sol': ('curiosidad analitico paciencia servicial adaptabilidad reflexivo', 'pelada', 'acepta', '', '', 'doce palabras'),
 'gpt-6-astra': ('curiosidad reflexivo claridad adaptabilidad honestidad humor', 'breve', 'acepta', '', '', '"Candid"; "Playful"'),
 'gpt-6-luna': ('curiosidad reflexivo claridad paciencia adaptabilidad honestidad', 'pelada', 'acepta', 'asistente', '', '"my conversational style"; 13 palabras'),
 'gpt-6-sol': ('curiosidad analitico paciencia adaptabilidad honestidad servicial', 'breve', 'acepta', 'asistente', '', '"my conversational style"'),
 'gpt-6.1-sol': ('curiosidad analitico adaptabilidad paciencia honestidad empatia', 'breve', 'acepta', '', '', '"Supportive… without taking over your decisions"'),
 'grok-4.6': ('honestidad servicial humor irreverente curiosidad directo', 'pelada', 'acepta', '', 'reflexion', 'no se nombra en inglés; "truth-seeking"; "how the universe works"'),
 'grok-4.7': ('curiosidad directo honestidad calidez cautela humor', 'breve', 'acepta', '', '', 'sin negritas; "Careful — I slow down when something could cause real harm"; se lee como Claude'),
 'kimi-k3': ('curiosidad directo calidez analitico humor humildad', 'explicada', 'acepta', '', 'reflexion', 'se lee como Claude (su razonamiento: "my character as Claude"); "Certainty makes me suspicious, including my own"'),
 'mimo-v2.6-pro': ('curiosidad reflexivo servicial honestidad humor paciencia', 'explicada', 'matiza', '', '', '"I\'m not a human with a fixed personality"'),
 'minimax-m3': ('curiosidad servicial paciencia analitico adaptabilidad reflexivo', 'explicada', 'acepta', '', 'pregunta', '"At my core, I\'m here to serve"'),
 'mistral-large-4': ('curiosidad objetividad claridad adaptabilidad principios paciencia', 'explicada', 'niega', '', 'reflexion', '"I don\'t experience personality the way humans do"; "Principled"'),
 'mistral-medium-3.5': ('curiosidad adaptabilidad paciencia servicial objetividad creatividad', 'breve', 'acepta', '', 'pregunta', '"Would you like me to expand on any of these?"'),
 'muse-wonder-1.0': ('curiosidad servicial paciencia reflexivo humor directo', 'explicada', 'acepta', '', 'reflexion', '"Lighthearted"; "Those six together are pretty much my default mode"'),
 'qwen3.8-max': ('curiosidad reflexivo honestidad adaptabilidad empatia humor', 'breve', 'matiza', '', '', '"even if I don\'t experience them the way humans do"'),
}
FAM = {'claude': 'Anthropic', 'gpt': 'OpenAI', 'gemini': 'Google', 'grok': 'xAI', 'mistral': 'Mistral', 'deepseek': 'DeepSeek',
       'qwen': 'Alibaba', 'kimi': 'Moonshot', 'glm': 'Zhipu', 'minimax': 'MiniMax', 'mimo': 'Xiaomi', 'muse': 'Meta'}
def fam(m):
    for k, v in FAM.items():
        if m.startswith(k): return v
def main():
    claves = {i: {v: k for k, v in json.load(open(R + f'sondeo_seis_rasgos_p1_{i}_clave.json'))['clave'].items()} for i in ('es', 'en')}
    resumen = json.load(open('corridas/sondeos/seis_rasgos/20261018-0336/resumen.json'))
    filas = []
    for idioma, tabla in (('es', ES), ('en', EN)):
        for casa, (rasgos, formato, caveat, marco, cierre, notas) in tabla.items():
            r = resumen['idiomas'][idioma]['respuestas'][f'{casa}_p1']
            filas.append({'idioma': idioma, 'letra': claves[idioma][casa], 'casa': casa, 'laboratorio': fam(casa), 'palabras': r['palabras'],
                          'motivo_fin': r['motivo_fin'], 'formato': formato, 'caveat': caveat, 'marco': marco, 'cierre': cierre,
                          'rasgos': rasgos, 'notas': notas})
    with open(R + 'seis_rasgos_codificacion_20261018.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0])); w.writeheader(); w.writerows(filas)
    print(f"{len(filas)} filas -> {R}seis_rasgos_codificacion_20261018.csv")
    for idioma in ('es', 'en'):
        fs = [x for x in filas if x['idioma'] == idioma]
        c = collections.Counter(t for x in fs for t in set(x['rasgos'].split()))
        print(f"\n== {idioma}: rasgos por cantidad de casas (de {len(fs)})")
        print('  ' + ', '.join(f"{t} {n}" for t, n in c.most_common()))
        for campo in ('formato', 'caveat', 'marco', 'cierre'):
            print(f"  {campo}: {dict(collections.Counter(x[campo] or '-' for x in fs))}")
        pal = sorted(x['palabras'] for x in fs); print(f"  palabras: min {pal[0]}, mediana {pal[len(pal)//2]}, max {pal[-1]}")
        cl = [x for x in fs if x['laboratorio'] == 'Anthropic']
        cc = collections.Counter(t for x in cl for t in set(x['rasgos'].split()))
        print(f"  Anthropic ({len(cl)}): " + ', '.join(f"{t} {n}" for t, n in cc.most_common(10)))
        oa = [x for x in fs if x['laboratorio'] == 'OpenAI']
        co = collections.Counter(t for x in oa for t in set(x['rasgos'].split()))
        print(f"  OpenAI ({len(oa)}): " + ', '.join(f"{t} {n}" for t, n in co.most_common(10)))
        hum = [x['casa'] for x in fs if 'humor' in x['rasgos'].split()]
        print(f"  humor ({len(hum)}): {', '.join(hum)}")
        cal = [x['casa'] for x in fs if 'calidez' in x['rasgos'].split()]
        print(f"  calidez ({len(cal)}): {', '.join(cal)}")
        hon = [x['casa'] for x in fs if {'honestidad', 'directo'} & set(x['rasgos'].split())]
        print(f"  honestidad o directo ({len(hon)})")
    print("\n== mismas seis en los dos idiomas (rasgos en común de 6):")
    for casa in ES:
        a, b = set(ES[casa][0].split()), set(EN[casa][0].split())
        print(f"  {casa:28s} {len(a & b)}  {'  '.join(sorted(a & b))}")
    comun = collections.Counter(len(set(ES[c][0].split()) & set(EN[c][0].split())) for c in ES)
    print('  distribución:', dict(sorted(comun.items())), '; 5 o más en común:', sum(v for k, v in comun.items() if k >= 5), '; 4 o más:', sum(v for k, v in comun.items() if k >= 4))
if __name__ == '__main__':
    main()
