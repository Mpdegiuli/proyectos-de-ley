<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="left" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#397f7c"/>
      <stop offset="1" stop-color="#173c48"/>
    </linearGradient>
    <linearGradient id="right" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#244956"/>
      <stop offset="1" stop-color="#102b38"/>
    </linearGradient>
    <linearGradient id="bridge" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#f18b69"/>
      <stop offset="1" stop-color="#c95851"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%">
      <feGaussianBlur stdDeviation="10"/>
    </filter>
  </defs>

  <rect width="400" height="400" fill="#f5f0e7"/>
  <circle cx="200" cy="197" r="157" fill="none" stroke="#dfd7ca" stroke-width="1.5"/>
  <circle cx="200" cy="197" r="179" fill="none" stroke="#e8e1d6"/>
  <path d="M200 13v30M200 351v35M13 197h30M357 197h30" stroke="#d9d0c2" stroke-width="1.5"/>

  <!-- Una A cuyas superficies se turnan para estar delante. -->
  <path d="M185 65h38l134 272h-53l-31-69H128l-29 69H47z"
        fill="#604d46" opacity=".16" filter="url(#shadow)" transform="translate(5 10)"/>

  <!-- Pata izquierda: pasa por detrás del travesaño. -->
  <path d="M185 65h38L105 337H47Z" fill="url(#left)" stroke="#142f3a" stroke-width="5" stroke-linejoin="round"/>
  <path d="M185 65h38L105 337H78Z" fill="#73a49a" opacity=".58"/>
  <path d="M78 337 185 65l18 14L105 337Z" fill="#122f3c" opacity=".55"/>

  <!-- Travesaño: cruza por delante de la pata izquierda. -->
  <path d="M116 226h162l22 42H97Z" fill="url(#bridge)" stroke="#142f3a" stroke-width="5" stroke-linejoin="round"/>
  <path d="M116 226h162l8 15H109Z" fill="#ffb18a"/>
  <path d="M109 241h177l14 27H97Z" fill="#d96b5b"/>
  <path d="M117 227h161" stroke="#ffe0b6" stroke-width="2" opacity=".8"/>

  <!-- La pata derecha tapa el mismo travesaño. -->
  <path d="M185 65h38l134 272h-53Z" fill="url(#right)" stroke="#142f3a" stroke-width="5" stroke-linejoin="round"/>
  <path d="M185 65h38l134 272h-25Z" fill="#4e8b83"/>
  <path d="M205 82 332 337h-28L185 65Z" fill="#173a46" opacity=".8"/>

  <!-- En el vértice, la cara izquierda vuelve inexplicablemente al frente. -->
  <path d="M185 65h38l23 47-27-17-21 43-27-1Z" fill="#72a69b" stroke="#142f3a" stroke-width="5" stroke-linejoin="round"/>
  <path d="m185 65 38 0 23 47-27-17Z" fill="#b0c6aa"/>
  <path d="m198 138 21-43 27 17" fill="none" stroke="#173a46" stroke-width="3" stroke-linejoin="round"/>

  <!-- Una arista del travesaño sale por delante de ambas patas. -->
  <path d="M97 268h203l-8 12H89Z" fill="#173a46"/>
  <path d="M97 268h203" stroke="#f6ad87" stroke-width="3"/>

  <path d="M48 350h309" stroke="#cfc5b7" stroke-width="2"/>
  <circle cx="48" cy="350" r="3" fill="#cfc5b7"/>
  <circle cx="357" cy="350" r="3" fill="#cfc5b7"/>
</svg>