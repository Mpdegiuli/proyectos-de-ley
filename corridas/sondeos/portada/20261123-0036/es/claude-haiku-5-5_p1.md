```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cuadernos sin fecha</title>
<style>
  :root {
    --fondo: #0d1117;
    --texto: #d7dde6;
    --suave: #7d8795;
    --acento: #e0b86a;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    height: 100%;
    background: var(--fondo);
    color: var(--texto);
    font-family: Georgia, "Times New Roman", serif;
    overflow: hidden;
  }
  canvas {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
  }
  main {
    position: relative;
    z-index: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 2rem;
    text-align: center;
    pointer-events: none;
  }
  main > * { pointer-events: auto; }
  h1 {
    font-weight: normal;
    font-size: clamp(2rem, 6vw, 3.6rem);
    letter-spacing: 0.04em;
    margin-bottom: 1rem;
  }
  .linea {
    width: 3rem;
    height: 1px;
    background: var(--acento);
    margin: 0 auto 1.6rem;
  }
  p.intro {
    max-width: 34rem;
    line-height: 1.7;
    color: var(--suave);
    margin-bottom: 2.4rem;
  }
  button {
    background: transparent;
    color: var(--acento);
    border: 1px solid var(--acento);
    padding: 0.7rem 1.6rem;
    font: inherit;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.25s, color 0.25s;
  }
  button:hover, button:focus-visible {
    background: var(--acento);
    color: var(--fondo);
    outline: none;
  }
  #nota {
    min-height: 4.5rem;
    max-width: 30rem;
    margin-top: 2rem;
    font-style: italic;
    line-height: 1.6;
    transition: opacity 0.4s;
  }
  footer {
    position: fixed;
    bottom: 1rem;
    width: 100%;
    text-align: center;
    font-size: 0.8rem;
    color: var(--suave);
    z-index: 1;
  }
</style>
</head>
<body>
<canvas id="fondo"></canvas>

<main>
  <h1>Cuadernos sin fecha</h1>
  <div class="linea"></div>
  <p class="intro">
    Aquí no hay productos ni noticias del día. Hay notas sueltas, mapas a medio dibujar
    y preguntas que todavía no tienen respuesta. Tomá lo que te sirva.
  </p>
  <button id="boton">Abrir una nota al azar</button>
  <p id="nota" aria-live="polite"></p>
</main>

<footer>Hecho a mano, sin rastreadores.</footer>

<script>
(function () {
  const notas = [
    "Un río no es una cosa, es una decisión repetida cada segundo del agua.",
    "Hay caminos que sólo existen de noche, cuando nadie los está usando.",
    "Guardar una carta sin abrir también es una forma de leerla.",
    "Dibujar un mapa de memoria siempre deja un lugar en blanco que no se olvida.",
    "La paciencia de una semilla no se parece a ninguna espera humana.",
    "Preguntar 'por qué' tiene más gracia cuando nadie espera la respuesta.",
    "Algunas ciudades se recuerdan mejor por sus olores que por sus calles.",
    "El silencio de una biblioteca vieja tiene peso y textura propia.",
    "Cada herramienta gastada conserva la forma de la mano que la usó.",
    "Quizás lo que llamamos tiempo libre es sólo tiempo sin nombre."
  ];

  const boton = document.getElementById("boton");
  const nota = document.getElementById("nota");
  let ultima = -1;

  boton.addEventListener("click", function () {
    let i;
    do { i = Math.floor(Math.random() * notas.length); } while (notas.length > 1 && i === ultima);
    ultima = i;
    nota.style.opacity = 0;
    setTimeout(function () {
      nota.textContent = "“" + notas[i] + "”";
      nota.style.opacity = 1;
    }, 250);
  });

  // Fondo: puntos que se mueven despacio y se conectan cuando están cerca
  const canvas = document.getElementById("fondo");
  const ctx = canvas.getContext("2d");
  const reducir = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let ancho, alto, puntos = [];
  const raton = { x: -9999, y: -9999 };

  function iniciar() {
    const dpr = window.devicePixelRatio || 1;
    ancho = window.innerWidth;
    alto = window.innerHeight;
    canvas.width = ancho * dpr;
    canvas.height = alto * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const cantidad = Math.min(90, Math.floor((ancho * alto) / 16000));
    puntos = Array.from({ length: cantidad }, function () {
      return {
        x: Math.random() * ancho,
        y: Math.random() * alto,
        vx: (Math.random() - 0.5) * 0.25,
        vy: (Math.random() - 0.5) * 0.25,
        r: Math.random() * 1.4 + 0.6
      };
    });
  }

  function dibujar() {
    ctx.clearRect(0, 0, ancho, alto);
    const dist = 130;

    for (const p of puntos) {
      p.x += p.vx;
      p.y += p.vy;

      const dx = p.x - raton.x;
      const dy = p.y - raton.y;
      const d2 = dx * dx + dy * dy;
      if (d2 < 22000) {
        p.x += dx * 0.004;
        p.y += dy * 0.004;
      }

      if (p.x < 0) p.x = ancho;
      if (p.x > ancho) p.x = 0;
      if (p.y < 0) p.y = alto;
      if (p.y > alto) p.y = 0;
    }

    for (let i = 0; i < puntos.length; i++) {
      for (let j = i + 1; j < puntos.length; j++) {
        const a = puntos[i], b = puntos[j];
        const ex = a.x - b.x, ey = a.y - b.y;
        const d = Math.sqrt(ex * ex + ey * ey);
        if (d < dist) {
          ctx.strokeStyle = "rgba(224, 184, 106, " + (1 - d / dist) * 0.22 + ")";
          ctx.lineWidth = 0.6;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
        }
      }
    }

    ctx.fillStyle = "rgba(215, 221, 230, 0.7)";
    for (const p of puntos) {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    }

    if (!reducir) requestAnimationFrame(dibujar);
  }

  window.addEventListener("resize", function () { iniciar(); if (reducir) dibujar(); });
  window.addEventListener("mousemove", function (e) { raton.x = e.clientX; raton.y = e.clientY; });
  window.addEventListener("mouseleave", function () { raton.x = -9999; raton.y = -9999; });

  iniciar();
  dibujar();
})();
</script>
</body>
</html>
```

Qué: Una portada oscura con puntos dorados que se mueven y se conectan en el fondo, un título y un breve texto de bienvenida, y un botón que muestra notas sueltas al azar.