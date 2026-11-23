```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f4f0e5">
<title>The Night Herbarium</title>
<style>
:root{--paper:#f4f0e5;--ink:#222e31;--blue:#164989;--rule:#b5b4a7}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,"Times New Roman",serif}
main{width:min(1160px,90%);margin:auto}
header,footer,.label,button,.figline,dt{font:11px/1.5 ui-monospace,"Courier New",monospace;letter-spacing:.1em;text-transform:uppercase}
header,footer,.figline{display:flex;justify-content:space-between;align-items:center;gap:1em}
header{padding:24px 0 16px;border-bottom:1px solid var(--ink)}
.seal{display:inline-block;border:1px solid;border-radius:50%;width:13px;height:13px;vertical-align:-2px;margin-right:9px;background:linear-gradient(90deg,var(--ink) 50%,transparent 50%);transform:rotate(-30deg)}
.spread{display:grid;grid-template-columns: .9fr 1.1fr;gap:7%;align-items:center;padding:clamp(28px,5vw,72px) 0}
h1{font-weight:normal;font-size:clamp(58px,7vw,104px);line-height:.93;letter-spacing:-.065em;margin:19px 0 24px}
h1 i{color:var(--blue);font-weight:normal}
.intro{font-size:clamp(18px,1.8vw,23px);line-height:1.45;max-width:32ch}
.entry{margin-top:38px;padding-top:16px;border-top:1px solid var(--rule)}
dt,.label{color:#4a5959}dl{margin:0}dd{margin:5px 0 16px;font-size:24px}
.note{font-size:17px;line-height:1.5;min-height:3em;max-width:36ch}
button{cursor:pointer;margin-top:10px;color:var(--paper);background:var(--blue);border:1px solid var(--blue);padding:12px 17px}
button:hover{background:var(--ink)}
button:focus-visible{outline:3px dashed var(--ink);outline-offset:4px}
figure{margin:0}svg{display:block;width:100%;height:auto;background:#123d78}
.figline{padding:10px 0;border-bottom:1px solid var(--rule);font-size:10px}
footer{padding:16px 0 24px;border-top:1px solid var(--ink);font-size:10px}
@media(max-width:740px){.spread{grid-template-columns:1fr;gap:24px}.entry{margin-top:20px}h1 br{display:none}h1{max-width:10ch}.intro{max-width:100%}.note{min-height:0}header{font-size:9px}}
@media print{button,header,footer{display:none}.spread{display:block}main{width:90%}h1{font-size:36px}h1 br{display:none}.intro,.entry{display:none}figure{width:82%;margin:1em auto}svg{print-color-adjust:exact}}
</style>
</head>
<body>
<main>
<header><span><b class="seal"></b>Department of small hours</span><span>Cabinet 01</span></header>
<div class="spread">
<section>
<div class="label">An atlas in blue</div>
<h1>The Night <br><i>Herbarium</i></h1>
<p class="intro">Contact prints of plants that grow in the interval between turning out the lamp and falling asleep.</p>
<div class="entry" aria-live="polite" aria-atomic="true">
<dl><dt id="accession">Accession / 001</dt><dd id="name">Landing fern</dd></dl>
<p class="note" id="note">Found on the half-lit stair. The lowest leaves are worn smooth where a hand goes looking for the rail.</p>
</div>
<button type="button" id="turn">Turn the sheet &nbsp; →</button>
</section>
<figure>
<svg viewBox="0 0 540 610" role="img" aria-labelledby="plateTitle" xmlns="http://www.w3.org/2000/svg">
<title id="plateTitle">A pale pressed landing fern on a deep blue field</title>
<defs>
<radialGradient id="wash" cx=".38" cy=".38" r=".85"><stop stop-color="#2866a7"/><stop offset=".68" stop-color="#174c8f"/><stop offset="1" stop-color="#0c3068"/></radialGradient>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".69" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
</defs>
<rect width="540" height="610" fill="url(#wash)"/>
<g stroke="#c3daec" stroke-width="1" fill="none" opacity=".66"><path d="M18 32V18h14m476 0h14v14M18 578v14h14m476 0h14v-14"/></g>
<g id="plant" fill="#e0e7dc" stroke="#e0e7dc" stroke-linecap="round"></g>
<rect width="540" height="610" filter="url(#grain)" opacity=".14" pointer-events="none"/>
<g fill="#e2e6dc" font-family="monospace" font-size="11" letter-spacing="2"><text x="32" y="565" id="plateNum">N.H. / 001</text></g>
<path d="M450 559v6h52v-6m-26 2v4" fill="none" stroke="#e2e6dc"/>
</svg>
<figcaption class="figline"><span id="caption">Fig. 01 — Landing fern</span><span>Imaginary cyanotype</span></figcaption>
</figure>
</div>
<footer><span>Specimens kept out of daylight</span><span id="count">Sheet 1 of 4</span></footer>
</main>
<script>
const sheets=[
 ["Landing fern","Found on the half-lit stair. The lowest leaves are worn smooth where a hand goes looking for the rail."],
 ["Glasswort of the sill","Rooted in the cold seam of a window. Each little bladder holds the reflection of a streetlamp, upside down."],
 ["Pillow awn","A grass of the cool side of linen. Combed flat at midnight, it stands quite straight again by three."],
 ["Latch penny","Pressed between the door and its frame. Its thin seed cases chatter for a moment after the latch has caught."]
];
const $=id=>document.getElementById(id), ns="http://www.w3.org/2000/svg";
let page=0;
function draw(){
 const group=$("plant");group.replaceChildren();
 let seed=381+page*71;
 function random(){seed=(1664525*seed+1013904223)>>>0;return seed/4294967296}
 function node(tag,attrs){const e=document.createElementNS(ns,tag);for(const [k,v] of Object.entries(attrs))e.setAttribute(k,v);group.append(e)}
 function line(d,w){node("path",{d,fill:"none","stroke-width":w})}
 function blade(x,y,dx,dy,width){
  const len=Math.hypot(dx,dy),a=-dy/len*width,b=dx/len*width;
  node("path",{d:`M${x} ${y}q${dx*.55+a} ${dy*.55+b} ${dx} ${dy}q${-dx*.36-a} ${-dy*.36-b} ${-dx} ${-dy}`,stroke:"none"});
 }
 const tips=[
 [[99,222],[174,99],[338,57],[442,168],[424,310]],
 [[105,211],[215,108],[290,72],[398,153],[448,290]],
 [[105,158],[168,94],[228,118],[305,54],[372,91],[432,156],[464,232]],
 [[89,251],[181,133],[319,82],[416,188],[431,309]]
 ][page];
 tips.forEach(([tx,ty],j)=>{
  const bx=241+j*3,by=550-j*3,cx=bx+(tx-bx)*.24,cy=by-(by-ty)*.57;
  function pos(t){return [(1-t)**2*bx+2*(1-t)*t*cx+t*t*tx,(1-t)**2*by+2*(1-t)*t*cy+t*t*ty]}
  line(`M${bx} ${by}Q${cx} ${cy} ${tx} ${ty}`,page===2?1.6:2.5);
  const n=[21,11,15,6][page];
  for(let k=0;k<n;k++){
   const f=k/n,t=(page===2?.66:.22)+(page===2?.34:.78)*f;
   for(const side of [-1,1]){
    const [x,y]=pos(t+(side===1?.009:0)),fan=(.30+.70*Math.sin(Math.PI*(.15+.85*f)))*(1+random()*.15);
    const dx=side*fan*[45,25,14,38][page]+(tx-bx)*.052,dy=-fan*[28,27,41,34][page];
    if(page===0)blade(x,y,dx,dy,3.3*fan);
    if(page===1){blade(x,y,dx,dy,5*fan);node("ellipse",{cx:x+dx,cy:y+dy,rx:4+4*fan,ry:7+5*fan,"fill-opacity":.7})}
    if(page===2){blade(x,y,dx,dy,2.3);line(`M${x+dx} ${y+dy}l${dx*.8} ${dy*.67}`, .8)}
    if(page===3){line(`M${x} ${y}q${dx*.8} -4 ${dx} ${dy}`,1.3);const r=7+fan*7;node("circle",{cx:x+dx,cy:y+dy,r,"fill-opacity":.52,"stroke-width":.8});line(`M${x+dx-2} ${y+dy+r}l4 ${-2*r}`, .8)}
   }
  }
 });
 const [name,note]=sheets[page],i=page+1,num=String(i).padStart(3,"0");
 $("name").textContent=name;$("note").textContent=note;$("accession").textContent="Accession / "+num;
 $("plateTitle").textContent=name+", a pale botanical silhouette on a deep blue field";
 $("caption").textContent="Fig. 0"+i+" — "+name;$("plateNum").textContent="N.H. / "+num;
 $("count").textContent="Sheet "+i+" of "+sheets.length;
}
$("turn").addEventListener("click",()=>{page=(page+1)%sheets.length;draw()});draw();
</script>
</body>
</html>
```

What: The Night Herbarium is a cabinet of four imaginary plants, each preserved in a blue contact print with a field note from the edge of sleep.