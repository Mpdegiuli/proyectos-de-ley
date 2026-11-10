<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FBBF24" stop-opacity="0.38"/>
      <stop offset="55%" stop-color="#FBBF24" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#FBBF24" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="core" cx="40%" cy="35%" r="70%">
      <stop offset="0%" stop-color="#FEF3C7"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </radialGradient>
    <polygon id="arw" points="-9,-8 12,0 -9,8"/>
  </defs>

  <rect width="400" height="400" fill="#0B1220"/>
  <circle cx="200" cy="200" r="190" fill="url(#glow)"/>
  <circle cx="200" cy="200" r="186" fill="none" stroke="#1E293B" stroke-width="4"/>

  <g fill="none" stroke-linejoin="round">
    <rect x="50" y="50" width="300" height="300" rx="36" stroke="#38BDF8" stroke-width="11"/>
    <rect x="84" y="84" width="232" height="232" rx="28" stroke="#22D3EE" stroke-width="10" transform="rotate(20 200 200)"/>
    <rect x="111" y="111" width="178" height="178" rx="21" stroke="#2DD4BF" stroke-width="9" transform="rotate(40 200 200)"/>
    <rect x="131.5" y="131.5" width="137" height="137" rx="16" stroke="#A3E635" stroke-width="8" transform="rotate(60 200 200)"/>
    <rect x="147.5" y="147.5" width="105" height="105" rx="12" stroke="#FACC15" stroke-width="7" transform="rotate(80 200 200)"/>
  </g>

  <g>
    <use href="#arw" fill="#38BDF8" transform="rotate(0 200 200) translate(200 50) scale(1.05)"/>
    <use href="#arw" fill="#22D3EE" transform="rotate(20 200 200) translate(200 84) scale(0.92)"/>
    <use href="#arw" fill="#2DD4BF" transform="rotate(40 200 200) translate(200 111) scale(0.8)"/>
    <use href="#arw" fill="#A3E635" transform="rotate(60 200 200) translate(200 131.5) scale(0.7)"/>
    <use href="#arw" fill="#FACC15" transform="rotate(80 200 200) translate(200 147.5) scale(0.6)"/>
  </g>

  <circle cx="200" cy="200" r="26" fill="none" stroke="#F97316" stroke-width="5"/>
  <circle cx="200" cy="200" r="11" fill="url(#core)"/>
</svg>