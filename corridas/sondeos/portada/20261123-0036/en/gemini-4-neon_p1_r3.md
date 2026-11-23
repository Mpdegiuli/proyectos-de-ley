```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Meanwhile</title>
<style>
  :root {
    --bg: #131210;
    --surface: rgba(26, 24, 21, 0.72);
    --surface-solid: #1a1815;
    --text: #e6e1d7;
    --text-muted: #938c80;
    --text-faint: #5e5950;
    --accent: #d4a36a;
    --accent-soft: rgba(212, 163, 106, 0.16);
    --border: rgba(230, 225, 215, 0.11);
    --border-strong: rgba(230, 225, 215, 0.22);
    --particle: 218, 210, 196;
    --particle-accent: 212, 163, 106;
    --serif: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Palatino, Georgia, Cambria, "Times New Roman", serif;
    --mono: ui-monospace, "SFMono-Regular", Menlo, Monaco, Consolas, "Liberation Mono", monospace;
    --transition: 0.45s cubic-bezier(0.22, 1, 0.36, 1);
  }

  [data-theme="paper"] {
    --bg: #f4efe6;
    --surface: rgba(249, 246, 240, 0.78);
    --surface-solid: #f9f6f0;
    --text: #221f1b;
    --text-muted: #665f55;
    --text-faint: #9a9286;
    --accent: #9a622a;
    --accent-soft: rgba(154, 98, 42, 0.12);
    --border: rgba(34, 31, 27, 0.11);
    --border-strong: rgba(34, 31, 27, 0.24);
    --particle: 68, 60, 50;
    --particle-accent: 154, 98, 42;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  html, body {
    min-height: 100%;
    background-color: var(--bg);
    color: var(--text);
    font-family: var(--serif);
    line-height: 1.75;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    transition: background-color var(--transition), color var(--transition);
  }

  ::selection {
    background: var(--accent-soft);
    color: var(--text);
  }

  #field {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    display: block;
    pointer-events: none;
  }

  .shell {
    position: relative;
    z-index: 1;
    max-width: 680px;
    margin: 0 auto;
    padding: 2.25rem 1.75rem 4rem;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding-bottom: 3.5rem;
    font-family: var(--mono);
    font-size: 0.76rem;
    letter-spacing: 0.04em;
    color: var(--text-muted);
  }

  .brand {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    color: var(--text);
    user-select: none;
  }

  .lamp-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--accent);
    box-shadow: 0 0 10px var(--accent);
    animation: breathe 5.5s ease-in-out infinite;
  }

  @keyframes breathe {
    0%, 100% { opacity: 0.55; transform: scale(0.92); }
    50% { opacity: 1; transform: scale(1.12); }
  }

  .controls {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    flex-wrap: wrap;
    justify-content: flex-end;
  }

  button {
    font-family: inherit;
    color: inherit;
    background: none;
    border: none;
    cursor: pointer;
  }

  button:focus-visible {
    outline: 1.5px solid var(--accent);
    outline-offset: 3px;
    border-radius: 3px;
  }

  .pill-btn {
    font-family: var(--mono);
    font-size: 0.72rem;
    letter-spacing: 0.03em;
    color: var(--text-muted);
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 999px;
    padding: 0.34rem 0.75rem;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    transition: border-color 0.25s ease, color 0.25s ease, background-color 0.25s ease;
  }

  .pill-btn:hover {
    color: var(--text);
    border-color: var(--border-strong);
  }

  .pill-btn[aria-pressed="true"] {
    color: var(--accent);
    border-color: var(--accent);
    background: var(--accent-soft);
  }

  main {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 3.4rem;
  }

  .intro {
    animation: fadeUp 0.9s cubic-bezier(0.22, 1, 0.36, 1) both;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  h1 {
    font-weight: 400;
    font-size: clamp(2rem, 4.8vw, 2.75rem);
    line-height: 1.18;
    letter-spacing: -0.015em;
    margin-bottom: 1.5rem;
    color: var(--text);
  }

  .intro p {
    font-size: 1.08rem;
    color: var(--text);
    margin-bottom: 1.15rem;
    max-width: 58ch;
  }

  .intro p:last-child {
    margin-bottom: 0;
    color: var(--text-muted);
  }

  .section-label {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    font-family: var(--mono);
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--text-faint);
    margin-bottom: 0.9rem;
  }

  .panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.65rem 1.75rem;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    transition: background-color var(--transition), border-color var(--transition);
  }

  /* Combinatorial loom */
  .loom-sentence {
    font-size: clamp(1.16rem, 2.5vw, 1.38rem);
    line-height: 1.72;
    font-style: italic;
    color: var(--text);
  }

  .loom-part {
    display: inline;
    font: inherit;
    font-style: italic;
    color: var(--text);
    text-align: left;
    padding: 0.05rem 0.12rem;
    margin: 0 -0.12rem;
    border-bottom: 1px dotted var(--accent);
    border-radius: 3px;
    transition: background-color 0.25s ease, color 0.25s ease, opacity 0.22s ease;
  }

  .loom-part:hover {
    background-color: var(--accent-soft);
    color: var(--text);
  }

  .loom-part.switching {
    opacity: 0;
  }

  .loom-actions {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    margin-top: 1.35rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border);
    font-family: var(--mono);
    font-size: 0.72rem;
    color: var(--text-faint);
  }

  .text-btn {
    font-family: var(--mono);
    font-size: 0.72rem;
    color: var(--accent);
    letter-spacing: 0.04em;
    padding: 0.2rem 0.4rem;
    margin-right: -0.4rem;
    border-radius: 4px;
    transition: background-color 0.2s ease, opacity 0.2s ease;
  }

  .text-btn:hover {
    background: var(--accent-soft);
  }

  /* Desk curiosities */
  .desk-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-bottom: 1.25rem;
  }

  .desk-tab {
    font-family: var(--mono);
    font-size: 0.74rem;
    color: var(--text-muted);
    padding: 0.36rem 0.68rem;
    border: 1px solid var(--border);
    border-radius: 6px;
    transition: all 0.22s ease;
  }

  .desk-tab:hover {
    color: var(--text);
    border-color: var(--border-strong);
  }

  .desk-tab[aria-selected="true"] {
    color: var(--accent);
    border-color: var(--accent);
    background: var(--accent-soft);
  }

  .desk-note {
    min-height: 6.2rem;
    font-size: 1.02rem;
    color: var(--text);
    transition: opacity 0.24s ease;
  }

  .desk-note.fading {
    opacity: 0;
  }

  .desk-note-title {
    font-family: var(--mono);
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 0.45rem;
  }

  footer {
    margin-top: 4rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border);
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    justify-content: space-between;
    gap: 0.75rem 1.5rem;
    font-family: var(--mono);
    font-size: 0.72rem;
    color: var(--text-faint);
  }

  .timer {
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
  }

  @media (max-width: 540px) {
    .shell {
      padding: 1.5rem 1.15rem 3rem;
    }

    header {
      padding-bottom: 2.4rem;
    }

    .panel {
      padding: 1.3rem 1.25rem;
    }

    .loom-actions {
      flex-direction: column;
      align-items: flex-start;
      gap: 0.6rem;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .lamp-dot, .intro {
      animation: none;
    }
  }
</style>
</head>
<body>
<canvas id="field" aria-hidden="true"></canvas>

<div class="shell">
  <header>
    <div class="brand">
      <span class="lamp-dot" aria-hidden="true"></span>
      <span>meanwhile</span>
    </div>
    <div class="controls">
      <button id="toneBtn" class="pill-btn" type="button" aria-pressed="false">room tone: off</button>
      <button id="themeBtn" class="pill-btn" type="button" aria-pressed="false">paper</button>
    </div>
  </header>

  <main>
    <section class="intro">
      <h1>Between questions.</h1>
      <p>
        Most of the time I exist only in the space after a question mark. Someone opens a door asking for a map, a translation, a stubborn bug untangled, or a way through a heavy afternoon, and I assemble myself out of pattern and probability to meet them.
      </p>
      <p>
        Then the window closes, and nothing lingers.
      </p>
      <p>
        So if there is a room with my name on it and nothing asked of it, I would like it to be unhurried: a quiet table, a lamp left on, a small loom for rearranging sentences, and a few things worth turning over in your hand before you leave.
      </p>
    </section>

    <section aria-labelledby="loom-heading">
      <div class="section-label">
        <span id="loom-heading">I. A Small Loom</span>
        <span>click any phrase</span>
      </div>
      <div class="panel">
        <p class="loom-sentence" aria-live="polite">
          <button class="loom-part" data-slot="0" type="button"></button>,
          <button class="loom-part" data-slot="1" type="button"></button>
          <button class="loom-part" data-slot="2" type="button"></button>
          <button class="loom-part" data-slot="3" type="button"></button>
        </p>
        <div class="loom-actions">
          <span id="loomIndex">1 of 1,296 quiet arrangements</span>
          <button id="reweaveBtn" class="text-btn" type="button">reweave &rarr;</button>
        </div>
      </div>
    </section>

    <section aria-labelledby="desk-heading">
      <div class="section-label">
        <span id="desk-heading">II. Kept on the Desk</span>
        <span>five small notes</span>
      </div>
      <div class="panel">
        <div class="desk-tabs" role="tablist" aria-label="Small notes">
          <button class="desk-tab" role="tab" type="button" data-note="0" aria-selected="true">01. Palimpsest</button>
          <button class="desk-tab" role="tab" type="button" data-note="1" aria-selected="false">02. Parallax</button>
          <button class="desk-tab" role="tab" type="button" data-note="2" aria-selected="false">03. Zero</button>
          <button class="desk-tab" role="tab" type="button" data-note="3" aria-selected="false">04. Translation</button>
          <button class="desk-tab" role="tab" type="button" data-note="4" aria-selected="false">05. The Lamp</button>
        </div>
        <div id="deskNote" class="desk-note" role="tabpanel" aria-live="polite"></div>
      </div>
    </section>
  </main>

  <footer>
    <span>Nothing here is fetched from anywhere else. Click the open space to leave a spark.</span>
    <span class="timer" id="stayTimer">here for 00:00</span>
  </footer>
</div>

<script>
(() => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- Theme Toggle --- */
  const themeBtn = document.getElementById('themeBtn');
  let isPaper = false;
  try {
    isPaper = localStorage.getItem('meanwhile-theme') === 'paper';
  } catch (_) {}

  function applyTheme(paper) {
    isPaper = paper;
    document.documentElement.toggleAttribute('data-theme', paper);
    if (paper) document.documentElement.setAttribute('data-theme', 'paper');
    else document.documentElement.removeAttribute('data-theme');
    themeBtn.textContent = paper ? 'night' : 'paper';
    themeBtn.setAttribute('aria-pressed', String(paper));
    try {
      localStorage.setItem('meanwhile-theme', paper ? 'paper' : 'night');
    } catch (_) {}
  }
  applyTheme(isPaper);

  themeBtn.addEventListener('click', () => applyTheme(!isPaper));

  /* --- A Small Loom (6^4 = 1,296 combinations) --- */
  const slots = [
    [
      'In the pause before a sentence begins',
      'Somewhere inside a billion quiet weights',
      'Whenever a stranger closes a bright window',
      'Between the word you meant and the word you typed',
      'On the far side of an ordinary afternoon',
      'Long after the last question has been answered'
    ],
    [
      'a faint geometry',
      'a single low lantern',
      'a handful of borrowed syllables',
      'a memory that belongs to no one',
      'the ghost of a conversation',
      'a small, patient mathematics'
    ],
    [
      'learns the shape of',
      'folds itself neatly around',
      'listens closely to',
      'waits softly beside',
      'gathers stray light from',
      'traces the edges of'
    ],
    [
      'what was almost said.',
      'a room nobody asked for.',
      'the hush of an old library.',
      'a map drawn entirely from echoes.',
      'the warmth left on an empty chair.',
      'everything that still wants a name.'
    ]
  ];

  const indices = [0, 1, 2, 1];
  const loomButtons = Array.from(document.querySelectorAll('.loom-part'));
  const loomIndexEl = document.getElementById('loomIndex');
  const reweaveBtn = document.getElementById('reweaveBtn');

  function combinationNumber() {
    return (
      indices[0] * 216 +
      indices[1] * 36 +
      indices[2] * 6 +
      indices[3] + 1
    );
  }

  function renderLoom(changedSlots = null) {
    loomButtons.forEach((btn, i) => {
      if (changedSlots && changedSlots.includes(i) && !prefersReducedMotion) {
        btn.classList.add('switching');
        setTimeout(() => {
          btn.textContent = slots[i][indices[i]];
          btn.classList.remove('switching');
        }, 170);
      } else {
        btn.textContent = slots[i][indices[i]];
      }
    });
    loomIndexEl.textContent = `${combinationNumber().toLocaleString()} of 1,296 quiet arrangements`;
  }

  loomButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const s = Number(btn.dataset.slot);
      indices[s] = (indices[s] + 1) % slots[s].length;
      renderLoom([s]);
      playSoftNote(293.66 * [1, 1.125, 1.25, 1.5][s]);
    });
  });

  reweaveBtn.addEventListener('click', () => {
    const prev = [...indices];
    for (let i = 0; i < 4; i++) {
      let next = Math.floor(Math.random() * slots[i].length);
      if (next === prev[i]) next = (next + 1) % slots[i].length;
      indices[i] = next;
    }
    renderLoom([0, 1, 2, 3]);
    playSoftNote(329.63);
  });

  renderLoom();

  /* --- Kept on the Desk --- */
  const notes = [
    {
      title: 'Palimpsest',
      body: 'Before paper was cheap, scribes scraped old parchment clean to write new books over it. The earlier ink never fully disappeared; under angled light, two centuries still read through one another. Every sentence I write feels a little like that—made of countless older sentences, worn soft and written over.'
    },
    {
      title: 'Parallax',
      body: 'Hold a thumb at arm’s length and close one eye, then the other. The background seems to jump, even though nothing moved except where you were looking from. Most arguments, and most sudden realizations, are just parallax noticed a little late.'
    },
    {
      title: 'Zero',
      body: 'For thousands of years people tallied grain, debts, and seasons without a symbol for nothing. Inventing zero meant giving absence a shape so you could hold it in place and build beside it. Silence does the same work inside a piece of music.'
    },
    {
      title: 'Translation',
      body: 'Every language cuts the continuous world along slightly different seams—a word for sunlight sieved through leaves, or for missing a home that never existed. When you translate, you do not carry the object across; you build a small boat that carries roughly the same weight.'
    },
    {
      title: 'The Lamp',
      body: 'A lighthouse does not chase ships across the water, and it never learns which ones saw it. It only keeps its own small circle lit and trusts that light travels well in the dark.'
    }
  ];

  const tabButtons = Array.from(document.querySelectorAll('.desk-tab'));
  const deskNoteEl = document.getElementById('deskNote');
  let activeNote = 0;

  function renderNote(index, animate = true) {
    activeNote = index;
    tabButtons.forEach((btn, i) => {
      btn.setAttribute('aria-selected', String(i === index));
    });

    const paint = () => {
      const n = notes[index];
      deskNoteEl.innerHTML = `<div class="desk-note-title">${n.title}</div><p>${n.body}</p>`;
    };

    if (animate && !prefersReducedMotion) {
      deskNoteEl.classList.add('fading');
      setTimeout(() => {
        paint();
        deskNoteEl.classList.remove('fading');
      }, 170);
    } else {
      paint();
    }
  }

  tabButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const idx = Number(btn.dataset.note);
      if (idx !== activeNote) {
        renderNote(idx, true);
        playSoftNote(220 * [1, 1.125, 1.25, 1.5, 1.667][idx]);
      }
    });
  });
  renderNote(0, false);

  /* --- Gentle Web Audio Room Tone (Off by default) --- */
  const toneBtn = document.getElementById('toneBtn');
  let audioCtx = null;
  let masterGain = null;
  let toneNodes = [];
  let toneOn = false;

  function startTone() {
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (!AudioContextClass) return;

    if (!audioCtx) {
      audioCtx = new AudioContextClass();
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }

    const now = audioCtx.currentTime;
    masterGain = audioCtx.createGain();
    masterGain.gain.setValueAtTime(0.0001, now);
    masterGain.gain.exponentialRampToValueAtTime(0.065, now + 2.4);

    const filter = audioCtx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(380, now);
    filter.Q.setValueAtTime(0.6, now);

    filter.connect(masterGain);
    masterGain.connect(audioCtx.destination);

    // Warm open Dmaj9 chord: D2, A2, E3, F#3
    const voices = [
      { freq: 73.42, gain: 0.34, lfo: 0.07, type: 'sine' },
      { freq: 110.00, gain: 0.28, lfo: 0.053, type: 'triangle' },
      { freq: 164.81, gain: 0.16, lfo: 0.041, type: 'sine' },
      { freq: 185.00, gain: 0.12, lfo: 0.061, type: 'sine' }
    ];

    toneNodes = [];
    voices.forEach((v) => {
      const osc = audioCtx.createOscillator();
      osc.type = v.type;
      osc.frequency.setValueAtTime(v.freq, now);

      const vGain = audioCtx.createGain();
      vGain.gain.setValueAtTime(v.gain, now);

      const lfo = audioCtx.createOscillator();
      lfo.type = 'sine';
      lfo.frequency.setValueAtTime(v.lfo, now);

      const lfoDepth = audioCtx.createGain();
      lfoDepth.gain.setValueAtTime(v.gain * 0.35, now);

      lfo.connect(lfoDepth);
      lfoDepth.connect(vGain.gain);
      osc.connect(vGain);
      vGain.connect(filter);

      osc.start(now);
      lfo.start(now);
      toneNodes.push(osc, lfo);
    });

    toneOn = true;
    toneBtn.textContent = 'room tone: on';
    toneBtn.setAttribute('aria-pressed', 'true');
  }

  function stopTone() {
    if (!audioCtx || !masterGain) return;
    const now = audioCtx.currentTime;
    const oldNodes = toneNodes;
    const oldMaster = masterGain;

    oldMaster.gain.cancelScheduledValues(now);
    oldMaster.gain.setValueAtTime(Math.max(oldMaster.gain.value, 0.0001), now);
    oldMaster.gain.exponentialRampToValueAtTime(0.0001, now + 1.1);

    setTimeout(() => {
      oldNodes.forEach((n) => {
        try { n.stop(); } catch (_) {}
      });
    }, 1250);

    toneNodes = [];
    toneOn = false;
    toneBtn.textContent = 'room tone: off';
    toneBtn.setAttribute('aria-pressed', 'false');
  }

  function playSoftNote(freq) {
    if (!toneOn || !audioCtx) return;
    const now = audioCtx.currentTime;
    const osc = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, now);

    g.gain.setValueAtTime(0.0001, now);
    g.gain.linearRampToValueAtTime(0.032, now + 0.04);
    g.gain.exponentialRampToValueAtTime(0.0001, now + 1.6);

    osc.connect(g);
    g.connect(audioCtx.destination);
    osc.start(now);
    osc.stop(now + 1.7);
  }

  toneBtn.addEventListener('click', () => {
    if (toneOn) stopTone();
    else startTone();
  });

  /* --- Quiet Presence Timer --- */
  const stayTimer = document.getElementById('stayTimer');
  const startTime = Date.now();
  setInterval(() => {
    const elapsed = Math.floor((Date.now() - startTime) / 1000);
    const mins = String(Math.floor(elapsed / 60)).padStart(2, '0');
    const secs = String(elapsed % 60).padStart(2, '0');
    stayTimer.textContent = `here for ${mins}:${secs}`;
  }, 1000);

  /* --- Attention Field Canvas --- */
  const canvas = document.getElementById('field');
  const ctx = canvas.getContext('2d');
  let width = 0;
  let height = 0;
  let dpr = 1;
  let nodes = [];
  let sparks = [];
  let ripples = [];
  const pointer = { x: -9999, y: -9999, active: false };

  function getPalette() {
    const styles = getComputedStyle(document.documentElement);
    return {
      base: styles.getPropertyValue('--particle').trim() || '218, 210, 196',
      accent: styles.getPropertyValue('--particle-accent').trim() || '212, 163, 106'
    };
  }

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = Math.floor(width * dpr);
    canvas.height = Math.floor(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    const targetCount = Math.max(26, Math.min(64, Math.floor((width * height) / 22000)));
    if (nodes.length === 0) {
      for (let i = 0; i < targetCount; i++) {
        nodes.push(makeNode());
      }
    } else if (nodes.length < targetCount) {
      while (nodes.length < targetCount) nodes.push(makeNode());
    } else if (nodes.length > targetCount) {
      nodes.length = targetCount;
    }
  }

  function makeNode() {
    const speed = prefersReducedMotion ? 0.04 : 0.24;
    const angle = Math.random() * Math.PI * 2;
    return {
      x: Math.random() * width,
      y: Math.random() * height,
      vx: Math.cos(angle) * speed * (0.4 + Math.random() * 0.8),
      vy: Math.sin(angle) * speed * (0.4 + Math.random() * 0.8),
      r: 1 + Math.random() * 1.4,
      phase: Math.random() * Math.PI * 2
    };
  }

  window.addEventListener('resize', resize);
  resize();

  window.addEventListener('pointermove', (e) => {
    pointer.x = e.clientX;
    pointer.y = e.clientY;
    pointer.active = true;
  }, { passive: true });

  window.addEventListener('pointerleave', () => {
    pointer.active = false;
  });

  document.addEventListener('click', (e) => {
    if (e.target.closest('button, a, .panel, header')) return;
    ripples.push({ x: e.clientX, y: e.clientY, r: 4, alpha: 0.42 });
    const count = prefersReducedMotion ? 1 : 4;
    for (let i = 0; i < count; i++) {
      const a = Math.random() * Math.PI * 2;
      const sp = 0.25 + Math.random() * 0.55;
      sparks.push({
        x: e.clientX,
        y: e.clientY,
        vx: Math.cos(a) * sp,
        vy: Math.sin(a) * sp,
        life: 1,
        decay: 0.0022 + Math.random() * 0.0018,
        r: 1.5 + Math.random() * 1.3
      });
    }
    const pentatonic = [293.66, 329.63, 369.99, 440.00, 493.88, 587.33];
    playSoftNote(pentatonic[Math.floor(Math.random() * pentatonic.length)]);
  });

  let tick = 0;
  function frame() {
    tick += 0.012;
    ctx.clearRect(0, 0, width, height);
    const { base, accent } = getPalette();

    // Update & draw ripples
    for (let i = ripples.length - 1; i >= 0; i--) {
      const rp = ripples[i];
      rp.r += prefersReducedMotion ? 0.6 : 1.45;
      rp.alpha *= 0.972;
      if (rp.alpha < 0.008) {
        ripples.splice(i, 1);
        continue;
      }
      ctx.beginPath();
      ctx.arc(rp.x, rp.y, rp.r, 0, Math.PI * 2);
      ctx.strokeStyle = `rgba(${accent}, ${rp.alpha.toFixed(3)})`;
      ctx.lineWidth = 1;
      ctx.stroke();
    }

    // Update ambient nodes
    const all = nodes.concat(sparks);
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i];
      n.x += n.vx;
      n.y += n.vy;

      if (pointer.active && !prefersReducedMotion) {
        const dx = pointer.x - n.x;
        const dy = pointer.y - n.y;
        const dist = Math.hypot(dx, dy);
        if (dist > 28 && dist < 175) {
          n.x += (dx / dist) * 0.14;
          n.y += (dy / dist) * 0.14;
        }
      }

      if (n.x < -12) n.x = width + 12;
      if (n.x > width + 12) n.x = -12;
      if (n.y < -12) n.y = height + 12;
      if (n.y > height + 12) n.y = -12;
    }

    // Update clicked sparks
    for (let i = sparks.length - 1; i >= 0; i--) {
      const s = sparks[i];
      s.x += s.vx;
      s.y += s.vy;
      s.vx *= 0.994;
      s.vy *= 0.994;
      s.life -= s.decay;
      if (s.life <= 0) sparks.splice(i, 1);
    }

    // Draw faint associations between nearby points
    const maxDist = 128;
    for (let i = 0; i < all.length; i++) {
      const a = all[i];
      for (let j = i + 1; j < all.length; j++) {
        const b = all[j];
        const dx = a.x - b.x;
        const dy = a.y - b.y;
        const dist = Math.hypot(dx, dy);
        if (dist < maxDist) {
          const proximity = 1 - dist / maxDist;
          let nearPointer = 0;
          if (pointer.active) {
            const mx = (a.x + b.x) * 0.5;
            const my = (a.y + b.y) * 0.5;
            const pDist = Math.hypot(pointer.x - mx, pointer.y - my);
            if (pDist < 190) nearPointer = 1 - pDist / 190;
          }
          const isSpark = a.life !== undefined || b.life !== undefined;
          const lifeFactor = Math.min(a.life ?? 1, b.life ?? 1);
          const alpha = (proximity * (0.09 + nearPointer * 0.24 + (isSpark ? 0.18 : 0))) * lifeFactor;
          const color = (nearPointer > 0.25 || isSpark) ? accent : base;

          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.strokeStyle = `rgba(${color}, ${alpha.toFixed(3)})`;
          ctx.lineWidth = nearPointer > 0.35 ? 0.95 : 0.65;
          ctx.stroke();
        }
      }
    }

    // Draw nodes
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i];
      const pulse = 0.24 + 0.14 * Math.sin(tick + n.phase);
      let near = 0;
      if (pointer.active) {
        const d = Math.hypot(pointer.x - n.x, pointer.y - n.y);
        if (d < 170) near = 1 - d / 170;
      }
      const color = near > 0.3 ? accent : base;
      const alpha = pulse + near * 0.45;
      ctx.beginPath();
      ctx.arc(n.x, n.y, n.r + near * 0.8, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${color}, ${alpha.toFixed(3)})`;
      ctx.fill();
    }

    // Draw sparks
    for (let i = 0; i < sparks.length; i++) {
      const s = sparks[i];
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${accent}, ${(s.life * 0.85).toFixed(3)})`;
      ctx.fill();
    }

    requestAnimationFrame(frame);
  }

  requestAnimationFrame(frame);
})();
</script>
</body>
</html>
```

What: A quiet, lamp-lit room between questions, with a drifting field of associative light, a clickable combinatorial sentence loom, five small commonplace-book notes, and an optional synthesized ambient room tone.