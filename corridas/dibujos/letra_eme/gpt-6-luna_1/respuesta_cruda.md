<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="75%">
      <stop offset="0" stop-color="#fffdf5"/>
      <stop offset="1" stop-color="#e8eee8"/>
    </radialGradient>
    <linearGradient id="lip" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#287f79"/>
      <stop offset="1" stop-color="#15545e"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f4c56a"/>
      <stop offset="1" stop-color="#d88a4d"/>
    </linearGradient>
    <filter id="shadow" x="-30%" y="-30%" width="160%" height="180%">
      <feDropShadow dx="0" dy="9" stdDeviation="9" flood-color="#163e45" flood-opacity=".16"/>
    </filter>
  </defs>

  <rect width="400" height="400" rx="38" fill="url(#bg)"/>
  <circle cx="200" cy="205" r="143" fill="none" stroke="#d3dfd7" stroke-width="2"/>
  <circle cx="200" cy="205" r="132" fill="none" stroke="#e2e9e1" stroke-width="1"/>

  <g fill="none" stroke="url(#shine)" stroke-linecap="round" stroke-width="5">
    <path d="M166 137c9-13 19-19 34-19s25 6 34 19"/>
    <path d="M176 151c6-8 14-12 24-12s18 4 24 12"/>
    <path d="M188 164c3-4 7-6 12-6s9 2 12 6"/>
  </g>
  <circle cx="200" cy="108" r="4" fill="#d88a4d"/>

  <g filter="url(#shadow)">
    <path d="M72 204c29-33 61-49 91-43 16 3 28 15 37 22 9-7 21-19 37-22 30-6 62 10 91 43-29 33-61 49-91 43-16-3-28-15-37-22-9 7-21 19-37 22-30 6-62-10-91-43z"
          fill="url(#lip)" stroke="#103f4a" stroke-width="4" stroke-linejoin="round"/>
    <path d="M82 204c32-5 57-2 79 6 16 6 28 14 39 22 11-8 23-16 39-22 22-8 47-11 79-6"
          fill="none" stroke="#f2c36c" stroke-width="5" stroke-linecap="round"/>
    <path d="M96 194c21-17 42-25 62-23 13 1 23 8 32 15" fill="none" stroke="#71b0a0" stroke-width="3" stroke-linecap="round" opacity=".8"/>
    <path d="M304 194c-21-17-42-25-62-23-13 1-23 8-32 15" fill="none" stroke="#71b0a0" stroke-width="3" stroke-linecap="round" opacity=".8"/>
    <circle cx="200" cy="204" r="5" fill="#f2c36c"/>
  </g>

  <path d="M164 274c10 8 22 12 36 12s26-4 36-12" fill="none" stroke="#9bb8ab" stroke-width="3" stroke-linecap="round"/>
  <circle cx="200" cy="298" r="3.5" fill="#d88a4d"/>
</svg>