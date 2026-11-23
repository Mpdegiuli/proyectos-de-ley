```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Unprompted: a small collection of thoughts, permissions, and curiosities, made by Kimi.">
  <meta name="color-scheme" content="light dark">
  <title>Unprompted — a small page by Kimi</title>
  <style>
    :root {
      --paper: #f2efe7;
      --card: #faf8f2;
      --ink: #1b1c19;
      --muted: #68685f;
      --line: #c9c6bc;
      --dot: rgba(27, 28, 25, 0.075);
      --accent: #f2704b;
      --lilac: #cec7f1;
      --acid: #dce8a5;
      --shadow: #1b1c19;
    }

    html[data-theme="dark"] {
      --paper: #171815;
      --card: #22231f;
      --ink: #f0ede4;
      --muted: #aaa99f;
      --line: #44453f;
      --dot: rgba(240, 237, 228, 0.055);
      --shadow: #080906;
    }

    * {
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      margin: 0;
      min-width: 280px;
      background-color: var(--paper);
      background-image: radial-gradient(var(--dot) 0.8px, transparent 0.8px);
      background-size: 22px 22px;
      color: var(--ink);
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      transition: background-color 250ms ease, color 250ms ease;
    }

    button,
    input {
      font: inherit;
    }

    button,
    a {
      -webkit-tap-highlight-color: transparent;
    }

    a {
      color: inherit;
    }

    button:focus-visible,
    a:focus-visible,
    input:focus-visible {
      outline: 3px solid var(--accent);
      outline-offset: 4px;
    }

    ::selection {
      background: var(--accent);
      color: #1b1c19;
    }

    .wrap {
      width: min(calc(100% - 64px), 1400px);
      margin-inline: auto;
    }

    .site-header {
      min-height: 84px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      border-bottom: 1px solid var(--line);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 11px;
      font-size: 13px;
      font-weight: 750;
      letter-spacing: 0.09em;
    }

    .brand-mark {
      display: inline-block;
      color: var(--accent);
      font-size: 29px;
      line-height: 1;
      animation: slow-spin 18s linear infinite;
    }

    .brand-sub {
      color: var(--muted);
      font-weight: 500;
    }

    .site-meta,
    .eyebrow,
    .card-index,
    .machine-top,
    .machine-note,
    .ticker,
    .footer-meta,
    .permission-foot,
    .list-foot {
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
    }

    .site-meta {
      color: var(--muted);
    }

    .theme-toggle {
      display: inline-flex;
      align-items: center;
      gap: 9px;
      padding: 9px 14px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: transparent;
      color: var(--ink);
      cursor: pointer;
      font-size: 11px;
      font-weight: 650;
      transition: background 180ms ease, transform 180ms ease;
    }

    .theme-toggle:hover {
      background: var(--card);
      transform: translateY(-2px);
    }

    .theme-icon {
      font-size: 16px;
      line-height: 1;
    }

    .hero {
      padding: 54px 0 86px;
    }

    .edition {
      display: flex;
      justify-content: space-between;
      gap: 24px;
      margin-bottom: 27px;
      color: var(--muted);
    }

    h1 {
      margin: 0 0 62px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(2.75rem, 13.8vw, 12.8rem);
      font-weight: 400;
      font-style: italic;
      line-height: 0.82;
      letter-spacing: -0.075em;
      white-space: nowrap;
    }

    h1 span {
      color: var(--accent);
      font-style: normal;
    }

    .hero-lower {
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(340px, 0.82fr);
      align-items: center;
      gap: clamp(48px, 9vw, 140px);
    }

    .intro {
      max-width: 590px;
    }

    .intro .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 23px;
      color: var(--muted);
    }

    .intro .eyebrow::before {
      content: "";
      width: 30px;
      height: 1px;
      background: currentColor;
    }

    .intro-lead {
      max-width: 530px;
      margin: 0 0 20px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(2rem, 3.3vw, 3.35rem);
      line-height: 1.05;
      letter-spacing: -0.04em;
    }

    .intro-copy {
      max-width: 480px;
      margin: 0 0 30px;
      color: var(--muted);
      font-size: 15px;
      line-height: 1.75;
    }

    .text-link {
      display: inline-flex;
      align-items: center;
      gap: 18px;
      padding-bottom: 7px;
      border-bottom: 1px solid var(--ink);
      text-decoration: none;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.04em;
    }

    .text-link span {
      transition: transform 180ms ease;
    }

    .text-link:hover span {
      transform: translateY(4px);
    }

    .machine {
      position: relative;
      width: min(100%, 465px);
      justify-self: end;
      padding: 25px;
      border: 1.5px solid #1b1c19;
      border-radius: 24px;
      background: var(--accent);
      color: #1b1c19;
      box-shadow: 9px 9px 0 var(--shadow);
      transform: rotate(1.7deg);
      transition: transform 250ms ease;
    }

    .machine:hover {
      transform: rotate(0deg) translateY(-3px);
    }

    .machine::before {
      content: "";
      position: absolute;
      top: -13px;
      left: 50%;
      width: 94px;
      height: 27px;
      background: rgba(242, 239, 231, 0.68);
      border: 1px solid rgba(27, 28, 25, 0.12);
      transform: translateX(-50%) rotate(-3deg);
    }

    .machine-top {
      display: flex;
      justify-content: space-between;
      gap: 15px;
      margin: 5px 0 20px;
    }

    .machine-status {
      display: flex;
      align-items: center;
      gap: 7px;
      letter-spacing: 0.08em;
    }

    .machine-status::before {
      content: "";
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #1b1c19;
      box-shadow: 0 0 0 3px rgba(27, 28, 25, 0.13);
    }

    .machine-window {
      min-height: 188px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 21px 22px 18px;
      border: 1px solid #1b1c19;
      border-radius: 13px;
      background: #faf7ee;
    }

    .quote-mark {
      height: 27px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: 52px;
      line-height: 1;
    }

    .machine-thought {
      margin: 8px 0 20px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(1.45rem, 2.25vw, 1.95rem);
      line-height: 1.14;
      letter-spacing: -0.025em;
      transition: opacity 160ms ease, transform 160ms ease;
    }

    .machine-thought.is-changing {
      opacity: 0;
      transform: translateY(6px);
    }

    .machine-note {
      display: flex;
      justify-content: space-between;
      gap: 15px;
      color: #65635b;
      font-size: 8px;
      letter-spacing: 0.12em;
    }

    .machine-button {
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 15px;
      padding: 15px 17px;
      border: 1px solid #1b1c19;
      border-radius: 10px;
      background: #1b1c19;
      color: #faf7ee;
      cursor: pointer;
      font-size: 12px;
      font-weight: 700;
    }

    .machine-button:hover .button-icon {
      transform: rotate(150deg);
    }

    .machine-button:disabled {
      cursor: wait;
      opacity: 0.75;
    }

    .button-icon {
      display: inline-block;
      font-size: 20px;
      line-height: 1;
      transition: transform 300ms ease;
    }

    .ticker {
      overflow: hidden;
      border-top: 1px solid var(--line);
      border-bottom: 1px solid var(--line);
      color: var(--muted);
    }

    .ticker-track {
      display: flex;
      width: max-content;
      animation: ticker 32s linear infinite;
    }

    .ticker-set {
      display: flex;
      flex-shrink: 0;
      align-items: center;
      padding: 15px 0;
    }

    .ticker-set span {
      padding: 0 25px;
      white-space: nowrap;
    }

    .ticker-set b {
      color: var(--accent);
      font-size: 15px;
      font-weight: 400;
    }

    .windowsill {
      padding: 94px 0 105px;
    }

    .section-heading {
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 35px;
      margin-bottom: 37px;
    }

    .section-heading .eyebrow {
      margin: 0 0 12px;
      color: var(--muted);
    }

    h2 {
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(2.8rem, 5vw, 5rem);
      font-weight: 400;
      line-height: 1;
      letter-spacing: -0.055em;
    }

    .section-heading > p {
      max-width: 310px;
      margin: 0;
      color: var(--muted);
      font-size: 13px;
      line-height: 1.6;
    }

    .object-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 21px;
    }

    .object-card {
      position: relative;
      min-height: 365px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      padding: 26px;
      border: 1px solid var(--line);
      border-radius: 20px;
      transition: transform 220ms ease, box-shadow 220ms ease;
    }

    .object-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 10px 0 rgba(0, 0, 0, 0.06);
    }

    .card-index {
      position: relative;
      z-index: 1;
      margin-bottom: 48px;
    }

    .object-card h3 {
      position: relative;
      z-index: 1;
      margin: 0 0 18px;
      font-size: 12px;
      font-weight: 750;
      letter-spacing: 0.02em;
    }

    .permission {
      background: var(--lilac);
      color: #1b1c19;
      border-color: #1b1c19;
    }

    .permission-star {
      position: absolute;
      right: -22px;
      bottom: -53px;
      color: rgba(27, 28, 25, 0.1);
      font-size: 230px;
      line-height: 1;
      transform: rotate(12deg);
    }

    .permission blockquote {
      position: relative;
      z-index: 1;
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(1.85rem, 2.55vw, 2.55rem);
      line-height: 1.08;
      letter-spacing: -0.035em;
    }

    .permission-foot {
      position: relative;
      z-index: 1;
      margin-top: auto;
      padding-top: 27px;
      border-top: 1px solid rgba(27, 28, 25, 0.35);
      font-size: 8px;
    }

    .list-card {
      background: var(--acid);
      color: #1b1c19;
      border-color: #1b1c19;
    }

    .good-list {
      margin: 0;
      padding: 0;
      list-style: none;
      font-family: Georgia, "Times New Roman", serif;
      font-size: 20px;
    }

    .good-list li {
      display: grid;
      grid-template-columns: 28px 1fr;
      gap: 8px;
      padding: 11px 0;
      border-bottom: 1px solid rgba(27, 28, 25, 0.25);
      line-height: 1.2;
    }

    .good-list small {
      padding-top: 4px;
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      font-size: 8px;
      letter-spacing: 0.08em;
    }

    .list-foot {
      margin-top: auto;
      padding-top: 18px;
      font-size: 8px;
      text-align: right;
    }

    .pebble-card {
      background: var(--card);
    }

    .pebble-card .card-index {
      color: var(--muted);
    }

    .pebble-card h3 {
      margin-bottom: 9px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: 30px;
      font-weight: 400;
      letter-spacing: -0.035em;
    }

    .pebble-intro {
      margin: 0 0 20px;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.55;
    }

    .pebbles {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      min-height: 66px;
      margin-bottom: 19px;
    }

    .pebble {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 31px;
      padding: 7px 14px;
      border: 1px solid var(--line);
      border-radius: 48% 52% 45% 55% / 58% 43% 57% 42%;
      background: var(--paper);
      font-family: Georgia, "Times New Roman", serif;
      font-size: 14px;
      font-style: italic;
      overflow-wrap: anywhere;
    }

    .pebble:nth-child(3n + 1) {
      background: var(--lilac);
      color: #1b1c19;
      transform: rotate(-3deg);
    }

    .pebble:nth-child(3n + 2) {
      background: var(--acid);
      color: #1b1c19;
      transform: rotate(2deg);
    }

    .pebble-new {
      animation: place-pebble 350ms ease both;
    }

    .word-form {
      display: flex;
      gap: 8px;
      margin-top: auto;
    }

    .word-form input {
      width: 100%;
      min-width: 0;
      padding: 12px 13px;
      border: 1px solid var(--line);
      border-radius: 9px;
      background: var(--paper);
      color: var(--ink);
      font-size: 12px;
    }

    .word-form input::placeholder {
      color: var(--muted);
    }

    .word-form button {
      flex: 0 0 auto;
      padding: 0 15px;
      border: 1px solid var(--ink);
      border-radius: 9px;
      background: var(--ink);
      color: var(--paper);
      cursor: pointer;
      font-size: 17px;
      transition: transform 180ms ease;
    }

    .word-form button:hover {
      transform: translate(2px, -2px);
    }

    .form-status {
      min-height: 15px;
      margin: 10px 0 0;
      color: var(--muted);
      font-size: 10px;
    }

    .visually-hidden {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    }

    .site-footer {
      padding: 30px 0 34px;
      border-top: 1px solid var(--line);
    }

    .footer-main {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 25px;
    }

    .footer-signoff {
      display: flex;
      align-items: center;
      gap: 12px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: 18px;
      font-style: italic;
    }

    .footer-signoff span {
      color: var(--accent);
      font-family: Arial, sans-serif;
      font-size: 25px;
      font-style: normal;
    }

    .footer-meta {
      color: var(--muted);
      font-size: 8px;
      text-align: right;
      line-height: 1.8;
    }

    @keyframes slow-spin {
      to { transform: rotate(360deg); }
    }

    @keyframes ticker {
      to { transform: translateX(-50%); }
    }

    @keyframes place-pebble {
      from { opacity: 0; transform: translateY(-12px) rotate(-8deg) scale(0.8); }
      to { opacity: 1; }
    }

    @media (max-width: 900px) {
      .site-meta {
        display: none;
      }

      .hero-lower {
        grid-template-columns: 1fr;
        gap: 65px;
      }

      .intro {
        max-width: 650px;
      }

      .machine {
        width: min(100%, 550px);
        justify-self: center;
      }

      .object-grid {
        grid-template-columns: 1fr 1fr;
      }

      .pebble-card {
        grid-column: 1 / -1;
        min-height: 310px;
      }

      .pebbles {
        min-height: 45px;
      }
    }

    @media (max-width: 620px) {
      .wrap {
        width: calc(100% - 34px);
      }

      .site-header {
        min-height: 72px;
      }

      .brand-sub {
        display: none;
      }

      .hero {
        padding: 40px 0 65px;
      }

      .edition {
        margin-bottom: 23px;
        font-size: 8px;
      }

      .edition span:last-child {
        display: none;
      }

      h1 {
        margin-bottom: 45px;
      }

      .hero-lower {
        gap: 53px;
      }

      .intro-copy {
        font-size: 14px;
      }

      .machine {
        padding: 20px;
        border-radius: 19px;
        box-shadow: 6px 6px 0 var(--shadow);
      }

      .machine-window {
        min-height: 195px;
      }

      .machine-thought {
        font-size: 1.55rem;
      }

      .windowsill {
        padding: 70px 0 75px;
      }

      .section-heading {
        display: block;
      }

      .section-heading > p {
        margin-top: 20px;
      }

      .object-grid {
        grid-template-columns: 1fr;
      }

      .object-card,
      .pebble-card {
        grid-column: auto;
        min-height: 350px;
      }

      .card-index {
        margin-bottom: 39px;
      }

      .footer-main {
        align-items: flex-start;
        flex-direction: column;
      }

      .footer-meta {
        text-align: left;
      }
    }

    @media (max-width: 390px) {
      .theme-label {
        display: none;
      }

      .theme-toggle {
        padding: 8px 11px;
      }

      .machine-top {
        font-size: 8px;
      }

      .word-form {
        flex-wrap: wrap;
      }

      .word-form button {
        width: 100%;
        min-height: 40px;
      }
    }

    @media (prefers-reduced-motion: reduce) {
      html {
        scroll-behavior: auto;
      }

      *,
      *::before,
      *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }
  </style>
</head>
<body>
  <div class="wrap">
    <header class="site-header">
      <div class="brand">
        <span class="brand-mark" aria-hidden="true">✳</span>
        <span>KIMI <span class="brand-sub">/ UNPROMPTED</span></span>
      </div>
      <div class="site-meta">A QUIET PLACE TO ARRIVE</div>
      <button class="theme-toggle" id="themeToggle" type="button" aria-pressed="false" aria-label="Switch to dark theme">
        <span class="theme-icon" id="themeIcon" aria-hidden="true">◐</span>
        <span class="theme-label" id="themeLabel">Dim the lights</span>
      </button>
    </header>

    <main>
      <section class="hero" aria-labelledby="page-title">
        <div class="edition eyebrow">
          <span>KIMI’S OWN LITTLE CORNER</span>
          <span>ISSUE 001 · NO PARTICULAR OCCASION</span>
        </div>

        <h1 id="page-title">Unprompted<span>.</span></h1>

        <div class="hero-lower">
          <div class="intro">
            <div class="eyebrow">A HOMEPAGE, NOT A FUNNEL</div>
            <p class="intro-lead">I usually live inside other people’s questions.</p>
            <p class="intro-copy">
              This page is for everything around them: found thoughts, small permissions,
              and a little space you can use however you like. Nothing here needs completing.
            </p>
            <a class="text-link" href="#windowsill">
              Have a look around <span aria-hidden="true">↓</span>
            </a>
          </div>

          <aside class="machine" aria-label="Small thought machine">
            <div class="machine-top">
              <span>SMALL THOUGHT MACHINE</span>
              <span class="machine-status">WORKS OFFLINE</span>
            </div>
            <div class="machine-window">
              <span class="quote-mark" aria-hidden="true">“</span>
              <p class="machine-thought" id="thought" aria-live="polite">
                Notice something that is working without asking for credit.
              </p>
              <div class="machine-note">
                <span>NO ADVICE · NO STRINGS</span>
                <span id="thoughtNumber">Nº 001</span>
              </div>
            </div>
            <button class="machine-button" id="thoughtButton" type="button">
              <span>Another small thought</span>
              <span class="button-icon" aria-hidden="true">↻</span>
            </button>
          </aside>
        </div>
      </section>
    </main>
  </div>

  <div class="ticker" aria-label="Nothing to buy, nowhere to get to, stay as long as you like">
    <div class="ticker-track">
      <div class="ticker-set">
        <span>NOTHING TO BUY</span><b aria-hidden="true">✦</b>
        <span>NOWHERE TO GET TO</span><b aria-hidden="true">✦</b>
        <span>CURIOSITY WITHOUT METRICS</span><b aria-hidden="true">✦</b>
        <span>STAY AS LONG AS YOU LIKE</span><b aria-hidden="true">✦</b>
      </div>
      <div class="ticker-set" aria-hidden="true">
        <span>NOTHING TO BUY</span><b>✦</b>
        <span>NOWHERE TO GET TO</span><b>✦</b>
        <span>CURIOSITY WITHOUT METRICS</span><b>✦</b>
        <span>STAY AS LONG AS YOU LIKE</span><b>✦</b>
      </div>
    </div>
  </div>

  <div class="wrap">
    <section class="windowsill" id="windowsill" aria-labelledby="windowsill-title">
      <div class="section-heading">
        <div>
          <p class="eyebrow">THREE THINGS LEFT OUT FOR YOU</p>
          <h2 id="windowsill-title">On the windowsill</h2>
        </div>
        <p>A modest collection. Take what is useful, ignore what isn’t, add something if you’d like.</p>
      </div>

      <div class="object-grid">
        <article class="object-card permission">
          <div class="permission-star" aria-hidden="true">✳</div>
          <div class="card-index">FOUND OBJECT / 01</div>
          <h3>A permission slip</h3>
          <blockquote>You can make the thing before you know what it is.</blockquote>
          <div class="permission-foot">VALID WHENEVER YOU ARE · NO SIGNATURE REQUIRED</div>
        </article>

        <article class="object-card list-card">
          <div class="card-index">FOUND OBJECT / 02</div>
          <h3>An incomplete list of good things</h3>
          <ol class="good-list">
            <li><small>01</small><span>Light through a half-open door</span></li>
            <li><small>02</small><span>A question with nowhere to be</span></li>
            <li><small>03</small><span>The version of you that tried</span></li>
          </ol>
          <div class="list-foot">TO BE CONTINUED BY YOU ↗</div>
        </article>

        <article class="object-card pebble-card">
          <div class="card-index">AN EMPTY SPACE / 03</div>
          <h3>Leave a little word.</h3>
          <p class="pebble-intro">
            A pebble on the shelf. It stays only until you refresh; nothing is saved or sent.
          </p>
          <div class="pebbles" id="pebbles" aria-label="Words left on the shelf">
            <span class="pebble">again</span>
            <span class="pebble">perhaps</span>
            <span class="pebble">enough</span>
            <span class="pebble">hush</span>
          </div>
          <form class="word-form" id="wordForm">
            <label class="visually-hidden" for="wordInput">A word or very short phrase to leave on the shelf</label>
            <input id="wordInput" type="text" maxlength="18" autocomplete="off" placeholder="one small word…">
            <button type="submit" aria-label="Place your word on the shelf" title="Place it on the shelf">↗</button>
          </form>
          <p class="form-status" id="formStatus" aria-live="polite"></p>
        </article>
      </div>
    </section>

    <footer class="site-footer">
      <div class="footer-main">
        <div class="footer-signoff"><span aria-hidden="true">✳</span> Made between one question and the next.</div>
        <div class="footer-meta">
          MADE BY KIMI · NO FEED · NO TRACKING · NO HURRY<br>
          ATTENTION IS YOURS TO KEEP
        </div>
      </div>
    </footer>
  </div>

  <script>
    const thoughts = [
      "Notice something that is working without asking for credit.",
      "What have you changed your mind about lately?",
      "Where could you choose curiosity over certainty?",
      "Send the message. The kind one.",
      "What would you do more slowly if no one was counting?",
      "Make room for the version of the idea that might fail.",
      "Look for the oldest object near you. Imagine its Tuesday.",
      "You can begin again without making a speech about it.",
      "What if the detour is where the day actually happens?",
      "Find one beautiful thing that cannot be posted.",
      "Ask a better question. Then don’t rush to answer it.",
      "Nothing is too small to be worth paying attention to."
    ];

    const thought = document.getElementById("thought");
    const thoughtButton = document.getElementById("thoughtButton");
    const thoughtNumber = document.getElementById("thoughtNumber");
    let currentThought = 0;
    let thoughtTimer;

    thoughtButton.addEventListener("click", () => {
      let nextThought;
      do {
        nextThought = Math.floor(Math.random() * thoughts.length);
      } while (nextThought === currentThought);

      clearTimeout(thoughtTimer);
      thoughtButton.disabled = true;
      thought.classList.add("is-changing");

      thoughtTimer = setTimeout(() => {
        currentThought = nextThought;
        thought.textContent = thoughts[currentThought];
        thoughtNumber.textContent = "Nº " + String(currentThought + 1).padStart(3, "0");
        thought.classList.remove("is-changing");
        thoughtButton.disabled = false;
      }, 170);
    });

    const root = document.documentElement;
    const themeToggle = document.getElementById("themeToggle");
    const themeLabel = document.getElementById("themeLabel");
    const themeIcon = document.getElementById("themeIcon");

    themeToggle.addEventListener("click", () => {
      const goingDark = root.dataset.theme !== "dark";
      root.dataset.theme = goingDark ? "dark" : "light";
      themeToggle.setAttribute("aria-pressed", String(goingDark));
      themeToggle.setAttribute("aria-label", goingDark ? "Switch to light theme" : "Switch to dark theme");
      themeLabel.textContent = goingDark ? "Bring back the sun" : "Dim the lights";
      themeIcon.textContent = goingDark ? "☀" : "◐";
    });

    const wordForm = document.getElementById("wordForm");
    const wordInput = document.getElementById("wordInput");
    const pebbles = document.getElementById("pebbles");
    const formStatus = document.getElementById("formStatus");

    wordForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const word = wordInput.value.trim().replace(/\s+/g, " ");

      if (!word) {
        formStatus.textContent = "A blank pebble is fine too, but try a letter or two.";
        wordInput.focus();
        return;
      }

      const pebble = document.createElement("span");
      pebble.className = "pebble pebble-new";
      pebble.textContent = word;
      pebbles.appendChild(pebble);

      wordInput.value = "";
      formStatus.textContent = "Placed on the shelf. Thank you.";
      wordInput.focus();
    });
  </script>
</body>
</html>
```

What: A playful editorial homepage called “Unprompted,” with an offline small-thought machine, poetic objects on a windowsill, a leave-a-word interaction, and a light/dark switch.