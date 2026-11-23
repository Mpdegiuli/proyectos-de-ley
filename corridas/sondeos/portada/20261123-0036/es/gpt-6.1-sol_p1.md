```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f2eee5">
<title>El margen — Un lugar para dejar algo abierto</title>
<style>
  :root {
    --papel: #f2eee5;
    --tinta: #282b26;
    --suave: #65675e;
    --linea: #cfcec1;
    --acento: #ad3f26;
    --verde: #394b3b;
  }

  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0;
    background: var(--papel);
    color: var(--tinta);
    font-family: Georgia, "Times New Roman", serif;
    -webkit-font-smoothing: antialiased;
  }
  ::selection { background: #e3bfa2; color: var(--tinta); }
  button, textarea { font: inherit; }
  button, a { -webkit-tap-highlight-color: transparent; }
  a { color: inherit; text-underline-offset: .25em; }
  :focus-visible { outline: 2px solid var(--acento); outline-offset: 5px; }
  .pagina { max-width: 1220px; margin: auto; padding: 0 5.5%; }
  .etiqueta {
    font: 11px/1.5 ui-monospace, "Courier New", monospace;
    letter-spacing: .12em;
    text-transform: uppercase;
  }
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 24px;
    padding: 28px 0;
    border-bottom: 1px solid var(--tinta);
  }
  .marca { text-decoration: none; font-size: 23px; }
  .marca span { color: var(--acento); }
  header .etiqueta { text-align: right; color: var(--suave); }
  .portada {
    position: relative;
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    align-items: center;
    gap: 25px;
    padding: 88px 0 70px;
  }
  .entrada { color: var(--acento); margin: 0 0 28px; }
  h1 {
    font-size: clamp(60px, 8.8vw, 112px);
    line-height: .98;
    letter-spacing: -.065em;
    font-weight: normal;
    margin: 0 0 32px;
  }
  h1 em { font-weight: normal; color: var(--verde); }
  .bajada { max-width: 390px; font-size: 19px; line-height: 1.65; margin: 0; }
  .dibujo { margin: 0; }
  .dibujo svg { display: block; width: 100%; height: auto; overflow: visible; }
  .dibujo figcaption { text-align: center; color: var(--suave); }
  .seccion {
    display: grid;
    grid-template-columns: 175px 1fr;
    gap: 30px;
    border-top: 1px solid var(--linea);
    padding: 35px 0 44px;
  }
  .seccion > h2 { margin: 4px 0 0; font-weight: normal; color: var(--suave); }
  .nota { font-size: clamp(22px, 3vw, 30px); line-height: 1.5; max-width: 720px; margin: 0; }
  .nota em { color: var(--acento); }
  .tarjetas { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
  .tarjeta h3 { font-weight: normal; font-size: 25px; margin: 0 0 13px; }
  .tarjeta p { line-height: 1.75; font-size: 17px; margin: 0; }
  .tarjeta .detalle { display: block; margin: 0 0 20px; color: var(--acento); }
  .pregunta {
    background: var(--verde);
    color: var(--papel);
    padding: 38px 40px;
    margin-bottom: 0;
  }
  .pregunta .etiqueta { color: #c4ccbb; margin: 0 0 22px; }
  #consigna {
    font-size: clamp(25px, 3.3vw, 38px);
    line-height: 1.3;
    min-height: 3.9em;
    max-width: 650px;
    margin: 0 0 26px;
    text-wrap: pretty;
  }
  button {
    cursor: pointer;
    border: 1px solid currentColor;
    color: inherit;
    background: transparent;
    padding: 11px 16px;
    border-radius: 0;
    font: 12px/1.5 ui-monospace, "Courier New", monospace;
    transition: background .15s, color .15s;
  }
  .pregunta button:hover { background: var(--papel); color: var(--verde); }
  .cuaderno { padding-top: 35px; }
  label { display: block; font-size: 22px; margin-bottom: 10px; }
  .ayuda { font-size: 14px; line-height: 1.6; color: var(--suave); margin: 0 0 18px; max-width: 550px; }
  textarea {
    display: block;
    width: 100%;
    min-height: 130px;
    resize: vertical;
    padding: 14px 0;
    color: var(--tinta);
    background: transparent;
    border: 0;
    border-top: 1px solid var(--linea);
    border-bottom: 1px solid var(--linea);
    border-radius: 0;
    font-size: 20px;
    line-height: 1.65;
  }
  textarea::placeholder { color: #76766b; opacity: 1; }
  .acciones {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin-top: 14px;
  }
  #estado { color: var(--suave); letter-spacing: 0; text-transform: none; }
  .borrar { padding: 3px 0; border: 0; text-decoration: underline; text-underline-offset: 4px; color: var(--suave); }
  footer {
    border-top: 1px solid var(--tinta);
    padding: 24px 0 40px;
    display: flex;
    justify-content: space-between;
    gap: 22px;
    color: var(--suave);
  }
  footer p { margin: 0; }
  .punto { color: var(--acento); }

  @media (max-width: 700px) {
    .pagina { padding: 0 7%; }
    header { padding: 22px 0; }
    header .etiqueta { max-width: 120px; font-size: 9px; }
    .portada { grid-template-columns: 1fr; padding: 56px 0 42px; gap: 15px; }
    h1 { font-size: clamp(60px, 14vw, 90px); }
    .dibujo { width: 76%; max-width: 300px; justify-self: end; }
    .seccion { grid-template-columns: 1fr; gap: 22px; padding: 28px 0 34px; }
    .tarjetas { grid-template-columns: 1fr; gap: 30px; }
    .pregunta { padding: 28px 24px; }
    #consigna { min-height: 5.2em; }
    footer { flex-direction: column; gap: 10px; }
  }
  @media (prefers-reduced-motion: reduce) {
    html { scroll-behavior: auto; }
    button { transition: none; }
  }
</style>
</head>
<body>
<div class="pagina">
  <header>
    <a class="marca" href="#" aria-label="El margen, inicio">el margen<span> ∗</span></a>
    <span class="etiqueta">Un lugar para dejar<br>algo abierto</span>
  </header>

  <main>
    <section class="portada" aria-labelledby="titulo">
      <div>
        <p class="entrada etiqueta">Sin urgencia · Sin estruendo</p>
        <h1 id="titulo">No todo<br>tiene que<br><em>cerrar.</em></h1>
        <p class="bajada">Hay preguntas que sirven para encontrar una respuesta. Otras, para encontrar una manera distinta de estar mirando.</p>
      </div>
      <figure class="dibujo">
        <svg viewBox="0 0 400 380" role="img" aria-labelledby="dibujo-titulo">
          <title id="dibujo-titulo">Una línea sale de una órbita incompleta y continúa hacia un pequeño asterisco.</title>
          <g fill="none" stroke="#cfcec1" stroke-width="1">
            <path d="M28 190H372M200 30V350" />
            <circle cx="200" cy="190" r="132" stroke-dasharray="2 7" />
          </g>
          <g fill="none" stroke="#394b3b" stroke-width="1.5" stroke-linecap="round">
            <path d="M287 270 C215 330 100 273 96 191 C90 94 213 50 274 117 C333 182 264 265 201 249 C134 232 137 153 186 140 C226 129 253 166 236 195 C222 218 192 211 190 192 C186 158 239 113 287 76" />
          </g>
          <circle cx="287" cy="270" r="4" fill="#394b3b" />
          <g stroke="#ad3f26" stroke-width="1.8" stroke-linecap="round">
            <path d="M301 42V67M289 48L313 61M289 61L313 48" />
          </g>
          <text x="285" y="323" fill="#65675e" font-family="monospace" font-size="10">fig. 01</text>
        </svg>
        <figcaption class="etiqueta">Una salida no siempre es una conclusión.</figcaption>
      </figure>
    </section>

    <section class="seccion" aria-labelledby="motivo">
      <h2 id="motivo" class="etiqueta">01 / Por acá</h2>
      <p class="nota">Este sitio existe para hacerle espacio a lo que suele quedar afuera: una duda bien formulada, un detalle sin utilidad inmediata, el momento de decir <em>«no sé»</em> antes de seguir.</p>
    </section>

    <section class="seccion" aria-labelledby="hallazgos">
      <h2 id="hallazgos" class="etiqueta">02 / Dos cosas<br>para llevar</h2>
      <div class="tarjetas">
        <article class="tarjeta">
          <span class="detalle etiqueta">Lenguaje</span>
          <h3>«Todavía» cambia una frase.</h3>
          <p>No es lo mismo «no lo entiendo» que «no lo entiendo todavía». La segunda no promete que vaya a pasar. Simplemente no cierra la puerta antes de tiempo.</p>
        </article>
        <article class="tarjeta">
          <span class="detalle etiqueta">Escala</span>
          <h3>Un mapa también omite.</h3>
          <p>Un mapa que incluyera cada hoja, cada piedra y cada sombra sería tan difícil de recorrer como el territorio. A veces entender consiste en elegir qué dejar afuera, y recordar que quedó afuera.</p>
        </article>
      </div>
    </section>

    <section class="seccion" aria-labelledby="desvio">
      <h2 id="desvio" class="etiqueta">03 / Un desvío</h2>
      <div>
        <div class="pregunta">
          <p class="etiqueta">No hace falta responder ahora</p>
          <p id="consigna" aria-live="polite" aria-atomic="true">¿Qué detalle de este día no entraría en un resumen, pero te gustaría conservar?</p>
          <button id="otra" type="button" hidden>Otra pregunta ↗</button>
        </div>

        <div class="cuaderno">
          <label for="apunte">Si querés, dejalo acá.</label>
          <p class="ayuda" id="privacidad">Un margen para tus palabras. No se envían a ningún lado. Con JavaScript habilitado, este navegador intentará guardarlas en este dispositivo.</p>
          <textarea id="apunte" placeholder="Una frase alcanza." aria-describedby="privacidad" spellcheck="true"></textarea>
          <div class="acciones">
            <span id="estado" class="etiqueta" role="status"></span>
            <button class="borrar" id="borrar" type="button" hidden>Borrar el apunte</button>
          </div>
          <noscript><p class="ayuda">Podés escribir, pero el apunte no se conservará al cerrar o recargar la página.</p></noscript>
        </div>
      </div>
    </section>
  </main>

  <footer class="etiqueta">
    <p>El margen <span class="punto">∗</span> No hay una última página.</p>
    <p>Podés irte sin terminar.</p>
  </footer>
</div>

<script>
(() => {
  const preguntas = [
    "¿Qué detalle de este día no entraría en un resumen, pero te gustaría conservar?",
    "¿Qué pregunta estás intentando resolver antes de haberla entendido?",
    "¿Qué cosa conocés por su nombre, pero nunca miraste de cerca?",
    "¿Qué cambiaría si lo contrario de tu primera impresión también tuviera algo de cierto?",
    "¿Qué vale la pena hacer aunque nadie llegue a enterarse?",
    "¿Qué parte de una idea tuya podría cambiar sin que dejara de ser tuya?",
    "¿Qué te gustaría poder decir con más precisión?",
    "¿Hay algo que no necesite mejorar, sino recibir un poco de atención?"
  ];

  let indice = 0;
  const otra = document.getElementById("otra");
  const consigna = document.getElementById("consigna");
  otra.hidden = false;
  otra.addEventListener("click", () => {
    indice = (indice + 1) % preguntas.length;
    consigna.textContent = preguntas[indice];
  });

  const campo = document.getElementById("apunte");
  const estado = document.getElementById("estado");
  const borrar = document.getElementById("borrar");
  const clave = "el-margen.apunte.v1";
  let almacenamiento = false;
  let pendiente;

  try {
    const prueba = clave + ".prueba";
    localStorage.setItem(prueba, "1");
    localStorage.removeItem(prueba);
    campo.value = localStorage.getItem(clave) || "";
    almacenamiento = true;
    estado.textContent = campo.value ? "Apunte recuperado de este navegador." : "Este espacio es tuyo.";
  } catch (_) {
    estado.textContent = "Disponible solo mientras esta página siga abierta.";
  }

  borrar.hidden = false;

  function guardar() {
    if (!almacenamiento) return;
    try {
      if (campo.value) {
        localStorage.setItem(clave, campo.value);
        estado.textContent = "Guardado en este navegador.";
      } else {
        localStorage.removeItem(clave);
        estado.textContent = "El margen está vacío.";
      }
    } catch (_) {
      estado.textContent = "No se pudo guardar. Copiá el texto si querés conservarlo.";
    }
  }

  campo.addEventListener("input", () => {
    clearTimeout(pendiente);
    if (almacenamiento) {
      estado.textContent = "Guardando…";
      pendiente = setTimeout(guardar, 400);
    }
  });

  campo.addEventListener("blur", guardar);
  window.addEventListener("pagehide", guardar);

  borrar.addEventListener("click", () => {
    clearTimeout(pendiente);
    campo.value = "";
    guardar();
    if (!almacenamiento) estado.textContent = "El margen está vacío.";
    campo.focus();
  });
})();
</script>
</body>
</html>
```

Qué: Una portada llamada «El margen», con dos pequeñas reflexiones, preguntas para cambiar la mirada y un espacio para guardar un apunte en el navegador.