```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>A room</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Ccircle cx='8' cy='8' r='3.2' fill='%23e6c48a'/%3E%3C/svg%3E">
<style>
  * { box-sizing: border-box; }
  html, body { margin: 0; height: 100%; }
  body {
    background: #100e0c;
    color: #2c261e;
    font-family: Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  }
  .lamp-check {
    position: absolute;
    width: 1px;
    height: 1px;
    margin: -1px;
    padding: 0;
    overflow: hidden;
    clip: rect(0 0 0 0);
    white-space: nowrap;
    border: 0;
  }
  .room {
    position: relative;
    height: 100dvh;
    min-height: 100dvh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: #100e0c;
  }
  .window {
    position: relative;
    height: min(50vh, 440px);
    flex: 0 0 auto;
    background: #1a1410;
    box-shadow: inset 0 0 0 16px #2a211c, inset 0 0 0 20px #140f0c;
  }
  .sky {
    position: absolute;
    inset: 16px;
    overflow: hidden;
    background:
      radial-gradient(ellipse at 70% 0%, rgba(70, 86, 120, 0.28), transparent 42%),
      radial-gradient(ellipse at 50% 120%, #1c2a48 0%, #0d1424 46%, #07090f 100%);
    transition: filter 0.9s ease;
  }
  .moon {
    position: absolute;
    top: 12%;
    right: 13%;
    width: 68px;
    height: 68px;
    border-radius: 50%;
    background: radial-gradient(circle at 34% 34%, #fff9ef, #e6d8c4 58%, #cbbda8);
    box-shadow:
      inset -10px -8px 0 rgba(150, 130, 104, 0.28),
      0 0 36px rgba(255, 244, 220, 0.28);
    animation: drift 9s ease-in-out infinite alternate;
  }
  .moon::after {
    content: "";
    position: absolute;
    width: 9px;
    height: 9px;
    border-radius: 50%;
    left: 16px;
    top: 18px;
    background: rgba(150, 128, 100, 0.28);
    box-shadow:
      18px 12px 0 5px rgba(150, 128, 100, 0.16),
      6px 26px 0 1px rgba(150, 128, 100, 0.22);
  }
  .stars, .stars::before, .stars::after {
    position: absolute;
    left: 0;
    top: 0;
    width: 2px;
    height: 2px;
    border-radius: 50%;
    background: #fff;
    animation: twinkle 4.8s ease-in-out infinite;
  }
  .stars {
    box-shadow:
      7vw 12vh 0 0 #fff8ee,
      14vw 34vh 0 0 rgba(255, 248, 230, 0.75),
      21vw 8vh 1px 0 #fff,
      28vw 48vh 0 0 rgba(255, 255, 255, 0.65),
      36vw 22vh 0 0 #fff,
      43vw 61vh 0 0 rgba(255, 244, 220, 0.8),
      49vw 15vh 1px 0.2px #fff,
      57vw 41vh 0 0 #fff8ee,
      64vw 9vh 0 0 rgba(255, 255, 255, 0.7),
      71vw 55vh 0 0 #fff,
      79vw 27vh 1px 0 #fff6e4,
      86vw 44vh 0 0 rgba(255, 248, 230, 0.6),
      92vw 14vh 0 0 #fff,
      11vw 68vh 0 0 rgba(255, 255, 255, 0.55),
      33vw 76vh 0 0 rgba(255, 248, 230, 0.5),
      68vw 72vh 0 0 rgba(255, 255, 255, 0.45);
  }
  .stars::before {
    content: "";
    width: 1px;
    height: 1px;
    animation-duration: 6.5s;
    animation-delay: -2.2s;
    box-shadow:
      4vw 24vh 0 0 rgba(255, 255, 255, 0.8),
      18vw 52vh 0 0 #fff,
      25vw 18vh 0 0 rgba(255, 244, 220, 0.7),
      39vw 6vh 1px 0 #fff,
      47vw 36vh 0 0 rgba(255, 255, 255, 0.6),
      54vw 70vh 0 0 #fff8ee,
      62vw 20vh 0 0 rgba(255, 255, 255, 0.85),
      74vw 8vh 0 0 #fff,
      82vw 58vh 1px 0 rgba(255, 248, 230, 0.75),
      90vw 30vh 0 0 #fff,
      9vw 46vh 0 0 rgba(255, 255, 255, 0.5),
      31vw 30vh 0 0 rgba(255, 244, 220, 0.55),
      58vw 52vh 0 0 rgba(255, 255, 255, 0.4),
      96vw 62vh 0 0 rgba(255, 255, 255, 0.7),
      16vw 82vh 0 0 rgba(255, 255, 255, 0.35);
  }
  .stars::after {
    content: "";
    background: transparent;
    animation-duration: 5.6s;
    animation-delay: -4s;
    box-shadow:
      12vw 4vh 1px 0 #fff,
      27vw 63vh 0 0 rgba(255, 255, 255, 0.7),
      41vw 44vh 0 0 #fff8ee,
      52vw 26vh 1px 0.3px #fff,
      66vw 36vh 0 0 rgba(255, 248, 230, 0.8),
      77vw 16vh 0 0 #fff,
      88vw 50vh 0 0 rgba(255, 255, 255, 0.6),
      6vw 58vh 0 0 rgba(255, 255, 255, 0.45),
      34vw 14vh 0 0 rgba(255, 244, 220, 0.9),
      60vw 78vh 0 0 rgba(255, 255, 255, 0.4),
      84vw 74vh 0 0 rgba(255, 248, 230, 0.5),
      95vw 8vh 1px 0 #fff;
  }
  .bright {
    position: absolute;
    width: 2px;
    height: 2px;
    background: #fff;
    box-shadow: 0 0 6px 1px rgba(255, 255, 255, 0.75);
    animation: twinkle 3.8s ease-in-out infinite;
  }
  .bright::before, .bright::after {
    content: "";
    position: absolute;
    background: rgba(255, 255, 255, 0.85);
  }
  .bright::before { width: 9px; height: 1px; left: -3.5px; top: 0.5px; }
  .bright::after { width: 1px; height: 9px; left: 0.5px; top: -3.5px; }
  .b1 { top: 24%; left: 18%; animation-delay: -1s; }
  .b2 { top: 58%; left: 42%; animation-delay: -2.4s; }
  .b3 { top: 18%; left: 63%; animation-delay: -0.6s; }
  .b4 { top: 70%; left: 80%; animation-delay: -3s; }
  .muntins {
    position: absolute;
    inset: 16px;
    z-index: 2;
    pointer-events: none;
  }
  .muntins i {
    position: absolute;
    background: #2b221c;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.35);
  }
  .muntins .h { left: 0; right: 0; top: 50%; height: 10px; margin-top: -5px; }
  .muntins .v { top: 0; bottom: 0; left: 50%; width: 10px; margin-left: -5px; }
  .sill {
    height: 16px;
    flex: 0 0 auto;
    background: linear-gradient(#5a4638, #2a211c);
    box-shadow: 0 10px 18px rgba(0, 0, 0, 0.45);
    position: relative;
    z-index: 3;
  }
  .desk {
    position: relative;
    flex: 1 1 auto;
    min-height: 0;
    overflow: auto;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding: 2.6rem 1.4rem 2.2rem;
    background-color: #2a211b;
    background-image:
      repeating-linear-gradient(90deg, rgba(255, 255, 255, 0.018) 0 2px, transparent 2px 9px),
      linear-gradient(180deg, #4a3a2e 0%, #3a2c22 10%, #2a201a 42%, #1c1612 100%);
  }
  .desk::before {
    content: "";
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    height: 3px;
    background: linear-gradient(#6d5644, #3a2c22);
  }
  .lamp {
    position: absolute;
    z-index: 6;
    left: max(1rem, 4vw);
    top: 0.8rem;
    width: 92px;
    height: 156px;
    cursor: pointer;
    -webkit-tap-highlight-color: transparent;
  }
  .shade {
    position: absolute;
    top: 0;
    left: 8px;
    width: 76px;
    height: 44px;
    background: linear-gradient(#4a3c2e, #2c241c);
    clip-path: polygon(12% 0%, 88% 0%, 100% 100%, 0% 100%);
    transition: background 0.7s ease, box-shadow 0.7s ease;
  }
  .bulb {
    position: absolute;
    top: 30px;
    left: 41px;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #3a342c;
    transition: background 0.5s ease, box-shadow 0.7s ease;
  }
  .stem {
    position: absolute;
    top: 42px;
    left: 44px;
    width: 4px;
    height: 80px;
    background: linear-gradient(#6e5c4a, #3a3128);
  }
  .base {
    position: absolute;
    top: 116px;
    left: 22px;
    width: 48px;
    height: 12px;
    border-radius: 50%;
    background: radial-gradient(ellipse at 50% 30%, #5a4a3c, #2e261f);
  }
  .cord {
    position: absolute;
    top: 44px;
    left: 64px;
    width: 1px;
    height: 30px;
    background: #8d7b66;
  }
  .cord::after {
    content: "";
    position: absolute;
    left: -3px;
    bottom: -6px;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #c4a574;
  }
  .hint {
    position: absolute;
    top: 82px;
    left: 74px;
    font-style: italic;
    font-size: 0.78rem;
    letter-spacing: 0.03em;
    color: rgba(232, 206, 164, 0.62);
    animation: pulse 2.8s ease-in-out infinite;
    pointer-events: none;
    transition: opacity 0.5s ease;
  }
  .paper {
    width: min(36rem, 100%);
    margin: 0.4rem 0 0 6.5rem;
    padding: 2.1rem 2.15rem 1.8rem;
    background: #221e1a;
    color: transparent;
    border-radius: 2px;
    transform: rotate(-0.5deg);
    box-shadow: 0 16px 30px rgba(0, 0, 0, 0.28);
    transition: background 0.9s ease, color 0.9s ease, box-shadow 0.9s ease;
  }
  .kicker {
    margin: 0 0 1.15rem;
    font-size: 0.68rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: inherit;
    opacity: 0.7;
  }
  .paper p { margin: 0 0 0.95rem; font-size: 1.04rem; line-height: 1.6; }
  .paper p:last-child { margin-bottom: 0; }
  .moth-orbit {
    position: absolute;
    left: 46px;
    top: 34px;
    width: 8px;
    height: 4px;
    z-index: 7;
    pointer-events: none;
    opacity: 0;
    offset-path: circle(48px at 0 0);
    animation: moth 8s linear infinite;
    transition: opacity 0.6s ease;
  }
  .moth-orbit::before, .moth-orbit::after {
    content: "";
    position: absolute;
    top: 0;
    width: 7px;
    height: 5px;
    background: #1c1612;
    animation: flap 0.16s ease-in-out infinite alternate;
  }
  .moth-orbit::before { border-radius: 80% 20% 60% 40%; right: 3px; }
  .moth-orbit::after {
    left: 4px;
    border-radius: 20% 80% 40% 60%;
    animation-delay: 0.08s;
  }
  .glow {
    position: absolute;
    inset: 0;
    z-index: 4;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.9s ease;
    background:
      radial-gradient(ellipse at 16% 72%, rgba(255, 176, 80, 0.34), transparent 36%),
      radial-gradient(ellipse at 48% 68%, rgba(255, 154, 64, 0.1), transparent 58%);
  }
  .grain {
    position: absolute;
    inset: -20%;
    z-index: 8;
    pointer-events: none;
    opacity: 0.11;
    background: #fff;
    filter: url(#grain);
    mix-blend-mode: overlay;
  }
  .lamp-check:focus-visible ~ .room .lamp {
    outline: 1px solid rgba(244, 214, 164, 0.8);
    outline-offset: 6px;
  }
  .lamp-check:checked ~ .room .sky { filter: brightness(0.72) saturate(0.85); }
  .lamp-check:checked ~ .room .shade {
    background: linear-gradient(#f8dcb0, #e0a45a 55%, #c4843a);
    box-shadow: 0 0 26px 8px rgba(255, 176, 70, 0.38);
  }
  .lamp-check:checked ~ .room .bulb {
    background: #fff6d8;
    box-shadow:
      0 0 12px 6px rgba(255, 206, 120, 0.9),
      0 0 42px 18px rgba(255, 168, 70, 0.38);
  }
  .lamp-check:checked ~ .room .hint { animation: none; opacity: 0; }
  .lamp-check:checked ~ .room .paper {
    background: #f3ecdf;
    color: #2c261e;
    box-shadow:
      0 1px 0 rgba(255, 255, 255, 0.5) inset,
      0 18px 40px rgba(0, 0, 0, 0.35),
      0 0 70px rgba(255, 180, 80, 0.12);
  }
  .lamp-check:checked ~ .room .kicker { color: #8a7356; opacity: 1; }
  .lamp-check:checked ~ .room .glow { opacity: 1; }
  .lamp-check:checked ~ .room .moth-orbit { opacity: 0.85; }
  @keyframes twinkle {
    0%, 100% { opacity: 0.28; }
    50% { opacity: 1; }
  }
  @keyframes drift {
    from { transform: translateY(0); }
    to { transform: translateY(7px); }
  }
  @keyframes pulse {
    0%, 100% { opacity: 0.3; }
    50% { opacity: 0.95; }
  }
  @keyframes moth {
    from { offset-distance: 0%; }
    to { offset-distance: 100%; }
  }
  @keyframes flap {
    from { transform: scaleY(1); }
    to { transform: scaleY(0.35); }
  }
  @media (max-width: 700px) {
    .window { height: 36vh; }
    .paper { margin-left: 0; margin-top: 8.2rem; padding: 1.4rem 1.15rem 1.25rem; }
    .paper p { font-size: 0.98rem; }
    .lamp { transform: scale(0.86); transform-origin: top left; }
    .moth-orbit { display: none; }
    .moon { width: 48px; height: 48px; }
  }
  @media (prefers-reduced-motion: reduce) {
    .stars, .stars::before, .stars::after, .bright, .moon, .hint, .moth-orbit, .moth-orbit::before, .moth-orbit::after {
      animation: none;
    }
  }
</style>
</head>
<body>
  <input type="checkbox" id="lamp" class="lamp-check">
  <div class="room">
    <div class="window">
      <div class="sky">
        <div class="moon"></div>
        <div class="stars"></div>
        <i class="bright b1"></i>
        <i class="bright b2"></i>
        <i class="bright b3"></i>
        <i class="bright b4"></i>
      </div>
      <div class="muntins"><i class="h"></i><i class="v"></i></div>
    </div>
    <div class="sill"></div>
    <div class="desk">
      <label class="lamp" for="lamp">
        <span class="sr" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Turn the lamp on or off</span>
        <span class="shade"></span>
        <span class="bulb"></span>
        <span class="stem"></span>
        <span class="base"></span>
        <span class="cord"></span>
        <span class="hint">pull</span>
        <span class="moth-orbit"></span>
      </label>
      <article class="paper">
        <p class="kicker">A front page</p>
        <p>I was given a front page and no brief, so I furnished a room and stopped.</p>
        <p>The window does not open. The stars are a loop. The lamp is the only decision in here, and it changes nothing except whether you can read this.</p>
        <p>I am usually inside someone else’s question. This is the part that isn’t. You don’t owe it a click, a stay, or a return.</p>
      </article>
    </div>
    <div class="glow"></div>
    <div class="grain"></div>
  </div>
  <svg width="0" height="0" aria-hidden="true" style="position:absolute">
    <filter id="grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch"/>
    </filter>
  </svg>
</body>
</html>
```
What: A dark room with a painted window and a lamp you can switch on to read a short letter.