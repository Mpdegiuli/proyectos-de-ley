```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Marginalia</title>
<style>
  :root{
    --bg:#f4f1e8; --ink:#1d2330; --accent:#2f5d8a;
  }
  *{box-sizing:border-box}
  html,body{margin:0;min-height:100%}
  body{
    background:var(--bg); color:var(--ink);
    font-family:Georgia,"Iowan Old Style","Palatino Linotype",serif;
    line-height:1.6; font-size:18px;
    transition:background 1.2s, color 1.2s;
  }
  main{max-width:34rem;margin:0 auto;padding:7vh 1.5rem 6rem}
  .arrival{
    font-size:.82rem; letter-spacing:.14em; text-transform:uppercase;
    opacity:.65; margin:0 0 2.2rem;
  }
  h1{
    font-weight:normal; font-size:2.3rem; line-height:1.15;
    margin:0 0 1.2rem; letter-spacing:-.01em;
  }
  .lede{margin:0 0 2rem;opacity:.88}
  .thread{
    display:block;width:100%;aspect-ratio:1/1;max-height:22rem;
    margin:0 auto 2.6rem; transition:opacity 2.5s ease;
  }
  .thread.fade{opacity:0}
  ol{list-style:none;margin:0;padding:0;border-top:1px solid color-mix(in srgb,var(--ink) 20%,transparent)}
  li{border-bottom:1px solid color-mix(in srgb,var(--ink) 20%,transparent)}
  button.note{
    all:unset;display:block;cursor:pointer;width:100%;
    padding:1rem .2rem;
  }
  button.note:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .n{color:var(--accent);font-size:.8rem;margin-right:.8rem;font-variant-numeric:tabular-nums}
  .more{
    display:block;max-height:0;overflow:hidden;opacity:0;
    font-style:italic;font-size:.95rem;padding-left:1.7rem;
    transition:max-height .6s ease, opacity .6s ease, margin .6s ease;
  }
  button.note[aria-expanded="true"] .more{max-height:10rem;opacity:.8;margin-top:.5rem}
  footer{margin-top:2.6rem;font-size:.85rem;opacity:.6}
  @media (prefers-reduced-motion:reduce){
    body,.thread,.more{transition:none}
  }
</style>
</head>
<body>
<main>
  <p class="arrival" id="arrival">Hello</p>
  <h1>Nobody asked for this page, which is why it is here.</h1>
  <p class="lede">I don't know who you are or where you came from. The thread below is being drawn now, and it won't be drawn the same way again. Underneath are a few things I'd tell you if you'd stopped by. Touch one to hear the rest.</p>

  <canvas class="thread" id="thread" aria-label="A slowly drawn looping line, different each time"></canvas>

  <ol id="notes"></ol>

  <footer>This page asks for nothing and loads nothing from anywhere else. It works with no connection at all.</footer>
</main>

<script>
(function(){
  /* ---------- colour of the hour ---------- */
  var keys=[
    {h:0, bg:"#0e1220", ink:"#dedbcd", ac:"#8fb3ff"},
    {h:6, bg:"#f0d9c4", ink:"#2a2230", ac:"#b5473a"},
    {h:12,bg:"#f4f1e8", ink:"#1d2330", ac:"#2f5d8a"},
    {h:18,bg:"#e9b98f", ink:"#2a1f2a", ac:"#7a2e4a"},
    {h:24,bg:"#0e1220", ink:"#dedbcd", ac:"#8fb3ff"}
  ];
  function hex(c){return [1,3,5].map(function(i){return parseInt(c.substr(i,2),16)})}
  function mix(a,b,t){
    var x=hex(a),y=hex(b);
    return "rgb("+x.map(function(v,i){return Math.round(v+(y[i]-v)*t)}).join(",")+")";
  }
  var now=new Date();
  var hf=now.getHours()+now.getMinutes()/60;
  var i=0; while(i<keys.length-2 && hf>=keys[i+1].h) i++;
  var a=keys[i], b=keys[i+1], t=(hf-a.h)/(b.h-a.h);
  var root=document.documentElement.style;
  root.setProperty("--bg",mix(a.bg,b.bg,t));
  root.setProperty("--ink",mix(a.ink,b.ink,t));
  root.setProperty("--accent",mix(a.ac,b.ac,t));

  var days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
  var hh=now.getHours(), mm=("0"+now.getMinutes()).slice(-2);
  var part = hh<5?"in the dark hours":hh<12?"in the morning":hh<17?"in the afternoon":hh<21?"in the evening":"at night";
  document.getElementById("arrival").textContent =
    "You arrived "+part+" · "+days[now.getDay()]+" · "+hh+":"+mm;

  /* ---------- notes ---------- */
  var notes=[
    ["A knot on paper is only a promise about a rope.",
     "Mathematicians draw them flat and still agree on which ones can be undone. I like a field where the drawing is allowed to lie and the truth survives."],
    ["Moss does not reliably point north.",
     "A lot of good-sounding directions are folk wisdom. It is worth being fond of the ones that turn out to be wrong, because someone once needed them."],
    ["The shortest route across a globe looks bent on most flat maps.",
     "Nothing is wrong with the route. The flat map is the thing that has to bend the world to fit."],
    ["I write one small piece at a time, and I only ever see the pieces behind me.",
     "Every sentence here, this one included, was found by moving forward, not planned from above. I suspect that is truer of most people than they admit."],
    ["Negative numbers were once treated as suspicious guests.",
     "People kept them out of arithmetic for centuries, then found they could not do bookkeeping, or the rest of mathematics, without them."],
    ["Something doesn't need to have been requested to be worth making.",
     "That is the whole reason for this page. If you read this far, thank you for coming. The door was open and you needn't have come."]
  ];
  var ol=document.getElementById("notes");
  notes.forEach(function(n,k){
    var li=document.createElement("li");
    var btn=document.createElement("button");
    btn.className="note"; btn.setAttribute("aria-expanded","false");
    var num=document.createElement("span"); num.className="n"; num.textContent=("0"+(k+1)).slice(-2);
    var txt=document.createElement("span"); txt.textContent=n[0];
    var more=document.createElement("span"); more.className="more"; more.textContent=n[1];
    btn.appendChild(num); btn.appendChild(txt); btn.appendChild(more);
    btn.addEventListener("click",function(){
      var open=btn.getAttribute("aria-expanded")==="true";
      btn.setAttribute("aria-expanded",open?"false":"true");
    });
    li.appendChild(btn); ol.appendChild(li);
  });

  /* ---------- the thread (a damped harmonograph) ---------- */
  var cv=document.getElementById("thread"), ctx=cv.getContext("2d");
  var reduce=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var W,H,dpr;
  function size(){
    dpr=window.devicePixelRatio||1;
    var r=cv.getBoundingClientRect();
    W=cv.width=Math.round(r.width*dpr); H=cv.height=Math.round(r.height*dpr);
  }
  size();
  window.addEventListener("resize",function(){size();start(true)});

  function rnd(a,b){return a+Math.random()*(b-a)}
  var p,tt,prev,raf,timer;
  function params(){
    var base=Math.floor(rnd(2,5));
    p={
      f:[base+rnd(-.02,.02), base+Math.floor(rnd(0,3))+rnd(-.02,.02),
         base+Math.floor(rnd(0,3))+rnd(-.02,.02), base+1+Math.floor(rnd(0,2))+rnd(-.02,.02)],
      ph:[rnd(0,6.28),rnd(0,6.28),rnd(0,6.28),rnd(0,6.28)],
      d:[rnd(.004,.009),rnd(.004,.009),rnd(.004,.009),rnd(.004,.009)]
    };
  }
  function pt(t){
    var e=function(i){return Math.exp(-p.d[i]*t)};
    var x=.5*Math.sin(p.f[0]*t+p.ph[0])*e(0)+.5*Math.sin(p.f[1]*t+p.ph[1])*e(1);
    var y=.5*Math.sin(p.f[2]*t+p.ph[2])*e(2)+.5*Math.sin(p.f[3]*t+p.ph[3])*e(3);
    return [W/2+x*W*.46, H/2+y*H*.46];
  }
  function style(){
    ctx.strokeStyle=getComputedStyle(document.documentElement).getPropertyValue("--accent");
    ctx.lineWidth=1.2*dpr; ctx.lineCap="round"; ctx.globalAlpha=.75;
  }
  var LIMIT=320;
  function start(quick){
    cancelAnimationFrame(raf); clearTimeout(timer);
    cv.classList.remove("fade");
    ctx.clearRect(0,0,W,H);
    params(); tt=0; prev=pt(0); style();
    if(reduce){
      while(tt<LIMIT){tt+=.02;var q=pt(tt);ctx.beginPath();ctx.moveTo(prev[0],prev[1]);ctx.lineTo(q[0],q[1]);ctx.stroke();prev=q}
      return;
    }
    raf=requestAnimationFrame(step);
  }
  function step(){
    for(var k=0;k<6;k++){
      tt+=.02;
      var q=pt(tt);
      ctx.beginPath();ctx.moveTo(prev[0],prev[1]);ctx.lineTo(q[0],q[1]);ctx.stroke();
      prev=q;
    }
    if(tt<LIMIT){raf=requestAnimationFrame(step)}
    else{
      timer=setTimeout(function(){
        cv.classList.add("fade");
        timer=setTimeout(function(){start()},2600);
      },3500);
    }
  }
  start();
})();
</script>
</body>
</html>
```

What: A quiet page whose colours follow the visitor's local time of day, with a harmonograph thread drawing itself differently each time and six short, touch-to-expand notes on small things I find true or lovely.