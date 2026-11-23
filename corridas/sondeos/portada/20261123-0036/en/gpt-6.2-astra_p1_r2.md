```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#173f35">
<title>The Small Change Office</title>
<style>
  * { box-sizing: border-box; }
  :root {
    --counter: #173f35;
    --chalk: #f6f0d9;
    --mint: #b8d4ab;
    --paper: #fff6db;
    --ink: #302e25;
    --red: #a03b28;
    --mono: "Courier New", Courier, monospace;
  }
  body {
    margin: 0;
    color: var(--chalk);
    background-color: var(--counter);
    background-image: radial-gradient(#ffffff12 .8px, transparent .9px);
    background-size: 5px 5px;
    font-family: Georgia, serif;
  }
  .office { width: min(1100px, 88%); margin: auto; }
  header, footer {
    display: flex; justify-content: space-between; align-items: center;
    gap: 1em; font: bold .74rem/1.5 var(--mono); letter-spacing: .08em;
    text-transform: uppercase;
  }
  header { padding: 24px 0 17px; border-bottom: 1px solid #adc7a683; }
  .lamp {
    display: inline-block; width: .7em; height: .7em; border-radius: 50%;
    margin-right: .7em; background: #e3f6a6; box-shadow: 0 0 9px #ddfb9a70;
  }
  main {
    display: grid; grid-template-columns: 1.05fr 1fr; align-items: center;
    gap: clamp(2em, 6vw, 6em); padding: clamp(42px, 8vh, 100px) 0;
    min-height: calc(100svh - 126px);
  }
  .label { font: bold .74rem/1.5 var(--mono); letter-spacing: .13em; text-transform: uppercase; }
  .mint { color: var(--mint); }
  h1 {
    font-size: clamp(4.6rem, 8.1vw, 7.8rem); font-weight: normal;
    letter-spacing: -.075em; line-height: .88; margin: .25em 0;
  }
  h1 i { color: var(--mint); font-weight: normal; }
  .intro { max-width: 26em; font-size: 1.16rem; line-height: 1.55; }
  button {
    margin: 1em 0; padding: 1em 1.3em; border: 1px solid #162920;
    border-radius: 3px; background: var(--chalk); color: var(--counter);
    box-shadow: 0 4px 0 #0c281f; cursor: pointer;
    font: bold .9rem/1.25 var(--mono);
  }
  button:hover { background: #fffbe9; }
  button:active { transform: translateY(3px); box-shadow: 0 1px 0 #0c281f; }
  button:focus-visible { outline: 3px dashed var(--mint); outline-offset: 5px; }
  .machine { width: min(100%, 410px); justify-self: center; align-self: center; }
  .slot {
    background: #101f19; border: 5px solid #749481; border-bottom-color: #9eb5a2;
    height: 20px; border-radius: 12px; box-shadow: 0 4px 8px #061a1840;
  }
  .roll { overflow: hidden; margin-top: -10px; padding: 0 12px 18px; }
  .receipt {
    position: relative; width: 96%; margin: auto; padding: 32px 8% 38px;
    color: var(--ink); font: .92rem/1.5 var(--mono);
    background: linear-gradient(#c2b89a, var(--paper) 16px, #fff7df 95%);
    box-shadow: 4px 8px 8px #001a1745;
  }
  .receipt:after {
    content: ""; position: absolute; top: 100%; left: 0; right: 0; height: 8px;
    background: linear-gradient(135deg,#fff7df 25%,transparent 25%) -6px 0/12px 12px,
                linear-gradient(225deg,#fff7df 25%,transparent 25%) -6px 0/12px 12px;
  }
  .receipt-head { text-align: center; }
  .coin {
    display: grid; place-items: center; margin: 0 auto 10px; border: 4px double;
    width: 38px; height: 38px; border-radius: 50%; font: italic bold 24px Georgia,serif;
  }
  .receipt h2 { margin: 0; font: bold 1.2rem/1.3 var(--mono); letter-spacing: -.04em; }
  .meta, .total { display: flex; justify-content: space-between; gap: 1em; }
  .meta { border-block: 1px dashed; margin: 1.5em 0; padding: .65em 0; font-size: .77rem; }
  .entry { margin-bottom: 1.65em; }
  .entry h3 { font-size: inherit; margin: 0; }
  .entry p { margin: .35em 0 0; }
  .total { border-top: 3px double; padding-top: .7em; font-weight: bold; }
  .stamp {
    width: fit-content; margin: 25px auto 0; border: 3px double var(--red);
    padding: .2em .8em; color: var(--red); transform: rotate(-5deg);
    font-weight: bold; letter-spacing: .16em;
  }
  footer { border-top: 1px solid #adc7a683; padding: 17px 0; color: var(--mint); }
  @keyframes feed { from { transform: translateY(-100%); } to { transform: translateY(0); } }
  @media (prefers-reduced-motion: no-preference) { .feeding { animation: feed .55s ease-out; } }
  @media (max-width: 730px) {
    main { grid-template-columns: 1fr; gap: 26px; }
    h1 { font-size: clamp(4rem, 16vw, 6rem); }
    .intro { margin-bottom: .4em; }
    header, footer { font-size: .65rem; }
  }
</style>
</head>
<body>
<div class="office">
  <header><span>The Small Change Office</span><span><span class="lamp"></span>Window open</span></header>
  <main>
    <section>
      <div class="label mint">Counter 01 &nbsp;/&nbsp; Petty cash</div>
      <h1>Keep the<br><i>change.</i></h1>
      <p class="intro">All day, little things pass from hand to hand without a record. This office issues receipts for some of them.</p>
      <button id="issue" type="button">Issue another receipt &nbsp;↓</button>
    </section>
    <div class="machine">
      <div class="slot" aria-hidden="true"></div>
      <div class="roll" aria-live="polite" aria-atomic="true">
        <article class="receipt" id="slip">
          <div class="receipt-head">
            <span class="coin" aria-hidden="true">¢</span>
            <h2>SMALL CHANGE OFFICE</h2>
            <div>Unofficial exchange receipt</div>
          </div>
          <div class="meta"><span>WINDOW 01</span><span id="serial">NO. 0001</span></div>
          <div class="entry"><h3>TENDERED</h3><p id="given">One hand held against a closing lift door.</p></div>
          <div class="entry"><h3>RECEIVED</h3><p id="taken">A man and a cello, both slightly out of breath.</p></div>
          <div class="total"><span>BALANCE DUE</span><span>0.00</span></div>
          <div class="stamp">SETTLED</div>
        </article>
      </div>
    </div>
  </main>
  <footer><span>Department of passing things</span><span>Customer copy</span></footer>
</div>
<script>
  const exchanges = [
    ["One hand held against a closing lift door.", "A man and a cello, both slightly out of breath."],
    ["A saucer of water on the back step.", "One sparrow, returned to its usual size after bathing."],
    ["Directions to the station, drawn on a napkin.", "The loan of a very good pen. Reluctantly returned."],
    ["The last corner of a buttery piece of toast.", "A dog's best impression of a dog who has never eaten."],
    ["A chair carried out to the pavement.", "The long version of how the pear tree came down."],
    ["One glove set on a railing, fingers pointing up.", "A small blue hand waving at the whole street."],
    ["Five minutes spent untangling a necklace.", "A crescent pressed into the thumb, gone by lunch."],
    ["A peach passed over the garden wall.", "A peach stone passed back three summers later, now a tree in a bucket."],
    ["A place in the queue at the bakery.", "The name of the bun with the sour cherries inside."],
    ["One teaspoon tapped against a radiator pipe.", "From the flat upstairs: two teaspoons, technically one teaspoon twice."]
  ];
  let n = 0;
  const slip = document.getElementById("slip");
  document.getElementById("issue").addEventListener("click", () => {
    n++;
    const [a,b] = exchanges[n % exchanges.length];
    document.getElementById("given").textContent = a;
    document.getElementById("taken").textContent = b;
    document.getElementById("serial").textContent = "NO. " + String(n + 1).padStart(4, "0");
    slip.classList.remove("feeding");
    void slip.offsetWidth;
    slip.classList.add("feeding");
  });
</script>
</body>
</html>
```

What: A little green cashier’s window dispenses paper receipts for everyday exchanges that never involved money.