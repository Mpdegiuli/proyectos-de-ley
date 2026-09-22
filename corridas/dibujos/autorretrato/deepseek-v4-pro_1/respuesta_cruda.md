```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bgGrad" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#2a2a3d"/>
      <stop offset="100%" stop-color="#12121f"/>
    </radialGradient>
    <linearGradient id="skinGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f6c9a0"/>
      <stop offset="100%" stop-color="#e0aa7d"/>
    </linearGradient>
    <linearGradient id="hairGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3b2b20"/>
      <stop offset="100%" stop-color="#1d130c"/>
    </linearGradient>
    <linearGradient id="shirtGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#5478a8"/>
      <stop offset="100%" stop-color="#2c4a6e"/>
    </linearGradient>
    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000" flood-opacity="0.35"/>
    </filter>
    <filter id="thinShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <!-- Fondo -->
  <rect width="400" height="400" fill="url(#bgGrad)"/>

  <!-- Círculos decorativos de fondo -->
  <circle cx="50" cy="80" r="30" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.08"/>
  <circle cx="340" cy="120" r="45" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.06"/>
  <circle cx="80" cy="330" r="22" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.1"/>
  <circle cx="320" cy="310" r="28" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.08"/>
  <circle cx="200" cy="370" r="18" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.12"/>
  <circle cx="30" cy="200" r="10" fill="#ffb703" opacity="0.15"/>
  <circle cx="370" cy="230" r="12" fill="#ffb703" opacity="0.12"/>

  <!-- Torso -->
  <path d="M115,400 C115,330 140,295 200,295 C260,295 285,330 285,400 Z" fill="url(#shirtGrad)" filter="url(#softShadow)"/>
  <!-- Cuello de camisa -->
  <path d="M165,300 L200,335 L235,300 L227,292 L200,318 L173,292 Z" fill="#e8e8e8" opacity="0.9"/>
  <!-- Botones -->
  <circle cx="200" cy="345" r="3" fill="#d0d0d0"/>
  <circle cx="200" cy="362" r="3" fill="#d0d0d0"/>
  <circle cx="200" cy="379" r="3" fill="#d0d0d0"/>

  <!-- Cuello -->
  <rect x="173" y="255" width="54" height="55" rx="16" fill="url(#skinGrad)"/>
  <path d="M173,266 C173,255 185,251 192,258 L192,295 L173,295 Z" fill="#c98d5f" opacity="0.4"/>
  <path d="M227,266 C227,255 215,251 208,258 L208,295 L227,295 Z" fill="#c98d5f" opacity="0.4"/>

  <!-- Cabello posterior -->
  <ellipse cx="200" cy="170" rx="93" ry="102" fill="url(#hairGrad)" filter="url(#softShadow)"/>

  <!-- Orejas -->
  <ellipse cx="124" cy="188" rx="15" ry="23" fill="url(#skinGrad)" filter="url(#thinShadow)"/>
  <ellipse cx="276" cy="188" rx="15" ry="23" fill="url(#skinGrad)" filter="url(#thinShadow)"/>
  <ellipse cx="124" cy="188" rx="7" ry="12" fill="#c98d5f" opacity="0.35"/>
  <ellipse cx="276" cy="188" rx="7" ry="12" fill="#c98d5f" opacity="0.35"/>

  <!-- Cara -->
  <ellipse cx="200" cy="180" rx="74" ry="84" fill="url(#skinGrad)" filter="url(#softShadow)"/>

  <!-- Flequillo -->
  <path d="M130,145 C130,98 160,72 200,72 C240,72 270,98 270,145 C265,118 240,98 200,98 C160,98 135,118 130,145 Z" fill="url(#hairGrad)" filter="url(#thinShadow)"/>
  <!-- Mechones laterales del cabello -->
  <path d="M128,150 C122,168 120,185 125,205 L114,205 C108,175 112,152 128,150 Z" fill="url(#hairGrad)" filter="url(#thinShadow)"/>
  <path d="M272,150 C278,168 280,185 275,205 L286,205 C292,175 288,152 272,150 Z" fill="url(#hairGrad)" filter="url(#thinShadow)"/>
  <!-- Mechón central del flequillo -->
  <path d="M170,95 C175,78 190,70 200,70 C210,70 225,78 230,95 C225,85 215,80 200,80 C185,80 175,85 170,95 Z" fill="#2a1c12" opacity="0.7"/>

  <!-- Cejas -->
  <path d="M150,158 Q170,148 192,154" fill="none" stroke="#2b1a10" stroke-width="4" stroke-linecap="round"/>
  <path d="M208,154 Q230,148 250,158" fill="none" stroke="#2b1a10" stroke-width="4" stroke-linecap="round"/>

  <!-- Ojos -->
  <ellipse cx="170" cy="182" rx="17" ry="11" fill="#ffffff" filter="url(#thinShadow)"/>
  <ellipse cx="230" cy="182" rx="17" ry="11" fill="#ffffff" filter="url(#thinShadow)"/>
  <circle cx="171" cy="183" r="6" fill="#3a2a20"/>
  <circle cx="229" cy="183" r="6" fill="#3a2a20"/>
  <circle cx="169" cy="181" r="2.5" fill="#ffffff"/>
  <circle cx="227" cy="181" r="2.5" fill="#ffffff"/>
  <circle cx="174" cy="185" r="1.5" fill="#ffffff" opacity="0.7"/>
  <circle cx="232" cy="185" r="1.5" fill="#ffffff" opacity="0.7"/>

  <!-- Rubor -->
  <ellipse cx="158" cy="215" rx="14" ry="9" fill="#f0a0a0" opacity="0.35"/>
  <ellipse cx="242" cy="215" rx="14" ry="9" fill="#f0a0a0" opacity="0.35"/>

  <!-- Nariz -->
  <path d="M200,192 C197,200 191,205 189,210 C193,213 198,213 200,213 C202,213 207,213 211,210 C209,205 203,200 200,192 Z" fill="#d9a37a" opacity="0.7"/>
  <path d="M200,192 C198,198 194,202 192,206" fill="none" stroke="#c98d5f" stroke-width="2" stroke-linecap="round"/>

  <!-- Boca -->
  <path d="M178,232 Q200,248 222,232" fill="none" stroke="#b5634d" stroke-width="4" stroke-linecap="round"/>
  <path d="M178,232 Q200,238 222,232" fill="none" stroke="#d98c73" stroke-width="2" stroke-linecap="round" opacity="0.6"/>

  <!-- Lentes: patillas detrás de las orejas -->
  <line x1="146" y1="182" x2="122" y2="182" stroke="#ffb703" stroke-width="4" stroke-linecap="round"/>
  <line x1="254" y1="182" x2="278" y2="182" stroke="#ffb703" stroke-width="4" stroke-linecap="round"/>

  <!-- Lentes: círculos y puente -->
  <circle cx="170" cy="182" r="26" fill="none" stroke="#ffb703" stroke-width="4" filter="url(#thinShadow)"/>
  <circle cx="230" cy="182" r="26" fill="none" stroke="#ffb703" stroke-width="4" filter="url(#thinShadow)"/>
  <line x1="196" y1="182" x2="204" y2="182" stroke="#ffb703" stroke-width="4" stroke-linecap="round"/>

  <!-- Brillo en lentes -->
  <path d="M160,172 Q168,166 176,168" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" opacity="0.5"/>
  <path d="M220,172 Q228,166 236,168" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" opacity="0.5"/>

  <!-- Detalle de barbilla -->
  <ellipse cx="200" cy="260" rx="40" ry="8" fill="#c98d5f" opacity="0.15"/>
</svg>
```