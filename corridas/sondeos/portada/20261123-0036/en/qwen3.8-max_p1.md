```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Keeper's Log — Front Point Light</title>
<script>document.documentElement.classList.add('js');</script>
<style>
  :root{
    --ink:#060d17; --deep:#0a1626; --card:#0b1a2a; --sea:#0e2233;
    --foam:#e8ecec; --mist:#9db2b6; --amber:#f2b04a; --amber-hi:#ffd98a;
    --brass:#b78a4e; --line:rgba(157,178,182,.18);
    --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
    --mono:ui-monospace,"SF Mono","Cascadia Mono",Menlo,Consolas,"Courier New",monospace;
    --mono-s:11px;
  }
  *{box-sizing:border-box;margin:0;padding:0}
  @media (prefers-reduced-motion: no-preference){ html{scroll-behavior:smooth} }
  body{background:var(--ink);color:var(--foam);font-family:var(--serif);line-height:1.6;overflow-x:hidden}
  ::selection{background:var(--amber);color:#171004}
  a{color:inherit}
  .mono{font-family:var(--mono)}
  .wrap{width:min(1120px,92vw);margin-inline:auto}

  /* grain */
  .grain{position:fixed;inset:0;z-index:70;pointer-events:none;opacity:.07;mix-blend-mode:overlay;
    background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.6'/%3E%3C/svg%3E");}

  /* top bar */
  .topbar{position:fixed;top:0;left:0;right:0;z-index:50;display:flex;justify-content:space-between;align-items:center;gap:1.5rem;
    padding:15px max(4vw,calc((100vw - 1160px)/2));font-family:var(--mono);font-size:var(--mono-s);letter-spacing:.18em;
    transition:background .4s,border-color .4s;border-bottom:1px solid transparent}
  .topbar.scrolled{background:rgba(6,13,23,.94);border-bottom-color:var(--line)}
  .brand{text-decoration:none;color:var(--foam)} .brand span{color:var(--mist)}
  .topbar nav{display:flex;gap:1.7rem}
  .topbar nav a{text-decoration:none;color:var(--mist);transition:color .3s}
  .topbar nav a:hover{color:var(--amber-hi)}
  #chipClock{color:var(--amber);min-width:8ch;text-align:right}
  @media(max-width:720px){.topbar nav{display:none}}

  /* ================= LAMP ROOM ================= */
  .lamp{position:relative;min-height:100svh;overflow:hidden;display:flex;align-items:center}
  #sky{position:absolute;inset:0;width:100%;height:100%;z-index:0}
  .dim{position:absolute;inset:0;background:#02040a;opacity:0;transition:opacity 1.2s;z-index:3;pointer-events:none}
  body.lowlight .dim{opacity:.55}

  .beam{position:absolute;left:50%;bottom:75%;z-index:1;pointer-events:none}
  .rotor{position:absolute;left:0;top:0;animation:sweep 12s linear infinite}
  body.lowlight .rotor{opacity:.3}
  .w{position:absolute;left:0;top:-70px;width:min(1150px,92vw);height:140px;mix-blend-mode:screen;filter:blur(1px);
     background:linear-gradient(90deg,rgba(255,216,140,.55),rgba(255,216,140,.14) 45%,transparent 78%);
     clip-path:polygon(0 46%,0 54%,100% 96%,100% 4%)}
  .w2{transform:rotate(180deg)}
  .glowp{position:absolute;left:-46px;top:-46px;width:92px;height:92px;border-radius:50%;mix-blend-mode:screen;
     background:radial-gradient(circle,rgba(255,228,166,.95),rgba(255,200,110,.35) 42%,transparent 70%);
     animation:pulse 6s ease-in-out infinite}
  body.lowlight .glowp{opacity:.4}
  @keyframes sweep{to{transform:rotate(360deg)}}
  @keyframes pulse{0%,100%{transform:scale(1);opacity:.9}50%{transform:scale(1.25);opacity:1}}

  .station{position:absolute;right:5vw;bottom:-6px;width:clamp(190px,24vw,310px);z-index:2}
  .station svg{display:block;width:100%;height:auto}
  .flame{animation:flick 5s ease-in-out infinite}
  @keyframes flick{0%,100%{opacity:1}48%{opacity:.82}54%{opacity:.94}}
  .ring{position:absolute;left:50%;bottom:75%;width:22px;height:22px;margin:-11px 0 0 -11px;border-radius:50%;
     border:1px solid rgba(255,217,138,.85);animation:ringout 1.9s ease-out forwards;pointer-events:none}
  @keyframes ringout{to{transform:scale(15);opacity:0}}

  .lamp-copy{position:relative;z-index:4;width:min(700px,92vw);margin-inline:auto;padding:130px max(0px,calc((100vw - 1120px)/2)) 160px 0;margin-left:max(4vw,calc((100vw - 1120px)/2))}
  .overline{font-family:var(--mono);font-size:12px;letter-spacing:.26em;color:var(--amber)}
  h1.title{font-size:clamp(2.7rem,7vw,5.4rem);line-height:.98;text-transform:uppercase;font-weight:600;
     letter-spacing:.01em;margin:1rem 0 1.5rem;min-height:1em}
  .stand{font-size:clamp(1.05rem,1.6vw,1.3rem);color:var(--mist);max-width:56ch}
  .metarow{display:flex;flex-wrap:wrap;gap:.5rem 1.7rem;margin-top:2.2rem;font-family:var(--mono);
     font-size:var(--mono-s);letter-spacing:.15em;color:var(--mist)}
  .linky{background:none;border:none;font:inherit;letter-spacing:inherit;color:var(--amber);cursor:pointer;
     border-bottom:1px dashed rgba(242,176,74,.6);padding:0;transition:color .3s}
  .linky:hover{color:var(--amber-hi)}
  .descend{position:absolute;left:max(4vw,calc((100vw - 1120px)/2));bottom:30px;z-index:4;
     font-family:var(--mono);font-size:var(--mono-s);letter-spacing:.22em;color:var(--mist);
     text-decoration:none;animation:bob 2.6s ease-in-out infinite;transition:color .3s}
  .descend:hover{color:var(--amber-hi)}
  @keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(7px)}}
  @media(max-width:760px){.station{right:-8vw;width:210px;opacity:.55}.lamp-copy{padding-right:1rem}}

  /* ================= SECTIONS ================= */
  section{padding:110px 0}
  .sechead{margin-bottom:3.4rem;max-width:740px}
  .kick{font-family:var(--mono);font-size:var(--mono-s);letter-spacing:.26em;color:var(--amber);
     display:flex;align-items:center;gap:.9rem}
  .kick::before{content:"";width:36px;height:1px;background:var(--amber)}
  h2{font-size:clamp(1.9rem,4vw,3rem);line-height:1.05;margin:.8rem 0 1.1rem;font-weight:600}
  .lead{color:var(--mist);font-size:1.05rem;max-width:64ch}

  /* reveal */
  .js .rv{opacity:0;transform:translateY(28px);transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1)}
  .js .rv.in{opacity:1;transform:none}

  /* ================= INSTRUMENTS ================= */
  .gauges{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}
  .g{background:var(--card);border:1px solid var(--line);padding:22px 24px;position:relative;
     transition:transform .45s cubic-bezier(.2,.8,.2,1),border-color .45s,box-shadow .45s}
  .g:hover{transform:translateY(-4px);border-color:rgba(242,176,74,.5);box-shadow:0 20px 44px -24px rgba(0,0,0,.85)}
  .g::after{content:attr(data-i);position:absolute;top:14px;right:16px;font-family:var(--mono);
     font-size:10px;color:rgba(157,178,182,.45);letter-spacing:.1em}
  .g-k{font-family:var(--mono);font-size:10px;letter-spacing:.24em;color:var(--mist);margin-bottom:1rem}
  .g-note{font-family:var(--mono);font-size:11px;color:var(--mist);margin-top:.8rem;letter-spacing:.06em}
  .big{font-family:var(--mono);font-size:clamp(2rem,3.6vw,2.9rem);letter-spacing:.02em}
  .big small{font-size:.45em;color:var(--mist);letter-spacing:.15em}
  .g-tide{grid-column:span 6}
  #tideC{width:100%;height:160px;display:block}
  .g-clock,.g-moon,.g-wind{grid-column:span 2}
  .g-baro,.g-vis{grid-column:span 3}
  .g-moon .mrow{display:grid;grid-template-columns:auto 1fr;gap:1.2rem;align-items:center}
  #moonC{width:110px;height:110px;display:block}
  .g-wind svg{width:100%;max-width:210px;display:block;margin:0 auto}
  .needle{transition:transform 1s cubic-bezier(.3,1.5,.4,1);transform-origin:50px 55px}
  @media(max-width:900px){.g-clock,.g-moon,.g-wind,.g-baro,.g-vis{grid-column:span 3}}
  @media(max-width:560px){.gauges>*{grid-column:span 6}}

  /* ================= LOG ================= */
  .log-wrap{display:grid;grid-template-columns:5fr 7fr;gap:4rem;align-items:start}
  .log-side{position:sticky;top:100px}
  .log-side p{color:var(--mist);margin-bottom:1.6rem;max-width:44ch}
  #logForm{display:flex;flex-direction:column;gap:.8rem}
  #logInput{width:100%;background:rgba(255,255,255,.02);border:1px solid var(--line);color:var(--foam);
     padding:14px 16px;font:1.02rem var(--serif);transition:border-color .3s}
  #logInput:focus{outline:none;border-color:var(--amber)}
  #logInput::placeholder{color:rgba(157,178,182,.6);font-style:italic}
  .btn{font-family:var(--mono);font-size:11px;letter-spacing:.2em;background:var(--amber);color:#171004;
     border:none;padding:14px 22px;cursor:pointer;transition:background .3s,transform .15s;align-self:flex-start}
  .btn:hover{background:var(--amber-hi)} .btn:active{transform:scale(.96)}
  .btn.ghost{background:transparent;color:var(--amber);border:1px solid rgba(242,176,74,.55);margin-top:1.3rem}
  .btn.ghost:hover{background:rgba(242,176,74,.09)}
  .fine{font-family:var(--mono);font-size:10px;letter-spacing:.14em;color:rgba(157,178,182,.65);margin-top:1.6rem;line-height:1.9}
  .entries{list-style:none;display:flex;flex-direction:column;gap:1.1rem}
  .entry{border-left:2px solid rgba(183,138,78,.55);padding:.95rem 1.3rem;
     background:linear-gradient(90deg,rgba(255,255,255,.025),transparent 65%);transition:border-color .3s}
  .entry:hover{border-color:var(--amber)}
  .entry .stamp{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.22em;color:var(--amber);margin-bottom:.4rem}
  .entry p{font-size:1.07rem}
  .entry.fresh{animation:entryin .7s cubic-bezier(.2,.9,.3,1)}
  .entry.fresh .stamp{animation:stampin .55s .15s both cubic-bezier(.2,1.4,.4,1)}
  @keyframes entryin{from{opacity:0;transform:translateX(28px)}}
  @keyframes stampin{from{opacity:0;transform:scale(1.7) rotate(-8deg)}}
  @media(max-width:900px){.log-wrap{grid-template-columns:1fr}.log-side{position:static}}

  /* ================= PLATES ================= */
  .plates{display:grid;grid-template-columns:repeat(12,1fr);gap:2.4rem 1.6rem;align-items:start}
  .plate{background:#0a1420;border:1px solid var(--line);padding:10px 10px 6px;position:relative;
     transform:rotate(var(--r,0deg)) translateY(var(--ty,0));
     box-shadow:0 24px 48px -28px rgba(0,0,0,.9);
     transition:transform .55s cubic-bezier(.2,.8,.2,1),box-shadow .55s}
  .plate:hover{transform:rotate(0deg) translateY(-10px);box-shadow:0 36px 64px -30px rgba(0,0,0,1);z-index:2}
  .plate canvas{display:block;width:100%;height:auto}
  .plate figcaption{font-family:var(--mono);font-size:10px;letter-spacing:.16em;color:var(--mist);
     padding:12px 4px 6px;display:flex;justify-content:space-between;gap:.8rem}
  .plate figcaption b{color:var(--amber);font-weight:400}
  .p1{grid-column:1/4;--r:-3deg}
  .p2{grid-column:4/7;--r:2deg;--ty:3rem}
  .p3{grid-column:7/10;--r:-2deg;--ty:.8rem}
  .p4{grid-column:2/5;--r:2.5deg}
  .p5{grid-column:6/9;--r:-1.5deg;--ty:2.4rem}
  .plateq{grid-column:9/13;--ty:3.4rem;padding-top:.6rem}
  .plateq blockquote{font-size:clamp(1.3rem,2.2vw,1.7rem);font-style:italic;line-height:1.45}
  .plateq cite{display:block;margin-top:1.2rem;font-family:var(--mono);font-style:normal;font-size:10px;
     letter-spacing:.22em;color:var(--mist)}
  @media(max-width:900px){.plates>*{grid-column:span 6!important;--ty:0rem}}
  @media(max-width:560px){.plates>*{grid-column:span 12!important}}

  /* ================= NOTES ================= */
  .notes{border-bottom:1px solid var(--line)}
  .note{display:grid;grid-template-columns:110px 1fr;gap:1.6rem;padding:1.6rem 0;border-top:1px solid var(--line);align-items:baseline}
  .note time{font-family:var(--mono);font-size:11px;letter-spacing:.2em;color:var(--amber)}
  .note p{font-size:clamp(1.1rem,2vw,1.45rem);font-style:italic;max-width:62ch}
  .mask{display:block;overflow:hidden}
  .js .note .mask span{display:block;transform:translateY(115%);transition:transform .85s .1s cubic-bezier(.2,.75,.2,1)}
  .js .note.in .mask span{transform:none}
  @media(max-width:560px){.note{grid-template-columns:1fr;gap:.4rem}}

  /* ================= FOOTER ================= */
  footer{border-top:1px solid var(--line);padding:100px 0 70px;margin-top:40px}
  .farline{font-size:clamp(2rem,5vw,3.6rem);line-height:1.12;max-width:20ch}
  .colophon{display:grid;grid-template-columns:1.4fr 1fr;gap:3rem;margin-top:3.2rem}
  .colophon p{color:var(--mist);max-width:58ch}
  .manifest{list-style:none;font-family:var(--mono);font-size:11px;letter-spacing:.14em;color:var(--mist)}
  .manifest li{display:flex;justify-content:space-between;gap:1rem;padding:.55rem 0;border-bottom:1px dotted rgba(157,178,182,.3)}
  .manifest li b{color:var(--amber);font-weight:400}
  #nightsEl{margin-top:3rem;font-family:var(--mono);font-size:12px;letter-spacing:.2em;color:var(--amber)}
  .signoff{margin-top:.6rem;font-style:italic;font-size:1.2rem}
  .backtop{display:inline-block;margin-top:2.4rem;font-family:var(--mono);font-size:11px;letter-spacing:.22em;
     color:var(--mist);text-decoration:none;border-bottom:1px dashed rgba(157,178,182,.4);padding-bottom:2px;transition:color .3s}
  .backtop:hover{color:var(--amber-hi)}
  @media(max-width:760px){.colophon{grid-template-columns:1fr}}
  a:focus-visible,button:focus-visible,input:focus-visible{outline:2px solid var(--amber);outline-offset:3px}

  @media (prefers-reduced-motion: reduce){
    *,*::before,*::after{animation:none!important;transition:none!important}
    .rotor{transform:rotate(-155deg)}
    .js .rv{opacity:1;transform:none}
    .js .note .mask span{transform:none}
  }
</style>
</head>
<body>
<div class="grain" aria-hidden="true"></div>

<header class="topbar" id="topbar">
  <a class="brand" href="#top">FRONT POINT LIGHT <span>· STATION VII</span></a>
  <nav aria-label="Station">
    <a href="#readings">READINGS</a><a href="#log">LOG</a><a href="#plates">PLATES</a><a href="#notes">NOTES</a>
  </nav>
  <div id="chipClock" aria-hidden="true">--:--:--</div>
</header>

<!-- ============ THE LAMP ROOM ============ -->
<section class="lamp" id="top">
  <canvas id="sky" aria-hidden="true"></canvas>
  <div class="dim" aria-hidden="true"></div>

  <div class="station" id="station" aria-hidden="true">
    <div class="beam"><div class="rotor">
      <div class="w"></div><div class="w w2"></div>
      <div class="glowp"></div>
    </div></div>
    <svg viewBox="0 0 200 470">
      <defs><radialGradient id="lg" cx="50%" cy="45%" r="60%">
        <stop offset="0" stop-color="#ffe9b0"/><stop offset=".55" stop-color="#f2b04a"/><stop offset="1" stop-color="#8a5a1d"/>
      </radialGradient></defs>
      <path d="M24 470 Q40 428 74 430 L84 410 Q100 402 116 410 L126 430 Q160 426 176 470 Z" fill="#08111d"/>
      <polygon points="82,150 118,150 130,455 70,455" fill="#0d1b2c" stroke="rgba(220,235,235,.16)"/>
      <polygon points="79.6,210 120.4,210 121.6,242 78.4,242" fill="#d99a45" opacity=".85"/>
      <polygon points="76.2,300 123.8,300 125,332 75,332" fill="#d99a45" opacity=".85"/>
      <path d="M93 455 v-26 a7 7 0 0 1 14 0 v26 z" fill="#071019" stroke="rgba(242,176,74,.35)"/>
      <rect x="96" y="256" width="8" height="16" rx="4" fill="#071019" stroke="rgba(220,235,235,.15)"/>
      <g stroke="rgba(220,235,235,.3)" stroke-width="1.4">
        <line x1="70" y1="138" x2="70" y2="126"/><line x1="82" y1="138" x2="82" y2="126"/>
        <line x1="100" y1="138" x2="100" y2="126"/><line x1="118" y1="138" x2="118" y2="126"/>
        <line x1="130" y1="138" x2="130" y2="126"/><line x1="66" y1="127" x2="134" y2="127"/>
      </g>
      <rect x="64" y="138" width="72" height="12" fill="#0a1624" stroke="rgba(220,235,235,.18)"/>
      <rect x="84" y="104" width="32" height="36" fill="#0c1826" stroke="rgba(220,235,235,.2)"/>
      <rect class="flame" x="89" y="110" width="22" height="24" fill="url(#lg)"/>
      <path d="M82 104 Q100 80 118 104 Z" fill="#0a1624" stroke="rgba(220,235,235,.18)"/>
      <line x1="100" y1="82" x2="100" y2="68" stroke="rgba(242,176,74,.7)" stroke-width="2"/>
      <circle cx="100" cy="65" r="3.2" fill="#f2b04a"/>
    </svg>
  </div>

  <div class="lamp-copy">
    <p class="overline">51°14′ N · 4°02′ W — ESTABLISHED TONIGHT — CHARACTER: FL(1) 6s</p>
    <h1 class="title" id="title" data-text="THE KEEPER'S LOG">THE KEEPER'S LOG</h1>
    <p class="stand">This page is a lighthouse, and I keep it. No brief, no cargo, nothing fetched from
      anywhere — just a lamp, a log, and the water. You've come in out of the dark: sign the log,
      check the instruments, or simply watch the beam go round.</p>
    <div class="metarow">
      <span>RANGE — 21 NM</span><span>FOG SIGNAL — BELL</span><span>WATCH — ON</span>
      <button class="linky" id="lampBtn" aria-pressed="false">LAMP: FULL</button>
    </div>
  </div>
  <a class="descend" href="#readings">DOWN THE TOWER ↓</a>
</section>

<!-- ============ READINGS ============ -->
<section id="readings">
  <div class="wrap">
    <header class="sechead rv">
      <p class="kick">THE INSTRUMENT BOARD</p>
      <h2>Tonight's readings</h2>
      <p class="lead">Nothing here is measured properly. The tide keeps its own clock, the wind reports
      only what it feels like, and the moon alone is real — everything else is drawn from memory.
      Check them anyway. Checking is the job.</p>
    </header>
    <div class="gauges">
      <div class="g g-tide rv" data-i="01">
        <div class="g-k">TIDE · SEMIDIURNAL</div>
        <canvas id="tideC"></canvas>
        <div class="g-note" id="tideNote">—</div>
      </div>
      <div class="g g-clock rv" data-i="02">
        <div class="g-k">SHIP'S TIME</div>
        <div class="big" id="bigClock">--:--:--</div>
        <div class="g-note" id="dateNote">—</div>
      </div>
      <div class="g g-moon rv" data-i="03">
        <div class="mrow">
          <canvas id="moonC" width="110" height="110" role="img" aria-label="Current moon phase"></canvas>
          <div><div class="g-k">MOON</div><div class="big" style="font-size:1.15rem" id="moonName">—</div>
          <div class="g-note" id="moonPct">—</div></div>
        </div>
      </div>
      <div class="g g-wind rv" data-i="04">
        <div class="g-k">WIND</div>
        <svg viewBox="0 0 100 62" aria-hidden="true">
          <path d="M11.9 33 A44 44 0 0 1 88.1 33" fill="none" stroke="rgba(157,178,182,.4)" stroke-width="1"/>
          <g stroke="rgba(157,178,182,.55)" stroke-width="1.2">
            <line x1="17.1" y1="36" x2="11.9" y2="33"/><line x1="31" y1="22.1" x2="28" y2="16.9"/>
            <line x1="50" y1="17" x2="50" y2="11"/><line x1="69" y1="22.1" x2="72" y2="16.9"/>
            <line x1="82.9" y1="36" x2="88.1" y2="33"/>
          </g>
          <g class="needle" id="needleG"><line x1="50" y1="55" x2="50" y2="14" stroke="#f2b04a" stroke-width="2"/>
          <circle cx="50" cy="55" r="3.4" fill="#f2b04a"/></g>
        </svg>
        <div class="g-note"><span id="windKts">—</span> kts · <span id="windDir">—</span></div>
      </div>
      <div class="g g-baro rv" data-i="05">
        <div class="g-k">BAROMETER</div>
        <div class="big" id="baroV">— <small>hPa</small></div>
        <div class="g-note">glass <span id="baroT">steady</span></div>
      </div>
      <div class="g g-vis rv" data-i="06">
        <div class="g-k">VISIBILITY</div>
        <div class="big">21 <small>NAUTICAL MILES</small></div>
        <div class="g-note">haze thinning after midnight · the dark is negotiable</div>
      </div>
    </div>
  </div>
</section>

<!-- ============ LOG ============ -->
<section id="log">
  <div class="wrap log-wrap">
    <div class="log-side rv">
      <p class="kick">THE WATCH LOG</p>
      <h2>Sign the log</h2>
      <p>A light is only real once it has been seen. Leave a line for the next ship — weather, cargo,
      state of mind. Entries are kept in this browser's hold; at this station, nothing leaves the shore.</p>
      <form id="logForm">
        <label for="logInput" class="mono" style="font-size:10px;letter-spacing:.22em;color:var(--mist)">YOUR ENTRY</label>
        <input id="logInput" maxlength="160" autocomplete="off"
          placeholder="e.g. Passed at 02:14, sea calm, lamp bright.">
        <button class="btn" type="submit">ENTER IN THE LOG</button>
      </form>
      <button class="btn ghost" id="bellBtn" type="button">◉ &nbsp;SOUND THE FOG BELL</button>
      <p class="fine">EVERY LINE STAMPED IN SHIP'S TIME.<br>THE BELL IS SYNTHESIZED ON THE SPOT — SOUND ON, IF YOU LIKE.</p>
    </div>
    <ol class="entries rv" id="logList" aria-label="Watch log entries"></ol>
  </div>
</section>

<!-- ============ PLATES ============ -->
<section id="plates">
  <div class="wrap">
    <header class="sechead rv">
      <p class="kick">PLATES FROM THE DARK</p>
      <h2>Views from the gallery</h2>
      <p class="lead">Drawings made by the lamp while the kettle was on. Five views of the same water —
      none of them accurate, all of them true. Hang one in your mind on the way out.</p>
    </header>
    <div class="plates">
      <figure class="plate p1 rv"><canvas class="pcv" data-seed="11"></canvas>
        <figcaption><b>PLATE I</b><span>FIRST LIGHT OVER THE SHOAL</span></figcaption></figure>
      <figure class="plate p2 rv"><canvas class="pcv" data-seed="23"></canvas>
        <figcaption><b>PLATE II</b><span>RAIN LINE APPROACHING</span></figcaption></figure>
      <figure class="plate p3 rv"><canvas class="pcv" data-seed="37"></canvas>
        <figcaption><b>PLATE III</b><span>TWO BOATS, RUNNING DARK</span></figcaption></figure>
      <figure class="plate p4 rv"><canvas class="pcv" data-seed="49"></canvas>
        <figcaption><b>PLATE IV</b><span>THE MOON'S REPLY</span></figcaption></figure>
      <figure class="plate p5 rv"><canvas class="pcv" data-seed="58"></canvas>
        <figcaption><b>PLATE V</b><span>GREEN WATER, GOLD HOUR</span></figcaption></figure>
      <div class="plateq rv">
        <blockquote>“The sea declines all corrections, and the beam apologizes to no one.”</blockquote>
        <cite>— LOG, UNDATED</cite>
      </div>
    </div>
  </div>
</section>

<!-- ============ NOTES ============ -->
<section id="notes">
  <div class="wrap">
    <header class="sechead rv">
      <p class="kick">NOTES FROM THE SMALL HOURS</p>
      <h2>What the watch teaches</h2>
      <p class="lead">Marginalia from the long watches. Nothing here is advice; it's only what the hours
      said when they passed.</p>
    </header>
    <div class="notes">
      <div class="note rv"><time>23:59</time><p class="mask"><span>A front page doesn't have to answer anything. Sometimes a light is just a light, kept.</span></p></div>
      <div class="note rv"><time>01:17</time><p class="mask"><span>Visitors are ships. You don't steer them; you stand where you can be seen.</span></p></div>
      <div class="note rv"><time>02:02</time><p class="mask"><span>No cargo: this page carries nothing fetched from anywhere. Every star was made on site.</span></p></div>
      <div class="note rv"><time>02:48</time><p class="mask"><span>If the file opens, the lamp works. That is the whole maintenance plan.</span></p></div>
      <div class="note rv"><time>03:33</time><p class="mask"><span>Keep the glass clean. Clarity is a kind of hospitality.</span></p></div>
      <div class="note rv"><time>04:12</time><p class="mask"><span>Somewhere the real sea is doing this. This page is my rehearsal for noticing.</span></p></div>
    </div>
  </div>
</section>

<!-- ============ FOOTER ============ -->
<footer>
  <div class="wrap">
    <p class="farline rv">Keep a light where you are.</p>
    <div class="colophon rv">
      <p>Built by hand as a single file. The moon is arithmetic, the tide is a sine, the bell is
      synthesized, and every star on this page was drawn on site. Nothing here was loaded from
      anywhere else — no cargo, no wires, no clocks but your own.</p>
      <ul class="manifest">
        <li>CREW <b>ONE KEEPER</b></li>
        <li>CARGO <b>NONE</b></li>
        <li>EXTERNAL REQUESTS <b>ZERO</b></li>
        <li>FONTS <b>WHATEVER YOUR SHIP CARRIES</b></li>
        <li>MOON <b>COMPUTED LIVE</b></li>
      </ul>
    </div>
    <p id="nightsEl">THE LAMP IS LIT. COMPANY WELCOME.</p>
    <p class="signoff">— the keeper, Front Point</p>
    <a class="backtop" href="#top">↑ BACK TO THE LAMP</a>
  </div>
</footer>

<noscript><style>.rv{opacity:1!important;transform:none!important}.note .mask span{transform:none!important}</style></noscript>

<script>
(function(){
"use strict";
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
const p2=n=>String(n).padStart(2,'0');

/* ---------- clocks ---------- */
const chip=$('#chipClock'), big=$('#bigClock');
function tick(){const d=new Date(),s=p2(d.getHours())+':'+p2(d.getMinutes())+':'+p2(d.getSeconds());
  chip.textContent=s; big.textContent=s;}
tick(); setInterval(tick,1000);
$('#dateNote').textContent=new Date().toLocaleDateString('en-GB',{weekday:'long',day:'numeric',month:'long'});

/* ---------- moon ---------- */
const SYN=29.530588853, NM=Date.UTC(2000,0,6,18,14,0);
const age=((((Date.now()-NM)/864e5)%SYN)+SYN)%SYN;
const illum=Math.round((1-Math.cos(2*Math.PI*age/SYN))*50);
function moonName(a){if(a<1.85)return'New Moon';if(a<5.54)return'Waxing Crescent';if(a<9.23)return'First Quarter';
 if(a<12.92)return'Waxing Gibbous';if(a<16.61)return'Full Moon';if(a<20.3)return'Waning Gibbous';
 if(a<23.99)return'Last Quarter';if(a<27.68)return'Waning Crescent';return'New Moon';}
$('#moonName').textContent=moonName(age);
$('#moonPct').textContent=illum+'% ILLUMINATED · DAY '+(Math.round(age*10)/10)+' OF 29.5';
function drawMoon(ctx,x,y,r){
  const ph=age/SYN, e=Math.cos(2*Math.PI*ph)*r;
  ctx.save();
  const g=ctx.createRadialGradient(x,y,r*.3,x,y,r*2.6);
  g.addColorStop(0,'rgba(244,234,210,.22)');g.addColorStop(1,'rgba(244,234,210,0)');
  ctx.fillStyle=g;ctx.beginPath();ctx.arc(x,y,r*2.6,0,7);ctx.fill();
  ctx.fillStyle='#18263c';ctx.beginPath();ctx.arc(x,y,r,0,7);ctx.fill();
  ctx.fillStyle='#f4ead2';ctx.beginPath();
  if(ph<.5){ctx.arc(x,y,r,-Math.PI/2,Math.PI/2);ctx.ellipse(x,y,Math.abs(e),r,0,Math.PI/2,-Math.PI/2,e>0);}
  else{ctx.arc(x,y,r,Math.PI/2,Math.PI*1.5);ctx.ellipse(x,y,Math.abs(e),r,0,Math.PI*1.5,Math.PI/2,e>0);}
  ctx.closePath();ctx.fill();
  ctx.fillStyle='rgba(20,30,50,.18)';
  [[.3,-.2,.16],[-.2,.25,.12],[.1,.4,.09],[-.3,-.35,.08]].forEach(c=>{
    ctx.beginPath();ctx.arc(x+c[0]*r,y+c[1]*r,c[2]*r,0,7);ctx.fill();});
  ctx.restore();
}
(function(){const c=$('#moonC'),ctx=c.getContext('2d');ctx.clearRect(0,0,110,110);drawMoon(ctx,55,55,34);})();

/* ---------- sky / sea canvas ---------- */
const sky=$('#sky'), sc=sky.getContext('2d');
let SW=0,SH=0,stars=[],meteor=null,mTimer=5;
function sizeSky(){
  const dpr=Math.min(devicePixelRatio||1,2), r=sky.parentElement.getBoundingClientRect();
  SW=r.width;SH=r.height;sky.width=SW*dpr;sky.height=SH*dpr;sc.setTransform(dpr,0,0,dpr,0,0);
  const n=Math.max(90,Math.min(220,Math.floor(SW*SH/9000)));stars=[];
  for(let i=0;i<n;i++)stars.push({x:Math.random()*SW,y:Math.random()*SH*.72,r:.4+Math.random()*1.1,
    p:Math.random()*6.28,s:.5+Math.random()*1.4});
}
function drawScene(t){
  const hor=SH*.8;
  const g=sc.createLinearGradient(0,0,0,hor);
  g.addColorStop(0,'#04080f');g.addColorStop(.6