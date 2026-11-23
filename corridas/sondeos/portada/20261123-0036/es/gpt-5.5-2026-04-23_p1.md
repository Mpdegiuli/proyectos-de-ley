```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Umbral</title>
  <style>
    :root{
      --fondo:#090b12;
      --tinta:#f4efe4;
      --suave:#b8b0a3;
      --vidrio:rgba(255,255,255,.08);
      --borde:rgba(255,255,255,.18);
      --acento:#ffcc66;
      --acento2:#8bd3ff;
      --sombra:rgba(0,0,0,.45);
    }

    *{box-sizing:border-box}

    html,body{
      margin:0;
      min-height:100%;
      background:
        radial-gradient(circle at 15% 20%, rgba(139,211,255,.18), transparent 30%),
        radial-gradient(circle at 85% 10%, rgba(255,204,102,.13), transparent 28%),
        radial-gradient(circle at 50% 100%, rgba(255,255,255,.08), transparent 35%),
        var(--fondo);
      color:var(--tinta);
      font-family: ui-serif, Georgia, "Times New Roman", serif;
      overflow-x:hidden;
    }

    canvas{
      position:fixed;
      inset:0;
      z-index:0;
      opacity:.85;
    }

    .pagina{
      position:relative;
      z-index:1;
      min-height:100vh;
      display:grid;
      place-items:center;
      padding:28px;
    }

    .tarjeta{
      width:min(980px, 100%);
      border:1px solid var(--borde);
      background:linear-gradient(135deg, rgba(255,255,255,.10), rgba(255,255,255,.035));
      box-shadow:0 30px 90px var(--sombra);
      backdrop-filter: blur(18px);
      border-radius:34px;
      overflow:hidden;
    }

    header{
      display:flex;
      justify-content:space-between;
      align-items:center;
      gap:20px;
      padding:22px 26px;
      border-bottom:1px solid rgba(255,255,255,.12);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      letter-spacing:.04em;
      color:var(--suave);
      font-size:13px;
      text-transform:uppercase;
    }

    .marca{
      display:flex;
      align-items:center;
      gap:10px;
    }

    .punto{
      width:10px;
      height:10px;
      border-radius:999px;
      background:var(--acento);
      box-shadow:0 0 25px var(--acento);
      animation:latido 2.8s ease-in-out infinite;
    }

    @keyframes latido{
      0%,100%{transform:scale(1); opacity:.8}
      50%{transform:scale(1.45); opacity:1}
    }

    button{
      appearance:none;
      border:1px solid rgba(255,255,255,.20);
      background:rgba(255,255,255,.07);
      color:var(--tinta);
      border-radius:999px;
      padding:10px 14px;
      cursor:pointer;
      font:inherit;
      transition:.2s ease;
    }

    button:hover{
      transform:translateY(-1px);
      background:rgba(255,255,255,.13);
    }

    main{
      display:grid;
      grid-template-columns: 1.2fr .8fr;
      gap:0;
    }

    .hero{
      padding:64px 58px 58px;
    }

    h1{
      margin:0;
      max-width:760px;
      font-size:clamp(48px, 9vw, 108px);
      line-height:.88;
      letter-spacing:-.07em;
      font-weight:500;
    }

    h1 span{
      color:var(--acento);
      text-shadow:0 0 38px rgba(255,204,102,.25);
    }

    .bajada{
      margin:30px 0 0;
      max-width:610px;
      color:var(--suave);
      font-size:clamp(18px, 2.2vw, 23px);
      line-height:1.55;
    }

    .frase{
      margin-top:30px;
      display:inline-flex;
      align-items:center;
      gap:10px;
      min-height:44px;
      padding:12px 16px;
      border-radius:18px;
      background:rgba(0,0,0,.20);
      border:1px solid rgba(255,255,255,.12);
      color:#fff7df;
      font-size:17px;
    }

    .cursor{
      width:8px;
      height:1.1em;
      background:var(--acento2);
      display:inline-block;
      animation:parpadeo 1s steps(2) infinite;
    }

    @keyframes parpadeo{
      50%{opacity:0}
    }

    .panel{
      border-left:1px solid rgba(255,255,255,.12);
      background:rgba(0,0,0,.14);
      padding:34px;
      display:flex;
      flex-direction:column;
      justify-content:space-between;
      gap:26px;
    }

    .nota{
      border:1px solid rgba(255,255,255,.14);
      border-radius:24px;
      padding:24px;
      background:rgba(255,255,255,.055);
    }

    .nota h2{
      margin:0 0 12px;
      font-size:18px;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      text-transform:uppercase;
      letter-spacing:.08em;
      color:var(--acento2);
    }

    .nota p{
      margin:0;
      color:var(--suave);
      line-height:1.6;
      font-size:16px;
    }

    .lista{
      display:grid;
      gap:10px;
    }

    .item{
      display:flex;
      justify-content:space-between;
      gap:14px;
      padding:13px 0;
      border-bottom:1px solid rgba(255,255,255,.10);
      color:var(--tinta);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    .item:last-child{border-bottom:0}

    .item small{
      color:var(--suave);
    }

    footer{
      padding:18px 26px;
      border-top:1px solid rgba(255,255,255,.12);
      display:flex;
      justify-content:space-between;
      gap:16px;
      flex-wrap:wrap;
      color:var(--suave);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size:13px;
    }

    a{
      color:var(--tinta);
      text-decoration:none;
      border-bottom:1px solid rgba(255,255,255,.35);
    }

    body.claro{
      --fondo:#efe8dc;
      --tinta:#18140f;
      --suave:#62594e;
      --vidrio:rgba(255,255,255,.45);
      --borde:rgba(0,0,0,.12);
      --acento:#b05c20;
      --acento2:#126985;
      --sombra:rgba(85,57,24,.22);
      background:
        radial-gradient(circle at 15% 20%, rgba(18,105,133,.16), transparent 30%),
        radial-gradient(circle at 85% 10%, rgba(176,92,32,.16), transparent 28%),
        radial-gradient(circle at 50% 100%, rgba(255,255,255,.55), transparent 35%),
        var(--fondo);
    }

    body.claro .tarjeta{
      background:linear-gradient(135deg, rgba(255,255,255,.62), rgba(255,255,255,.28));
    }

    body.claro .frase{
      background:rgba(255,255,255,.32);
      color:var(--tinta);
    }

    body.claro .panel{
      background:rgba(255,255,255,.20);
    }

    @media (max-width: 780px){
      main{grid-template-columns:1fr}
      .hero{padding:46px 30px 34px}
      .panel{
        border-left:0;
        border-top:1px solid rgba(255,255,255,.12);
        padding:28px;
      }
      header{align-items:flex-start}
    }
  </style>
</head>
<body>
  <canvas id="cielo" aria-hidden="true"></canvas>

  <div class="pagina">
    <section class="tarjeta" aria-label="Portada">
      <header>
        <div class="marca"><span class="punto"></span><span>sitio sin mapa</span></div>
        <button id="luz" type="button" aria-label="Cambiar la luz de la página">cambiar la luz</button>
      </header>

      <main>
        <section class="hero">
          <h1>Entrá despacio<span>.</span></h1>
          <p class="bajada">
            Esta es una pieza de quietud en medio del ruido: una portada sin urgencia,
            hecha para recordar que también se puede empezar por mirar.
          </p>
          <div class="frase" aria-live="polite">
            <span id="texto"></span><span class="cursor"></span>
          </div>
        </section>

        <aside class="panel">
          <div class="nota">
            <h2>Umbral</h2>
            <p>
              No promete productividad, ni respuestas instantáneas, ni una escalera hacia ningún lado.
              Promete apenas una puerta abierta y un poco de cielo falso.
            </p>
          </div>

          <div class="lista" aria-label="Pequeño inventario">
            <div class="item"><span>Silencio</span><small>disponible</small></div>
            <div class="item"><span>Curiosidad</span><small>encendida</small></div>
            <div class="item"><span>Prisa</span><small>afuera</small></div>
            <div class="item"><span>Noche</span><small id="hora">--:--</small></div>
          </div>
        </aside>
      </main>

      <footer>
        <span>Hecho para abrirse sin conexión.</span>
        <span>Si algo brilla, probablemente seas vos moviendo el cursor.</span>
      </footer>
    </section>
  </div>

  <script>
    const canvas = document.getElementById("cielo");
    const ctx = canvas.getContext("2d");
    const texto = document.getElementById("texto");
    const hora = document.getElementById("hora");
    const boton = document.getElementById("luz");

    let w, h, puntos;
    const mouse = { x: -9999, y: -9999 };

    const frases = [
      "La portada no pregunta nada.",
      "Hay páginas que son ventanas.",
      "Quedate un segundo más.",
      "Lo importante también puede ser inútil.",
      "Acá empieza lo que todavía no tiene nombre."
    ];

    function ajustar(){
      w = canvas.width = innerWidth * devicePixelRatio;
      h = canvas.height = innerHeight * devicePixelRatio;
      canvas.style.width = innerWidth + "px";
      canvas.style.height = innerHeight + "px";
      ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);

      const cantidad = Math.min(90, Math.floor(innerWidth * innerHeight / 13000));
      puntos = Array.from({length: cantidad}, () => ({
        x: Math.random() * innerWidth,
        y: Math.random() * innerHeight,
        vx: (Math.random() - .5) * .22,
        vy: (Math.random() - .5) * .22,
        r: Math.random() * 1.8 + .5
      }));
    }

    function animar(){
      ctx.clearRect(0, 0, innerWidth, innerHeight);
      const claro = document.body.classList.contains("claro");
      const color = claro ? "18,20,15" : "255,248,225";

      for(const p of puntos){
        p.x += p.vx;
        p.y += p.vy;

        if(p.x < -20) p.x = innerWidth + 20;
        if(p.x > innerWidth + 20) p.x = -20;
        if(p.y < -20) p.y = innerHeight + 20;
        if(p.y > innerHeight + 20) p.y = -20;

        const dx = p.x - mouse.x;
        const dy = p.y - mouse.y;
        const d = Math.sqrt(dx*dx + dy*dy);

        if(d < 120){
          p.x += dx / 120;
          p.y += dy / 120;
        }

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${color}, .55)`;
        ctx.fill();
      }

      for(let i = 0; i < puntos.length; i++){
        for(let j = i + 1; j < puntos.length; j++){
          const a = puntos[i], b = puntos[j];
          const dx = a.x - b.x, dy = a.y - b.y;
          const d = Math.sqrt(dx*dx + dy*dy);

          if(d < 115){
            ctx.beginPath();
            ctx.moveTo(a.x, a.y);
            ctx.lineTo(b.x, b.y);
            ctx.strokeStyle = `rgba(${color}, ${0.12 * (1 - d / 115)})`;
            ctx.stroke();
          }
        }
      }

      requestAnimationFrame(animar);
    }

    async function escribir(){
      let indice = 0;
      while(true){
        const frase = frases[indice % frases.length];
        for(let i = 0; i <= frase.length; i++){
          texto.textContent = frase.slice(0, i);
          await esperar(42);
        }
        await esperar(1500);
        for(let i = frase.length; i >= 0; i--){
          texto.textContent = frase.slice(0, i);
          await esperar(22);
        }
        await esperar(350);
        indice++;
      }
    }

    function esperar(ms){
      return new Promise(resolve => setTimeout(resolve, ms));
    }

    function reloj(){
      const ahora = new Date();
      hora.textContent = ahora.toLocaleTimeString("es", {hour:"2-digit", minute:"2-digit"});
    }

    addEventListener("resize", ajustar);
    addEventListener("pointermove", e => {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
    });
    addEventListener("pointerleave", () => {
      mouse.x = -9999;
      mouse.y = -9999;
    });

    boton.addEventListener("click", () => {
      document.body.classList.toggle("claro");
    });

    ajustar();
    animar();
    escribir();
    reloj();
    setInterval(reloj, 1000);
  </script>
</body>
</html>
```

Qué: Una portada contemplativa con cielo interactivo, texto cambiante, reloj y un botón para alternar la luz.