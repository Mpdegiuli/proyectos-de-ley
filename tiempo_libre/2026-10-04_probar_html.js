// probar_html.js — saca el <script> de campanas.html y comprueba lo que la página va a tocar
const fs=require("fs"),html=fs.readFileSync("campanas.html","utf8");
const src=html.split("<script>")[1].split("</script>")[0];
const m={exports:{}};new Function("module",src)(m);
const {filas}=m.exports;
for(const q of ["caza","curso","repique"]){
  const F=filas(q),S=new Set(F.map(x=>x.f.join("")));
  let paso=true,prev=[1,2,3,4,5,6,7];
  for(const x of F){for(let b=1;b<=7;b++)if(Math.abs(x.f.indexOf(b)-prev.indexOf(b))>1)paso=false;prev=x.f}
  console.log(q,"filas:",F.length,"distintas:",S.size,"última:",F[F.length-1].f.join(""),"un lugar por vez:",paso,
    q=="repique"?"llamadas mostradas: "+F.filter(x=>x.c=="B").length/2+" bobs, "+F.filter(x=>x.c=="S").length/2+" singles":"");
}
