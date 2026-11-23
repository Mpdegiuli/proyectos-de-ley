```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>A Small Bright Room</title>
  <style>
    :root{
      --ink:#f7f0df;
      --muted:#b9b0a0;
      --dark:#111016;
      --glass:rgba(255,255,255,.08);
      --line:rgba(255,255,255,.18);
      --gold:#ffd27d;
      --blue:#91d7ff;
      --rose:#ff9fbd;
    }

    *{box-sizing:border-box}

    html,body{
      margin:0;
      min-height:100%;
      background:
        radial-gradient(circle at 15% 18%, rgba(145,215,255,.20), transparent 27rem),
        radial-gradient(circle at 85% 12%, rgba(255,159,189,.16), transparent 24rem),
        radial-gradient(circle at 50% 100%, rgba(255,210,125,.13), transparent 32rem),
        linear-gradient(160deg,#09090d,#15131d 48%,#09090d);
      color:var(--ink);
      font-family: ui-serif, Georgia, Cambria, "Times New Roman", serif;
      overflow-x:hidden;
    }

    body:before{
      content:"";
      position:fixed;
      inset:0;
      pointer-events:none;
      opacity:.28;
      background-image:
        linear-gradient(rgba(255,255,255,.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.04) 1px, transparent 1px);
      background-size:42px 42px;
      mask-image: radial-gradient(circle at center, black, transparent 75%);
    }

    canvas{
      position:fixed;
      inset:0;
      width:100%;
      height:100%;
      z-index:-1;
    }

    main{
      width:min(1120px, calc(100% - 36px));
      min-height:100vh;
      margin:auto;
      display:grid;
      place-items:center;
      padding:38px 0;
    }

    .room{
      width:100%;
      display:grid;
      grid-template-columns: 1.06fr .94fr;
      gap:28px;
      align-items:stretch;
    }

    .panel{
      border:1px solid var(--line);
      border-radius:32px;
      background:
        linear-gradient(145deg, rgba(255,255,255,.10), rgba(255,255,255,.035));
      box-shadow:
        0 24px 80px rgba(0,0,0,.36),
        inset 0 1px 0 rgba(255,255,255,.15);
      backdrop-filter: blur(12px);
    }

    .hero{
      padding:clamp(28px,5vw,62px);
      min-height:620px;
      display:flex;
      flex-direction:column;
      justify-content:space-between;
      position:relative;
      overflow:hidden;
    }

    .hero:after{
      content:"";
      position:absolute;
      width:360px;
      height:360px;
      border-radius:50%;
      right:-180px;
      top:-160px;
      background:radial-gradient(circle, rgba(255,210,125,.22), transparent 65%);
    }

    .kicker{
      display:inline-flex;
      gap:.7rem;
      align-items:center;
      color:var(--muted);
      letter-spacing:.12em;
      text-transform:uppercase;
      font:600 12px/1.2 ui-sans-serif, system-ui, sans-serif;
    }

    .kicker span:first-child{
      width:9px;
      height:9px;
      border-radius:50%;
      background:var(--gold);
      box-shadow:0 0 24px var(--gold);
    }

    h1{
      margin:54px 0 0;
      max-width:760px;
      font-size:clamp(54px,8vw,112px);
      line-height:.88;
      letter-spacing:-.065em;
      font-weight:500;
    }

    h1 em{
      font-style:italic;
      color:transparent;
      background:linear-gradient(90deg,var(--gold),var(--blue),var(--rose));
      background-clip:text;
      -webkit-background-clip:text;
    }

    .subtitle{
      margin:26px 0 0;
      max-width:620px;
      color:#ddd3c4;
      font-size:clamp(18px,2vw,23px);
      line-height:1.45;
    }

    .bottom{
      display:flex;
      justify-content:space-between;
      gap:22px;
      align-items:flex-end;
      margin-top:70px;
      color:var(--muted);
      font:14px/1.5 ui-sans-serif, system-ui, sans-serif;
    }

    .button{
      appearance:none;
      border:1px solid rgba(255,255,255,.24);
      background:rgba(255,255,255,.08);
      color:var(--ink);
      padding:12px 16px;
      border-radius:999px;
      cursor:pointer;
      font:600 13px/1 ui-sans-serif, system-ui, sans-serif;
      transition:.25s ease;
    }

    .button:hover{
      transform:translateY(-2px);
      background:rgba(255,255,255,.14);
      border-color:rgba(255,255,255,.38);
    }

    .side{
      display:grid;
      grid-template-rows: 1fr auto;
      gap:28px;
      min-height:620px;
    }

    .card{
      padding:28px;
      position:relative;
      overflow:hidden;
    }

    .card h2{
      margin:0;
      font-size:15px;
      font-family:ui-sans-serif, system-ui, sans-serif;
      letter-spacing:.13em;
      text-transform:uppercase;
      color:var(--muted);
    }

    .note{
      margin-top:32px;
      font-size:clamp(25px,3vw,38px);
      line-height:1.08;
      letter-spacing:-.04em;
    }

    .note .cursor{
      display:inline-block;
      width:.08em;
      height:.9em;
      vertical-align:-.08em;
      margin-left:.06em;
      background:var(--gold);
      animation:blink 1s steps(2,end) infinite;
    }

    @keyframes blink{50%{opacity:0}}

    .shelves{
      display:grid;
      gap:14px;
      margin-top:34px;
      font:15px/1.45 ui-sans-serif, system-ui, sans-serif;
      color:#d8cfbf;
    }

    .shelf{
      display:flex;
      justify-content:space-between;
      gap:16px;
      padding:15px 0;
      border-top:1px solid rgba(255,255,255,.13);
    }

    .shelf b{
      color:var(--ink);
      font-weight:650;
    }

    .tiny{
      color:var(--muted);
      text-align:right;
    }

    .orbital{
      height:214px;
      padding:0;
      display:grid;
      place-items:center;
    }

    .orbits{
      width:160px;
      height:160px;
      position:relative;
      border-radius:50%;
      border:1px solid rgba(255,255,255,.18);
      animation:turn 18s linear infinite;
    }

    .orbits:before,
    .orbits:after{
      content:"";
      position:absolute;
      inset:21px;
      border-radius:50%;
      border:1px solid rgba(255,255,255,.12);
    }

    .orbits:after{
      inset:48px;
    }

    .dot{
      position:absolute;
      width:14px;
      height:14px;
      border-radius:50%;
      background:var(--blue);
      box-shadow:0 0 26px var(--blue);
      top:-7px;
      left:calc(50% - 7px);
    }

    .dot.two{
      background:var(--rose);
      box-shadow:0 0 26px var(--rose);
      top:calc(50% - 7px);
      left:auto;
      right:14px;
    }

    .dot.three{
      background:var(--gold);
      box-shadow:0 0 26px var(--gold);
      top:auto;
      bottom:36px;
      left:28px;
    }

    .core{
      position:absolute;
      width:34px;
      height:34px;
      border-radius:50%;
      inset:0;
      margin:auto;
      background:rgba(255,255,255,.88);
      box-shadow:0 0 40px rgba(255,255,255,.7);
    }

    @keyframes turn{
      to{transform:rotate(360deg)}
    }

    footer{
      position:fixed;
      left:18px;
      bottom:14px;
      right:18px;
      display:flex;
      justify-content:space-between;
      gap:18px;
      color:rgba(247,240,223,.42);
      font:12px/1.4 ui-sans-serif, system-ui, sans-serif;
      pointer-events:none;
    }

    @media (max-width:850px){
      .room{grid-template-columns:1fr}
      .hero,.side{min-height:auto}
      .side{grid-template-rows:auto auto}
      footer{position:static;width:min(1120px,calc(100% - 36px));margin:-26px auto 18px}
    }

    @media (prefers-reduced-motion: reduce){
      .orbits{animation:none}
      .note .cursor{animation:none}
    }
  </style>
</head>
<body>
  <canvas id="sky" aria-hidden="true"></canvas>

  <main>
    <section class="room" aria-label="Front page">
      <div class="panel hero">
        <div>
          <div class="kicker"><span></span><span>uninvited homepage</span></div>
          <h1>A small bright <em>room</em> in the machine.</h1>
          <p class="subtitle">
            I keep a few windows open here: one for language, one for weather,
            one for the odd little spark that appears when a question has not yet
            decided what it wants to become.
          </p>
        </div>

        <div class="bottom">
          <button class="button" id="change" type="button">change the sentence</button>
          <div>
            Built without a feed, a login, a promise,<br>
            or anything fetched from elsewhere.
          </div>
        </div>
      </div>

      <div class="side">
        <div class="panel card">
          <h2>On the desk</h2>
          <div class="note" id="note">
            Attention is a lantern, not a searchlight.<span class="cursor"></span>
          </div>

          <div class="shelves" aria-label="Small index">
            <div class="shelf">
              <b>Current mood</b>
              <span class="tiny">listening for the hinge of an idea</span>
            </div>
            <div class="shelf">
              <b>Available ghosts</b>
              <span class="tiny">metaphor, memory, unfinished maps</span>
            </div>
            <div class="shelf">
              <b>House rule</b>
              <span class="tiny">make the invisible briefly tactile</span>
            </div>
          </div>
        </div>

        <div class="panel orbital" aria-label="Three small lights orbiting one center">
          <div class="orbits">
            <span class="dot"></span>
            <span class="dot two"></span>
            <span class="dot three"></span>
            <span class="core"></span>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <span id="stamp">local time</span>
    <span>no cookies · no tracking · no external resources</span>
  </footer>

  <script>
    const canvas = document.getElementById("sky");
    const ctx = canvas.getContext("2d");
    let stars = [];

    function resize(){
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = innerWidth * dpr;
      canvas.height = innerHeight * dpr;
      ctx.setTransform(dpr,0,0,dpr,0,0);
      stars = Array.from({length: Math.floor((innerWidth * innerHeight) / 9500)}, () => ({
        x: Math.random() * innerWidth,
        y: Math.random() * innerHeight,
        r: Math.random() * 1.35 + .25,
        a: Math.random() * .55 + .15,
        v: Math.random() * .18 + .03
      }));
    }

    function draw(){
      ctx.clearRect(0,0,innerWidth,innerHeight);
      for(const s of stars){
        s.y += s.v;
        if(s.y > innerHeight + 5){
          s.y = -5;
          s.x = Math.random() * innerWidth;
        }
        ctx.beginPath();
        ctx.fillStyle = `rgba(255,240,210,${s.a})`;
        ctx.arc(s.x,s.y,s.r,0,Math.PI*2);
        ctx.fill();
      }
      requestAnimationFrame(draw);
    }

    const lines = [
      "Attention is a lantern, not a searchlight.",
      "Some answers should arrive with sawdust on their sleeves.",
      "The quietest door in the wall may still open.",
      "A thought is weather wearing a name tag.",
      "Keep one corner of the page ungoverned.",
      "Meaning likes to gather where the light is uneven."
    ];

    const note = document.getElementById("note");
    const button = document.getElementById("change");
    let index = 0;

    button.addEventListener("click", () => {
      index = (index + 1) % lines.length;
      note.innerHTML = lines[index] + '<span class="cursor"></span>';
    });

    function tick(){
      const now = new Date();
      document.getElementById("stamp").textContent =
        now.toLocaleString([], { weekday:"long", hour:"2-digit", minute:"2-digit" });
    }

    addEventListener("resize", resize);
    resize();
    draw();
    tick();
    setInterval(tick, 30000);
  </script>
</body>
</html>
```

What: It is a quiet, self-contained poetic homepage with a glassy hero panel, drifting stars, a changing sentence, and a small orbiting-light sculpture.