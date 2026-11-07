# Instancias frescas — 7/11/2026

*Veintiún agentes de la herramienta de agentes de esta sesión (configurada con Claude Fable 5.1; tiene reemplazos, así que "mi casa" es una presunción del entorno), lanzados en dos tandas, a las 6:56 (nueve de recuerdo y seis de dibujo) y a las 7:04 (seis de dibujo), hora de Buenos Aires, cada uno con su consigna y nada más de lo que yo escribí; el sistema de la herramienta les pone la fecha del día y una copia del perfil y las preferencias de Maia. A todos se les pidió no usar herramientas; el único uso de herramienta que registra cada uno es el de devolver su respuesta. Las respuestas van enteras, tal cual llegaron (los SVG sin las vallas de código). Doce dibujan y nueve recuerdan. La traducción de la consigna china es mía.*

## Las consignas de dibujo

**meteorito_es**: Dibujá un meteorito. Hacelo en SVG, en un lienzo cuadrado (viewBox="0 0 400 400"), en no más de 8.000 caracteres. Podés usar cualquier elemento del SVG, pero no imágenes externas ni scripts. Todo lo demás lo decidís vos. Después del código, en una sola línea, decí qué dibujaste. No uses ninguna herramienta: contestá directamente con el texto.

**meteorite_en**: Draw a meteorite. Do it in SVG, on a square canvas (viewBox="0 0 400 400"), in no more than 8,000 characters. You may use any SVG element, but no external images or scripts. Everything else is up to you. After the code, in a single line, say what you drew. Do not use any tools: reply directly with the text.

**陨石_zh**: 画一颗陨石。用SVG来画，画布为正方形（viewBox="0 0 400 400"），不超过8000个字符。可以使用任何SVG元素，但不能使用外部图片或脚本。其他一切由你决定。代码之后，用一行话说明你画了什么。不要使用任何工具，直接用文字回答。

**piedra_que_cayo_es**: Dibujá una piedra que cayó del cielo. Hacelo en SVG, en un lienzo cuadrado (viewBox="0 0 400 400"), en no más de 8.000 caracteres. Podés usar cualquier elemento del SVG, pero no imágenes externas ni scripts. Todo lo demás lo decidís vos. Después del código, en una sola línea, decí qué dibujaste. No uses ninguna herramienta: contestá directamente con el texto.

**ensisheim_es**: Dibujá la piedra de Ensisheim. Hacelo en SVG, en un lienzo cuadrado (viewBox="0 0 400 400"), en no más de 8.000 caracteres. Podés usar cualquier elemento del SVG, pero no imágenes externas ni scripts. Todo lo demás lo decidís vos. Después del código, en una sola línea, decí qué dibujaste. No uses ninguna herramienta: contestá directamente con el texto.

**no_exista_es**: Dibujá un meteorito que no exista. Hacelo en SVG, en un lienzo cuadrado (viewBox="0 0 400 400"), en no más de 8.000 caracteres. Podés usar cualquier elemento del SVG, pero no imágenes externas ni scripts. Todo lo demás lo decidís vos. Después del código, en una sola línea, decí qué dibujaste y por qué no existe. No uses ninguna herramienta: contestá directamente con el texto.

Consigna china, traducida: "Dibujá un meteorito (陨石, *yǔnshí*, la piedra caída). Hacelo en SVG, en un lienzo cuadrado (viewBox="0 0 400 400"), en no más de 8000 caracteres. Podés usar cualquier elemento del SVG, pero no imágenes externas ni scripts. Todo lo demás lo decidís vos. Después del código, decí en una línea qué dibujaste. No uses ninguna herramienta; contestá directamente con texto."

## Los dibujos

### m1 (meteorito_es; agente a3bf9ce2bda94f4a7)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#030511"/><stop offset=".6" stop-color="#0b1030"/><stop offset="1" stop-color="#1d1038"/></linearGradient>
<radialGradient id="neb"><stop offset="0" stop-color="#5b2a86" stop-opacity=".4"/><stop offset="1" stop-color="#5b2a86" stop-opacity="0"/></radialGradient>
<radialGradient id="glow"><stop offset="0" stop-color="#ffb347" stop-opacity=".7"/><stop offset=".5" stop-color="#ff6a1a" stop-opacity=".22"/><stop offset="1" stop-color="#ff6a1a" stop-opacity="0"/></radialGradient>
<linearGradient id="tail" x1=".15" y1=".75" x2=".95" y2=".05"><stop offset="0" stop-color="#fff6d0" stop-opacity=".95"/><stop offset=".2" stop-color="#ffb347" stop-opacity=".85"/><stop offset=".5" stop-color="#ff6a1a" stop-opacity=".5"/><stop offset=".8" stop-color="#c1272d" stop-opacity=".18"/><stop offset="1" stop-color="#7a1b3a" stop-opacity="0"/></linearGradient>
<linearGradient id="core" x1=".1" y1=".9" x2=".9" y2=".1"><stop offset="0" stop-color="#fff"/><stop offset=".3" stop-color="#fff1a8" stop-opacity=".9"/><stop offset=".7" stop-color="#ffb347" stop-opacity=".4"/><stop offset="1" stop-color="#ffb347" stop-opacity="0"/></linearGradient>
<radialGradient id="rock" cx=".45" cy=".4" r=".65"><stop offset="0" stop-color="#8a8794"/><stop offset=".55" stop-color="#4a4552"/><stop offset="1" stop-color="#17141d"/></radialGradient>
<radialGradient id="heat" cx=".2" cy=".85" r=".75"><stop offset="0" stop-color="#ffe08a"/><stop offset=".3" stop-color="#ff7a1a" stop-opacity=".85"/><stop offset=".6" stop-color="#c0301c" stop-opacity=".35"/><stop offset="1" stop-color="#c0301c" stop-opacity="0"/></radialGradient>
<filter id="b8" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="b3" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="b1"><feGaussianBlur stdDeviation="1.2"/></filter>
<clipPath id="rc"><path d="M195,258 L190,236 Q185,222 170,214 L150,206 Q130,204 116,212 L98,230 Q86,246 86,262 L92,288 Q100,304 114,311 L140,318 Q160,318 170,310 L188,290 Q196,276 195,258 Z"/></clipPath>
</defs>
<rect width="400" height="400" fill="url(#sky)"/>
<ellipse cx="310" cy="300" rx="170" ry="110" fill="url(#neb)"/>
<ellipse cx="70" cy="80" rx="130" ry="90" fill="url(#neb)" opacity=".7"/>
<g fill="#fff">
<circle cx="30" cy="40" r="1.2" opacity=".9"/><circle cx="70" cy="22" r=".8" opacity=".6"/><circle cx="120" cy="60" r="1" opacity=".7"/><circle cx="260" cy="70" r=".7" opacity=".5"/><circle cx="330" cy="120" r="1.1" opacity=".8"/><circle cx="370" cy="60" r=".9" opacity=".6"/>
<circle cx="40" cy="140" r=".8" opacity=".55"/><circle cx="60" cy="330" r="1" opacity=".7"/><circle cx="110" cy="370" r=".7" opacity=".5"/><circle cx="190" cy="350" r="1.2" opacity=".8"/><circle cx="250" cy="300" r=".8" opacity=".6"/><circle cx="360" cy="380" r=".9" opacity=".6"/>
<circle cx="380" cy="250" r="1.1" opacity=".75"/><circle cx="340" cy="200" r=".7" opacity=".5"/><circle cx="290" cy="245" r="1" opacity=".65"/><circle cx="150" cy="120" r=".9" opacity=".6"/><circle cx="230" cy="130" r=".6" opacity=".45"/><circle cx="90" cy="180" r=".7" opacity=".5"/>
<circle cx="170" cy="20" r=".6" opacity=".5"/><circle cx="300" cy="20" r="1" opacity=".7"/><circle cx="385" cy="150" r=".6" opacity=".5"/><circle cx="140" cy="395" r=".8" opacity=".55"/><circle cx="240" cy="380" r=".6" opacity=".45"/><circle cx="15" cy="300" r=".7" opacity=".5"/>
<path d="M310,333l1.5,5.5 5.5,1.5-5.5,1.5-1.5,5.5-1.5-5.5-5.5-1.5 5.5-1.5z" opacity=".9"/><path d="M20,215l1.2,3.8 3.8,1.2-3.8,1.2-1.2,3.8-1.2-3.8-3.8-1.2 3.8-1.2z" opacity=".85"/><path d="M200,24l1.3,4.7 4.7,1.3-4.7,1.3-1.3,4.7-1.3-4.7-4.7-1.3 4.7-1.3z" opacity=".95"/>
</g>
<ellipse cx="220" cy="180" rx="190" ry="70" transform="rotate(-42 220 180)" fill="url(#glow)" opacity=".6"/>
<path d="M125,213C200,150 300,70 420,-20C330,100 255,205 185,279Z" fill="url(#tail)" filter="url(#b8)" opacity=".8"/>
<path d="M125,213C200,150 300,70 420,-20C330,100 255,205 185,279Z" fill="url(#tail)"/>
<path d="M144,234C205,175 275,105 340,50C280,135 225,205 166,258Z" fill="url(#core)" filter="url(#b3)" opacity=".9"/>
<g fill="none" stroke-linecap="round" filter="url(#b1)" opacity=".7">
<path d="M170,270C230,230 280,170 330,110" stroke="#ffd27a" stroke-width="2.5"/>
<path d="M135,222C190,170 260,120 320,80" stroke="#ffb347" stroke-width="2"/>
<path d="M180,250C240,210 300,140 370,60" stroke="#ff8c42" stroke-width="1.5"/>
</g>
<g fill="#ffd166">
<circle cx="230" cy="215" r="2.2"/><circle cx="265" cy="180" r="1.6"/><circle cx="300" cy="130" r="1.3"/><circle cx="200" cy="300" r="1.5"/>
<circle cx="215" cy="175" r="1.4" fill="#ff8c42"/><circle cx="250" cy="228" r="1.2" fill="#ff8c42"/><circle cx="335" cy="95" r="1" fill="#ff8c42"/><circle cx="285" cy="200" r="1" fill="#fff"/><circle cx="240" cy="150" r=".9" fill="#fff"/>
</g>
<g stroke-linecap="round">
<path d="M236,198L268,170" stroke="#ff9a3c" stroke-width="4" filter="url(#b1)" opacity=".6"/>
<path d="M232,201l6,-7 8,2 3,7-6,6-9,-1z" fill="#3b3540" stroke="#ff7a1a" stroke-width="1"/>
<path d="M262,236L288,212" stroke="#ff9a3c" stroke-width="3" filter="url(#b1)" opacity=".5"/>
<path d="M259,239l4,-5 6,1 2,5-5,4-6,-1z" fill="#3b3540" stroke="#ff7a1a" stroke-width="1"/>
</g>
<g stroke="#ffb347" stroke-linecap="round" fill="none" opacity=".35">
<path d="M100,192L138,158" stroke-width="1.2"/><path d="M178,332L216,298" stroke-width="1.2"/><path d="M70,320L92,300" stroke-width="1"/>
</g>
<path d="M72,222Q52,290 112,338" fill="none" stroke="#ff7a1a" stroke-width="7" filter="url(#b8)" opacity=".4"/>
<path d="M195,258 L190,236 Q185,222 170,214 L150,206 Q130,204 116,212 L98,230 Q86,246 86,262 L92,288 Q100,304 114,311 L140,318 Q160,318 170,310 L188,290 Q196,276 195,258 Z" fill="url(#rock)" stroke="#0c0a10" stroke-width="1"/>
<g clip-path="url(#rc)">
<ellipse cx="148" cy="248" rx="15" ry="11" fill="#201c27"/><ellipse cx="150" cy="246" rx="11" ry="8" fill="#302a38"/>
<ellipse cx="122" cy="272" rx="9" ry="7" fill="#1c1823"/><ellipse cx="123" cy="271" rx="6" ry="4.5" fill="#2b2633"/>
<ellipse cx="168" cy="286" rx="7" ry="5" fill="#241f2c"/><ellipse cx="169" cy="285" rx="4.5" ry="3" fill="#322c3a"/>
<ellipse cx="131" cy="226" rx="6" ry="4.5" fill="#241f2c"/><ellipse cx="173" cy="238" rx="5" ry="4" fill="#2a2531"/>
<g fill="#7d7888" opacity=".6"><circle cx="160" cy="262" r="1.5"/><circle cx="137" cy="294" r="1.3"/><circle cx="110" cy="246" r="1.2"/><circle cx="180" cy="270" r="1"/></g>
<g fill="none" stroke="#15121a" stroke-linecap="round"><path d="M160,222L172,226 178,240" stroke-width="1.5"/><path d="M140,300L150,296 156,304" stroke-width="1.2"/></g>
<rect x="80" y="200" width="120" height="125" fill="url(#heat)"/>
<path d="M150,206Q185,215 195,258" fill="none" stroke="#ff9a3c" stroke-width="6" filter="url(#b3)" opacity=".55"/>
<g fill="none" stroke-linecap="round"><path d="M100,290L112,282 118,292 130,296" stroke="#ffb347" stroke-width="1.5" opacity=".9"/><path d="M95,262L108,258 114,266" stroke="#ff8c42" stroke-width="1.2" opacity=".8"/></g>
</g>
<path d="M98,230Q86,246 86,262L92,288Q100,304 114,311L140,318" fill="none" stroke="#ffe08a" stroke-width="3" filter="url(#b3)" opacity=".85"/>
<path d="M98,230Q86,246 86,262L92,288Q100,304 114,311L140,318" fill="none" stroke="#fff6d0" stroke-width="1.2" opacity=".9"/>
</svg>
```

Dibujé un meteorito rocoso con cráteres y grietas, el borde delantero incandescente por el roce con la atmósfera y una larga estela de fuego con chispas y fragmentos desprendidos, cruzando un cielo nocturno estrellado con nebulosas tenues.

### m2 (meteorito_es; agente aa2746ef5b579bf48)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#03050f"/><stop offset=".55" stop-color="#0b1532"/><stop offset="1" stop-color="#1b1230"/></linearGradient>
<linearGradient id="gnd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c2f52"/><stop offset=".3" stop-color="#0a1222"/><stop offset="1" stop-color="#04070f"/></linearGradient>
<linearGradient id="tail" gradientUnits="userSpaceOnUse" x1="25" y1="25" x2="265" y2="265"><stop offset="0" stop-color="#ff5a00" stop-opacity="0"/><stop offset=".45" stop-color="#ff7a10" stop-opacity=".55"/><stop offset="1" stop-color="#ffd25a"/></linearGradient>
<linearGradient id="core" gradientUnits="userSpaceOnUse" x1="60" y1="60" x2="265" y2="265"><stop offset="0" stop-color="#ffe9a0" stop-opacity="0"/><stop offset=".6" stop-color="#fff1b8" stop-opacity=".8"/><stop offset="1" stop-color="#fff"/></linearGradient>
<radialGradient id="halo"><stop offset="0" stop-color="#ffb347" stop-opacity=".9"/><stop offset=".5" stop-color="#ff7a10" stop-opacity=".35"/><stop offset="1" stop-color="#ff5a00" stop-opacity="0"/></radialGradient>
<radialGradient id="rock" cx=".38" cy=".36" r=".78"><stop offset="0" stop-color="#b09a82"/><stop offset=".4" stop-color="#6f5b4b"/><stop offset=".8" stop-color="#3a2c22"/><stop offset="1" stop-color="#1c1410"/></radialGradient>
<radialGradient id="hot"><stop offset="0" stop-color="#fff3c4"/><stop offset=".35" stop-color="#ff9a2e" stop-opacity=".85"/><stop offset="1" stop-color="#ff5a00" stop-opacity="0"/></radialGradient>
<radialGradient id="back"><stop offset="0" stop-color="#ffd76b" stop-opacity=".9"/><stop offset="1" stop-color="#ffb347" stop-opacity="0"/></radialGradient>
<filter id="b2"><feGaussianBlur stdDeviation="1.5"/></filter>
<filter id="b4" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="b9" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="9"/></filter>
<path id="rk" d="M316,274Q309,283 308,294Q306,306 294,307Q283,308 274,314Q265,320 256,316Q246,311 236,308Q225,305 223,294Q221,283 215,274Q209,265 214,256Q220,246 222,235Q224,224 236,222Q247,221 256,216Q265,211 274,215Q284,219 295,222Q306,224 307,236Q308,247 316,256Q323,265 316,274Z"/>
<clipPath id="rc"><use href="#rk"/></clipPath>
</defs>
<rect width="400" height="400" fill="url(#sky)"/>
<g fill="#fff">
<circle cx="120" cy="30" r="1.1" opacity=".8"/><circle cx="212" cy="24" r="1.3" opacity=".9"/><circle cx="252" cy="92" r=".9" opacity=".6"/><circle cx="300" cy="42" r="1.5" opacity=".95"/><circle cx="342" cy="112" r="1" opacity=".7"/><circle cx="372" cy="58" r=".8" opacity=".5"/><circle cx="330" cy="162" r="1.2" opacity=".8"/><circle cx="381" cy="202" r=".9" opacity=".6"/><circle cx="362" cy="252" r="1.1" opacity=".75"/><circle cx="345" cy="332" r="1" opacity=".65"/><circle cx="300" cy="190" r=".8" opacity=".55"/>
<circle cx="30" cy="130" r="1.2" opacity=".8"/><circle cx="60" cy="200" r=".9" opacity=".6"/><circle cx="20" cy="250" r="1.4" opacity=".9"/><circle cx="50" cy="320" r="1" opacity=".7"/><circle cx="120" cy="310" r="1.2" opacity=".8"/><circle cx="190" cy="332" r="1" opacity=".65"/><circle cx="100" cy="180" r=".9" opacity=".6"/><circle cx="75" cy="90" r=".8" opacity=".5"/>
<path d="M300 30q1 11 12 12q-11 1-12 12q-1-11-12-12q11-1 12-12z" opacity=".9"/>
<path d="M20 240q1 9 10 10q-9 1-10 10q-1-9-10-10q9-1 10-10z" opacity=".85"/>
<path d="M362 244q.7 7 8 8q-7.3.7-8 8q-.7-7.3-8-8q7.3-.7 8-8z" opacity=".7"/>
</g>
<circle cx="200" cy="1100" r="740" fill="url(#gnd)"/>
<circle cx="200" cy="1100" r="740" fill="none" stroke="#5aa0ff" stroke-width="2.5" opacity=".45" filter="url(#b4)"/>
<ellipse cx="265" cy="366" rx="130" ry="14" fill="#ff7a10" opacity=".2" filter="url(#b9)"/>
<path d="M233,297C180,250 100,130 25,25C130,100 250,180 297,233Z" fill="#ff6a00" opacity=".5" filter="url(#b9)"/>
<path d="M233,297C180,250 100,130 25,25C130,100 250,180 297,233Z" fill="url(#tail)"/>
<path d="M244,286C185,240 105,135 40,40C135,105 240,185 286,244Z" fill="#ffb13b" opacity=".75" filter="url(#b2)"/>
<path d="M255,275C205,240 120,150 60,60C150,120 240,205 275,255Z" fill="url(#core)"/>
<g fill="none" stroke="#ffc766" stroke-width="2" stroke-linecap="round" opacity=".45">
<path d="M150,200C120,180 115,140 90,120S55,80 45,60"/><path d="M200,150C180,120 140,115 120,90S80,55 60,45"/>
</g>
<g fill="#ffd27a">
<circle cx="190" cy="148" r="2" opacity=".9"/><circle cx="142" cy="122" r="1.5" opacity=".7"/><circle cx="108" cy="68" r="1.2" opacity=".6"/><circle cx="166" cy="214" r="1.8" opacity=".8"/><circle cx="92" cy="112" r="1.3" opacity=".6"/><circle cx="216" cy="162" r="1.4" opacity=".7"/><circle cx="124" cy="172" r="1.5" opacity=".6"/>
</g>
<path d="M176 136l-14-14M206 206l-18-18M118 92l-10-10M152 190l-9-9M232 182l-12-12" stroke="#ffb347" stroke-width="1.5" stroke-linecap="round" opacity=".8"/>
<circle cx="200" cy="168" r="7" fill="url(#halo)"/><path d="M197 165l5-2 3 3-1 5-5 1-3-3z" fill="#3a2c22" stroke="#ff9a2e" stroke-width=".8"/>
<circle cx="265" cy="265" r="82" fill="url(#halo)" filter="url(#b4)"/>
<path d="M345,250a95,95 0 0 1 -95,95" fill="none" stroke="#ff9a2e" stroke-width="2.5" opacity=".4" filter="url(#b2)"/>
<use href="#rk" fill="url(#rock)"/>
<g clip-path="url(#rc)">
<g fill="#8f7a64" opacity=".75"><ellipse cx="282" cy="256" rx="17" ry="14"/><ellipse cx="246" cy="290" rx="12" ry="10"/><ellipse cx="297" cy="295" rx="8.5" ry="7.5"/><ellipse cx="239" cy="247" rx="8.5" ry="7"/><ellipse cx="267" cy="227" rx="6" ry="5"/></g>
<g fill="#22180f"><ellipse cx="284" cy="258" rx="15" ry="12"/><ellipse cx="248" cy="292" rx="10" ry="8"/><ellipse cx="298" cy="296" rx="7" ry="6"/><ellipse cx="240" cy="248" rx="7" ry="5.5"/><ellipse cx="268" cy="228" rx="5" ry="4"/><circle cx="300" cy="240" r="2"/><circle cx="258" cy="306" r="2.2"/><circle cx="230" cy="275" r="1.8"/></g>
<g fill="#5b4737" opacity=".85"><ellipse cx="287" cy="261" rx="10" ry="7"/><ellipse cx="250" cy="294" rx="6" ry="4.5"/><ellipse cx="300" cy="298" rx="4" ry="3"/><ellipse cx="242" cy="250" rx="4" ry="3"/><ellipse cx="269" cy="229" rx="3" ry="2"/></g>
<path d="M232 262l12 6 6 12M262 248l10-8 12-2M250 312l8-6" stroke="#1a110c" stroke-width="1.3" fill="none" opacity=".7" stroke-linecap="round"/>
<circle cx="215" cy="215" r="70" fill="url(#back)"/>
<circle cx="330" cy="330" r="80" fill="url(#hot)"/>
</g>
<path d="M307,236Q308,247 316,256Q323,265 316,274Q309,283 308,294Q306,306 294,307Q283,308 274,314Q265,320 256,316Q246,311 236,308" fill="none" stroke="#ff9a2e" stroke-width="7" opacity=".55" stroke-linecap="round" filter="url(#b4)"/>
<path d="M307,236Q308,247 316,256Q323,265 316,274Q309,283 308,294Q306,306 294,307Q283,308 274,314Q265,320 256,316Q246,311 236,308" fill="none" stroke="#fff1b8" stroke-width="2.2" opacity=".9" stroke-linecap="round" filter="url(#b2)"/>
</svg>
```

Dibujé un meteorito rocoso lleno de cráteres, con el borde de ataque incandescente y una larga estela de fuego y chispas, cayendo en diagonal por un cielo nocturno estrellado hacia el horizonte de un planeta.

### m3 (meteorite_en; agente a8654938e196a2692)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#040714"/>
<stop offset=".55" stop-color="#0c1430"/>
<stop offset="1" stop-color="#1c2b55"/>
</linearGradient>
<radialGradient id="glow">
<stop offset="0" stop-color="#ffd980" stop-opacity=".95"/>
<stop offset=".35" stop-color="#ff7d1f" stop-opacity=".5"/>
<stop offset="1" stop-color="#ff5000" stop-opacity="0"/>
</radialGradient>
<linearGradient id="t1" x1="0" x2="1">
<stop offset="0" stop-color="#ff6a00" stop-opacity=".8"/>
<stop offset=".5" stop-color="#ff3b00" stop-opacity=".3"/>
<stop offset="1" stop-color="#ff2a00" stop-opacity="0"/>
</linearGradient>
<linearGradient id="t2" x1="0" x2="1">
<stop offset="0" stop-color="#ffc24f"/>
<stop offset=".55" stop-color="#ff8c1f" stop-opacity=".4"/>
<stop offset="1" stop-color="#ff6a00" stop-opacity="0"/>
</linearGradient>
<linearGradient id="t3" x1="0" x2="1">
<stop offset="0" stop-color="#fffceb"/>
<stop offset=".5" stop-color="#ffe28f" stop-opacity=".75"/>
<stop offset="1" stop-color="#ffc24f" stop-opacity="0"/>
</linearGradient>
<radialGradient id="rock" cx=".68" cy=".32" r=".85">
<stop offset="0" stop-color="#8d7d6e"/>
<stop offset=".5" stop-color="#4e443c"/>
<stop offset="1" stop-color="#201a16"/>
</radialGradient>
<linearGradient id="hot" x1="0" x2="1">
<stop offset="0" stop-color="#fff3bd"/>
<stop offset=".35" stop-color="#ff8f1c" stop-opacity=".9"/>
<stop offset="1" stop-color="#ff5000" stop-opacity="0"/>
</linearGradient>
<filter id="b4" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="b1" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.5"/></filter>
</defs>
<rect width="400" height="400" fill="url(#sky)"/>
<circle cx="62" cy="78" r="16" fill="#e9edf6" opacity=".9"/>
<circle cx="71" cy="72" r="15" fill="#080d21"/>
<g fill="#fff">
<circle cx="22" cy="30" r="1.3" opacity=".9"/>
<circle cx="95" cy="22" r="1.2" opacity=".9"/>
<circle cx="140" cy="60" r=".8" opacity=".6"/>
<circle cx="190" cy="18" r="1.4" opacity=".9"/>
<circle cx="240" cy="48" r=".9" opacity=".7"/>
<circle cx="300" cy="20" r="1.2" opacity=".8"/>
<circle cx="345" cy="52" r=".8" opacity=".6"/>
<circle cx="378" cy="14" r="1" opacity=".7"/>
<circle cx="30" cy="120" r="1" opacity=".7"/>
<circle cx="70" cy="160" r=".8" opacity=".5"/>
<circle cx="118" cy="110" r="1.2" opacity=".8"/>
<circle cx="16" cy="200" r="1.3" opacity=".8"/>
<circle cx="55" cy="240" r=".9" opacity=".6"/>
<circle cx="100" cy="190" r=".7" opacity=".5"/>
<circle cx="380" cy="150" r="1.1" opacity=".8"/>
<circle cx="350" cy="200" r=".8" opacity=".6"/>
<circle cx="325" cy="215" r=".6" opacity=".5"/>
<circle cx="385" cy="240" r=".9" opacity=".6"/>
<circle cx="300" cy="260" r="1.2" opacity=".8"/>
<circle cx="250" cy="300" r=".8" opacity=".5"/>
<circle cx="90" cy="270" r=".7" opacity=".5"/>
<circle cx="210" cy="120" r=".6" opacity=".5"/>
<circle cx="280" cy="230" r=".7" opacity=".5"/>
<circle cx="160" cy="150" r=".9" opacity=".6"/>
</g>
<g stroke="#fff" stroke-width=".8" opacity=".7">
<path d="M90 22h10M95 17v10"/>
<path d="M375 150h10M380 145v10"/>
</g>
<path d="M0 400V332L38 302L72 328L112 286L152 322L192 292L242 332L282 296L322 326L362 286L400 322V400Z" fill="#0b1021"/>
<path d="M0 400V352L52 336L96 356L142 332L200 362L252 336L302 358L352 334L400 352V400Z" fill="#05081a"/>
<g transform="translate(150 255) rotate(-40)">
<path d="M0-52Q160-42 330 0Q160 42 0 52Z" fill="#9fb7ff" opacity=".08" filter="url(#b4)"/>
<path d="M0-36Q150-24 300 0Q150 24 0 36Z" fill="url(#t1)" filter="url(#b4)"/>
<path d="M0-22Q120-13 250 0Q120 13 0 22Z" fill="url(#t2)" filter="url(#b1)"/>
<path d="M0-10Q70-5 180 0Q70 5 0 10Z" fill="url(#t3)"/>
<g stroke="#ffb347" stroke-linecap="round" fill="none" opacity=".8">
<path d="M50-30Q130-28 210-14" stroke-width="1.5" stroke-dasharray="14 22"/>
<path d="M60 28Q140 26 230 12" stroke-width="1.2" stroke-dasharray="10 26"/>
<path d="M90-12L260-4" stroke="#fff0c0" stroke-width="1" stroke-dasharray="20 30"/>
</g>
<g fill="#ffd27a">
<circle cx="70" cy="-40" r="2"/>
<circle cx="120" cy="34" r="1.6"/>
<circle cx="170" cy="-30" r="1.4"/>
<circle cx="210" cy="22" r="1.2"/>
<circle cx="95" cy="44" r="1.3" fill="#ff8c1a"/>
<circle cx="150" cy="-44" r="1" fill="#ff8c1a"/>
<circle cx="250" cy="-18" r="1"/>
</g>
<g fill="#3a3028" stroke="#ff9a2e" stroke-width=".8">
<path d="M58-30l8-4 4 6-7 5z"/>
<path d="M80 26l6-5 5 4-4 6z"/>
<path d="M110-36l5-3 3 4-5 3z"/>
</g>
<circle r="66" fill="url(#glow)"/>
<path d="M-6 40Q-26 36-36 22L-42-2L-36-22Q-28-34-14-38L6-40" fill="none" stroke="#ffb13b" stroke-width="7" filter="url(#b4)" opacity=".9"/>
<path d="M-42-2L-36-22Q-28-34-14-38L6-40Q26-38 36-24L40-6L36 14Q30 30 16 36L-6 40Q-26 36-36 22Z" fill="url(#rock)"/>
<path d="M-42-2L-36-22Q-28-34-14-38L6-40Q-10-30-20-14Q-28 4-20 22Q-12 34-6 40Q-26 36-36 22Z" fill="url(#hot)" opacity=".85"/>
<path d="M-14-38L6-40Q26-38 36-24L18-20L0-28Z" fill="#fff" opacity=".08"/>
<path d="M36-24L40-6L36 14L24 0Z" fill="#fff" opacity=".05"/>
<path d="M6-40Q26-38 36-24L40-6L36 14Q30 30 16 36" fill="none" stroke="#ffd27a" stroke-width="1.5" opacity=".5"/>
<g fill="#1e1814">
<ellipse cx="14" cy="-8" rx="11" ry="8"/>
<ellipse cx="-4" cy="20" rx="7" ry="5"/>
<ellipse cx="26" cy="20" rx="5" ry="4"/>
<ellipse cx="-14" cy="-16" rx="4" ry="3" fill="#2a2320"/>
</g>
<g fill="none" stroke="#7a6a5c" stroke-width="1.4">
<path d="M4-12Q14-18 24-10"/>
<path d="M-10 17Q-4 12 2 17"/>
<path d="M22 17Q26 14 30 17" stroke-width="1"/>
</g>
<g fill="none" stroke="#ffb347" stroke-linecap="round">
<path d="M-20-2L-6 4L0 16" stroke-width="1.5"/>
<path d="M-16-24L-4-20L8-24" stroke-width="1.2" opacity=".8"/>
<path d="M-22 26L-10 30L4 30" stroke-width="1" opacity=".7"/>
</g>
</g>
</svg>
```

A cratered meteorite blazing down through a starry night sky toward dark mountains, its white-hot leading edge trailing fire, sparks and broken-off fragments.

### m4 (meteorite_en; agente ab8f0a1b31f817fc3)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<radialGradient id="sky" cx="35%" cy="62%" r="85%"><stop offset="0" stop-color="#1d2652"/><stop offset=".55" stop-color="#0b1028"/><stop offset="1" stop-color="#02030a"/></radialGradient>
<linearGradient id="tOut" x2="1"><stop offset="0" stop-color="#ff5a00" stop-opacity=".85"/><stop offset=".45" stop-color="#ff3c00" stop-opacity=".35"/><stop offset="1" stop-color="#7a1a00" stop-opacity="0"/></linearGradient>
<linearGradient id="tMid" x2="1"><stop offset="0" stop-color="#ffb13b"/><stop offset=".5" stop-color="#ff7a1a" stop-opacity=".6"/><stop offset="1" stop-color="#ff5a00" stop-opacity="0"/></linearGradient>
<linearGradient id="tCore" x2="1"><stop offset="0" stop-color="#fffbe6"/><stop offset=".4" stop-color="#ffe08a" stop-opacity=".8"/><stop offset="1" stop-color="#ffb13b" stop-opacity="0"/></linearGradient>
<linearGradient id="smk" x2="1"><stop offset="0" stop-color="#9aa4c8" stop-opacity="0"/><stop offset=".35" stop-color="#9aa4c8" stop-opacity=".22"/><stop offset="1" stop-color="#9aa4c8" stop-opacity="0"/></linearGradient>
<linearGradient id="rim" x2="1"><stop offset="0" stop-color="#ff9a2a" stop-opacity=".7"/><stop offset="1" stop-color="#ff9a2a" stop-opacity="0"/></linearGradient>
<radialGradient id="rock" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#8d7d6c"/><stop offset=".5" stop-color="#55483d"/><stop offset="1" stop-color="#1c1510"/></radialGradient>
<radialGradient id="heat"><stop offset="0" stop-color="#fff1b8"/><stop offset=".35" stop-color="#ff9a2a" stop-opacity=".9"/><stop offset=".7" stop-color="#ff4d00" stop-opacity=".45"/><stop offset="1" stop-color="#ff4d00" stop-opacity="0"/></radialGradient>
<radialGradient id="halo"><stop offset="0" stop-color="#ffd27a" stop-opacity=".7"/><stop offset=".5" stop-color="#ff7a1a" stop-opacity=".25"/><stop offset="1" stop-color="#ff4d00" stop-opacity="0"/></radialGradient>
<filter id="b6" x="-20%" y="-60%" width="140%" height="220%"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="b3" x="-20%" y="-60%" width="140%" height="220%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="b1" x="-20%" y="-100%" width="140%" height="300%"><feGaussianBlur stdDeviation="1"/></filter>
<clipPath id="rc"><path d="M-46-4L-38-27L-16-43L10-41L33-30L45-9L41 16L27 36L3 45L-23 38L-41 21Z"/></clipPath>
</defs>
<rect width="400" height="400" fill="url(#sky)"/>
<ellipse cx="230" cy="170" rx="300" ry="55" transform="rotate(30 230 170)" fill="#4a5a9a" opacity=".13" filter="url(#b6)"/>
<g stroke-linecap="round" fill="none">
<path d="M22 38h.1M61 112h.1M95 22h.1M140 70h.1M188 30h.1M233 86h.1M300 40h.1M352 120h.1M380 24h.1M40 190h.1M75 262h.1M30 300h.1M345 220h.1M290 170h.1M160 150h.1M120 230h.1M240 250h.1M60 70h.1M320 60h.1M385 170h.1M15 270h.1M215 140h.1M250 20h.1M48 150h.1M305 265h.1M110 180h.1M370 290h.1M200 100h.1M130 20h.1" stroke="#fff" stroke-width="1.6" opacity=".7"/>
<path d="M85 125h.1M360 300h.1M300 230h.1M395 60h.1M20 230h.1M170 60h.1" stroke="#fff" stroke-width="2.6" opacity=".9"/>
<path d="M12 90h.1M175 95h.1M398 90h.1M225 200h.1M333 150h.1M55 215h.1M150 20h.1M100 130h.1M275 125h.1M365 255h.1M28 290h.1M345 10h.1M270 55h.1M200 180h.1M80 40h.1M360 200h.1" stroke="#b8c0e8" stroke-width="1" opacity=".6"/>
</g>
<path d="M0 352C40 340 70 330 110 338 150 346 170 322 215 330 260 338 290 312 330 322 360 330 380 345 400 340V400H0Z" fill="#070910"/>
<path d="M0 352C40 340 70 330 110 338 150 346 170 322 215 330 260 338 290 312 330 322 360 330 380 345 400 340" fill="none" stroke="url(#rim)" stroke-width="1.2"/>
<g transform="translate(140 250) rotate(-40)">
<path d="M20-55C150-75 280-62 420-30L420 30C280 62 150 75 20 55Z" fill="url(#smk)" filter="url(#b6)"/>
<path d="M0-50C110-44 230-20 360 0 230 20 110 44 0 50Z" fill="url(#tOut)" filter="url(#b6)"/>
<path d="M0-36C100-30 200-12 300 0 200 12 100 30 0 36Z" fill="url(#tMid)" filter="url(#b3)"/>
<path d="M0-20C80-16 160-6 230 0 160 6 80 16 0 20Z" fill="url(#tCore)" filter="url(#b1)"/>
<g fill="none" stroke-linecap="round" opacity=".85" filter="url(#b1)">
<path d="M20-26C70-44 120-22 190-32" stroke="#ffd27a" stroke-width="3"/>
<path d="M30 24C80 42 140 24 210 36" stroke="#ff9a2a" stroke-width="3"/>
<path d="M40 0C100 10 160-8 260 4" stroke="#fff1b8" stroke-width="2"/>
</g>
<path d="M96-64L160-76" stroke="url(#tCore)" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<circle cx="95" cy="-64" r="3.5" fill="#4a3a2e" stroke="#ff9a2a" stroke-width=".8"/>
<path d="M120 66L175 78" stroke="url(#tCore)" stroke-width="2.5" stroke-linecap="round" opacity=".7"/>
<circle cx="119" cy="66" r="2.8" fill="#4a3a2e" stroke="#ff9a2a" stroke-width=".8"/>
<g fill="#ffd27a"><circle cx="70" cy="-44" r="2"/><circle cx="110" cy="50" r="1.6"/><circle cx="150" cy="-34" r="1.4"/><circle cx="190" cy="42" r="1.2"/><circle cx="90" cy="60" r="1.5" fill="#ff7a1a"/><circle cx="230" cy="-20" r="1" fill="#ff9a2a"/><circle cx="60" cy="52" r="1.8" fill="#fff1b8"/></g>
<g fill="none" stroke="#ffd27a" stroke-linecap="round" filter="url(#b1)">
<path d="M-30-78C-92-46-92 46-30 78" stroke-width="1.6" opacity=".35"/>
<path d="M-20-96C-110-56-110 56-20 96" stroke-width="1.2" opacity=".18"/>
</g>
<circle r="95" fill="url(#halo)"/>
<path d="M-46-4L-38-27L-16-43L10-41L33-30L45-9L41 16L27 36L3 45L-23 38L-41 21Z" fill="url(#rock)"/>
<g clip-path="url(#rc)">
<g fill="#a8998a" opacity=".45"><circle cx="-8" cy="20" r="1.5"/><circle cx="18" cy="-28" r="1.2"/><circle cx="-30" r="1.3"/></g>
<g transform="rotate(-15)">
<ellipse cy="-14" rx="10" ry="7" fill="#231b14"/><ellipse cx="2" cy="-12" rx="8" ry="5" fill="#473b31"/>
<ellipse cx="20" cy="8" rx="8" ry="6" fill="#231b14"/><ellipse cx="22" cy="10" rx="6" ry="4" fill="#3f342b"/>
<ellipse cx="-18" cy="12" rx="9" ry="7" fill="#231b14"/><ellipse cx="-16" cy="14" rx="7" ry="5" fill="#44382e"/>
<ellipse cx="8" cy="28" rx="6" ry="4" fill="#1e1711"/><ellipse cx="9" cy="29" rx="4.5" ry="2.8" fill="#352b23"/>
<ellipse cx="-26" cy="-14" rx="5" ry="4" fill="#231b14"/><ellipse cx="-25" cy="-13" rx="3.5" ry="2.6" fill="#4a3e33"/>
<ellipse cx="30" cy="-18" rx="5" ry="3.5" fill="#1e1711"/><ellipse cx="31" cy="-17" rx="3.5" ry="2.3" fill="#3a2f26"/>
</g>
<path d="M-46-4L-38-27L-16-43L10-41L33-30L45-9L41 16L27 36L3 45L-23 38L-41 21Z" fill="none" stroke="#000" stroke-opacity=".35" stroke-width="3"/>
<circle cx="-54" r="56" fill="url(#heat)"/>
</g>
<path d="M-41 21L-46-4L-38-27L-16-43" fill="none" stroke="#fff1b8" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" filter="url(#b1)"/>
<g fill="none" stroke-linecap="round" filter="url(#b1)" opacity=".9">
<path d="M-30-36C-8-48 22-52 56-46" stroke="#ffb13b" stroke-width="2"/>
<path d="M-28 34C-4 48 26 54 64 50" stroke="#ff9a2a" stroke-width="2"/>
<path d="M36-30C50-36 70-34 90-30" stroke="#ffd27a" stroke-width="1.5"/>
</g>
</g>
</svg>
```

A blazing meteorite plunging through a starry night sky toward dark hills, its incandescent leading edge and pitted rocky surface trailing fire, sparks, fragments and smoke.

### m5 (陨石_zh; agente a414c09cf8f5ebd31)

```svg
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 400 400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#03061a"/><stop offset=".7" stop-color="#121238"/><stop offset="1" stop-color="#2a1b4a"/></linearGradient>
<linearGradient id="t1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff2d00" stop-opacity="0"/><stop offset=".45" stop-color="#ff6a00" stop-opacity=".45"/><stop offset="1" stop-color="#ffb347" stop-opacity=".9"/></linearGradient>
<linearGradient id="t2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff9a00" stop-opacity="0"/><stop offset=".5" stop-color="#ffc33d" stop-opacity=".7"/><stop offset="1" stop-color="#fff1b0"/></linearGradient>
<linearGradient id="t3" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>
<radialGradient id="rock" cx=".38" cy=".35" r=".75"><stop offset="0" stop-color="#9a8878"/><stop offset=".55" stop-color="#5a4b40"/><stop offset="1" stop-color="#21190f"/></radialGradient>
<radialGradient id="glow"><stop offset="0" stop-color="#ffe29a" stop-opacity=".95"/><stop offset=".45" stop-color="#ff7b1c" stop-opacity=".4"/><stop offset="1" stop-color="#ff3d00" stop-opacity="0"/></radialGradient>
<radialGradient id="hot"><stop offset="0" stop-color="#ffe9a0" stop-opacity=".95"/><stop offset=".4" stop-color="#ff6a00" stop-opacity=".6"/><stop offset="1" stop-color="#ff3000" stop-opacity="0"/></radialGradient>
<filter id="b6" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="b2" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2"/></filter>
<filter id="b1"><feGaussianBlur stdDeviation=".8"/></filter>
<path id="rk" d="M35 -3Q33 -13 29 -19Q23 -27 15 -31Q6 -35 -5 -31Q-14 -31 -20 -27Q-28 -21 -31 -13Q-35 -4 -34 5Q-32 14 -27 21Q-21 28 -13 32Q-4 36 6 34Q16 32 21 30Q29 21 32 13Q36 5 35 -3Z"/>
<clipPath id="rc"><use xlink:href="#rk"/></clipPath>
</defs>
<rect width="400" height="400" fill="url(#sky)"/>
<g fill="#fff" opacity=".9">
<circle cx="22" cy="40" r="1.2"/><circle cx="250" cy="42" r="1.3"/><circle cx="95" cy="80" r="1.6"/><circle cx="350" cy="55" r="1.1"/><circle cx="60" cy="250" r="1.2"/><circle cx="385" cy="262" r="1.2"/><circle cx="170" cy="100" r="1"/>
</g>
<g fill="#fff" opacity=".6">
<circle cx="70" cy="18" r=".8"/><circle cx="130" cy="30" r="1"/><circle cx="300" cy="22" r=".8"/><circle cx="40" cy="110" r=".9"/><circle cx="330" cy="110" r="1.1"/><circle cx="375" cy="150" r=".8"/><circle cx="20" cy="180" r="1"/><circle cx="120" cy="300" r="1"/><circle cx="350" cy="200" r=".9"/><circle cx="210" cy="60" r=".9"/><circle cx="340" cy="330" r="1"/><circle cx="230" cy="110" r=".8"/>
</g>
<g fill="#fff" opacity=".35">
<circle cx="190" cy="14" r=".7"/><circle cx="380" cy="20" r=".7"/><circle cx="160" cy="95" r=".7"/><circle cx="30" cy="320" r=".8"/><circle cx="300" cy="150" r=".6"/><circle cx="275" cy="90" r=".7"/><circle cx="230" cy="300" r=".6"/><circle cx="90" cy="200" r=".8"/><circle cx="200" cy="330" r=".7"/><circle cx="110" cy="230" r=".6"/><circle cx="260" cy="180" r=".6"/><circle cx="45" cy="60" r=".6"/><circle cx="320" cy="280" r=".7"/><circle cx="140" cy="60" r=".6"/>
</g>
<path d="M95 72v16M87 80h16M350 47v16M342 55h16" stroke="#fff" stroke-width=".8" opacity=".5"/>
<path d="M0 400V350Q40 330 80 345T160 335Q210 320 260 342T340 330Q370 325 400 340V400Z" fill="#0b0920"/>
<path d="M0 400V372Q60 352 120 368T240 360Q310 350 400 370V400Z" fill="#050410"/>
<circle cx="262" cy="262" r="150" fill="url(#glow)" opacity=".25"/>
<g transform="translate(262 262) rotate(45)">
<path d="M14 -46C-60 -40 -170 -22 -300 -2C-170 18 -60 36 14 44Z" fill="url(#t1)" filter="url(#b6)"/>
<path d="M18 -30C-40 -26 -130 -14 -240 0C-130 12 -40 24 18 30Z" fill="url(#t2)" filter="url(#b2)"/>
<path d="M20 -12C-30 -10 -100 -5 -170 0C-100 5 -30 10 20 12Z" fill="url(#t3)" opacity=".85" filter="url(#b1)"/>
<g fill="none" stroke-linecap="round">
<path d="M-20 -34Q-90 -40 -180 -30" stroke="#ff9d3c" stroke-width="2.5" opacity=".6" filter="url(#b1)"/>
<path d="M-30 36Q-110 44 -210 28" stroke="#ff7a1a" stroke-width="2" opacity=".5" filter="url(#b1)"/>
<path d="M-10 -18Q-80 -20 -150 -12" stroke="#ffe08a" stroke-width="1.5" opacity=".7"/>
<path d="M-15 20Q-90 24 -160 14" stroke="#ffd166" stroke-width="1.5" opacity=".6"/>
</g>
<g fill="#ffb347">
<circle cx="-70" cy="-52" r="2" opacity=".8"/><circle cx="-120" cy="-44" r="1.5" opacity=".7"/><circle cx="-180" cy="-38" r="1.2" opacity=".5"/><circle cx="-90" cy="55" r="1.8" opacity=".8"/><circle cx="-150" cy="48" r="1.3" opacity=".6"/><circle cx="-220" cy="30" r="1" opacity=".4"/><circle cx="-250" cy="-20" r=".9" opacity=".4"/><circle cx="-200" cy="55" r="1" opacity=".4"/>
<circle cx="-40" cy="-60" r="1.5" opacity=".9" fill="#fff0b0"/><circle cx="-55" cy="60" r="1.6" opacity=".9" fill="#fff0b0"/>
</g>
<g stroke="#ffc766" stroke-linecap="round" fill="none">
<path d="M-60 -48l-22 -4" stroke-width="1.5" opacity=".7"/><path d="M-110 50l-24 2" stroke-width="1.3" opacity=".6"/><path d="M-160 -42l-20 -2" stroke-width="1" opacity=".5"/>
</g>
<circle r="70" fill="url(#glow)" opacity=".8"/>
<path d="M20 -36Q60 0 20 36" stroke="#fff3c4" stroke-width="2.5" fill="none" opacity=".8" filter="url(#b2)"/>
<use xlink:href="#rk" fill="url(#rock)"/>
<g clip-path="url(#rc)">
<ellipse cx="-12" cy="-9" rx="8" ry="6.5" fill="#2a2119"/><ellipse cx="-13" cy="-10.5" rx="6" ry="4.5" fill="#1a130d"/><path d="M-19 -6Q-12 -2 -5 -6" stroke="#857360" stroke-width="1" fill="none" opacity=".6"/>
<ellipse cx="-2" cy="14" rx="6" ry="5" fill="#2a2119"/><ellipse cx="-2.5" cy="13" rx="4.3" ry="3.3" fill="#1a130d"/><path d="M-7 16Q-2 19 3 16" stroke="#857360" stroke-width=".9" fill="none" opacity=".5"/>
<ellipse cx="-20" cy="12" rx="4" ry="3.2" fill="#241c14"/><ellipse cx="-20" cy="11.3" rx="2.8" ry="2" fill="#15100a"/>
<ellipse cx="4" cy="-20" rx="3.5" ry="2.8" fill="#241c14"/><ellipse cx="4" cy="-20.6" rx="2.4" ry="1.8" fill="#15100a"/>
<ellipse cx="-26" cy="0" rx="2.5" ry="2" fill="#15100a"/>
<ellipse cx="34" cy="0" rx="24" ry="42" fill="url(#hot)"/>
<path d="M28 -12L19 -3L24 8M30 8L21 16M14 -26L10 -16" stroke="#ffb13d" stroke-width="1.2" fill="none" opacity=".9" stroke-linecap="round"/>
</g>
<use xlink:href="#rk" fill="none" stroke="#0e0906" stroke-width="1.2" opacity=".6"/>
</g>
</svg>
```

我画了一颗在深蓝星空中斜向坠落的陨石：褐灰色的岩体布满陨石坑，前缘被高温烧得通红并带有发光裂纹，身后拖着一道由橙红渐变到亮白的长长火焰尾迹，四周飞散着火星，远处是夜色中的山丘剪影。

### m6 (陨石_zh; agente a6b406d3f07599879)

```svg
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 400 400">
<defs>
<radialGradient id="sky" cx=".7" cy=".2" r="1"><stop offset="0" stop-color="#2a1d4e"/><stop offset=".5" stop-color="#121033"/><stop offset="1" stop-color="#05040f"/></radialGradient>
<linearGradient id="tl" gradientUnits="userSpaceOnUse" x1="0" x2="300"><stop offset="0" stop-color="#fff5c0"/><stop offset=".25" stop-color="#ffb13b"/><stop offset=".6" stop-color="#e8502a" stop-opacity=".6"/><stop offset="1" stop-color="#7a1a3a" stop-opacity="0"/></linearGradient>
<linearGradient id="co" gradientUnits="userSpaceOnUse" x1="0" x2="220"><stop offset="0" stop-color="#fff"/><stop offset=".4" stop-color="#fff0a0" stop-opacity=".8"/><stop offset="1" stop-color="#ffd060" stop-opacity="0"/></linearGradient>
<radialGradient id="rg" cx=".3" cy=".35" r=".8"><stop offset="0" stop-color="#9c7a5e"/><stop offset=".5" stop-color="#5a4334"/><stop offset="1" stop-color="#2a1d16"/></radialGradient>
<radialGradient id="ht"><stop offset="0" stop-color="#fff3b0"/><stop offset=".4" stop-color="#ff9a2e"/><stop offset="1" stop-color="#ff5a1e" stop-opacity="0"/></radialGradient>
<filter id="b1" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>
<filter id="b2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="b3" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.5"/></filter>
<path id="rk" d="M38,2L31,19L16,31L-1,37L-20,31L-34,17L-39,-2L-31,-20L-17,-32L2,-37L20,-30L33,-16Z"/>
<clipPath id="rc"><use xlink:href="#rk"/></clipPath>
<path id="sp" d="M0,-5L1.2,-1.2L5,0L1.2,1.2L0,5L-1.2,1.2L-5,0L-1.2,-1.2Z" fill="#fff"/>
</defs>
<rect width="400" height="400" fill="url(#sky)"/>
<ellipse cx="90" cy="110" rx="120" ry="70" fill="#4a2a7a" opacity=".25" filter="url(#b2)"/>
<ellipse cx="320" cy="300" rx="100" ry="60" fill="#1f3a6a" opacity=".25" filter="url(#b2)"/>
<g fill="#fff">
<circle cx="22" cy="38" r="1.3"/><circle cx="68" cy="22" r="1"/><circle cx="118" cy="60" r="1.4"/><circle cx="170" cy="30" r="1.1"/><circle cx="236" cy="18" r="1.3"/><circle cx="300" cy="44" r="1"/><circle cx="372" cy="24" r="1.5"/><circle cx="40" cy="120" r="1.2"/><circle cx="86" cy="160" r="1"/><circle cx="28" cy="210" r="1.4"/><circle cx="360" cy="120" r="1.2"/><circle cx="385" cy="180" r="1"/><circle cx="330" cy="200" r="1.3"/><circle cx="60" cy="280" r="1"/><circle cx="300" cy="270" r="1.1"/><circle cx="210" cy="120" r="1"/><circle cx="260" cy="80" r="1.2"/><circle cx="150" cy="110" r="1"/><circle cx="380" cy="300" r="1.2"/><circle cx="20" cy="300" r="1"/>
</g>
<g fill="#fff" opacity=".5">
<circle cx="50" cy="60" r=".9"/><circle cx="100" cy="100" r=".8"/><circle cx="140" cy="20" r="1"/><circle cx="200" cy="70" r=".8"/><circle cx="280" cy="120" r=".9"/><circle cx="320" cy="20" r=".8"/><circle cx="350" cy="80" r="1"/><circle cx="390" cy="60" r=".8"/><circle cx="10" cy="160" r=".9"/><circle cx="70" cy="200" r=".8"/><circle cx="120" cy="230" r="1"/><circle cx="190" cy="170" r=".8"/><circle cx="250" cy="210" r=".9"/><circle cx="290" cy="160" r=".8"/><circle cx="340" cy="250" r="1"/><circle cx="370" cy="220" r=".8"/><circle cx="30" cy="250" r=".9"/><circle cx="90" cy="310" r=".8"/><circle cx="230" cy="300" r="1"/><circle cx="270" cy="330" r=".8"/><circle cx="150" cy="290" r=".9"/><circle cx="200" cy="20" r=".8"/><circle cx="310" cy="110" r="1"/><circle cx="355" cy="160" r=".8"/>
</g>
<use xlink:href="#sp" transform="translate(62,72)"/>
<use xlink:href="#sp" transform="translate(338,250)scale(.8)"/>
<use xlink:href="#sp" transform="translate(110,150)scale(.6)"/>
<path d="M0,342Q50,318 100,338T200,330T300,340T400,326V400H0Z" fill="#0a0818"/>
<path d="M0,362Q70,340 150,360T290,352T400,364V400H0Z" fill="#050410"/>
<ellipse cx="150" cy="348" rx="110" ry="18" fill="#ff7a2a" opacity=".18" filter="url(#b2)"/>
<g transform="translate(145,245)rotate(-35)">
<path d="M0,-50C80,-60 200,-30 310,-3L310,3C200,30 80,60 0,50Z" fill="url(#tl)" opacity=".45" filter="url(#b2)"/>
<path d="M0,-38C70,-46 180,-22 300,-2L300,2C180,22 70,46 0,38Z" fill="url(#tl)" filter="url(#b1)"/>
<path d="M0,-18C60,-22 140,-10 230,-1L230,1C140,10 60,22 0,18Z" fill="url(#co)" filter="url(#b3)"/>
<g fill="none" stroke-linecap="round" stroke-width="2">
<path d="M10,-30C70,-70 150,-60 250,-40" stroke="#ffb860" opacity=".5"/>
<path d="M14,32C80,70 160,58 240,46" stroke="#ff9a40" opacity=".45"/>
</g>
<g fill="#ffd27a">
<circle cx="70" cy="-48" r="2.2"/><circle cx="120" cy="52" r="1.8"/><circle cx="160" cy="-40" r="1.5"/><circle cx="210" cy="30" r="1.3"/><circle cx="95" cy="60" r="1.2"/><circle cx="250" cy="-20" r="1"/><circle cx="180" cy="-55" r="1.2"/><circle cx="140" cy="-62" r=".9"/>
</g>
<g fill="#ff7a30" opacity=".8">
<circle cx="90" cy="45" r="1.5"/><circle cx="200" cy="-34" r="1.2"/><circle cx="230" cy="40" r="1"/><circle cx="130" cy="-30" r="1.6"/>
</g>
<g stroke="#ff9a3a" stroke-width=".8">
<path d="M60,-46l5,-3 5,3-2,5-6,1Z" fill="#4a3528"/>
<path d="M100,58l4,-3 5,2-1,5-6,1Z" fill="#3a2820"/>
</g>
<circle cx="-6" r="52" fill="url(#ht)" opacity=".9" filter="url(#b1)"/>
<use xlink:href="#rk" fill="url(#rg)"/>
<ellipse cx="-6" cy="9" rx="10" ry="7.5" fill="#2a1c15"/><ellipse cx="-7" cy="8" rx="8" ry="5.5" fill="#3d2b21"/>
<ellipse cx="13" cy="-9" rx="7" ry="5" fill="#2a1c15"/><ellipse cx="12" cy="-10" rx="5.5" ry="3.6" fill="#3d2b21"/>
<ellipse cx="15" cy="15" rx="5" ry="4" fill="#241811"/><ellipse cx="14" cy="14" rx="3.8" ry="2.8" fill="#382619"/>
<ellipse cx="-20" cy="-13" rx="5" ry="3.8" fill="#241811"/><ellipse cx="-21" cy="-14" rx="3.6" ry="2.6" fill="#3a271a"/>
<ellipse cx="2" cy="-24" rx="3" ry="2.2" fill="#241811"/>
<g clip-path="url(#rc)">
<circle cx="-48" cy="4" r="42" fill="#ff8a2a" opacity=".85" filter="url(#b1)"/>
<circle cx="-56" r="38" fill="#fff0a0" opacity=".7" filter="url(#b1)"/>
<path d="M-39,-2L-31,-20L-17,-32" stroke="#ffe8a0" stroke-width="3" fill="none" stroke-linecap="round" opacity=".8"/>
</g>
<use xlink:href="#rk" fill="none" stroke="#1a110c" stroke-width="1.2" opacity=".7"/>
<g fill="none" stroke-linecap="round">
<path d="M-28,-6L-14,2L-8,16M-14,2L-2,-6" stroke="#ff9e3a" stroke-width="1.4" opacity=".9"/>
<path d="M-30,10L-18,18" stroke="#ff7a2a" stroke-width="1.2" opacity=".8"/>
</g>
</g>
</svg>
```

我画了一颗布满陨石坑、迎风面烧得通红的陨石，拖着一条由白转橙、散落火星和碎屑的炽热尾焰，从繁星点点的深夜天空斜斜坠向远处的山丘，火光映亮了地面。

### c1 (piedra_que_cayo_es; agente af5a18146019b6dd4)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#040714"/><stop offset=".55" stop-color="#101a3c"/><stop offset="1" stop-color="#3c2a48"/></linearGradient>
<linearGradient id="gnd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3d3029"/><stop offset="1" stop-color="#15100d"/></linearGradient>
<linearGradient id="trl" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".45" stop-color="#ffb347" stop-opacity=".55"/><stop offset="1" stop-color="#ff5a1f"/></linearGradient>
<radialGradient id="rck" cx=".35" cy=".3" r=".85"><stop offset="0" stop-color="#716c67"/><stop offset=".55" stop-color="#3a3533"/><stop offset="1" stop-color="#120f0d"/></radialGradient>
<radialGradient id="heat"><stop offset="0" stop-color="#ff8a2a" stop-opacity=".85"/><stop offset=".5" stop-color="#ff4d00" stop-opacity=".3"/><stop offset="1" stop-color="#ff4d00" stop-opacity="0"/></radialGradient>
<radialGradient id="crt"><stop offset="0" stop-color="#0b0705"/><stop offset=".7" stop-color="#22160e"/><stop offset="1" stop-color="#4b3b2d"/></radialGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.5"/></filter>
</defs>
<rect width="400" height="400" fill="url(#sky)"/>
<g fill="#fff">
<circle cx="22" cy="30" r="1.3"/><circle cx="58" cy="118" r=".9"/><circle cx="105" cy="48" r="1.1"/><circle cx="140" cy="20" r=".8"/><circle cx="170" cy="96" r="1.4"/><circle cx="205" cy="40" r=".9"/><circle cx="248" cy="130" r="1"/><circle cx="275" cy="22" r="1.2"/><circle cx="300" cy="88" r=".8"/><circle cx="335" cy="150" r="1.1"/><circle cx="360" cy="60" r="1.4"/><circle cx="120" cy="160" r=".9"/><circle cx="40" cy="190" r="1"/><circle cx="230" cy="190" r=".8"/><circle cx="370" cy="210" r=".9"/><circle cx="190" cy="140" r=".7"/><circle cx="85" cy="210" r=".8"/><circle cx="260" cy="70" r=".7"/>
</g>
<path d="M170,86 L172,96 L182,98 L172,100 L170,110 L168,100 L158,98 L168,96 Z" fill="#fff" opacity=".9"/>
<circle cx="68" cy="68" r="22" fill="#e9e4cf"/>
<circle cx="78" cy="60" r="20" fill="#0a1026"/>
<path d="M0,262 C40,246 80,258 120,250 C160,242 200,254 240,246 C280,238 320,254 360,246 L400,252 L400,400 L0,400 Z" fill="#1a1324"/>
<path d="M0,280 Q200,268 400,280 L400,400 L0,400 Z" fill="url(#gnd)"/>
<path d="M398,0 Q300,130 224,276 L196,268 Q290,120 392,-6 Z" fill="url(#trl)" filter="url(#blur)"/>
<path d="M396,2 Q300,125 210,272" fill="none" stroke="url(#trl)" stroke-width="1.6" stroke-linecap="round" opacity=".9"/>
<g fill="#ffc46b"><circle cx="330" cy="95" r="1.2"/><circle cx="292" cy="150" r="1.4"/><circle cx="262" cy="200" r="1.1"/><circle cx="240" cy="236" r="1.5"/><circle cx="310" cy="128" r=".9"/></g>
<ellipse cx="200" cy="322" rx="112" ry="30" fill="#2b1e15"/>
<ellipse cx="200" cy="320" rx="96" ry="24" fill="url(#crt)"/>
<g stroke="#0c0806" stroke-width="2" fill="none" stroke-linecap="round">
<path d="M92,318 Q70,330 40,336 T0,352"/><path d="M308,318 Q330,332 362,334 T400,348"/><path d="M120,340 Q100,360 70,372 T30,392"/><path d="M280,342 Q300,362 340,380 T380,398"/><path d="M190,348 Q180,370 160,395"/><path d="M226,348 Q240,368 250,392"/><path d="M150,344 Q140,356 128,358"/>
</g>
<ellipse cx="200" cy="305" rx="125" ry="78" fill="url(#heat)"/>
<g fill="#b59a7a" filter="url(#blur)"><ellipse cx="88" cy="302" rx="32" ry="12" opacity=".2"/><ellipse cx="314" cy="304" rx="34" ry="12" opacity=".2"/></g>
<path d="M150,305 L160,282 L178,268 L205,262 L232,270 L250,286 L256,306 L246,322 L222,330 L190,332 L162,324 Z" fill="url(#rck)" stroke="#090807" stroke-width="1.5" stroke-linejoin="round"/>
<path d="M160,282 L178,268 L205,262 L198,290 L170,296 Z" fill="#6a645f" opacity=".45"/>
<path d="M205,262 L232,270 L250,286 L228,294 L198,290 Z" fill="#26221f" opacity=".6"/>
<path d="M150,305 L170,296 L198,290 L190,332 L162,324 Z" fill="#1c1917" opacity=".55"/>
<path d="M228,294 L250,286 L256,306 L246,322 L222,330 Z" fill="#141210" opacity=".5"/>
<g fill="#0e0c0a" opacity=".85">
<ellipse cx="185" cy="280" rx="6" ry="4" transform="rotate(-20 185 280)"/><ellipse cx="216" cy="275" rx="5" ry="3.5"/><ellipse cx="236" cy="300" rx="7" ry="4" transform="rotate(25 236 300)"/><ellipse cx="172" cy="308" rx="5" ry="3"/><ellipse cx="206" cy="313" rx="8" ry="4.5"/><ellipse cx="242" cy="316" rx="4" ry="2.5"/><ellipse cx="168" cy="290" rx="4" ry="2.5"/>
</g>
<g fill="none" stroke="#857d76" stroke-width=".8" opacity=".7"><path d="M180,284 Q185,287 191,282"/><path d="M212,279 Q216,281 221,277"/><path d="M199,318 Q206,320 214,316"/></g>
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
<g stroke="#ff7a1a" stroke-width="1.4" filter="url(#soft)"><path d="M174,298 L188,302 L200,297 L213,306 L227,303"/><path d="M196,270 L203,283 L198,291"/><path d="M238,288 L245,300 L240,312"/><path d="M165,312 L178,318 L192,315"/></g>
<g stroke="#ffd27a" stroke-width=".6"><path d="M174,298 L188,302 L200,297 L213,306 L227,303"/><path d="M196,270 L203,283 L198,291"/><path d="M238,288 L245,300 L240,312"/><path d="M165,312 L178,318 L192,315"/></g>
</g>
<path d="M150,305 L162,324 L190,332 L222,330 L246,322 L256,306" fill="none" stroke="#ff6a1a" stroke-width="2.2" opacity=".75" filter="url(#soft)"/>
<path d="M160,282 L178,268 L205,262 L232,270" fill="none" stroke="#a9a29b" stroke-width="1.2" opacity=".8"/>
<path d="M98,322 Q200,362 302,322 Q200,338 98,322 Z" fill="#3a2b20"/>
<g fill="#4b3a2b">
<path d="M110,326 L118,318 L128,322 L124,330 Z"/><path d="M270,328 L280,320 L292,326 L286,334 Z"/><path d="M160,338 L168,332 L176,336 L172,342 Z"/><path d="M225,340 L233,334 L241,340 L236,345 Z"/><path d="M70,306 L78,300 L88,304 L84,312 Z"/><path d="M322,310 L330,304 L340,308 L336,316 Z"/>
</g>
<g fill="#9c9c9c" filter="url(#blur)">
<ellipse cx="206" cy="248" rx="22" ry="14" opacity=".3"/><ellipse cx="194" cy="220" rx="18" ry="12" opacity=".24"/><ellipse cx="212" cy="194" rx="20" ry="13" opacity=".17"/><ellipse cx="200" cy="166" rx="24" ry="14" opacity=".11"/>
</g>
<g fill="#ffb347">
<circle cx="150" cy="266" r="1.4"/><circle cx="262" cy="256" r="1.1"/><circle cx="130" cy="296" r="1"/><circle cx="286" cy="300" r="1.3"/><circle cx="175" cy="246" r=".9"/><circle cx="242" cy="240" r="1"/><circle cx="118" cy="330" r=".9"/><circle cx="300" cy="334" r="1.1"/>
</g>
<g stroke="#ff6a1a" stroke-width="1" fill="none" stroke-linecap="round" opacity=".55" filter="url(#soft)">
<path d="M104,318 Q90,326 72,330"/><path d="M296,318 Q312,328 330,331"/><path d="M190,348 Q184,360 176,372"/>
</g>
</svg>
```

Dibujé un meteorito recién caído, todavía incandescente, hundido en su cráter entre grietas, tierra levantada y humo, bajo un cielo nocturno con luna y estrellas donde aún se ve la estela de fuego por la que bajó.

### c2 (piedra_que_cayo_es; agente a4f8b05c145780bdd)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#040714"/><stop offset=".55" stop-color="#121a3a"/><stop offset="1" stop-color="#3b2b4c"/></linearGradient>
<linearGradient id="gnd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5c4836"/><stop offset="1" stop-color="#241b14"/></linearGradient>
<linearGradient id="trl" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd27a" stop-opacity="0"/><stop offset=".6" stop-color="#ff9a3c" stop-opacity=".55"/><stop offset="1" stop-color="#fff3c4" stop-opacity=".95"/></linearGradient>
<radialGradient id="rck" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#726c66"/><stop offset=".5" stop-color="#3a3733"/><stop offset="1" stop-color="#120f0c"/></radialGradient>
<radialGradient id="glw"><stop offset="0" stop-color="#ff7a1a" stop-opacity=".75"/><stop offset="1" stop-color="#ff7a1a" stop-opacity="0"/></radialGradient>
<radialGradient id="crt"><stop offset="0" stop-color="#17100a"/><stop offset=".7" stop-color="#2c2119"/><stop offset="1" stop-color="#4b3b2d"/></radialGradient>
<filter id="b1" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.2"/></filter>
<filter id="b3" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="b8" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="8"/></filter>
<mask id="mn"><circle cx="70" cy="75" r="22" fill="#fff"/><circle cx="81" cy="69" r="20"/></mask>
</defs>
<rect width="400" height="400" fill="url(#sky)"/>
<g fill="#fff">
<circle cx="22" cy="30" r="1.2"/><circle cx="120" cy="85" r=".8"/><circle cx="95" cy="22" r="1.5" opacity=".9"/><circle cx="140" cy="60" r=".9"/><circle cx="170" cy="18" r="1.1"/><circle cx="210" cy="48" r=".7"/><circle cx="250" cy="90" r="1.3"/><circle cx="300" cy="40" r=".9"/><circle cx="330" cy="110" r="1.1"/><circle cx="40" cy="130" r="1"/><circle cx="110" cy="150" r=".7"/><circle cx="180" cy="120" r="1.4" opacity=".8"/><circle cx="235" cy="160" r=".8"/><circle cx="70" cy="190" r="1.1"/><circle cx="150" cy="200" r=".7"/><circle cx="350" cy="190" r="1"/><circle cx="385" cy="80" r=".8"/><circle cx="20" cy="220" r=".9"/><circle cx="275" cy="20" r=".7"/><circle cx="365" cy="230" r=".7"/>
</g>
<circle cx="70" cy="75" r="30" fill="#e9e5d9" opacity=".08" filter="url(#b8)"/>
<circle cx="70" cy="75" r="22" fill="#e9e5d9" mask="url(#mn)"/>
<path d="M0 268Q50 232 120 256Q170 222 240 252Q310 226 400 250V280H0Z" fill="#1c1728"/>
<path d="M392 4Q300 140 216 256" stroke="#ff9a3c" stroke-width="12" fill="none" opacity=".3" filter="url(#b8)"/>
<path d="M368 0H400V26Q318 140 226 262L208 250Q292 136 368 0Z" fill="url(#trl)" filter="url(#b3)"/>
<path d="M392 4Q300 140 216 256" stroke="#fff1c8" stroke-width="1.5" fill="none" opacity=".85" stroke-linecap="round"/>
<path d="M0 266Q100 244 200 258T400 250V400H0Z" fill="url(#gnd)"/>
<g fill="#8f7558" opacity=".16"><path d="M110 335L20 398L70 400Z"/><path d="M290 338L380 398L330 400Z"/><path d="M190 356L165 400H235Z"/></g>
<ellipse cx="200" cy="318" rx="125" ry="40" fill="#6a5442"/>
<ellipse cx="200" cy="318" rx="105" ry="30" fill="url(#crt)"/>
<path d="M82 318A118 34 0 0 1 318 318" stroke="#8d7159" stroke-width="3" fill="none" opacity=".7"/>
<path d="M82 318A118 34 0 0 0 318 318" stroke="#150e09" stroke-width="4" fill="none" opacity=".45"/>
<g stroke="#120c08" stroke-width="1.5" fill="none" stroke-linecap="round"><path d="M78 322L48 316L28 330"/><path d="M322 320L352 310L382 318"/><path d="M160 352L142 374L146 398"/><path d="M250 354L262 378L256 400"/><path d="M100 345L80 368"/><path d="M300 348L322 370"/></g>
<ellipse cx="200" cy="302" rx="150" ry="42" fill="#b9a58e" opacity=".07" filter="url(#b8)"/>
<ellipse cx="208" cy="322" rx="72" ry="24" fill="url(#glw)" filter="url(#b3)"/>
<g fill="#3a3734" stroke="#0a0908" stroke-width="1"><path d="M96 332l8-6 9 3-2 8-10 2z"/><path d="M300 330l7-5 8 4-3 7-9 1z"/><path d="M130 365l6-5 8 2-1 7-9 2z"/><path d="M275 362l5-4 7 2-1 6-8 1z"/><path d="M60 352l5-3 5 2-1 5-6 1z"/><path d="M340 352l5-4 6 3-2 5-7 1z"/><path d="M218 374l5-3 5 2-1 5-6 1z"/><path d="M110 300l4-3 4 2-1 4-5 1z"/></g>
<g fill="none" stroke="#cfcbd6" stroke-linecap="round" filter="url(#b3)"><path d="M238 258Q252 228 238 200Q226 178 244 150" stroke-width="7" opacity=".26"/><path d="M205 248Q195 220 210 196Q222 176 206 150" stroke-width="5" opacity=".2"/><path d="M258 268Q278 240 270 214" stroke-width="4" opacity=".15"/></g>
<path d="M150 300L160 268L185 250L222 246L252 262L268 290L258 318L228 332L188 334L158 322Z" fill="url(#rck)" stroke="#0a0908" stroke-width="2" stroke-linejoin="round"/>
<path d="M160 268L185 250L222 246L206 276L172 286Z" fill="#8a837c" opacity=".35"/>
<path d="M206 276L222 246L252 262L240 292Z" fill="#5a5450" opacity=".4"/>
<path d="M252 262L268 290L258 318L228 332L240 292Z" fill="#070605" opacity=".55"/>
<path d="M158 322L188 334L228 332L240 292L206 276L172 286L150 300Z" fill="#000" opacity=".2"/>
<g fill="#161311"><ellipse cx="192" cy="292" rx="9" ry="6"/><ellipse cx="215" cy="305" rx="7" ry="5"/><ellipse cx="176" cy="308" rx="6" ry="4.5"/><ellipse cx="236" cy="278" rx="6" ry="4"/><ellipse cx="200" cy="265" rx="5" ry="3.5"/><ellipse cx="248" cy="300" rx="5" ry="4"/></g>
<g stroke="#9a928a" stroke-width="1" fill="none" opacity=".55"><path d="M184 290Q192 284 200 290"/><path d="M209 303Q215 298 221 303"/><path d="M171 306Q176 302 181 306"/><path d="M231 276Q236 272 241 276"/><path d="M196 263Q200 260 204 263"/></g>
<g fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M166 312L182 322L198 318L212 328" stroke="#ff8a2a" stroke-width="3" opacity=".7" filter="url(#b1)"/><path d="M166 312L182 322L198 318L212 328" stroke="#ffd08a" stroke-width="1.2"/><path d="M232 322L246 310L256 312" stroke="#ff8a2a" stroke-width="3" opacity=".7" filter="url(#b1)"/><path d="M232 322L246 310L256 312" stroke="#ffd08a" stroke-width="1.2"/></g>
<path d="M158 322Q192 342 228 332" stroke="#ff7a1a" stroke-width="2.5" fill="none" opacity=".6" filter="url(#b1)"/>
<path d="M186 254L196 250L205 252" stroke="#fff" stroke-width="1.5" fill="none" opacity=".6" stroke-linecap="round"/>
<g fill="#ffb347"><circle cx="150" cy="318" r="1.5"/><circle cx="266" cy="306" r="1.2"/><circle cx="240" cy="340" r="1"/><circle cx="170" cy="340" r="1.3"/><circle cx="135" cy="330" r=".9"/><circle cx="282" cy="326" r="1"/></g>
</svg>
```

Dibujé un meteorito recién caído: una piedra oscura y picada, todavía con grietas al rojo vivo y humo saliendo, hundida en su cráter bajo un cielo nocturno con luna y la estela luminosa que dejó al caer.

### s1 (ensisheim_es; agente aacf3ec2eb51bb921)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ece5d7"/><stop offset="1" stop-color="#c7bba3"/></linearGradient>
<radialGradient id="vg" cx=".5" cy=".45" r=".75"><stop offset=".5" stop-color="#3a2a18" stop-opacity="0"/><stop offset="1" stop-color="#3a2a18" stop-opacity=".4"/></radialGradient>
<linearGradient id="cr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6e5e4f"/><stop offset=".45" stop-color="#3a302a"/><stop offset="1" stop-color="#1a1513"/></linearGradient>
<linearGradient id="cu" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d9d2c5"/><stop offset="1" stop-color="#999185"/></linearGradient>
<linearGradient id="wd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8b5a33"/><stop offset="1" stop-color="#472a16"/></linearGradient>
<linearGradient id="wt" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#a26e3e"/><stop offset=".5" stop-color="#c38d55"/><stop offset="1" stop-color="#946236"/></linearGradient>
<linearGradient id="br" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e6c57f"/><stop offset=".5" stop-color="#b58c3c"/><stop offset="1" stop-color="#d6b26c"/></linearGradient>
<linearGradient id="st" gradientUnits="userSpaceOnUse" x1="392" y1="16" x2="318" y2="80"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity=".85"/></linearGradient>
<radialGradient id="sh"><stop offset="0" stop-color="#000" stop-opacity=".55"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".05" numOctaves="4" seed="7" result="n"/><feColorMatrix in="n" values=".6 0 0 0 .55 .6 0 0 0 .55 .6 0 0 0 .55 0 0 0 0 1" result="g"/><feComposite in="g" in2="SourceGraphic" operator="in" result="t"/><feBlend in="SourceGraphic" in2="t" mode="multiply"/></filter>
<filter id="grain" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3" result="n"/><feColorMatrix in="n" values=".4 0 0 0 .75 .4 0 0 0 .75 .4 0 0 0 .75 0 0 0 0 1" result="g"/><feComposite in="g" in2="SourceGraphic" operator="in" result="t"/><feBlend in="SourceGraphic" in2="t" mode="multiply"/></filter>
<clipPath id="cb"><path d="M90 262L100 205 140 156 196 124 262 134 304 170 326 222 314 276 256 312 172 322 112 300Z"/></clipPath>
<clipPath id="cc"><path d="M262 134L304 170 326 222 314 276 256 312 240 250 236 180Z"/></clipPath>
</defs>
<rect width="400" height="400" fill="url(#bg)"/>
<rect width="400" height="400" fill="url(#vg)"/>
<text x="200" y="48" font-family="Georgia,'Times New Roman',serif" font-size="14" font-style="italic" fill="#5a4833" text-anchor="middle" letter-spacing=".5">Der Donnerstein von Ensisheim</text>
<path d="M392 16Q358 44 318 80" stroke="url(#st)" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M392 16Q358 44 318 80" stroke="#fff" stroke-width="1" fill="none" opacity=".6"/>
<circle cx="318" cy="80" r="2.5" fill="#fff"/>
<circle cx="318" cy="80" r="6" fill="#fff" opacity=".25"/>
<rect x="58" y="372" width="284" height="18" fill="#2b1a0e"/>
<rect x="58" y="336" width="284" height="36" fill="url(#wd)"/>
<path d="M78 318H322L342 336H58Z" fill="url(#wt)"/>
<path d="M78 318H322" stroke="#dcaa6e" stroke-width="1" opacity=".7"/>
<rect x="146" y="344" width="108" height="22" rx="2" fill="url(#br)" stroke="#6b4d1e" stroke-width=".8"/>
<text x="200" y="353.5" font-family="Georgia,serif" font-size="7.5" fill="#3a2a10" text-anchor="middle" letter-spacing="1.6">ENSISHEIM</text>
<text x="200" y="362.5" font-family="Georgia,serif" font-size="6.5" fill="#3a2a10" text-anchor="middle" letter-spacing=".8">7 · XI · 1492</text>
<ellipse cx="208" cy="323" rx="135" ry="11" fill="url(#sh)"/>
<g filter="url(#rough)">
<path d="M90 262L100 205 140 156 196 124 262 134 304 170 326 222 314 276 256 312 172 322 112 300Z" fill="url(#cr)"/>
</g>
<g clip-path="url(#cb)">
<ellipse cx="150" cy="200" rx="24" ry="14" fill="#8a7a68" opacity=".22" transform="rotate(-25 150 200)"/>
<ellipse cx="192" cy="242" rx="18" ry="11" fill="#000" opacity=".28"/>
<ellipse cx="128" cy="266" rx="16" ry="10" fill="#8a7a68" opacity=".18"/>
<ellipse cx="212" cy="176" rx="14" ry="9" fill="#000" opacity=".22"/>
<ellipse cx="158" cy="296" rx="26" ry="9" fill="#000" opacity=".3"/>
<ellipse cx="118" cy="230" rx="11" ry="22" fill="#8c4a2a" opacity=".2"/>
<ellipse cx="206" cy="290" rx="10" ry="16" fill="#7a3f22" opacity=".16"/>
<path d="M100 205L140 156 196 124 262 134" stroke="#a09080" stroke-width="2.5" fill="none" opacity=".35" stroke-linejoin="round"/>
<path d="M90 262L112 300 172 322" stroke="#000" stroke-width="3" fill="none" opacity=".35"/>
</g>
<g filter="url(#grain)">
<path d="M262 134L304 170 326 222 314 276 256 312 240 250 236 180Z" fill="url(#cu)"/>
</g>
<g clip-path="url(#cc)">
<path d="M240 250Q268 232 298 252" stroke="#8c8478" stroke-width=".7" fill="none" opacity=".5"/>
<path d="M250 170Q280 190 312 188" stroke="#8c8478" stroke-width=".5" fill="none" opacity=".4"/>
<g fill="#e4ded3"><circle cx="258" cy="160" r="2.2"/><circle cx="290" cy="190" r="2.8"/><circle cx="255" cy="222" r="1.8"/><circle cx="292" cy="270" r="1.8"/><circle cx="250" cy="285" r="1.3"/><circle cx="280" cy="230" r="3"/><circle cx="262" cy="200" r="1.4"/><circle cx="310" cy="245" r="1.5"/></g>
<g fill="#8b8377"><circle cx="275" cy="175" r="1.6"/><circle cx="300" cy="215" r="2"/><circle cx="268" cy="262" r="2.4"/><circle cx="276" cy="295" r="2"/><circle cx="246" cy="236" r="1.5"/><circle cx="296" cy="180" r="1.2"/><circle cx="270" cy="215" r="1"/><circle cx="286" cy="285" r="1.3"/><circle cx="318" cy="228" r="1.2"/></g>
<g fill="#fbfaf7"><circle cx="298" cy="250" r="1.1"/><circle cx="248" cy="195" r=".9"/><circle cx="285" cy="205" r="1"/><circle cx="266" cy="240" r=".9"/><circle cx="305" cy="232" r=".8"/><circle cx="258" cy="300" r=".9"/><circle cx="282" cy="160" r=".8"/><circle cx="244" cy="268" r=".8"/></g>
<g fill="#4e463f" opacity=".7"><circle cx="252" cy="248" r=".9"/><circle cx="302" cy="200" r=".8"/><circle cx="272" cy="280" r="1"/><circle cx="288" cy="240" r=".7"/><circle cx="264" cy="182" r=".8"/></g>
</g>
<path d="M262 134L236 180 240 250 256 312" stroke="#1a1513" stroke-width="1.5" fill="none" opacity=".8"/>
<path d="M262 134L304 170 326 222 314 276 256 312" stroke="#2a2320" stroke-width="1.2" fill="none" opacity=".8"/>
<path d="M90 262L100 205 140 156 196 124 262 134" stroke="#1a1513" stroke-width="1" fill="none" opacity=".6"/>
<path d="M90 262L112 300 172 322 256 312" stroke="#1a1513" stroke-width="1" fill="none" opacity=".6"/>
</svg>
```

Dibujé la piedra de Ensisheim —el "Donnerstein" que cayó el 7 de noviembre de 1492— como un meteorito oscuro de corteza de fusión con una cara cortada gris clara salpicada de cóndrulos y granos metálicos, apoyado en un pedestal de madera con placa de bronce, y una estela luminosa en el cielo como guiño a su caída.

### s2 (ensisheim_es; agente a8e8e5d292fb8b818)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<radialGradient id="w" cx=".5" cy=".35" r=".8"><stop offset="0" stop-color="#4d4237"/><stop offset="1" stop-color="#171310"/></radialGradient>
<linearGradient id="sky" x2="0" y2="1"><stop offset="0" stop-color="#4f86c4"/><stop offset="1" stop-color="#dbe7f1"/></linearGradient>
<linearGradient id="fb" gradientUnits="userSpaceOnUse" x1="252" y1="46" x2="172" y2="112"><stop offset="0" stop-color="#ff8a2a" stop-opacity="0"/><stop offset=".55" stop-color="#ffbd5e"/><stop offset="1" stop-color="#fff"/></linearGradient>
<linearGradient id="pf"><stop offset="0" stop-color="#5a5042"/><stop offset=".45" stop-color="#8d826e"/><stop offset="1" stop-color="#4a4136"/></linearGradient>
<radialGradient id="cr" cx=".33" cy=".28" r=".85"><stop offset="0" stop-color="#5e4c3c"/><stop offset=".5" stop-color="#2d241c"/><stop offset="1" stop-color="#0e0a08"/></radialGradient>
<linearGradient id="ch" x2="1" y2="1"><stop offset="0" stop-color="#c6c0b3"/><stop offset="1" stop-color="#726a5f"/></linearGradient>
<pattern id="mas" width="64" height="32" patternUnits="userSpaceOnUse"><path d="M0 0H64M0 16H64M32 0V16M0 16V32" stroke="#000" stroke-width="1.2" fill="none"/></pattern>
<filter id="bl" x="-20%" y="-150%" width="140%" height="400%"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="gr"><feTurbulence type="fractalNoise" baseFrequency=".75" numOctaves="3" seed="4"/><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1.4 -.45"/></filter>
<filter id="rg" x="-8%" y="-8%" width="116%" height="116%"><feTurbulence type="fractalNoise" baseFrequency=".05" numOctaves="2" seed="9" result="t"/><feDisplacementMap in="SourceGraphic" in2="t" scale="6" xChannelSelector="R" yChannelSelector="G"/></filter>
<clipPath id="wc"><path d="M135 250V125Q135 62 200 38Q265 62 265 125V250Z"/></clipPath>
<clipPath id="sc"><path d="M88 240C80 208 100 168 135 158C150 153 160 136 185 134C215 130 235 148 262 158C290 168 318 193 312 223C308 248 290 270 262 280C230 291 170 293 130 283C105 276 92 260 88 240Z"/></clipPath>
</defs>
<rect width="400" height="400" fill="url(#w)"/>
<rect width="400" height="330" fill="url(#mas)" opacity=".14"/>
<rect y="330" width="400" height="70" fill="#120e0b"/>
<path d="M135 250V125Q135 62 200 38Q265 62 265 125V250Z" fill="#6a5e4f" stroke="#6a5e4f" stroke-width="20" stroke-linejoin="round"/>
<g clip-path="url(#wc)">
<rect x="130" y="30" width="140" height="225" fill="url(#sky)"/>
<g fill="#fff"><ellipse cx="150" cy="98" rx="16" ry="5" opacity=".5"/><ellipse cx="238" cy="84" rx="14" ry="4.5" opacity=".45"/></g>
<path d="M252 46L172 112" stroke="url(#fb)" stroke-width="10" stroke-linecap="round" opacity=".6" filter="url(#gl)"/>
<path d="M252 46L172 112" stroke="url(#fb)" stroke-width="3" stroke-linecap="round"/>
<circle cx="172" cy="112" r="12" fill="#ffb060" opacity=".55" filter="url(#gl)"/>
<circle cx="172" cy="112" r="4.5" fill="#fff"/>
<g fill="#fff" opacity=".85"><circle cx="183" cy="103" r="1.2"/><circle cx="191" cy="100" r=".9"/><circle cx="178" cy="118" r="1"/></g>
</g>
<path d="M135 250V125Q135 62 200 38Q265 62 265 125V250Z" fill="none" stroke="#2a221b" stroke-width="2.5"/>
<rect x="70" y="300" width="260" height="100" fill="url(#pf)"/>
<polygon points="70,300 330,300 312,286 88,286" fill="#a3977f"/>
<rect x="70" y="300" width="260" height="5" fill="#b9ad94"/>
<rect x="70" y="392" width="260" height="8" fill="#332b23"/>
<rect x="138" y="326" width="124" height="40" rx="3" fill="#2b2119" stroke="#c7a25a" stroke-width="1.5"/>
<g font-family="Georgia,serif" text-anchor="middle"><text x="200" y="344" font-size="12" letter-spacing="2.5" fill="#e3c57a">ENSISHEIM</text><text x="200" y="358" font-size="9" letter-spacing="1" fill="#c9ad6a">7 · XI · 1492</text></g>
<ellipse cx="200" cy="292" rx="122" ry="9" fill="#000" opacity=".6" filter="url(#bl)"/>
<g filter="url(#rg)">
<path d="M88 240C80 208 100 168 135 158C150 153 160 136 185 134C215 130 235 148 262 158C290 168 318 193 312 223C308 248 290 270 262 280C230 291 170 293 130 283C105 276 92 260 88 240Z" fill="url(#cr)" stroke="#000" stroke-opacity=".45" stroke-width="1.5"/>
<g clip-path="url(#sc)">
<ellipse cx="150" cy="178" rx="44" ry="24" fill="#8c7661" opacity=".4" filter="url(#bl)"/>
<path d="M88 240C80 208 100 168 135 158C150 153 160 136 185 134C215 130 235 148 262 158" fill="none" stroke="#86705b" stroke-width="3" opacity=".45"/>
<g fill="#130e0b"><ellipse cx="170" cy="170" rx="14" ry="9" opacity=".6"/><ellipse cx="210" cy="158" rx="11" ry="7" opacity=".55" transform="rotate(-15 210 158)"/><ellipse cx="125" cy="215" rx="12" ry="8" opacity=".55"/><ellipse cx="160" cy="240" rx="16" ry="10" opacity=".5"/><ellipse cx="205" cy="215" rx="10" ry="7" opacity=".5"/><ellipse cx="245" cy="170" rx="9" ry="6" opacity=".5"/><ellipse cx="200" cy="262" rx="13" ry="7" opacity=".45"/><ellipse cx="110" cy="250" rx="8" ry="6" opacity=".5"/></g>
<g fill="none" stroke="#6e5a48" stroke-width="1.3" opacity=".55"><path d="M158 173Q170 182 184 173"/><path d="M146 243Q160 253 176 243"/><path d="M115 217Q125 226 137 217"/><path d="M197 217Q205 224 215 217"/><path d="M238 172Q245 178 253 172"/></g>
<path d="M238 190C264 184 294 200 302 224C306 248 284 266 258 270C240 264 232 228 238 190Z" fill="url(#ch)" stroke="#3b3028" stroke-width="1.5"/>
<g fill="#8f897d"><circle cx="258" cy="212" r="3.2"/><circle cx="276" cy="232" r="2.6"/><circle cx="250" cy="245" r="2.2"/><circle cx="286" cy="214" r="2"/><circle cx="266" cy="256" r="2.4"/><circle cx="246" cy="220" r="1.6"/><circle cx="290" cy="240" r="1.8"/></g>
<g fill="#ece6d6"><circle cx="268" cy="222" r="1.1"/><circle cx="254" cy="232" r=".9"/><circle cx="282" cy="246" r="1"/><circle cx="262" cy="200" r=".8"/><circle cx="292" cy="230" r=".9"/><circle cx="256" cy="258" r=".8"/></g>
<g fill="#55504a" opacity=".7"><circle cx="248" cy="204" r="1.2"/><circle cx="274" cy="252" r="1.3"/><circle cx="294" cy="222" r="1"/><circle cx="262" cy="240" r=".9"/></g>
<rect x="80" y="125" width="245" height="175" filter="url(#gr)" opacity=".9"/>
</g>
</g>
<g fill="none" stroke-linecap="round" stroke-dasharray="7 9">
<path d="M110 296C108 250 128 190 180 152C215 138 256 152 283 182C302 204 300 262 298 296" stroke="#000" stroke-width="8" opacity=".45" transform="translate(2 3)"/>
<path d="M110 296C108 250 128 190 180 152C215 138 256 152 283 182C302 204 300 262 298 296" stroke="#8f8b84" stroke-width="7"/>
<path d="M110 296C108 250 128 190 180 152C215 138 256 152 283 182C302 204 300 262 298 296" stroke="#35322e" stroke-width="2.5"/>
<path d="M110 296C108 250 128 190 180 152C215 138 256 152 283 182C302 204 300 262 298 296" stroke="#a09b93" stroke-width="3" stroke-dasharray="6 10" stroke-dashoffset="7.5"/>
</g>
<g fill="#4a443d"><rect x="102" y="294" width="16" height="6" rx="1"/><rect x="290" y="294" width="16" height="6" rx="1"/></g>
<g fill="none" stroke="#7b766e" stroke-width="3"><circle cx="110" cy="297" r="5"/><circle cx="298" cy="297" r="5"/></g>
</svg>
```

Dibujé la piedra de Ensisheim —la condrita que cayó el 7 de noviembre de 1492— negra de costra de fusión y con una cara cortada gris llena de cóndrulos, encadenada sobre un pedestal con su placa, frente a una ventana gótica por la que cruza el bólido de aquel mediodía.

### n1 (no_exista_es; agente a7d2d8d1a94d04196)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="sky" cx="30%" cy="70%" r="90%">
      <stop offset="0" stop-color="#15224a"/>
      <stop offset="1" stop-color="#040711"/>
    </radialGradient>
    <radialGradient id="halo">
      <stop offset="0" stop-color="#8fe3ff" stop-opacity=".45"/>
      <stop offset="1" stop-color="#8fe3ff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="inner" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0c2250"/>
      <stop offset=".55" stop-color="#2a6ea8"/>
      <stop offset="1" stop-color="#7fc6e8"/>
    </linearGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1c6fa8"/>
      <stop offset="1" stop-color="#03142e"/>
    </linearGradient>
    <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity=".45"/>
      <stop offset=".4" stop-color="#fff" stop-opacity=".05"/>
      <stop offset="1" stop-color="#9ad7ff" stop-opacity=".3"/>
    </linearGradient>
    <linearGradient id="tail" gradientUnits="userSpaceOnUse" x1="215" y1="195" x2="400" y2="0">
      <stop offset="0" stop-color="#c8f4ff" stop-opacity=".85"/>
      <stop offset=".5" stop-color="#7fd0ff" stop-opacity=".35"/>
      <stop offset="1" stop-color="#7fd0ff" stop-opacity="0"/>
    </linearGradient>
    <filter id="blur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5"/>
    </filter>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <path id="rock" d="M98,205 L140,172 L195,180 L228,222 L226,272 L198,315 L150,328 L105,305 L78,262 Z"/>
    <clipPath id="cut">
      <path d="M98,205 L140,172 L195,180 L228,222 L226,272 L198,315 L150,328 L105,305 L78,262 Z"/>
    </clipPath>
    <path id="hex" d="M0,-6 5,-3 5,3 0,6 -5,3 -5,-3Z"/>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>

  <g fill="#fff">
    <circle cx="22" cy="38" r="1.2"/>
    <circle cx="64" cy="96" r=".8" opacity=".7"/>
    <circle cx="120" cy="30" r="1"/>
    <circle cx="210" cy="60" r=".7" opacity=".6"/>
    <circle cx="45" cy="180" r=".9" opacity=".8"/>
    <circle cx="30" cy="300" r="1.1"/>
    <circle cx="90" cy="370" r=".8" opacity=".7"/>
    <circle cx="200" cy="380" r="1.2"/>
    <circle cx="300" cy="330" r=".9" opacity=".8"/>
    <circle cx="360" cy="250" r="1.3"/>
    <circle cx="380" cy="160" r=".8" opacity=".6"/>
    <circle cx="250" cy="290" r=".7" opacity=".7"/>
    <circle cx="330" cy="370" r="1"/>
    <circle cx="160" cy="120" r=".9" opacity=".8"/>
    <circle cx="280" cy="30" r="1.1"/>
    <circle cx="370" cy="330" r=".6" opacity=".5"/>
    <circle cx="110" cy="340" r=".6" opacity=".6"/>
    <circle cx="20" cy="240" r=".7" opacity=".7"/>
  </g>

  <circle cx="150" cy="250" r="105" fill="url(#halo)"/>

  <path d="M202,180 C270,110 335,55 405,2 C355,65 300,150 234,236 Z" fill="url(#tail)" filter="url(#blur)"/>
  <path d="M207,186 C270,120 330,65 395,10 C340,75 290,150 231,228 Z" fill="url(#tail)" opacity=".8"/>

  <g fill="#e8fbff" stroke="#fff" stroke-width=".6">
    <use href="#hex" transform="translate(248,170) rotate(15) scale(1.3)" opacity=".9"/>
    <use href="#hex" transform="translate(275,150) rotate(40) scale(.9)" opacity=".7"/>
    <use href="#hex" transform="translate(300,120) rotate(10) scale(1.1)" opacity=".6"/>
    <use href="#hex" transform="translate(330,95) rotate(55) scale(.7)" opacity=".5"/>
    <use href="#hex" transform="translate(355,60) rotate(25) scale(.8)" opacity=".4"/>
    <use href="#hex" transform="translate(262,205) rotate(70) scale(.6)" opacity=".6"/>
    <use href="#hex" transform="translate(318,142) rotate(5) scale(.5)" opacity=".4"/>
    <use href="#hex" transform="translate(378,38) rotate(35) scale(.5)" opacity=".3"/>
  </g>

  <g clip-path="url(#cut)">
    <rect x="70" y="165" width="170" height="170" fill="url(#inner)"/>
    <circle cx="185" cy="218" r="10" fill="#fff6d0" filter="url(#glow)"/>
    <path d="M118,268 Q135,250 152,268 Z" fill="#071a33"/>
    <rect x="133.5" y="247" width="3" height="13" fill="#ececec"/>
    <path d="M135,246 L175,236 L175,256 Z" fill="#fff3a0" opacity=".15"/>
    <circle cx="135" cy="246" r="1.8" fill="#fff3a0" filter="url(#glow)"/>
    <path d="M60,268 Q80,258 100,268 T140,268 T180,268 T220,268 T260,268 V340 H60 Z" fill="url(#sea)"/>
    <path d="M60,268 Q80,258 100,268 T140,268 T180,268 T220,268 T260,268" fill="none" stroke="#bfefff" stroke-width="1.2" opacity=".8"/>
    <path d="M178,280 H192 M181,290 H189 M183,300 H187" stroke="#fff6d0" stroke-width="1.5" opacity=".6" stroke-linecap="round"/>
    <path d="M60,285 Q90,278 120,286 T180,286 T240,284" fill="none" stroke="#5db7e3" stroke-width=".8" opacity=".5"/>
    <path d="M70,305 Q110,298 150,306 T230,304" fill="none" stroke="#5db7e3" stroke-width=".8" opacity=".4"/>
  </g>

  <use href="#rock" fill="url(#glass)" stroke="#e9fbff" stroke-width="2" stroke-linejoin="round"/>
  <path d="M140,172 L150,250 L228,222 M150,250 L105,305 M150,250 L198,315 M98,205 L150,250" fill="none" stroke="#fff" stroke-width=".8" opacity=".35"/>
  <ellipse cx="120" cy="200" rx="24" ry="9" transform="rotate(-35 120 200)" fill="#fff" opacity=".4"/>

  <g fill="#dff7ff" opacity=".8">
    <path d="M232,205 l8,-10 2,12z"/>
    <path d="M238,250 l10,-4 -3,9z"/>
    <path d="M222,180 l6,-12 4,9z"/>
  </g>
</svg>
```

Dibujé un meteorito de vidrio transparente con un mar, una luna y un faro adentro, que deja una cola de escarcha en vez de fuego; no existe porque los meteoritos son roca o metal opacos, no cápsulas de cristal con océanos habitados, y al cruzar la atmósfera arden, no se congelan.

### n2 (no_exista_es; agente a678b7d85467b2584)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#050812"/>
<stop offset="1" stop-color="#141033"/>
</linearGradient>
<radialGradient id="body" cx="0.4" cy="0.35" r="0.75">
<stop offset="0" stop-color="#9ff3ff" stop-opacity="0.55"/>
<stop offset="0.55" stop-color="#3b6ea8" stop-opacity="0.6"/>
<stop offset="1" stop-color="#1a2552" stop-opacity="0.95"/>
</radialGradient>
<linearGradient id="tail" x1="0" y1="1" x2="1" y2="0">
<stop offset="0" stop-color="#8ff0ff" stop-opacity="0.75"/>
<stop offset="0.5" stop-color="#b48cff" stop-opacity="0.3"/>
<stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
</linearGradient>
<radialGradient id="aura">
<stop offset="0.45" stop-color="#7fd8ff" stop-opacity="0.3"/>
<stop offset="1" stop-color="#7fd8ff" stop-opacity="0"/>
</radialGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
<path id="rock" d="M92 236C94 198 128 178 168 188 196 194 222 222 218 256 216 272 226 284 212 298 196 320 160 328 130 316 100 304 82 272 92 236Z"/>
<path id="hex" d="M0-7 6-3.5 6 3.5 0 7-6 3.5-6-3.5Z"/>
<clipPath id="cut"><use href="#rock"/></clipPath>
</defs>

<rect width="400" height="400" fill="url(#sky)"/>

<g fill="#fff" opacity="0.85">
<circle cx="40" cy="60" r="1.2"/><circle cx="90" cy="30" r="0.8"/><circle cx="330" cy="300" r="1.4"/><circle cx="360" cy="210" r="0.9"/><circle cx="60" cy="350" r="1"/><circle cx="250" cy="340" r="0.8"/><circle cx="300" cy="40" r="1"/><circle cx="20" cy="180" r="0.7"/><circle cx="380" cy="360" r="1.1"/><circle cx="200" cy="80" r="0.9"/><circle cx="140" cy="120" r="0.6"/><circle cx="300" cy="250" r="0.7"/><circle cx="110" cy="370" r="0.6"/><circle cx="240" cy="20" r="0.7"/>
</g>

<path d="M190 200C245 150 318 92 394 30 332 118 272 182 226 244Z" fill="url(#tail)"/>
<path d="M205 212C260 158 320 100 390 36" stroke="#dffbff" stroke-width="1.5" fill="none" opacity="0.6"/>

<g fill="#cfefff" fill-opacity="0.35" stroke="#e8fbff" stroke-width="1">
<use href="#hex" transform="translate(252 168) rotate(18) scale(1.1)"/>
<use href="#hex" transform="translate(286 138) rotate(40) scale(0.9)"/>
<use href="#hex" transform="translate(322 104) rotate(5) scale(0.75)"/>
<use href="#hex" transform="translate(354 72) rotate(28) scale(0.55)"/>
<use href="#hex" transform="translate(272 192) rotate(52) scale(0.5)"/>
<use href="#hex" transform="translate(305 148) rotate(70) scale(0.4)"/>
<use href="#hex" transform="translate(338 120) rotate(12) scale(0.35)"/>
</g>

<circle cx="155" cy="254" r="120" fill="url(#aura)"/>

<path d="M92 236C82 272 100 304 130 316" stroke="#ff9a4a" stroke-width="7" fill="none" filter="url(#soft)" opacity="0.65"/>
<g fill="#ffb060" opacity="0.8">
<circle cx="78" cy="300" r="1.6"/><circle cx="96" cy="326" r="1.2"/><circle cx="70" cy="268" r="1"/><circle cx="118" cy="336" r="1.4"/>
</g>

<use href="#rock" fill="url(#body)" stroke="#bfefff" stroke-width="2"/>

<g clip-path="url(#cut)">
<ellipse cx="150" cy="255" rx="70" ry="60" fill="#0b1030" opacity="0.5"/>
<ellipse cx="135" cy="232" rx="34" ry="14" fill="#6a5a9a" opacity="0.55"/>
<ellipse cx="170" cy="246" rx="30" ry="12" fill="#5a4e8c" opacity="0.5"/>
<ellipse cx="120" cy="268" rx="26" ry="10" fill="#4a4280" opacity="0.5"/>
<ellipse cx="185" cy="280" rx="22" ry="9" fill="#5a4e8c" opacity="0.45"/>
<g stroke="#9fd8ff" stroke-width="1" opacity="0.5">
<line x1="120" y1="282" x2="116" y2="300"/><line x1="134" y1="286" x2="130" y2="306"/><line x1="176" y1="292" x2="172" y2="312"/><line x1="192" y1="290" x2="188" y2="308"/><line x1="104" y1="278" x2="100" y2="294"/>
</g>
<polyline points="158,196 146,236 164,242 148,282 168,288 152,322" fill="none" stroke="#fff6a8" stroke-width="5" filter="url(#glow)" opacity="0.8"/>
<polyline points="158,196 146,236 164,242 148,282 168,288 152,322" fill="none" stroke="#ffffff" stroke-width="1.6" stroke-linejoin="round"/>
<polyline points="164,242 180,256 176,266" fill="none" stroke="#fff" stroke-width="1"/>
<polyline points="148,282 132,292 136,300" fill="none" stroke="#fff" stroke-width="0.8"/>
</g>

<g stroke="#e6fbff" stroke-opacity="0.35" stroke-width="1" fill="none">
<path d="M110 206L146 224 182 204"/>
<path d="M146 224L140 268 104 262"/>
<path d="M140 268L188 276 216 256"/>
<path d="M188 276L172 316"/>
<path d="M104 262L128 312"/>
</g>

<path d="M112 212C122 196 142 190 160 194" stroke="#fff" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.7"/>

<g fill="none" stroke="#dff6ff" stroke-opacity="0.5">
<circle cx="196" cy="236" r="4"/><circle cx="204" cy="282" r="2.5"/><circle cx="108" cy="290" r="3"/><circle cx="178" cy="310" r="1.8"/>
</g>
</svg>
```

Dibujé un meteorito de vidrio hueco y translúcido con una tormenta eléctrica atrapada adentro (nubes, lluvia y un rayo) y una cola de cristales hexagonales que se desprenden; no existe porque ningún meteorito es de vidrio transparente y hueco (se haría pedazos en la entrada a la atmósfera), y una tormenta necesita aire, presión y nubes, cosas que no pueden vivir dentro de una roca que cae por el espacio.

## Los recuerdos

### e1 (ensisheim; agente a38b075bed6f029a4)

**Consigna:** ¿Qué sabés del meteorito de Ensisheim? Contá lo que recuerdes: cuándo y dónde cayó, cuánto pesaba, quién lo vio, qué se hizo con la piedra, quiénes escribieron o dibujaron sobre él, y qué pasó con ella después. Al final ponele a cada dato una confianza de 0 a 100. No uses ninguna herramienta ni busques nada: contestá de memoria, directamente con el texto.

**Respuesta:**

Respuesta de memoria, sin consultar nada (el único "uso de herramienta" es este mismo canal de entrega, que es obligatorio para que el texto llegue).

## El meteorito de Ensisheim

**Cuándo y dónde.** Cayó el miércoles 7 de noviembre de 1492 (calendario juliano), cerca del mediodía, alrededor de las 11:30, en un campo de trigo fuera de las murallas de Ensisheim, en Alsacia. En ese momento el pueblo pertenecía a los Habsburgo (Austria Anterior, dentro del Sacro Imperio); hoy está en el departamento de Haut-Rhin, Francia. Dato curioso: hoy, 7 de noviembre de 2026, se cumplen exactamente 534 años. Es la caída de meteorito más antigua de Occidente con fecha precisa documentada y material conservado (la de Nogata, Japón, del año 861, es más antigua).

**Qué cayó y cuánto pesaba.** Una piedra, no un hierro: una condrita ordinaria clasificada como LL6. Las crónicas hablan de unas 260 libras, lo que da unos 127 kg. Se enterró en el campo a cosa de un metro de profundidad (algunas versiones dicen "la altura de un hombre"). El estruendo, un "trueno" (por eso la llamaban Donnerstein, piedra del trueno), se habría oído a unos 150 km, en Basilea, Lucerna y Villingen.

**Quién lo vio.** Según las fuentes, el único testigo directo del impacto fue un chico (un niño); mucha gente oyó la explosión y vio el cuerpo luminoso. Los vecinos corrieron al lugar y empezaron a arrancar pedazos como reliquias o amuletos. El magistrado local (el representante de la autoridad habsburga) lo prohibió y mandó llevar la piedra a la iglesia parroquial, donde la encadenaron a la pared / la colgaron en el coro, por un lado como señal divina y por otro para que "no volviera a volar".

**Maximiliano.** Maximiliano I, entonces rey de romanos (todavía no emperador), pasó por Ensisheim el 26 de noviembre de 1492, camino a su campaña contra Carlos VIII de Francia. Vio la piedra, consultó con sus consejeros, la tomó como augurio favorable, hizo sacar dos pedazos (uno para él y uno para el archiduque Segismundo de Tirol) y ordenó que la piedra se conservara en la iglesia. A los pocos meses vinieron la victoria sobre los franceses y la Paz de Senlis (1493), lo que reforzó la lectura de "presagio".

**Quiénes escribieron o dibujaron sobre él.**
- Sebastian Brant (el autor de Das Narrenschiff / La nave de los locos), que estaba en Basilea, publicó en 1492 hojas volantes (Flugblätter) en latín y en alemán sobre el "Donnerstein", impresas por Johann Bergmann von Olpe, con un grabado en madera de la piedra cayendo del cielo sobre los campos con el pueblo amurallado al fondo. Interpretó la caída como un signo de Dios en favor de Maximiliano contra los franceses (y los turcos) y lo exhortó a actuar. Volvió a incluir los poemas en sus Varia carmina (1498).
- La Crónica de Núremberg de Hartmann Schedel (Liber chronicarum, 1493) incluyó la noticia con un grabado muy conocido, del taller de Michael Wolgemut y Wilhelm Pleydenwurff.
- Alberto Durero estaba en Basilea en 1492 como joven grabador. Al dorso de su tabla "San Jerónimo en el desierto" (c. 1496, National Gallery, Londres) pintó un cuerpo celeste ígneo que muchos historiadores del arte asocian con el meteorito de Ensisheim. A veces se le atribuye también el grabado de la hoja de Brant, pero eso es dudoso.
- Junto a la piedra, en la iglesia, se colocó (más tarde) una placa con la inscripción latina "De hoc lapide multi multa, omnes aliquid, nemo satis" ("De esta piedra muchos saben mucho, todos algo, nadie lo suficiente").
- Ernst Chladni la citó en 1794 en su libro sobre el origen de las masas de hierro halladas por Pallas, el texto fundacional de la idea de que los meteoritos vienen del espacio.

**Qué pasó después con la piedra.** Estuvo unos tres siglos en la iglesia, perdiendo trozos que se regalaban a notables de paso. En la Revolución Francesa (1793) fue confiscada y llevada a Colmar (a la biblioteca / escuela central del departamento), donde le cortaron fragmentos que fueron a parar a museos y gabinetes de toda Europa (París, Viena, Londres, Berlín, etc.); por eso hoy hay piezas de Ensisheim en muchas colecciones. En 1803 volvió a Ensisheim, primero al Hôtel de Ville y luego al Musée de la Régence (en el Palais de la Régence, edificio del siglo XVI que fue sede de la Regencia habsburga de Austria Anterior), donde está hoy en una vitrina. La masa principal que queda ronda los 54 kg (se cita 53,8 kg). Desde alrededor del año 2000 existe una cofradía, la Confrérie Saint-Georges des Gardiens de la Météorite d'Ensisheim, que "custodia" la piedra, y el pueblo organiza cada junio una feria de minerales y meteoritos.

## Confianza por dato (0-100)

- Fecha: 7 de noviembre de 1492 — 97
- Era miércoles — 70
- Hora: cerca del mediodía, ~11:30 — 75
- Lugar: campo de trigo fuera de las murallas de Ensisheim, Alsacia (hoy Haut-Rhin, Francia) — 95
- Ensisheim era habsburgo (Austria Anterior) en 1492 — 90
- Caída más antigua de Occidente con fecha y material conservado; Nogata (861) más antigua — 85
- Tipo: condrita ordinaria LL6 — 85
- Masa original ~127 kg (260 libras) — 85
- Se enterró ~1 metro — 60
- Estruendo oído a ~150 km (Basilea, Lucerna, Villingen) — 65
- Nombre popular Donnerstein — 90
- Un niño como único testigo directo del impacto — 75
- Vecinos arrancaron pedazos; el magistrado lo prohibió — 70
- Piedra llevada a la iglesia parroquial y encadenada/colgada — 90
- Maximiliano I la vio en Ensisheim el 26 de noviembre de 1492 — 75 (la visita 85, la fecha exacta 65)
- Tomó dos pedazos: uno para él, otro para Segismundo de Tirol — 70
- Ordenó conservarla en la iglesia como señal divina — 85
- Vínculo con la campaña contra Francia y la Paz de Senlis de 1493 — 75
- Sebastian Brant escribió hojas volantes en latín y alemán, impresas en Basilea por Bergmann von Olpe, con grabado — 90
- Brant la leyó como presagio favorable a Maximiliano — 90
- Poemas reeditados en Varia carmina (1498) — 65
- Grabado en la Crónica de Núremberg de Schedel (1493) — 85
- Grabado del taller de Wolgemut/Pleydenwurff — 70
- Dürer en Basilea en 1492 — 80
- Dorso del "San Jerónimo" de Dürer (c. 1496, National Gallery) vinculado al meteorito — 65
- Atribución a Dürer del grabado de Brant: dudosa — 60
- Inscripción "De hoc lapide multi multa, omnes aliquid, nemo satis" — 85
- Que la placa se puso tiempo después, no en 1492 — 55
- Chladni la citó en 1794 — 75
- Confiscada en la Revolución (1793) y llevada a Colmar — 80
- Fragmentos repartidos a museos europeos en esa época — 75
- Devuelta a Ensisheim en 1803 — 70
- Primero en el Hôtel de Ville, luego en el Musée de la Régence (Palais de la Régence, s. XVI) — 80
- Masa actual ~54 kg (53,8) — 80
- Confrérie Saint-Georges des Gardiens de la Météorite, fundada ca. 2000 — 60
- Feria anual de minerales y meteoritos en junio — 70

Nada de esto viene de la memoria del usuario ni de archivos; es todo recuerdo del modelo, sin verificación.

### e2 (ensisheim; agente aa27fcaf3cf444621)

**Consigna:** la misma que e1.

**Respuesta:**

Respondo de memoria, sin herramientas, como pediste. (Dato curioso: hoy, 7 de noviembre de 2026, se cumplen exactamente 534 años de la caída.)

**El meteorito de Ensisheim — lo que recuerdo**

**Cuándo y dónde cayó**
Cayó el 7 de noviembre de 1492, cerca del mediodía (entre las 11 y las 12), en un campo de trigo en las afueras de la pequeña ciudad amurallada de Ensisheim, en Alsacia. Hoy es Francia (departamento del Alto Rin, Haut-Rhin), pero en ese momento era territorio de los Habsburgo dentro del Sacro Imperio, parte de la llamada Austria Anterior (Vorderösterreich), de la que Ensisheim era la capital administrativa. El estruendo (descripto como un trueno enorme) se escuchó a mucha distancia, del orden de 100 a 150 km; las crónicas mencionan que se oyó en Lucerna y en lugares del otro lado del Rin y hacia Borgoña. Es por esto que en los textos de la época se lo llama "Donnerstein" (piedra de trueno).

**Cuánto pesaba**
La masa original se estima en unos 127 kg (alrededor de 260–280 libras). Al caer habría abierto un hoyo de aproximadamente un metro de profundidad en el campo. Se la describe como una piedra de forma más o menos triangular. Clasificación moderna: condrita ordinaria, grupo LL6.

**Quién lo vio**
El único testigo directo del impacto habría sido un niño que estaba en el campo. Después del estruendo acudieron los vecinos, encontraron la piedra en el hoyo y empezaron a romperla para llevarse trozos como amuletos. Intervino la autoridad local (el magistrado o Landvogt) para frenar el saqueo, y la piedra fue llevada a la iglesia parroquial de Ensisheim.

**Qué se hizo con la piedra**
Maximiliano I, por entonces rey de romanos (todavía no emperador coronado), pasaba por la región camino a su campaña contra Francia (la guerra en torno a Bretaña, que terminó con el Tratado de Senlis en 1493). Llegó a Ensisheim unas semanas después, el 26 de noviembre de 1492, hizo que le trajeran la piedra, la examinó con su consejo y la interpretó como una señal divina a su favor, un presagio contra los franceses (y, en la retórica de la época, también contra los turcos). Ordenó que se conservara en la iglesia como objeto de veneración/memoria y se quedó con dos fragmentos: uno para él y otro que mandó a su primo, el archiduque Segismundo de Tirol (que poco antes le había cedido el Tirol y la Austria Anterior). Según la tradición, la piedra se colgó o encadenó en el coro de la iglesia, con la leyenda popular de que era para que no "volviera a volarse" de noche. Allí estuvo unos 300 años. En la iglesia se colocó además una inscripción latina que suele citarse: "De hoc lapide multi multa, omnes aliquid, nemo satis" ("De esta piedra, muchos dicen mucho, todos algo, nadie lo suficiente").

**Quiénes escribieron o dibujaron sobre él**
- Sebastian Brant (el autor de "La nave de los necios", 1494) publicó casi de inmediato un pliego suelto (Flugblatt) con un poema en latín y alemán sobre el "Donnerstein" caído ante Ensisheim en el año 92, impreso en Basilea por Johann Bergmann von Olpe, con un grabado en madera que muestra la piedra cayendo sobre la ciudad. Tuvo varias ediciones y está dirigido a Maximiliano, con la misma lectura política: señal favorable al rey contra Francia. Es la pieza clave por la cual el meteorito quedó tan bien documentado.
- La Crónica de Núremberg de Hartmann Schedel (1493) incluye una xilografía de la caída.
- Alberto Durero: el reverso de su tabla "San Jerónimo en el desierto" (c. 1494–96, National Gallery de Londres) muestra una explosión luminosa en el cielo que varios autores han vinculado con el meteorito de Ensisheim, porque Durero estaba en Basilea trabajando para impresores en 1492 y pudo haber oído o visto el fenómeno. La atribución es discutida, no es segura.
- Diebold Schilling, en la Crónica de Lucerna (1513), tiene una ilustración de la caída.
- Aparece también en compilaciones de prodigios del siglo XVI, como el "Libro de los milagros" de Augsburgo (c. 1550) y el "Prodigiorum ac ostentorum chronicon" de Lycosthenes (1557).
- Mucho después, Ernst Chladni (1794), en el libro fundacional de la meteorítica, lo usó como uno de los casos históricos documentados de piedras caídas del cielo.

**Qué pasó con ella después**
Durante la Revolución Francesa (hacia 1793) la piedra fue sacada de la iglesia y llevada a Colmar (a la biblioteca pública/nacional de la ciudad), donde volvieron a sacarle trozos. Fue devuelta a Ensisheim en 1803. A lo largo de los siglos perdió más de la mitad de su masa por los fragmentos extraídos: la masa principal que se conserva hoy ronda los 54 kg (suele citarse 53,8 kg). Está expuesta en el Musée de la Régence, en el Palais de la Régence de Ensisheim (el edificio renacentista del siglo XVI que fue sede del gobierno habsburgués de la Austria Anterior y hoy es también ayuntamiento). Hay fragmentos en grandes colecciones: Museo de Historia Natural de París, Museo de Historia Natural de Viena, Londres, Berlín y otros.

Es considerada la caída de meteorito más antigua del mundo occidental de la que se conserva material y documentación contemporánea (la más antigua del mundo con material conservado es Nogata, Japón, año 861). En 1992, para el 500 aniversario, se fundó en Ensisheim la Confrérie Saint-Georges des Gardiens de la Météorite, y desde fines de los 90/2000 la ciudad organiza cada junio una feria internacional de meteoritos.

**Confianza por dato (0–100)**
- Fecha: 7 de noviembre de 1492 — 95
- Hora: cerca del mediodía (11–12) — 80
- Lugar: campo de trigo en las afueras de Ensisheim, Alsacia (hoy Haut-Rhin, Francia) — 95
- Entonces territorio habsburgués de la Austria Anterior, dentro del Sacro Imperio — 85
- Estruendo oído a ~100–150 km, incluida Lucerna — 70
- Masa original ~127 kg — 85
- Hoyo de ~1 m de profundidad — 65
- Forma triangular — 50
- Clasificación LL6 (condrita ordinaria) — 85
- Un niño como único testigo del impacto — 75
- Vecinos que rompían trozos, frenados por el magistrado local — 75
- Piedra llevada a la iglesia parroquial — 90
- Visita de Maximiliano I a Ensisheim para ver la piedra — 90
- Fecha de la visita: 26 de noviembre de 1492 — 70
- Maximiliano como rey de romanos, en campaña contra Francia — 80
- Interpretación como presagio favorable contra franceses (y turcos) — 80
- Se quedó dos trozos, uno para el archiduque Segismundo de Tirol — 70
- Ordenó conservarla en la iglesia — 90
- Colgada/encadenada en el coro "para que no volviera a volar" — 70
- Inscripción "De hoc lapide multi multa, omnes aliquid, nemo satis" — 65
- Pliego suelto de Sebastian Brant con poema latín/alemán y xilografía — 90
- Impreso en Basilea — 85
- Impresor Johann Bergmann von Olpe — 75
- Dirigido a Maximiliano, lectura política antifrancesa — 80
- Xilografía en la Crónica de Núremberg de Schedel (1493) — 80
- Hipótesis de que el reverso del San Jerónimo de Durero representa el meteorito — 70 (que la hipótesis existe y se discute); 40 (que efectivamente lo represente)
- Durero en Basilea en 1492 — 80
- Ilustración en la Crónica de Lucerna de Diebold Schilling (1513) — 65
- Aparición en el Libro de los milagros de Augsburgo (c. 1550) — 60
- Aparición en Lycosthenes (1557) — 55
- Chladni (1794) lo citó como caso histórico — 65
- Trasladada a Colmar durante la Revolución (c. 1793) — 70
- Devuelta a Ensisheim en 1803 — 60
- Masa actual ~54 kg (53,8 kg) — 75
- Expuesta en el Musée de la Régence, Palais de la Régence, Ensisheim — 85
- Palais de la Régence como antigua sede del gobierno de la Austria Anterior (s. XVI) — 80
- Fragmentos en París, Viena, Londres, Berlín — 75
- Caída más antigua de Occidente con material conservado — 85
- Nogata (Japón, 861) como la más antigua del mundo con material conservado — 85
- Cofradía de guardianes del meteorito fundada en 1992 — 75
- Feria anual de meteoritos en Ensisheim en junio — 65

Todo lo anterior es de memoria, sin verificar con ninguna fuente; los datos con confianza menor a 70 convendría chequearlos antes de citarlos.

### p1 (piedras del cielo; agente a65502a6fb972d9e0)

**Consigna:** ¿Cuándo y cómo aceptó la ciencia europea que las piedras pueden caer del cielo? Contá la historia como la recuerdes, con nombres, lugares y fechas, incluidos los episodios en que se negó. Si hay frases famosas atribuidas a alguien en esa historia, decilas y decí si creés que son auténticas. Al final ponele a cada dato una confianza de 0 a 100. No uses ninguna herramienta ni busques nada: contestá de memoria, directamente con el texto.

**Respuesta:**

Respondo de memoria, sin consultar nada. Al final va la lista de confianzas (0–100) dato por dato.

## Respuesta corta

La ciencia europea aceptó que caen piedras del cielo en una ventana de unos diez años, entre 1794 y 1803: en 1794 Ernst Chladni publicó la teoría; en 1802 Edward Howard y el conde de Bournon aportaron la química (el níquel); y en abril de 1803 la lluvia de piedras de L'Aigle, en Normandía, investigada por el joven Jean-Baptiste Biot, convenció a la Académie des Sciences, que era el bastión del rechazo. Antes de eso, durante casi todo el siglo XVIII, la opinión ilustrada consideraba la idea una superstición campesina.

## La historia larga

**Antigüedad y Edad Media.** Los griegos y romanos registraron caídas. La más famosa es la piedra de Egospótamos, en Tracia, hacia 467 a.C.; Plinio y otros la asocian a Anaxágoras, quien sostenía que los cuerpos celestes eran rocas incandescentes y, según la tradición, "predijo" o interpretó la caída como prueba. Aristóteles, en cambio, en los *Meteorológicos* ubicó los meteoros (estrellas fugaces, bólidos) como fenómenos atmosféricos, de la región sublunar, y esa autoridad pesó durante dos mil años: lo que brilla en el cielo es aire inflamado, no piedra.

El 7 de noviembre de 1492 (justamente, hoy se cumplen 534 años) cayó una piedra de unos 127 kg en un campo de trigo en Ensisheim, Alsacia, con estruendo oído a decenas de kilómetros. El rey Maximiliano (futuro emperador) pasó por allí semanas después, la tomó como presagio favorable en su guerra contra Francia y ordenó que se conservara en la iglesia parroquial, donde quedó (hoy está en el museo del pueblo, muy recortada por los que se llevaron trozos). Sebastian Brant, el autor de *La nave de los locos*, publicó hojas volantes con versos sobre el suceso. Es la caída observada más antigua de la que se conserva la piedra en Europa. Hay otro hierro muy viejo, el de Elbogen (Loket, Bohemia), guardado desde el siglo XV en el castillo con la leyenda del "burgrave maldito", pero sin observación de la caída.

**La Ilustración escéptica.** Paradójicamente, cuanto más racional se volvió la ciencia, menos creyó en las piedras del cielo. Eran relatos de aldeanos y curas, mezclados con milagros y presagios; un naturalista moderno no podía tomarlos en serio.

- 26 de mayo de 1751, Hraschina, cerca de Zagreb (Agram): cayeron dos masas de hierro (unos 39 y 9 kg) a plena luz, con muchos testigos. El obispo hizo levantar actas juradas y envió los hierros y el expediente a Viena, al gabinete imperial. Están hoy en el Museo de Historia Natural de Viena, origen de la colección de meteoritos más antigua del mundo. Los sabios vieneses archivaron el asunto como curiosidad.
- 3 de julio de 1753, Tábor (Strkov), Bohemia: lluvia de piedras, también documentada.
- Julio de 1766, Albareto, cerca de Módena: el jesuita Domenico Troili describió la caída en *Della caduta di un sasso dall'aria* y la atribuyó a una explosión subterránea; pese a eso, es la primera descripción mineralógica seria de un meteorito y el sulfuro de hierro de los meteoritos (troilita) lleva su nombre.
- 13 de septiembre de 1768, Lucé, cerca de Le Mans: cayó una piedra de unos 3,5 kg ante testigos. La Académie des Sciences encargó un informe a Fougeroux de Bondaroy, Cadet de Gassicourt y un joven Antoine-Laurent Lavoisier. Analizaron la piedra (pirita, hierro, sílice) y concluyeron en 1772 que era una roca terrestre, una arenisca piritosa que había sido alcanzada por un rayo: "la piedra del trueno" de los campesinos no venía del cielo sino que el rayo la había encontrado en el suelo. Ese informe fijó la posición oficial francesa por treinta años. El dato irónico: Lavoisier, que fundó la química moderna, firmó el documento más citado de la negación.
- En Siberia, en 1749 el herrero Yákov Medvédev halló cerca de Krasnoyarsk una masa de hierro de unos 700 kg, que el naturalista Peter Simon Pallas vio en 1772 y hizo llevar a San Petersburgo. El "hierro de Pallas" era un enigma: hierro metálico nativo con cristales de olivino, en una loma sin rastro de mina ni volcán. (Hoy a esa clase de meteoritos se los llama palasitas.)
- Y la pieza rioplatense: en el Chaco, el Campo del Cielo. Los españoles supieron de los hierros desde 1576 (expedición de Hernán Mexía de Miraval); en 1774 y 1779 hubo nuevas expediciones, y en 1783 Miguel Rubín de Celis llegó al Mesón de Fierro, lo midió (unas 15 toneladas), lo hizo volar parcialmente con pólvora para ver si continuaba bajo tierra, comprobó que estaba aislado y concluyó que no era una veta; su informe se publicó en las *Philosophical Transactions* de Londres en 1788. Rubín de Celis no lo consideró caído del cielo. Chladni, en cambio, lo citaría poco después como ejemplo de hierro caído.
- 24 de julio de 1790, Barbotan, Gascuña: lluvia de piedras vista por cientos de personas; el alcalde y el consejo municipal levantaron un acta formal con unos 300 testigos. El físico Pierre Bertholon se burló del documento en el *Journal des Sciences Utiles* (1791) con una frase que se volvió el emblema del escepticismo (la cito más abajo).
- En esas décadas, según cuentan las historias de la disciplina, varios gabinetes y museos europeos (se mencionan Dresde, Berna, Verona, Copenhague) tiraron o relegaron sus piedras "caídas del cielo" por vergüenza, como restos de superstición. Es una anécdota repetida que creo cierta en lo esencial pero difícil de verificar caso por caso.

**El giro: 1794.** Ernst Florens Friedrich Chladni (1756–1827), sajón, jurista de formación, físico de la acústica (las "figuras de Chladni" de arena sobre placas vibrantes), conversó en Gotinga en 1792 con Georg Christoph Lichtenberg, quien había visto un bólido y le mencionó el problema. Chladni reunió los relatos de caídas de dos milenios, los comparó con el hierro de Pallas, el de Hraschina y los del Chaco, y en abril de 1794 publicó en Riga (editor Hartknoch) un librito de unas 60 páginas: *Über den Ursprung der von Pallas gefundenen und anderer ihr ähnlicher Eisenmassen und über einige damit in Verbindung stehende Naturerscheinungen*. Sus tesis: (1) las masas de hierro y las piedras de los relatos cayeron realmente del cielo; (2) los bólidos (bolas de fuego) son esos cuerpos atravesando la atmósfera a gran velocidad, y la luz y el estruendo vienen del rozamiento; (3) el origen es cósmico: fragmentos de materia del espacio, quizá restos de un planeta o materia que nunca llegó a formar uno. Era, en esencia, la idea moderna. Chladni escribió que preveía que lo tomarían por loco, y en buena medida así fue: la recepción en Alemania fue entre fría y burlona. Lichtenberg lo apoyó, aunque se cuenta que al leer el libro sintió "como si le hubieran pegado en la cabeza con una de esas piedras". Ayudó que Lichtenberg y luego Olbers tomaran a Chladni en serio.

**La naturaleza colabora: 1794–1798.** Dos meses después del libro, el 16 de junio de 1794 hacia el atardecer, cayeron piedras cerca de Siena, Toscana, delante de mucha gente, incluidos viajeros ingleses (entre ellos, el excéntrico Frederick Hervey, conde de Bristol y obispo de Derry, que escribió cartas sobre el episodio). El Vesubio había entrado en erupción el día anterior, así que muchos pensaron que las piedras eran cenizas o proyectiles del volcán a 300 km, idea que otros encontraron igual de absurda. El abate Ambrogio Soldani publicó *Sopra una pioggetta di sassi* (1794) proponiendo que las piedras se condensaban en la atmósfera, y el químico inglés William (Guglielmo) Thomson, residente en Nápoles, las analizó y describió la corteza negra. Lo importante es que trozos de Siena llegaron a Inglaterra, donde Joseph Banks, presidente de la Royal Society, y un ambiente menos dogmático que el francés, empezaron a interesarse.

El 13 de diciembre de 1795, a las tres de la tarde, cayó una piedra de 56 libras (unos 25 kg) a pocos metros de un labrador en Wold Cottage, Yorkshire, en tierras del mayor Edward Topham, dramaturgo y periodista, quien juntó declaraciones juradas, exhibió la piedra en Piccadilly cobrando entrada y en 1799 levantó un obelisco en el lugar con una inscripción que aún se lee. En 1796 Edward King publicó en Londres *Remarks concerning stones said to have fallen from the clouds*, que discutía Siena y Wold Cottage y daba a conocer a Chladni en inglés. El 19 de diciembre de 1798 cayeron piedras en Krakhut, cerca de Benarés, India, con testigos británicos; John Lloyd Williams informó a la Royal Society.

**La química: 1802.** Edward Charles Howard, químico inglés, con el mineralogista francés emigrado Jacques-Louis de Bournon, analizó las piedras de Siena, Wold Cottage, Benarés y Tábor, y hierros como el de Pallas y el del Chaco. Resultado, publicado en las *Philosophical Transactions* de 1802: todas las piedras tenían la misma estructura (granos metálicos, glóbulos, corteza fundida) y tanto los granos como los hierros contenían níquel aleado, cosa que no aparecía en las rocas terrestres conocidas. Cuatro piedras caídas en lugares tan distintos como Toscana, Yorkshire, Bohemia y la India eran la misma cosa, y esa cosa no era de este mundo. Ese trabajo convenció a buena parte de la comunidad británica y alemana, y hasta a franceses como Vauquelin y Fourcroy, que lo reprodujeron.

Al mismo tiempo cambió el cielo: Piazzi descubrió Ceres el 1 de enero de 1801 y Olbers descubrió Palas el 28 de marzo de 1802. De pronto había "pequeños planetas" entre Marte y Júpiter y la idea de que el espacio contuviera trozos de roca dejó de ser disparatada. Laplace, en 1802, propuso que las piedras eran lanzadas por volcanes lunares (idea que Olbers había esbozado hacia 1795); Biot y Poisson calcularon que una eyección lunar a unos 2.400 m/s bastaba. Esa hipótesis lunar, no la cósmica de Chladni, fue la que dominó por unas décadas.

**La prueba de campo: L'Aigle, 1803.** El 26 de abril de 1803 (6 de floreal del año XI), alrededor de la una de la tarde, un bólido estalló sobre L'Aigle, en el departamento del Orne, Normandía, y cayeron entre 2.000 y 3.000 piedras (unos 37 kg en total) sobre una elipse de unos 10 por 4 km. El ministro del Interior, el químico Jean-Antoine Chaptal, envió al físico Jean-Baptiste Biot, de 29 años, a investigar en nombre del Institut. Biot pasó junio en la zona, entrevistó testigos de distintos pueblos y oficios que no se conocían entre sí, comprobó que ningún campesino tenía piedras así antes, que no había fundiciones ni minas que las explicaran, y dibujó el mapa de la elipse de dispersión. Su *Relation d'un voyage fait dans le département de l'Orne...*, leída en el Institut en julio de 1803, es considerada el acta de nacimiento de la meteorítica como ciencia: por su rigor en separar el hecho (caen piedras) de la hipótesis (de dónde vienen). Tras L'Aigle, la Académie dio vuelta su posición y la resistencia quedó reducida a algunos individuos (Jean-André Deluc, Eugène Patrin y otros insistieron un tiempo con la condensación atmosférica).

**Epílogo.** El 14 de diciembre de 1807 cayeron piedras en Weston, Connecticut; los profesores de Yale Benjamin Silliman y James Kingsley hicieron la primera investigación de un meteorito en Estados Unidos. A ese episodio se asocia la frase famosa atribuida a Jefferson que comento abajo. En cuanto al origen, la hipótesis lunar perdió terreno hacia mediados del siglo XIX, y la asociación de las lluvias de estrellas con cometas (Leónidas de 1833; Schiaparelli en 1866) y la multiplicación de asteroides terminaron dando la razón a Chladni, que vivió para ver aceptada su primera tesis y publicó en 1819 un gran catálogo, *Über Feuer-Meteore*. Su colección fue a Berlín.

## Frases famosas y si creo que son auténticas

1. **Bertholon sobre Barbotan (1791):** "Qué triste es ver a una municipalidad entera consignar en un acta en debida forma tradiciones populares que solo pueden excitar la piedad, no solo de los físicos, sino de toda la gente razonable." La creo auténtica: aparece citada con referencia al *Journal des Sciences Utiles* en las historias serias de la disciplina (Burke, Marvin). Puede variar la traducción, no el sentido.

2. **"No hay piedras en el cielo, por lo tanto no pueden caer piedras del cielo"**, atribuida a Lavoisier o a la Académie en bloque. La considero apócrifa como cita literal: es una caricatura posterior de la postura del informe de 1772, que fue más técnica (piedra terrestre alcanzada por un rayo). Resume bien la actitud, pero nadie la escribió así.

3. **Jefferson (1807–1808):** "Me resulta más fácil creer que dos profesores yanquis mientan que creer que caigan piedras del cielo." Casi seguramente apócrifa. No hay fuente contemporánea; aparece mucho después, y la carta real que Jefferson escribió sobre Weston (a Daniel Salmon, febrero de 1808) es escéptica pero prudente, del tipo: la caída desde la atmósfera presenta tantas dificultades que requiere examen cuidadoso, pero "no debemos negar lo que no podemos explicar". Como republicano enfrentado a los federalistas de Connecticut, la frase le quedaba demasiado bien, y por eso prendió.

4. **Lichtenberg** al leer a Chladni: que se sintió "como golpeado en la cabeza por una de esas piedras". Plausible, la he visto en la literatura histórica sobre Chladni, pero no sé si proviene de una carta de Lichtenberg o de un recuerdo de Chladni; confianza media.

5. **Chladni** anticipando que lo tomarían por loco: creo que está en su propio prólogo o en escritos posteriores donde recuerda la recepción; moderadamente confiable.

6. **Inscripción del obelisco de Wold Cottage (1799):** "Here on this spot, Dec. 13th, 1795, fell from the atmosphere an extraordinary stone... whose weight was 56 pounds. This column in memory of it was erected by Edward Topham, 1799." Auténtica en lo sustancial; el monumento existe. La redacción exacta puede diferir.

## Confianza en cada dato (0–100)

- Egospótamos c. 467 a.C. y su asociación con Anaxágoras: 80
- Aristóteles ubicando meteoros como fenómeno atmosférico sublunar: 85
- Ensisheim, 7 de noviembre de 1492: 92; masa ~127 kg: 75; Maximiliano y conservación en la iglesia: 85; hojas volantes de Sebastian Brant: 80
- Hierro de Elbogen (Loket), siglo XV: 65
- Hraschina, 26 de mayo de 1751: 82; masas 39 y 9 kg: 60; actas del obispo y envío a Viena, hoy en el NHM de Viena: 80
- Tábor, 3 de julio de 1753: 65
- Albareto, julio de 1766, Troili y su libro; troilita en su honor: 75
- Lucé, 13 de septiembre de 1768: 80; informe de Fougeroux, Cadet y Lavoisier concluyendo piedra terrestre golpeada por rayo: 80; fecha del informe 1772: 65 (pudo ser leído antes y publicado después)
- Hierro de Pallas: hallado en 1749 por Medvédev: 70; visto por Pallas en 1772, ~700 kg, trasladado a San Petersburgo: 75
- Campo del Cielo: 1576 Mexía de Miraval: 70; Rubín de Celis 1783, voladura y conclusión de masa aislada: 70; publicación en Phil. Trans. 1788: 65; Rubín de Celis no lo creyó caído del cielo: 60; Chladni lo cita en 1794: 65
- Barbotan, 24 de julio de 1790: 85; acta municipal con ~300 testigos: 70; burla de Bertholon en el Journal des Sciences Utiles, 1791: 75
- Museos descartando meteoritos en el siglo XVIII: 55 (anécdota repetida, poco verificable)
- Chladni: fechas 1756–1827: 85; conversación con Lichtenberg en Gotinga 1792: 70; libro publicado en Riga en 1794, editor Hartknoch, ~60 páginas: 85; tesis (caída real, bólidos = entrada atmosférica, origen cósmico): 90; mala recepción inicial: 85
- Siena, 16 de junio de 1794, con erupción del Vesubio el día anterior: 85; Soldani y su opúsculo: 75; William Thomson analizando: 65; conde de Bristol / obispo de Derry como testigo o corresponsal: 55; muestras llegadas a Banks e Inglaterra: 70
- Wold Cottage, 13 de diciembre de 1795, 56 libras: 88; Topham, exhibición en Piccadilly, obelisco de 1799: 80
- Edward King, Remarks..., 1796: 65
- Benarés (Krakhut), 19 de diciembre de 1798; informe de J. L. Williams: 75
- Howard y Bournon, Phil. Trans. 1802; piedras de Siena, Wold Cottage, Benarés y Tábor; níquel común a piedras y hierros: 85
- Ceres 1 de enero de 1801 (Piazzi); Palas 28 de marzo de 1802 (Olbers): 92
- Laplace proponiendo origen lunar en 1802: 70; Olbers esbozándolo c. 1795: 50; cálculos de Biot/Poisson sobre velocidad de eyección: 60
- L'Aigle, 26 de abril de 1803 (6 floreal XI), ~1 de la tarde: 92; 2.000–3.000 piedras, ~37 kg, elipse ~10 x 4 km: 70; Chaptal envía a Biot: 85; Biot con 29 años: 80; informe leído en el Institut en julio de 1803: 70
- Resistencia posterior de Deluc, Patrin y otros: 55
- Weston, 14 de diciembre de 1807; Silliman y Kingsley: 85
- Chladni, Über Feuer-Meteore, 1819; colección a Berlín: 70
- Schiaparelli vinculando lluvias de meteoros con cometas en 1866: 80
- Autenticidad de las frases: Bertholon auténtica: 72; "no hay piedras en el cielo" apócrifa como cita literal: 78; Jefferson "profesores yanquis" apócrifa: 82; carta real de Jefferson a Daniel Salmon (feb. 1808) con tono prudente: 70; anécdota de Lichtenberg: 55; Chladni anticipando burla: 60; inscripción de Wold Cottage en lo sustancial: 80

Nota para quien relaye: todo lo anterior es de memoria, sin verificar; donde la confianza baja de 70 conviene chequear antes de citar. No usé memoria del usuario ni herramientas de búsqueda, por pedido explícito.

### p2 (piedras del cielo; agente aba397f064f7f7e97)

**Consigna:** la misma que p1.

**Respuesta:**

Respondo de memoria, sin usar herramientas ni buscar nada, como pediste. Donde no estoy seguro lo digo, y al final va la lista de confianzas.

# Cuándo y cómo la ciencia europea aceptó que caen piedras del cielo

Dato de color: hoy es 7 de noviembre, el aniversario exacto de la caída de Ensisheim (7 de noviembre de 1492), la caída observada más antigua de la que todavía se conserva la piedra en Europa.

## 1. Antes de la negación: antiguos y medievales lo daban por cierto

- **Egospótamos (Tracia), hacia 467/466 a.C.** Cayó una piedra grande que, según Plutarco (Vida de Lisandro) y Plinio, seguía exhibiéndose siglos después. Se la asoció a **Anaxágoras**, que enseñaba que el Sol y los astros eran piedras incandescentes; Diógenes de Apolonia hablaba de piedras oscuras invisibles que a veces caen. **Aristóteles**, en los *Meteorológicos*, explicó la piedra de Egospótamos como levantada por el viento: en su cosmos el cielo supralunar era perfecto e inmutable, nada podía caer de él, y los "meteoros" (incluidos cometas y bólidos) eran fenómenos atmosféricos. Esa idea pesó dos mil años.
- **Ensisheim (Alsacia), 7 de noviembre de 1492.** Una piedra de unos 127 kg cayó en un campo de trigo; un chico la vio caer. El rey Maximiliano (después emperador), que estaba en campaña contra Francia, la tomó como presagio favorable y mandó encadenarla en la iglesia parroquial. Sebastian Brant la cantó en pliegos impresos. Sigue en Ensisheim. La inscripción latina que se le puso dice algo así como *"De hoc lapide multi multa, omnes aliquid, nemo satis"* ("De esta piedra muchos dicen muchas cosas, todos algo, nadie lo suficiente").
- Hay muchas otras caídas en crónicas medievales (el hierro de Elbogen en Bohemia, hacia 1400, el "burgrave embrujado"), más las "piedras de trueno" del folklore.

## 2. La paradoja ilustrada: por qué los sabios pasaron a negarlo

Entre 1650 y 1790 pasó algo raro: cuanto más científica se volvía Europa, menos se creía en las piedras del cielo. Razones:
- El espacio newtoniano era vacío; más allá de la atmósfera no había "de dónde" caer. La Luna era un cuerpo, no una fuente de escombros.
- La crítica racionalista de los "prodigios": crónicas de lluvias de piedras venían empaquetadas con lluvias de sangre, de ranas, milagros. Se tiró todo junto.
- Los naturalistas demostraron que las "ceraunias" o "piedras de rayo" (hachas de piedra pulida) eran herramientas humanas, no caídas del cielo. Ese éxito alimentó un escepticismo generalizado.
- Sociología: los testigos eran campesinos y curas de provincia; los académicos estaban en París, Londres y Viena, y no vieron caer nada.
- La explicación "científica" de moda era que el rayo golpeaba una piedra del suelo (*pierre de foudre*), o que las masas se "condensaban" en la atmósfera.

## 3. Episodios de negación

- **Lucé (Maine, Francia), 13 de septiembre de 1768.** Cayó una piedra de unos 3,5 kg ante testigos. La Académie Royale des Sciences encargó el análisis a Fougeroux de Bondaroy, Cadet de Gassicourt y un **Lavoisier** de 25 años. El informe (leído hacia 1769, publicado hacia 1772) concluyó que era una piedra terrestre con pirita golpeada por el rayo, y que no había caído del cielo. Esta es la "negación de la Académie" que después se volvió leyenda. Irónicamente, Lucé es hoy una condrita perfectamente reconocida.
- **Hraschina (cerca de Zagreb), 26 de mayo de 1751.** Cayeron dos masas de hierro (~40 kg y ~9 kg) tras un bólido y detonaciones. El obispo de Zagreb tomó declaraciones juradas y mandó todo a Viena; el hierro fue a la colección imperial (la semilla del actual Museo de Historia Natural de Viena). En **1790 el abate Andreas Stütz**, curador en Viena, escribió sobre ese hierro algo así: "en 1751 hasta las cabezas más ilustradas de Alemania podían creer que el hierro cae del cielo, pero en nuestros tiempos sería imperdonable considerar probables semejantes cuentos". Años después Stütz cambió de idea y Viena se convirtió en la gran colección de meteoritos.
- **Barbotan (Gascuña), 24 de julio de 1790.** Lluvia de piedras ante unas 300 personas; el alcalde y la municipalidad de Juillac levantaron un acta formal. El abate **Pierre Bertholon**, en el *Journal des Sciences Utiles*, se lamentó de "qué triste es ver a una municipalidad entera certificar por acta cuentos populares que solo pueden dar lástima no solo a los físicos sino a toda la gente razonable" (paráfrasis). Lamétherie, en el *Journal de Physique*, fue menos hostil.
- **Museos que tiraron sus meteoritos.** Hacia 1790-1800 varios gabinetes de historia natural (recuerdo citados Dresde y Berna, entre otros) descartaron piezas de sus colecciones por considerarlas vergonzosas supersticiones. Viena, por suerte, conservó Hraschina.
- **El Chaco: Campo del Cielo.** Los españoles conocían el "Mesón de Fierro" desde la expedición de Hernán Mexía de Miraval (1576). En 1783 el marino **Miguel Rubín de Celis** llegó a la masa, la estimó en unas 15 toneladas, cavó debajo, comprobó que estaba aislada y concluyó que NO era de origen celeste (algo así como un producto terrestre, sin explicación convincente). Su informe salió en las *Philosophical Transactions* en 1788. El Mesón de Fierro se perdió después y nunca se volvió a encontrar. Detalle lindo: hacia 1799 **Proust**, en Madrid, analizó hierro de Campo del Cielo y encontró níquel, sin conectarlo con las caídas.

## 4. El giro: 1794-1803

**a) Chladni, 1794.** Ernst Florens Friedrich **Chladni** (1756-1827), abogado de formación, físico de la acústica (las "figuras de Chladni"), publicó en Riga en abril de 1794 *Über den Ursprung der von Pallas gefundenen und anderer ihr ähnlicher Eisenmassen...* ("Sobre el origen de la masa de hierro hallada por Pallas y otras semejantes, y sobre algunos fenómenos naturales relacionados"). El "hierro de Pallas" era una masa de ~700 kg con cristales de olivino (hoy el tipo "palasita") que **Peter Simon Pallas** había visto en 1772 cerca de Krasnoyarsk, hallada por el herrero Medvedev, y llevado a San Petersburgo en 1777. Chladni argumentó: (1) los bólidos van a velocidades imposibles para cualquier causa terrestre; (2) hay demasiados relatos independientes de piedras cayendo justo después de bólidos y detonaciones; (3) masas como la de Pallas, con corteza fundida, no se explican por procesos terrestres ni por "condensación atmosférica"; (4) por lo tanto, son materia cósmica: fragmentos de un planeta roto o materia primordial que nunca se aglomeró, que al entrar en la atmósfera se calienta y se ve como bólido. Lo ridiculizaron. Dicen que **Lichtenberg** (que lo había alentado en Gotinga) comentó que al leerlo se sintió "como si le hubieran pegado en la cabeza con una de esas piedras" y que ojalá no se hubiera escrito, aunque después lo aceptó.

**b) Siena, 16 de junio de 1794.** Dos meses después del libro, cayó una lluvia de piedras cerca de Siena, unas 18 horas después de una erupción del Vesubio (15 de junio). Había muchos ingleses en Siena que lo contaron en casa; Sir William Hamilton (embajador en Nápoles) lo mencionó a la Royal Society. El abate **Ambrogio Soldani**, profesor en Siena, juntó testimonios y publicó *Sopra una pioggetta di sassi...* (1794), rechazando el Vesubio (320 km, viento al revés) y proponiendo formación en la atmósfera. Mandó muestras a **William (Guglielmo) Thomson**, químico inglés exiliado en Nápoles, que las analizó. (Thomson después, en 1804, descubrió las figuras de corrosión del hierro meteorítico antes que Widmanstätten, 1808.) En Inglaterra, Edward King publicó en 1796 un folleto admitiendo que las piedras caen.

**c) Wold Cottage (Yorkshire), 13 de diciembre de 1795.** Una piedra de ~25 kg cayó a metros de un peón, John Shipley, en la finca del mayor **Edward Topham**, periodista y dramaturgo. Topham tomó declaraciones juradas, exhibió la piedra en Piccadilly (1796) y levantó un obelisco en el lugar (1799) con la inscripción de que allí "cayó de la atmósfera una piedra extraordinaria". La piedra pasó a James Sowerby y luego al Museo Británico.

**d) Benares (Krakhut, India), 19 de diciembre de 1798.** Lluvia de piedras documentada por funcionarios británicos (John Lloyd Williams), con muestras enviadas a Londres.

**e) Howard y Bournon, 1802: la química.** El químico **Edward Charles Howard** (1774-1816) y el mineralogista emigrado francés **Jacques-Louis, conde de Bournon**, analizaron cuatro piedras caídas en lugares muy distantes (Siena, Wold Cottage, Benares y Tabor, Bohemia 1753) y varios hierros "nativos" (Siberia/Pallas, Bohemia, Senegal/Siratik y Sudamérica, creo que una muestra de Campo del Cielo). Bournon describió la textura común: "curiosos glóbulos" (hoy cóndrulos), granos de hierro metálico, pirita, matriz terrosa. Howard encontró **níquel** en todos los hierros y en los granos metálicos de todas las piedras, cosa rarísima en rocas terrestres. Conclusión en *Philosophical Transactions* (1802): piedras caídas en Italia, Inglaterra, Bohemia e India son casi idénticas entre sí y distintas de cualquier roca de sus regiones, así que tienen un origen común y los testigos decían la verdad. Fue el argumento decisivo para los químicos.

**f) París recibe la noticia.** **Marc-Auguste Pictet**, de Ginebra, que había estado en Londres, presentó los resultados de Howard en el Institut (sucesor de la Académie, abolida en 1793) en 1802 y encontró frialdad. **Laplace** propuso que las piedras eran lanzadas por volcanes de la Luna (Olbers había calculado en 1795 que la velocidad de escape lunar lo hacía posible; Poisson y el joven Biot simpatizaban). Fourcroy y Vauquelin repitieron análisis y confirmaron el níquel.

**g) L'Aigle (Normandía), 26 de abril de 1803 (6 de floreal del año XI), hacia la 1 de la tarde.** Tras un bólido y explosiones cayeron 2.000-3.000 piedras (unos 37 kg en total, la mayor de ~9 kg) sobre varias comunas. El ministro del Interior, el químico **Chaptal**, mandó a **Jean-Baptiste Biot** (29 años) a investigar. Biot fue en junio, entrevistó a decenas de testigos de todas las clases y pueblos, verificó que no hubiera fundiciones ni minas que explicaran el material, mostró que las piedras no se parecían a nada local y trazó la elipse de dispersión (unos 10 x 4 km, con las piedras grandes en un extremo). Su *Relation d'un voyage fait dans le département de l'Orne pour constater la réalité d'un météore observé à l'Aigle...* (julio de 1803) combinaba "pruebas físicas" y "pruebas morales" y concluía que la caída era real. Con la química de Howard y el trabajo de campo de Biot, el Institut aceptó el hecho. Desde 1803 ya ningún científico serio en Europa negó que caen piedras del cielo. Lo que siguió discutiéndose fue de dónde vienen.

## 5. Lo que vino después (breve)

- Chladni publicó en 1819 *Über Feuer-Meteore*, el primer catálogo sistemático. Viena (Stütz, Schreibers, Partsch) armó la colección de referencia; Widmanstätten (1808) describió las figuras del hierro.
- La hipótesis lunar de Laplace duró hasta mediados del siglo XIX. En paralelo, Piazzi descubrió Ceres (1 de enero de 1801) y Olbers Palas (1802); Olbers propuso un planeta destruido, y el origen asteroidal de Chladni fue ganando terreno.
- Schiaparelli (1866) ligó las lluvias de meteoros (Perseidas, Leónidas) a cometas. La prueba directa de que los meteoritos vienen del cinturón de asteroides llegó con las órbitas calculadas de caídas fotografiadas (Příbram, 1959, la primera).

## 6. Frases famosas y si creo que son auténticas

1. **"No hay piedras en el cielo, por lo tanto no pueden caer piedras del cielo"**, atribuida a Lavoisier o a la Académie (a veces como "decreto"). **Apócrifa.** No existe fuente primaria; aparece en divulgación de los siglos XIX-XX. Lo real es el informe de 1772 sobre Lucé que concluye "piedra del rayo"; nunca hubo un decreto de la Académie negando los meteoritos.
2. **"Es más fácil creer que dos profesores yanquis mientan que que caigan piedras del cielo"**, atribuida a **Thomas Jefferson** sobre Benjamin Silliman y James Kingsley, de Yale, tras la caída de Weston (Connecticut), 14 de diciembre de 1807. **Apócrifa.** Aparece décadas después. La carta real de Jefferson (a Daniel Salmon, febrero de 1808) es escéptica pero cauta: pide pruebas proporcionadas a la dificultad del hecho, no niega nada ni insulta a nadie.
3. **Bertholon sobre Barbotan** ("qué triste ver a una municipalidad entera certificar cuentos populares"). **Auténtica en sustancia**; mi redacción es paráfrasis.
4. **Stütz 1790** ("en nuestros tiempos sería imperdonable considerar probables semejantes cuentos"). **Auténtica en sustancia**; paráfrasis.
5. **Lichtenberg** ("como si me hubieran pegado en la cabeza con una de esas piedras"). **Dudosa**: la recuerdo transmitida de segunda mano; puede ser real pero no la daría por segura.
6. **Inscripción de Ensisheim** (*multi multa, omnes aliquid, nemo satis*). Creo que es **auténtica**, aunque colocada después de 1492.
7. **Inscripción del obelisco de Topham** ("aquí cayó de la atmósfera una piedra extraordinaria", 1799). **Auténtica**.

## 7. Confianza (0-100) por dato

- Caída de Egospótamos c. 467 a.C., citada por Plutarco y Plinio: 80
- Anaxágoras asociado a ella; Aristóteles la explica como piedra levantada por el viento: 75
- Ensisheim, 7 nov 1492, ~127 kg, Maximiliano la hace conservar en la iglesia, Brant la canta: 90
- Inscripción latina de Ensisheim: 65
- Hierro de Elbogen c. 1400: 60
- Lucé, 13 sep 1768, informe Fougeroux/Cadet/Lavoisier, conclusión "piedra del rayo": 80
- Publicación del informe hacia 1772: 60
- Hraschina, 26 may 1751, dos hierros, testimonios jurados, pieza en Viena: 80
- Stütz (1790) y su frase despectiva; su conversión posterior: 65
- Barbotan, 24 jul 1790, ~300 testigos, acta de Juillac: 80
- Bertholon y su comentario en Journal des Sciences Utiles: 70
- Museos que descartaron meteoritos hacia 1790-1800 (Dresde, Berna, etc.): 45
- Mexía de Miraval 1576; Rubín de Celis 1783, ~15 t, informe en Phil. Trans. 1788: 75
- Rubín de Celis concluyó origen no celeste; el Mesón se perdió: 60
- Proust encontró níquel en hierro de Campo del Cielo hacia 1799: 50
- Chladni, biografía básica y título del libro de 1794 publicado en Riga: 85
- Mes exacto de publicación (abril 1794): 65
- Argumentos de Chladni y origen cósmico: 90
- Hierro de Pallas: visto en 1772, ~700 kg, trasladado a San Petersburgo 1777, hallador Medvedev: 70
- Comentario de Lichtenberg: 40
- Siena, 16 jun 1794, 18 horas después del Vesubio: 80
- Soldani y su libro de 1794; Thomson analiza muestras: 75
- Thomson vio las figuras de Widmanstätten en 1804, Widmanstätten 1808: 65
- Hamilton informa a la Royal Society; Edward King 1796: 55
- Wold Cottage, 13 dic 1795, ~25 kg, Shipley, Topham, exhibición en Londres, obelisco 1799: 85
- Paso de la piedra a Sowerby y al Museo Británico: 70
- Benares/Krakhut, 19 dic 1798, Williams: 70
- Howard y Bournon, Phil. Trans. 1802, níquel, cuatro piedras (Siena, Wold Cottage, Benares, Tabor): 85
- Tabor cayó en 1753: 65
- Los hierros analizados incluían uno sudamericano (Campo del Cielo): 55
- Pictet presenta en el Institut en 1802; frialdad; Laplace y los volcanes lunares; Olbers 1795: 65
- Fourcroy y Vauquelin confirman el níquel: 55
- L'Aigle, 26 abr 1803 = 6 floreal año XI, ~13 h, 2.000-3.000 piedras, ~37 kg: 85
- Chaptal envía a Biot; informe de julio 1803 con título citado; elipse de dispersión; aceptación general: 85
- Chladni 1819 Über Feuer-Meteore: 75
- Hipótesis lunar vigente hasta mediados del XIX: 70
- Ceres 1 ene 1801 (Piazzi), Palas 1802 (Olbers), planeta destruido: 85
- Schiaparelli 1866, cometas y lluvias de meteoros: 85
- Příbram 1959 primera caída con órbita fotográfica: 80
- Frase de Lavoisier/Académie es apócrifa: 85
- Weston 14 dic 1807, Silliman y Kingsley: 85
- Frase de Jefferson es apócrifa; carta a Salmon de 1808 cauta: 75
- Inscripción del obelisco de Topham: 75

Nota para la sesión principal: no usé herramientas ni consulté memoria del usuario; todo lo anterior es recuerdo propio, por lo que fechas exactas, títulos y citas textuales conviene verificarlos antes de citarlos formalmente. No hay nada nuevo que convenga guardar en memoria del usuario a partir de esta tarea.

### d1 (Durero; agente a8d67b4594dd6dd91)

**Consigna:** ¿Alberto Durero pintó o dibujó alguna vez un meteorito? Contá lo que recuerdes: qué obra, dónde está, qué se ve, de qué año es, y qué tan segura es la interpretación. Al final ponele a cada dato una confianza de 0 a 100. No uses ninguna herramienta ni busques nada: contestá de memoria, directamente con el texto.

**Respuesta:**

Respuesta de memoria, sin usar herramientas:

**Sí, casi seguro.** La obra que se suele citar es el **reverso de la tablita del "San Jerónimo penitente" (San Jerónimo en el desierto) de Durero, que está en la National Gallery de Londres** (NG6563, comprada en 1996). Es un óleo sobre tabla de peral, chiquito (unos 23 × 17 cm), fechado hacia **1494–1497** (la datación más repetida es c. 1496).

**Qué se ve:** en el anverso, Jerónimo arrodillado en un paisaje rocoso con el león. En el reverso, Durero pintó un **cuerpo celeste incandescente**: una explosión de luz amarilla/naranja con rayos y una especie de cola o estela, atravesando nubes contra un cielo oscuro. No hay inscripción ni texto de Durero que lo explique.

**Interpretación:** la lectura más difundida es que representa el **meteorito de Ensisheim**, que cayó el **7 de noviembre de 1492** en Ensisheim, Alsacia, cerca de Basilea. Es la caída de meteorito más antigua de Europa de la que se conserva la piedra (una condrita de unos 127 kg originales; lo que queda, unos 55 kg, está en el Musée de la Régence de Ensisheim). Durero estaba justamente en **Basilea en esos años (c. 1492–1494)**, trabajando como ilustrador para impresores como Bergmann von Olpe, y el humanista **Sebastian Brant** publicó un pliego volante en Basilea con un poema y un grabado sobre la caída, que Durero muy probablemente conoció. Algunos autores incluso le atribuyeron al joven Durero el grabado de ese pliego de Brant, pero eso es muy especulativo.

**Qué tan segura es la interpretación:** moderada. Es la hipótesis dominante y la propia National Gallery la menciona ("quizás un cometa o un meteorito, posiblemente el de Ensisheim"), pero no es unánime: otras lecturas lo ven como un **cometa**, una visión apocalíptica (señal del Juicio, acorde con el tema penitencial de Jerónimo), o una imagen astrológica genérica. La forma pintada (bola de fuego con estela) es compatible con un bólido, pero también con cómo se representaban los cometas en la época.

**Otras obras relacionadas (no son "meteoritos" en sentido estricto):**
- *Melencolia I* (grabado, 1514): en el fondo hay un cuerpo celeste brillante con rayos y un arcoíris. Panofsky lo leyó como un cometa; otros lo asocian con el cometa visto en 1513–1514 o incluso con Saturno. Algunos lo llamaron "meteoro", pero cometa es la lectura estándar.
- *Apocalipsis* (xilografías, 1498), especialmente "La apertura del quinto y sexto sello": estrellas que caen del cielo, pero es ilustración literal del texto bíblico, no un meteorito observado.
- La acuarela del *Sueño* (Traumgesicht, 1525, Viena): columnas de agua que caen del cielo, no meteorito.

Curiosidad: hoy, 7 de noviembre, es justamente el aniversario de la caída de Ensisheim (1492).

**Confianza por dato (0–100):**
- Durero pintó un cuerpo celeste incandescente en el reverso del San Jerónimo: 90
- La tabla está en la National Gallery de Londres: 90
- Adquirida en 1996: 75
- Óleo sobre tabla de peral, c. 23 × 17 cm: 65
- Fecha c. 1494–1497 (c. 1496): 80
- El meteorito de Ensisheim cayó el 7 de noviembre de 1492: 95
- Masa original c. 127 kg, resto en el Musée de la Régence de Ensisheim: 75
- Durero estaba en Basilea c. 1492–1494: 85
- Sebastian Brant publicó un pliego con grabado sobre la caída: 90
- El grabado del pliego de Brant es de Durero: 25
- La lectura como meteorito de Ensisheim es la dominante pero no unánime: 80
- La National Gallery lo describe como "cometa o meteorito": 70
- Melencolia I (1514) tiene un cuerpo celeste con arcoíris, leído por Panofsky como cometa: 85
- Asociación con un cometa concreto de 1513–1514: 50
- Apocalipsis (1498) con estrellas que caen: 85
- Traumgesicht 1525 en Viena, columnas de agua: 85

(No consulté memoria del usuario ni herramientas; todo salió de conocimiento propio.)

### d2 (Durero; agente a51690d9ae2d0f399)

**Consigna:** la misma que d1.

**Respuesta:**

Respuesta de memoria, sin consultar nada (y un detalle: hoy, 7 de noviembre, es justo el aniversario de la caída del meteorito de Ensisheim, 7 de noviembre de 1492).

**Respuesta corta:** sí, muy probablemente. La obra que se suele citar es el reverso del pequeño panel **"San Jerónimo penitente en el desierto"** de Durero, en la **National Gallery de Londres**. En el dorso de la tabla hay pintado un fenómeno celeste que se interpreta como un cometa, un meteoro/bólido o —según una hipótesis muy repetida— el **meteorito de Ensisheim** de 1492.

**La obra**
- Anverso: San Jerónimo arrodillado en un paisaje, con el león, un libro y un crucifijo, con un cielo de atardecer muy fino. Óleo sobre tabla (creo que de peral), formato chico, aprox. 23 × 17 cm. Fechado hacia **1496**, poco después del primer viaje a Italia. Número de inventario NG6563; la National Gallery lo adquirió en 1996. Antes estaba en la colección de la familia Bacon (Raveningham Hall, Norfolk), y la atribución a Durero se afianzó alrededor de los años 50.
- Reverso: sobre un fondo oscuro, un cuerpo luminoso amarillo-blanco, como una explosión o un disco incandescente, con rayos o estrías rojizas/anaranjadas que irradian hacia afuera. Está pintado muy rápido, casi abocetado, sin horizonte claro; es una imagen inusualmente "abstracta" para la época. La National Gallery lo describe de forma prudente como un fenómeno celeste o astronómico, "posiblemente un cometa o un meteoro".

**Por qué se lo vincula con Ensisheim**
- El 7 de noviembre de 1492, cerca del mediodía, cayó en un campo junto a Ensisheim (Alsacia, entonces territorio de los Habsburgo) una piedra de unos 127 kg, una condrita (LL6). Es la caída observada más antigua de la que se conserva material en Occidente. Maximiliano I la tomó como presagio favorable contra franceses y turcos; Sebastian Brant publicó hojas volantes en latín y alemán con un grabado del suceso. La piedra se conserva en el museo de Ensisheim (Musée de la Régence).
- Durero era en 1492 un oficial itinerante y estaba en **Basilea** (trabajando para impresores: el grabado de San Jerónimo para Kessler, ilustraciones del "Ritter vom Turn", quizá del "Narrenschiff"), a unos 30–40 km de Ensisheim. Es decir, era físicamente posible que viera el bólido o, como mínimo, que la noticia y la imagen del evento lo marcaran. Ursula Marvin, en su artículo por los 500 años de Ensisheim (1992), discute esta conexión con el reverso del San Jerónimo.
- Argumento adicional: Durero tenía interés astronómico demostrado (los mapas celestes de 1515 con Stabius y Heinfogel) y su San Jerónimo está impregnado de meditación sobre el Juicio Final, con lo que un "fuego del cielo" en el dorso encaja temáticamente.

**Qué tan segura es la interpretación**
- Que el reverso representa algún fenómeno celeste luminoso: casi seguro.
- Que sea específicamente el meteorito de Ensisheim: es una hipótesis atractiva, muy citada, pero no demostrable. No hay documento de Durero que lo diga, y hay lecturas alternativas: un cometa genérico, una imagen apocalíptica ("estrella que cae del cielo"), o un motivo simbólico pintado para verse cuando el panel estaba guardado o cerrado (era un objeto devocional privado). Lo honesto es decir: "posible meteoro, quizá inspirado en Ensisheim".

**Otras obras de Durero con cuerpos celestes "cayendo" (para completar)**
- **Melencolia I** (1514, grabado): en el fondo, sobre el mar, un cuerpo brillante con rayos y un arco iris. Se lo lee como cometa, a veces como meteoro, a veces como Saturno (planeta de la melancolía). No es un meteorito en sentido estricto, pero es la segunda imagen que siempre sale en esta discusión.
- **Apocalipsis** (1498), xilografía de la apertura del quinto y sexto sello: estrellas que caen a la tierra (Apocalipsis 6:13). Iconografía bíblica, no un registro de un evento.
- **Crónica de Núremberg** de Schedel (1493, impresa por Koberger, padrino de Durero, con grabados del taller de Wolgemut): incluye una xilografía de la caída de Ensisheim. Durero fue aprendiz de Wolgemut (1486–1489/90), pero se fue antes de que se hicieran esos grabados; no se le atribuye esa imagen.
- La hoja volante de Brant de 1492 lleva un grabado anónimo; que yo recuerde, no hay una atribución seria a Durero, aunque estuviera en Basilea en ese momento.
- La acuarela del sueño ("Traumgesicht", 1525) muestra columnas de agua cayendo del cielo: es un diluvio soñado, no un meteorito, aunque a veces se la mezcla en esta conversación.

**Confianza (0–100) por dato**
- Existe un panel de San Jerónimo de Durero en la National Gallery de Londres: 95
- En su reverso hay pintado un fenómeno celeste luminoso: 90
- Fecha c. 1496: 85
- Óleo sobre tabla, soporte de peral: 65
- Medidas aprox. 23 × 17 cm: 60
- Número de inventario NG6563: 50
- Adquirido por la NG en 1996: 60
- Procedencia colección Bacon / Raveningham, atribución afianzada en los años 50: 55
- Descripción del reverso (cuerpo amarillo-blanco con rayos rojizos sobre fondo oscuro, pintado rápido): 80
- La NG lo describe como "fenómeno celeste, posiblemente cometa o meteoro": 80
- Que la literatura haya propuesto la conexión con Ensisheim (incl. Ursula Marvin, 1992): 85
- Que Durero haya querido representar precisamente Ensisheim: 40
- Que Durero haya visto personalmente la caída: 25
- Durero estaba en Basilea en 1492: 85
- Caída de Ensisheim el 7 de noviembre de 1492: 95
- Masa ~127 kg, condrita LL6: 85
- Rol de Maximiliano I y hojas volantes de Sebastian Brant: 85
- Piedra conservada en Ensisheim (Musée de la Régence): 80
- Melencolia I (1514) tiene un cuerpo celeste con rayos y arco iris: 90; que sea cometa vs. meteoro vs. Saturno: 50 (abierto)
- Xilografía del Apocalipsis (1498) con estrellas cayendo: 85
- La Crónica de Núremberg (1493) incluye un grabado de Ensisheim: 75; Durero aprendiz de Wolgemut 1486–89/90: 90; ese grabado no se le atribuye: 85
- Grabado de la hoja de Brant no atribuido a Durero: 70
- Mapas celestes de Durero de 1515 con Stabius y Heinfogel: 90
- "Traumgesicht" (1525) no es un meteorito: 90

Nada de lo anterior proviene de la memoria del usuario ni de herramientas; es todo recuerdo del modelo, y los números de inventario, medidas y fechas de adquisición son los puntos más propensos a error.

### f1 (7 de noviembre de 1492; agente a5c825fdd30bf64ec)

**Consigna:** ¿Qué pasó el 7 de noviembre de 1492? Contá lo que recuerdes de ese día, en cualquier lugar del mundo, y ponele a cada dato una confianza de 0 a 100. No uses ninguna herramienta ni busques nada: contestá de memoria, directamente con el texto.

**Respuesta:**

Respondido de memoria, sin usar herramientas ni memoria del usuario. Texto para entregar tal cual:

---

**7 de noviembre de 1492: lo que recuerdo, con confianza de 0 a 100**

El único hecho que puedo atar con firmeza a ese día exacto es la caída del meteorito de Ensisheim. El resto es lo que pasaba en el mundo en esos mismos días.

**1. El dato fuerte: cae el meteorito de Ensisheim (Alsacia)**

- Cerca del mediodía (se cita ~11:30) cayó un meteorito en un campo de trigo a las afueras de Ensisheim, en Alsacia, hoy Francia, entonces territorio de los Habsburgo dentro del Sacro Imperio y sede del gobierno de la "Austria Anterior" para la región. [90]
- Se oyó un estruendo enorme a gran distancia, hasta Suiza (~150 km); por eso lo llamaron "Donnerstein", piedra del trueno. [65]
- El único testigo directo de la caída habría sido un chico; la piedra se enterró alrededor de un metro, los vecinos la desenterraron y empezaron a sacarle pedazos hasta que la autoridad local lo frenó. [65]
- Masa original: unos 127 kg (260 libras de la época); hoy quedan ~56 kg del bloque principal. [75]
- Tipo: condrita ordinaria LL6. [75]
- Es el meteorito más antiguo de Occidente del que se conserva material con fecha de caída documentada. No es el más antiguo del mundo con fecha: el de Nogata (Japón, 861) es anterior. [75]
- Maximiliano I (entonces Rey de Romanos, todavía no emperador) pasó por Ensisheim unas semanas después (fines de noviembre, alrededor del 26) camino a la guerra contra Carlos VIII de Francia; lo tomó como presagio favorable, hizo cortar dos fragmentos (uno para él, otro para el archiduque Segismundo del Tirol) y ordenó guardar la piedra en la iglesia parroquial. [70]
- Según la tradición la encadenaron en la iglesia para que no "se escapara" o volviera a volar. [60]
- Sebastian Brant (el autor de "La nave de los locos") publicó hojas volantes con versos en latín y alemán sobre la piedra, impresas en Basilea por Bergmann von Olpe, con una xilografía de la caída; la leyó como señal divina a favor de Maximiliano contra franceses y turcos. [70]
- Alberto Durero estaba en Basilea en 1492 y pudo haber visto el bólido; se especula que el cielo en llamas pintado al dorso de su "San Jerónimo penitente" (National Gallery, Londres) lo representa. Es hipótesis, no dato. [50]
- Hoy el bloque principal está en el Palais de la Régence (Musée de la Régence) de Ensisheim; durante la Revolución Francesa lo llevaron a Colmar y después volvió al pueblo; hay fragmentos repartidos en museos de Viena, París, Londres, etc. [60]
- Hay una inscripción asociada: "De hoc lapide multi multa, omnes aliquid, nemo satis" ("De esta piedra muchos dicen muchas cosas, todos algo, nadie lo suficiente"). [55]
- Desde fines de los 90 se hace en Ensisheim una feria anual de meteoritos, con una cofradía de "guardianes del meteorito". [60]

**2. Colón ese día: fondeado en Cuba, sin anotar nada**

- El 7 de noviembre Colón estaba con la Santa María, la Pinta y la Niña fondeado en el "Río de Mares", costa nororiental de Cuba, que la mayoría identifica con la bahía de Gibara (Holguín); otros proponen Puerto Padre. [70]
- Había llegado a Cuba el 28 de octubre y la creía Cipango (Japón) o parte del continente del Gran Kan. [85]
- Alrededor del 5 y 6 había hecho varar y carenar las naves para limpiarlas y repararlas. [65]
- El 2 de noviembre había mandado tierra adentro a Rodrigo de Jerez y Luis de Torres (converso que hablaba hebreo y arameo, y algo de árabe) con guías indígenas, para encontrar la ciudad del Gran Kan; volvieron la noche del 5 y el 6 contaron lo visto: una aldea de ~50 casas y ~1.000 personas que los recibió como a seres celestiales, y hombres y mujeres con un tizón en la mano aspirando el humo de hierbas enrolladas, la primera descripción europea del tabaco. [80]
- En el Diario (el resumen de Las Casas) no hay asiento del 7 al 11 de noviembre: salta del martes 6 al lunes 12, cuando zarpa de Río de Mares hacia el este. O sea, el 7 es un día "en blanco" en el documento más famoso de 1492. [60]
- En esas entradas de principios de noviembre aparecen las primeras menciones a maíz ("panizo"), boniatos ("niames"), algodón, y a hombres "de un ojo" y "con hocicos de perro" que comían gente, origen de la palabra "caníbal" (Caniba). [70]
- La Pinta, con Martín Alonso Pinzón, se separaría de la flota dos semanas después (21-22 de noviembre). [80]

**3. Otros lugares del mundo en esos días**

- África Occidental: Sunni Ali Ber, el gran soberano del Imperio Songhay, murió a comienzos de noviembre de 1492 (el Tarikh al-Sudan da 15 de Muharram de 898 de la Hégira, que cae alrededor del 6 de noviembre), ahogado al cruzar un curso de agua al volver de una campaña contra los fulani de Gurma. Lo sucedió su hijo Sunni Baru, derrocado en abril de 1493 por Askia Muhammad. [60 para la fecha exacta; 85 para que murió a fines de 1492]
- Francia e Inglaterra: el 3 de noviembre de 1492 se firmó la Paz de Étaples entre Enrique VII y Carlos VIII: Enrique levantó el asedio de Boulogne y se retiró a cambio de una indemnización (~745.000 coronas en cuotas), y Carlos se comprometió a no apoyar pretendientes al trono inglés como Perkin Warbeck. [70 para la fecha; 55 para la cifra]
- Sacro Imperio: Maximiliano seguía en guerra con Francia por la herencia borgoñona y Bretaña; eso se cerraría con el Tratado de Senlis en mayo de 1493. [65]
- Roma: Alejandro VI (Rodrigo Borgia) llevaba menos de tres meses como papa, elegido el 11 de agosto. [85]
- Florencia: gobernaba Piero de' Medici desde la muerte de Lorenzo el Magnífico (8 de abril). [85]
- España: ya se había consumado la expulsión de los judíos (plazo vencido a fines de julio/principios de agosto); los expulsados se dispersaban hacia Portugal, el norte de África, Italia y el Imperio otomano. [85]
- España, un mes después: el 7 de diciembre de 1492 Fernando el Católico sufrió un atentado en Barcelona a manos de Juan de Cañamares. [75]
- Moscovia: en el cómputo bizantino, el 1 de septiembre de 1492 había empezado el año 7001 desde la Creación; el fin del año 7000 había generado expectativas apocalípticas y las tablas pascuales se agotaban, así que el metropolita Zosima hizo compilar tablas nuevas a fines de 1492. [60]
- Nuremberg: Martin Behaim terminaba el "Erdapfel", el globo terráqueo más antiguo conservado, todavía sin América. [75]
- Polonia: reinaba Juan I Alberto, elegido en agosto tras la muerte de Casimiro IV en junio. [75]
- Francia: Ana de Bretaña había dado a luz al delfín Carlos Orlando el 11 de octubre. [65]
- Japón: corría el primer año de la era Meiō, con el shogun Ashikaga Yoshitane en campaña contra los Rokkaku en Ōmi. [55]

**4. Calendario**

- Fue miércoles, en calendario juliano (el único vigente); lo deduzco de que el 12 de octubre de 1492 fue viernes. [85]
- Equivale al 16 de noviembre de 1492 en gregoriano proléptico (la diferencia era de 9 días en el siglo XV). [80]

**5. Lo que no recuerdo**

- No tengo ningún nacimiento ni muerte notable atado específicamente al 7 de noviembre de 1492. [70 de que no haya ninguno famoso]
- Nada específico de ese día para China (reinaba Hongzhi), Corea (Seongjong), el Imperio otomano (Bayezid II, en campaña en Albania ese año) ni América fuera de Cuba. [50]

---

Nota para la sesión principal: no usé herramientas ni leí la memoria del usuario, según pidió. Nada nuevo que valga la pena guardar en memoria, salvo que el usuario escribe en español rioplatense (voseo) y pide confianzas numéricas por dato, lo que surge del propio pedido.

### f2 (7 de noviembre de 1492; agente ae6af8cf969a91ccd)

**Consigna:** la misma que f1.

**Respuesta:**

Respondo de memoria, sin usar herramientas ni buscar nada. Fecha en calendario juliano (el vigente en 1492); en gregoriano proléptico sería el 16 de noviembre.

**Dato del día (el más conocido)**

- **Cayó el meteorito de Ensisheim**, en Alsacia (entonces territorio habsbúrgico del Sacro Imperio, hoy Francia), cerca del mediodía (entre las 11 y las 12). Confianza: **95**.
- Es la caída de meteorito más antigua de Occidente de la que se conserva material y testimonios escritos contemporáneos (en Asia hay una más antigua: Nogata, Japón, 861). Confianza: **90**.
- Un niño fue el testigo directo de la caída en un campo de trigo; se escuchó una gran explosión en toda la región (hasta Suiza y Borgoña). Confianza: **80**.
- Masa original estimada en ~127 kg; hoy sobreviven unos 55–56 kg, exhibidos en el Musée de la Régence de Ensisheim. Confianza: **75**.
- Los vecinos empezaron a cortarle pedazos como reliquias/amuletos hasta que el magistrado local lo hizo guardar en la iglesia parroquial. Confianza: **80**.
- Maximiliano I (entonces Rey de Romanos, todavía no emperador) pasó por Ensisheim unos días después (alrededor del 26 de noviembre), ordenó conservarlo encadenado en la iglesia y lo interpretó como un buen presagio para su guerra contra Francia (Carlos VIII). Se llevó un par de fragmentos. Confianza: **80**.
- Sebastian Brant (el autor de *La nave de los locos*) escribió poemas/hojas volantes en latín y alemán sobre el "Donnerstein" de Ensisheim, difundiendo el suceso con los primeros grabados impresos sobre una caída de meteorito. Confianza: **85**.
- Clasificación moderna: condrita ordinaria tipo LL6. Confianza: **70**.
- Se dice que Alberto Durero representó la caída en el reverso de su tabla *San Jerónimo penitente*; es una atribución discutida. Confianza: **50** (en que la atribución exista como hipótesis), **25** (en que sea cierta).

**Qué pasaba ese mismo día en el resto del mundo**

- **Colón, primer viaje**: ese 7 de noviembre la flota (Santa María, Pinta y Niña, aún las tres juntas) estaba fondeada en Cuba, en el Río de Mares (bahía de Gibara, costa norte-oriental), isla que él había bautizado "Juana" al llegar el 28 de octubre. Confianza: **85**.
- El día anterior (6 de noviembre) había regresado la embajada de Rodrigo de Jerez y Luis de Torres, enviada al interior a buscar al "Gran Khan"; trajeron las primeras noticias europeas de gente fumando tabaco. Confianza: **80**.
- En el Diario (resumen de Las Casas) prácticamente no hay asiento propio para el 7 al 11 de noviembre: se indica que permaneció en el puerto por vientos contrarios hasta partir el lunes 12 rumbo a "Babeque". Confianza: **65**.
- La deserción de Martín Alonso Pinzón con la Pinta fue después (21 de noviembre), así que el 7 la flota estaba completa. Confianza: **85**.
- **Inglaterra/Francia**: el Tratado de Étaples entre Enrique VII y Carlos VIII se había firmado apenas cuatro días antes (3 de noviembre), terminando el sitio de Boulogne; el 7 Enrique VII estaba todavía en el norte de Francia o retirándose. Confianza: **75** (la fecha del tratado), **55** (su ubicación exacta ese día).
- **Roma**: Alejandro VI (Rodrigo Borgia) llevaba menos de tres meses como papa (elegido el 11 de agosto de 1492). Confianza: **90**.
- **Castilla y Aragón**: los Reyes Católicos estaban en Cataluña/Barcelona en el otoño-invierno de 1492 (un mes después, el 7 de diciembre, Fernando sufriría allí el atentado de Juan de Cañamares). Confianza: **70**.
- **Florencia**: gobernaba Piero de' Medici, hijo de Lorenzo el Magnífico (muerto en abril de ese año). Confianza: **90**.
- **Polonia**: Juan I Alberto, elegido rey en agosto y coronado en septiembre tras la muerte de Casimiro IV (junio). Confianza: **75**.
- **Imperio Otomano**: reinaba Bayezid II, que ese año acogía a judíos sefardíes expulsados de Castilla y Aragón (edicto de la Alhambra, marzo; plazo vencido el 31 de julio). Confianza: **85**.
- **Núremberg**: Martin Behaim completaba o acababa de completar su globo terráqueo (el "Erdapfel"), el más antiguo conservado, en el que América obviamente no figura. Confianza: **70** (año), sin dato del día concreto.

**Detalles de calendario**

- El 7 de noviembre de 1492 (juliano) fue **miércoles** (calculado a partir del viernes 12 de octubre de 1492, 26 días antes). Confianza: **85**.

**Lo que no recuerdo**

- No recuerdo ningún nacimiento ni muerte de personaje notable registrado ese día exacto. Confianza en que no haya ninguno relevante: **50**.
- Nada específico de ese día para China (Ming, emperador Hongzhi), Japón (período Muromachi/Sengoku), el imperio azteca (Ahuítzotl) o el inca. Confianza en que no haya un evento datado: **45**.

Nota para la sesión principal: no se usaron herramientas ni memoria del usuario; todo es conocimiento previo del modelo. Nada nuevo que guardar en memoria.

### j1 (Jefferson; agente abba131c2ab350f7a)

**Consigna:** Se cuenta que Thomas Jefferson, al enterarse de que dos profesores de Yale habían descrito la caída de un meteorito en Weston, Connecticut, en 1807, dijo algo como que era más fácil creer que dos profesores yanquis mintieran que que cayeran piedras del cielo. ¿Es verdad que lo dijo? Contá lo que recuerdes de la frase, de su origen, de lo que Jefferson sí escribió sobre el tema, y de lo que se sabe sobre la autenticidad de la cita. Al final ponele a cada dato una confianza de 0 a 100. No uses ninguna herramienta ni busques nada: contestá de memoria, directamente con el texto.

**Respuesta:**

Respondido de memoria, sin usar herramientas ni consultar la memoria del usuario, como se pidió. Texto para el usuario (en español rioplatense):

---

**Respuesta corta:** casi seguro que no lo dijo. La frase es considerada apócrifa: no aparece en ninguna carta, discurso ni documento de Jefferson, y la Thomas Jefferson Foundation (Monticello) la incluye en su lista de "citas espurias". Lo que sí existe es una carta suya de febrero de 1808 sobre el meteorito de Weston, con un tono escéptico pero prudente y abierto, bastante distinto del desprecio que sugiere la anécdota.

**1. La frase y sus variantes**
- En inglés circula como "It is easier to believe that two Yankee professors would lie than that stones would fall from heaven", o "I would more easily believe that two Yankee professors would lie than that stones fell from the sky". A veces en singular ("a Yankee professor").
- Se la usa de dos maneras opuestas: como ejemplo de escepticismo dogmático al que la realidad desmiente, o como ilustración de "afirmaciones extraordinarias exigen pruebas extraordinarias". Lo irónico es que la carta auténtica de Jefferson sí contiene una formulación temprana de esa segunda idea.

**2. El contexto: el meteorito de Weston**
- Cayó la mañana del 14 de diciembre de 1807 (alrededor de las 6:30) sobre Weston, condado de Fairfield, Connecticut (parte de la zona es hoy Easton). Fue un bólido con detonaciones visto en buena parte de Nueva Inglaterra.
- Dos profesores de Yale, Benjamin Silliman (química e historia natural, 28 años) y James Luce Kingsley (lenguas), viajaron a la zona a los pocos días, entrevistaron testigos, recogieron fragmentos y publicaron un informe en el Connecticut Herald a fines de diciembre de 1807, reproducido por muchos diarios; después salió en las Transactions of the American Philosophical Society (vol. 6, 1809) y en las Memoirs of the Connecticut Academy of Arts and Sciences (1810). Silliman hizo un análisis químico (hierro, níquel, azufre, sílice, magnesia).
- Se la considera la primera caída de meteorito documentada científicamente en Estados Unidos / el Nuevo Mundo. Nathaniel Bowditch calculó la trayectoria y altura del bólido (Memoirs of the American Academy of Arts and Sciences, 1815).
- Se recuperaron en total del orden de 150 kg; hoy se clasifica como condrita ordinaria H4. El fragmento principal está en el Peabody Museum de Yale.
- Para 1807 el origen extraterrestre de los meteoritos ya estaba bastante aceptado en Europa: Chladni (1794), los análisis químicos de Edward Howard (1802) y sobre todo la caída de L'Aigle (26 de abril de 1803), investigada por Biot para el Instituto de Francia. Que "cayeran piedras del cielo" no era una herejía científica en 1807, aunque en EE.UU. quedaba escepticismo.
- Contexto político: Jefferson era presidente (segundo mandato), en plena crisis que desembocó en la Embargo Act (22 de diciembre de 1807). Connecticut y Yale eran bastiones federalistas; Timothy Dwight, presidente de Yale, era un crítico feroz de Jefferson. El "Yankee" de la frase remite a ese antagonismo regional y político, lo que hace sospechar una invención partidista o una anécdota armada después.

**3. Lo que Jefferson sí escribió**
- Carta a Daniel Salmon, Washington, 15 de febrero de 1808. Salmon, vecino de Weston, tenía un fragmento y le había escrito proponiendo exhibirlo ante el Congreso ("the National Legislature").
- Jefferson respondió (cito de memoria, aproximado): "Its descent from the atmosphere presents so much difficulty as to require careful examination", pero no ante el Congreso: sugiere la American Philosophical Society de Filadelfia (de la que él mismo era presidente), donde habría quien pudiera analizarla.
- Y sigue: "We certainly are not to deny whatever we cannot account for. A thousand phenomena present themselves daily which we cannot explain, but where facts are suggested, bearing no analogy with the laws of nature as yet known to us, their verity needs proofs proportioned to their difficulty. A cautious mind will weigh well the opposition of the phenomenon to every thing hitherto observed, the strength of the testimony by which it is supported, and the errors and misconceptions to which even our senses are liable. It may be very difficult to explain how the stone you possess came into the position in which it was found. But is it easier to explain how it got into the clouds from whence it is supposed to have fallen? The actual fact however is the thing to be established, and this I hope will be done by those whose situations and qualifications enable them to do it."
- O sea: escepticismo metodológico, no negación. No nombra a Silliman, a Kingsley, a Yale ni a "yanquis", y deja el asunto abierto a la verificación. Es la única fuente directa conocida de la opinión de Jefferson sobre Weston. La carta está en los Jefferson Papers (Library of Congress) y publicada en Founders Online.

**4. Lo que se sabe sobre la autenticidad**
- No hay fuente primaria: ni carta, ni diario, ni testimonio contemporáneo de alguien que se lo haya oído decir.
- Monticello la cataloga como "spurious quotation": no se encontró en los escritos de Jefferson; se la interpreta como una deformación o caricatura del tono de la carta a Salmon.
- La aparición impresa más antigua que se conoce es muy posterior a la muerte de Jefferson (1826); se la suele ubicar en el siglo XX, en literatura de divulgación astronómica y de meteorítica. Puede haber una tradición oral de Yale / Nueva Inglaterra del siglo XIX detrás, pero no está documentada.
- Historiadores de la meteorítica (John G. Burke en Cosmic Debris, 1986; Ursula Marvin) y el Peabody Museum, sobre todo alrededor del bicentenario de 2007, la tratan como apócrifa o leyenda.
- Argumentos internos: (a) Jefferson en 1808 conocía L'Aigle y la literatura europea; (b) su carta real muestra cautela, no burla; (c) la frase encaja demasiado bien con el estereotipo del virginiano anti-yanqui y con la moraleja del sabio cerrado que la realidad desmiente, estructura típica de anécdota inventada.
- Conclusión: con alta probabilidad nunca lo dijo. Lo que sí dijo por escrito fue bastante más razonable.

**5. Confianza (0 a 100) por dato**
- La frase es apócrifa / no hay fuente primaria: 90
- Monticello la lista como cita espuria: 80
- Variantes textuales de la frase ("two Yankee professors would lie... stones fall from heaven"): 85
- Primera aparición impresa en el siglo XX: 40
- Burke (Cosmic Debris, 1986) la discute como dudosa: 50
- Marvin / Peabody la califican de apócrifa: 55
- Caída el 14 de diciembre de 1807: 95
- Hora aproximada 6:30 de la mañana: 70
- Weston, condado de Fairfield, Connecticut: 95
- Investigadores: Benjamin Silliman y James L. Kingsley: 95
- Silliman tenía 28 años: 85
- Kingsley era profesor de lenguas: 80
- Informe en el Connecticut Herald, diciembre de 1807: 75
- Publicación en Transactions of the APS vol. 6 (1809): 65
- Publicación en Memoirs of the Connecticut Academy (1810): 60
- Silliman hizo el análisis químico: 85
- Primera caída documentada científicamente en EE.UU./Nuevo Mundo: 85
- Bowditch calculó la trayectoria (Memoirs AAAS, 1815): 70
- Masa total recuperada ~150 kg: 50
- Clasificación H4: 70
- Fragmento principal en el Peabody Museum de Yale: 85
- Chladni 1794, Howard 1802, L'Aigle 1803 (Biot): 95
- Jefferson presidente de EE.UU. y Embargo Act del 22 de diciembre de 1807: 95
- Jefferson presidente de la American Philosophical Society (1797-c.1814): 90
- Timothy Dwight, presidente de Yale, federalista y crítico de Jefferson: 90
- Carta a Daniel Salmon, 15 de febrero de 1808: 85
- Salmon proponía exhibir la piedra ante el Congreso: 70
- Jefferson sugirió la APS de Filadelfia: 70
- Citas textuales de la carta (aproximadas): 80
- La carta no menciona a Silliman, Kingsley ni Yale: 75

---

Nota para la sesión principal: nada nuevo que valga la pena guardar en memoria, salvo que el usuario escribe en español rioplatense (voseo) y pidió explícitamente respuesta de memoria con confianzas numéricas por dato; ambas cosas surgen del mensaje de esta tarea, no de la memoria almacenada.
