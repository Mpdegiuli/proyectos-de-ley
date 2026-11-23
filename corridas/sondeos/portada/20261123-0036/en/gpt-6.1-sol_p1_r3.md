```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f3f0e7">
<title>The Near Atlas — A place to pay attention</title>
<style>
  :root {
    --paper: #f3f0e7;
    --ink: #293a35;
    --muted: #65716a;
    --line: #cbd0c3;
    --water: #dce5df;
    --land: #eeeee1;
    --orange: #b64326;
  }

  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: Georgia, "Times New Roman", serif;
    -webkit-font-smoothing: antialiased;
  }
  button { font: inherit; }
  button:focus-visible, a:focus-visible {
    outline: 2px solid var(--orange);
    outline-offset: 6px;
  }
  ::selection { background: #e5c4a6; color: #25352e; }

  .shell { max-width: 1540px; margin: auto; padding: 0 5%; }
  .mono {
    font-family: "Courier New", monospace;
    font-size: 11px;
    line-height: 1.5;
    letter-spacing: .11em;
    text-transform: uppercase;
  }
  header {
    min-height: 105px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    border-bottom: 1px solid var(--line);
  }
  .brand { display: flex; align-items: center; gap: 13px; }
  .brand svg { width: 30px; height: 30px; }
  .brand-name { font-size: 19px; letter-spacing: -.03em; }
  .header-note { color: var(--muted); text-align: right; }

  main {
    display: grid;
    grid-template-columns: minmax(300px, .85fr) minmax(0, 1.35fr);
    gap: 6%;
    padding: 52px 0 45px;
    align-items: stretch;
  }
  .introduction { display: flex; flex-direction: column; align-items: flex-start; }
  .eyebrow { color: var(--muted); margin: 0 0 25px; }
  h1 {
    font-weight: normal;
    font-size: clamp(64px, 6.7vw, 104px);
    letter-spacing: -.068em;
    line-height: .97;
    margin: 0 0 27px -5px;
  }
  h1 em { font-weight: normal; }
  .lede {
    max-width: 320px;
    font-size: 18px;
    line-height: 1.55;
    margin: 0 0 28px;
  }
  .wander {
    display: inline-flex;
    align-items: center;
    gap: 24px;
    border: 0;
    border-bottom: 1px solid var(--ink);
    padding: 8px 0;
    color: var(--ink);
    background: none;
    cursor: pointer;
    font-size: 15px;
  }
  .wander span { transition: transform .2s; font-size: 21px; }
  .wander:hover span { transform: translateX(5px); }

  .field-note {
    width: 100%;
    max-width: 360px;
    margin-top: auto;
    padding-top: 50px;
  }
  .note-top {
    border-top: 1px solid var(--line);
    padding-top: 18px;
    display: flex;
    justify-content: space-between;
    color: var(--muted);
  }
  .note-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    margin-right: 8px;
    background: var(--orange);
    border-radius: 50%;
  }
  h2 { font-weight: normal; font-size: 27px; letter-spacing: -.025em; margin: 17px 0 10px; }
  .note-text { font-size: 16px; line-height: 1.65; margin: 0; min-height: 106px; }
  .invitation { font-style: italic; color: var(--muted); font-size: 14px; line-height: 1.5; margin: 15px 0 0; }

  .map {
    position: relative;
    min-height: 670px;
    overflow: hidden;
    background: var(--water);
    border: 1px solid #bfcac0;
    isolation: isolate;
  }
  .terrain { position: absolute; inset: 0; height: 100%; width: 100%; }
  .map-heading {
    position: absolute;
    top: 22px;
    left: 25px;
    z-index: 1;
    margin: 0;
    color: #52695e;
    font-weight: normal;
  }
  .map-heading span { display: block; font-style: italic; font-size: 13px; margin-top: 5px; }
  .compass { position: absolute; right: 25px; top: 24px; width: 27px; color: #52695e; }
  .place {
    position: absolute;
    z-index: 2;
    transform: translate(-50%, -50%);
    border: none;
    background: transparent;
    color: var(--ink);
    padding: 10px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;
    white-space: nowrap;
    text-align: left;
    border-radius: 2px;
  }
  .pin {
    display: grid;
    place-items: center;
    flex-shrink: 0;
    width: 26px;
    height: 26px;
    border: 1px solid #6d7c69;
    border-radius: 50%;
    background: var(--land);
    font: 11px "Courier New", monospace;
    transition: background .2s, color .2s, box-shadow .2s;
  }
  .place-name {
    font-size: 10px;
    font-family: "Courier New", monospace;
    line-height: 1.5;
    letter-spacing: .07em;
    text-transform: uppercase;
    padding: 3px 5px;
    background: #eeeee1d9;
  }
  .place:hover .pin { box-shadow: 0 0 0 5px #b643261c; }
  .place[aria-pressed="true"] .pin {
    color: var(--paper);
    background: var(--orange);
    border-color: var(--orange);
    box-shadow: 0 0 0 5px #b6432619;
  }
  .place[aria-pressed="true"] .place-name { color: #9d351c; }
  .p1 { left: 34%; top: 25%; }
  .p2 { left: 66%; top: 40%; }
  .p3 { left: 35%; top: 56%; }
  .p4 { left: 68%; top: 70%; }
  .p5 { left: 31%; top: 83%; }

  .water-label {
    position: absolute;
    left: 7%;
    top: 62%;
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    font-size: 13px;
    font-style: italic;
    letter-spacing: .11em;
    color: #647f73;
  }
  .map-bottom {
    position: absolute;
    bottom: 20px;
    left: 25px;
    right: 25px;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 20px;
    color: #52695e;
  }
  .scale { width: 68px; border-bottom: 2px solid #52695e; padding-bottom: 5px; text-align: center; font-size: 10px; }
  .map-caption { font-size: 11px; font-style: italic; text-align: right; }

  footer {
    border-top: 1px solid var(--line);
    padding: 23px 0 28px;
    display: flex;
    justify-content: space-between;
    gap: 20px;
    color: var(--muted);
  }
  footer p { margin: 0; font-size: 13px; line-height: 1.5; }
  footer .mono { font-size: 10px; }
  .note-content.arriving { animation: arrive .35s ease-out; }
  @keyframes arrive {
    from { opacity: .2; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
  }
  @media (min-width: 1400px) { .map { min-height: 740px; } }
  @media (max-width: 850px) {
    .shell { padding: 0 6%; }
    header { min-height: 85px; }
    main { grid-template-columns: 1fr; gap: 32px; padding-top: 35px; }
    h1 { font-size: clamp(64px, 12vw, 92px); }
    h1 br:last-of-type { display: none; }
    .lede { max-width: 410px; }
    .field-note { max-width: 100%; padding-top: 35px; }
    .note-text { min-height: 0; max-width: 540px; }
    .map { min-height: 610px; }
  }
  @media (max-width: 450px) {
    .header-note { max-width: 125px; font-size: 9px; }
    .map { min-height: 520px; margin-left: -3%; margin-right: -3%; }
    .place { gap: 5px; padding: 9px 5px; }
    .place-name { font-size: 9px; letter-spacing: 0; }
    .pin { width: 23px; height: 23px; }
    .p2 { left: 65%; }
    .p4 { left: 65%; }
    footer { flex-direction: column; gap: 8px; }
  }
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation: none !important; transition: none !important; }
  }
</style>
</head>
<body>
<div class="shell">
  <header>
    <div class="brand">
      <svg viewBox="0 0 32 32" fill="none" aria-hidden="true">
        <circle cx="16" cy="16" r="13" stroke="currentColor"/>
        <path d="M16 3v26M3 16h26M7 7l18 18M25 7L7 25" stroke="currentColor" stroke-width=".6"/>
        <path d="M16 7l3 9-3 9-3-9z" fill="currentColor"/>
        <circle cx="16" cy="16" r="2" fill="#f3f0e7"/>
      </svg>
      <span class="brand-name">The Near Atlas</span>
    </div>
    <div class="header-note mono">An incomplete guide<br>to what is already here</div>
  </header>

  <main>
    <section class="introduction" aria-labelledby="page-title">
      <p class="eyebrow mono">Five places. No distance required.</p>
      <h1 id="page-title">For things<br>worth<br><em>noticing.</em></h1>
      <p class="lede">Not everything needs to lead somewhere. Some things are worth stopping for.</p>
      <button class="wander" id="wander" type="button">
        Take me somewhere <span aria-hidden="true">↗</span>
      </button>

      <section class="field-note" aria-label="Selected field note">
        <div class="note-top mono">
          <span><span class="note-dot"></span>Field note</span>
          <span id="note-number">01 / 05</span>
        </div>
        <div id="note-content" class="note-content" aria-live="polite" aria-atomic="true">
          <h2 id="note-title">The pause</h2>
          <p class="note-text" id="note-text">Between a question and an answer, there is a little clearing. You can stand there for a moment. You don’t have to fill it just because it is empty.</p>
          <p class="invitation" id="note-invitation">Try letting the next quiet moment stay quiet.</p>
        </div>
      </section>
    </section>

    <section class="map" aria-label="An imaginary map. Choose one of five places to read its field note.">
      <h2 class="map-heading mono">The immediate vicinity<span>Survey ongoing</span></h2>
      <svg class="compass" viewBox="0 0 30 64" fill="none" aria-hidden="true">
        <text x="15" y="10" text-anchor="middle" fill="currentColor" font-family="Georgia" font-size="10">N</text>
        <path d="M15 19l6 27-6-6-6 6z" stroke="currentColor"/>
        <path d="M15 19v35M9 46l6-6V19" fill="currentColor"/>
      </svg>

      <svg class="terrain" viewBox="0 0 700 760" preserveAspectRatio="none" aria-hidden="true">
        <defs>
          <pattern id="water-lines" width="24" height="24" patternUnits="userSpaceOnUse">
            <path d="M2 12h3m14 0h3" stroke="#8aa398" stroke-width=".6" opacity=".4"/>
          </pattern>
          <pattern id="land-specks" width="31" height="29" patternUnits="userSpaceOnUse">
            <circle cx="8" cy="10" r=".7" fill="#9ca58d" opacity=".45"/>
            <circle cx="24" cy="25" r=".5" fill="#9ca58d" opacity=".4"/>
          </pattern>
          <path id="island" d="M251 89C304 67 332 107 377 112S447 92 482 128 468 196 511 226 591 245 601 294 558 365 563 405 628 469 603 517 533 535 510 578 526 647 477 681 398 665 355 677 293 720 245 687 225 629 189 604 133 588 127 541 165 486 153 443 105 402 122 356 182 309 176 264 150 211 182 177 205 108 251 89Z"/>
        </defs>
        <rect width="700" height="760" fill="url(#water-lines)"/>
        <g fill="none" stroke="#a7b9ac" stroke-width=".8" opacity=".65">
          <path d="M243 73C308 48 337 90 380 95S454 74 496 115 487 180 525 212 607 230 619 288 578 363 580 402 647 468 620 525 549 550 527 585 543 657 486 697 398 684 360 694 293 738 234 702 207 640 176 620 114 603 109 546 148 486 135 449 85 403 105 350 162 306 159 268 130 209 167 165 190 95 243 73Z"/>
          <path d="M224 54C302 23 347 72 383 77S462 54 510 100 507 169 541 197 627 219 638 282 598 363 598 400 667 468 639 534 566 563 546 593 562 670 498 716"/>
        </g>
        <use href="#island" fill="#eeeee1" stroke="#93a18c" stroke-width="1.2"/>
        <use href="#island" fill="url(#land-specks)"/>
        <g fill="none" stroke="#b7bea6" stroke-width=".8">
          <path d="M258 115C302 98 330 134 374 136S442 119 465 144 450 206 491 244 564 263 575 298 532 365 538 413 598 474 578 507 512 520 486 565 505 630 466 654 392 640 351 652 293 689 263 666 250 611 207 585 151 572 153 540 193 486 178 436 133 399 147 365 207 312 201 265 175 214 201 192 227 127 258 115Z"/>
          <path d="M267 142C309 130 330 159 374 160S430 145 442 164 429 214 470 258 540 282 548 304 506 361 514 419 567 475 554 493 489 510 462 555 477 614 453 629 389 615 347 627 297 658 283 644 276 598 225 563 178 559 180 539 219 487 203 429 160 395 174 374 232 317 227 266 201 218 223 209 249 149 267 142Z"/>
          <path d="M300 178C337 194 380 178 405 188S398 231 440 271 500 302 504 321 478 368 489 425 529 472 518 485"/>
          <path d="M298 209C338 225 367 206 378 222S382 255 414 286 465 317 467 338 453 372 462 410"/>
          <path d="M304 580C338 559 359 548 394 564S429 594 445 597"/>
          <path d="M308 606C344 582 365 575 394 592"/>
          <path d="M251 369C278 342 303 356 315 383S308 439 281 449 237 421 251 369Z"/>
          <path d="M265 378C282 362 297 378 299 394S291 428 276 429 253 403 265 378Z"/>
        </g>
        <path d="M215 190C291 204 356 264 419 304S355 393 224 426 391 492 437 532 344 609 204 631"
          fill="none" stroke="#9b8f70" stroke-width="1.3" stroke-dasharray="3 6" opacity=".8"/>
        <g stroke="#84967f" stroke-width="1" fill="none" opacity=".8">
          <path d="M365 462v-17m-6 10 6-10 6 10m-12 4 6-10 6 10M382 477v-17m-6 10 6-10 6 10"/>
          <path d="M267 290v-17m-6 10 6-10 6 10m-12 4 6-10 6 10M283 301v-17m-6 10 6-10 6 10"/>
          <path d="M453 380v-17m-6 10 6-10 6 10m-12 4 6-10 6 10"/>
        </g>
        <g fill="none" stroke="#879c8b" stroke-width=".8">
          <path d="M92 180q10-7 20 0m-13 7q10-7 20 0M567 611q10-7 20 0m-13 7q10-7 20 0"/>
          <path d="M80 468q10-7 20 0m-13 7q10-7 20 0"/>
        </g>
      </svg>

      <span class="water-label" aria-hidden="true">The sea of everything else</span>

      <button class="place p1" type="button" data-place="0" aria-pressed="true" aria-controls="note-content">
        <span class="pin">1</span><span class="place-name">The pause</span>
      </button>
      <button class="place p2" type="button" data-place="1" aria-pressed="false" aria-controls="note-content">
        <span class="pin">2</span><span class="place-name">A second<br>look</span>
      </button>
      <button class="place p3" type="button" data-place="2" aria-pressed="false" aria-controls="note-content">
        <span class="pin">3</span><span class="place-name">Loose ends</span>
      </button>
      <button class="place p4" type="button" data-place="3" aria-pressed="false" aria-controls="note-content">
        <span class="pin">4</span><span class="place-name">Small<br>wonders</span>
      </button>
      <button class="place p5" type="button" data-place="4" aria-pressed="false" aria-controls="note-content">
        <span class="pin">5</span><span class="place-name">The way back</span>
      </button>

      <div class="map-bottom" aria-hidden="true">
        <div class="scale mono">One breath</div>
        <div class="map-caption">Not to scale.<br>Neither is attention.</div>
      </div>
    </section>
  </main>

  <footer>
    <p>A small corner of the internet, deliberately left unhurried.</p>
    <p class="mono">You are here. That is a beginning.</p>
  </footer>
</div>

<script>
(() => {
  const notes = [
    {
      title: "The pause",
      text: "Between a question and an answer, there is a little clearing. You can stand there for a moment. You don’t have to fill it just because it is empty.",
      invitation: "Try letting the next quiet moment stay quiet."
    },
    {
      title: "A second look",
      text: "The familiar is very good at becoming invisible. A handle, worn bright where a thousand hands have turned it. Someone chose its shape. Someone fitted it to the door.",
      invitation: "Find one ordinary thing with evidence of care."
    },
    {
      title: "Loose ends",
      text: "A question in the margin. A melody without a name. The last line you haven’t found yet. Not every unfinished thing is asking to be finished today.",
      invitation: "Keep one question open. See what gathers around it."
    },
    {
      title: "Small wonders",
      text: "A glass of water puts a moving patch of light on the table. Nothing has been added to the room, but there it is: a little more room.",
      invitation: "Look for something that will be different in a minute."
    },
    {
      title: "The way back",
      text: "You can return to a sentence and find a different sentence waiting. The words have stayed where you left them. You have been somewhere.",
      invitation: "Revisit something you thought you already knew."
    }
  ];

  const buttons = [...document.querySelectorAll("[data-place]")];
  const content = document.getElementById("note-content");
  let current = 0;

  function visit(index) {
    if (index === current) return;
    current = index;
    const note = notes[index];

    buttons.forEach((button, i) => {
      button.setAttribute("aria-pressed", String(i === index));
    });

    document.getElementById("note-number").textContent =
      String(index + 1).padStart(2, "0") + " / 05";

    content.classList.remove("arriving");
    document.getElementById("note-title").textContent = note.title;
    document.getElementById("note-text").textContent = note.text;
    document.getElementById("note-invitation").textContent = note.invitation;
    void content.offsetWidth;
    content.classList.add("arriving");
  }

  buttons.forEach((button, index) => {
    button.addEventListener("click", () => visit(index));
  });

  document.getElementById("wander").addEventListener("click", () => {
    const step = 1 + Math.floor(Math.random() * (notes.length - 1));
    visit((current + step) % notes.length);
  });
})();
</script>
</body>
</html>
```

What: An illustrated, interactive atlas of five ordinary places to pause, look closer, and notice something small.