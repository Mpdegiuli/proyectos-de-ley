```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>a sky</title>
<style>
  :root{
    --top:#05070f;
    --mid:#0a1020;
    --bot:#121a2e;
    --ink:#f4f1ea;
    --ink-soft:rgba(244,241,234,.62);
  }

  *{box-sizing:border-box;}
  html,body{height:100%;}

  body{
    margin:0;
    overflow:hidden;
    background:#05070f;
    color:var(--ink);
    font-family:ui-serif, Georgia, "Times New Roman", serif;
    -webkit-font-smoothing:antialiased;
  }

  /* ---------- the sky ---------- */

  .sky{
    position:fixed;
    inset:0;
    background:linear-gradient(to bottom, var(--top) 0%, var(--mid) 58%, var(--bot) 100%);
  }

  .vignette{
    position:fixed;
    inset:0;
    pointer-events:none;
    background:radial-gradient(130% 100% at 50% 38%, rgba(0,0,0,0) 42%, rgba(0,0,0,.30) 100%);
  }

  .stars{
    position:fixed;
    inset:0;
    pointer-events:none;
    opacity:0;
  }

  .star{
    position:absolute;
    background:#fff;
    border-radius:50%;
    animation:twinkle linear infinite;
  }

  @keyframes twinkle{
    0%,100%{opacity:.10;}
    50%{opacity:.95;}
  }

  .orb{
    position:fixed;
    border-radius:50%;
    transform:translate(-50%,-50%);
    pointer-events:none;
    opacity:0;
    transition:opacity .8s linear;
  }

  #sun{
    width:54px;height:54px;
    background:radial-gradient(circle at 50% 50%, #fffdf4 0%, #ffeba8 50%, #ffc661 100%);
    box-shadow:
      0 0 52px 18px rgba(255,214,140,.42),
      0 0 150px 72px rgba(255,186,104,.16);
  }

  #moon{
    width:44px;height:44px;
    background:radial-gradient(circle at 36% 34%, #ffffff 0%, #e8eef7 56%, #b3bfd2 100%);
    box-shadow:
      0 0 40px 12px rgba(206,220,244,.26),
      0 0 120px 56px rgba(150,175,220,.11);
  }

  /* ---------- the ground ---------- */

  .ground{
    position:fixed;
    left:0;right:0;bottom:0;
    height:28vh;
    background:linear-gradient(to bottom, #0b0b0e 0%, #060608 55%, #030304 100%);
    border-top:1px solid rgba(255,255,255,.12);
  }

  /* ---------- the page ---------- */

  header{
    position:fixed;
    top:0;left:0;right:0;
    z-index:5;
    display:flex;
    justify-content:space-between;
    align-items:baseline;
    gap:16px;
    padding:22px clamp(18px,4vw,42px);
    font-family:ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size:11px;
    letter-spacing:.16em;
    text-transform:lowercase;
    color:var(--ink);
  }

  header .mark{
    display:inline-block;
    width:7px;height:7px;
    margin-right:10px;
    border:1px solid currentColor;
    border-radius:50%;
    vertical-align:1px;
  }

  .clock{font-variant-numeric:tabular-nums;}

  .caption{
    position:fixed;
    z-index:4;
    left:clamp(18px,6vw,90px);
    right:clamp(18px,6vw,90px);
    bottom:calc(28vh + clamp(26px,5vh,58px));
    max-width:36rem;
  }

  h1{
    margin:0;
    font-weight:400;
    font-size:clamp(30px,5.6vw,58px);
    line-height:1.02;
    letter-spacing:-.022em;
    color:var(--ink);
  }

  .note{
    margin:clamp(14px,2.6vh,24px) 0 0;
    max-width:38ch;
    min-height:3.4em;
    font-size:clamp(13px,1.15vw,15px);
    line-height:1.68;
    color:var(--ink-soft);
    transition:opacity .45s ease;
  }

  footer{
    position:fixed;
    z-index:6;
    left:0;right:0;bottom:0;
    height:28vh;
    min-height:110px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:28px;
    padding:0 clamp(18px,4vw,42px);
    color:#efece6;
    font-family:ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size:11px;
    letter-spacing:.12em;
  }

  .scrub{
    display:flex;
    align-items:center;
    gap:18px;
    text-transform:lowercase;
    color:rgba(239,236,230,.55);
  }

  input[type=range]{
    -webkit-appearance:none;
    appearance:none;
    width:min(420px,44vw);
    height:20px;
    background:transparent;
    cursor:pointer;
  }

  input[type=range]::-webkit-slider-runnable-track{
    height:1px;
    background:rgba(255,255,255,.32);
  }

  input[type=range]::-webkit-slider-thumb{
    -webkit-appearance:none;
    appearance:none;
    width:9px;height:9px;
    margin-top:-4px;
    border-radius:50%;
    background:#fff;
    box-shadow:0 0 10px rgba(255,255,255,.85);
  }

  input[type=range]::-moz-range-track{
    height:1px;
    background:rgba(255,255,255,.32);
  }

  input[type=range]::-moz-range-thumb{
    width:9px;height:9px;
    border:0;
    border-radius:50%;
    background:#fff;
    box-shadow:0 0 10px rgba(255,255,255,.85);
  }

  button{
    font:inherit;
    letter-spacing:.14em;
    text-transform:lowercase;
    color:#efece6;
    background:transparent;
    border:1px solid rgba(255,255,255,.26);
    border-radius:999px;
    padding:9px 18px;
    cursor:pointer;
    transition:background .25s ease, border-color .25s ease, opacity .25s ease;
  }

  button:hover:not(:disabled){
    background:rgba(255,255,255,.10);
    border-color:rgba(255,255,255,.5);
  }

  button:disabled{
    opacity:.3;
    cursor:default;
  }

  @media (max-width:640px){
    footer{
      flex-direction:column;
      align-items:flex-start;
      justify-content:center;
      gap:16px;
    }
    input[type=range]{width:62vw;}
  }

  @media (prefers-reduced-motion: reduce){
    .star{animation:none;opacity:.45;}
    .orb{transition:none;}
    .note{transition:none;}
  }
</style>
</head>
<body>

<div class="sky"></div>
<div class="vignette"></div>
<div class="stars" id="stars"></div>
<div class="orb" id="sun"></div>
<div class="orb" id="moon"></div>
<div class="ground"></div>

<header>
  <div><span class="mark"></span>a front page</div>
  <div class="clock" id="clock">--:--</div>
</header>

<section class="caption">
  <h1 id="heading">hello.</h1>
  <p class="note" id="note">This page is a sky, generated from the clock on your machine.</p>
</section>

<footer>
  <div class="scrub">
    <span>move the day</span>
    <input id="scrub" type="range" min="0" max="1439" step="1" value="720" aria-label="time of day">
  </div>
  <button id="now" type="button" disabled>back to now</button>
</footer>

<script>
(function(){
  "use strict";

  var root      = document.documentElement;
  var sunEl     = document.getElementById("sun");
  var moonEl    = document.getElementById("moon");
  var starsEl   = document.getElementById("stars");
  var clockEl   = document.getElementById("clock");
  var noteEl    = document.getElementById("note");
  var headingEl = document.getElementById("heading");
  var slider    = document.getElementById("scrub");
  var nowBtn    = document.getElementById("now");

  /* ---------- a field of stars ---------- */

  for (var i = 0; i < 150; i++) {
    var s = document.createElement("div");
    s.className = "star";
    var size = Math.random() < 0.88 ? 1 : 2;
    s.style.width  = size + "px";
    s.style.height = size + "px";
    s.style.left   = (Math.random() * 100).toFixed(2) + "%";
    s.style.top    = (Math.random() * 68).toFixed(2) + "%";
    s.style.animationDuration = (2.6 + Math.random() * 4.4).toFixed(2) + "s";
    s.style.animationDelay    = (-Math.random() * 7).toFixed(2) + "s";
    starsEl.appendChild(s);
  }

  /* ---------- a small table of light ---------- */

  var KF = [
    {h: 0.0,  top:"#05070f", mid:"#0a1020", bot:"#121a2e", star:1.00},
    {h: 4.5,  top:"#060a18", mid:"#131b33", bot:"#2a2b45", star:0.85},
    {h: 6.0,  top:"#1b2340", mid:"#6b4a63", bot:"#e2936a", star:0.15},
    {h: 7.5,  top:"#6f9ec9", mid:"#b9d4e6", bot:"#f3dcc0", star:0.00},
    {h:12.0,  top:"#4f9ad4", mid:"#9dc9e8", bot:"#dceaf3", star:0.00},
    {h:17.0,  top:"#5d9ecb", mid:"#b7cfe0", bot:"#f0dcc2", star:0.00},
    {h:19.0,  top:"#2d2a4a", mid:"#9a5570", bot:"#e88a52", star:0.10},
    {h:20.5,  top:"#131a33", mid:"#3a2b4d", bot:"#8a4a55", star:0.50},
    {h:22.0,  top:"#070b18", mid:"#0c1226", bot:"#161f36", star:0.90},
    {h:24.0,  top:"#05070f", mid:"#0a1020", bot:"#121a2e", star:1.00}
  ];

  function hexToRgb(hex){
    var h = hex.replace("#","");
    return [
      parseInt(h.slice(0,2),16),
      parseInt(h.slice(2,4),16),
      parseInt(h.slice(4,6),16)
    ];
  }

  KF.forEach(function(k){
    k.top = hexToRgb(k.top);
    k.mid = hexToRgb(k.mid);
    k.bot = hexToRgb(k.bot);
  });

  function lerp(a,b,t){ return a + (b-a) * t; }

  function mix(c1,c2,t){
    return "rgb(" +
      Math.round(lerp(c1[0],c2[0],t)) + "," +
      Math.round(lerp(c1[1],c2[1],t)) + "," +
      Math.round(lerp(c1[2],c2[2],t)) + ")";
  }

  function sample(h){
    h = ((h % 24) + 24) % 24;
    var i = 0;
    while (i < KF.length - 2 && h >= KF[i+1].h) i++;
    var a = KF[i], b = KF[i+1];
    var span = (b.h - a.h) || 1;
    var t = (h - a.h) / span;
    t = t < 0 ? 0 : (t > 1 ? 1 : t);
    return {
      top: mix(a.top, b.top, t),
      mid: mix(a.mid, b.mid, t),
      bot: mix(a.bot, b.bot, t),
      midRaw: [
        lerp(a.mid[0], b.mid[0], t),
        lerp(a.mid[1], b.mid[1], t),
        lerp(a.mid[2], b.mid[2], t)
      ],
      star: lerp(a.star, b.star, t)
    };
  }

  /* ---------- language ---------- */

  var NOTES = [
    "This page is a sky, generated from the clock on your machine.",
    "One file. No network. Nothing is measured and nothing is kept.",
    "The colours are guesses about light, read from a small table.",
    "Drag the day around if the current light does not suit you.",
    "No newsletter, no cookie banner, no thing to buy.",
    "It looks quite different at four in the morning."
  ];

  var noteIndex = 0;

  function greeting(h){
    if (h < 5)  return "good night.";
    if (h < 11) return "good morning.";
    if (h < 17) return "good afternoon.";
    if (h < 22) return "good evening.";
    return "good night.";
  }

  function pad(n){ return n < 10 ? "0" + n : "" + n; }

  /* ---------- drawing ---------- */

  var lastGreeting = "";
  var lastClock = "";

  function render(h){
    var s = sample(h);

    root.style.setProperty("--top", s.top);
    root.style.setProperty("--mid", s.mid);
    root.style.setProperty("--bot", s.bot);

    var lum = 0.2126 * s.midRaw[0] + 0.7152 * s.midRaw[1] + 0.0722 * s.midRaw[2];
    var dark = lum > 134;
    root.style.setProperty("--ink", dark ? "#151a24" : "#f4f1ea");
    root.style.setProperty("--ink-soft", dark ? "rgba(21,26,36,.68)" : "rgba(244,241,234,.62)");

    starsEl.style.opacity = (s.star * 0.9).toFixed(3);

    /* the sun keeps the hours 06:00 to 19:00 */
    var sunT = (h - 6) / 13;
    if (sunT > 0 && sunT < 1) {
      var sa = Math.sin(Math.PI * sunT);
      sunEl.style.left = (8 + 84 * sunT).toFixed(3) + "%";
      sunEl.style.top  = (72 - sa * 54).toFixed(3) + "%";
      sunEl.style.opacity = Math.min(1, sa * 6).toFixed(3);
    } else {
      sunEl.style.opacity = "0";
    }

    /* the moon keeps the other twelve hours */
    var moonT = h >= 19 ? (h - 19) / 12 : (h + 5) / 12;
    if (h >= 19 || h < 7) {
      var ma = Math.sin(Math.PI * moonT);
      moonEl.style.left = (8 + 84 * moonT).toFixed(3) + "%";
      moonEl.style.top  = (72 - ma * 50).toFixed(3) + "%";
      moonEl.style.opacity = Math.min(1, ma * 6).toFixed(3);
    } else {
      moonEl.style.opacity = "0";
    }

    var g = greeting(h);
    if (g !== lastGreeting) {
      headingEl.textContent = g;
      lastGreeting = g;
    }

    var hh = Math.floor(h) % 24;
    var mm = Math.floor((h % 1) * 60);
    var c = pad(hh) + ":" + pad(mm);
    if (c !== lastClock) {
      clockEl.textContent = c;
      lastClock = c;
    }
  }

  /* ---------- time ---------- */

  function realHour(){
    var d = new Date();
    return d.getHours() + d.getMinutes() / 60 + d.getSeconds() / 3600 + d.getMilliseconds() / 3600000;
  }

  var scrubbing = false;
  var scrubHour = 12;
  var shown = realHour();

  function frame(){
    var target = scrubbing ? scrubHour : realHour();
    var diff = ((target - shown + 12) % 24 + 24) % 24 - 12;
    shown = (shown + diff * 0.10 + 24) % 24;

    render(shown);

    if (!scrubbing) slider.value = Math.round(shown * 60) % 1440;

    requestAnimationFrame(frame);
  }

  /* ---------- controls ---------- */

  slider.addEventListener("input", function(){
    scrubbing = true;
    scrubHour = parseFloat(slider.value) / 60;
    nowBtn.disabled = false;
  });

  nowBtn.addEventListener("click", function(){
    scrubbing = false;
    nowBtn.disabled = true;
  });

  function rotateNote(){
    noteEl.style.opacity = "0";
    setTimeout(function(){
      noteIndex = (noteIndex + 1) % NOTES.length;
      noteEl.textContent = NOTES[noteIndex];
      noteEl.style.opacity = "1";
    }, 460);
  }

  var still = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!still) setInterval(rotateNote, 9000);

  render(shown);
  requestAnimationFrame(frame);
})();
</script>
</body>
</html>
```

What: A full-screen sky that reads your computer's clock — sun, moon, stars and colour shifting through the day — with a greeting, a rotating line of plain text, and a slider that lets you drag the day to another hour.