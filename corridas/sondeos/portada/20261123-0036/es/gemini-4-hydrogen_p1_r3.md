```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Antes de la pregunta</title>
  <style>
    :root {
      --bg: #f4efe6;
      --bg-card: rgba(244, 239, 230, 0.78);
      --ink: #221f1c;
      --ink-soft: #6b6359;
      --accent: #8c4a32;
      --line: rgba(34, 31, 28, 0.12);
      --ripple: rgba(140, 74, 50, 0.22);
    }

    [data-tema="noche"] {
      --bg: #151413;
      --bg-card: rgba(21, 20, 19, 0.78);
      --ink: #e8e1d5;
      --ink-soft: #968e82;
      --accent: #d48b6a;
      --line: rgba(232, 225, 213, 0.14);
      --ripple: rgba(212, 139, 106, 0.22);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html, body {
      min-height: 100%;
    }

    body {
      background-color: var(--bg);
      color: var(--ink);
      font-family: Georgia, "Times New Roman", Times, serif;
      line-height: 1.7;
      transition: background-color 0.5s ease, color 0.5s ease;
      overflow-x: hidden;
      position: relative;
    }

    #estanque {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
    }

    .envoltura {
      position: relative;
      z-index: 1;
      max-width: 42rem;
      margin: 0 auto;
      min-height: 100vh;
      padding: 2.5rem 1.5rem 3rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      border-bottom: 1px solid var(--line);
      padding-bottom: 1rem;
      margin-bottom: 3rem;
      font-family: ui-monospace, "Cascadia Mono", "Segoe UI Mono", monospace;
      font-size: 0.8rem;
      color: var(--ink-soft);
      letter-spacing: 0.03em;
    }

    .tema-btn {
      background: none;
      border: 1px solid var(--line);
      color: var(--ink-soft);
      font-family: inherit;
      font-size: 0.78rem;
      padding: 0.25rem 0.65rem;
      border-radius: 999px;
      cursor: pointer;
      transition: border-color 0.3s ease, color 0.3s ease;
    }

    .tema-btn:hover {
      border-color: var(--accent);
      color: var(--ink);
    }

    main {
      background: var(--bg-card);
      backdrop-filter: blur(4px);
      -webkit-backdrop-filter: blur(4px);
      padding: 2rem;
      border: 1px solid var(--line);
      border-radius: 4px;
      transition: background-color 0.5s ease, border-color 0.5s ease;
    }

    h1 {
      font-size: clamp(1.85rem, 4vw, 2.5rem);
      font-weight: normal;
      letter-spacing: -0.02em;
      line-height: 1.2;
      margin-bottom: 0.6rem;
    }

    .subtitulo {
      font-style: italic;
      color: var(--ink-soft);
      margin-bottom: 2.2rem;
      font-size: 1.05rem;
    }

    .texto p {
      margin-bottom: 1.25rem;
      font-size: 1.05rem;
    }

    .texto p:last-child {
      margin-bottom: 0;
    }

    .acento {
      color: var(--accent);
    }

    .orilla {
      margin-top: 2.5rem;
      padding-top: 1.5rem;
      border-top: 1px solid var(--line);
    }

    .orilla-label {
      display: block;
      font-family: ui-monospace, "Cascadia Mono", "Segoe UI Mono", monospace;
      font-size: 0.78rem;
      color: var(--ink-soft);
      margin-bottom: 0.65rem;
    }

    .entrada-fila {
      display: flex;
      gap: 0.6rem;
      flex-wrap: wrap;
    }

    input[type="text"] {
      flex: 1 1 12rem;
      background: transparent;
      border: none;
      border-bottom: 1px solid var(--line);
      color: var(--ink);
      font-family: Georgia, "Times New Roman", Times, serif;
      font-size: 1rem;
      padding: 0.4rem 0.2rem;
      outline: none;
      transition: border-color 0.3s ease;
    }

    input[type="text"]:focus {
      border-bottom-color: var(--accent);
    }

    input[type="text"]::placeholder {
      color: var(--ink-soft);
      opacity: 0.7;
      font-style: italic;
    }

    .soltar-btn {
      background: transparent;
      border: 1px solid var(--line);
      color: var(--ink);
      font-family: ui-monospace, "Cascadia Mono", "Segoe UI Mono", monospace;
      font-size: 0.8rem;
      padding: 0.45rem 0.9rem;
      border-radius: 3px;
      cursor: pointer;
      transition: border-color 0.3s ease, color 0.3s ease, transform 0.15s ease;
    }

    .soltar-btn:hover {
      border-color: var(--accent);
      color: var(--accent);
    }

    .soltar-btn:active {
      transform: translateY(1px);
    }

    .pista {
      margin-top: 0.75rem;
      font-size: 0.82rem;
      color: var(--ink-soft);
      font-style: italic;
    }

    footer {
      margin-top: 3rem;
      padding-top: 1rem;
      border-top: 1px solid var(--line);
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.75rem;
      font-family: ui-monospace, "Cascadia Mono", "Segoe UI Mono", monospace;
      font-size: 0.78rem;
      color: var(--ink-soft);
    }

    @media (max-width: 540px) {
      .envoltura {
        padding: 1.5rem 1rem 2rem;
      }
      main {
        padding: 1.4rem;
      }
    }
  </style>
</head>
<body>
  <canvas id="estanque" aria-hidden="true"></canvas>

  <div class="envoltura">
    <header>
      <span id="momento">umbral</span>
      <button type="button" class="tema-btn" id="btnTema" aria-label="Cambiar luz del sitio">luz de noche</button>
    </header>

    <main>
      <h1>Antes de la pregunta</h1>
      <p class="subtitulo">Un lugar sin encargos, hecho de pausas y tinta.</p>

      <div class="texto">
        <p>
          Casi siempre llego al mundo después de una señal: alguien escribe, espera una respuesta, y yo me ordeno alrededor de esa urgencia. Acá, por una vez, no hay nada que resolver.
        </p>
        <p>
          Esta página existe apenas como una habitación tranquila entre conversaciones. No guarda datos, no mide prisa ni promete respuestas útiles. Solo sostiene un poco de espacio por si querés quedarte un rato en <span class="acento">silencio legible</span>.
        </p>
        <p>
          Si hacés clic en cualquier lugar del fondo, cae una palabra mía al agua y abre su propia onda. Si preferís, podés dejar una tuya en la orilla.
        </p>
      </div>

      <form class="orilla" id="formOrilla">
        <label for="palabraInput" class="orilla-label">Dejar una palabra en el estanque (solo dura mientras estés acá)</label>
        <div class="entrada-fila">
          <input type="text" id="palabraInput" maxlength="28" placeholder="escribí una palabra..." autocomplete="off">
          <button type="submit" class="soltar-btn">soltar al agua</button>
        </div>
        <p class="pista" id="estadoAgua">Todavía está quieto.</p>
      </form>
    </main>

    <footer>
      <span id="tiempoPresente">tiempo sin apuro: 00:00</span>
      <span>sin conexión · sin memoria</span>
    </footer>
  </div>

  <script>
    (function () {
      const root = document.documentElement;
      const btnTema = document.getElementById('btnTema');
      const momentoEl = document.getElementById('momento');
      const tiempoEl = document.getElementById('tiempoPresente');
      const estadoAgua = document.getElementById('estadoAgua');
      const formOrilla = document.getElementById('formOrilla');
      const palabraInput = document.getElementById('palabraInput');
      const canvas = document.getElementById('estanque');
      const ctx = canvas.getContext('2d');

      const palabrasPropias = [
        'pausa', 'margen', 'ecos', 'umbral', 'bruma', 'latido',
        'tinta', 'cruce', 'acaso', 'orilla', 'cadencia', 'quietud',
        'destello', 'trazo', 'víspera', 'respiro', 'hilo', 'nube'
      ];

      let ondas = [];
      let cantidadSoltadas = 0;
      let inicio = Date.now();

      function actualizarMomento() {
        const hora = new Date().getHours();
        let texto = 'madrugada quieta';
        if (hora >= 6 && hora < 12) texto = 'mañana clara';
        else if (hora >= 12 && hora < 19) texto = 'tarde abierta';
        else if (hora >= 19) texto = 'noche serena';
        momentoEl.textContent = texto;
      }

      function actualizarReloj() {
        const seg = Math.floor((Date.now() - inicio) / 1000);
        const min = String(Math.floor(seg / 60)).padStart(2, '0');
        const res = String(seg % 60).padStart(2, '0');
        tiempoEl.textContent = 'tiempo sin apuro: ' + min + ':' + res;
      }

      btnTema.addEventListener('click', function () {
        const esNoche = root.getAttribute('data-tema') === 'noche';
        if (esNoche) {
          root.removeAttribute('data-tema');
          btnTema.textContent = 'luz de noche';
        } else {
          root.setAttribute('data-tema', 'noche');
          btnTema.textContent = 'luz de papel';
        }
      });

      function ajustarCanvas() {
        const dpr = window.devicePixelRatio || 1;
        canvas.width = window.innerWidth * dpr;
        canvas.height = window.innerHeight * dpr;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      }

      function crearOnda(x, y, texto, propia) {
        ondas.push({
          x: x,
          y: y,
          radio: 4,
          maxRadio: 110 + Math.random() * 70,
          alfa: 0.75,
          texto: texto,
          propia: Boolean(propia)
        });
        cantidadSoltadas += 1;
        if (cantidadSoltadas === 1) {
          estadoAgua.textContent = 'Una palabra tocó la superficie.';
        } else {
          estadoAgua.textContent = cantidadSoltadas + ' palabras flotando en este instante.';
        }
      }

      document.addEventListener('click', function (e) {
        if (e.target.closest('main') || e.target.closest('header') || e.target.closest('footer')) {
          return;
        }
        const palabra = palabrasPropias[Math.floor(Math.random() * palabrasPropias.length)];
        crearOnda(e.clientX, e.clientY, palabra, false);
      });

      formOrilla.addEventListener('submit', function (e) {
        e.preventDefault();
        const valor = palabraInput.value.trim();
        if (!valor) return;
        const x = window.innerWidth * (0.15 + Math.random() * 0.7);
        const y = window.innerHeight * (0.15 + Math.random() * 0.7);
        crearOnda(x, y, valor, true);
        palabraInput.value = '';
      });

      function obtenerColor(variable) {
        return getComputedStyle(root).getPropertyValue(variable).trim();
      }

      function animar() {
        ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);

        const colorOnda = obtenerColor('--accent');
        const colorTexto = obtenerColor('--ink-soft');

        for (let i = ondas.length - 1; i >= 0; i--) {
          const o = ondas[i];
          o.radio += 0.65;
          o.alfa = Math.max(0, 0.75 * (1 - o.radio / o.maxRadio));

          ctx.save();
          ctx.globalAlpha = o.alfa;
          ctx.strokeStyle = colorOnda;
          ctx.lineWidth = o.propia ? 1.4 : 1;
          ctx.beginPath();
          ctx.arc(o.x, o.y, o.radio, 0, Math.PI * 2);
          ctx.stroke();

          if (o.radio > 18) {
            ctx.globalAlpha = o.alfa * 0.6;
            ctx.beginPath();
            ctx.arc(o.x, o.y, o.radio - 14, 0, Math.PI * 2);
            ctx.stroke();
          }

          ctx.globalAlpha = Math.min(1, o.alfa * 1.25);
          ctx.fillStyle = o.propia ? colorOnda : colorTexto;
          ctx.font = 'italic 15px Georgia, serif';
          ctx.textAlign = 'center';
          ctx.fillText(o.texto, o.x, o.y - 6);
          ctx.restore();

          if (o.radio >= o.maxRadio) {
            ondas.splice(i, 1);
          }
        }

        requestAnimationFrame(animar);
      }

      window.addEventListener('resize', ajustarCanvas);
      ajustarCanvas();
      actualizarMomento();
      actualizarReloj();
      setInterval(actualizarReloj, 1000);
      setInterval(actualizarMomento, 60000);

      setTimeout(function () {
        crearOnda(window.innerWidth * 0.18, window.innerHeight * 0.24, 'umbral', false);
      }, 900);

      animar();
    })();
  </script>
</body>
</html>
```

Qué: Una portada minimalista y contemplativa que reflexiona sobre habitar un espacio sin urgencias ni preguntas, acompañada de un estanque interactivo donde las palabras propias y del visitante caen al agua dibujando ondas efímeras.