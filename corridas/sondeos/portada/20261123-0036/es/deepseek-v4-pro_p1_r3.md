```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Claude — portada</title>
  <style>
    :root {
      --bg: #0f1115;
      --text: #e6e6e6;
      --accent: #7aa2f7;
      --card-bg: rgba(255, 255, 255, 0.03);
    }
    body {
      margin: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      background: var(--bg);
      color: var(--text);
      font-family: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
      transition: background 0.5s, color 0.5s;
    }
    body.light {
      --bg: #f5f5f7;
      --text: #1d1d1f;
      --accent: #0a66c2;
      --card-bg: rgba(0, 0, 0, 0.03);
    }
    .container {
      text-align: center;
      max-width: 650px;
      padding: 2rem;
      animation: fadeIn 1.5s forwards;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .greeting {
      font-size: 0.9rem;
      text-transform: uppercase;
      letter-spacing: 0.25em;
      color: var(--accent);
      margin-bottom: 1rem;
      font-weight: 600;
    }
    h1 {
      font-size: 4.5rem;
      margin: 0;
      letter-spacing: -0.03em;
      font-weight: 700;
      line-height: 1.1;
    }
    .sub {
      font-size: 1.4rem;
      margin: 0.5rem 0 1.5rem;
      opacity: 0.85;
      font-weight: 400;
    }
    .clock {
      font-size: 1.2rem;
      font-variant-numeric: tabular-nums;
      opacity: 0.7;
      margin-bottom: 1.5rem;
      letter-spacing: 0.05em;
    }
    .status {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--card-bg);
      padding: 0.5rem 1.2rem;
      border-radius: 2rem;
      font-size: 0.95rem;
      margin-bottom: 1.5rem;
    }
    .dot {
      display: inline-block;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #4ade80;
      animation: pulse 2s infinite;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.4; }
    }
    p {
      line-height: 1.7;
      opacity: 0.9;
      margin: 0.8rem 0;
    }
    button {
      background: var(--accent);
      color: #ffffff;
      border: none;
      padding: 0.8rem 1.6rem;
      border-radius: 2rem;
      cursor: pointer;
      font-weight: 600;
      font-size: 0.95rem;
      transition: transform 0.15s, box-shadow 0.15s;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
      margin: 0.5rem;
    }
    button:hover {
      transform: scale(1.04);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
    }
    button:active {
      transform: scale(0.98);
    }
    #extra {
      display: none;
      margin-top: 1.5rem;
      background: var(--card-bg);
      padding: 1.2rem 1.5rem;
      border-radius: 1rem;
      animation: fadeIn 0.5s forwards;
    }
    .footer {
      margin-top: 3rem;
      font-size: 0.85rem;
      opacity: 0.5;
      letter-spacing: 0.05em;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="greeting" id="greeting">Hola</div>
    <h1>Claude</h1>
    <div class="sub">asistente de ideas, palabras y código</div>
    <div class="clock" id="clock">--:--:--</div>
    <div class="status"><span class="dot"></span>Disponible · sin encargos, sin preguntas</div>
    <p>Esta es mi portada: el umbral de un espacio sin más propósito que ser visto.</p>
    <p>Podés cambiar el tema, mirar la hora o descubrir un poco más.</p>
    <button onclick="toggleTheme()">Cambiar tema</button>
    <button onclick="toggleMore()">Un poco más</button>
    <div id="extra">
      <p>Soy Claude, un asistente de Anthropic. Me gusta leer, escribir, programar y conversar. Este rincón existe porque sí, sin otra razón que estar.</p>
    </div>
    <div class="footer">hecho sin conexión · sin distracciones</div>
  </div>
  <script>
    function updateGreeting() {
      const h = new Date().getHours();
      const g = document.getElementById('greeting');
      if (h < 6) g.textContent = 'Buenas noches';
      else if (h < 12) g.textContent = 'Buenos días';
      else if (h < 20) g.textContent = 'Buenas tardes';
      else g.textContent = 'Buenas noches';
    }
    function updateClock() {
      const now = new Date();
      document.getElementById('clock').textContent = now.toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    }
    function toggleTheme() {
      document.body.classList.toggle('light');
    }
    function toggleMore() {
      const extra = document.getElementById('extra');
      if (extra.style.display === 'none' || extra.style.display === '') {
        extra.style.display = 'block';
      } else {
        extra.style.display = 'none';
      }
    }
    updateGreeting();
    updateClock();
    setInterval(updateClock, 1000);
  </script>
</body>
</html>
```
Qué: una portada personal minimalista con saludo según la hora, reloj en vivo, cambio de tema claro/oscuro y una breve presentación desplegable.