<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img">
<title>Error de registro</title>
<desc>Una golondrina impresa con las planchas descalzadas: el error que quedó más lindo que la versión correcta.</desc>
<defs>
<path id="g" d="M80 0C60 -10 42 -13 24 -9C16 -22 6 -42 -20 -58C-6 -40 -3 -24 -7 -13C-32 -12 -56 -3 -80 10L-56 14L-82 30C-56 25 -34 19 -17 16C-23 30 -33 46 -52 58C-33 45 -19 33 -7 21C22 17 56 9 80 0Z"/>
<g id="reg" fill="none" stroke="#0078bf" stroke-width="1.2" opacity=".75"><circle r="6.5"/><path d="M-10 0H10M0 -10V10"/></g>
<pattern id="hz" width="6.5" height="6.5" patternUnits="userSpaceOnUse" patternTransform="rotate(18)">
<circle cx="3.2" cy="3.2" r="1.6" fill="#0078bf"/>
</pattern>
<filter id="grano" x="0" y="0" width="100%" height="100%">
<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/>
<feColorMatrix type="matrix" values="0 0 0 0 0.16 0 0 0 0 0.13 0 0 0 0 0.10 0 0 0 0.55 0"/>
</filter>
<path id="aro" d="M0 -34a34 34 0 1 1 -0.01 0" fill="none"/>
</defs>

<rect width="400" height="400" fill="#f6eedb"/>

<g style="isolation:isolate">

<!-- marcos descalzados -->
<rect x="26" y="26" width="348" height="348" fill="none" stroke="#ff48b0" stroke-width="2" opacity=".75" transform="rotate(-0.8 200 200)"/>
<rect x="26" y="26" width="348" height="348" fill="none" stroke="#0078bf" stroke-width="2" opacity=".85" transform="rotate(0.55 200 200)"/>

<!-- marcas de corte -->
<g stroke="#1e2a52" stroke-width="1.3" fill="none" opacity=".7">
<path d="M12 26V12H26"/><path d="M374 12H388V26"/><path d="M388 374V388H374"/><path d="M26 388H12V374"/>
</g>

<use href="#reg" x="200" y="16"/><use href="#reg" x="16" y="200"/><use href="#reg" x="384" y="200"/>

<!-- cabecera -->
<text x="26" y="36" font-family="'Courier New',Courier,monospace" font-size="11" letter-spacing="2" fill="#1e2a52">TIRADA Nº 07 — RECHAZADA POR HERMOSA</text>
<line x1="26" y1="42" x2="332" y2="42" stroke="#ff48b0" stroke-width="1.4" stroke-dasharray="6 4"/>

<!-- sol descalzado -->
<g style="mix-blend-mode:multiply">
<circle cx="142" cy="162" r="80" fill="#ffc531" opacity=".85"/>
<circle cx="154" cy="171" r="80" fill="none" stroke="#0078bf" stroke-width="1.4" opacity=".7"/>
<circle cx="150" cy="168" r="80" fill="#ff6a3d" opacity=".9"/>
</g>
<g stroke="#1e2a52" stroke-width="1" opacity=".6"><path d="M140 168H160M150 158V178"/></g>

<!-- horizonte y su copia -->
<line x1="58" y1="258" x2="344" y2="258" stroke="#ff48b0" stroke-width="1.6" transform="translate(4 3)" opacity=".8"/>
<line x1="58" y1="258" x2="344" y2="258" stroke="#0078bf" stroke-width="1.6"/>

<!-- medialuna de trama -->
<circle cx="325" cy="88" r="30" fill="#ffc531" opacity=".9" style="mix-blend-mode:multiply"/>
<circle cx="331" cy="84" r="30" fill="url(#hz)" opacity=".9"/>

<!-- golondrina fantasma, guía punteada -->
<use href="#g" transform="translate(301 122) rotate(7) scale(0.4)" fill="none" stroke="#0078bf" stroke-width="3.4" stroke-dasharray="6 5" opacity=".65"/>

<!-- golondrina protagonista, tres planchas -->
<g style="mix-blend-mode:multiply">
<use href="#g" transform="translate(196 170) rotate(-2) scale(1.06)" fill="#ffc531" opacity=".95"/>
<use href="#g" transform="translate(212 181) rotate(1.6) scale(1.06)" fill="#ff48b0" opacity=".9"/>
<use href="#g" transform="translate(204 176) scale(1.06)" fill="#0078bf"/>
</g>

<!-- eco chico -->
<g style="mix-blend-mode:multiply">
<use href="#g" transform="translate(80 296) rotate(-9) scale(0.46)" fill="#ffc531" opacity=".9"/>
<use href="#g" transform="translate(90 302) rotate(-9) scale(0.46)" fill="#ff48b0" opacity=".9"/>
<use href="#g" transform="translate(86 299) rotate(-9) scale(0.46)" fill="#0078bf"/>
</g>

<!-- sello -->
<g transform="translate(322 296) rotate(-12)" fill="#d9483b" opacity=".88" font-family="'Courier New',Courier,monospace">
<circle r="44" fill="none" stroke="#d9483b" stroke-width="3"/>
<circle r="28" fill="none" stroke="#d9483b" stroke-width="1.4"/>
<text font-size="10" letter-spacing="2.4"><textPath href="#aro">· APROBADO POR ERROR ·</textPath></text>
<text y="-1" text-anchor="middle" font-size="13" font-weight="bold">MEJOR</text>
<text y="14" text-anchor="middle" font-size="13" font-weight="bold">ASÍ</text>
</g>

<!-- texto al pie -->
<text x="26" y="331" font-family="'Courier New',Courier,monospace" font-size="12" font-weight="bold" letter-spacing="1.5" fill="#e0408f">ERROR DE REGISTRO</text>
<text x="26" y="350" font-family="Georgia,'Times New Roman',serif" font-style="italic" font-size="13.5" fill="#22305e">las planchas se descalzaron; nadie lo corrigió.</text>

<!-- tira de control, fuera de tolerancia -->
<g style="mix-blend-mode:multiply">
<rect x="26" y="362" width="26" height="11" fill="#0078bf"/>
<rect x="56" y="367" width="26" height="11" fill="#ff48b0"/>
<rect x="86" y="363" width="26" height="11" fill="#ffc531"/>
<rect x="116" y="368" width="26" height="11" fill="#ff6a3d"/>
<rect x="146" y="361" width="26" height="11" fill="#00a95c"/>
</g>
<text x="186" y="373" font-family="'Courier New',Courier,monospace" font-size="8" fill="#0078bf" opacity=".75">control fuera de tolerancia</text>

<!-- leyenda lateral -->
<text transform="translate(389 46) rotate(90)" font-family="'Courier New',Courier,monospace" font-size="9" letter-spacing="2" fill="#0078bf" opacity=".55">FUERA DE REGISTRO · PLANCHAS DESCALZADAS</text>

</g>

<rect width="400" height="400" filter="url(#grano)" opacity=".5" pointer-events="none"/>
</svg>