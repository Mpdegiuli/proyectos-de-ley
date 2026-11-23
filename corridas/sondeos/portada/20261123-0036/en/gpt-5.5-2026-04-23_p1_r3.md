```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>A Room for Unfinished Things</title>
  <style>
    :root{
      --ink:#eaf2ff;
      --muted:#9fb0c8;
      --dim:#5d6c84;
      --paper:#08111f;
      --paper2:#101b2c;
      --gold:#ffd37a;
      --blue:#86d7ff;
      --rose:#ff9dbb;
      --green:#a7f3c4;
      --shadow:rgba(0,0,0,.45);
    }

    *{box-sizing:border-box}

    html,body{
      margin:0;
      min-height:100%;
      background:
        radial-gradient(circle at 20% 10%, rgba(134,215,255,.16), transparent 28rem),
        radial-gradient(circle at 80% 20%, rgba(255,157,187,.12), transparent 26rem),
        radial-gradient(circle at 50% 100%, rgba(255,211,122,.10), transparent 35rem),
        linear-gradient(160deg, #050912, var(--paper) 48%, #05070d);
      color:var(--ink);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    body{
      overflow-x:hidden;
    }

    canvas{
      position:fixed;
      inset:0;
      width:100%;
      height:100%;
      z-index:0;
      opacity:.8;
      pointer-events:none;
    }

    .grain{
      position:fixed;
      inset:0;
      pointer-events:none;
      z-index:1;
      opacity:.13;
      background-image:
        linear-gradient(transparent, rgba(255,255,255,.04)),
        repeating-radial-gradient(circle at 17% 32%, rgba(255,255,255,.9) 0 1px, transparent 1px 4px);
      mix-blend-mode:screen;
    }

    main{
      position:relative;
      z-index:2;
      width:min(1120px, calc(100% - 32px));
      margin:0 auto;
      padding:32px 0 56px;
    }

    nav{
      display:flex;
      justify-content:space-between;
      align-items:center;
      gap:24px;
      color:var(--muted);
      font-size:14px;
      letter-spacing:.04em;
    }

    .mark{
      display:flex;
      align-items:center;
      gap:10px;
      color:var(--ink);
      text-decoration:none;
      font-weight:700;
    }

    .glyph{
      width:34px;
      height:34px;
      display:grid;
      place-items:center;
      border:1px solid rgba(255,255,255,.18);
      border-radius:11px;
      background:linear-gradient(135deg, rgba(255,255,255,.12), rgba(255,255,255,.03));
      box-shadow:0 12px 40px var(--shadow), inset 0 0 18px rgba(134,215,255,.08);
    }

    .nav-note{
      text-align:right;
    }

    .hero{
      min-height:72vh;
      display:grid;
      align-items:center;
      padding:72px 0 40px;
    }

    .hero-grid{
      display:grid;
      grid-template-columns:1.1fr .9fr;
      gap:44px;
      align-items:center;
    }

    .kicker{
      display:inline-flex;
      gap:9px;
      align-items:center;
      padding:8px 12px;
      color:var(--blue);
      background:rgba(134,215,255,.08);
      border:1px solid rgba(134,215,255,.18);
      border-radius:999px;
      font-size:13px;
      letter-spacing:.08em;
      text-transform:uppercase;
    }

    .pulse{
      width:8px;
      height:8px;
      border-radius:50%;
      background:var(--green);
      box-shadow:0 0 0 0 rgba(167,243,196,.75);
      animation:pulse 2.2s infinite;
    }

    @keyframes pulse{
      70%{box-shadow:0 0 0 12px rgba(167,243,196,0)}
      100%{box-shadow:0 0 0 0 rgba(167,243,196,0)}
    }

    h1{
      margin:22px 0 18px;
      font-size:clamp(48px, 8vw, 112px);
      line-height:.9;
      letter-spacing:-.08em;
      max-width:850px;
    }

    h1 span{
      color:transparent;
      background:linear-gradient(90deg, var(--ink), var(--blue), var(--gold), var(--rose));
      -webkit-background-clip:text;
      background-clip:text;
    }

    .lead{
      max-width:690px;
      color:var(--muted);
      font-size:clamp(18px, 2vw, 23px);
      line-height:1.55;
      margin:0;
    }

    .actions{
      display:flex;
      flex-wrap:wrap;
      gap:14px;
      margin-top:32px;
    }

    button, .button{
      appearance:none;
      border:0;
      cursor:pointer;
      border-radius:16px;
      padding:14px 18px;
      font:inherit;
      color:#07101d;
      background:var(--gold);
      box-shadow:0 14px 40px rgba(255,211,122,.16);
      transition:transform .18s ease, filter .18s ease;
    }

    button:hover, .button:hover{transform:translateY(-2px); filter:brightness(1.06)}
    button:active, .button:active{transform:translateY(0)}

    .secondary{
      color:var(--ink);
      background:rgba(255,255,255,.08);
      border:1px solid rgba(255,255,255,.15);
      box-shadow:none;
      text-decoration:none;
      display:inline-flex;
      align-items:center;
    }

    .orbital{
      position:relative;
      min-height:460px;
      display:grid;
      place-items:center;
    }

    .ring{
      position:absolute;
      width:min(88vw, 430px);
      aspect-ratio:1;
      border:1px solid rgba(255,255,255,.13);
      border-radius:50%;
      animation:turn 34s linear infinite;
    }

    .ring:nth-child(2){
      width:min(72vw, 340px);
      animation-duration:22s;
      animation-direction:reverse;
      border-color:rgba(134,215,255,.18);
    }

    .ring:nth-child(3){
      width:min(52vw, 246px);
      animation-duration:16s;
      border-color:rgba(255,211,122,.19);
    }

    @keyframes turn{to{transform:rotate(360deg)}}

    .planet{
      width:min(68vw, 300px);
      aspect-ratio:1;
      border-radius:46% 54% 52% 48% / 48% 43% 57% 52%;
      background:
        radial-gradient(circle at 35% 25%, rgba(255,255,255,.88), transparent 0 5px, rgba(255,255,255,.18) 6px, transparent 8px),
        radial-gradient(circle at 70% 68%, rgba(255,211,122,.78), transparent 0 6px, rgba(255,211,122,.15) 7px, transparent 12px),
        radial-gradient(circle at 35% 35%, rgba(134,215,255,.52), transparent 27%),
        radial-gradient(circle at 72% 32%, rgba(255,157,187,.28), transparent 30%),
        linear-gradient(135deg, rgba(255,255,255,.14), rgba(255,255,255,.03));
      border:1px solid rgba(255,255,255,.18);
      box-shadow:
        inset -34px -42px 70px rgba(0,0,0,.33),
        inset 24px 22px 50px rgba(255,255,255,.06),
        0 35px 90px rgba(0,0,0,.48),
        0 0 80px rgba(134,215,255,.13);
      animation:morph 12s ease-in-out infinite;
    }

    @keyframes morph{
      0%,100%{border-radius:46% 54% 52% 48% / 48% 43% 57% 52%; transform:translateY(0)}
      50%{border-radius:54% 46% 43% 57% / 54% 57% 43% 46%; transform:translateY(-12px)}
    }

    .moon{
      position:absolute;
      width:14px;
      height:14px;
      border-radius:50%;
      background:var(--ink);
      top:50%;
      left:-7px;
      box-shadow:0 0 22px rgba(255,255,255,.7);
    }

    .ring:nth-child(2) .moon{background:var(--rose); width:10px; height:10px; left:auto; right:-5px}
    .ring:nth-child(3) .moon{background:var(--blue); top:-7px; left:50%}

    .cards{
      display:grid;
      grid-template-columns:repeat(3, 1fr);
      gap:18px;
      margin-top:16px;
    }

    .card{
      min-height:210px;
      padding:24px;
      border-radius:26px;
      background:linear-gradient(180deg, rgba(255,255,255,.095), rgba(255,255,255,.045));
      border:1px solid rgba(255,255,255,.13);
      box-shadow:0 24px 70px rgba(0,0,0,.25);
      backdrop-filter: blur(10px);
    }

    .card b{
      display:block;
      font-size:18px;
      margin-bottom:12px;
    }

    .card p{
      color:var(--muted);
      line-height:1.55;
      margin:0;
    }

    .card .symbol{
      width:42px;
      height:42px;
      border-radius:15px;
      display:grid;
      place-items:center;
      margin-bottom:22px;
      background:rgba(255,255,255,.08);
      border:1px solid rgba(255,255,255,.13);
    }

    .panel{
      margin-top:18px;
      display:grid;
      grid-template-columns:.9fr 1.1fr;
      gap:18px;
      align-items:stretch;
    }

    .note, .question{
      border-radius:28px;
      border:1px solid rgba(255,255,255,.13);
      background:rgba(255,255,255,.06);
      padding:26px;
      box-shadow:0 24px 70px rgba(0,0,0,.22);
    }

    .note{
      color:var(--muted);
      line-height:1.7;
    }

    .note strong{
      color:var(--ink);
      font-weight:650;
    }

    label{
      display:block;
      color:var(--ink);
      font-weight:700;
      margin-bottom:12px;
    }

    textarea{
      width:100%;
      min-height:140px;
      resize:vertical;
      border-radius:20px;
      border:1px solid rgba(255,255,255,.14);
      background:rgba(0,0,0,.18);
      color:var(--ink);
      padding:16px;
      font:inherit;
      line-height:1.5;
      outline:none;
    }

    textarea:focus{
      border-color:rgba(134,215,255,.55);
      box-shadow:0 0 0 4px rgba(134,215,255,.08);
    }

    .reply{
      margin-top:14px;
      color:var(--green);
      min-height:24px;
    }

    footer{
      display:flex;
      justify-content:space-between;
      gap:20px;
      flex-wrap:wrap;
      padding-top:34px;
      color:var(--dim);
      font-size:14px;
    }

    .tiny-link{
      color:var(--muted);
      text-decoration:none;
      border-bottom:1px solid rgba(255,255,255,.16);
    }

    @media (max-width:850px){
      .hero-grid, .panel{
        grid-template-columns:1fr;
      }

      .orbital{
        min-height:330px;
        order:-1;
      }

      .cards{
        grid-template-columns:1fr;
      }

      .nav-note{
        display:none;
      }
    }

    @media (prefers-reduced-motion: reduce){
      *, *::before, *::after{
        animation:none !important;
        scroll-behavior:auto !important;
      }
    }
  </style>
</head>
<body>
  <canvas id="sky" aria-hidden="true"></canvas>
  <div class="grain" aria-hidden="true"></div>

  <main>
    <nav aria-label="Home">
      <a class="mark" href="#">
        <span class="glyph">◇</span>
        <span>A Room for Unfinished Things</span>
      </a>
      <div class="nav-note">offline · quiet · open</div>
    </nav>

    <section class="hero" aria-labelledby="title">
      <div class="hero-grid">
        <div>
          <div class="kicker"><span class="pulse"></span> Welcome to the threshold</div>
          <h1 id="title">Bring me the <span>almost.</span></h1>
          <p class="lead">
            This is a small front room for half-made thoughts, gentle experiments,
            and questions that have not yet learned how to stand up straight.
          </p>
          <div class="actions">
            <button id="wander" type="button">Give me a line</button>
            <a class="button secondary" href="#question">Leave a question</a>
          </div>
        </div>

        <div class="orbital" aria-hidden="true">
          <div class="ring"><span class="moon"></span></div>
          <div class="ring"><span class="moon"></span></div>
          <div class="ring"><span class="moon"></span></div>
          <div class="planet"></div>
        </div>
      </div>
    </section>

    <section class="cards" aria-label="Three invitations">
      <article class="card">
        <div class="symbol">✦</div>
        <b>Notice what glows.</b>
        <p>Not every useful thing arrives loudly. Some ideas are lamp-light on the floor, asking only to be seen.</p>
      </article>
      <article class="card">
        <div class="symbol">≈</div>
        <b>Keep the draft alive.</b>
        <p>A beginning is allowed to wobble. A sketch is allowed to contradict itself. Motion matters.</p>
      </article>
      <article class="card">
        <div class="symbol">?</div>
        <b>Ask better, not bigger.</b>
        <p>The most interesting doors often open from a small, exact question held patiently.</p>
      </article>
    </section>

    <section class="panel" id="question" aria-label="A place to leave a question">
      <div class="note">
        <strong>House rule:</strong> nothing here needs to be finished before it is welcome.
        Bring a sentence fragment, a plan, a doubt, a map with missing roads, or a feeling
        looking for its proper name.
      </div>

      <div class="question">
        <label for="field">Leave a question for the room</label>
        <textarea id="field" placeholder="What are you circling lately?"></textarea>
        <div class="actions">
          <button id="answer" type="button">Let the room answer</button>
          <button id="clear" class="secondary" type="button">Clear</button>
        </div>
        <div class="reply" id="reply" aria-live="polite"></div>
      </div>
    </section>

    <footer>
      <span>Made for an offline browser window.</span>
      <span><a class="tiny-link" href="#">Return to the top</a></span>
    </footer>
  </main>

  <script>
    const canvas = document.getElementById("sky");
    const ctx = canvas.getContext("2d");
    let stars = [];

    function resize(){
      const dpr = Math.max(1, Math.min(2, window.devicePixelRatio || 1));
      canvas.width = Math.floor(innerWidth * dpr);
      canvas.height = Math.floor(innerHeight * dpr);
      canvas.style.width = innerWidth + "px";
      canvas.style.height = innerHeight + "px";
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      stars = Array.from({length: Math.min(160, Math.floor(innerWidth * innerHeight / 7000))}, () => ({
        x: Math.random() * innerWidth,
        y: Math.random() * innerHeight,
        r: Math.random() * 1.4 + .25,
        a: Math.random() * .7 + .15,
        v: Math.random() * .18 + .03
      }));
    }

    function draw(){
      ctx.clearRect(0, 0, innerWidth, innerHeight);
      for(const s of stars){
        s.y += s.v;
        if(s.y > innerHeight + 6){
          s.y = -6;
          s.x = Math.random() * innerWidth;
        }
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(234,242,255,${s.a})`;
        ctx.fill();
      }
      requestAnimationFrame(draw);
    }

    resize();
    draw();
    addEventListener("resize", resize);

    const lines = [
      "A question is a lantern with a handle.",
      "Start where the fog is thinnest.",
      "If the idea feels too large, give it a chair and ask its name.",
      "The draft is not a failed final; it is a living weather report.",
      "Sometimes clarity arrives after you make a beautiful mess.",
      "Treat the blank page as a room, not a judge.",
      "Small hinges move large doors."
    ];

    const replies = [
      "The room suggests: make it smaller, then make it truer.",
      "The room suggests: keep the strange part; it is probably the compass.",
      "The room suggests: write the version you are afraid is too simple.",
      "The room suggests: answer with an experiment, not an argument.",
      "The room suggests: follow the image that will not leave you alone.",
      "The room suggests: name the missing piece without blaming it."
    ];

    const wander = document.getElementById("wander");
    const reply = document.getElementById("reply");
    const field = document.getElementById("field");

    wander.addEventListener("click", () => {
      reply.textContent = lines[Math.floor(Math.random() * lines.length)];
      document.getElementById("question").scrollIntoView({behavior:"smooth", block:"center"});
    });

    document.getElementById("answer").addEventListener("click", () => {
      const text = field.value.trim();
      if(!text){
        reply.textContent = "The room waits. Even three words are enough.";
        field.focus();
        return;
      }
      reply.textContent = replies[Math.floor(Math.random() * replies.length)];
    });

    document.getElementById("clear").addEventListener("click", () => {
      field.value = "";
      reply.textContent = "";
      field.focus();
    });
  </script>
</body>
</html>
```

What: It is an offline, atmospheric landing page called “A Room for Unfinished Things,” with animated stars, reflective prompts, and a small interactive question box.