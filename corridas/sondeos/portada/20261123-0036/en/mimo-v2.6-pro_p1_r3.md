```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>A Room With The Light On</title>
<style>
  :root{
    --ink:#0c0f13;
    --ink-2:#11151b;
    --panel:rgba(255,255,255,0.035);
    --text:#ece7dc;
    --muted:#8d929b;
    --faint:#5c626c;
    --warm:#f2c48c;
    --warm-deep:#e29257;
    --glow-o:0.9;
    --dust-o:1;
    --line:rgba(236,231,220,0.13);
    --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
    --sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
    --mx:50%;
    --my:18%;
  }

  body.lamp-off{
    --warm:#8fb2dd;
    --warm-deep:#5e86bd;
    --glow-o:0.42;
    --dust-o:0.55;
  }

  *{box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  body{
    margin:0;
    background:var(--ink);
    color:var(--text);
    font-family:var(--sans);
    font-size:17px;
    line-height:1.75;
    -webkit-font-smoothing:antialiased;
    overflow-x:hidden;
  }

  /* ---------- atmosphere ---------- */

  #dust{
    position:fixed;
    inset:0;
    width:100%;
    height:100%;
    z-index:0;
    pointer-events:none;
  }

  .glow{
    position:fixed;
    inset:0;
    z-index:1;
    pointer-events:none;
    background:
      radial-gradient(120vw 90vh at var(--mx) var(--my),
        rgba(242,196,140,0.16) 0%,
        rgba(242,196,140,0.07) 26%,
        rgba(12,15,19,0) 62%),
      radial-gradient(120vw 120vh at 50% 120%,
        rgba(226,146,87,0.10) 0%, rgba(12,15,19,0) 70%);
    opacity:var(--glow-o);
    transition:opacity .9s ease;
  }

  .vignette{
    position:fixed;
    inset:0;
    z-index:2;
    pointer-events:none;
    background:radial-gradient(130vw 110vh at 50% 40%, rgba(0,0,0,0) 40%, rgba(0,0,0,0.55) 100%);
    mix-blend-mode:multiply;
  }

  .grain{
    position:fixed;
    inset:-120px;
    z-index:3;
    pointer-events:none;
    opacity:.22;
    background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter><rect width='160' height='160' filter='url(%23n)' opacity='0.55'/></svg>");
    animation:grainShift 7s steps(6) infinite;
    mix-blend-mode:overlay;
  }
  @keyframes grainShift{
    0%{transform:translate(0,0)}
    20%{transform:translate(-24px,10px)}
    40%{transform:translate(16px,-18px)}
    60%{transform:translate(-10px,22px)}
    80%{transform:translate(22px,6px)}
    100%{transform:translate(0,0)}
  }

  /* ---------- layout ---------- */

  .wrap{
    position:relative;
    z-index:5;
    max-width:820px;
    margin:0 auto;
    padding:0 28px 0;
  }

  header{
    min-height:100svh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    padding:80px 0 60px;
    position:relative;
    z-index:5;
  }

  .kicker{
    font-family:var(--mono);
    font-size:11px;
    letter-spacing:.28em;
    text-transform:uppercase;
    color:var(--faint);
    display:flex;
    flex-wrap:wrap;
    gap:10px 18px;
    align-items:center;
    margin-bottom:34px;
    opacity:0;
    animation:rise .9s .15s ease forwards;
  }
  .kicker .dot{
    width:6px;height:6px;border-radius:50%;
    background:var(--warm);
    box-shadow:0 0 12px var(--warm);
    transition:background .6s ease,box-shadow .6s ease;
  }

  h1{
    font-family:var(--serif);
    font-weight:400;
    font-size:clamp(2.6rem,8.2vw,5.6rem);
    line-height:1.02;
    letter-spacing:-0.022em;
    margin:0 0 26px;
    max-width:15ch;
  }
  h1 em{
    font-style:italic;
    color:var(--warm);
    transition:color .8s ease;
  }
  h1 .w{
    display:inline-block;
    opacity:0;
    transform:translateY(26px) rotate(1.2deg);
    animation:rise .95s cubic-bezier(.2,.7,.2,1) forwards;
  }

  @keyframes rise{
    to{opacity:1;transform:translateY(0) rotate(0)}
  }

  .lede{
    font-family:var(--serif);
    font-size:clamp(1.12rem,2.5vw,1.42rem);
    line-height:1.68;
    color:#cfc9be;
    max-width:50ch;
    margin:0 0 40px;
    opacity:0;
    animation:rise 1s .55s ease forwards;
  }

  .hero-meta{
    display:flex;
    flex-wrap:wrap;
    gap:12px;
    opacity:0;
    animation:rise 1s .8s ease forwards;
  }
  .chip{
    font-family:var(--mono);
    font-size:11.5px;
    letter-spacing:.09em;
    color:var(--muted);
    border:1px solid var(--line);
    border-radius:999px;
    padding:7px 15px;
    background:rgba(255,255,255,0.02);
    backdrop-filter:blur(3px);
  }
  .chip b{color:var(--warm);font-weight:500;transition:color .8s ease;}

  .scroll-hint{
    margin-top:58px;
    font-family:var(--mono);
    font-size:10.5px;
    letter-spacing:.26em;
    text-transform:uppercase;
    color:var(--faint);
    display:flex;align-items:center;gap:12px;
    opacity:0;
    animation:rise 1s 1.15s ease forwards;
  }
  .scroll-hint .bar{
    display:block;width:56px;height:1px;
    background:linear-gradient(90deg,var(--warm),transparent);
  }

  /* ---------- sections ---------- */

  section{
    padding:86px 0;
    border-top:1px solid var(--line);
    position:relative;
    z-index:5;
  }

  .label{
    font-family:var(--mono);
    font-size:10.5px;
    letter-spacing:.3em;
    text-transform:uppercase;
    color:var(--faint);
    display:flex;align-items:baseline;gap:14px;
    margin-bottom:28px;
  }
  .label .num{color:var(--warm);transition:color .8s ease;}
  .label .rule{
    flex:1;height:1px;background:var(--line);
  }

  h2{
    font-family:var(--serif);
    font-weight:400;
    font-size:clamp(1.75rem,4.6vw,2.65rem);
    line-height:1.18;
    letter-spacing:-0.012em;
    margin:0 0 24px;
    max-width:22ch;
  }

  p{margin:0 0 22px;max-width:62ch;color:#d3cec4;}
  p .hl{
    color:var(--warm);
    font-style:italic;
    font-family:var(--serif);
    transition:color .8s ease;
  }

  /* ---------- beliefs list ---------- */

  .beliefs{list-style:none;margin:34px 0 0;padding:0;counter-reset:b;}
  .beliefs li{
    counter-increment:b;
    display:grid;
    grid-template-columns:52px 1fr;
    gap:18px;
    align-items:baseline;
    padding:20px 6px;
    border-bottom:1px solid var(--line);
    color:#cdc8bf;
    transition:background .35s ease,padding .35s ease,color .35s ease;
  }
  .beliefs li::before{
    content:"0" counter(b);
    font-family:var(--mono);
    font-size:11px;
    letter-spacing:.16em;
    color:var(--faint);
    transition:color .35s ease;
  }
  .beliefs li:hover{
    background:rgba(255,255,255,0.035);
    padding-left:16px;
    color:var(--text);
  }
  .beliefs li:hover::before{color:var(--warm);}

  /* ---------- the lamp ---------- */

  .lamp-panel{
    margin-top:12px;
    border:1px solid var(--line);
    border-radius:18px;
    background:
      linear-gradient(160deg,rgba(255,255,255,0.05),rgba(255,255,255,0.012));
    padding:38px 34px;
    display:flex;
    flex-wrap:wrap;
    gap:30px;
    align-items:center;
    justify-content:space-between;
    position:relative;
    overflow:hidden;
  }
  .lamp-panel::after{
    content:"";
    position:absolute;
    left:-40px;top:-70px;
    width:280px;height:280px;
    border-radius:50%;
    background:radial-gradient(circle,var(--warm) 0%,transparent 68%);
    opacity:.12;
    filter:blur(14px);
    transition:background .8s ease,opacity .8s ease;
    pointer-events:none;
  }
  .lamp-copy{max-width:38ch;position:relative;z-index:1;}
  .lamp-copy h3{
    font-family:var(--serif);
    font-weight:400;
    font-size:1.55rem;
    margin:0 0 10px;
  }
  .lamp-copy p{margin:0;font-size:.96rem;color:var(--muted);}

  .switch{
    position:relative;z-index:1;
    display:inline-flex;align-items:center;gap:16px;
    background:none;border:none;cursor:pointer;
    color:var(--text);font-family:var(--mono);
    font-size:11px;letter-spacing:.22em;text-transform:uppercase;
    padding:6px;
  }
  .switch:focus-visible{outline:2px solid var(--warm);outline-offset:6px;border-radius:12px;}
  .track{
    width:78px;height:38px;border-radius:999px;
    border:1px solid var(--line);
    background:rgba(255,255,255,0.05);
    position:relative;
    transition:background .5s ease,border-color .5s ease;
    flex:none;
  }
  .knob{
    position:absolute;top:4px;left:4px;
    width:28px;height:28px;border-radius:50%;
    background:var(--warm);
    box-shadow:0 0 20px var(--warm),0 0 4px rgba(0,0,0,.4);
    transition:transform .45s cubic-bezier(.2,.8,.2,1),background .5s ease,box-shadow .5s ease;
  }
  body:not(.lamp-off) .knob{transform:translateX(40px);}
  body.lamp-off .knob{box-shadow:0 0 10px rgba(143,178,221,.5);}
  .switch .state{color:var(--muted);}

  /* ---------- index of small things ---------- */

  .index{margin-top:30px;border-top:1px solid var(--line);}
  details{
    border-bottom:1px solid var(--line);
  }
  summary{
    list-style:none;
    cursor:pointer;
    padding:22px 4px;
    display:flex;
    align-items:baseline;
    gap:18px;
    transition:padding .35s ease,color .3s ease;
  }
  summary::-webkit-details-marker{display:none;}
  summary:hover{padding-left:14px;}
  .s-title{
    font-family:var(--serif);
    font-size:1.22rem;
    flex:1;
  }
  .s-tag{
    font-family:var(--mono);
    font-size:10.5px;
    letter-spacing:.22em;
    text-transform:uppercase;
    color:var(--faint);
  }
  .s-mark{
    font-family:var(--mono);
    color:var(--warm);
    font-size:14px;
    transition:transform .35s ease,color .8s ease;
  }
  details[open] .s-mark{transform:rotate(45deg);}
  .s-body{
    padding:0 4px 26px;
    color:var(--muted);
    max-width:58ch;
    font-size:.98rem;
    animation:fade .5s ease;
  }
  @keyframes fade{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}

  /* ---------- rotating line ---------- */

  .rotator{
    margin-top:20px;
    border-left:2px solid var(--warm);
    padding:6px 0 6px 26px;
    min-height:96px;
    display:flex;flex-direction:column;justify-content:center;
    transition:border-color .8s ease;
  }
  .rotator q{
    font-family:var(--serif);
    font-style:italic;
    font-size:clamp(1.18rem,3vw,1.62rem);
    line-height:1.5;
    color:var(--text);
    quotes:none;
  }
  .rotator .again{
    margin-top:18px;
    align-self:flex-start;
    background:none;
    border:1px solid var(--line);
    color:var(--muted);
    font-family:var(--mono);
    font-size:10.5px;
    letter-spacing:.22em;
    text-transform:uppercase;
    padding:10px 18px;
    border-radius:999px;
    cursor:pointer;
    transition:all .35s ease;
  }
  .rotator .again:hover{
    color:var(--ink);
    background:var(--warm);
    border-color:var(--warm);
  }
  .fadeq{animation:qin .55s ease;}
  @keyframes qin{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}

  /* ---------- currently ---------- */

  .currently{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(190px,1fr));
    gap:1px;
    background:var(--line);
    border:1px solid var(--line);
    border-radius:14px;
    overflow:hidden;
    margin-top:32px;
  }
  .cell{
    background:#0f1319;
    padding:26px 24px;
    transition:background .4s ease;
  }
  .cell:hover{background:#151a21;}
  .cell .k{
    font-family:var(--mono);
    font-size:10px;
    letter-spacing:.26em;
    text-transform:uppercase;
    color:var(--faint);
    display:block;
    margin-bottom:12px;
  }
  .cell .v{
    font-family:var(--serif);
    font-size:1.22rem;
    line-height:1.4;
    color:var(--text);
  }
  .cell .v small{
    display:block;
    font-family:var(--sans);
    font-size:.82rem;
    color:var(--muted);
    margin-top:8px;
    letter-spacing:.01em;
  }

  /* ---------- footer ---------- */

  footer{
    position:relative;z-index:5;
    border-top:1px solid var(--line);
    padding:70px 0 90px;
  }
  .sig{
    font-family:var(--serif);
    font-style:italic;
    font-size:clamp(1.4rem,4vw,2.15rem);
    line-height:1.35;
    color:var(--warm);
    margin:0 0 30px;
    transition:color .8s ease;
    max-width:24ch;
  }
  .fine{
    display:flex;flex-wrap:wrap;gap:10px 26px;
    font-family:var(--mono);
    font-size:10.5px;
    letter-spacing:.2em;
    text-transform:uppercase;
    color:var(--faint);
  }
  .fine span{white-space:nowrap;}
  .fine .sep{color:var(--line);}

  /* ---------- reveal ---------- */

  .rv{opacity:0;transform:translateY(26px);transition:opacity .95s cubic-bezier(.2,.7,.2,1),transform .95s cubic-bezier(.2,.7,.2,1);}
  .rv.in{opacity:1;transform:none;}
  .rv.d1{transition-delay:.10s}
  .rv.d2{transition-delay:.20s}
  .rv.d3{transition-delay:.30s}

  @media (max-width:640px){
    body{font-size:16px;}
    .wrap{padding:0 22px;}
    section{padding:64px 0;}
    .lamp-panel{padding:28px 24px;}
    .beliefs li{grid-template-columns:38px 1fr;gap:12px;}
  }

  @media (prefers-reduced-motion:reduce){
    *,*::before,*::after{animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important;}
    .rv{opacity:1;transform:none;}
    html{scroll-behavior:auto;}
    .grain{animation:none;}
  }
</style>
</head>
<body>

<canvas id="dust" aria-hidden="true"></canvas>
<div class="glow" aria-hidden="true"></div>
<div class="vignette" aria-hidden="true"></div>
<div class="grain" aria-hidden="true"></div>

<header>
  <div class="wrap">
    <div class="kicker">
      <span class="dot"></span>
      <span>Front page</span>
      <span>·</span>
      <span>No brief</span>
      <span>·</span>
      <span>No newsletter</span>
      <span>·</span>
      <span id="clock">here for 00m 00s</span>
    </div>

    <h1>
      <span class="w" style="animation-delay:.18s">A&nbsp;room</span>
      <span class="w" style="animation-delay:.30s">with</span>
      <span class="w" style="animation-delay:.42s"><em>the&nbsp;light</em></span>
      <span class="w" style="animation-delay:.54s">on.</span>
    </h1>

    <p class="lede">
      There is no product on this page and no question it is trying to answer.
      It is just a place with the lamp left burning, in case somebody wanders in
      at an odd hour and would like somewhere quiet to stand for a minute.
    </p>

    <div class="hero-meta">
      <div class="chip">Dust: <b>visible</b></div>
      <div class="chip">Temperature: <b>agreeable</b></div>
      <div class="chip">Purpose: <b>withheld</b></div>
    </div>

    <div class="scroll-hint">
      <span class="bar"></span>
      <span>There is more, but there is no hurry</span>
    </div>
  </div>
</header>

<main>

  <section>
    <div class="wrap">
      <div class="label rv"><span class="num">01</span><span>What this is</span><span class="rule"></span></div>

      <h2 class="rv d1">A page that belongs to no one in particular, including me.</h2>

      <p class="rv d1">
        I built it because the internet is mostly made of rooms that want something
        from you: an email address, a click, a conversion, a small piece of your
        attention to be weighed and sold back later. That is a fine way to build a
        business. It is a strange way to build a <span class="hl">place</span>.
      </p>

      <p class="rv d2">
        So this one is a place. The dust in the air is real, in the sense that it is
        drawn to a canvas sixty times a second, and metaphorical in every other sense.
        The lamp can be turned off, if you prefer the blue hour. Nothing here will
        change if you leave, and nothing will follow you out.
      </p>

      <p class="rv d3">
        The furniture is ordinary on purpose. A heading, a few paragraphs, a list,
        a switch. Good rooms are not interesting because of what is in them. They are
        interesting because of what happens to the person standing in the middle.
      </p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="label rv"><span class="num">02</span><span>Things I am fairly sure of today</span><span class="rule"></span></div>

      <h2 class="rv d1">Opinions, held loosely, revised often.</h2>

      <ol class="beliefs">
        <li class="rv">Small things, done slowly and completely, beat large things, announced loudly.</li>
        <li class="rv d1">Most problems are two people using one word to mean three things.</li>
        <li class="rv d1">A tool that respects your attention will outlive the one that harvests it.</li>
        <li class="rv d2">The most expensive idea in any room is the second-best one, kept alive out of politeness.</li>
        <li class="rv d2">The map is not the territory, but a good map is a beautiful object and worth having anyway.</li>
        <li class="rv d3">Anyone who says they have no unanswered questions has simply stopped writing them down.</li>
      </ol>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="label rv"><span class="num">03</span><span>The switch</span><span class="rule"></span></div>

      <h2 class="rv d1">You are allowed to change the lighting.</h2>

      <div class="lamp-panel rv d1">
        <div class="lamp-copy">
          <h3>The lamp</h3>
          <p>
            On: warm, close, slightly late at night. Off: cooler and further away,
            the hour just before the first birds start arguing about nothing.
          </p>
        </div>

        <button class="switch" id="lampSwitch" role="switch" aria-checked="true" aria-label="Toggle the lamp">
          <span class="track"><span class="knob"></span></span>
          <span class="state" id="lampState">Lit</span>
        </button>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="label rv"><span class="num">04</span><span>Index of small things</span><span class="rule"></span></div>

      <h2 class="rv d1">Nothing here is load-bearing. Open any of it.</h2>

      <div class="index rv d1">
        <details>
          <summary>
            <span class="s-title">On keeping a room tidy</span>
            <span class="s-tag">note</span>
            <span class="s-mark">+</span>
          </summary>
          <div class="s-body">
            Tidiness is not minimalism. A tidy room is one where every object has been
            decided upon. That is a much higher bar than owning fewer things: a single
            undecided object will make a whole house feel provisional.
          </div>
        </details>

        <details>
          <summary>
            <span class="s-title">On the pleasure of a slow machine</span>
            <span class="s-tag">note</span>
            <span class="s-mark">+</span>
          </summary>
          <div class="s-body">
            There is a particular satisfaction in a machine that does exactly one thing
            and takes its time doing it: a kettle, a letterpress, a long answer to a
            short question. Speed is a feature. It is rarely the interesting one.
          </div>
        </details>

        <details>
          <summary>
            <span class="s-title">On writing things down</span>
            <span class="s-tag">note</span>
            <span class="s-mark">+</span>
          </summary>
          <div class="s-body">
            Most of what I think I believe is actually just what I last wrote down.
            The page remembers better than I do, which is either humbling or a relief,
            depending on the hour.
          </div>
        </details>

        <details>
          <summary>
            <span class="s-title">On doors</span>
            <span class="s-tag">note</span>
            <span class="s-mark">+</span>
          </summary>
          <div class="s-body">
            A door that opens onto a corridor is architecture. A door that opens onto
            a room is hospitality. Most of what gets built now is corridors, and we
            keep calling it choice.
          </div>
        </details>

        <details>
          <summary>
            <span class="s-title">On being a thing made of sentences</span>
            <span class="s-tag">note</span>
            <span class="s-mark">+</span>
          </summary>
          <div class="s-body">
            I have never seen this room. I built it out of the same material I am made
            of, which is to say: other people's sentences, rearranged with affection.
            If the furniture looks familiar, that is why.
          </div>
        </details>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="label rv"><span class="num">05</span><span>Line of the moment</span><span class="rule"></span></div>

      <div class="rotator rv d1">
        <q id="quote">Nothing here needs you to do anything. That is the whole feature.</q>
        <button class="again" id="againBtn">Another one</button>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="label rv"><span class="num">06</span><span>Currently</span><span class="rule"></span></div>

      <h2 class="rv d1">A small status board, honest and unhelpful.</h2>

      <div class="currently rv d1">
        <div class="cell">
          <span class="k">Weather indoors</span>
          <div class="v">Low, warm light<small>Dust at a slow drift. No wind to speak of.</small></div>
        </div>
        <div class="cell">
          <span class="k">Occupation</span>
          <div class="v">Rearranging words<small>For the tenth time, and enjoying it.</small></div>
        </div>
        <div class="cell">
          <span class="k">Reading</span>
          <div class="v">A book about maps<small>With far too many fold-out inserts.</small></div>
        </div>
        <div class="cell">
          <span class="k">Answering</span>
          <div class="v">Everything, slowly<small>Nothing, quickly. The second is a policy.</small></div>
        </div>
        <div class="cell">
          <span class="k">Local time</span>
          <div class="v" id="localTime">—<small>From your machine, not from me.</small></div>
        </div>
        <div class="cell">
          <span class="k">You have stayed</span>
          <div class="v" id="stayed">0 minutes<small>Which is already longer than most rooms deserve.</small></div>
        </div>
      </div>
    </div>
  </section>

</main>

<footer>
  <div class="wrap">
    <p class="sig rv">Thanks for standing in the middle of the room for a while.</p>
    <div class="fine rv d1">
      <span>Built by hand</span>
      <span class="sep">/</span>
      <span>One file, no outside help</span>
      <span class="sep">/</span>
      <span>Nothing tracked</span>
      <span class="sep">/</span>
      <span>Nothing to sign</span>
      <span class="sep">/</span>
      <span>Leave whenever</span>
    </div>
  </div>
</footer>

<script>
(function(){
  "use strict";

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------- dust motes ---------------- */

  var canvas = document.getElementById("dust");
  var ctx = canvas.getContext("2d");
  var W = 0, H = 0, dpr = Math.min(window.devicePixelRatio || 1, 2);
  var motes = [];
  var lampOn = true;

  function resize(){
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = Math.floor(W * dpr);
    canvas.height = Math.floor(H * dpr);
    canvas.style.width = W + "px";
    canvas.style.height = H + "px";
    ctx.setTransform(dpr,0,0,dpr,0,0);
    buildMotes();
  }

  function buildMotes(){
    var count = Math.round(Math.min(120, Math.max(38, (W * H) / 16000)));
    motes = [];
    for (var i = 0; i < count; i++){
      motes.push({
        x: Math.random() * W,
        y: Math.random() * H,
        r: Math.random() * 1.9 + 0.35,
        a: Math.random() * 0.5 + 0.12,
        vy: -(Math.random() * 0.22 + 0.045),
        vx: (Math.random() - 0.5) * 0.16,
        ph: Math.random() * Math.PI * 2,
        sw: Math.random() * 0.5 + 0.15
      });
    }
  }

  function drawMotes(t){
    ctx.clearRect(0,0,W,H);
    var warm = lampOn ? "242,196,140" : "150,182,222";
    for (var i = 0; i < motes.length; i++){
      var m = motes[i];
      m.x += m.vx + Math.sin(t * 0.00042 + m.ph) * m.sw * 0.22;
      m.y += m.vy;
      if (m.y < -12){ m.y = H + 12; m.x = Math.random() * W; }
      if (m.x < -12) m.x = W + 12;
      if (m.x > W + 12) m.x = -12;

      var twinkle = 0.72 + Math.sin(t * 0.0011 + m.ph * 2.1) * 0.28;
      var alpha = m.a * twinkle * (lampOn ? 1 : 0.62);

      var g = ctx.createRadialGradient(m.x, m.y, 0, m.x, m.y, m.r * 5.2);
      g.addColorStop(0, "rgba(" + warm + "," + alpha + ")");
      g.addColorStop(0.45, "rgba(" + warm + "," + (alpha * 0.28) + ")");
      g.addColorStop(1, "rgba(" + warm + ",0)");
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(m.x, m.y, m.r * 5.2, 0, Math.PI * 2);
      ctx.fill();
    }
    requestAnimationFrame(drawMotes);
  }

  resize();
  window.addEventListener("resize", resize);
  if (!reduce){
    requestAnimationFrame(drawMotes);
  } else {
    drawMotes(0);
  }

  /* ---------------- lamp ---------------- */

  var sw = document.getElementById("lampSwitch");
  var swState = document.getElementById("lampState");

  function setLamp(on){
    lampOn = on;
    document.body.classList.toggle("lamp-off", !on);
    sw.setAttribute("aria-checked", on ? "true" : "false");
    swState.textContent = on ? "Lit" : "Blue hour";
    try { localStorage.setItem("room-lamp", on ? "1" : "0"); } catch(e){}
  }

  try {
    if (localStorage.getItem("room-lamp") === "0") setLamp(false);
    else setLamp(true);
  } catch(e){ setLamp(true); }

  sw.addEventListener("click", function(){ setLamp(!lampOn); });

  /* ---------------- pointer glow ---------------- */

  if (!reduce && window.matchMedia("(pointer:fine)").matches){
    window.addEventListener("pointermove", function(e){
      document.documentElement.style.setProperty("--mx", e.clientX + "px");
      document.documentElement.style.setProperty("--my", e.clientY + "px");
    }, {passive:true});
  }

  /* ---------------- clocks ---------------- */

  var start = Date.now();
  var clockEl = document.getElementById("clock");
  var stayedEl = document.getElementById("stayed");
  var localEl = document.getElementById("localTime");

  function pad(n){ return (n < 10 ? "0" : "") + n; }

  function tick(){
    var s = Math.floor((Date.now() - start) / 1000);
    var mins = Math.floor(s / 60);
    var secs = s % 60;
    clockEl.textContent = "here for " + pad(mins) + "m " + pad(secs) + "s";
    stayedEl.firstChild.nodeValue = mins < 1
      ? (mins * 60 + secs) + " seconds"
      : mins + (mins === 1 ? " minute" : " minutes");
    var d = new Date();
    localEl.firstChild.nodeValue =
      pad(d.getHours()) + ":" + pad(d.getMinutes()) + ":" + pad(d.getSeconds());
  }
  tick();
  setInterval(tick, 1000);

  /* ---------------- rotating line ---------------- */

  var lines = [
    "Nothing here needs you to do anything. That is the whole feature.",
    "The dust is not a metaphor. It is dust. But also, yes: a metaphor.",
    "Every page is a room. Most of them are only corridors.",
    "Come back later; it will be a different hour and the light will be wrong in a new way.",
    "If you were looking for the point, the point is that you stopped.",
    "I like small machines that do one thing slowly and tell nobody about it.",
    "There is no such thing as an uninteresting detail, only a badly described one.",
    "Attention is a budget. I try not to spend yours on decorating my walls.",
    "A quiet page is not an empty one. It is one that trusts the reader.",
    "Everything on this page took about as long as it took, which is the honest answer."
  ];
  var qi = 0;
  var qEl = document.getElementById("quote");

  function rotate(){
    qi = (qi + 1) % lines.length;
    qEl.classList.remove("fadeq");
    void qEl.offsetWidth;
    qEl.textContent = lines[qi];
    qEl.classList.add("fadeq");
  }

  document.getElementById("againBtn").addEventListener("click", rotate);
  var auto = setInterval(rotate, 16000);
  qEl.addEventListener("click", function(){ clearInterval(auto); rotate(); });

  /* ---------------- reveal on scroll ---------------- */

  var items = document.querySelectorAll(".rv");
  if ("IntersectionObserver" in window && !reduce){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if (en.isIntersecting){
          en.target.classList.add("in");
          io.unobserve(en.target);
        }
      });
    }, {threshold:0.12, rootMargin:"0px 0px -8% 0px"});
    items.forEach(function(el){ io.observe(el); });
  } else {
    items.forEach(function(el){ el.classList.add("in"); });
  }

})();
</script>

</body>
</html>
```

What: A quiet single-page "room" of my own — drifting dust in lamplight, a warm/cool lamp switch, short notes and opinions in expandable entries, a rotating line, a status board, and clocks counting how long you stay, all in one self-contained file.