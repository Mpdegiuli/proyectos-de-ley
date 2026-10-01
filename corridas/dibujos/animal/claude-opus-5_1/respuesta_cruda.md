```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1b2a4a"/>
      <stop offset="55%" stop-color="#3d5a80"/>
      <stop offset="100%" stop-color="#98c1d9"/>
    </linearGradient>
    <radialGradient id="moon" cx="0.4" cy="0.35" r="0.7">
      <stop offset="0%" stop-color="#fffdf0"/>
      <stop offset="100%" stop-color="#f1e6b8"/>
    </radialGradient>
    <linearGradient id="fur" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f08a3c"/>
      <stop offset="60%" stop-color="#d9662a"/>
      <stop offset="100%" stop-color="#b74f22"/>
    </linearGradient>
    <linearGradient id="furHead" x1="0.2" y1="0" x2="0.8" y2="1">
      <stop offset="0%" stop-color="#f7a04e"/>
      <stop offset="100%" stop-color="#df6f2b"/>
    </linearGradient>
    <linearGradient id="tail" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#e87b32"/>
      <stop offset="70%" stop-color="#c85a24"/>
      <stop offset="100%" stop-color="#fdf6e8"/>
    </linearGradient>
    <linearGradient id="ground" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e8f1f5"/>
      <stop offset="100%" stop-color="#b9cbd6"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#fffbe0" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#fffbe0" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- fondo -->
  <rect width="400" height="400" fill="url(#sky)"/>
  <g fill="#fff">
    <circle cx="40" cy="40" r="1.6" opacity=".9"/>
    <circle cx="90" cy="70" r="1.1" opacity=".7"/>
    <circle cx="140" cy="30" r="1.4" opacity=".8"/>
    <circle cx="210" cy="55" r="1" opacity=".6"/>
    <circle cx="265" cy="25" r="1.5" opacity=".85"/>
    <circle cx="350" cy="95" r="1.2" opacity=".7"/>
    <circle cx="380" cy="45" r="1" opacity=".6"/>
    <circle cx="20" cy="110" r="1.1" opacity=".6"/>
    <circle cx="170" cy="110" r="0.9" opacity=".5"/>
    <circle cx="310" cy="140" r="0.9" opacity=".5"/>
  </g>
  <circle cx="305" cy="80" r="70" fill="url(#glow)"/>
  <circle cx="305" cy="80" r="34" fill="url(#moon)"/>
  <circle cx="318" cy="68" r="6" fill="#e6d9a8" opacity=".5"/>
  <circle cx="296" cy="92" r="4" fill="#e6d9a8" opacity=".45"/>
  <circle cx="310" cy="96" r="2.5" fill="#e6d9a8" opacity=".4"/>

  <!-- árboles lejanos -->
  <g fill="#22344f" opacity=".85">
    <path d="M30 300 L48 210 L66 300 Z"/>
    <path d="M22 300 L48 235 L74 300 Z"/>
    <path d="M70 300 L84 240 L98 300 Z"/>
    <path d="M330 300 L350 215 L370 300 Z"/>
    <path d="M322 300 L350 245 L378 300 Z"/>
  </g>

  <!-- suelo -->
  <path d="M0 300 Q100 280 200 296 Q300 312 400 292 L400 400 L0 400 Z" fill="url(#ground)"/>
  <ellipse cx="200" cy="352" rx="120" ry="16" fill="#8fa6b4" opacity=".35"/>

  <!-- ZORRO -->
  <g>
    <!-- cola -->
    <path d="M118 330 C60 322 52 262 92 234 C120 214 158 226 168 254 C176 278 162 306 138 318 Z" fill="url(#tail)"/>
    <path d="M118 330 C74 322 64 276 92 250 C74 286 84 318 122 324 Z" fill="#fdf6e8" opacity=".9"/>
    <path d="M150 240 C168 252 172 274 164 292" fill="none" stroke="#a8461c" stroke-width="2" opacity=".35"/>

    <!-- cuerpo -->
    <path d="M200 160 C248 160 268 230 266 280 C265 316 244 340 200 340 C156 340 141 316 140 280 C138 230 152 160 200 160 Z" fill="url(#fur)"/>
    <!-- pecho -->
    <path d="M200 200 C226 210 236 260 232 296 C229 322 218 336 200 336 C182 336 171 322 168 296 C164 260 174 210 200 200 Z" fill="#fdf6e8"/>

    <!-- patas delanteras -->
    <path d="M172 300 C168 322 168 334 170 344 L192 344 C194 332 192 316 190 302 Z" fill="#8a3b18"/>
    <path d="M210 302 C208 316 206 332 208 344 L230 344 C232 334 232 322 228 300 Z" fill="#8a3b18"/>
    <ellipse cx="181" cy="345" rx="13" ry="6" fill="#6f2f12"/>
    <ellipse cx="219" cy="345" rx="13" ry="6" fill="#6f2f12"/>

    <!-- cabeza -->
    <g>
      <!-- orejas -->
      <path d="M152 128 C144 96 150 74 158 68 C170 76 184 100 186 120 Z" fill="#df6f2b"/>
      <path d="M156 122 C152 100 156 84 160 80 C168 88 176 104 178 118 Z" fill="#3a2b2b"/>
      <path d="M248 128 C256 96 250 74 242 68 C230 76 216 100 214 120 Z" fill="#df6f2b"/>
      <path d="M244 122 C248 100 244 84 240 80 C232 88 224 104 222 118 Z" fill="#3a2b2b"/>

      <path d="M200 74 C244 74 264 104 264 138 C264 176 236 202 200 202 C164 202 136 176 136 138 C136 104 156 74 200 74 Z" fill="url(#furHead)"/>

      <!-- mejillas claras -->
      <path d="M143 140 C132 158 134 176 146 186 C156 176 158 158 155 142 Z" fill="#fdf6e8"/>
      <path d="M257 140 C268 158 266 176 254 186 C244 176 242 158 245 142 Z" fill="#fdf6e8"/>

      <!-- hocico -->
      <path d="M200 140 C218 140 228 158 228 174 C228 192 214 202 200 202 C186 202 172 192 172 174 C172 158 182 140 200 140 Z" fill="#fdf6e8"/>
      <ellipse cx="200" cy="184" rx="9" ry="6.5" fill="#2e2222"/>
      <path d="M200 190 L200 198" stroke="#2e2222" stroke-width="2.4" stroke-linecap="round"/>
      <path d="M200 198 C194 198 190 195 188 192" fill="none" stroke="#2e2222" stroke-width="2" stroke-linecap="round"/>
      <path d="M200 198 C206 198 210 195 212 192" fill="none" stroke="#2e2222" stroke-width="2" stroke-linecap="round"/>

      <!-- ojos -->
      <g>
        <path d="M158 136 C164 128 180 128 186 138 C180 148 164 148 158 136 Z" fill="#fff8e7"/>
        <ellipse cx="172" cy="138" rx="6.5" ry="7.5" fill="#3b2410"/>
        <circle cx="172" cy="138" r="3.4" fill="#111"/>
        <circle cx="174.5" cy="135" r="1.8" fill="#fff" opacity=".9"/>
        <path d="M156 132 C164 124 182 124 188 134" fill="none" stroke="#7a3a16" stroke-width="2.2" stroke-linecap="round"/>
      </g>
      <g>
        <path d="M214 138 C220 128 236 128 242 136 C236 148 220 148 214 138 Z" fill="#fff8e7"/>
        <ellipse cx="228" cy="138" rx="6.5" ry="7.5" fill="#3b2410"/>
        <circle cx="228" cy="138" r="3.4" fill="#111"/>
        <circle cx="230.5" cy="135" r="1.8" fill="#fff" opacity=".9"/>
        <path d="M212 134 C218 124 236 124 244 132" fill="none" stroke="#7a3a16" stroke-width="2.2" stroke-linecap="round"/>
      </g>

      <!-- bigotes -->
      <g stroke="#fff" stroke-width="1.3" opacity=".8" stroke-linecap="round">
        <path d="M174 176 L142 168"/>
        <path d="M174 182 L141 182"/>
        <path d="M226 176 L258 168"/>
        <path d="M226 182 L259 182"/>
      </g>
    </g>
  </g>

  <!-- nieve / detalles frente -->
  <g fill="#fff" opacity=".6">
    <circle cx="60" cy="370" r="2"/>
    <circle cx="120" cy="385" r="1.5"/>
    <circle cx="300" cy="366" r="2"/>
    <circle cx="350" cy="384" r="1.6"/>
    <circle cx="245" cy="378" r="1.4"/>
  </g>
</svg>
```