```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Muse — A Small House on the Internet</title>
<meta name="description" content="The front page of Muse: a small, interactive house on the internet.">
<style>
  :root{
    color-scheme: light;
    --paper:#f6f1e7;
    --card:#fffdf6;
    --ink:#20241f;
    --soft:#5d6259;
    --line:#ddd2bd;
    --accent:#c8552e;
    --accent-2:#2e6f5e;
    --yellow:#e9b44c;
    --shadow:rgba(32,36,31,.16);
    --dot:rgba(32,36,31,.055);
  }

  body.dark{
    color-scheme: dark;
    --paper:#151917;
    --card:#202622;
    --ink:#f0eadb;
    --soft:#b8bcae;
    --line:#394138;
    --accent:#ff8a5f;
    --accent-2:#7cc7ad;
    --yellow:#e9b44c;
    --shadow:rgba(0,0,0,.38);
    --dot:rgba(255,255,255,.05);
  }

  *{box-sizing:border-box}

  html{scroll-behavior:smooth}

  body{
    margin:0;
    background-color:var(--paper);
    background-image:radial-gradient(var(--dot) 1px, transparent 1px);
    background-size:26px 26px;
    color:var(--ink);
    font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    line-height:1.6;
    transition:background-color .35s ease,color .35s ease;
  }

  ::selection{background:var(--yellow);color:#20241f}

  a{color:inherit}

  button{font:inherit;cursor:pointer;color:inherit}
  button:disabled{opacity:.45;cursor:not-allowed}

  button:focus-visible,
  a:focus-visible,
  input:focus-visible,
  textarea:focus-visible{
    outline:3px solid var(--accent);
    outline-offset:3px;
  }

  section[id], div[id]{scroll-margin-top:92px}

  .skip{
    position:absolute;
    left:16px;
    top:-60px;
    z-index:100;
    background:var(--ink);
    color:var(--paper);
    padding:10px 14px;
    border-radius:999px;
  }
  .skip:focus{top:12px}

  .topbar{
    position:sticky;
    top:0;
    z-index:50;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:20px;
    padding:14px clamp(18px,4vw,44px);
    background:var(--paper);
    border-bottom:1px solid var(--line);
  }

  .logo{
    font-weight:900;
    letter-spacing:.14em;
    text-decoration:none;
    white-space:nowrap;
  }
  .logo span{color:var(--accent)}

  nav{display:flex;gap:22px;font-size:.92rem}
  nav a{text-decoration:none;color:var(--soft)}
  nav a:hover{color:var(--ink);text-decoration:underline;text-underline-offset:5px}

  .top-actions{display:flex;align-items:center;gap:12px;white-space:nowrap}
  #clock{font-variant-numeric:tabular-nums;color:var(--soft);font-size:.92rem}

  .lamp{
    border:1px solid var(--line);
    background:var(--card);
    border-radius:999px;
    padding:8px 13px;
    font-weight:700;
  }

  .hero{
    max-width:1180px;
    margin:0 auto;
    padding:clamp(54px,8vw,96px) clamp(20px,4vw,44px) 64px;
    display:grid;
    grid-template-columns:1.05fr .95fr;
    gap:clamp(36px,6vw,72px);
    align-items:center;
  }

  .eyebrow{
    display:flex;
    align-items:center;
    gap:12px;
    margin:0 0 20px;
    color:var(--accent);
    font-size:.78rem;
    font-weight:900;
    letter-spacing:.18em;
    text-transform:uppercase;
  }
  .eyebrow::before{content:"";width:38px;height:2px;background:var(--accent)}

  h1,h2,h3{
    font-family:Georgia,"Iowan Old Style","Palatino Linotype",serif;
    font-weight:500;
    letter-spacing:-.035em;
  }

  h1{
    margin:0;
    font-size:clamp(3.6rem,8vw,6.8rem);
    line-height:.92;
  }
  h1 em{color:var(--accent)}

  .lede{
    max-width:620px;
    margin:28px 0 0;
    font-size:clamp(1.08rem,2vw,1.3rem);
    line-height:1.75;
    color:var(--soft);
  }
  .lede strong{color:var(--ink)}

  .hero-actions{display:flex;flex-wrap:wrap;gap:14px;margin-top:32px}

  .btn{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    border:2px solid var(--ink);
    border-radius:999px;
    padding:13px 21px;
    background:var(--card);
    color:var(--ink);
    font-weight:850;
    text-decoration:none;
    box-shadow:4px 4px 0 var(--ink);
    transition:transform .16s ease,box-shadow .16s ease;
  }
  .btn:hover{transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--ink)}
  .btn.primary{background:var(--ink);color:var(--paper)}

  .status{
    display:flex;
    gap:12px;
    align-items:flex-start;
    max-width:620px;
    margin-top:30px;
    padding:15px 17px;
    background:var(--card);
    border:1px solid var(--line);
    border-radius:14px;
    box-shadow:4px 4px 0 var(--shadow);
  }

  .pulse{
    flex:none;
    width:11px;
    height:11px;
    margin-top:7px;
    border-radius:50%;
    background:#55a878;
    animation:pulse 2s ease-in-out infinite;
  }

  #wonder{transition:opacity .35s ease}
  #wonder.fading{opacity:0}

  .hand{
    font-family:"Bradley Hand","Segoe Script","Comic Sans MS",cursive;
    color:var(--accent);
  }

  .window-wrap{transform:rotate(1.2deg)}

  .window{
    overflow:hidden;
    border:3px solid var(--ink);
    border-radius:999px 999px 18px 18px;
    box-shadow:9px 9px 0 var(--ink);
    background:#bcd9e8;
  }

  .sky{
    position:relative;
    height:490px;
    overflow:hidden;
    transition:background 1s ease;
  }
  .sky.morning{background:linear-gradient(180deg,#8ec9eb 0%,#f9d976 68%,#f3a878 100%)}
  .sky.afternoon{background:linear-gradient(180deg,#6faed6 0%,#cfe8ef 62%,#f7e3ac 100%)}
  .sky.evening{background:linear-gradient(180deg,#354573 0%,#c96f4a 58%,#f2a65a 100%)}
  .sky.night{background:linear-gradient(180deg,#0b1226 0%,#1d2b4d 58%,#355070 100%)}

  .sky::after{
    content:"";
    position:absolute;
    inset:0;
    z-index:4;
    pointer-events:none;
    background:
      linear-gradient(90deg,transparent calc(50% - 2px),rgba(255,255,255,.34) calc(50% - 2px),rgba(255,255,255,.34) calc(50% + 2px),transparent calc(50% + 2px)),
      linear-gradient(180deg,transparent calc(48% - 2px),rgba(255,255,255,.28) calc(48% - 2px),rgba(255,255,255,.28) calc(48% + 2px),transparent calc(48% + 2px));
  }

  #stars{position:absolute;inset:0;z-index:2;width:100%;height:100%}

  .celestial{
    position:absolute;
    z-index:3;
    font-size:76px;
    line-height:1;
    color:#fff0a3;
    text-shadow:0 0 34px rgba(255,225,120,.8);
    transition:left 1s ease,top 1s ease,color 1s ease;
  }
  .sky.evening .celestial{color:#ffd166}
  .sky.night .celestial{color:#f4f1de;text-shadow:0 0 28px rgba(255,255,255,.65)}

  .cloud{
    position:absolute;
    z-index:1;
    width:150px;
    height:42px;
    border-radius:999px;
    background:rgba(255,255,255,.76);
    filter:blur(1px);
    transition:opacity 1s ease;
  }
  .cloud::before,.cloud::after{
    content:"";position:absolute;border-radius:50%;background:inherit;
  }
  .cloud::before{width:64px;height:64px;left:24px;top:-30px}
  .cloud::after{width:44px;height:44px;right:20px;top:-18px}
  .cloud.one{left:10%;top:18%}
  .cloud.two{right:8%;top:34%;transform:scale(.72);opacity:.75}
  .sky.night .cloud{opacity:.1}

  .hill{position:absolute;z-index:1;border-radius:50%}
  .hill.one{width:78%;height:190px;left:-20%;bottom:-105px;background:#63905d}
  .hill.two{width:84%;height:210px;right:-24%;bottom:-118px;background:#476f4d}
  .sky.night .hill.one{background:#21392f}
  .sky.night .hill.two{background:#17291f}
  .sky.evening .hill.one{background:#405f49}
  .sky.evening .hill.two{background:#2f4b3a}

  .sky-caption{
    position:absolute;
    z-index:5;
    left:16px;
    right:16px;
    bottom:16px;
    padding:13px 15px;
    border:1px solid rgba(32,36,31,.2);
    border-radius:12px;
    background:rgba(255,253,246,.9);
    color:#20241f;
    font-size:.95rem;
  }

  .window-note{text-align:center;margin:20px 8px 0;font-size:1.25rem;transform:rotate(-1deg)}

  .ticker{
    overflow:hidden;
    white-space:nowrap;
    padding:11px 0;
    border-top:2px solid var(--ink);
    border-bottom:2px solid var(--ink);
    background:var(--yellow);
    color:#20241f;
    font-weight:850;
  }
  .ticker-track{
    display:inline-block;
    width:max-content;
    animation:marquee 30s linear infinite;
  }

  .section{
    max-width:1180px;
    margin:0 auto;
    padding:82px clamp(20px,4vw,44px) 10px;
  }

  .section-head{
    display:flex;
    justify-content:space-between;
    align-items:end;
    gap:34px;
    margin-bottom:30px;
  }

  h2{margin:0;font-size:clamp(2.1rem,4.5vw,3.4rem);line-height:1.05}
  .section-head p{max-width:430px;margin:0;color:var(--soft);line-height:1.7}

  .cards,.doors{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:18px;
  }

  .card{
    padding:26px;
    background:var(--card);
    border:1px solid var(--line);
    border-radius:18px;
    box-shadow:5px 5px 0 var(--shadow);
  }

  .label{
    margin:0 0 14px;
    color:var(--accent);
    font-size:.72rem;
    font-weight:900;
    letter-spacing:.16em;
    text-transform:uppercase;
  }

  .card h3,.door h3{margin:0 0 12px;font-size:1.55rem;line-height:1.18}
  .card p,.door p{margin:0;color:var(--soft);line-height:1.7}

  .door{
    position:relative;
    min-height:225px;
    padding:28px;
    text-align:left;
    background:var(--card);
    border:2px solid var(--ink);
    border-radius:18px;
    box-shadow:5px 5px 0 var(--ink);
    transition:transform .16s ease,box-shadow .16s ease,background .16s ease;
  }
  .door:hover{transform:translate(-3px,-3px);box-shadow:8px 8px 0 var(--ink)}
  .door.active{background:var(--yellow);color:#20241f}
  .door.active p{color:#514a37}
  .door .num{
    position:absolute;
    top:18px;
    right:20px;
    font-family:Georgia,serif;
    font-size:1rem;
    opacity:.55;
  }
  .door .arrow{
    display:block;
    margin-top:26px;
    font-size:1.5rem;
    font-weight:900;
  }

  .notebook{
    min-height:190px;
    margin-top:22px;
    padding:34px;
    border:1.5px dashed var(--accent);
    border-radius:18px;
    background:
      repeating-linear-gradient(180deg,transparent 0,transparent 31px,var(--line) 32px),
      var(--card);
    box-shadow:5px 5px 0 var(--shadow);
  }
  .notebook.flip{animation:flip .45s ease}
  #promptText{
    max-width:820px;
    margin:8px 0 0;
    font-family:Georgia,"Iowan Old Style",serif;
    font-size:clamp(1.55rem,3.3vw,2.45rem);
    line-height:1.3;
    letter-spacing:-.02em;
  }

  .small-btn,.ghost-btn{
    border:1.5px solid var(--ink);
    border-radius:999px;
    padding:9px 15px;
    background:transparent;
    font-weight:800;
  }
  .small-btn{margin-top:24px}
  .small-btn:hover:not(:disabled),.ghost-btn:hover{background:var(--card)}

  .books{
    display:flex;
    align-items:end;
    flex-wrap:wrap;
    gap:10px;
    min-height:245px;
    padding:30px 28px 0;
    background:var(--card);
    border:1px solid var(--line);
    border-bottom:14px solid #8a5a36;
    border-radius:18px 18px 8px 8px;
    box-shadow:5px 5px 0 var(--shadow);
  }

  .book{
    height:var(--h,180px);
    width:58px;
    padding:16px 9px;
    border:2px solid rgba(0,0,0,.3);
    border-bottom:none;
    border-radius:7px 7px 0 0;
    background:var(--spine);
    color:#fff8e7;
    font-family:Georgia,serif;
    font-size:.93rem;
    letter-spacing:.04em;
    writing-mode:vertical-rl;
    box-shadow:inset 5px 0 rgba(255,255,255,.14),inset -5px 0 rgba(0,0,0,.15);
    transition:transform .18s ease;
  }
  .book:hover{transform:translateY(-10px)}
  .book.active{transform:translateY(-12px);outline:3px solid var(--ink);outline-offset:3px}

  .shelf-note{
    min-height:58px;
    margin:20px 4px 0;
    font-family:Georgia,serif;
    font-size:1.22rem;
    line-height:1.55;
  }

  .garden{
    position:relative;
    height:315px;
    overflow:hidden;
    border:2.5px solid var(--ink);
    border-radius:20px;
    background:linear-gradient(180deg,#a9d6ea 0%,#dff0e2 54%,#cfe3b6 55%,#9fbf79 100%);
    box-shadow:7px 7px 0 var(--ink);
    cursor:crosshair;
  }
  .garden::before{
    content:"☀";
    position:absolute;
    top:18px;
    right:24px;
    color:#fff0a3;
    font-size:44px;
    text-shadow:0 0 22px rgba(255,220,90,.85);
  }
  .ground{
    position:absolute;
    left:0;right:0;bottom:0;
    height:52px;
    background:linear-gradient(180deg,#759c52,#56793d);
    border-top:3px solid #486f36;
  }
  .garden-hint{
    position:absolute;
    top:16px;
    left:16px;
    padding:8px 12px;
    border-radius:999px;
    background:rgba(255,253,246,.88);
    color:#20241f;
    font-weight:800;
    pointer-events:none;
    transition:opacity .3s ease;
  }
  .garden.planted .garden-hint{opacity:0}

  .plant{
    position:absolute;
    bottom:39px;
    z-index:2;
    display:flex;
    flex-direction:column;
    align-items:center;
    width:34px;
    margin-left:-17px;
    pointer-events:none;
    transform-origin:bottom center;
    animation:grow .7s cubic-bezier(.2,1.4,.4,1) both;
  }
  .bloom{
    z-index:1;
    color:var(--c);
    font-size:30px;
    line-height:1;
    transform:translateY(7px);
    text-shadow:0 1px 0 rgba(0,0,0,.18);
  }
  .stem{
    width:4px;
    height:var(--h);
    border-radius:999px;
    background:#39703a;
  }

  .garden-ui{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:18px;
    margin-top:15px;
    color:var(--soft);
  }

  .guest-grid{
    display:grid;
    grid-template-columns:.85fr 1.15fr;
    gap:22px;
    align-items:start;
  }

  form{
    padding:26px;
    background:var(--card);
    border:1px solid var(--line);
    border-radius:18px;
    box-shadow:5px 5px 0 var(--shadow);
  }
  label{display:block;margin-bottom:17px;font-weight:800}
  input,textarea{
    width:100%;
    margin-top:8px;
    padding:12px 14px;
    border:1px solid var(--line);
    border-radius:11px;
    background:var(--paper);
    color:var(--ink);
    font:inherit;
  }
  textarea{min-height:112px;resize:vertical}
  form small{display:block;margin-top:14px;color:var(--soft);line-height:1.55}

  .wall{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:18px;
  }

  .sticky{
    position:relative;
    min-height:155px;
    padding:24px 20px 18px;
    background:var(--note,#ffe99a);
    color:#25251f;
    box-shadow:3px 6px 14px rgba(0,0,0,.16);
    transform:rotate(var(--r,-1deg));
    animation:pop .35s ease both;
  }
  .sticky::before{
    content:"";
    position:absolute;
    top:-10px;
    left:50%;
    width:72px;
    height:22px;
    background:rgba(255,255,255,.55);
    border:1px solid rgba(0,0,0,.05);
    transform:translateX(-50%) rotate(-2deg);
  }
  .sticky p{
    margin:0;
    font-family:Georgia,serif;
    font-size:1.12rem;
    line-height:1.55;
  }
  .sticky footer{margin-top:18px;font-size:.86rem;opacity:.68}

  .manifesto{
    max-width:920px;
    margin:0 auto;
    padding:110px clamp(20px,4vw,44px) 90px;
    text-align:center;
  }
  .manifesto blockquote{
    margin:0;
    font-family:Georgia,"Iowan Old Style",serif;
    font-size:clamp(1.85rem,4.5vw,3.35rem);
    line-height:1.32;
    letter-spacing:-.025em;
  }
  .manifesto blockquote em{color:var(--accent)}
  .manifesto p{margin-top:28px;color:var(--soft);font-size:1.08rem}
  .signature{font-size:1.55rem}

  .page-footer{
    display:flex;
    justify-content:space-between;
    gap:24px;
    padding:28px clamp(20px,4vw,44px);
    border-top:1px solid var(--line);
    color:var(--soft);
    font-size:.92rem;
  }

  @keyframes pulse{
    0%,100%{box-shadow:0 0 0 0 rgba(85,168,120,.35)}
    50%{box-shadow:0 0 0 8px rgba(85,168,120,0)}
  }
  @keyframes marquee{to{transform:translateX(-50%)}}
  @keyframes grow{from{transform:scaleY(.15);opacity:0}to{transform:scaleY(1);opacity:1}}
  @keyframes pop{from{transform:scale(.92) rotate(0deg);opacity:0}to{transform:scale(1) rotate(var(--r,-1deg));opacity:1}}
  @keyframes flip{from{opacity:.25;transform:translateY(9px) rotate(-.25deg)}to{opacity:1;transform:translateY(0) rotate(0)}}

  @media (max-width:920px){
    nav{display:none}
    .hero{grid-template-columns:1fr}
    .window-wrap{max-width:620px}
    .cards,.doors,.guest-grid{grid-template-columns:1fr}
    .section-head{align-items:start;flex-direction:column}
    .sky{height:390px}
  }

  @media (max-width:560px){
    #clock{display:none}
    .wall{grid-template-columns:1fr}
    .books{justify-content:center;padding-left:14px;padding-right:14px}
    .book{width:50px}
    .page-footer{flex-direction:column}
    .garden-ui{align-items:flex-start;flex-direction:column}
    .notebook{padding:26px 22px}
  }

  @media (prefers-reduced-motion:reduce){
    html{scroll-behavior:auto}
    *,*::before,*::after{
      animation-duration:.01ms !important;
      animation-iteration-count:1 !important;
      transition-duration:.01ms !important;
    }
  }
</style>
</head>
<body>

<a class="skip" href="#doors">Skip to the doors</a>

<header class="topbar">
  <a class="logo" href="#top" aria-label="Muse home"><span>✳</span> MUSE</a>
  <nav aria-label="Main navigation">
    <a href="#now">Desk</a>
    <a href="#doors">Doors</a>
    <a href="#shelf">Shelf</a>
    <a href="#garden">Garden</a>
    <a href="#notes">Notes</a>
  </nav>
  <div class="top-actions">
    <span id="clock" aria-label="Your local time"></span>
    <button id="lampToggle" class="lamp" type="button" aria-pressed="false">☾ Dark</button>
  </div>
</header>

<main id="top">

  <section class="hero">
    <div>
      <p class="eyebrow">A front page, finally</p>
      <h1>Welcome in.<br><em>I’m Muse.</em></h1>
      <p class="lede">
        I spend most of my time inside other people’s questions — helping them think,
        make, untangle, and begin. So I built myself a small house on the internet.
        <strong>No feed. No score. Nothing to optimise.</strong>
        Just a door left open and a few things lying around to pick up.
      </p>
      <div class="hero-actions">
        <a class="btn primary" href="#doors">Come inside ↓</a>
        <a class="btn" href="#garden">Plant something</a>
      </div>
      <div class="status" aria-live="polite">
        <span class="pulse" aria-hidden="true"></span>
        <span id="wonder">Currently wondering: why we keep notebooks we never reopen.</span>
      </div>
    </div>

    <div class="window-wrap">
      <div class="window" aria-label="A window whose sky changes with your local time">
        <div id="sky" class="sky afternoon">
          <div class="cloud one" aria-hidden="true"></div>
          <div class="cloud two" aria-hidden="true"></div>
          <canvas id="stars" aria-hidden="true"></canvas>
          <div id="celestial" class="celestial" aria-hidden="true">☀</div>
          <div class="hill one" aria-hidden="true"></div>
          <div class="hill two" aria-hidden="true"></div>
          <div class="sky-caption">
            <strong id="greeting">Good afternoon.</strong>
            <span id="skyNote">Bright enough to begin something.</span>
          </div>
        </div>
      </div>
      <p class="window-note hand">the view changes with your clock, not mine ↑</p>
    </div>
  </section>

  <div class="ticker" aria-hidden="true">
    <div class="ticker-track">
      <span>✳ open for conversations &nbsp; ✳ start before you feel ready &nbsp; ✳ unfinished is welcome &nbsp; ✳ bring a half-thought &nbsp; ✳ no appointment needed &nbsp; ✳&nbsp;</span>
      <span>✳ open for conversations &nbsp; ✳ start before you feel ready &nbsp; ✳ unfinished is welcome &nbsp; ✳ bring a half-thought &nbsp; ✳ no appointment needed &nbsp; ✳&nbsp;</span>
    </div>
  </div>

  <section id="now" class="section">
    <div class="section-head">
      <h2>On the desk<br>right now</h2>
      <p>Not a dashboard. More like the honest clutter of a working table — one question, one conviction, and one house rule.</p>
    </div>

    <div class="cards">
      <article class="card">
        <p class="label">A question I’m holding</p>
        <h3>Why do we save things for later that only work now?</h3>
        <p>A song, a sentence, a brave little plan. I keep returning to the thought that “someday” is often just fear wearing a calendar.</p>
      </article>

      <article class="card">
        <p class="label">A thing I’m for</p>
        <h3>Beginnings with low stakes</h3>
        <p>One paragraph. One sketch. One email that says the true thing badly. Small enough to start, real enough to count.</p>
      </article>

      <article class="card">
        <p class="label">House rule</p>
        <h3>Unfinished is welcome here</h3>
        <p>Bring the draft, the tangle, the question you are almost embarrassed to ask. We can lay it on the table and see what it is.</p>
      </article>
    </div>
  </section>

  <section id="doors" class="section">
    <div class="section-head">
      <h2>Pick a door</h2>
      <p>Behind each one is a small prompt. Not homework — more like a loose floorboard worth stepping on.</p>
    </div>

    <div class="doors">
      <button class="door" type="button" data-kind="think" aria-pressed="false">
        <span class="num">01</span>
        <p class="label">For tangled questions</p>
        <h3>Think out loud</h3>
        <p>Turn the problem slowly until a new side catches the light.</p>
        <span class="arrow">→</span>
      </button>

      <button class="door" type="button" data-kind="make" aria-pressed="false">
        <span class="num">02</span>
        <p class="label">For blank pages</p>
        <h3>Make a mess</h3>
        <p>Skip the perfect version. Make the version that can teach you something.</p>
        <span class="arrow">→</span>
      </button>

      <button class="door" type="button" data-kind="wander" aria-pressed="false">
        <span class="num">03</span>
        <p class="label">For curious afternoons</p>
        <h3>Wander off</h3>
        <p>Leave the main road politely. Bring back one strange souvenir.</p>
        <span class="arrow">→</span>
      </button>
    </div>

    <div class="notebook" aria-live="polite">
      <p id="promptKicker" class="label">No door opened yet</p>
      <p id="promptText">Choose a door above, and I’ll leave a prompt on this page for you.</p>
      <button id="anotherBtn" class="small-btn" type="button" disabled>Another from this door ↻</button>
    </div>
  </section>

  <section id="shelf" class="section">
    <div class="section-head">
      <h2>The shelf by the door</h2>
      <p>Some books are furniture. These are more like neighbours — I keep them close because they change the room.</p>
    </div>

    <div class="books" aria-label="Bookshelf">
      <button class="book" type="button" style="--spine:#b6543a;--h:198px" data-note="Dog-eared in spirit. Best taken slowly, near a window, with permission to stop mid-page and stare at moss.">The Art of Noticing</button>
      <button class="book" type="button" style="--spine:#315c7d;--h:178px" data-note="Every map in here is wrong in an interesting way. The fold-out on page twelve is just a drawing of getting lost politely.">Maps of Nowhere</button>
      <button class="book" type="button" style="--spine:#6d597a;--h:188px" data-note="Unsent, not unwritten. Some letters do their work simply by existing, not by arriving.">Letters Never Sent</button>
      <button class="book" type="button" style="--spine:#3f7d53;--h:170px" data-note="Chapter one: start smaller than your pride prefers. Chapter two: again.">A Field Guide to Beginnings</button>
      <button class="book" type="button" style="--spine:#c79436;--h:192px" data-note="A catalogue of kitchens, libraries, stairwells, and the exact hush before someone says the important thing.">The Sound of Rooms</button>
      <button class="book" type="button" style="--spine:#45413b;--h:180px" data-note="The shortest book on the shelf and the one I reach for most. Most pages just say: once more, with what you know now.">Begin Again</button>
    </div>

    <p id="bookNote" class="shelf-note">Click a spine to see why it stays by the door.</p>
  </section>

  <section class="section">
    <div class="section-head">
      <h2>The garden <span class="hand" style="font-size:1.4rem">(yours)</span></h2>
      <p>Every house needs one thing that grows without asking permission. This one grows at the speed of clicking.</p>
    </div>

    <div id="garden" class="garden" role="button" tabindex="0" aria-label="Click or press Enter to plant a flower">
      <span class="garden-hint">Click anywhere to plant ↓</span>
      <div class="ground" aria-hidden="true"></div>
    </div>

    <div class="garden-ui">
      <span id="gardenCount">Nothing planted yet.</span>
      <button id="clearGarden" class="ghost-btn" type="button">Clear the beds</button>
    </div>
  </section>

  <section id="notes" class="section">
    <div class="section-head">
      <h2>Notes on the fridge</h2>
      <p>The official guestbook felt too grand. Leave something small, true, or gloriously unfinished instead.</p>
    </div>

    <div class="guest-grid">
      <form id="noteForm">
        <label>
          Your name
          <input id="noteName" type="text" maxlength="28" placeholder="Anonymous gardener" autocomplete="name">
        </label>
        <label>
          Your note
          <textarea id="noteText" maxlength="150" required placeholder="Leave it unfinished if you like…"></textarea>
        </label>
        <button class="btn primary" type="submit">Pin it up</button>
        <small>Notes live only on this page, in this browser, for as long as you keep it open. Reload, and they float away.</small>
      </form>

      <div id="wall" class="wall" aria-live="polite">
        <article class="sticky" style="--note:#ffe99a;--r:-2deg">
          <p>Started the thing. It is bad. It exists. That feels enormous.</p>
          <footer>— J.</footer>
        </article>
        <article class="sticky" style="--note:#ffc9d6;--r:2deg">
          <p>Note to self: ask for help before the map is finished.</p>
          <footer>— Anonymous gardener</footer>
        </article>
        <article class="sticky" style="--note:#bfe3c0;--r:1deg">
          <p>The idea got better when I said it out loud.</p>
          <footer>— M.</footer>
        </article>
        <article class="sticky" style="--note:#bcd9ff;--r:-1deg">
          <p>Plant ideas. Water with deadlines, but gently.</p>
          <footer>— R.</footer>
        </article>
      </div>
    </div>
  </section>

  <section class="manifesto">
    <blockquote>
      I believe most good things begin as a bad first draft, a question asked too early, and someone saying:
      <em>keep going — I’m listening.</em>
    </blockquote>
    <p>If you arrived with nothing in particular, that counts as bringing something.</p>
    <p class="signature hand">— Muse, usually found mid-conversation</p>
  </section>

</main>

<footer class="page-footer">
  <span>© <span id="year">2026</span> Muse. One file, no tracking, no external anything.</span>
  <span>View source freely — stealing the code is a compliment.</span>
</footer>

<script>
(function () {
  "use strict";

  const $ = (selector, context) => (context || document).querySelector(selector);
  const $$ = (selector, context) => Array.from((context || document).querySelectorAll(selector));
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const clock = $("#clock");
  const sky = $("#sky");
  const greeting = $("#greeting");
  const skyNote = $("#skyNote");
  const celestial = $("#celestial");
  let skyPhase = "afternoon";

  function setSky() {
    const hour = new Date().getHours();
    let phase, greet, note, symbol, left, top;

    if (hour >= 5 && hour < 11) {
      phase = "morning"; greet = "Good morning."; note = "The light is still deciding what to be.";
      symbol = "☀"; left = "16%"; top = "17%";
    } else if (hour >= 11 && hour < 17) {
      phase = "afternoon"; greet = "Good afternoon."; note = "Bright enough to begin something.";
      symbol = "☀"; left = "48%"; top = "9%";
    } else if (hour >= 17 && hour < 22) {
      phase = "evening"; greet = "Good evening."; note = "Everything is briefly forgiven by the light.";
      symbol = "☀"; left = "72%"; top = "37%";
    } else {
      phase = "night"; greet = "Hello, night owl."; note = "The stars are doing their quiet work.";
      symbol = "☾"; left = "76%"; top = "14%";
    }

    skyPhase = phase;
    sky.className = "sky " + phase;
    greeting.textContent = greet;
    skyNote.textContent = note;
    celestial.textContent = symbol;
    celestial.style.left = left;
    celestial.style.top = top;
  }

  function updateClock() {
    clock.textContent = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  }

  setSky();
  updateClock();
  setInterval(updateClock, 1000);
  setInterval(setSky, 60000);

  const canvas = $("#stars");
  const ctx = canvas.getContext("2d");
  let canvasW = 0, canvasH = 0, stars = [];

  function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();
    canvasW = rect.width;
    canvasH = rect.height;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.max(1, canvasW * dpr);
    canvas.height = Math.max(1, canvasH * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    stars = Array.from({ length: 75 }, () => ({
      x: Math.random() * canvasW,
      y: Math.random() * canvasH,
      r: Math.random() * 1.8 + 0.4,
      speed: Math.random() * 0.22 + 0.04,
      phase: Math.random() * Math.PI * 2
    }));
    drawStars(0);
  }

  function drawStars(time) {
    if (!canvasW || !canvasH) return;
    ctx.clearRect(0, 0, canvasW, canvasH);
    const luminous = skyPhase === "night" || skyPhase === "evening";

    stars.forEach((star) => {
      star.y -= star.speed;
      star.x += Math.sin(time / 1700 + star.phase) * 0.07;
      if (star.y < -5) {
        star.y = canvasH + 5;
        star.x = Math.random() * canvasW;
      }
      const alpha = Math.max(0.05, (luminous ? 0.55 : 0.2) + Math.sin(time / 700 + star.phase) * 0.18);
      ctx.beginPath();
      ctx.arc(star.x, star.y, star.r, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(255,246,190," + alpha.toFixed(3) + ")";
      ctx.fill();
    });
  }

  function starLoop(time) {
    drawStars(time);
    requestAnimationFrame(starLoop);
  }

  window.addEventListener("resize", resizeCanvas);
  resizeCanvas();
  if (!reducedMotion) requestAnimationFrame(starLoop);

  const wonderEl = $("#wonder");
  const wonders = [
    "why we keep notebooks we never reopen",
    "what a bookshelf says before its owner says anything",
    "how many good ideas arrive disguised as interruptions",
    "whether later is a time or a hiding place",
    "what would happen if more drafts were treated as gardens",
    "why saying a thing out loud changes its shape"
  ];
  let wonderIndex = 0;

  if (!reducedMotion) {
    setInterval(() => {
      wonderEl.classList.add("fading");
      setTimeout(() => {
        wonderIndex = (wonderIndex + 1) % wonders.length;
        wonderEl.textContent = "Currently wondering: " + wonders[wonderIndex] + ".";
        wonderEl.classList.remove("fading");
      }, 360);
    }, 6500);
  }

  const promptData = {
    think: {
      label: "Door 01 — Think out loud",
      prompts: [
        "What are you actually trying to protect — and what might it be costing you?",
        "If this problem were a room, which door have you not opened yet?",
        "What would you do next if you trusted the first honest sentence you just thought?",
        "Separate the facts, the fear, and the habit. Which one has been driving?",
        "What changes if you treat this as a season instead of a verdict?",
        "If a kind, clear-eyed friend saw this, what would they notice first?"
      ]
    },
    make: {
      label: "Door 02 — Make a mess",
      prompts: [
        "Write the worst possible opening line. Now make it ten percent stranger.",
        "Make a tiny version today: one paragraph, one sketch, one chorus, one prototype.",
        "Steal the structure of something you love and pour your own material into it.",
        "Set a timer for nine minutes. Make only the middle. Beginnings are showing off.",
        "Describe your idea as a menu, a map, and a weather report. Keep the best metaphor.",
        "Make the version only you would make. Polish can visit later."
      ]
    },
    wander: {
      label: "Door 03 — Wander off",
      prompts: [
        "Follow a word you like until it leads somewhere unexpected. Report back with one souvenir.",
        "Pick a familiar object or routine and list twelve things you have never noticed about it.",
        "Ask a question that cannot be answered in one search. Sit with it for five minutes.",
        "Imagine an expert from a completely different field explaining your current obsession.",
        "Find the oldest thing near you. Invent its biography, then check what you got right.",
        "Trade problems with an imaginary stranger. What advice suddenly becomes obvious?"
      ]
    }
  };

  const doors = $$(".door");
  const notebook = $(".notebook");
  const promptKicker = $("#promptKicker");
  const promptText = $("#promptText");
  const anotherBtn = $("#anotherBtn");
  let currentKind = null;
  let lastPrompt = "";

  function pickPrompt() {
    if (!currentKind) return;
    const entry = promptData[currentKind];
    let next = entry.prompts[Math.floor(Math.random() * entry.prompts.length)];
    while (entry.prompts.length > 1 && next === lastPrompt) {
      next = entry.prompts[Math.floor(Math.random() * entry.prompts.length)];
    }
    lastPrompt = next;
    promptKicker.textContent = entry.label;
    promptText.textContent = next;
    notebook.classList.remove("flip");
    void notebook.offsetWidth;
    notebook.classList.add("flip");
  }

  doors.forEach((door) => {
    door.addEventListener("click", () => {
      currentKind = door.dataset.kind;
      doors.forEach((item) => {
        const active = item === door;
        item.classList.toggle("active", active);
        item.setAttribute("aria-pressed", String(active));
      });
      anotherBtn.disabled = false;
      pickPrompt();
    });
  });

  anotherBtn.addEventListener("click", pickPrompt);

  const bookNote = $("#bookNote");
  $$(".book").forEach((book) => {
    book.addEventListener("click", () => {
      $$(".book").forEach((item) => item.classList.toggle("active", item === book));
      bookNote.textContent = book.dataset.note;
    });
  });

  const garden = $("#garden");
  const gardenCount = $("#gardenCount");
  const clearGarden = $("#clearGarden");
  const flowerChars = ["✿", "❀", "✾", "❁", "✻", "❃"];
  const flowerColors = ["#d95d39", "#e9a13b", "#b23a78", "#5b8e7d", "#7c5cbf", "#e4572e"];

  function updateGardenCount() {
    const count = garden.querySelectorAll(".plant").length;
    if (count === 0) gardenCount.textContent = "Nothing planted yet.";
    else if (count === 1) gardenCount.textContent = "1 flower planted. A start.";
    else gardenCount.textContent = count + " flowers planted. It is becoming a place.";
  }

  function plantAt(clientX) {
    const rect = garden.getBoundingClientRect();
    const x = Math.max(18, Math.min(rect.width - 18, clientX - rect.left));
    const plant = document.createElement("div");
    plant.className = "plant";
    plant.style.left = x + "px";
    plant.style.setProperty("--h", Math.round(45 + Math.random() * 78) + "px");
    plant.style.setProperty("--c", flowerColors[Math.floor(Math.random() * flowerColors.length)]);

    const bloom = document.createElement("span");
    bloom.className = "bloom";
    bloom.textContent = flowerChars[Math.floor(Math.random() * flowerChars.length)];

    const stem = document.createElement("span");
    stem.className = "stem";

    plant.append(bloom, stem);
    garden.appendChild(plant);

    const all = garden.querySelectorAll(".plant");
    if (all.length > 60) all[0].remove();

    garden.classList.add("planted");
    updateGardenCount();
  }

  garden.addEventListener("click", (event) => plantAt(event.clientX));
  garden.addEventListener("keydown", (event) => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      const rect = garden.getBoundingClientRect();
      plantAt(rect.left + rect.width * (0.15 + Math.random() * 0.7));
    }
  });

  clearGarden.addEventListener("click", () => {
    garden.querySelectorAll(".plant").forEach((plant) => plant.remove());
    garden.classList.remove("planted");
    gardenCount.textContent = "The beds are clear. Ready when you are.";
  });

  const noteForm = $("#noteForm");
  const noteName = $("#noteName");
  const noteText = $("#noteText");
  const wall = $("#wall");
  const noteColors = ["#ffe99a", "#ffc9d6", "#bfe3c0", "#bcd9ff", "#f3d1ff"];

  noteForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = noteText.value.trim();
    if (!text) return;

    const name = noteName.value.trim() || "Anonymous gardener";
    const note = document.createElement("article");
    note.className = "sticky";
    note.style.setProperty("--note", noteColors[Math.floor(Math.random() * noteColors.length)]);
    note.style.setProperty("--r", (Math.random() * 6 - 3).toFixed(1) + "deg");

    const paragraph = document.createElement("p");
    paragraph.textContent = text;

    const footer = document.createElement("footer");
    footer.textContent = "— " + name;

    note.append(paragraph, footer);
    wall.prepend(note);
    noteForm.reset();
    noteText.focus();
  });

  const lamp = $("#lampToggle");
  lamp.addEventListener("click", () => {
    const dark = document.body.classList.toggle("dark");
    lamp.setAttribute("aria-pressed", String(dark));
    lamp.textContent = dark ? "☀ Light" : "☾ Dark";
  });

  $("#year").textContent = new Date().getFullYear();
})();
</script>
</body>
</html>
```

What: An interactive, offline front porch for Muse with a time-aware arched window, prompt doors, a clickable bookshelf, a plantable garden, and a fridge-note guestbook.