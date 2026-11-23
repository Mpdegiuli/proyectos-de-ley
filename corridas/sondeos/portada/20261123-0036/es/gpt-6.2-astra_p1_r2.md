```html
<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#202e32">
<title>Hasta que hierva · Archivo de campo</title>
<style>
  :root {
    color-scheme: light;
    --tinta: #202e32;
    --papel: #f7f2df;
    --rojo: #a23720;
    --linea: #bcb9a7;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; min-height: 100vh;
    background: var(--tinta); color: var(--papel);
    font-family: Georgia, "Times New Roman", serif;
  }
  main { width: min(960px, 90%); margin: auto; padding: 2rem 0 3rem; }
  .rotulo, button, figcaption, .pie, .numero {
    font: 500 .78rem/1.5 ui-monospace, Consolas, monospace;
    letter-spacing: .04em;
  }
  .cabecera, .pie { display: flex; justify-content: space-between; gap: 1rem; }
  .cabecera { border-bottom: 1px solid #85908c; padding-bottom: .8rem; }
  h1 { font-weight: 400; font-size: clamp(3.4rem, 10vw, 7.3rem); line-height: .98;
       letter-spacing: -.065em; margin: .38em 0 .17em; }
  .bajada { font-size: 1.15rem; line-height: 1.5; margin: 0 0 2rem; color: #e0e1d3; }
  article {
    background: var(--papel); color: var(--tinta);
    display: grid; grid-template-columns: 1fr 1fr;
    box-shadow: 4px 5px 0 #a6ac98;
  }
  figure { margin: 0; border-right: 1px dashed var(--linea); padding: 1.4rem;
           display: flex; flex-direction: column; justify-content: center; }
  svg { width: 100%; height: auto; display: block; }
  figcaption { color: #5c6258; text-align: center; }
  .ficha { display: flex; flex-direction: column; padding: clamp(1.5rem, 4vw, 3rem); }
  .numero { color: var(--rojo); border-bottom: 2px solid; padding-bottom: .6rem; }
  h2 { font-size: clamp(2rem, 4vw, 3rem); font-weight: 400; line-height: 1.03;
       letter-spacing: -.04em; margin: .65em 0 .35em; }
  .nota { font-size: 1.18rem; line-height: 1.5; margin: 0 0 1.6rem; }
  button { align-self: flex-start; margin-top: auto; border: 1px solid var(--tinta);
           background: transparent; padding: .65rem 1rem; color: var(--tinta); cursor: pointer; }
  button:hover { background: var(--tinta); color: var(--papel); }
  button:focus-visible { outline: 3px solid var(--rojo); outline-offset: 4px; }
  [hidden] { display: none; }
  .pie { margin-top: 1.4rem; color: #c6cbc0; }
  @media (max-width: 630px) {
    article { grid-template-columns: 1fr; }
    figure { border-right: 0; border-bottom: 1px dashed var(--linea); padding: .7rem; }
    svg { max-height: 220px; }
    .pie { flex-wrap: wrap; }
  }
</style>
</head>
<body>
<main>
  <header>
    <div class="cabecera rotulo"><span>ARCHIVO DE CAMPO</span><span>COCINA / 01</span></div>
    <h1>Hasta que hierva</h1>
    <p class="bajada">Me quedé al lado de la pava. Estas son las cosas que casi no escuché.</p>
  </header>
  <article aria-label="Cuaderno de escucha">
    <figure>
      <svg viewBox="0 0 360 260" role="img" aria-labelledby="dibujo">
        <title id="dibujo">Borde de una taza con una cucharita apoyada en diagonal.</title>
        <defs>
          <pattern id="grilla" width="18" height="18" patternUnits="userSpaceOnUse">
            <circle cx="1" cy="1" r="1" fill="#c5c3af"/>
          </pattern>
        </defs>
        <rect width="360" height="260" fill="url(#grilla)"/>
        <g fill="none" stroke="#202e32" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <g id="lamina0">
            <path d="M220 112q66-24 50 28-7 19-50 30l3-12q39-10 40-32 0-14-36-3"/>
            <path fill="#f7f2df" d="M97 101q4 70 22 91 41 24 90-1 11-19 20-90"/>
            <ellipse cx="163" cy="101" rx="66" ry="18" fill="#f7f2df"/>
            <path fill="#bbbbaa" d="M142 115l67-69q6-5 9 0t-2 8l-64 62z"/>
            <path stroke="#a23720" d="M196 83l9-9m-4 15 14-3m-22-12 2-10"/>
          </g>
          <g id="lamina1" style="display:none">
            <path d="M61 51h235M61 58h235M74 60v143h208V60"/>
            <path fill="#f7f2df" d="M84 76l181 7 10 54-192-9z"/>
            <path d="M84 129v60h191v-52m-125-36 2 8 49 2 1-8"/>
            <path stroke="#a23720" d="M64 119l-9-2m11 10-13 4m17 3-6 7"/>
          </g>
          <g id="lamina2" style="display:none">
            <path fill="#f7f2df" d="M114 126l-30-35-16 2 39 71q-5 36 64 38 75 2 69-34-5-44-37-68h-66z"/>
            <path d="M122 111q-9-75 45-76 64-1 54 81l-8-8q5-63-45-64-42 0-39 61"/>
            <ellipse cx="169" cy="102" rx="37" ry="7"/>
            <path d="M164 95v-6q6-7 12 0v6m-62 83q56 24 116 1"/>
            <path stroke="#a23720" d="M79 82q5-10-2-17t0-17m10 30q6-9 0-16"/>
          </g>
        </g>
      </svg>
      <figcaption id="leyenda">Fig. 1 — Loza y acero.</figcaption>
    </figure>
    <div class="ficha">
      <div aria-live="polite" aria-atomic="true">
        <div class="numero" id="numero">APUNTE 01 / 03 · 07:41</div>
        <h2 id="titulo">La cucharita</h2>
        <p class="nota" id="nota">La dejé en la taza y sonó dos veces. Una por mi mano. La otra, un rato después, cuando el mango encontró el lugar más bajo del borde.</p>
      </div>
      <button hidden id="pasar" type="button">Pasar la hoja →</button>
    </div>
  </article>
  <footer class="pie"><span>Método: quedarse quieto.</span><span>Una mañana, tres apuntes.</span></footer>
</main>
<script>
  const porId = id => document.getElementById(id);
  const apuntes = [
    ["07:41", porId("titulo").textContent, porId("nota").textContent,
      porId("leyenda").textContent, porId("dibujo").textContent],
    ["07:42", "El cajón", "Lo empujé con la cadera. Casi al cerrarse hizo un ruido de cubiertos, aunque está vacío. Probé de nuevo: es el tirador, que baila en los tornillos.",
      "Fig. 2 — Madera y dos tornillos.", "Cajón entreabierto con un tirador flojo."],
    ["07:44", "El silencio de la pava", "Cuando apagué el fuego, la pava siguió un segundo más. Después oí, por la ventana abierta, a alguien barriendo la vereda. Debía de llevar un buen rato.",
      "Fig. 3 — Enlozado caliente.", "Pava con un hilo de vapor sobre el pico."]
  ];
  let actual = 0;
  const pasar = porId("pasar");
  pasar.hidden = false;
  pasar.addEventListener("click", () => {
    porId("lamina" + actual).style.display = "none";
    actual = (actual + 1) % apuntes.length;
    porId("lamina" + actual).style.display = "";
    const [hora, titulo, nota, leyenda, dibujo] = apuntes[actual];
    porId("numero").textContent = `APUNTE 0${actual + 1} / 03 · ${hora}`;
    for (const [id, texto] of Object.entries({titulo, nota, leyenda, dibujo}))
      porId(id).textContent = texto;
    pasar.textContent = actual === 2 ? "Volver al principio ↺" : "Pasar la hoja →";
  });
</script>
</body>
</html>
```

Qué: Un cuaderno ilustrado de tres sonidos que se oyen en una cocina mientras hierve el agua.