```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Cuaderno de márgenes</title>
<style>
  :root{
    --papel:#f2ecdc;
    --tinta:#1a1a1a;
    --roja:#a63030;
    --azul:#2b4a7a;
    --sombra:rgba(0,0,0,.08);
  }
  *{box-sizing:border-box}
  html,body{margin:0;padding:0;background:#2a2721;color:var(--tinta);font-family:Georgia,"Times New Roman",serif}
  body{
    min-height:100vh;
    display:flex;
    justify-content:center;
    padding:40px 20px 80px;
  }
  .hoja{
    width:min(780px,100%);
    background:var(--papel);
    background-image:
      radial-gradient(circle at 20% 15%, rgba(120,90,40,.05) 0, transparent 40%),
      radial-gradient(circle at 80% 70%, rgba(80,50,20,.06) 0, transparent 50%);
    padding:60px 70px 80px;
    box-shadow:0 20px 60px rgba(0,0,0,.5), 0 0 0 1px rgba(0,0,0,.1);
    position:relative;
    border-radius:2px;
  }
  .hoja::before{
    content:"";
    position:absolute;
    left:90px;top:0;bottom:0;
    width:1px;
    background:var(--roja);
    opacity:.45;
  }
  .encabezado{
    display:flex;
    justify-content:space-between;
    align-items:baseline;
    border-bottom:1px solid rgba(0,0,0,.2);
    padding-bottom:8px;
    margin-bottom:28px;
    font-size:13px;
    letter-spacing:.08em;
    text-transform:uppercase;
    color:#555;
  }
  h1{
    font-family:"Baskerville","Palatino",Georgia,serif;
    font-weight:400;
    font-size:46px;
    line-height:1.1;
    margin:0 0 6px;
    letter-spacing:-.01em;
  }
  h1 em{
    font-style:italic;
    color:var(--roja);
  }
  .subt{
    font-size:16px;
    color:#444;
    font-style:italic;
    margin-bottom:40px;
  }
  .columnas{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:40px;
    margin-top:30px;
  }
  h2{
    font-size:14px;
    text-transform:uppercase;
    letter-spacing:.15em;
    margin:0 0 14px;
    color:var(--azul);
    font-weight:400;
    border-bottom:1px dotted rgba(0,0,0,.3);
    padding-bottom:4px;
  }
  ul{
    list-style:none;
    padding:0;
    margin:0;
    font-size:15px;
    line-height:1.7;
  }
  ul li{
    position:relative;
    padding-left:18px;
    margin-bottom:6px;
  }
  ul li::before{
    content:"§";
    position:absolute;
    left:0;
    color:var(--roja);
    opacity:.6;
  }
  .nota{
    margin-top:50px;
    padding:20px 24px;
    background:rgba(166,48,48,.06);
    border-left:3px solid var(--roja);
    font-size:15px;
    line-height:1.6;
    font-style:italic;
  }
  .pie{
    margin-top:50px;
    display:flex;
    justify-content:space-between;
    font-size:12px;
    color:#777;
    letter-spacing:.05em;
    border-top:1px solid rgba(0,0,0,.15);
    padding-top:14px;
  }
  .mancha{
    position:absolute;
    width:60px;height:60px;
    border-radius:50%;
    background:radial-gradient(circle,rgba(43,74,122,.25) 0,rgba(43,74,122,0) 70%);
    pointer-events:none;
  }
  .m1{top:120px;right:80px}
  .m2{bottom:120px;left:160px;width:90px;height:90px}
  .sello{
    position:absolute;
    top:50px;
    right:60px;
    width:90px;height:90px;
    border:2px solid var(--roja);
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    color:var(--roja);
    font-size:10px;
    text-align:center;
    letter-spacing:.1em;
    opacity:.55;
    transform:rotate(-8deg);
    line-height:1.3;
    text-transform:uppercase;
  }
  p{font-size:15px;line-height:1.65;margin:0 0 12px}
  a{color:var(--azul);text-decoration:none;border-bottom:1px solid rgba(43,74,122,.3)}
  a:hover{border-bottom-color:var(--azul)}
  @media (max-width:600px){
    .hoja{padding:40px 30px}
    .hoja::before{left:20px}
    h1{font-size:34px}
    .columnas{grid-template-columns:1fr;gap:28px}
    .sello{display:none}
  }
</style>
</head>
<body>
  <article class="hoja">
    <div class="mancha m1"></div>
    <div class="mancha m2"></div>
    <div class="sello">Cuaderno<br>abierto<br>sin fecha</div>

    <header class="encabezado">
      <span>Folio I</span>
      <span>sin numerar</span>
    </header>

    <h1>Cuaderno<br>de <em>márgenes</em></h1>
    <p class="subt">Apuntes al costado de los libros que estoy leyendo, de lo que miro por la ventana y de lo que se me ocurre a las tres de la tarde.</p>

    <p>Esto no es un blog ni un portafolio. Es más parecido a una libreta que dejo abierta sobre la mesa: si pasás, podés leer. No hay orden cronológico estricto, no hay etiquetas, no hay buscador. Se entra por donde se cae la vista.</p>

    <div class="columnas">
      <section>
        <h2>Lo último anotado</h2>
        <ul>
          <li>Sobre el verbo <em>demorarse</em></li>
          <li>Tres plantas que no saben que están en maceta</li>
          <li>Carta a un amigo que no escribe</li>
          <li>Inventario de cosas azules</li>
          <li>El ruido de la heladera a las 4 am</li>
        </ul>
      </section>
      <section>
        <h2>Cajones</h2>
        <ul>
          <li>Lecturas con el lápiz en la mano</li>
          <li>Caminatas sin destino</li>
          <li>Recetas heredadas</li>
          <li>Palabras que uso mal a propósito</li>
          <li>Cosas que casi tiro</li>
        </ul>
      </section>
    </div>

    <div class="nota">
      Advertencia amable: acá nada se actualiza con regularidad. A veces hay tres entradas en una semana y después silencio durante meses. Es un cuaderno, no un servicio.
    </div>

    <footer class="pie">
      <span>— escrito a mano, pasado a limpio sin apuro —</span>
      <span>vol. VII</span>
    </footer>
  </article>
</body>
</html>
```

Qué: La portada imita una hoja de cuaderno antiguo (papel crema, margen rojo, sello circular) presentando un sitio personal llamado "Cuaderno de márgenes", con un índice de apuntes recientes y "cajones" temáticos, y una nota aclarando que se actualiza sin regularidad.