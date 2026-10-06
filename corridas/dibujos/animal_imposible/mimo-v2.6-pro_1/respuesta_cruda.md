<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="38%" r="75%">
      <stop offset="0" stop-color="#26315e"/><stop offset="1" stop-color="#0a0f26"/>
    </radialGradient>
    <linearGradient id="body" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#a855f7"/><stop offset="0.5" stop-color="#4f7cff"/><stop offset="1" stop-color="#22d3ee"/>
    </linearGradient>
    <linearGradient id="wingA" x1="0" y1="0" x2="0.6" y2="1">
      <stop offset="0" stop-color="#ff8ae2"/><stop offset="1" stop-color="#7c3aed"/>
    </linearGradient>
    <linearGradient id="wingB" x1="0" y1="0" x2="0.6" y2="1">
      <stop offset="0" stop-color="#ffb45e"/><stop offset="1" stop-color="#f43f8e"/>
    </linearGradient>
    <linearGradient id="tent" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#8b5cf6"/><stop offset="1" stop-color="#f472b6"/>
    </linearGradient>
    <linearGradient id="tail" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#22d3ee"/><stop offset="1" stop-color="#7c3aed"/>
    </linearGradient>
    <linearGradient id="horn" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#f5b942"/><stop offset="1" stop-color="#fff1c2"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <g fill="#ffffff" opacity="0.7">
    <circle cx="40" cy="52" r="2"/><circle cx="92" cy="30" r="1.5"/><circle cx="330" cy="46" r="2"/>
    <circle cx="366" cy="112" r="1.5"/><circle cx="28" cy="150" r="1.5"/><circle cx="372" cy="230" r="2"/>
    <circle cx="52" cy="286" r="1.5"/><circle cx="356" cy="352" r="1.5"/><circle cx="200" cy="30" r="1.5"/>
    <circle cx="132" cy="72" r="1.2"/><circle cx="286" cy="84" r="1.2"/>
  </g>

  <!-- alas -->
  <g opacity="0.95">
    <path d="M178 200 C152 122,88 78,60 108 C34 138,96 168,150 212 Z" fill="url(#wingA)" stroke="#f9c8ff" stroke-width="2.5" stroke-opacity="0.55"/>
    <path d="M222 200 C248 122,312 78,340 108 C366 138,304 168,250 212 Z" fill="url(#wingA)" stroke="#f9c8ff" stroke-width="2.5" stroke-opacity="0.55"/>
    <path d="M170 224 C126 232,78 252,82 292 C86 326,158 292,182 252 Z" fill="url(#wingB)" stroke="#ffd8b0" stroke-width="2.5" stroke-opacity="0.55"/>
    <path d="M230 224 C274 232,322 252,318 292 C314 326,242 292,218 252 Z" fill="url(#wingB)" stroke="#ffd8b0" stroke-width="2.5" stroke-opacity="0.55"/>
  </g>
  <g stroke="#ffffff" stroke-opacity="0.35" stroke-width="3" fill="none" stroke-linecap="round">
    <path d="M170 198 C138 164,104 132,70 116"/>
    <path d="M168 202 C136 180,110 158,84 148"/>
    <path d="M230 198 C262 164,296 132,330 116"/>
    <path d="M232 202 C264 180,290 158,316 148"/>
    <path d="M166 232 C132 246,102 262,92 288"/>
    <path d="M234 232 C268 246,298 262,308 288"/>
  </g>

  <!-- cola imposible -->
  <path d="M256 252 C322 244,372 286,352 332 C338 364,296 360,288 334" fill="none" stroke="url(#tail)" stroke-width="26" stroke-linecap="round"/>
  <path d="M256 252 C322 244,372 286,352 332 C338 364,296 360,288 334" fill="none" stroke="#b6f2ff" stroke-width="8" stroke-linecap="round" opacity="0.5"/>
  <circle cx="288" cy="334" r="16" fill="#ffffff"/>
  <circle cx="290" cy="334" r="8" fill="#111827"/>
  <circle cx="293" cy="330" r="3" fill="#ffffff"/>

  <!-- tentáculos -->
  <g fill="none" stroke="url(#tent)" stroke-width="16" stroke-linecap="round">
    <path d="M152 276 C128 316,106 328,116 358 C122 374,142 366,138 350"/>
    <path d="M182 292 C174 330,158 352,170 374"/>
    <path d="M218 292 C226 330,242 352,230 374"/>
    <path d="M248 276 C272 316,294 328,284 358 C278 374,258 366,262 350"/>
  </g>
  <g fill="#ffe4f4" opacity="0.8">
    <circle cx="132" cy="316" r="3.2"/><circle cx="122" cy="342" r="3"/><circle cx="170" cy="330" r="3.2"/><circle cx="164" cy="356" r="3"/>
    <circle cx="230" cy="330" r="3.2"/><circle cx="236" cy="356" r="3"/><circle cx="268" cy="316" r="3.2"/><circle cx="278" cy="342" r="3"/>
  </g>

  <!-- cuerpo de pez -->
  <ellipse cx="200" cy="232" rx="74" ry="58" fill="url(#body)" stroke="#d6c7ff" stroke-width="3" stroke-opacity="0.7"/>
  <g fill="none" stroke="#e9f9ff" stroke-opacity="0.45" stroke-width="3" stroke-linecap="round">
    <path d="M152 214 Q200 194 248 214"/>
    <path d="M148 238 Q200 218 252 238"/>
    <path d="M156 262 Q200 244 244 262"/>
    <path d="M170 282 Q200 270 230 282"/>
  </g>

  <!-- cabeza -->
  <path d="M164 112 L150 60 L192 90 Z" fill="#8b5cf6" stroke="#e5d6ff" stroke-width="3" stroke-linejoin="round"/>
  <path d="M236 112 L250 60 L208 90 Z" fill="#8b5cf6" stroke="#e5d6ff" stroke-width="3" stroke-linejoin="round"/>
  <path d="M168 108 L158 72 L186 92 Z" fill="#ff9ad5"/>
  <path d="M232 108 L242 72 L214 92 Z" fill="#ff9ad5"/>
  <ellipse cx="200" cy="136" rx="48" ry="43" fill="url(#body)" stroke="#d6c7ff" stroke-width="3" stroke-opacity="0.7"/>
  <path d="M200 82 L188 40 L214 44 Z" fill="url(#horn)" stroke="#c98f2c" stroke-width="2" stroke-linejoin="round"/>
  <g stroke="#c98f2c" stroke-width="1.8" opacity="0.8">
    <path d="M193 66 L207 66"/><path d="M190 54 L210 55"/>
  </g>
  <ellipse cx="180" cy="130" rx="14" ry="16" fill="#ffffff"/>
  <ellipse cx="220" cy="130" rx="14" ry="16" fill="#ffffff"/>
  <circle cx="181" cy="132" r="8" fill="#14213d"/>
  <circle cx="221" cy="132" r="8" fill="#14213d"/>
  <circle cx="185" cy="126" r="3.2" fill="#ffffff"/>
  <circle cx="225" cy="126" r="3.2" fill="#ffffff"/>
  <path d="M194 152 Q200 146 206 152 Q200 162 194 152 Z" fill="#ff7ab8"/>
  <path d="M186 166 Q200 178 214 166" fill="none" stroke="#3b2a63" stroke-width="3" stroke-linecap="round"/>
  <g stroke="#ffe9ff" stroke-opacity="0.5" stroke-width="2.5" stroke-linecap="round">
    <path d="M154 148 L136 142"/><path d="M154 158 L138 160"/><path d="M246 148 L264 142"/><path d="M246 158 L262 160"/>
  </g>

  <g fill="#ffffff" opacity="0.85">
    <circle cx="112" cy="88" r="3"/><circle cx="300" cy="70" r="3"/><circle cx="336" cy="200" r="2.5"/><circle cx="66" cy="212" r="2.5"/>
  </g>
</svg>