```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Marginalia</title>
<style>
  :root{
    --paper:#f2ead9;
    --paper-edge:#e6dcc6;
    --rule:#ded4bf;
    --lit:#bfae8c;
    --ink:#2f2a23;
    --faint:#8a8072;
  }
  *{box-sizing:border-box}
  html,body{margin:0;padding:0}
  body{
    background:#211e1a;
    background-image:
      radial-gradient(1200px 700px at 50% -10%, #2f2b25 0%, #1b1916 70%);
    color:var(--ink);
    font-family:Georgia,"Iowan Old Style","Palatino Linotype",serif;
    padding:46px 18px 90px;
    -webkit-font-smoothing:antialiased;
  }
  .sheet{
    max-width:1060px;
    margin:0 auto;
    background:var(--paper);
    background-image:
      repeating-linear-gradient(94deg, rgba(0,0,0,.013) 0 1px, transparent 1px 3px),
      repeating-linear-gradient(2deg, rgba(0,0,0,.010) 0 1px, transparent 1px 4px),
      radial-gradient(900px 600px at 20% 0%, #f7f0e1 0%, rgba(247,240,225,0) 60%),
      radial-gradient(700px 800px at 100% 100%, #e9dfc8 0%, rgba(233,223,200,0) 55%);
    box-shadow:0 30px 70px rgba(0,0,0,.55), 0 2px 0 rgba(255,255,255,.06) inset;
    border-radius:2px;
    padding:64px 58px 70px;
    position:relative;
  }
  .sheet::after{
    content:"";position:absolute;inset:0;pointer-events:none;border-radius:2px;
    box-shadow:inset 0 0 120px rgba(90,72,40,.16);
  }

  header{max-width:640px;margin-bottom:54px}
  h1{
    font-size:clamp(30px,5vw,46px);
    font-weight:400;letter-spacing:.055em;margin:0 0 14px;
  }
  .lede{font-size:17px;line-height:1.6;margin:0 0 10px;color:#413a31}
  .hint{
    font:italic 13.5px/1.5 Georgia,serif;color:var(--faint);
    border-top:1px solid var(--rule);padding-top:10px;margin-top:18px;max-width:420px;
  }

  #page{display:flex;gap:58px;align-items:flex-start;position:relative}
  .col{flex:0 0 50%;max-width:50%}
  .margin{flex:1;position:relative;min-height:10px}

  .line{
    height:8px;border-radius:2px;
    background:linear-gradient(90deg,var(--rule),#e4dbc7 70%,var(--rule));
    margin:0 0 15px;opacity:.85;
    transition:background .25s ease, box-shadow .25s ease, opacity .25s ease;
  }
  .line.indent{margin-left:26px}
  .line.gap{margin-bottom:28px}
  .line.lit{
    background:linear-gradient(90deg,var(--lit),#cdbb97 70%,var(--lit));
    box-shadow:0 0 0 2px rgba(191,174,140,.22);
    opacity:1;
  }

  .note{
    position:absolute;left:0;width:100%;
    cursor:default;transform-origin:left center;
    transition:transform .22s ease, filter .22s ease;
  }
  .note .body{font-size:15.5px;line-height:1.42;display:block}
  .note .who{
    display:block;font:11px/1.4 ui-sans-serif,system-ui,sans-serif;
    letter-spacing:.09em;text-transform:uppercase;color:#9a9082;margin-top:5px;
  }
  .note::before{
    content:"";position:absolute;left:-54px;top:11px;width:46px;
    border-top:1px dotted rgba(60,54,44,.5);opacity:0;transition:opacity .25s ease;
  }
  .note:hover::before{opacity:1}
  .note:hover{transform:rotate(0deg) translateX(2px)}

  /* hands */
  .h1{font:italic 15.5px/1.42 Georgia,serif;color:#38445c}
  .h2{font:13.8px/1.45 "Gill Sans","Trebuchet MS",ui-sans-serif,sans-serif;color:#5d5346;letter-spacing:.015em}
  .h3{font:italic 15px/1.4 "Palatino Linotype",Georgia,serif;color:#7c3a2b}
  .h4{font:600 14.5px/1.4 "Courier New",ui-monospace,monospace;color:#262220;letter-spacing:.01em}
  .h5{font:15px/1.44 Georgia,serif;color:#3f6448}

  .narrow #page{flex-direction:column;gap:30px}
  .narrow .col,.narrow .margin{flex:none;max-width:100%;width:100%}
  .narrow .note{position:static;width:auto;margin:0 0 20px;transform:none!important}
  .narrow .note::before{display:none}

  /* back cover */
  .cover{
    margin:76px auto 0;max-width:1060px;background:#e7dcc3;
    background-image:radial-gradient(600px 300px at 30% 0%, #efe5cf 0%, rgba(239,229,207,0) 70%);
    box-shadow:0 20px 50px rgba(0,0,0,.45);border-radius:2px;padding:44px 58px 52px;
  }
  .cover h2{font:400 22px/1.3 Georgia,serif;letter-spacing:.05em;margin:0 0 8px}
  .cover p.small{font:italic 14px/1.6 Georgia,serif;color:#6d6454;margin:0 0 26px;max-width:46ch}
  .sigs{list-style:none;margin:0 0 26px;padding:0;max-width:62ch}
  .sigs li{
    font:italic 16px/1.5 Georgia,serif;color:#2b3a4f;
    border-bottom:1px dotted rgba(0,0,0,.14);padding:9px 0;
  }
  .sigs li span{
    display:block;font:11px/1.4 ui-sans-serif,system-ui,sans-serif;
    letter-spacing:.09em;text-transform:uppercase;color:#9a9082;margin-top:4px;font-style:normal;
  }
  .composer{
    border:1px dashed rgba(0,0,0,.25);padding:14px 16px;max-width:62ch;background:rgba(255,255,255,.22);
  }
  #pen{
    min-height:26px;outline:none;font:italic 16px/1.5 Georgia,serif;color:#2b3a4f;
  }
  #pen:empty::before{content:"write something here";color:#a0978a;font-style:italic}
  .row{display:flex;gap:14px;align-items:center;margin-top:12px}
  button{
    font:12px/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;
    background:none;border:1px solid rgba(0,0,0,.35);color:#3a332a;padding:9px 15px;cursor:pointer;
    border-radius:1px;transition:background .2s,color .2s;
  }
  button:hover{background:#3a332a;color:var(--paper)}
  .note-small{font:11px/1.4 ui-sans-serif,system-ui,sans-serif;color:#8d8475;letter-spacing:.06em}

  footer{
    max-width:1060px;margin:40px auto 0;color:#6f675c;
    font:12.5px/1.7 ui-sans-serif,system-ui,sans-serif;letter-spacing:.05em;text-align:center;
  }
  @media (max-width:700px){ .sheet,.cover{padding:36px 24px 44px} }
</style>
</head>
<body>

<div class="sheet">
  <header>
    <h1>Marginalia</h1>
    <p class="lede">The book is gone. Nobody knows which one it was. What survived is the writing in the margins — four hands, maybe five, across sixty years of being lent and shelved and lent again.</p>
    <p class="hint">Hover a note to see the line it was pointing at.</p>
  </header>

  <main id="page">
    <div class="col" id="col" aria-hidden="true"></div>
    <div class="margin" id="margin"></div>
  </main>
</div>

<section class="cover">
  <h2>Inside the back cover</h2>
  <p class="small">Where readers sign. Yours stays on this machine only; nothing here goes anywhere.</p>
  <ul class="sigs" id="sigs"></ul>
  <div class="composer">
    <div id="pen" contenteditable="true" role="textbox" aria-label="Write a note"></div>
  </div>
  <div class="row">
    <button id="leave">Leave it</button>
    <span class="note-small" id="status"></span>
  </div>
</section>

<footer>no connection required · a page kept for its own sake</footer>

<script>
(function(){
  /* ---- the vanished text ---- */
  var PARAS=[5,8,4,10,6,9,5,7,11,4,8,6,9,5,7];
  var seed=20240711;
  function rnd(){seed=(seed*1664525+1013904223)%4294967296;return seed/4294967296;}

  var col=document.getElementById('col'), lines=[];
  PARAS.forEach(function(n,pi){
    for(var i=0;i<n;i++){
      var d=document.createElement('div');
      d.className='line';
      var last=(i===n-1);
      var w=last? (24+rnd()*52) : (94+rnd()*6);
      d.style.width=w.toFixed(1)+'%';
      if(i===0&&pi>0) d.classList.add('indent');
      if(last) d.classList.add('gap');
      col.appendChild(d); lines.push(d);
    }
  });

  /* ---- what is left of the readers ---- */
  var NOTES=[
    {at:2,  h:'h1', r:-1.1, t:'Begins in the middle, as if we had already agreed to something.'},
    {at:7,  h:'h2', r:0.7,  t:'borrowed from Ruth, March 1987. not returning it.'},
    {at:12, h:'h3', r:-0.6, t:'He is lying here. Compare the scene at the station.'},
    {at:13, h:'h1', r:1.0,  t:'He isn’t lying. He’s remembering it the way it was survivable.', d:'a later hand'},
    {at:19, h:'h4', r:-0.8, t:'read aloud — you run out of breath exactly at the comma.'},
    {at:24, h:'h2', r:0.5,  t:'ANNEAL: to heat, then cool slowly, so the thing stops being brittle.'},
    {at:25, h:'h5', r:-1.3, t:'whoever looked that word up — thank you. I needed it today.'},
    {at:30, h:'h1', r:0.9,  t:'the only page in the book with no weather in it.'},
    {at:35, h:'h3', r:-0.5, t:'a pressed flower was here. gone now. the stain is the shape of it.'},
    {at:39, h:'h2', r:0.6,  t:'skip ahead if you’re tired. you’re allowed to come back.'},
    {at:44, h:'h4', r:-1.0, t:'I don’t believe a word of this and I have read it four times.'},
    {at:48, h:'h2', r:0.4,  t:'NOT on the exam'},
    {at:49, h:'h5', r:-0.7, t:'it was on the exam.'},
    {at:54, h:'h1', r:1.2,  t:'My mother underlined this twice. I can’t see what is good about it.'},
    {at:55, h:'h1', r:-0.9, t:'Oh. Now I see what is good about it.', d:'same hand, twenty years on'},
    {at:60, h:'h3', r:0.8,  t:'nothing happens here and it takes nine pages'},
    {at:61, h:'h5', r:-0.6, t:'nine perfect pages'},
    {at:67, h:'h4', r:0.5,  t:'STOP WRITING IN BOOKS.'},
    {at:68, h:'h2', r:-1.1, t:'make me'},
    {at:73, h:'h1', r:0.7,  t:'I was in a hospital the first time I read this paragraph, and it was not comforting then either.'},
    {at:79, h:'h2', r:-0.5, t:'the top corner still smells like the shelf it sat on.'},
    {at:86, h:'h3', r:0.9,  t:'✓'},
    {at:92, h:'h5', r:-0.8, t:'started again from here. third time. it is a different book each time, which is surely cheating.'},
    {at:100,h:'h1', r:0.6,  t:'If you find this copy: write something. The book is going. We are what is left.'}
  ];

  var margin=document.getElementById('margin'), els=[];
  NOTES.forEach(function(n){
    if(n.at>=lines.length) n.at=lines.length-1;
    var el=document.createElement('div');
    el.className='note '+n.h;
    el.style.setProperty('--rot',n.r+'deg');
    el.innerHTML='<span class="body"></span>'+(n.d?'<span class="who">'+n.d+'</span>':'');
    el.querySelector('.body').textContent=n.t;
    var line=lines[n.at];
    el.addEventListener('mouseenter',function(){line.classList.add('lit');});
    el.addEventListener('mouseleave',function(){line.classList.remove('lit');});
    line.addEventListener('mouseenter',function(){el.style.filter='none';el.style.textShadow='0 0 10px rgba(191,174,140,.9)';});
    line.addEventListener('mouseleave',function(){el.style.textShadow='';});
    margin.appendChild(el); els.push({el:el,line:line,rot:n.r});
  });

  function layout(){
    var narrow=window.innerWidth<780;
    document.body.classList.toggle('narrow',narrow);
    if(narrow){ els.forEach(function(o){o.el.style.top='';o.el.style.transform='';}); margin.style.height=''; return; }
    var top0=margin.getBoundingClientRect().top+window.scrollY;
    var floor=0, last=0;
    els.forEach(function(o){
      var t=o.line.getBoundingClientRect().top+window.scrollY-top0-4;
      if(t<floor) t=floor;
      o.el.style.top=t+'px';
      o.el.style.transform='rotate('+o.rot+'deg)';
      floor=t+o.el.offsetHeight+16;
      last=floor;
    });
    margin.style.height=last+'px';
  }
  layout();
  window.addEventListener('resize',layout);
  window.addEventListener('load',layout);

  /* ---- the back cover ---- */
  var KEY='marginalia.signatures';
  var sigs=document.getElementById('sigs'), pen=document.getElementById('pen'),
      btn=document.getElementById('leave'), status=document.getElementById('status');

  function read(){ try{return JSON.parse(localStorage.getItem(KEY))||[];}catch(e){return [];} }
  function write(a){ try{localStorage.setItem(KEY,JSON.stringify(a));}catch(e){} }
  function render(){
    var a=read(); sigs.innerHTML='';
    if(!a.length){
      var li=document.createElement('li');
      li.style.color='#8d8475';
      li.textContent='(blank, so far)';
      sigs.appendChild(li); return;
    }
    a.forEach(function(n){
      var li=document.createElement('li');
      li.textContent=n.t;
      var s=document.createElement('span'); s.textContent=n.d;
      li.appendChild(s); sigs.appendChild(li);
    });
  }
  function commit(){
    var t=(pen.textContent||'').trim();
    if(!t){ pen.focus(); return; }
    var a=read();
    a.push({t:t.slice(0,400), d:new Date().toLocaleDateString(undefined,{year:'numeric',month:'long',day:'numeric'})});
    write(a); pen.textContent=''; render();
    status.textContent='added to this copy.';
    setTimeout(function(){status.textContent='';},2600);
  }
  btn.addEventListener('click',commit);
  pen.addEventListener('keydown',function(e){
    if(e.key==='Enter'&&!e.shiftKey){ e.preventDefault(); commit(); }
  });
  render();
})();
</script>
</body>
</html>
```

What: A page called *Marginalia* that shows only the annotations left by generations of readers in a book whose text has vanished into blank grey lines — hovering a note lights the line it once pointed at — with an "inside the back cover" where you can add your own note, saved locally.