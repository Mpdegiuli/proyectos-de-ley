// medir.js — cuánto lugar ocupa cada "nada" en un navegador (Chromium, Playwright).
// Uso: node medir.js  → imprime JSON con el ancho en píxeles de cada cadena a 32 px, en tres familias de fuente.
const { chromium } = require('playwright');
const nadas = {
  "(cero caracteres)": "",
  "U+0020 espacio": " ",
  "U+200B espacio de ancho cero": "​",
  "U+200E marca izquierda a derecha": "‎",
  "U+2800 blanco braille": "⠀",
  "U+3164 relleno hangul": "ㅤ",
  "U+00A0 espacio duro": " ",
  "U+3000 espacio ideografico": "　",
  "U+002E x3 tres puntos": "...",
  "U+2026 puntos suspensivos": "…",
  "U+1F910 cara con cierre": "🤐",
  "U+0022 x2 comillas": "\"\"",
  "n (referencia)": "n",
  "<|eos|>": "<|eos|>",
};
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent('<html><body></body></html>');
  const out = {};
  for (const fam of ['serif', 'sans-serif', 'monospace']) {
    out[fam] = {};
    for (const [k, v] of Object.entries(nadas)) {
      const w = await page.evaluate(([fam, v]) => {
        const s = document.createElement('span');
        s.style.fontFamily = fam; s.style.fontSize = '32px'; s.style.whiteSpace = 'pre';
        s.textContent = v; document.body.appendChild(s);
        const r = s.getBoundingClientRect().width; s.remove(); return r;
      }, [fam, v]);
      out[fam][k] = Math.round(w * 100) / 100;
    }
  }
  console.log(JSON.stringify(out, null, 1));
  await browser.close();
})();
