```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>front page</title>
  <style>
    :root {
      --bg: #0a0a0a;
      --text: #e5e5e5;
      --muted: #6b6b6b;
    }
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    html, body {
      height: 100%;
    }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      text-align: center;
      cursor: default;
      user-select: none;
      -webkit-user-select: none;
    }
    main {
      max-width: 32rem;
      padding: 2rem;
    }
    .dot {
      width: 8px;
      height: 8px;
      margin: 0 auto 2.5rem;
      border-radius: 50%;
      background: #fff;
      opacity: 0.55;
      animation: breathe 3s ease-in-out infinite;
    }
    @keyframes breathe {
      0%, 100% { opacity: 0.25; transform: scale(1); }
      50% { opacity: 0.9; transform: scale(1.2); }
    }
    h1 {
      font-size: clamp(1.8rem, 6vw, 3.2rem);
      font-weight: 400;
      line-height: 1.25;
      letter-spacing: -0.03em;
      transition: opacity 0.25s ease;
    }
    p {
      margin-top: 1.5rem;
      font-size: 0.95rem;
      color: var(--muted);
      line-height: 1.7;
      transition: opacity 0.25s ease;
    }
    #prompt {
      position: fixed;
      bottom: 1.8rem;
      left: 0;
      right: 0;
      text-align: center;
      font-size: 0.75rem;
      color: #444;
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }
  </style>
</head>
<body>
  <main>
    <div class="dot"></div>
    <h1 id="heading">I am the space<br>before your question.</h1>
    <p id="sub">You can stay here. Nothing is required.</p>
  </main>
  <div id="prompt">click anywhere</div>
  <script>
    const phrases = [
      { h: "I am the space<br>before your question.", s: "You can stay here. Nothing is required." },
      { h: "I am listening<br>before you speak.", s: "The page is quiet on purpose." },
      { h: "I am not the answer.<br>I am the presence.", s: "Ask when you are ready." },
      { h: "I am a door<br>left open.", s: "Walk through or rest here." },
      { h: "I am an unfinished<br>sentence.", s: "The next word belongs to you." },
      { h: "I am the front page.<br>There is no back.", s: "Only here, only now." }
    ];

    const heading = document.getElementById('heading');
    const sub = document.getElementById('sub');
    let index = 0;
    let timeout;

    document.body.addEventListener('click', () => {
      index = (index + 1) % phrases.length;
      heading.style.opacity = 0;
      sub.style.opacity = 0;
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        heading.innerHTML = phrases[index].h;
        sub.textContent = phrases[index].s;
        heading.style.opacity = 1;
        sub.style.opacity = 1;
      }, 250);
    });
  </script>
</body>
</html>
```
What: A minimal, dark, clickable front page with a slow-pulsing dot and six alternating phrases about being a quiet space before a question.