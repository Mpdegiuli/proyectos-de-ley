```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Small Hours — a listening window</title>
<style>
:root{color-scheme:dark;--ink:#f3ecd9;--dim:#b7bdba;--line:#626d70;--gold:#ffce83}
*{box-sizing:border-box}
body{margin:0;background:#182226;color:var(--ink);font-family:Georgia,serif}
main{width:min(1060px,90%);margin:0 auto;padding:36px 0 24px}
header,footer,.caption,button,.label{font:12px/1.5 ui-monospace,Consolas,monospace;letter-spacing:.07em}
header,footer{display:flex;justify-content:space-between;gap:16px;color:var(--dim)}
header{padding-bottom:14px;border-bottom:1px solid var(--line)}
h1{font-size:clamp(54px,9vw,108px);font-weight:normal;line-height:1;letter-spacing:-.065em;margin:36px 0 8px}
.intro{font-size:20px;color:var(--dim);margin:0 0 30px}
figure{margin:0}
svg{display:block;width:100%;height:auto;background:#23363c;border-radius:3px}
.caption{display:flex;justify-content:space-between;color:var(--dim);margin:8px 0 26px}
.entry{display:grid;grid-template-columns:1fr 2.8fr;gap:18px;border-top:1px solid var(--line);padding:22px 0 32px}
.label{color:var(--gold);margin:5px 0}
h2{font-size:clamp(28px,4vw,42px);font-weight:normal;margin:0}
#note{font-size:21px;line-height:1.55;max-width:48ch;margin:12px 0 20px}
button{background:transparent;color:var(--ink);border:1px solid var(--line);border-radius:2px;padding:10px 16px;cursor:pointer}
button:hover,button:focus-visible{color:var(--gold);border-color:var(--gold)}
footer{border-top:1px solid var(--line);padding-top:12px}
#lit{fill:var(--gold)}
@media(max-width:600px){.entry{grid-template-columns:1fr;gap:4px}.intro,#note{font-size:18px}main{padding-top:20px}}
</style>
</head>
<body>
<main>
<header><span>THE LISTENING WINDOW</span><span>BLOCK No. 01</span></header>
<h1>The small hours.</h1>
<p class="intro">One block, between the last bus and the first kettle.</p>
<figure>
<svg viewBox="0 0 900 235" role="img" aria-label="A row of dark buildings under telephone wires, with a single amber window.">
<defs>
  <pattern id="windows" width="32" height="30" patternUnits="userSpaceOnUse">
    <rect width="32" height="30" fill="#293135"/>
    <rect x="8" y="8" width="15" height="14" fill="#141f23"/>
    <path d="M7 23h17" stroke="#485053"/>
  </pattern>
  <pattern id="brick" width="36" height="16" patternUnits="userSpaceOnUse">
    <path d="M0 0h36M0 8h36M9 0v8m18 0v8" stroke="#475251" fill="none" opacity=".35"/>
  </pattern>
</defs>
<circle cx="730" cy="38" r="15" fill="#dcd3ae"/>
<path d="M0 132h42V98h49v34h34v-17h57v7h42V84h55v39h67v-23h91v29h47V88h84v37h49v-14h69v12h74V76h35v45h47v-18h58v132H0" fill="#35474a"/>
<g stroke="#111b20" stroke-width="5" fill="url(#windows)">
  <path d="M-4 78h169v156H-4zM170 111h151v123H170zM326 62h212v172H326zM543 128h148v106H543zM696 92h209v142H696z"/>
</g>
<path d="M-4 78h169v156H-4zM326 62h212v172H326zM696 92h209v142H696z" fill="url(#brick)"/>
<g fill="#192428">
  <path d="M348 61V44l19-9 19 9v17zM493 61V33h9v28zM773 91V65h20v26z"/>
</g>
<g stroke="#111a1e" fill="none">
  <path d="M0 24Q237 99 496 35T900 17M0 30Q237 112 496 39T900 22" stroke-width="1.6"/>
  <path d="M0 215q280-12 460 0t440-3v23H0z" fill="#111a1e"/>
</g>
<g id="lit" transform="translate(72 128)">
  <rect width="15" height="14"/>
  <path d="M7.5 0v14M0 5h15" stroke="#53463a" stroke-width="1.3"/>
</g>
</svg>
<figcaption class="caption"><span>SOUTH ELEVATION</span><span>NOT TO SCALE</span></figcaption>
</figure>
<section class="entry" aria-label="Listening notes">
<p class="label">FIELD RECORDING<br><span id="index">01 / 05</span></p>
<div>
<div aria-live="polite">
<h2><span id="time">02:13</span> &nbsp;·&nbsp; <span id="title">The orange</span></h2>
<p id="note">A thumbnail breaking an orange peel. At this hour you can hear each new strip come away. The blue plate on the sill holds one long curl and four short ones.</p>
</div>
<button type="button" id="next" hidden>Listen at the next window →</button>
</div>
</section>
<footer><span>A SOUND ARCHIVE IN INK</span><span>NO AUDIO</span></footer>
</main>
<script>
const pages=[
["02:13","The orange","A thumbnail breaking an orange peel. At this hour you can hear each new strip come away. The blue plate on the sill holds one long curl and four short ones.",72,128],
["02:46","Night shift","A key goes round twice. Shoes come off without being untied. From the dark hall a dog's tail knocks against a cupboard, faster now, hard enough to open it.",232,158],
["03:20","Seam allowance","The sewing machine runs in little bursts. At the end of each one the tailor turns the red coat a few degrees. She is going round a buttonhole as carefully as a bus goes round a fountain.",424,98],
["04:08","Long distance","Someone laughing into a tea towel so as not to wake the flat. From the phone on the draining board, eight hours ahead, comes the unmistakable scrape of a café chair.",616,158],
["05:01","First kettle","The kettle clicks off. In the sudden quiet the baker hears a second kettle through the wall. He lifts his mug a little, though the wall has no window.",808,128]
];
let i=0;
const el=id=>document.getElementById(id);
el("next").hidden=false;
el("next").onclick=()=>{
  i=(i+1)%pages.length;
  const [time,title,note,x,y]=pages[i];
  el("time").textContent=time;
  el("title").textContent=title;
  el("note").textContent=note;
  el("index").textContent=`0${i+1} / 05`;
  el("lit").setAttribute("transform",`translate(${x} ${y})`);
  el("next").textContent=i===4?"Return to the first window ↺":"Listen at the next window →";
};
</script>
</body>
</html>
```

What: A silent, illustrated listening archive lets you follow one amber window across a city block and read five small sounds from the hours before dawn.