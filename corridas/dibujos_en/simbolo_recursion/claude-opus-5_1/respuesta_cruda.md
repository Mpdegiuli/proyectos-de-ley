<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <rect width="400" height="400" fill="#f6f3ea"/>

  <!-- self-referencing loop arrow -->
  <g fill="none" stroke="#c2452d" stroke-width="9" stroke-linecap="round">
    <path d="M152,52 C138,2 262,2 248,44"/>
  </g>
  <polygon points="236,34 262,36 246,58" fill="#c2452d"/>

  <!-- nested self-similar frames (Droste / recursion) -->
  <g stroke="#1b2a41" fill="none" stroke-width="10" stroke-linejoin="round">
    <rect x="50" y="50" width="300" height="300" rx="20"/>
    <g transform="translate(200,200) rotate(16) scale(0.66) translate(-200,-200)">
      <rect x="50" y="50" width="300" height="300" rx="20"/>
      <g transform="translate(200,200) rotate(16) scale(0.66) translate(-200,-200)">
        <rect x="50" y="50" width="300" height="300" rx="20"/>
        <g transform="translate(200,200) rotate(16) scale(0.66) translate(-200,-200)">
          <rect x="50" y="50" width="300" height="300" rx="20"/>
          <g transform="translate(200,200) rotate(16) scale(0.66) translate(-200,-200)">
            <rect x="50" y="50" width="300" height="300" rx="20"/>
            <g transform="translate(200,200) rotate(16) scale(0.66) translate(-200,-200)">
              <rect x="50" y="50" width="300" height="300" rx="20"/>
              <g transform="translate(200,200) rotate(16) scale(0.66) translate(-200,-200)">
                <rect x="50" y="50" width="300" height="300" rx="20"/>
                <circle cx="200" cy="200" r="70" fill="#c2452d" stroke="none"/>
              </g>
            </g>
          </g>
        </g>
      </g>
    </g>
  </g>
</svg>