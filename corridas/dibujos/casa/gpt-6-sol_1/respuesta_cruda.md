<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="sky" x2="0" y2="1">
      <stop stop-color="#80bfd0"/>
      <stop offset="1" stop-color="#f6d7a9"/>
    </linearGradient>
    <linearGradient id="wall" x2="1" y2="1">
      <stop stop-color="#fff1d4"/>
      <stop offset="1" stop-color="#eacb9f"/>
    </linearGradient>
    <linearGradient id="roof" x2="0" y2="1">
      <stop stop-color="#c66b5d"/>
      <stop offset="1" stop-color="#9d4e50"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <circle cx="337" cy="65" r="29" fill="#fff3bf" opacity=".9"/>
  <g fill="#fff8e8" opacity=".75">
    <ellipse cx="64" cy="76" rx="31" ry="12"/>
    <ellipse cx="87" cy="72" rx="24" ry="15"/>
    <ellipse cx="113" cy="79" rx="29" ry="10"/>
    <ellipse cx="289" cy="111" rx="23" ry="9"/>
    <ellipse cx="311" cy="107" rx="19" ry="12"/>
  </g>

  <path d="M0 290Q74 252 150 282T300 276Q357 254 400 281V400H0Z" fill="#96b994"/>
  <path d="M0 318Q95 294 192 319T400 310V400H0Z" fill="#79a579"/>
  <path d="M0 353Q91 336 174 351T400 341V400H0Z" fill="#6b996b"/>

  <!-- Fence behind the house -->
  <g fill="#f7e7c6" stroke="#d6ba92" stroke-width="2">
    <path d="M12 278h8v54h-8zm22-5h8v59h-8zm22 5h8v54h-8zm278 0h8v54h-8zm22-5h8v59h-8zm22 5h8v54h-8z"/>
    <path d="M8 294h61v7H8zm0 23h61v7H8zm321-23h63v7h-63zm0 23h63v7h-63z"/>
  </g>

  <!-- Chimney -->
  <path d="M258 83h39v85h-39z" fill="#b86259" stroke="#854b49" stroke-width="3"/>
  <path d="M253 78h49v12h-49z" fill="#d07b66" stroke="#854b49" stroke-width="3"/>
  <path d="M265 105h13m7 18h12m-39 20h17" stroke="#e7a17b" stroke-width="3" opacity=".7"/>

  <!-- House and roof -->
  <path d="M85 166h230v160H85z" fill="url(#wall)" stroke="#765c55" stroke-width="4"/>
  <path d="M85 168 200 70l115 98z" fill="#b9615c" stroke="#75454b" stroke-width="5" stroke-linejoin="round"/>
  <path d="M74 174 200 65l126 109-8 9-118-102L82 183z" fill="url(#roof)" stroke="#75454b" stroke-width="4" stroke-linejoin="round"/>
  <path d="M95 185h210M95 318h210" stroke="#d6ac85" stroke-width="3"/>
  <path d="M95 186v132m210-132v132" stroke="#f8e4bf" stroke-width="5"/>

  <!-- Attic window -->
  <circle cx="200" cy="142" r="21" fill="#fff1ce" stroke="#744d4b" stroke-width="4"/>
  <circle cx="200" cy="142" r="15" fill="#8ebec0"/>
  <path d="M200 127v30m-15-15h30" stroke="#fff1ce" stroke-width="4"/>
  <circle cx="194" cy="136" r="3" fill="#fff9dc" opacity=".75"/>

  <!-- Windows -->
  <g stroke="#765b52" stroke-width="4">
    <rect x="109" y="205" width="53" height="66" rx="3" fill="#fff1ce"/>
    <rect x="238" y="205" width="53" height="66" rx="3" fill="#fff1ce"/>
  </g>
  <g fill="#a6c9c2">
    <rect x="116" y="212" width="39" height="52"/>
    <rect x="245" y="212" width="39" height="52"/>
  </g>
  <g fill="#fbe8aa">
    <path d="M116 212h39v52h-39zM245 212h39v52h-39z" opacity=".28"/>
  </g>
  <g stroke="#fff4d7" stroke-width="5">
    <path d="M135.5 210v56m-21-28h43M264.5 210v56m-21-28h43"/>
  </g>
  <g fill="#fff6df" opacity=".8">
    <path d="m118 215 11-1-11 13zm129 0 11-1-11 13z"/>
  </g>
  <g fill="#a86d58" stroke="#765b52" stroke-width="3">
    <path d="M104 272h63v9h-63zm129 0h63v9h-63z"/>
  </g>
  <g fill="#5b966c">
    <ellipse cx="119" cy="270" rx="12" ry="7"/>
    <ellipse cx="140" cy="269" rx="14" ry="8"/>
    <ellipse cx="155" cy="270" rx="10" ry="6"/>
    <ellipse cx="248" cy="270" rx="12" ry="7"/>
    <ellipse cx="269" cy="269" rx="14" ry="8"/>
    <ellipse cx="284" cy="270" rx="10" ry="6"/>
  </g>
  <g fill="#f9d899">
    <circle cx="125" cy="267" r="3"/><circle cx="149" cy="265" r="3"/>
    <circle cx="254" cy="267" r="3"/><circle cx="278" cy="265" r="3"/>
  </g>

  <!-- Front door -->
  <path d="M176 326v-61a24 24 0 0 1 48 0v61z" fill="#8c6660" stroke="#654b49" stroke-width="4"/>
  <path d="M183 326v-60a17 17 0 0 1 34 0v60z" fill="#527d78"/>
  <path d="M200 250v76" stroke="#345e5c" stroke-width="3"/>
  <circle cx="209" cy="291" r="3.5" fill="#f8d68f"/>
  <path d="M169 327h62v9h-62z" fill="#c59274" stroke="#765b52" stroke-width="3"/>

  <!-- Path, shrubs and flowers -->
  <path d="M181 336h38q27 28 48 64H129q25-41 52-64Z" fill="#dbc5a6"/>
  <path d="M187 346h27m-41 19h53m-70 24h89" stroke="#f4e5ca" stroke-width="4" stroke-linecap="round"/>
  <g fill="#4f8b68">
    <circle cx="72" cy="326" r="20"/><circle cx="93" cy="334" r="15"/>
    <circle cx="315" cy="329" r="17"/><circle cx="335" cy="326" r="20"/>
  </g>
  <g fill="#76a978">
    <circle cx="64" cy="319" r="11"/><circle cx="322" cy="321" r="10"/>
  </g>
  <g fill="#f4ba87">
    <circle cx="58" cy="320" r="4"/><circle cx="91" cy="330" r="4"/>
    <circle cx="328" cy="313" r="4"/><circle cx="346" cy="330" r="4"/>
  </g>
  <g stroke="#48845f" stroke-width="2" stroke-linecap="round">
    <path d="M39 371v-16m5 18v-12m267 14v-18m8 18v-12m41 3v-16"/>
  </g>
  <g fill="#fff1d6">
    <circle cx="39" cy="353" r="5"/><circle cx="44" cy="359" r="4"/>
    <circle cx="311" cy="355" r="5"/><circle cx="319" cy="361" r="4"/>
    <circle cx="360" cy="349" r="5"/>
  </g>
  <g fill="#e9aa69">
    <circle cx="39" cy="353" r="2"/><circle cx="311" cy="355" r="2"/>
    <circle cx="360" cy="349" r="2"/>
  </g>
</svg>