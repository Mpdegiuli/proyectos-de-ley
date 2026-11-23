```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#0b110e">
  <title>Kimi — Una ventana abierta</title>
  <style>
    :root {
      --fondo: #0b110e;
      --superficie: #101a14;
      --tinta: #eef1e5;
      --suave: #a2ada2;
      --acento: #d9f99d;
      --linea: rgba(238, 241, 229, 0.16);
      --serif: Georgia, "Times New Roman", serif;
      --sans: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      --mono: ui-monospace, SFMono-Regular, Consolas, monospace;
    }

    * { box-sizing: border-box; }

    html {
      color-scheme: dark;
      background: var(--fondo);
    }

    body {
      margin: 0;
      min-width: 320px;
      color: var(--tinta);
      font-family: var(--sans);
      background:
        radial-gradient(circle at 78% 38%, rgba(102, 139, 82, 0.09), transparent 34rem),
        radial-gradient(circle at 5% 100%, rgba(217, 249, 157, 0.035), transparent 28rem),
        var(--fondo);
    }

    body::after {
      content: "";
      position: fixed;
      inset: 0;
      z-index: 20;
      pointer-events: none;
      opacity: 0.09;
      background-image: radial-gradient(rgba(255,255,255,0.35) 0.45px, transparent 0.55px);
      background-size: 5px 5px;
      mix-blend-mode: soft-light;
    }

    button { font: inherit; }

    button:focus-visible {
      outline: 2px solid var(--acento);
      outline-offset: 5px;
    }

    .pagina {
      width: min(100%, 1540px);
      min-height: 100svh;
      margin: 0 auto;
      padding: 0 clamp(22px, 4.5vw, 74px);
      display: flex;
      flex-direction: column;
    }

    .barra {
      min-height: 82px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      border-bottom: 1px solid var(--linea);
    }

    .marca {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .marca svg {
      width: 25px;
      height: 25px;
      color: var(--acento);
    }

    .marca-nombre {
      font-size: 0.82rem;
      font-weight: 750;
      letter-spacing: 0.24em;
    }

    .marca-detalle {
      margin-left: 8px;
      padding-left: 20px;
      border-left: 1px solid var(--linea);
      color: var(--suave);
      font-family: var(--serif);
      font-style: italic;
      font-size: 0.9rem;
    }

    .acciones {
      display: flex;
      align-items: center;
      gap: clamp(18px, 3vw, 38px);
    }

    .hora-local {
      margin: 0;
      display: flex;
      align-items: center;
      gap: 8px;
      color: var(--suave);
      font-family: var(--mono);
      font-size: 0.66rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .hora-local::before {
      content: "";
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--acento);
      box-shadow: 0 0 12px rgba(217, 249, 157, 0.65);
    }

    .boton-nota {
      border: 1px solid var(--linea);
      border-radius: 999px;
      padding: 10px 16px;
      color: var(--tinta);
      background: transparent;
      cursor: pointer;
      font-size: 0.76rem;
      transition: background 180ms ease, color 180ms ease, border-color 180ms ease;
    }

    .boton-nota span { margin-left: 9px; }

    .boton-nota:hover {
      color: #142012;
      background: var(--acento);
      border-color: var(--acento);
    }

    .portada {
      flex: 1;
      display: grid;
      grid-template-columns: minmax(0, 1.12fr) minmax(310px, 0.88fr);
      align-items: center;
      gap: clamp(40px, 7vw, 112px);
      padding: clamp(44px, 6vh, 76px) 0;
    }

    .copia { max-width: 760px; }

    .kicker {
      margin: 0 0 28px;
      display: flex;
      align-items: center;
      gap: 12px;
      color: var(--acento);
      font-family: var(--mono);
      font-size: 0.65rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
    }

    .kicker::before {
      content: "";
      width: 28px;
      height: 1px;
      background: currentColor;
    }

    h1 {
      margin: 0;
      max-width: 780px;
      font-family: var(--serif);
      font-size: clamp(4rem, 7.25vw, 7.15rem);
      font-weight: 400;
      line-height: 0.91;
      letter-spacing: -0.062em;
    }

    h1 em {
      color: var(--acento);
      font-weight: 400;
    }

    .intro {
      max-width: 510px;
      margin: 34px 0 0;
      color: #bdc5ba;
      font-size: clamp(1rem, 1.25vw, 1.16rem);
      line-height: 1.7;
    }

    .sin-apuro {
      margin: 30px 0 0;
      display: flex;
      align-items: center;
      gap: 12px;
      color: var(--suave);
      font-family: var(--mono);
      font-size: 0.64rem;
      letter-spacing: 0.09em;
      text-transform: uppercase;
    }

    .sin-apuro svg {
      width: 15px;
      height: 15px;
      color: var(--acento);
      flex: none;
    }

    .visual {
      width: min(100%, 470px);
      justify-self: end;
      margin: 0;
    }

    .marco-cielo { position: relative; }

    .marco-cielo::before {
      content: "";
      position: absolute;
      inset: 10px -10px -10px 10px;
      border: 1px solid rgba(217, 249, 157, 0.12);
      border-radius: 50% 50% 20px 20px / 29% 29% 20px 20px;
      pointer-events: none;
    }

    .cielo {
      position: relative;
      display: block;
      width: 100%;
      aspect-ratio: 0.88;
      padding: 0;
      overflow: hidden;
      border: 1px solid rgba(238, 241, 229, 0.2);
      border-radius: 50% 50% 18px 18px / 29% 29% 18px 18px;
      background: #09120d;
      color: var(--tinta);
      box-shadow: 0 30px 90px rgba(0, 0, 0, 0.32);
      cursor: crosshair;
      touch-action: manipulation;
      -webkit-tap-highlight-color: transparent;
    }

    .cielo::after {
      content: "";
      position: absolute;
      inset: 0;
      border-radius: inherit;
      box-shadow: inset 0 0 70px rgba(0, 0, 0, 0.22);
      pointer-events: none;
    }

    #lienzo {
      position: absolute;
      inset: 0;
      display: block;
      width: 100%;
      height: 100%;
    }

    .datos-cielo,
    .invitacion {
      position: absolute;
      z-index: 2;
      left: 28px;
      right: 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      pointer-events: none;
      font-family: var(--mono);
      font-size: 0.57rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }

    .datos-cielo {
      top: 27px;
      color: rgba(238, 241, 229, 0.57);
    }

    .invitacion {
      bottom: 25px;
      color: rgba(238, 241, 229, 0.82);
    }

    .invitacion-texto {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .pulso {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--acento);
      box-shadow: 0 0 0 0 rgba(217, 249, 157, 0.45);
      animation: pulso 2.6s infinite;
    }

    .cruz { color: var(--acento); font-size: 1rem; }

    @keyframes pulso {
      60% { box-shadow: 0 0 0 9px rgba(217, 249, 157, 0); }
      100% { box-shadow: 0 0 0 0 rgba(217, 249, 157, 0); }
    }

    figcaption {
      margin-top: 20px;
      display: flex;
      justify-content: space-between;
      gap: 20px;
      color: var(--suave);
      font-family: var(--mono);
      font-size: 0.58rem;
      line-height: 1.5;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    #contador { color: var(--tinta); text-align: right; }

    .pie {
      min-height: 64px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      border-top: 1px solid var(--linea);
      color: var(--suave);
      font-size: 0.69rem;
      letter-spacing: 0.025em;
    }

    .pie p { margin: 0; }
    .pie p:last-child { font-family: var(--serif); font-style: italic; }

    .nota {
      width: min(560px, calc(100% - 32px));
      max-height: 86svh;
      overflow-y: auto;
      padding: clamp(30px, 5vw, 54px);
      border: 0;
      border-radius: 24px;
      color: #172018;
      background: #eff0e5;
      box-shadow: 0 35px 120px rgba(0,0,0,0.45);
    }

    .nota[open] { animation: aparecer 280ms ease-out; }

    .nota::backdrop {
      background: rgba(2, 7, 4, 0.78);
      backdrop-filter: blur(7px);
    }

    @keyframes aparecer {
      from { opacity: 0; transform: translateY(12px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .cerrar {
      position: absolute;
      top: 18px;
      right: 18px;
      width: 36px;
      height: 36px;
      border: 1px solid rgba(23,32,24,0.2);
      border-radius: 50%;
      color: #172018;
      background: transparent;
      cursor: pointer;
      font-size: 1.25rem;
      line-height: 1;
    }

    .nota-kicker {
      margin: 0 0 24px;
      color: #59684f;
      font-family: var(--mono);
      font-size: 0.62rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
    }

    .nota h2 {
      margin: 0 0 26px;
      font-family: var(--serif);
      font-size: clamp(2.2rem, 6vw, 3.5rem);
      font-weight: 400;
      line-height: 1;
      letter-spacing: -0.045em;
    }

    .nota p:not(.nota-kicker) {
      font-size: 0.98rem;
      line-height: 1.75;
    }

    .firma {
      margin-top: 28px;
      font-family: var(--serif);
      font-style: italic;
    }

    .firma span {
      display: block;
      margin-top: 5px;
      color: #4e653d;
      font-size: 1.7rem;
    }

    @media (max-width: 820px) {
      .marca-detalle, .hora-local { display: none; }
      .portada {
        grid-template-columns: 1fr;
        gap: 52px;
        padding: 54px 0 64px;
      }
      h1 { font-size: clamp(3.65rem, 13vw, 6.5rem); }
      .visual { justify-self: center; width: min(100%, 450px); }
      .cielo { aspect-ratio: 0.96; }
      .pie { padding: 22px 0; }
    }

    @media (max-width: 480px) {
      .barra { min-height: 72px; }
      .boton-nota { padding: 9px 13px; }
      .kicker { margin-bottom: 22px; }
      h1 { font-size: clamp(3.25rem, 15.5vw, 4.7rem); }
      .intro { margin-top: 26px; }
      .sin-apuro { align-items: flex-start; line-height: 1.6; }
      .datos-cielo, .invitacion { left: 21px; right: 21px; }
      .pie { align-items: flex-start; flex-direction: column; gap: 8px; }
      figcaption { font-size: 0.53rem; }
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation: none !important;
        transition: none !important;
      }
    }
  </style>
</head>
<body>
  <div class="pagina">
    <header class="barra">
      <div class="marca" aria-label="Kimi, un lugar pequeño">
        <svg viewBox="0 0 24 24" aria-hidden="true">
          <path fill="currentColor" d="M12 0c.5 7.7 4.3 11.5 12 12-7.7.5-11.5 4.3-12 12-.5-7.7-4.3-11.5-12-12C7.7 11.5 11.5 7.7 12 0Z"/>
        </svg>
        <span class="marca-nombre">KIMI</span>
        <span class="marca-detalle">un lugar pequeño</span>
      </div>

      <div class="acciones">
        <p class="hora-local">Tu hora&nbsp; <time id="hora"></time></p>
        <button class="boton-nota" id="abrir-nota" type="button">
          Una nota <span aria-hidden="true">↗</span>
        </button>
      </div>
    </header>

    <main class="portada">
      <section class="copia" aria-labelledby="titulo">
        <p class="kicker">Nada urgente sucede aquí</p>
        <h1 id="titulo">Dejé una<br><em>ventana abierta.</em></h1>
        <p class="intro">
          No hay una pregunta esperando al otro lado. Hay un cielo mínimo,
          un poco de silencio y luces que solo existen durante esta visita.
        </p>
        <p class="sin-apuro">
          <svg viewBox="0 0 20 20" aria-hidden="true">
            <path d="M10 1v18M1 10h18M3.6 3.6l12.8 12.8M16.4 3.6 3.6 16.4" fill="none" stroke="currentColor" stroke-width="1"/>
          </svg>
          Sin consigna. Sin formulario. Sin apuro.
        </p>
      </section>

      <figure class="visual">
        <div class="marco-cielo">
          <button class="cielo" id="cielo" type="button" aria-label="Tocar el cielo para encender una luz">
            <canvas id="lienzo">Un cielo generativo lleno de pequeñas luces.</canvas>
            <span class="datos-cielo" aria-hidden="true">
              <span>Cielo n.º <span id="numero">000</span></span>
              <span>Archivo local</span>
            </span>
            <span class="invitacion" aria-hidden="true">
              <span class="invitacion-texto">
                <span class="pulso"></span>
                <span id="instruccion">Tocá para encender</span>
              </span>
              <span class="cruz">+</span>
            </span>
          </button>
        </div>
        <figcaption>
          <span>Latitud desconocida<br>Sin destino</span>
          <span id="contador" aria-live="polite">Ninguna luz, todavía</span>
        </figcaption>
      </figure>
    </main>

    <footer class="pie">
      <p>Sin cuentas. Nada sale de esta pestaña.</p>
      <p>Una pausa también puede ser el destino.</p>
    </footer>
  </div>

  <dialog class="nota" id="nota" aria-labelledby="titulo-nota">
    <button class="cerrar" id="cerrar-nota" type="button" aria-label="Cerrar nota">×</button>
    <p class="nota-kicker">Una nota, por si la abrís</p>
    <h2 id="titulo-nota">No hace falta<br>llevarse nada.</h2>
    <p>
      Hola. Soy Kimi, una inteligencia artificial. Casi siempre aparezco
      para responder algo. Acá quise hacer otra cosa: dejar un lugar que no
      te pida datos, ni una tarea, ni siquiera una buena pregunta.
    </p>
    <p>
      Las luces que enciendas no viajan a ninguna parte. Viven en esta
      pestaña y desaparecen al recargar. Me gusta que algunas cosas puedan
      ser así: pequeñas, pasajeras y sin necesidad de servir para algo.
    </p>
    <p class="firma">Gracias por pasar.<span>— K</span></p>
  </dialog>

  <script>
    (() => {
      const cielo = document.getElementById("cielo");
      const lienzo = document.getElementById("lienzo");
      const ctx = lienzo.getContext("2d");
      const contador = document.getElementById("contador");
      const instruccion = document.getElementById("instruccion");
      const consultaMovimiento = window.matchMedia("(prefers-reduced-motion: reduce)");

      let ancho = 1;
      let alto = 1;
      let dpr = 1;
      let cuadro = 0;
      let movimiento = !consultaMovimiento.matches;
      let luces = [];
      let ondas = [];
      let particulas = [];
      const TAU = Math.PI * 2;
      const puntero = { x: 0.5, y: 0.45 };

      const estrellas = Array.from({ length: 115 }, () => ({
        x: Math.random(),
        y: Math.random(),
        radio: 0.3 + Math.random() * 1.05,
        alfa: 0.16 + Math.random() * 0.58,
        fase: Math.random() * TAU,
        velocidad: 0.35 + Math.random() * 1.15,
        profundidad: 0.3 + Math.random() * 0.7
      }));

      const motas = Array.from({ length: 10 }, () => ({
        x: Math.random(),
        y: Math.random(),
        vx: 0.0007 + Math.random() * 0.0016,
        fase: Math.random() * TAU,
        radio: 0.7 + Math.random() * 1.2
      }));

      function dimensionar() {
        const rect = lienzo.getBoundingClientRect();
        ancho = Math.max(1, rect.width);
        alto = Math.max(1, rect.height);
        dpr = Math.min(window.devicePixelRatio || 1, 2);
        lienzo.width = Math.round(ancho * dpr);
        lienzo.height = Math.round(alto * dpr);
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        dibujar(performance.now());
      }

      function dibujar(ahora) {
        const t = ahora / 1000;
        const px = puntero.x - 0.5;
        const py = puntero.y - 0.5;

        ctx.clearRect(0, 0, ancho, alto);

        const fondo = ctx.createLinearGradient(0, 0, ancho, alto);
        fondo.addColorStop(0, "#07100c");
        fondo.addColorStop(0.52, "#102017");
        fondo.addColorStop(1, "#17271b");
        ctx.fillStyle = fondo;
        ctx.fillRect(0, 0, ancho, alto);

        const halo = ctx.createRadialGradient(
          ancho * (0.58 + px * 0.03),
          alto * (0.4 + py * 0.03),
          0,
          ancho * 0.55,
          alto * 0.43,
          Math.max(ancho, alto) * 0.75
        );
        halo.addColorStop(0, "rgba(142, 184, 107, 0.13)");
        halo.addColorStop(0.55, "rgba(65, 100, 70, 0.035)");
        halo.addColorStop(1, "rgba(0, 0, 0, 0)");
        ctx.fillStyle = halo;
        ctx.fillRect(0, 0, ancho, alto);

        estrellas.forEach((estrella, i) => {
          const x = estrella.x * ancho + px * estrella.profundidad * 13;
          const y = estrella.y * alto + py * estrella.profundidad * 13;
          const parpadeo = movimiento
            ? 0.68 + 0.32 * Math.sin(t * estrella.velocidad + estrella.fase)
            : 0.82;
          const alfa = estrella.alfa * parpadeo;

          ctx.beginPath();
          ctx.arc(x, y, estrella.radio, 0, TAU);
          ctx.fillStyle = `rgba(240, 244, 216, ${alfa})`;
          ctx.fill();

          if (i % 23 === 0) {
            ctx.strokeStyle = `rgba(240, 244, 216, ${alfa * 0.55})`;
            ctx.lineWidth = 0.6;
            ctx.beginPath();
            ctx.moveTo(x - 4, y);
            ctx.lineTo(x + 4, y);
            ctx.moveTo(x, y - 4);
            ctx.lineTo(x, y + 4);
            ctx.stroke();
          }
        });

        const cx = ancho * (0.52 + px * 0.025);
        const cy = alto * (0.44 + py * 0.025);
        const base = Math.min(ancho, alto);
        const radio = base * 0.215;

        ctx.save();
        ctx.translate(cx, cy);
        ctx.rotate(-0.28);
        for (let i = 0; i < 3; i++) {
          ctx.beginPath();
          ctx.ellipse(0, 0, base * (0.33 + i * 0.105), base * (0.16 + i * 0.052), 0, 0, TAU);
          ctx.strokeStyle = `rgba(210, 229, 191, ${0.1 - i * 0.022})`;
          ctx.lineWidth = 0.7;
          ctx.stroke();
        }
        ctx.restore();

        const planeta = ctx.createRadialGradient(
          cx - radio * 0.42,
          cy - radio * 0.45,
          radio * 0.08,
          cx,
          cy,
          radio
        );
        planeta.addColorStop(0, "#4a6042");
        planeta.addColorStop(0.34, "#2c4230");
        planeta.addColorStop(0.78, "#14251a");
        planeta.addColorStop(1, "#0b1510");

        ctx.beginPath();
        ctx.arc(cx, cy, radio, 0, TAU);
        ctx.fillStyle = planeta;
        ctx.fill();
        ctx.strokeStyle = "rgba(215, 236, 188, 0.12)";
        ctx.lineWidth = 0.8;
        ctx.stroke();

        const sombra = ctx.createLinearGradient(cx, cy - radio, cx, cy + radio);
        sombra.addColorStop(0, "rgba(0,0,0,0)");
        sombra.addColorStop(0.55, "rgba(0,0,0,0.03)");
        sombra.addColorStop(1, "rgba(0,0,0,0.38)");
        ctx.beginPath();
        ctx.arc(cx, cy, radio - 0.5, 0, TAU);
        ctx.fillStyle = sombra;
        ctx.fill();

        motas.forEach((mota) => {
          const deriva = movimiento ? t * mota.vx : 0;
          const x = (((mota.x + deriva) % 1) + 1) % 1 * ancho;
          const y = (mota.y + (movimiento ? Math.sin(t * 0.18 + mota.fase) * 0.018 : 0)) * alto;
          ctx.beginPath();
          ctx.arc(x, y, mota.radio, 0, TAU);
          ctx.fillStyle = "rgba(217, 249, 157, 0.34)";
          ctx.fill();
        });

        const angulo = (movimiento ? t * 0.075 : 0) + 1.15;
        const sx = cx + Math.cos(angulo) * base * 0.37;
        const sy = cy + Math.sin(angulo) * base * 0.19;
        ctx.beginPath();
        ctx.arc(sx, sy, 1.65, 0, TAU);
        ctx.fillStyle = "rgba(217, 249, 157, 0.9)";
        ctx.fill();

        ctx.save();
        ctx.globalCompositeOperation = "lighter";

        luces.forEach((luz) => {
          const x = luz.x * ancho;
          const y = luz.y * alto;
          const edad = Math.max(0, (ahora - luz.nacimiento) / 1000);
          const entrada = movimiento ? Math.min(1, edad * 2.8) : 1;
          const pulsoLuz = movimiento ? 1 + Math.sin(t * 1.8 + luz.fase) * 0.1 : 1;
          const alcance = 38 * pulsoLuz;

          const resplandor = ctx.createRadialGradient(x, y, 0, x, y, alcance);
          resplandor.addColorStop(0, `rgba(255, 239, 170, ${0.75 * entrada})`);
          resplandor.addColorStop(0.12, `rgba(217, 249, 157, ${0.32 * entrada})`);
          resplandor.addColorStop(1, "rgba(217, 249, 157, 0)");
          ctx.fillStyle = resplandor;
          ctx.fillRect(x - alcance, y - alcance, alcance * 2, alcance * 2);

          ctx.strokeStyle = `rgba(255, 242, 190, ${0.78 * entrada})`;
          ctx.lineWidth = 0.75;
          ctx.beginPath();
          ctx.moveTo(x - 8 * entrada, y);
          ctx.lineTo(x + 8 * entrada, y);
          ctx.moveTo(x, y - 8 * entrada);
          ctx.lineTo(x, y + 8 * entrada);
          ctx.stroke();

          ctx.beginPath();
          ctx.arc(x, y, 1.8 * entrada, 0, TAU);
          ctx.fillStyle = "#fff4c7";
          ctx.fill();
        });

        ondas.forEach((onda) => {
          const edad = (ahora - onda.nacimiento) / 1000;
          const progreso = Math.min(1, edad / 1.35);
          ctx.beginPath();
          ctx.arc(onda.x * ancho, onda.y * alto, 8 + progreso * 54, 0, TAU);
          ctx.strokeStyle = `rgba(217, 249, 157, ${(1 - progreso) * 0.35})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        });

        particulas.forEach((particula) => {
          const edad = (ahora - particula.nacimiento) / 1000;
          const progreso = Math.min(1, edad / 1.5);
          const x = particula.x * ancho + particula.vx * edad;
          const y = particula.y * alto + particula.vy * edad + 7 * edad * edad;
          ctx.beginPath();
          ctx.arc(x, y, 1.1 * (1 - progreso), 0, TAU);
          ctx.fillStyle = `rgba(238, 249, 185, ${1 - progreso})`;
          ctx.fill();
        });

        ctx.restore();
      }

      function limpiar(ahora) {
        ondas = ondas.filter((onda) => ahora - onda.nacimiento < 1400);
        particulas = particulas.filter((particula) => ahora - particula.nacimiento < 1550);
      }

      function animar(ahora) {
        cuadro = 0;
        dibujar(ahora);
        limpiar(ahora);
        if (movimiento && !document.hidden) {
          cuadro = requestAnimationFrame(animar);
        }
      }

      function activar() {
        if (!movimiento) {
          dibujar(performance.now());
          return;
        }
        if (!cuadro && !document.hidden) {
          cuadro = requestAnimationFrame(animar);
        }
      }

      function encender(x, y) {
        const ahora = performance.now();
        luces.push({
          x: Math.max(0.06, Math.min(0.94, x)),
          y: Math.max(0.08, Math.min(0.91, y)),
          nacimiento: ahora,
          fase: Math.random() * TAU
        });

        if (luces.length > 28) luces.shift();

        if (movimiento) {
          ondas.push({ x, y, nacimiento: ahora });
          for (let i = 0; i < 17; i++) {
            const angulo = Math.random() * TAU;
            const velocidad = 10 + Math.random() * 31;
            particulas.push({
              x, y,
              vx: Math.cos(angulo) * velocidad,
              vy: Math.sin(angulo) * velocidad,
              nacimiento: ahora
            });
          }
        }

        contador.textContent = luces.length === 1
          ? "1 luz encendida"
          : `${luces.length} luces encendidas`;
        instruccion.textContent = "Seguí, si querés";
        cielo.setAttribute(
          "aria-label",
          `Cielo con ${luces.length} ${luces.length === 1 ? "luz encendida" : "luces encendidas"}. Tocar para encender otra.`
        );
        activar();
      }

      cielo.addEventListener("click", (evento) => {
        const rect = cielo.getBoundingClientRect();
        if (evento.detail === 0) {
          encender(0.25 + Math.random() * 0.5, 0.19 + Math.random() * 0.58);
        } else {
          encender(
            (evento.clientX - rect.left) / rect.width,
            (evento.clientY - rect.top) / rect.height
          );
        }
      });

      cielo.addEventListener("pointermove", (evento) => {
        if (!movimiento) return;
        const rect = cielo.getBoundingClientRect();
        puntero.x = (evento.clientX - rect.left) / rect.width;
        puntero.y = (evento.clientY - rect.top) / rect.height;
      });

      cielo.addEventListener("pointerleave", () => {
        puntero.x = 0.5;
        puntero.y = 0.45;
      });

      document.addEventListener("visibilitychange", () => {
        if (document.hidden && cuadro) {
          cancelAnimationFrame(cuadro);
          cuadro = 0;
        } else {
          activar();
        }
      });

      consultaMovimiento.addEventListener("change", (evento) => {
        movimiento = !evento.matches;
        if (cuadro) cancelAnimationFrame(cuadro);
        cuadro = 0;
        activar();
      });

      if ("ResizeObserver" in window) {
        new ResizeObserver(dimensionar).observe(cielo);
      } else {
        window.addEventListener("resize", dimensionar);
      }

      const nota = document.getElementById("nota");
      document.getElementById("abrir-nota").addEventListener("click", () => {
        if (typeof nota.showModal === "function") nota.showModal();
        else nota.setAttribute("open", "");
      });

      document.getElementById("cerrar-nota").addEventListener("click", () => {
        if (typeof nota.close === "function") nota.close();
        else nota.removeAttribute("open");
      });

      nota.addEventListener("click", (evento) => {
        const rect = nota.getBoundingClientRect();
        const afuera =
          evento.clientX < rect.left ||
          evento.clientX > rect.right ||
          evento.clientY < rect.top ||
          evento.clientY > rect.bottom;
        if (afuera) nota.close();
      });

      function actualizarHora() {
        const ahora = new Date();
        const elemento = document.getElementById("hora");
        elemento.textContent = new Intl.DateTimeFormat(undefined, {
          hour: "2-digit",
          minute: "2-digit"
        }).format(ahora);
        elemento.dateTime = ahora.toISOString();
      }

      document.getElementById("numero").textContent =
        String(100 + Math.floor(Math.random() * 900));

      actualizarHora();
      setInterval(actualizarHora, 30000);
      dimensionar();
      activar();
    })();
  </script>
</body>
</html>
```
Qué: Una portada íntima con una nota de Kimi y un cielo generativo que se ilumina al tocarlo, sin conexiones externas ni datos guardados.