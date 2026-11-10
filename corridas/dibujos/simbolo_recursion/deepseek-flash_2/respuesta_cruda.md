```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="72%">
      <stop offset="0" stop-color="#17253f"/>
      <stop offset="1" stop-color="#0a111f"/>
    </radialGradient>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#22d3ee"/>
      <stop offset="0.55" stop-color="#60a5fa"/>
      <stop offset="1" stop-color="#a78bfa"/>
    </linearGradient>
  </defs>

  <rect x="0" y="0" width="400" height="400" rx="58" fill="url(#bg)"/>

  <!-- halo suave -->
  <path d="M350 350 V50 H50 V350 H325 V75 H75 V325 H300 V100 H100 V300 H275 V125 H125 V275 H250 V150 H150 V250 H225 V175 H175 V225 H200 V200"
        fill="none" stroke="url(#g)" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" opacity="0.13"/>

  <!-- espiral cuadrada que se repite hacia adentro -->
  <path d="M350 350 V50 H50 V350 H325 V75 H75 V325 H300 V100 H100 V300 H275 V125 H125 V275 H250 V150 H150 V250 H225 V175 H175 V225 H200 V200"
        fill="none" stroke="url(#g)" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- caso base -->
  <circle cx="200" cy="200" r="15" fill="#eafcff"/>
  <circle cx="200" cy="200" r="26" fill="none" stroke="#eafcff" stroke-opacity="0.35" stroke-width="3"/>
</svg>
```