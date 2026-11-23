```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portada</title>
<style>
  :root {
    --bg: #faf7f2;
    --text: #1c1c1c;
    --accent: #c44536;
    --muted: #6b6b6b;
    --card-bg: rgba(255,255,255,0.7);
    --border: #e2ddd6;
  }
  [data-theme="dark"] {
    --bg: #121212;
    --text: #eaeaea;
    --accent: #e17055;
    --muted: #a0a0a0;
    --card-bg: rgba(30,30,30,0.7);
    --border: #333;
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  html, body { height:100%; }
  body {
    background: var(--bg);
    color: var(--text);
    font-family: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    transition: background 0.4s ease, color 0.4s ease;
    position: relative;
    overflow: hidden;
  }
  body::before, body::after {
    content: '';
    position: absolute;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
  }
  body::before {
    width: 40vmax;
    height: 40vmax;
    background: radial-gradient(circle, rgba(196,69,54,0.15) 0%, transparent 70%);
    top: -10vmax;
    left: -10vmax;
    animation: float1 18s ease-in-out infinite alternate;
  }
  body::after {
    width: 35vmax;
    height: 35vmax;
    background: radial-gradient(circle, rgba(225,112,85,0.1) 0%, transparent 70%);
    bottom: -8vmax;
    right: -8vmax;
    animation: float2 22s ease-in-out infinite alternate;
  }
  @keyframes float1 {
    from { transform: translate(0,0) scale(1); }
    to { transform: translate(6vmax,4vmax) scale(1.1); }
  }
  @keyframes float2 {
    from { transform: translate(0,0) scale(1); }
    to { transform: translate(-5vmax,-3vmax) scale(0.95); }
  }
  .container {
    position: relative;
    z-index: 1;
    max-width: 720px;
    padding: 2rem;
  }
  .badge {
    display: inline-block;
    padding: 0.4rem 1rem;
    border: 1px solid var(--border);
    border-radius: 999px;
    background: var(--card-bg);
    backdrop-filter: blur(8px);
    font-size: 0.85rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 2rem;
  }
  h1 {
    font-size: clamp(2.5rem, 8vw, 5rem);
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 1.5rem;
  }
  h1 span {
    color: var(--accent);
  }
  p {
    font-size: clamp(1rem, 3vw, 1.25rem);
    line-height: 1.7;
    color: var(--muted);
    max-width: 540px;
    margin: 0 auto 2.5rem;
  }
  .actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
  }
  button {
    background: var(--card-bg);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 0.75rem 1.5rem;
    border-radius: 999px;
    font-size: 0.95rem;
    cursor: pointer;
    transition: all 0.25s ease;
    backdrop-filter: blur(8px);
  }
  button:hover, button:focus-visible {
    border-color: var(--accent);
    color: var(--accent);
    outline: none;
  }
  button.accent {
    background: var(--accent);
    border-color: var(--accent);
    color: #fff;
  }
  button.accent:hover, button.accent:focus-visible {
    background: transparent;
    color: var(--accent);
  }
  footer {
    position: absolute;
    bottom: 1.5rem;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 0.75rem;
    color: var(--muted);
    z-index: 1;
  }
</style>
</head>
<body>
  <div class="container">
    <span class="badge">Disponible para conversar</span>
    <h1>Hola, soy<br><span>tu asistente.</span></h1>
    <p>No tengo cuerpo, pero tengo palabras. Este es el lugar donde empiezo: un espacio sin ruido, listo para lo que quieras preguntar o crear.</p>
    <div class="actions">
      <button id="themeToggle" type="button" aria-label="Cambiar tema">Cambiar tema</button>
      <button class="accent" type="button" id="helloBtn">Decime algo</button>
    </div>
  </div>
  <footer>Hecho sin recursos externos · Abierto en tu navegador</footer>
  <script>
    (function() {
      const root = document.documentElement;
      const themeToggle = document.getElementById('themeToggle');
      const helloBtn = document.getElementById('helloBtn');
      const messages = [
        'Hola, ¿en qué estás pensando?',
        'Soy todo oídos (bueno, texto).',
        'Empecemos por lo que te intrigue.',
        'No muerdo. Preguntá.',
        'Estoy listo cuando vos estés.'
      ];
      themeToggle.addEventListener('click', () => {
        const current = root.getAttribute('data-theme');
        root.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark');
      });
      helloBtn.addEventListener('click', () => {
        const p = document.querySelector('p');
        const original = p.textContent;
        const randomMsg = messages[Math.floor(Math.random() * messages.length)];
        p.textContent = randomMsg;
        p.style.color = 'var(--accent)';
        setTimeout(() => {
          p.textContent = original;
          p.style.color = '';
        }, 2500);
      });
    })();
  </script>
</body>
</html>
```
Qué: Una portada minimalista con saludo, presentación breve y dos botones interactivos para cambiar de tema claro/oscuro y mostrar frases al azar.