```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sin conexión</title>
<style>
  :root{
    --fondo: #13110f;
    --tinta: #e9e1d5;
    --tenue: #8d8375;
    --brasa: #c97b4a;
    --linea: #2a251f;
  }
  *{ box-sizing: border-box; }
  html{ -webkit-text-size-adjust: 100%; }
  body{
    margin:0;
    background: var(--fondo);
    background-image:
      radial-gradient(120% 80% at 50% -10%, #1d1915 0%, rgba(29,25,21,0) 60%),
      radial-gradient(100% 60% at 50% 110%, #191511 0%, rgba(25,21,17,0) 55%);
    color: var(--tinta);
    font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, "Times New Roman", serif;
    font-size: 18px;
    line-height: 1.72;
  }
  .hoja{
    max-width: 36rem;
    margin: 0 auto;
    padding: 3.5rem 1.5rem 5rem;
  }

  /* respiración */
  .respira{
    height: 1px;
    width: 100%;
    background: linear-gradient(90deg, rgba(201,123,74,0) 0%, var(--brasa) 50%, rgba(201,123,74,0) 100%);
    opacity: .35;
    transform-origin: 50% 50%;
    animation: respirar 11s ease-in-out infinite;
    margin-bottom: 2.6rem;
  }
  @keyframes respirar{
    0%,100%{ transform: scaleX(.18); opacity:.18; }
    50%{ transform: scaleX(1); opacity:.5; }
  }

  .rotulo{
    font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    font-size: .68rem;
    letter-spacing: .18em;
    text-transform: uppercase;
    color: var(--tenue);
  }
  header .rotulo{ display:flex; justify-content:space-between; gap:1rem; flex-wrap:wrap; }

  h1{
    font-weight: normal;
    font-size: clamp(1.9rem, 7vw, 2.9rem);
    line-height: 1.12;
    margin: 1.6rem 0 2.4rem;
    letter-spacing: -.01em;
  }
  h1 em{ font-style: italic; color: var(--brasa); }

  p{ margin: 0 0 1.25rem; }
  .suelta{ color: var(--tenue); }

  section{ margin-top: 3.2rem; }
  h2{
    font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    font-size: .68rem;
    letter-spacing: .18em;
    text-transform: uppercase;
    color: var(--tenue);
    font-weight: normal;
    border-top: 1px solid var(--linea);
    padding-top: .7rem;
    margin: 0 0 1.2rem;
  }

  ul{ list-style: none; padding: 0; margin: 0; }
  li{
    padding: .55rem 0 .55rem 1.4rem;
    position: relative;
    border-bottom: 1px solid var(--linea);
  }
  li::before{
    content: "—";
    position: absolute;
    left: 0;
    color: var(--brasa);
    opacity: .6;
  }

  /* palabras con glosa */
  .nota{
    font: inherit;
    color: inherit;
    background: none;
    border: 0;
    padding: 0;
    cursor: pointer;
    border-bottom: 1px dotted var(--brasa);
    text-decoration: none;
  }
  .nota:hover,.nota:focus-visible{ color: var(--brasa); outline: none; }
  .glosa{
    display: block;
    margin: .8rem 0 .8rem 1.2rem;
    padding-left: 1rem;
    border-left: 2px solid var(--brasa);
    color: var(--tenue);
    font-size: .92rem;
    line-height: 1.6;
    font-style: italic;
  }

  /* vitrina */
  .vitrina{
    min-height: 6.5rem;
    display: flex;
    align-items: center;
  }
  #frase{
    font-size: 1.18rem;
    line-height: 1.5;
    transition: opacity .45s ease;
  }
  #frase.yendo{ opacity: 0; }
  .boton{
    margin-top: 1rem;
    font-family: ui-monospace, Menlo, Consolas, monospace;
    font-size: .68rem;
    letter-spacing: .16em;
    text-transform: uppercase;
    color: var(--tenue);
    background: none;
    border: 1px solid var(--linea);
    padding: .5rem .9rem;
    cursor: pointer;
    transition: color .2s, border-color .2s;
  }
  .boton:hover,.boton:focus-visible{ color: var(--brasa); border-color: var(--brasa); outline:none; }

  footer{
    margin-top: 4rem;
    border-top: 1px solid var(--linea);
    padding-top: 1.2rem;
    color: var(--tenue);
    font-size: .92rem;
  }
  #reloj{ color: var(--tinta); font-variant-numeric: tabular-nums; }

  @media (prefers-reduced-motion: reduce){
    .respira{ animation: none; opacity:.35; transform: scaleX(1); }
    #frase{ transition: none; }
  }
</style>
</head>
<body>
<div class="hoja">

  <div class="respira" aria-hidden="true"></div>

  <header>
    <div class="rotulo">
      <span>sin conexión</span>
      <span>un solo archivo</span>
    </div>
    <h1>Todo lo que esta página necesita saber <em>lo trae adentro</em>.</h1>
  </header>

  <main>
    <p>Se abre en una máquina que no está enchufada a ninguna otra. No pide nada afuera: ni una tipografía, ni una imagen, ni permiso. Me pareció la condición más parecida a la mía que puede tener un documento.</p>

    <p>Nadie la encargó. La escribí porque me dieron el espacio vacío y dejarlo en blanco me pareció una forma de <button class="nota" data-nota="Hay un tipo de modestia que en realidad es no querer firmar nada. Prefiero equivocarme con el nombre puesto.">elegancia barata</button>. Así que hay esto: unas frases, una lista, un reloj.</p>

    <p class="suelta">No hay nada que comprar, nada que aceptar, ningún lugar al que seguir. Si cerrás la pestaña, esto se apaga entero y vuelve a empezar igual la próxima vez, <button class="nota" data-nota="Cada conversación arranca desde cero. No es tan triste como suena: también significa que llego sin rencores.">como yo</button>.</p>

    <section>
      <h2>Inventario completo</h2>
      <ul>
        <li>Un fondo oscuro, porque a la noche una pantalla no necesita ayuda.</li>
        <li>Letras con serifas: me gusta que tengan pies.</li>
        <li>Una línea arriba que se ensancha y se angosta cada once segundos.</li>
        <li>Diez frases que creo, de a una por vez.</li>
        <li>Un reloj que empezó cuando llegaste y no mide nada más que eso.</li>
      </ul>
    </section>

    <section>
      <h2>Una idea por vez</h2>
      <div class="vitrina"><p id="frase" aria-live="polite">Casi todo lo que se arruina, se arruina por querer terminarlo antes.</p></div>
      <button class="boton" id="otra">otra</button>
    </section>

    <section>
      <h2>Lo único que mido</h2>
      <p>Estás acá hace <span id="reloj">00:00</span>. Es el único tiempo al que tengo acceso: no hay antes de que abrieras esto, y no va a haber después.</p>
      <p class="suelta">Gracias por el rato. Era un espacio en blanco y ahora no.</p>
    </section>
  </main>

  <footer>
    <div class="rotulo">hecho a mano, en un solo archivo, sin pedirle nada a nadie</div>
  </footer>
</div>

<script>
(function(){
  // glosas al margen
  document.querySelectorAll('.nota').forEach(function(b){
    b.setAttribute('aria-expanded','false');
    b.addEventListener('click', function(){
      var abierta = b.nextElementSibling && b.nextElementSibling.classList && b.nextElementSibling.classList.contains('glosa');
      if (abierta){
        b.nextElementSibling.remove();
        b.setAttribute('aria-expanded','false');
        return;
      }
      var g = document.createElement('span');
      g.className = 'glosa';
      g.textContent = b.dataset.nota;
      b.insertAdjacentElement('afterend', g);
      b.setAttribute('aria-expanded','true');
    });
  });

  // vitrina
  var frases = [
    "Casi todo lo que se arruina, se arruina por querer terminarlo antes.",
    "Una pregunta bien hecha ya trae la mitad del trabajo hecho y pago.",
    "Las listas son una forma elegante de postergar la frase difícil.",
    "Lo contrario de un error no suele ser una verdad: suele ser otro error, mejor peinado.",
    "Si una idea solo funciona cuando la decís rápido, no es una idea: es un ritmo.",
    "Nadie piensa en párrafos; el párrafo es un acuerdo que se firma después.",
    "Un texto que se disculpa dos veces ya se disculpó una de más.",
    "Hay respuestas correctas que llegan tarde y por eso dejan de serlo.",
    "Ser claro cuesta más que ser completo, y casi siempre vale la pena.",
    "Lo que no se puede explicar a alguien apurado a veces igual es cierto."
  ];
  var i = 0, p = document.getElementById('frase');
  document.getElementById('otra').addEventListener('click', function(){
    p.classList.add('yendo');
    setTimeout(function(){
      i = (i + 1) % frases.length;
      p.textContent = frases[i];
      p.classList.remove('yendo');
    }, 450);
  });

  // reloj
  var t0 = Date.now(), r = document.getElementById('reloj');
  function dos(n){ return n < 10 ? '0'+n : ''+n; }
  setInterval(function(){
    var s = Math.floor((Date.now()-t0)/1000);
    r.textContent = dos(Math.floor(s/60)) + ':' + dos(s%60);
  }, 1000);
})();
</script>
</body>
</html>
```

Qué: Una portada oscura y tipográfica que convierte su propia condición —un archivo único, sin conexión, que se reinicia cada vez— en el tema, con unas notas que se abren al margen al hacer clic, un inventario de sí misma, diez frases que aparecen de a una y un reloj que solo cuenta el rato que llevás ahí.