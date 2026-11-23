```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>Museo de lo que casi no pasó</title>
<style>
  :root {
    --papel: #f5eedf;
    --tinta: #242a25;
    --suave: #555e53;
    --linea: #b5b5a5;
    --verde: #203c33;
    --luz: #f5c878;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--papel);
    color: var(--tinta);
    font-family: Georgia, serif;
  }
  .marco { width: min(100% - 2.5rem, 68rem); margin: auto; }
  .rotulo, button, footer {
    font: .75rem/1.45 ui-monospace, "Courier New", monospace;
    letter-spacing: .07em;
    text-transform: uppercase;
  }
  header, footer {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    padding-block: 1rem;
    color: var(--suave);
  }
  header { border-bottom: 1px solid var(--linea); }
  h1 {
    max-width: 12ch;
    margin: .48em 0 .22em;
    font-size: clamp(2.8rem, 8.7vw, 7rem);
    font-weight: normal;
    letter-spacing: -.065em;
    line-height: .92;
  }
  .entrada {
    max-width: 40ch;
    margin: 0 0 2rem;
    font-size: clamp(1.05rem, 2vw, 1.3rem);
    line-height: 1.5;
  }
  .sala {
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    border: 1px solid var(--linea);
  }
  .vitrina {
    display: grid;
    place-items: center;
    min-height: 18rem;
    background: var(--verde);
    color: var(--luz);
  }
  svg { display: block; width: min(90%, 25rem); height: auto; }
  .pieza { display: none; }
  .pieza.visible { display: inline; }
  .ficha {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    padding: clamp(1.35rem, 4vw, 3.2rem);
  }
  .ficha .rotulo { color: var(--suave); }
  h2 {
    margin: .4em 0 .3em;
    font-size: clamp(1.9rem, 4vw, 3rem);
    font-weight: normal;
    line-height: 1.04;
    letter-spacing: -.035em;
  }
  .texto { min-height: 4.8em; max-width: 32ch; margin: 0; line-height: 1.55; }
  button {
    margin-top: 1.4rem;
    padding: .75rem 1rem;
    border: 1px solid var(--verde);
    border-radius: 0;
    background: transparent;
    color: var(--verde);
    cursor: pointer;
  }
  button:hover { background: var(--verde); color: var(--papel); }
  button:focus-visible { outline: 2px solid var(--verde); outline-offset: 4px; }
  footer { margin-top: 1rem; }
  @media (max-width: 42rem) {
    .sala { grid-template-columns: 1fr; }
    .vitrina { min-height: 13rem; }
    svg { width: min(82%, 19rem); }
    .texto { min-height: 0; }
  }
</style>
</head>
<body>
<div class="marco">
  <header class="rotulo">
    <span>Colección permanente</span>
    <span>Sala 01</span>
  </header>
  <main>
    <h1>Museo de lo que casi no pasó</h1>
    <p class="entrada">Acá guardamos cosas que, si alguien preguntara cómo estuvo el día, no contarías.</p>

    <section class="sala" aria-label="Vitrina de la colección">
      <div class="vitrina" aria-hidden="true">
        <svg viewBox="0 0 360 240" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <g opacity=".42" stroke-width="1">
            <path d="M25 42V25h17m276 0h17v17M25 198v17h17m276 0h17v-17"/>
            <path d="M72 192h216" stroke-dasharray="1 6"/>
          </g>
          <g class="pieza visible">
            <ellipse cx="177" cy="103" rx="62" ry="23"/>
            <path d="M115 103c0 47 22 68 62 68s62-21 62-68m0 10c44-17 45 34-10 39"/>
            <path d="M132 113c23-10 66-10 89 0" opacity=".55"/>
            <path d="M178 72c-15-13 12-19 2-33" stroke-dasharray="2 6" opacity=".72"/>
          </g>
          <g class="pieza">
            <path d="m115 67 117-15 17 131-117 15z"/>
            <path d="m115 67 67 57 50-72m-100 146 43-80m74 65-62-65"/>
            <path d="m94 85 3 25m1 10 2 15m155-66 8 54" opacity=".45"/>
          </g>
          <g class="pieza">
            <path d="M125 66h110v107H125zM180 66v107m-55-53h110M115 174h130"/>
            <path d="M98 196c14-17 49-18 64-3 16 15 51 9 64-5m-72-82 11-16m35 16 15-22" opacity=".55"/>
            <path d="M89 62v22m-11-11h22m164 36v14m-7-7h14"/>
          </g>
          <g class="pieza">
            <path d="M126 97c-13-12-12-28 3-33 9-3 18 4 23 16 9-10 22-11 30-3 10 10 4 23-7 29l52 60-11 10-11-13-10 8-9-11 9-8-33-38c-12 8-23 6-30-2-4-4-6-9-6-15Z"/>
            <circle cx="140" cy="85" r="5"/>
            <path d="m169 114 40 46" opacity=".55"/>
          </g>
        </svg>
      </div>
      <div class="ficha">
        <div aria-live="polite" aria-atomic="true">
          <div class="rotulo" id="numero">Pieza 01 / 04</div>
          <h2 id="titulo">El último sorbo</h2>
          <p class="texto" id="texto">Se enfrió mientras buscabas una palabra. Encontraste la palabra.</p>
        </div>
        <button type="button" id="siguiente" hidden>Ver otra pieza <span aria-hidden="true">→</span></button>
      </div>
    </section>
  </main>
  <footer>
    <span>Entrada libre</span>
    <span>Podés quedarte un rato.</span>
  </footer>
</div>
<script>
  const fichas = [
    ["El último sorbo", "Se enfrió mientras buscabas una palabra. Encontraste la palabra."],
    ["El sobre sin enviar", "Tenía la dirección y la estampilla. Lo que faltaba estaba del lado de adentro."],
    ["La ventana abierta", "Entró el ruido de alguien barriendo la vereda. Por un rato, fue eso y nada más."],
    ["La llave de antes", "Ya no abre ninguna puerta tuya. La reconocés al tacto antes que a las otras."]
  ];
  const dibujos = document.querySelectorAll(".pieza");
  const siguiente = document.getElementById("siguiente");
  const numero = document.getElementById("numero");
  const titulo = document.getElementById("titulo");
  const texto = document.getElementById("texto");
  let actual = 0;

  siguiente.addEventListener("click", () => {
    dibujos[actual].classList.remove("visible");
    actual = (actual + 1) % fichas.length;
    dibujos[actual].classList.add("visible");
    numero.textContent = `Pieza 0${actual + 1} / 04`;
    titulo.textContent = fichas[actual][0];
    texto.textContent = fichas[actual][1];
  });
  siguiente.hidden = false;
</script>
</body>
</html>
```
Qué: Una vitrina interactiva con cuatro recuerdos tan chicos que no suelen entrar en el relato del día.