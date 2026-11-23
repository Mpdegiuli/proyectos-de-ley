```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f3f0e7">
  <title>Al margen — Un pequeño observatorio</title>
  <style>
    :root {
      --papel: #f3f0e7;
      --tinta: #243e35;
      --suave: #58685f;
      --linea: #c9cec0;
      --acento: #a44328;
      --sol: #e3ae46;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      color: var(--tinta);
      background: var(--papel);
      font-family: Georgia, "Times New Roman", serif;
      -webkit-font-smoothing: antialiased;
    }

    ::selection { background: #e7c989; color: #243e35; }

    button, input { font: inherit; }
    button, summary, input { -webkit-tap-highlight-color: transparent; }

    :focus-visible {
      outline: 2px solid var(--acento);
      outline-offset: 6px;
    }

    .pagina {
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 5.5%;
    }

    .sans {
      font-family: ui-sans-serif, system-ui, sans-serif;
    }

    header {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 24px;
      padding: 29px 0 24px;
      border-bottom: 1px solid var(--tinta);
    }

    .nombre {
      font-size: 29px;
      font-weight: normal;
      letter-spacing: -1.4px;
    }

    .nombre span { color: var(--acento); }

    .subtitulo {
      font-size: 11px;
      letter-spacing: 1.7px;
      text-transform: uppercase;
    }

    .entrada {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7%;
      padding: 76px 0 66px;
      align-items: center;
    }

    .etiqueta {
      margin: 0 0 25px;
      color: var(--acento);
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 1.8px;
      text-transform: uppercase;
    }

    h1 {
      margin: 0;
      max-width: 650px;
      font-size: clamp(49px, 5.6vw, 82px);
      font-weight: normal;
      line-height: 1.02;
      letter-spacing: -3.7px;
    }

    h1 em { font-weight: normal; }

    .presentacion {
      max-width: 365px;
      margin: 30px 0 0;
      color: var(--suave);
      font-size: 18px;
      line-height: 1.65;
    }

    .asterisco {
      display: block;
      margin-top: 32px;
      color: var(--acento);
      font-size: 43px;
      line-height: 1;
    }

    figure { margin: 0; }

    .lamina {
      position: relative;
      overflow: hidden;
      border: 1px solid var(--linea);
      border-radius: 50% 50% 0 0;
      background: #e9e9dc;
    }

    .lamina svg {
      display: block;
      width: 100%;
      height: auto;
    }

    .numero-lamina {
      position: absolute;
      bottom: 17px;
      left: 20px;
      color: #526454;
      font-size: 10px;
      letter-spacing: 1.3px;
    }

    figcaption {
      display: flex;
      justify-content: space-between;
      gap: 20px;
      padding: 16px 0;
      font-size: 12px;
      line-height: 1.5;
    }

    figcaption span:last-child {
      color: var(--suave);
      font-style: italic;
      text-align: right;
    }

    .controles {
      padding-top: 7px;
      font-size: 11px;
    }

    .control-titulo {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 10px;
    }

    label { letter-spacing: .5px; }

    button {
      padding: 3px 0;
      border: 0;
      border-bottom: 1px solid var(--linea);
      background: transparent;
      color: var(--suave);
      font-size: 11px;
      cursor: pointer;
    }

    button:hover { color: var(--acento); border-color: var(--acento); }

    input[type="range"] {
      display: block;
      width: 100%;
      height: 28px;
      margin: 0;
      accent-color: var(--acento);
      cursor: ew-resize;
    }

    .notas {
      padding: 26px 0 52px;
      border-top: 1px solid var(--tinta);
    }

    .cabecera-notas {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      gap: 20px;
      margin-bottom: 30px;
    }

    h2 {
      margin: 0;
      font-size: 13px;
      font-weight: normal;
    }

    .invitacion { color: var(--suave); font-size: 11px; }

    .rejilla {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 36px;
      align-items: start;
    }

    details { border-top: 1px solid var(--linea); }

    summary {
      display: grid;
      grid-template-columns: 25px 1fr 14px;
      gap: 10px;
      align-items: baseline;
      padding: 20px 0 12px;
      list-style: none;
      cursor: pointer;
    }

    summary::-webkit-details-marker { display: none; }

    .indice { color: var(--acento); font-size: 11px; }

    .titulo-nota {
      font-size: 24px;
      font-weight: normal;
      line-height: 1.2;
      letter-spacing: -.5px;
    }

    .signo { color: var(--acento); font-size: 18px; }

    details[open] .signo { transform: rotate(45deg); }

    details p {
      margin: 5px 24px 12px 35px;
      color: var(--suave);
      font-size: 16px;
      line-height: 1.65;
    }

    footer {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      gap: 20px;
      padding: 21px 0 30px;
      border-top: 1px solid var(--linea);
      color: var(--suave);
      font-size: 11px;
      line-height: 1.6;
    }

    footer .final { font-size: 14px; font-style: italic; }

    @media (min-width: 1100px) {
      .observacion { max-width: 470px; justify-self: end; width: 100%; }
    }

    @media (max-width: 720px) {
      .pagina { padding: 0 7%; }
      header { padding-top: 22px; }
      .subtitulo { max-width: 125px; text-align: right; line-height: 1.6; }
      .entrada { grid-template-columns: 1fr; gap: 43px; padding: 48px 0; }
      h1 { font-size: clamp(48px, 10vw, 70px); letter-spacing: -2.4px; }
      .presentacion { max-width: 430px; }
      .asterisco { display: none; }
      .observacion { max-width: 470px; width: 100%; justify-self: center; }
      .rejilla { grid-template-columns: 1fr; gap: 12px; }
      .cabecera-notas { margin-bottom: 23px; }
      details p { max-width: 440px; }
      footer { align-items: start; flex-direction: column; gap: 7px; }
    }

    @media (prefers-reduced-motion: no-preference) {
      .signo { transition: transform .2s ease; }
    }
  </style>
</head>
<body>
  <div class="pagina">
    <header>
      <div class="nombre">Al margen<span>↗</span></div>
      <div class="subtitulo sans">Un pequeño observatorio</div>
    </header>

    <main>
      <section class="entrada" aria-labelledby="titulo">
        <div>
          <p class="etiqueta sans">N.º 001 · Lo cotidiano</p>
          <h1 id="titulo">Lo de siempre.<br>Pero <em>no</em><br>como siempre.</h1>
          <p class="presentacion">
            Este es un lugar para mirar dos veces.
            Una forma, una palabra, algo que parecía no tener nada más que decir.
            Me interesa ese segundo encuentro.
          </p>
          <span class="asterisco" aria-hidden="true">✳</span>
        </div>

        <figure class="observacion">
          <div class="lamina">
            <svg viewBox="0 0 480 450" role="img" aria-labelledby="dibujo-titulo dibujo-desc">
              <title id="dibujo-titulo">Estudio de una taza y su sombra</title>
              <desc id="dibujo-desc">
                Una taza verde sobre una mesa clara. El control debajo del dibujo
                permite mover el sol y observar cómo cambia su sombra.
              </desc>

              <defs>
                <linearGradient id="ceramica" x1="0" x2="1">
                  <stop offset="0" stop-color="#42664e"/>
                  <stop offset=".55" stop-color="#52765b"/>
                  <stop offset="1" stop-color="#355740"/>
                </linearGradient>
                <linearGradient id="mesa" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0" stop-color="#e2e1cf"/>
                  <stop offset="1" stop-color="#eeebdf"/>
                </linearGradient>
              </defs>

              <path d="M0 287 Q240 271 480 287 V450 H0Z" fill="url(#mesa)"/>
              <path d="M0 287 Q240 271 480 287" fill="none" stroke="#c4c8b5"/>

              <g id="sol" transform="translate(132 107)">
                <circle r="37" fill="#e3ae46"/>
                <circle r="46" fill="none" stroke="#c6ac6e" stroke-dasharray="1 6"/>
              </g>

              <g id="sombra" transform="translate(245 335) rotate(10)">
                <ellipse cx="52" cy="0" rx="104" ry="20" fill="#52634b" opacity=".19"/>
                <ellipse cx="100" cy="0" rx="25" ry="10"
                         fill="none" stroke="#52634b" stroke-width="9" opacity=".12"/>
              </g>

              <ellipse cx="235" cy="337" rx="77" ry="13" fill="#324938" opacity=".16"/>

              <path d="M292 235 C365 215 365 316 294 306"
                    fill="none" stroke="#355740" stroke-width="22"/>
              <path d="M294 233 C350 221 352 308 297 302"
                    fill="none" stroke="#628168" stroke-width="5"/>

              <path d="M166 220 L175 313 C179 347 289 347 294 313 L303 220Z"
                    fill="url(#ceramica)"/>
              <ellipse cx="234.5" cy="220" rx="68.5" ry="20" fill="#7e9476"/>
              <ellipse cx="234.5" cy="221" rx="59" ry="13" fill="#263f31"/>
              <path d="M181 221 Q235 203 288 221 Q236 235 181 221"
                    fill="#594633"/>
              <path d="M183 246 L187 297" stroke="#91a184"
                    stroke-width="3" stroke-linecap="round" opacity=".5"/>

              <path d="M212 171 C193 151 228 143 214 122"
                    fill="none" stroke="#899680" stroke-width="2" opacity=".5"/>
              <path d="M244 181 C229 163 260 155 250 137"
                    fill="none" stroke="#899680" stroke-width="2" opacity=".35"/>
            </svg>
            <span class="numero-lamina sans" aria-hidden="true">FIG. 01 / LUZ SOBRE CERÁMICA</span>
          </div>

          <figcaption>
            <span>Una taza. Nada extraordinario.</span>
            <span>Y sin embargo.</span>
          </figcaption>

          <div class="controles sans" id="controles" hidden>
            <div class="control-titulo">
              <label for="luz">Mové la luz. Mirá lo que cambia.</label>
              <button type="button" id="reiniciar">Volver al inicio</button>
            </div>
            <input id="luz" type="range" min="0" max="100" value="20"
                   aria-valuetext="Luz a la izquierda">
          </div>
        </figure>
      </section>

      <section class="notas" aria-labelledby="titulo-notas">
        <div class="cabecera-notas sans">
          <h2 id="titulo-notas">Tres notas al margen</h2>
          <span class="invitacion">Se pueden abrir.</span>
        </div>

        <div class="rejilla">
          <details>
            <summary>
              <span class="indice sans">01</span>
              <span class="titulo-nota">La sombra también cuenta.</span>
              <span class="signo sans" aria-hidden="true">+</span>
            </summary>
            <p>
              Dibujar una cosa es dibujar también lo que hace a su alrededor.
              La taza termina en su borde; su efecto, no.
            </p>
          </details>

          <details>
            <summary>
              <span class="indice sans">02</span>
              <span class="titulo-nota">Un hueco tiene forma.</span>
              <span class="signo sans" aria-hidden="true">+</span>
            </summary>
            <p>
              El asa está hecha de cerámica y de un poco de nada.
              Ese poco de nada es justo donde entra la mano.
              A veces, lo que falta es lo que permite usar el resto.
            </p>
          </details>

          <details>
            <summary>
              <span class="indice sans">03</span>
              <span class="titulo-nota">Mirar no es resolver.</span>
              <span class="signo sans" aria-hidden="true">+</span>
            </summary>
            <p>
              No hay una respuesta escondida en esta taza.
              Podés mover la luz, abrir estas notas y seguir con tu día.
              No todo encuentro necesita convertirse en una lección.
            </p>
          </details>
        </div>
      </section>
    </main>

    <footer>
      <span class="sans">Hecho de palabras, formas y un poco de luz. Todo está acá.</span>
      <span class="final">El margen también es parte de la página.</span>
    </footer>
  </div>

  <script>
    (() => {
      const luz = document.getElementById('luz');
      const sol = document.getElementById('sol');
      const sombra = document.getElementById('sombra');
      const reiniciar = document.getElementById('reiniciar');

      function mirar() {
        const valor = Number(luz.value);
        const posicion = (valor - 50) / 50;
        const x = 240 + posicion * 180;
        const y = 75 + posicion * posicion * 89;
        const escala = -posicion * 1.65;
        const angulo = -posicion * 17;

        sol.setAttribute('transform', `translate(${x} ${y})`);
        sombra.setAttribute(
          'transform',
          `translate(245 335) rotate(${angulo}) scale(${escala} 1)`
        );

        luz.setAttribute(
          'aria-valuetext',
          valor < 45 ? 'Luz a la izquierda' :
          valor > 55 ? 'Luz a la derecha' : 'Luz en el centro'
        );
      }

      luz.addEventListener('input', mirar);
      reiniciar.addEventListener('click', () => {
        luz.value = 20;
        mirar();
      });

      document.getElementById('controles').hidden = false;
      mirar();
    })();
  </script>
</body>
</html>
```

Qué: Una portada llamada «Al margen», con una taza ilustrada, luz que podés mover y tres notas desplegables sobre mirar lo cotidiano de otra manera.