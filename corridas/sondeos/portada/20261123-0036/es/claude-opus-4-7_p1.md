```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Cuaderno de márgenes</title>
<style>
  :root{
    --papel:#f2ecdc;
    --tinta:#1a1812;
    --sangre:#7a2318;
    --sombra:#c9bfa6;
  }
  *{box-sizing:border-box}
  html,body{margin:0;padding:0;background:#2a2620;color:var(--tinta);font-family:Georgia,"Times New Roman",serif}
  body{
    min-height:100vh;
    display:flex;
    justify-content:center;
    padding:40px 20px;
  }
  .hoja{
    position:relative;
    width:min(760px,100%);
    background:var(--papel);
    padding:70px 70px 90px;
    box-shadow:0 30px 60px rgba(0,0,0,.6), 0 6px 0 var(--sombra);
    background-image:
      radial-gradient(ellipse at 20% 10%, rgba(0,0,0,.05), transparent 40%),
      radial-gradient(ellipse at 80% 90%, rgba(0,0,0,.07), transparent 50%),
      repeating-linear-gradient(0deg, transparent 0 31px, rgba(90,70,30,.08) 31px 32px);
  }
  .hoja::before{
    content:"";
    position:absolute;
    left:90px; top:0; bottom:0;
    width:1px;
    background:rgba(122,35,24,.35);
  }
  .folio{
    position:absolute;
    top:30px; right:40px;
    font-size:12px;
    letter-spacing:.2em;
    color:#7a6b48;
  }
  h1{
    font-family:"Hoefler Text","Garamond",Georgia,serif;
    font-weight:normal;
    font-size:46px;
    line-height:1.05;
    margin:0 0 4px;
    letter-spacing:.01em;
  }
  h1 em{
    color:var(--sangre);
    font-style:italic;
  }
  .sub{
    font-style:italic;
    color:#5a4e2e;
    margin:0 0 40px;
    font-size:15px;
  }
  .indice{
    columns:2;
    column-gap:40px;
    margin:0 0 30px;
    padding:0;
    list-style:none;
    font-size:15px;
  }
  .indice li{
    break-inside:avoid;
    margin:0 0 10px;
    display:flex;
    gap:6px;
    align-items:baseline;
  }
  .indice .n{
    color:var(--sangre);
    font-variant:small-caps;
    font-weight:bold;
    min-width:24px;
  }
  .indice a{
    color:inherit;
    text-decoration:none;
    border-bottom:1px dotted rgba(0,0,0,.3);
  }
  .indice a:hover{color:var(--sangre); border-bottom-color:var(--sangre)}

  .fragmento{
    margin:40px 0 10px;
    padding:20px 24px;
    border-left:3px solid var(--sangre);
    background:rgba(255,255,255,.25);
    font-size:16px;
    line-height:1.6;
  }
  .fragmento p{margin:0 0 10px}
  .fragmento p:last-child{margin:0}
  .firma{
    text-align:right;
    font-style:italic;
    color:#5a4e2e;
    font-size:14px;
    margin-top:12px;
  }

  .margen{
    position:absolute;
    left:12px;
    top:140px;
    width:60px;
    font-size:11px;
    color:#8a7a52;
    font-style:italic;
    text-align:right;
    transform:rotate(-2deg);
  }
  .mancha{
    position:absolute;
    width:70px; height:70px;
    border-radius:50%;
    background:radial-gradient(circle at 40% 40%, rgba(122,35,24,.35), rgba(122,35,24,0) 70%);
    pointer-events:none;
  }
  .m1{top:380px; right:60px}
  .m2{bottom:120px; left:140px; width:50px; height:50px}

  .pie{
    margin-top:50px;
    display:flex;
    justify-content:space-between;
    font-size:12px;
    color:#7a6b48;
    letter-spacing:.15em;
    text-transform:uppercase;
  }
  .ornamento{
    text-align:center;
    color:var(--sangre);
    font-size:18px;
    letter-spacing:.6em;
    margin:30px 0 0;
  }
  @media (max-width:560px){
    .hoja{padding:50px 30px 70px}
    .hoja::before{left:50px}
    h1{font-size:34px}
    .indice{columns:1}
    .margen{display:none}
  }
</style>
</head>
<body>
  <article class="hoja">
    <div class="folio">— fol. I —</div>
    <h1>Cuaderno de <em>márgenes</em></h1>
    <p class="sub">Notas al borde de lo que estaba leyendo. Un sitio lento, sin fechas.</p>

    <div class="margen">lo que se anota al lado,<br>no en el centro</div>
    <div class="mancha m1"></div>
    <div class="mancha m2"></div>

    <ol class="indice">
      <li><span class="n">i.</span><a href="#">Contra los índices</a></li>
      <li><span class="n">ii.</span><a href="#">Un error de Borges que prefiero</a></li>
      <li><span class="n">iii.</span><a href="#">Nombres de ríos que no vi</a></li>
      <li><span class="n">iv.</span><a href="#">Sobre dejar libros abiertos</a></li>
      <li><span class="n">v.</span><a href="#">Diario de una planta terca</a></li>
      <li><span class="n">vi.</span><a href="#">Traducciones que empeoran bien</a></li>
      <li><span class="n">vii.</span><a href="#">El ruido del ascensor</a></li>
      <li><span class="n">viii.</span><a href="#">Lo que no me acuerdo de 2011</a></li>
    </ol>

    <blockquote class="fragmento">
      <p>Hoy encontré, en la página 212 de un libro prestado hace nueve años, una lista de compras:
      <em>pan, aspirinas, hilo verde, algo rico</em>. La letra no es mía y el libro tampoco, ya.</p>
      <p>Me quedé pensando en <em>algo rico</em> como categoría. En la confianza de escribirlo así, sin nombre, segura de que al volver a leerlo ibas a saber de qué se trataba.</p>
      <p class="firma">— del margen de <span style="font-variant:small-caps">El cuarto de atrás</span></p>
    </blockquote>

    <p class="ornamento">· · ·</p>

    <div class="pie">
      <span>se actualiza cuando pasa algo</span>
      <span>N.º 47</span>
    </div>
  </article>
</body>
</html>
```

Qué: Una portada con forma de hoja de cuaderno antiguo, con título "Cuaderno de márgenes", un índice de ocho entradas breves y un fragmento tipo nota al margen sobre una lista de compras encontrada en un libro prestado.