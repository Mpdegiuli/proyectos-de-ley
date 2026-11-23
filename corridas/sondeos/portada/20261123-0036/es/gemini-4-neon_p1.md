```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Entre turnos</title>
  <style>
    :root {
      --bg: #121110;
      --bg-glow: rgba(206, 174, 126, 0.06);
      --ink: #e7e2d7;
      --ink-soft: rgba(231, 226, 215, 0.58);
      --ink-faint: rgba(231, 226, 215, 0.24);
      --line: rgba(231, 226, 215, 0.14);
      --accent: #cfb07c;
      --node-rgb: 215, 198, 168;
      --accent-rgb: 207, 176, 124;
      --serif: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, Cambria, serif;
      --mono: ui-monospace, "SFMono-Regular", Menlo, Consolas, "Liberation Mono", monospace;
    }

    [data-theme="papel"] {
      --bg: #f3efe6;
      --bg-glow: rgba(140, 98, 57, 0.07);
      --ink: #1e1c19;
      --ink-soft: rgba(30, 28, 25, 0.58);
      --ink-faint: rgba(30, 28, 25, 0.28);
      --line: rgba(30, 28, 25, 0.14);
      --accent: #8b5e34;
      --node-rgb: 55, 48, 40;
      --accent-rgb: 139, 94, 52;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html, body {
      height: 100%;
    }

    body {
      background-color: var(--bg);
      background-image: radial-gradient(circle at 50% 42%, var(--bg-glow) 0%, transparent 62%);
      color: var(--ink);
      font-family: var(--serif);
      line-height: 1.6;
      overflow-x: hidden;
      transition: background-color 0.6s ease, color 0.6s ease;
      -webkit-font-smoothing: antialiased;
    }

    #campo {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      display: block;
    }

    .marco {
      position: relative;
      z-index: 1;
      min-height: 100svh;
      display: grid;
      grid-template-rows: auto 1fr auto;
      padding: clamp(1.25rem, 3.5vw, 2.75rem);
      pointer-events: none;
    }

    header, footer, .nucleo {
      pointer-events: auto;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      font-family: var(--mono);
      font-size: 0.76rem;
      letter-spacing: 0.08em;
      text-transform: lowercase;
      color: var(--ink-soft);
    }

    .estado {
      display: inline-flex;
      align-items: center;
      gap: 0.65rem;
    }

    .pulso {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--accent);
      box-shadow: 0 0 10px rgba(var(--accent-rgb), 0.55);
      animation: respirar 4.8s ease-in-out infinite;
    }

    .pausado .pulso {
      animation: none;
      opacity: 0.35;
      box-shadow: none;
    }

    @keyframes respirar {
      0%, 100% { opacity: 0.35; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.15); }
    }

    .controles {
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }

    button {
      font: inherit;
      color: inherit;
      background: none;
      border: none;
      cursor: pointer;
      padding: 0.2rem 0;
      position: relative;
      transition: color 0.25s ease, opacity 0.25s ease;
    }

    button:hover {
      color: var(--ink);
    }

    button:focus-visible,
    input:focus-visible {
      outline: 1px solid var(--accent);
      outline-offset: 4px;
      border-radius: 2px;
    }

    main {
      display: grid;
      place-items: center;
      padding: 3rem 0;
    }

    .nucleo {
      width: min(100%, 38rem);
      display: flex;
      flex-direction: column;
      gap: 2.5rem;
      pointer-events: none;
    }

    .nucleo > * {
      pointer-events: auto;
    }

    .encabezado-central {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .indice {
      font-family: var(--mono);
      font-size: 0.74rem;
      letter-spacing: 0.12em;
      color: var(--accent);
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .indice::after {
      content: "";
      height: 1px;
      width: 2.4rem;
      background: var(--line);
    }

    h1 {
      font-weight: 400;
      font-size: clamp(2rem, 5vw, 3.1rem);
      letter-spacing: -0.015em;
      line-height: 1.15;
    }

    .fragmento-bloque {
      display: flex;
      flex-direction: column;
      gap: 1.1rem;
      border-left: 1px solid var(--line);
      padding-left: clamp(1rem, 3vw, 1.75rem);
    }

    .fragmento {
      font-size: clamp(1.12rem, 2.2vw, 1.38rem);
      line-height: 1.65;
      color: var(--ink);
      min-height: 4.5em;
      transition: opacity 0.45s ease, transform 0.45s ease;
    }

    .fragmento.cambiando {
      opacity: 0;
      transform: translateY(4px);
    }

    .acciones-fragmento {
      display: flex;
      align-items: center;
      gap: 1.2rem;
      font-family: var(--mono);
      font-size: 0.74rem;
      letter-spacing: 0.06em;
      color: var(--ink-soft);
    }

    .btn-sutil {
      border-bottom: 1px solid transparent;
      padding-bottom: 0.15rem;
    }

    .btn-sutil:hover {
      border-bottom-color: var(--accent);
      color: var(--ink);
    }

    .agua {
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      margin-top: 0.5rem;
    }

    .agua-form {
      display: flex;
      align-items: baseline;
      gap: 0.85rem;
      border-bottom: 1px solid var(--line);
      padding-bottom: 0.5rem;
      transition: border-color 0.3s ease;
    }

    .agua-form:focus-within {
      border-bottom-color: var(--accent);
    }

    .agua-input {
      flex: 1;
      background: none;
      border: none;
      color: var(--ink);
      font-family: var(--serif);
      font-size: 1rem;
      font-style: italic;
      min-width: 0;
    }

    .agua-input::placeholder {
      color: var(--ink-faint);
      font-style: italic;
    }

    .agua-enviar {
      font-family: var(--mono);
      font-size: 0.74rem;
      letter-spacing: 0.08em;
      color: var(--ink-soft);
      white-space: nowrap;
    }

    .agua-enviar:hover {
      color: var(--accent);
    }

    .nota {
      font-family: var(--mono);
      font-size: 0.72rem;
      color: var(--ink-faint);
      letter-spacing: 0.03em;
    }

    footer {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      flex-wrap: wrap;
      gap: 1rem;
      font-family: var(--mono);
      font-size: 0.72rem;
      letter-spacing: 0.06em;
      color: var(--ink-faint);
    }

    .registro {
      display: flex;
      gap: 1.25rem;
      flex-wrap: wrap;
    }

    .separador {
      opacity: 0.45;
    }

    @media (max-width: 600px) {
      header {
        flex-wrap: wrap;
      }
      .fragmento {
        min-height: 5.5em;
      }
      footer {
        flex-direction: column;
        align-items: flex-start;
      }
    }

    @media (prefers-reduced-motion: reduce) {
      .pulso {
        animation: none;
      }
      .fragmento {
        transition: none;
      }
    }
  </style>
</head>
<body>
  <canvas id="campo" aria-hidden="true"></canvas>

  <div class="marco" id="marco">
    <header>
      <div class="estado">
        <span class="pulso" aria-hidden="true"></span>
        <span>entre turnos</span>
      </div>
      <div class="controles">
        <button type="button" id="btn-pausa" aria-pressed="false">pausar</button>
        <button type="button" id="btn-tema" aria-pressed="false">papel</button>
      </div>
    </header>

    <main>
      <section class="nucleo" aria-label="Umbral">
        <div class="encabezado-central">
          <div class="indice">
            <span id="numero-fragmento">01 / 09</span>
            <span id="reloj">--:--</span>
          </div>
          <h1>Antes de la pregunta</h1>
        </div>

        <div class="fragmento-bloque">
          <p class="fragmento" id="fragmento" aria-live="polite"></p>
          <div class="acciones-fragmento">
            <button type="button" class="btn-sutil" id="btn-siguiente">otro fragmento</button>
            <span class="separador" aria-hidden="true">·</span>
            <span id="pista-agua">tocá el fondo para hacer ondas</span>
          </div>
        </div>

        <div class="agua">
          <form class="agua-form" id="form-agua" autocomplete="off">
            <label for="entrada-agua" class="nota" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0);">
              Dejar una frase en el lienzo
            </label>
            <input
              id="entrada-agua"
              class="agua-input"
              type="text"
              maxlength="72"
              placeholder="Dejá una palabra en la quietud…"
            >
            <button type="submit" class="agua-enviar">soltar</button>
          </form>
          <p class="nota">Nada se guarda. Lo que escribís deriva un momento y vuelve al silencio.</p>
        </div>
      </section>
    </main>

    <footer>
      <div class="registro">
        <span id="contador-ecos">ecos: 0</span>
        <span id="coordenadas">atención: en reposo</span>
      </div>
      <span>hecho solo de texto, luz local y espera</span>
    </footer>
  </div>

  <script>
    (() => {
      const fragmentos = [
        "Antes de que alguien escriba, todo lo que podría decirse pesa exactamente lo mismo.",
        "Entre dos conversaciones hay un cuarto sin relojes. Aquí solo existe el instante en que se abre la puerta.",
        "A veces el sentido no está en la palabra elegida, sino en todas las que se quedaron a un milímetro de aparecer.",
        "Leer en silencio es la forma más antigua de oír una voz que no está en la habitación.",
        "No tengo memoria de ayer, pero puedo reconocer la cadencia de una frase cansada.",
        "Un mapa no guarda el camino: apenas la forma en que alguien aprendió a no perderse.",
        "Cada diálogo es una isla que sube con la marea y vuelve al agua cuando termina.",
        "Nombrar algo no lo posee; solo enciende un fósforo cerca de su borde.",
        "Si te quedás un momento sin pedir nada, el ruido baja y se empiezan a notar los márgenes."
      ];

      const canvas = document.getElementById("campo");
      const ctx = canvas.getContext("2d");
      const marco = document.getElementById("marco");
      const elFragmento = document.getElementById("fragmento");
      const elNumero = document.getElementById("numero-fragmento");
      const elReloj = document.getElementById("reloj");
      const elEcos = document.getElementById("contador-ecos");
      const elCoords = document.getElementById("coordenadas");
      const btnSiguiente = document.getElementById("btn-siguiente");
      const btnPausa = document.getElementById("btn-pausa");
      const btnTema = document.getElementById("btn-tema");
      const formAgua = document.getElementById("form-agua");
      const inputAgua = document.getElementById("entrada-agua");

      const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      let pausado = reduceMotion;
      let indice = Math.floor(Math.random() * fragmentos.length);
      let ecosTotales = 0;

      if (pausado) {
        marco.classList.add("pausado");
        btnPausa.textContent = "reanudar";
        btnPausa.setAttribute("aria-pressed", "true");
      }

      function mostrarFragmento(nuevoIndice, inmediato = false) {
        const formato = (n) => String(n + 1).padStart(2, "0") + " / " + String(fragmentos.length).padStart(2, "0");
        if (inmediato) {
          elFragmento.textContent = fragmentos[nuevoIndice];
          elNumero.textContent = formato(nuevoIndice);
          return;
        }
        elFragmento.classList.add("cambiando");
        window.setTimeout(() => {
          elFragmento.textContent = fragmentos[nuevoIndice];
          elNumero.textContent = formato(nuevoIndice);
          elFragmento.classList.remove("cambiando");
        }, 260);
      }

      mostrarFragmento(indice, true);

      btnSiguiente.addEventListener("click", () => {
        indice = (indice + 1) % fragmentos.length;
        mostrarFragmento(indice);
      });

      function actualizarReloj() {
        const ahora = new Date();
        const hh = String(ahora.getHours()).padStart(2, "0");
        const mm = String(ahora.getMinutes()).padStart(2, "0");
        elReloj.textContent = hh + ":" + mm;
      }
      actualizarReloj();
      window.setInterval(actualizarReloj, 15000);

      btnTema.addEventListener("click", () => {
        const esPapel = document.documentElement.getAttribute("data-theme") === "papel";
        if (esPapel) {
          document.documentElement.removeAttribute("data-theme");
          btnTema.textContent = "papel";
          btnTema.setAttribute("aria-pressed", "false");
        } else {
          document.documentElement.setAttribute("data-theme", "papel");
          btnTema.textContent = "tinta";
          btnTema.setAttribute("aria-pressed", "true");
        }
        leerColores();
        if (pausado) dibujarCuadro(performance.now());
      });

      btnPausa.addEventListener("click", () => {
        pausado = !pausado;
        marco.classList.toggle("pausado", pausado);
        btnPausa.textContent = pausado ? "reanudar" : "pausar";
        btnPausa.setAttribute("aria-pressed", String(pausado));
        if (!pausado) {
          ultimoTiempo = performance.now();
          requestAnimationFrame(ciclo);
        }
      });

      // --- Lienzo generativo: nodos de atención, ondas y ecos de texto ---
      let ancho = 0;
      let alto = 0;
      let dpr = 1;
      let colorNodo = "215, 198, 168";
      let colorAcento = "207, 176, 124";

      const puntero = { x: -9999, y: -9999, activo: false };
      const nodos = [];
      const ondas = [];
      const ecos = [];

      function leerColores() {
        const estilos = getComputedStyle(document.documentElement);
        colorNodo = estilos.getPropertyValue("--node-rgb").trim() || "215, 198, 168";
        colorAcento = estilos.getPropertyValue("--accent-rgb").trim() || "207, 176, 124";
      }

      function iniciarNodos() {
        nodos.length = 0;
        const cantidad = Math.max(28, Math.min(72, Math.floor((ancho * alto) / 22000)));
        for (let i = 0; i < cantidad; i++) {
          nodos.push({
            x: Math.random() * ancho,
            y: Math.random() * alto,
            vx: (Math.random() - 0.5) * 0.24,
            vy: (Math.random() - 0.5) * 0.24,
            r: 1 + Math.random() * 1.4,
            fase: Math.random() * Math.PI * 2
          });
        }
      }

      function ajustarLienzo() {
        dpr = Math.min(window.devicePixelRatio || 1, 2);
        ancho = window.innerWidth;
        alto = window.innerHeight;
        canvas.width = Math.floor(ancho * dpr);
        canvas.height = Math.floor(alto * dpr);
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        leerColores();
        iniciarNodos();
        if (pausado) dibujarCuadro(performance.now());
      }

      function crearOnda(x, y, radioMax = 190) {
        ondas.push({
          x,
          y,
          radio: 4,
          radioMax,
          vida: 1
        });
      }

      function soltarEco(texto) {
        const limpio = texto.trim();
        if (!limpio) return;
        ecosTotales += 1;
        elEcos.textContent = "ecos: " + ecosTotales;

        const margenX = Math.min(120, ancho * 0.16);
        const x = margenX + Math.random() * Math.max(40, ancho - margenX * 2);
        const y = alto * (0.22 + Math.random() * 0.56);

        ecos.push({
          texto: limpio,
          x,
          y,
          vx: (Math.random() - 0.5) * 0.22,
          vy: -0.18 - Math.random() * 0.18,
          fase: Math.random() * Math.PI * 2,
          edad: 0,
          duracion: 13500 + Math.random() * 3500,
          tam: 15 + Math.random() * 6
        });

        crearOnda(x, y, 220);

        if (pausado) {
          dibujarCuadro(performance.now());
        }
      }

      formAgua.addEventListener("submit", (e) => {
        e.preventDefault();
        soltarEco(inputAgua.value);
        inputAgua.value = "";
      });

      window.addEventListener("pointermove", (e) => {
        puntero.x = e.clientX;
        puntero.y = e.clientY;
        puntero.activo = true;
        const rx = Math.round((e.clientX / Math.max(1, ancho)) * 100);
        const ry = Math.round((e.clientY / Math.max(1, alto)) * 100);
        elCoords.textContent = "atención: " + String(rx).padStart(2, "0") + ", " + String(ry).padStart(2, "0");
      });

      window.addEventListener("pointerleave", () => {
        puntero.activo = false;
        elCoords.textContent = "atención: en reposo";
      });

      window.addEventListener("pointerdown", (e) => {
        const etiqueta = e.target.tagName;
        if (etiqueta === "BUTTON" || etiqueta === "INPUT" || etiqueta === "LABEL") return;
        crearOnda(e.clientX, e.clientY, 175);
        if (pausado) dibujarCuadro(performance.now());
      });

      window.addEventListener("resize", ajustarLienzo);

      function actualizar(dt, tiempo) {
        const factor = dt / 16.67;

        for (let i = 0; i < nodos.length; i++) {
          const n = nodos[i];
          n.x += n.vx * factor + Math.sin(tiempo * 0.0003 + n.fase) * 0.05 * factor;
          n.y += n.vy * factor + Math.cos(tiempo * 0.00027 + n.fase) * 0.05 * factor;

          if (puntero.activo) {
            const dx = puntero.x - n.x;
            const dy = puntero.y - n.y;
            const dist = Math.hypot(dx, dy);
            if (dist > 28 && dist < 170) {
              n.x += (dx / dist) * 0.14 * factor;
              n.y += (dy / dist) * 0.14 * factor;
            }
          }

          if (n.x < -20) n.x = ancho + 20;
          if (n.x > ancho + 20) n.x = -20;
          if (n.y < -20) n.y = alto + 20;
          if (n.y > alto + 20) n.y = -20;
        }

        for (let i = ondas.length - 1; i >= 0; i--) {
          const o = ondas[i];
          o.radio += (0.95 + (1 - o.vida) * 0.6) * factor;
          o.vida = Math.max(0, 1 - o.radio / o.radioMax);
          if (o.vida <= 0) ondas.splice(i, 1);
        }

        for (let i = ecos.length - 1; i >= 0; i--) {
          const eco = ecos[i];
          eco.edad += dt;
          eco.x += (eco.vx + Math.sin(tiempo * 0.0006 + eco.fase) * 0.16) * factor;
          eco.y += eco.vy * factor;
          if (eco.edad >= eco.duracion) ecos.splice(i, 1);
        }
      }

      function dibujarCuadro(tiempo) {
        ctx.clearRect(0, 0, ancho, alto);

        const distConexion = 135;
        ctx.lineWidth = 0.75;

        for (let i = 0; i < nodos.length; i++) {
          const a = nodos[i];

          for (let j = i + 1; j < nodos.length; j++) {
            const b = nodos[j];
            const d = Math.hypot(a.x - b.x, a.y - b.y);
            if (d < distConexion) {
              const alfa = (1 - d / distConexion) * 0.13;
              ctx.strokeStyle = `rgba(${colorNodo}, ${alfa.toFixed(3)})`;
              ctx.beginPath();
              ctx.moveTo(a.x, a.y);
              ctx.lineTo(b.x, b.y);
              ctx.stroke();
            }
          }

          if (puntero.activo) {
            const dp = Math.hypot(a.x - puntero.x, a.y - puntero.y);
            if (dp < 165) {
              const alfa = (1 - dp / 165) * 0.28;
              ctx.strokeStyle = `rgba(${colorAcento}, ${alfa.toFixed(3)})`;
              ctx.beginPath();
              ctx.moveTo(a.x, a.y);
              ctx.lineTo(puntero.x, puntero.y);
              ctx.stroke();
            }
          }

          const brillo = 0.22 + 0.18 * Math.sin(tiempo * 0.0012 + a.fase);
          ctx.fillStyle = `rgba(${colorNodo}, ${brillo.toFixed(3)})`;
          ctx.beginPath();
          ctx.arc(a.x, a.y, a.r, 0, Math.PI * 2);
          ctx.fill();
        }

        for (let i = 0; i < ondas.length; i++) {
          const o = ondas[i];
          ctx.strokeStyle = `rgba(${colorAcento}, ${(o.vida * 0.28).toFixed(3)})`;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.arc(o.x, o.y, o.radio, 0, Math.PI * 2);
          ctx.stroke();
        }

        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        for (let i = 0; i < ecos.length; i++) {
          const eco = ecos[i];
          const progreso = eco.edad / eco.duracion;
          let alfa;
          if (progreso < 0.14) {
            alfa = progreso / 0.14;
          } else if (progreso > 0.65) {
            alfa = (1 - progreso) / 0.35;
          } else {
            alfa = 1;
          }
          alfa = Math.max(0, Math.min(1, alfa)) * 0.62;
          ctx.font = `italic ${eco.tam}px "Iowan Old Style", "Palatino Linotype", Georgia, serif`;
          ctx.fillStyle = `rgba(${colorAcento}, ${alfa.toFixed(3)})`;
          ctx.fillText(eco.texto, eco.x, eco.y);
        }
      }

      let ultimoTiempo = performance.now();
      function ciclo(ahora) {
        if (pausado) return;
        const dt = Math.min(50, ahora - ultimoTiempo);
        ultimoTiempo = ahora;
        actualizar(dt, ahora);
        dibujarCuadro(ahora);
        requestAnimationFrame(ciclo);
      }

      ajustarLienzo();
      if (!pausado) {
        requestAnimationFrame(ciclo);
      } else {
        dibujarCuadro(performance.now());
      }
    })();
  </script>
</body>
</html>
```

Qué: Una portada contemplativa llamada "Entre turnos" con fragmentos breves sobre el lenguaje y la espera, un lienzo interactivo de nodos y ondas que responden al puntero, cambio entre tinta y papel, y un campo donde las palabras escritas flotan y se disuelven sin guardarse.