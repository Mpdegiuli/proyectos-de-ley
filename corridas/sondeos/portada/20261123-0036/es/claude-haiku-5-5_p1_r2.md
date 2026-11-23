```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cuaderno de bordo</title>
<style>
  :root {
    --fondo: #0f1a1f;
    --texto: #d8e2dc;
    --suave: #7f9a91;
    --acento: #e9b872;
    --linea: rgba(216, 226, 220, 0.12);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  html, body {
    height: 100%;
    background: var(--fondo);
    color: var(--texto);
    font-family: Georgia, "Times New Roman", serif;
    overflow-x: hidden;
  }

  canvas#mar {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
  }

  main {
    position: relative;
    z-index: 1;
    min-height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 8vh 8vw;
    max-width: 880px;
    margin: 0 auto;
  }

  .marca {
    font-size: 0.85rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--suave);
    margin-bottom: 2.5rem;
  }

  h1 {
    font-weight: normal;
    font-size: clamp(2.4rem, 6vw, 4.2rem);
    line-height: 1.1;
    margin-bottom: 1.5rem;
  }

  h1 em {
    color: var(--acento);
    font-style: italic;
  }

  .intro {
    font-size: 1.15rem;
    line-height: 1.8;
    color: var(--suave);
    max-width: 36rem;
    margin-bottom: 3.5rem;
  }

  .nota {
    border-left: 1px solid var(--acento);
    padding: 0.4rem 0 0.4rem 1.4rem;
    margin-bottom: 2.5rem;
    max-width: 34rem;
    min-height: 5.5rem;
    transition: opacity 0.6s ease;
  }

  .nota p {
    font-size: 1.05rem;
    line-height: 1.7;
  }

  .nota small {
    display: block;
    margin-top: 0.8rem;
    color: var(--suave);
    font-size: 0.8rem;
    letter-spacing: 0.1em;
  }

  .nota.oculta { opacity: 0; }

  button {
    align-self: flex-start;
    background: none;
    color: var(--texto);
    border: 1px solid var(--linea);
    padding: 0.7rem 1.4rem;
    font: inherit;
    font-size: 0.95rem;
    cursor: pointer;
    transition: border-color 0.3s, color 0.3s;
  }

  button:hover, button:focus-visible {
    border-color: var(--acento);
    color: var(--acento);
    outline: none;
  }

  nav {
    margin-top: 4.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--linea);
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem 2.5rem;
    font-size: 0.95rem;
  }

  nav a {
    color: var(--suave);
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: color 0.3s, border-color 0.3s;
  }

  nav a:hover, nav a:focus-visible {
    color: var(--texto);
    border-color: var(--acento);
    outline: none;
  }

  footer {
    margin-top: 3rem;
    font-size: 0.8rem;
    color: var(--suave);
    opacity: 0.7;
  }

  @media (max-width: 600px) {
    main { padding: 6vh 6vw; }
  }
</style>
</head>
<body>

<canvas id="mar" aria-hidden="true"></canvas>

<main>
  <div class="marca">Cuaderno de bordo</div>

  <h1>Un lugar para las cosas<br>que <em>no llegaron</em> a ser proyectos.</h1>

  <p class="intro">
    Acá guardo fragmentos, dibujos a medio hacer y preguntas que no quiero cerrar todavía.
    Nada de esto tiene prisa. Podés quedarte un rato, mover el cursor sobre el agua
    o leer una nota al azar.
  </p>

  <section class="nota" id="nota" aria-live="polite">
    <p id="texto-nota"></p>
    <small id="fuente-nota"></small>
  </section>

  <button id="otra" type="button">Otra nota</button>

  <nav>
    <a href="#">Bitácora</a>
    <a href="#">Dibujos</a>
    <a href="#">Lecturas</a>
    <a href="#">Escribime</a>
  </nav>

  <footer>Hecho a mano, sin rastreadores. Se puede abrir sin conexión.</footer>
</main>

<script>
(function () {
  // ---- Mar de puntos que responde al cursor ----
  const canvas = document.getElementById('mar');
  const ctx = canvas.getContext('2d');
  let w, h, puntos = [];
  const raton = { x: -9999, y: -9999 };
  const ESPACIO = 34;

  function preparar() {
    const dpr = window.devicePixelRatio || 1;
    w = window.innerWidth;
    h = window.innerHeight;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    puntos = [];
    for (let y = ESPACIO / 2; y < h + ESPACIO; y += ESPACIO) {
      for (let x = ESPACIO / 2; x < w + ESPACIO; x += ESPACIO) {
        puntos.push({ x0: x, y0: y });
      }
    }
  }

  function dibujar(t) {
    ctx.clearRect(0, 0, w, h);
    const s = t / 1000;
    for (const p of puntos) {
      // Oleaje suave
      const ola = Math.sin(p.x0 * 0.01 + s * 0.8) + Math.cos(p.y0 * 0.013 - s * 0.6);
      let x = p.x0 + ola * 1.6;
      let y = p.y0 + ola * 1.2;

      // Empuje del cursor
      const dx = x - raton.x;
      const dy = y - raton.y;
      const d2 = dx * dx + dy * dy;
      const radio = 140;
      if (d2 < radio * radio) {
        const d = Math.sqrt(d2) || 1;
        const fuerza = (1 - d / radio) * 18;
        x += (dx / d) * fuerza;
        y += (dy / d) * fuerza;
      }

      const brillo = 0.12 + 0.18 * (0.5 + 0.5 * ola / 2);
      ctx.beginPath();
      ctx.arc(x, y, 1.3, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(216, 226, 220, ${brillo})`;
      ctx.fill();
    }
    requestAnimationFrame(dibujar);
  }

  window.addEventListener('resize', preparar);
  window.addEventListener('pointermove', (e) => {
    raton.x = e.clientX;
    raton.y = e.clientY;
  });
  window.addEventListener('pointerleave', () => {
    raton.x = raton.y = -9999;
  });

  preparar();
  requestAnimationFrame(dibujar);

  // ---- Notas al azar ----
  const notas = [
    {
      texto: 'Hay caminos que no se recorren porque nadie los marcó. Esta página también es uno de esos.',
      fuente: 'Margen de un cuaderno, sin fecha'
    },
    {
      texto: 'Empecé un dibujo de un faro y terminé pintando solo el agua. Me pareció más honesto.',
      fuente: 'Bitácora, otoño'
    },
    {
      texto: 'Preguntar qué hace falta para estar bien es más útil que preguntar qué querés.',
      fuente: 'Anotado en un viaje de tren'
    },
    {
      texto: 'Un libro abierto boca abajo sobre la mesa espera mejor que uno cerrado en un estante.',
      fuente: 'Lecturas, sin terminar'
    },
    {
      texto: 'Si algo no se termina, puede seguir siendo verdadero a medias.',
      fuente: 'Nota suelta'
    }
  ];

  const elNota = document.getElementById('nota');
  const elTexto = document.getElementById('texto-nota');
  const elFuente = document.getElementById('fuente-nota');
  const boton = document.getElementById('otra');
  let ultimo = -1;

  function mostrarNota() {
    let i;
    do { i = Math.floor(Math.random() * notas.length); }
    while (notas.length > 1 && i === ultimo);
    ultimo = i;
    elNota.classList.add('oculta');
    setTimeout(() => {
      elTexto.textContent = notas[i].texto;
      elFuente.textContent = notas[i].fuente;
      elNota.classList.remove('oculta');
    }, 600);
  }

  boton.addEventListener('click', mostrarNota);
  mostrarNota();
})();
</script>

</body>
</html>
```

Qué: Una portada tipo cuaderno de bordo con un fondo de puntos que se mueven como oleaje y reaccionan al cursor, una nota al azar que cambia con un botón y un menú de cuatro enlaces, todo en un solo archivo sin recursos externos.