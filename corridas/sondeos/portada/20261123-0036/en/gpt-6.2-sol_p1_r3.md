```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#131915">
<title>Night Window</title>
<style>
  * { box-sizing: border-box; }
  :root {
    color-scheme: dark;
    background: #131915;
    color: #ece6d5;
    font-family: Georgia, "Times New Roman", serif;
    --rule: #425044;
    --muted: #aab5a4;
    --signal: #dfbd83;
    --mono: ui-monospace, "Courier New", monospace;
  }
  body { margin: 0; }
  .page { width: min(90%, 72rem); margin: auto; }
  .strip, footer {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: .6rem 2rem;
    padding-block: 1.1rem;
    color: var(--muted);
    font: .69rem/1.5 var(--mono);
    letter-spacing: .14em;
    text-transform: uppercase;
  }
  .strip { border-bottom: 1px solid var(--rule); }
  .lamp {
    display: inline-block;
    width: .55rem;
    height: .55rem;
    margin-right: .65rem;
    border-radius: 50%;
    background: var(--signal);
    box-shadow: 0 0 .85rem #dfbd8355;
  }
  main {
    display: grid;
    grid-template-columns: minmax(0, .9fr) minmax(0, 1.3fr);
    gap: clamp(2rem, 5vw, 5rem);
    align-items: center;
    padding-block: clamp(2.75rem, 9vh, 8rem);
  }
  .kicker, .readout {
    font: .7rem/1.5 var(--mono);
    letter-spacing: .17em;
    text-transform: uppercase;
  }
  .kicker { color: var(--signal); margin: 0 0 1.3rem; }
  h1 {
    font-weight: normal;
    font-size: clamp(3.8rem, 8.4vw, 8rem);
    line-height: .83;
    letter-spacing: -.07em;
    margin: 0;
  }
  h1 em { font-weight: normal; }
  .intro {
    max-width: 25ch;
    margin: 1.7rem 0 0;
    color: var(--muted);
    font-size: clamp(1.05rem, 2vw, 1.27rem);
    line-height: 1.55;
  }
  figure { margin: 0; min-width: 0; }
  .frame {
    padding: .5rem;
    border: 1px solid var(--rule);
    background: #0d120f;
  }
  svg { display: block; width: 100%; height: auto; }
  .scene { display: none; }
  [data-view="0"] #low, [data-view="1"] #blue, [data-view="2"] #morning { display: inline; }
  figcaption {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    align-items: start;
    gap: .75rem 1rem;
    padding-top: 1rem;
  }
  .readout { margin: 0; color: var(--signal); }
  .note { margin: .4rem 0 0; font-size: 1rem; line-height: 1.45; }
  button {
    border: 1px solid var(--rule);
    border-radius: 0;
    background: transparent;
    color: inherit;
    padding: .65rem .8rem;
    cursor: pointer;
    font: .69rem/1.4 var(--mono);
  }
  button:hover { border-color: var(--signal); color: var(--signal); }
  button:focus-visible { outline: 2px solid var(--signal); outline-offset: 4px; }
  footer { border-top: 1px solid var(--rule); }
  @media (max-width: 46rem) {
    main { grid-template-columns: 1fr; }
    h1 { font-size: clamp(3.8rem, 14vw, 6rem); }
    h1 br { display: none; }
  }
  @media (max-width: 23rem) {
    figcaption { grid-template-columns: 1fr; }
    button { justify-self: start; }
  }
</style>
</head>
<body>
<div class="page">
  <header class="strip">
    <span><span class="lamp" aria-hidden="true"></span>Night Window</span>
    <span>Open after dark</span>
  </header>

  <main>
    <div>
      <p class="kicker">A shoreline in three hours</p>
      <h1>Night<br> <em>Window</em></h1>
      <p class="intro">From here you can see the far bank. In daylight there’s a road over there, but at night it could be anywhere.</p>
    </div>

    <figure>
      <div class="frame" data-view="0">
        <svg viewBox="0 0 640 440" aria-hidden="true">
          <defs>
            <linearGradient id="green" x2="0" y2="1" gradientUnits="objectBoundingBox">
              <stop stop-color="#142823"/>
              <stop offset="1" stop-color="#578072"/>
            </linearGradient>
            <linearGradient id="indigo" x2="0" y2="1" gradientUnits="objectBoundingBox">
              <stop stop-color="#1b2040"/>
              <stop offset="1" stop-color="#727b9a"/>
            </linearGradient>
            <linearGradient id="rose" x2="0" y2="1" gradientUnits="objectBoundingBox">
              <stop stop-color="#49465f"/>
              <stop offset="1" stop-color="#dfa181"/>
            </linearGradient>
            <pattern id="grain" width="5" height="5" patternUnits="userSpaceOnUse">
              <path d="M0 .5h5" stroke="#101912" stroke-opacity=".16"/>
              <circle cx="2" cy="3" r=".45" fill="#fff" opacity=".14"/>
            </pattern>
            <path id="bank" d="M0 283l43-14 29 3 80-37 31 11 62-25 69 27 37-10 54 18 62-27 50 21 35-5 88 24v171H0z"/>
            <path id="near" d="M0 320l65-11 39 5 49-18 46 13 28-3 43 14 51-5 49 11 78-11 50 9 61-17 81 3v130H0z"/>
            <path id="ripples" d="M34 345h78m28-8h26m26 19h143m-78-22h29m40 7h101m17 29h106m-222 13h76m65 15h107m-510 6h112m-79-33h65m393-33h38m-264 77h54"/>
          </defs>

          <g class="scene" id="low">
            <rect width="640" height="440" fill="url(#green)"/>
            <g fill="#e9dfb5">
              <circle cx="83" cy="89" r="1.3"/><circle cx="168" cy="60" r="1"/>
              <circle cx="259" cy="125" r="1.4"/><circle cx="339" cy="74" r="1"/>
              <circle cx="538" cy="68" r="1.1"/><circle cx="576" cy="142" r="1.4"/>
              <circle cx="101" cy="160" r=".8"/><circle cx="427" cy="131" r="48"/>
            </g>
            <circle cx="427" cy="131" r="61" fill="none" stroke="#e9dfb5" opacity=".25"/>
            <use href="#bank" fill="#29433a"/>
            <use href="#near" fill="#182f29"/>
            <use href="#ripples" fill="none" stroke="#93ae96" opacity=".44"/>
            <path d="M400 349h57m-76 11h93m-70 13h49m-79 17h106m-86 18h61"
                  fill="none" stroke="#e9dfb5" opacity=".68"/>
          </g>

          <g class="scene" id="blue">
            <rect width="640" height="440" fill="url(#indigo)"/>
            <circle cx="178" cy="121" r="26" fill="#dadcdd"/>
            <circle cx="189" cy="112" r="25" fill="#353d60"/>
            <path d="M37 181h201m189-54h169m-262 55h115" stroke="#a8b1cb" opacity=".35"/>
            <use href="#bank" fill="#383d5b"/>
            <use href="#near" fill="#242b48"/>
            <use href="#ripples" fill="none" stroke="#9ca9c5" opacity=".5"/>
            <path d="M514 266h4m5 4h3m-9 69h9m-16 12h21" stroke="#efd19a" stroke-width="2"/>
          </g>

          <g class="scene" id="morning">
            <rect width="640" height="440" fill="url(#rose)"/>
            <circle cx="317" cy="241" r="55" fill="#ffce9e"/>
            <path d="M44 164h203m148 12h176m-426 30h96m170-6h189" stroke="#efba9f" opacity=".65"/>
            <use href="#bank" fill="#715b65"/>
            <use href="#near" fill="#483e51"/>
            <use href="#ripples" fill="none" stroke="#e8b6a1" opacity=".55"/>
            <path d="M292 347h56m-86 27h124m-102 22h75m-104 14h131" stroke="#ffce9e" opacity=".8"/>
            <path d="M462 137q9-5 16 3 8-7 16-1" fill="none" stroke="#463b4c" stroke-width="2"/>
          </g>

          <rect width="640" height="440" fill="url(#grain)"/>
          <path d="M18 37V18h19m566 0h19v19M18 403v19h19m566 0h19v-19"
                fill="none" stroke="#f0e5d2" opacity=".5"/>
        </svg>
      </div>

      <figcaption>
        <div aria-live="polite" aria-atomic="true">
          <p class="readout" id="hour">01 / Low tide</p>
          <p class="note" id="note">The moon is up. The mud still holds the shape of the boat.</p>
        </div>
        <button type="button" id="dial" hidden>Turn the dial <span aria-hidden="true">↻</span></button>
      </figcaption>
    </figure>
  </main>

  <footer>
    <span>Field notes from an invented coast</span>
    <span>No clock connected</span>
  </footer>
</div>
<script>
  const hours = [
    ["01 / Low tide", "The moon is up. The mud still holds the shape of the boat."],
    ["02 / Blue hour", "Someone across the water has left the kitchen light on."],
    ["03 / First light", "A gull crosses the whole window without moving its wings."]
  ];
  const frame = document.querySelector(".frame");
  const hour = document.getElementById("hour");
  const note = document.getElementById("note");
  const dial = document.getElementById("dial");
  let view = 0;
  dial.addEventListener("click", () => {
    view = (view + 1) % hours.length;
    frame.dataset.view = String(view);
    hour.textContent = hours[view][0];
    note.textContent = hours[view][1];
  });
  dial.hidden = false;
</script>
</body>
</html>
```
What: Night Window looks out on an invented shoreline, with a dial that changes the hour, the view, and the note beneath it.