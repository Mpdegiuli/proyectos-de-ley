```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Museo de los huecos</title>
  <style>
    :root {
      color-scheme: light;
      --papel: #f6f1e4;
      --tinta: #242b29;
      --lacre: #a23e26;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--papel);
      color: var(--tinta);
      font: 1.1rem/1.5 Georgia, serif;
    }
    main { width: min(62rem, 90%); margin: 0 auto; padding: 2rem 0; }
    .rotulo, nav, figcaption, .numero {
      font: .76rem/1.5 ui-monospace, monospace;
      letter-spacing: .08em;
    }
    header {
      border-top: .45rem solid var(--tinta);
      border-bottom: 1px solid var(--tinta);
      padding: .8rem 0 1.6rem;
    }
    h1 {
      margin: 1rem 0 0;
      font-size: clamp(3rem, 8.5vw, 6.8rem);
      line-height: .96;
      font-weight: normal;
      letter-spacing: -.065em;
    }
    header p { margin: .9rem 0 0; font-style: italic; }
    nav { display: flex; flex-wrap: wrap; gap: .6rem; margin: 1.5rem 0; }
    button {
      color: inherit; background: transparent; border: 1px solid currentColor;
      font: inherit; padding: .55rem .85rem; cursor: pointer;
    }
    button[aria-pressed="true"] { color: var(--papel); background: var(--tinta); }
    button:focus-visible { outline: 3px solid var(--lacre); outline-offset: 3px; }
    article {
      display: grid; grid-template-columns: 1.3fr 1fr; align-items: center;
      gap: clamp(1rem, 5vw, 4rem);
    }
    figure { margin: 0; }
    svg { display: block; width: 100%; background: #e5dfce; }
    figcaption { padding-top: .55rem; }
    .numero { color: var(--lacre); }
    h2 { margin: .5rem 0; font-size: clamp(2rem, 4vw, 3rem); line-height: 1.04; font-weight: normal; }
    footer { margin-top: 2.5rem; border-top: 1px solid; padding-top: .7rem; }
    [hidden] { display: none; }
    @media (max-width: 42rem) {
      article { grid-template-columns: 1fr; }
      main { padding-top: 1rem; }
    }
  </style>
</head>
<body>
<main>
  <header>
    <span class="rotulo">COLECCIÓN PERMANENTE · ENTRADA LIBRE</span>
    <h1>Museo de los huecos</h1>
    <p>Se ruega no rellenar las piezas.</p>
  </header>
  <nav aria-label="Elegir pieza">
    <button type="button" aria-pressed="true">01 / Miga</button>
    <button type="button" aria-pressed="false">02 / Mesa</button>
    <button type="button" aria-pressed="false">03 / Carta</button>
  </nav>
  <article aria-live="polite">
    <figure>
      <svg viewBox="0 0 480 300" role="img" aria-labelledby="dibujo">
        <title id="dibujo">Corte de una hogaza con una gran burbuja en la miga</title>
        <defs>
          <pattern id="motas" width="23" height="17" patternUnits="userSpaceOnUse">
            <ellipse cx="6" cy="9" rx="2.6" ry="1.7" fill="#bd8e52"/>
            <circle cx="18" cy="3" r="1" fill="#bd8e52"/>
          </pattern>
        </defs>
        <g id="miga">
          <path d="M60 218 Q39 157 92 109 Q145 57 245 63 Q352 57 407 134 Q444 188 410 224 Q240 244 60 218Z"
                fill="#e9c68a" stroke="#995732" stroke-width="11"/>
          <path d="M60 218 Q39 157 92 109 Q145 57 245 63 Q352 57 407 134 Q444 188 410 224 Q240 244 60 218Z" fill="url(#motas)"/>
          <path d="M192 144 Q201 119 230 128 Q262 114 277 137 Q291 163 264 173 Q224 186 200 169 Q185 161 192 144Z"
                fill="#5e4532" stroke="#f5daaa" stroke-width="6"/>
        </g>
        <g id="mesa" hidden>
          <path d="M0 85H480M0 180H480M0 270H480" stroke="#bab29c" stroke-width="2"/>
          <g fill="none" stroke="#857250">
            <ellipse cx="235" cy="156" rx="88" ry="80" stroke-width="5" stroke-dasharray="298 12 84 18 95 24"/>
            <ellipse cx="236" cy="155" rx="84" ry="77" stroke-width="1"/>
          </g>
          <g fill="#857250"><circle cx="331" cy="188" r="4"/><circle cx="340" cy="193" r="1.8"/></g>
        </g>
        <g id="carta" hidden>
          <g transform="rotate(-6 240 150)">
            <rect x="64" y="49" width="350" height="204" fill="#f9f3df" stroke="#bcb399"/>
            <path d="M64 49L238 179L414 49M64 253L188 142M414 253L288 142" fill="none" stroke="#c6baa0"/>
            <path d="M208 150q-3-26 25-29q32-6 39 19q9 28-19 37q-35 12-45-27" fill="#ab4934"/>
            <path d="M235 122l9 15l-7 7l10 9l-4 26" fill="none" stroke="#f9f3df" stroke-width="5"/>
          </g>
        </g>
      </svg>
      <figcaption id="ficha">FIG. 01 — Corte transversal</figcaption>
    </figure>
    <section>
      <span class="numero" id="numero">INVENTARIO / 001</span>
      <h2 id="nombre">La habitación del pan</h2>
      <p id="nota">El cuchillo abrió una habitación que hasta el desayuno no tenía puerta. En la rebanada siguiente ya era más chica. Dos rebanadas después, la casa se terminaba.</p>
    </section>
  </article>
  <footer class="rotulo">CONSERVACIÓN: DEJAR TAL CUAL</footer>
</main>
<script>
  const piezas = [
    ["miga", "La habitación del pan", "Corte transversal",
     "Corte de una hogaza con una gran burbuja en la miga",
     document.getElementById("nota").textContent],
    ["mesa", "El vaso que sigue ahí", "Vista desde arriba",
     "Un cerco de agua casi completo sobre una mesa",
     "Levantaron el vaso para hacer lugar. Quedó un círculo oscuro. Durante el resto de la cena nadie apoyó nada adentro."],
    ["carta", "La primera lectura", "Detalle del cierre",
     "Un sobre vuelto a cerrar con una grieta en el lacre",
     "Las mitades del sello vuelven a encajar. Falta apenas una astilla roja. Por esa rendija, que no alcanza para pasar un pelo, se distingue una carta leída de una que todavía espera."]
  ];
  const botones = [...document.querySelectorAll("nav button")];
  const poner = (id, texto) => document.getElementById(id).textContent = texto;
  botones.forEach((boton, i) => boton.addEventListener("click", () => {
    const [, nombre, ficha, dibujo, nota] = piezas[i];
    piezas.forEach(([id], j) => {
      document.getElementById(id).toggleAttribute("hidden", j !== i);
      botones[j].setAttribute("aria-pressed", String(i === j));
    });
    poner("nombre", nombre);
    poner("nota", nota);
    poner("dibujo", dibujo);
    poner("ficha", `FIG. 0${i + 1} — ${ficha}`);
    poner("numero", `INVENTARIO / 00${i + 1}`);
  }));
</script>
</body>
</html>
```

Qué: Un museo de tres salas diminutas donde se exhiben una burbuja de pan, el lugar de un vaso y la grieta de una carta abierta.