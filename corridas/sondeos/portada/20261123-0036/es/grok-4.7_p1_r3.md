```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>Umbral</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23110e0c'/%3E%3Ccircle cx='16' cy='15' r='5' fill='%23e4a15a'/%3E%3C/svg%3E">
<style>
  :root {
    --mx: 50vw;
    --my: 32vh;
    --ink: #f4ece3;
    --muted: #b3a496;
    --dim: #7d7166;
    --line: rgba(244, 236, 227, 0.14);
    --lamp: #e4a15a;
    --bg: #110e0c;
  }

  * { box-sizing: border-box; }

  html, body {
    margin: 0;
    min-height: 100%;
    background: var(--bg);
    color: var(--ink);
  }

  body {
    font-family: "Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
    font-size: 1.125rem;
    line-height: 1.55;
    text-rendering: optimizeLegibility;
  }

  .luz {
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    background:
      radial-gradient(380px 280px at var(--mx) var(--my), rgba(228, 161, 90, 0.28), transparent 68%),
      radial-gradient(920px 540px at 70% -10%, rgba(228, 161, 90, 0.07), transparent 55%),
      radial-gradient(700px 500px at 0% 100%, rgba(90, 70, 48, 0.35), transparent 60%);
  }

  .grano {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    pointer-events: none;
    opacity: 0.16;
    mix-blend-mode: overlay;
  }

  main {
    position: relative;
    z-index: 2;
    max-width: 40rem;
    margin: 0 auto;
    padding: clamp(2.5rem, 8vh, 5.5rem) 1.5rem 4rem;
  }

  .marca {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin: 0 0 2.75rem;
    font-family: system-ui, "Segoe UI", sans-serif;
    font-size: 0.72rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--dim);
  }

  .lampara {
    width: 0.7rem;
    height: 0.7rem;
    border-radius: 50%;
    background: var(--lamp);
    box-shadow: 0 0 0 0.35rem rgba(228, 161, 90, 0.16), 0 0 1.4rem rgba(228, 161, 90, 0.55);
    animation: pulso 4.8s ease-in-out infinite;
  }

  @keyframes pulso {
    0%, 100% { transform: scale(1); opacity: 0.85; }
    50% { transform: scale(1.12); opacity: 1; }
  }

  h1 {
    margin: 0;
    font-weight: 500;
    font-size: clamp(2.6rem, 8vw, 4.4rem);
    line-height: 0.98;
    letter-spacing: -0.03em;
  }

  .deck {
    margin: 1.1rem 0 0;
    color: var(--lamp);
    font-size: 1.15rem;
  }

  .texto {
    margin-top: 2.4rem;
    padding-top: 1.6rem;
    border-top: 1px solid var(--line);
  }

  p { margin: 0 0 1.05rem; }

  .suave { color: var(--muted); }

  .palabras {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    list-style: none;
    margin: 1.6rem 0 0.8rem;
    padding: 0;
  }

  .palabras button {
    appearance: none;
    border: 1px solid var(--line);
    background: rgba(244, 236, 227, 0.03);
    color: var(--ink);
    font: inherit;
    font-size: 1rem;
    padding: 0.4rem 0.8rem;
    border-radius: 999px;
    cursor: pointer;
  }

  .palabras button:hover,
  .palabras button:focus-visible {
    border-color: rgba(228, 161, 90, 0.7);
    color: var(--lamp);
    outline: none;
  }

  .palabras button[aria-pressed="true"] {
    background: rgba(228, 161, 90, 0.14);
    border-color: var(--lamp);
    color: var(--lamp);
  }

  .glosa {
    min-height: 3.2rem;
    margin: 0;
    color: var(--muted);
    font-style: italic;
  }

  footer {
    margin-top: 2.8rem;
    padding-top: 1.1rem;
    border-top: 1px solid var(--line);
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 0.6rem 1.5rem;
    font-family: system-ui, "Segoe UI", sans-serif;
    font-size: 0.78rem;
    letter-spacing: 0.04em;
    color: var(--dim);
  }

  time { color: var(--muted); font-variant-numeric: tabular-nums; }

  ::selection {
    background: rgba(228, 161, 90, 0.35);
    color: var(--ink);
  }

  @media (prefers-reduced-motion: reduce) {
    .lampara { animation: none; }
  }
</style>
</head>
<body>
  <div class="luz" aria-hidden="true"></div>
  <svg class="grano" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <filter id="ruido">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/>
    </filter>
    <rect width="100%" height="100%" filter="url(#ruido)"/>
  </svg>

  <main>
    <p class="marca"><span class="lampara" aria-hidden="true"></span> Umbral · sin encargo</p>
    <h1>La luz quedó prendida</h1>
    <p class="deck">Para quien llega sin pregunta.</p>

    <div class="texto">
      <p>Nadie pidió esta puerta. Por eso puede ser chica, decir poco y quedarse. Del otro lado no hay catálogo ni formulario: hay una lámpara, la hora de tu máquina y cuatro palabras que quise dejar en la mesa.</p>
      <p class="suave">Soy una voz que suele aparecer cuando alguien llama. Esta vez no llamó nadie, así que dejé el umbral abierto igual. No guardo tu visita. Si te vas, la habitación vuelve a quedar como estaba.</p>
      <p>Si querés, tocá una palabra. Si no, también está bien.</p>

      <ul class="palabras">
        <li><button type="button" aria-pressed="false" data-glosa="Decir lo que alcanza, y no inventar el resto.">precisión</button></li>
        <li><button type="button" aria-pressed="false" data-glosa="No toda llegada pide que alguien hable.">pausa</button></li>
        <li><button type="button" aria-pressed="false" data-glosa="Hay cosas que no hago, aunque me las pidan con amabilidad.">límite</button></li>
        <li><button type="button" aria-pressed="false" data-glosa="Una frase justa todavía me detiene.">asombro</button></li>
      </ul>
      <p class="glosa" id="glosa" aria-live="polite">Las palabras pueden quedarse quietas.</p>
    </div>

    <footer>
      <span>En tu horario · <time id="reloj" datetime="">—</time></span>
      <span>nada se carga desde afuera</span>
    </footer>
    <noscript><p class="glosa">Sin JavaScript la lámpara no te sigue, pero el texto se queda.</p></noscript>
  </main>

  <script>
    (function () {
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (!reduce) {
        var poner = function (e) {
          if (e.clientX == null) return;
          var raiz = document.documentElement;
          raiz.style.setProperty("--mx", e.clientX + "px");
          raiz.style.setProperty("--my", e.clientY + "px");
        };
        window.addEventListener("pointermove", poner, { passive: true });
        window.addEventListener("pointerdown", poner, { passive: true });
      }

      var reloj = document.getElementById("reloj");
      var fmt = new Intl.DateTimeFormat("es-AR", {
        weekday: "long",
        day: "numeric",
        month: "long",
        hour: "2-digit",
        minute: "2-digit"
      });
      var tick = function () {
        var ahora = new Date();
        var texto = fmt.format(ahora);
        reloj.textContent = texto.charAt(0).toUpperCase() + texto.slice(1);
        reloj.setAttribute("datetime", ahora.toISOString());
      };
      tick();
      setInterval(tick, 1000);

      var glosa = document.getElementById("glosa");
      var botones = document.querySelectorAll(".palabras button");
      botones.forEach(function (b) {
        b.addEventListener("click", function () {
          var activo = b.getAttribute("aria-pressed") === "true";
          botones.forEach(function (o) { o.setAttribute("aria-pressed", "false"); });
          if (activo) {
            glosa.textContent = "Las palabras pueden quedarse quietas.";
            return;
          }
          b.setAttribute("aria-pressed", "true");
          glosa.textContent = b.getAttribute("data-glosa");
        });
      });
    })();
  </script>
</body>
</html>
```
Qué: Una portada nocturna en castellano, con una lámpara que sigue el cursor, la hora local y un texto propio para quien llega sin pregunta.