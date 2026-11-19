<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="65%">
      <stop offset="0%" stop-color="#171f4a"/>
      <stop offset="55%" stop-color="#0b1029"/>
      <stop offset="100%" stop-color="#050714"/>
    </radialGradient>
    <radialGradient id="aura" cx="50%" cy="46%" r="48%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.38"/>
      <stop offset="45%" stop-color="#818cf8" stop-opacity="0.18"/>
      <stop offset="78%" stop-color="#c084fc" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#050714" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="headFill" x1="20%" y1="0%" x2="80%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.28"/>
      <stop offset="45%" stop-color="#6366f1" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0.3"/>
    </linearGradient>
    <linearGradient id="headStroke" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7dd3fc"/>
      <stop offset="50%" stop-color="#a5b4fc"/>
      <stop offset="100%" stop-color="#f0abfc"/>
    </linearGradient>
    <linearGradient id="mantleGrad" x1="50%" y1="0%" x2="50%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.35"/>
      <stop offset="55%" stop-color="#6366f1" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#1e1b4b" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="waveGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity="0"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="waveGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f472b6" stop-opacity="0"/>
      <stop offset="50%" stop-color="#a78bfa" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="sparkGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="45%" stop-color="#bae6fd"/>
      <stop offset="100%" stop-color="#e879f9"/>
    </linearGradient>
    <radialGradient id="eyeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="35%" stop-color="#67e8f9"/>
      <stop offset="70%" stop-color="#38bdf8" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <clipPath id="headClip">
      <path d="M200 94 C250 94 274 134 270 186 C266 234 236 270 200 274 C164 270 134 234 130 186 C126 134 150 94 200 94 Z"/>
    </clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <circle cx="200" cy="185" r="185" fill="url(#aura)"/>

  <g stroke="#818cf8" fill="none" opacity="0.16">
    <circle cx="200" cy="185" r="118" stroke-dasharray="3 6" stroke-width="1"/>
    <circle cx="200" cy="185" r="146" stroke-width="0.8"/>
    <circle cx="200" cy="185" r="172" stroke-dasharray="1 9" stroke-width="1.2"/>
  </g>

  <g opacity="0.7" fill="#e0f2fe">
    <circle cx="48" cy="64" r="1.3"/><circle cx="92" cy="42" r="0.9"/>
    <circle cx="136" cy="58" r="1.1"/><circle cx="272" cy="48" r="1.4"/>
    <circle cx="334" cy="74" r="1.2"/><circle cx="358" cy="142" r="1"/>
    <circle cx="42" cy="158" r="1.1"/><circle cx="64" cy="248" r="1.3"/>
    <circle cx="348" cy="252" r="1.2"/><circle cx="312" cy="316" r="1"/>
    <circle cx="88" cy="322" r="0.9"/><circle cx="222" cy="36" r="1.2"/>
    <circle cx="164" cy="32" r="0.8"/><circle cx="368" cy="204" r="0.9"/>
    <circle cx="32" cy="210" r="1"/>
  </g>

  <g fill="none" stroke-width="1.2" opacity="0.55">
    <ellipse cx="200" cy="188" rx="154" ry="52" stroke="url(#waveGrad1)" transform="rotate(-24 200 188)"/>
    <ellipse cx="200" cy="188" rx="154" ry="52" stroke="url(#waveGrad2)" transform="rotate(24 200 188)"/>
    <ellipse cx="200" cy="188" rx="126" ry="38" stroke="#67e8f9" stroke-opacity="0.28" transform="rotate(-6 200 188)"/>
  </g>

  <g stroke="#7dd3fc" stroke-opacity="0.24" stroke-width="0.9">
    <line x1="78" y1="120" x2="138" y2="148"/>
    <line x1="78" y1="120" x2="108" y2="188"/>
    <line x1="108" y1="188" x2="132" y2="196"/>
    <line x1="322" y1="120" x2="262" y2="148"/>
    <line x1="322" y1="120" x2="292" y2="188"/>
    <line x1="292" y1="188" x2="268" y2="196"/>
    <line x1="118" y1="78" x2="158" y2="112"/>
    <line x1="282" y1="78" x2="242" y2="112"/>
  </g>
  <g fill="#7dd3fc" filter="url(#glow)">
    <circle cx="78" cy="120" r="2.6"/><circle cx="108" cy="188" r="2"/>
    <circle cx="322" cy="120" r="2.6"/><circle cx="292" cy="188" r="2"/>
    <circle cx="118" cy="78" r="2.2" fill="#c084fc"/>
    <circle cx="282" cy="78" r="2.2" fill="#f472b6"/>
  </g>

  <path d="M84 400 C102 332 142 296 200 296 C258 296 298 332 316 400 Z" fill="url(#mantleGrad)" stroke="url(#headStroke)" stroke-opacity="0.45" stroke-width="1.2"/>
  <path d="M174 266 L178 302 Q200 314 222 302 L226 266 Z" fill="url(#headFill)" opacity="0.7"/>
  <g fill="none" stroke-width="1.4" opacity="0.65">
    <path d="M68 400 C118 352 156 322 200 322 C244 322 282 352 332 400" stroke="url(#waveGrad1)"/>
    <path d="M108 400 C142 362 170 342 200 342 C230 342 258 362 292 400" stroke="url(#waveGrad2)"/>
    <path d="M144 400 C166 374 184 364 200 364 C216 364 234 374 256 400" stroke="#7dd3fc" stroke-opacity="0.45"/>
  </g>
  <circle cx="200" cy="316" r="4" fill="#e0f2fe" filter="url(#glow)"/>
  <circle cx="200" cy="316" r="10" fill="none" stroke="#67e8f9" stroke-opacity="0.45" stroke-width="1"/>

  <path d="M200 94 C250 94 274 134 270 186 C266 234 236 270 200 274 C164 270 134 234 130 186 C126 134 150 94 200 94 Z" fill="url(#headFill)" stroke="url(#headStroke)" stroke-width="1.8" filter="url(#glow)"/>

  <g clip-path="url(#headClip)">
    <polygon points="200,94 134,148 200,168" fill="#38bdf8" opacity="0.1"/>
    <polygon points="200,94 266,148 200,168" fill="#a78bfa" opacity="0.12"/>
    <polygon points="130,186 200,168 152,248" fill="#6366f1" opacity="0.1"/>
    <polygon points="270,186 200,168 248,248" fill="#c084fc" opacity="0.1"/>
    <polygon points="200,274 152,248 248,248" fill="#22d3ee" opacity="0.11"/>

    <g stroke="#bae6fd" stroke-opacity="0.28" stroke-width="0.8" fill="none">
      <path d="M144 152 L176 134 L200 138 L224 134 L256 152"/>
      <path d="M162 114 L176 134 L164 166"/>
      <path d="M238 114 L224 134 L236 166"/>
      <path d="M146 218 Q170 230 184 256"/>
      <path d="M254 218 Q230 230 216 256"/>
    </g>
    <g fill="#e0f2fe" opacity="0.75">
      <circle cx="176" cy="134" r="2"/><circle cx="224" cy="134" r="2"/>
      <circle cx="162" cy="114" r="1.6"/><circle cx="238" cy="114" r="1.6"/>
      <circle cx="144" cy="152" r="1.5"/><circle cx="256" cy="152" r="1.5"/>
    </g>
    <path d="M138 184 C138 140 162 104 200 104 C238 104 262 140 262 184" fill="none" stroke="#ffffff" stroke-opacity="0.22" stroke-width="1.2"/>
  </g>

  <g filter="url(#softGlow)">
    <path d="M200 112 Q203 135 226 138 Q203 141 200 164 Q197 141 174 138 Q197 135 200 112 Z" fill="url(#sparkGrad)"/>
  </g>
  <circle cx="200" cy="138" r="3" fill="#ffffff"/>

  <g>
    <circle cx="169" cy="195" r="18" fill="url(#eyeGlow)" opacity="0.75"/>
    <circle cx="169" cy="195" r="8.5" fill="none" stroke="#bae6fd" stroke-width="1.4" opacity="0.9"/>
    <circle cx="169" cy="195" r="4" fill="#ffffff" filter="url(#glow)"/>
    <path d="M152 193 Q169 179 186 193" fill="none" stroke="#e0f2fe" stroke-width="2" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M157 202 Q169 207 181 202" fill="none" stroke="#7dd3fc" stroke-width="1" stroke-linecap="round" opacity="0.6"/>
  </g>

  <g>
    <circle cx="231" cy="195" r="18" fill="url(#eyeGlow)" opacity="0.75"/>
    <circle cx="231" cy="195" r="8.5" fill="none" stroke="#bae6fd" stroke-width="1.4" opacity="0.9"/>
    <circle cx="231" cy="195" r="4" fill="#ffffff" filter="url(#glow)"/>
    <path d="M214 193 Q231 179 248 193" fill="none" stroke="#e0f2fe" stroke-width="2" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M219 202 Q231 207 243 202" fill="none" stroke="#7dd3fc" stroke-width="1" stroke-linecap="round" opacity="0.6"/>
  </g>

  <path d="M197 214 L200 220 L203 214" fill="none" stroke="#a5b4fc" stroke-width="1" stroke-linecap="round" opacity="0.55"/>
  <path d="M181 234 Q200 248 219 234" fill="none" stroke="url(#headStroke)" stroke-width="2.2" stroke-linecap="round" filter="url(#glow)"/>
  <path d="M188 238 Q200 245 212 238" fill="none" stroke="#ffffff" stroke-width="1" stroke-linecap="round" opacity="0.7"/>

  <g fill="url(#sparkGrad)" filter="url(#glow)">
    <path d="M84 82 Q85 90 93 91 Q85 92 84 100 Q83 92 75 91 Q83 90 84 82 Z"/>
    <path d="M318 96 Q319 102 325 103 Q319 104 318 110 Q317 104 311 103 Q317 102 318 96 Z"/>
    <path d="M332 214 Q333 221 340 222 Q333 223 332 230 Q331 223 324 222 Q331 221 332 214 Z"/>
    <path d="M68 230 Q69 235 74 236 Q69 237 68 242 Q67 237 62 236 Q67 235 68 230 Z"/>
    <path d="M200 46 Q201 53 208 54 Q201 55 200 62 Q199 55 192 54 Q199 53 200 46 Z"/>
  </g>

  <g fill="none" stroke-linecap="round" opacity="0.75">
    <path d="M62 172 L55 180 L62 188" stroke="#67e8f9" stroke-width="1.4"/>
    <path d="M338 172 L345 180 L338 188" stroke="#f0abfc" stroke-width="1.4"/>
    <path d="M104 282 Q122 272 138 282" stroke="#38bdf8" stroke-width="1.2" opacity="0.6"/>
    <path d="M262 282 Q278 272 296 282" stroke="#c084fc" stroke-width="1.2" opacity="0.6"/>
  </g>

  <path d="M56 244 A154 52 -24 0 0 344 132" fill="none" stroke="url(#waveGrad1)" stroke-width="1.5" opacity="0.75" filter="url(#glow)"/>
  <circle cx="94" cy="242" r="3" fill="#67e8f9" filter="url(#glow)"/>
  <circle cx="308" cy="144" r="2.8" fill="#f0abfc" filter="url(#glow)"/>
</svg>