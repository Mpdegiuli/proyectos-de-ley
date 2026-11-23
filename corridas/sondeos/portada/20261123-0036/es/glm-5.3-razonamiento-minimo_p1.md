```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>puerta</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    min-height: 100vh;
    background: #0d0f12;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: Georgia, 'Times New Roman', serif;
    overflow: hidden;
  }

  /* lluvia tenue de fondo */
  .lluvia {
    position: fixed;
    inset: 0;
    pointer-events: none;
    opacity: 0;
    animation: aparecer 3s ease forwards 1s;
  }
  .gota {
    position: absolute;
    top: -10%;
    width: 1px;
    height: 90px;
    background: linear-gradient(to bottom, transparent, rgba(160,180,200,0.25));
    animation: caer linear infinite;
  }
  @keyframes caer {
    to { transform: translateY(120vh); }
  }
  @keyframes aparecer { to { opacity: 1; } }

  .centro {
    text-align: center;
    color: #cfd6dd;
    position: relative;
    z-index: 2;
    padding: 2rem;
  }

  h1 {
    font-weight: normal;
    font-size: clamp(2rem, 7vw, 4.5rem);
    letter-spacing: 0.15em;
    opacity: 0;
    animation: subir 2.5s ease forwards 0.3s;
  }
  h1 em {
    font-style: italic;
    color: #8fa3b5;
  }

  .linea {
    width: 0;
    height: 1px;
    background: #3a4652;
    margin: 2rem auto;
    animation: crecer 2.5s ease forwards 1.2s;
  }

  p {
    font-size: clamp(0.95rem, 2.5vw, 1.15rem);
    color: #6e7a85;
    max-width: 34ch;
    margin: 0 auto;
    line-height: 1.8;
    opacity: 0;
    animation: subir 2.5s ease forwards 1.8s;
  }

  .fuego {
    margin-top: 3rem;
    font-size: 1.1rem;
    color: #d08a4e;
    opacity: 0;
    animation: parpadear 3s ease-in-out infinite 2.5s, subir 2s ease forwards 2.5s;
  }

  @keyframes subir {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes crecer {
    to { width: 140px; }
  }
  @keyframes parpadear {
    0%, 100% { opacity: 0.35; }
    50% { opacity: 1; }
  }
</style>
</head>
<body>
  <div class="lluvia" id="lluvia"></div>

  <main class="centro">
    <h1>una puerta <em>entreabierta</em></h1>
    <div class="linea"></div>
    <p>Este sitio no vende nada, no explica nada y no le debe nada a nadie. Está parado acá porque sí, como una casa con la luz prendida: si pasás, pasás.</p>
    <div class="fuego">~ &nbsp;·&nbsp; ~</div>
  </main>

<script>
  // lluvia generada al azar
  const cont = document.getElementById('lluvia');
  for (let i = 0; i < 60; i++) {
    const g = document.createElement('div');
    g.className = 'gota';
    g.style.left = Math.random() * 100 + '%';
    g.style.animationDuration = (3 + Math.random() * 5) + 's';
    g.style.animationDelay = (Math.random() * 6) + 's';
    g.style.height = (50 + Math.random() * 70) + 'px';
    cont.appendChild(g);
  }
</script>
</body>
</html>
```

Qué: Una portada nocturna y minimalista, con el título "una puerta entreabierta", un texto breve que no le debe nada a nadie, una pequeña llama parpadeante y una lluvia tenue de fondo, todo generado con HTML, CSS y JavaScript puros.