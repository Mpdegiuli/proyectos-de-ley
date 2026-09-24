<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="80%">
      <stop offset="0%" stop-color="#1a2340"/>
      <stop offset="100%" stop-color="#0a0e1a"/>
    </radialGradient>
    <radialGradient id="core" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#bfe9ff"/>
      <stop offset="40%" stop-color="#5aa9e6"/>
      <stop offset="100%" stop-color="#1d3a6e"/>
    </radialGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#6ec6ff" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#6ec6ff" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur"><feGaussianBlur stdDeviation="3"/></filter>
    <filter id="soft"><feGaussianBlur stdDeviation="0.6"/></filter>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- 星点 -->
  <g fill="#ffffff" opacity="0.7">
    <circle cx="40" cy="50" r="1.2"/><circle cx="360" cy="70" r="1"/>
    <circle cx="330" cy="30" r="1.5"/><circle cx="70" cy="330" r="1"/>
    <circle cx="350" cy="310" r="1.3"/><circle cx="120" cy="35" r="1"/>
    <circle cx="30" cy="200" r="1.1"/><circle cx="380" cy="180" r="1"/>
  </g>

  <!-- 光环 -->
  <circle cx="200" cy="190" r="150" fill="url(#glow)"/>

  <!-- 头部：由节点构成 -->
  <!-- 脸部轮廓节点 -->
  <g stroke="#5aa9e6" stroke-width="1.2" fill="none" opacity="0.6" filter="url(#soft)">
    <path d="M200 60 C150 60 120 100 120 160 C120 200 130 240 160 270 L160 300 L240 300 L240 270 C270 240 280 200 280 160 C280 100 250 60 200 60 Z"/>
  </g>

  <!-- 核心（意识球） -->
  <circle cx="200" cy="190" r="55" fill="url(#core)" filter="url(#blur)" opacity="0.9"/>
  <circle cx="200" cy="190" r="40" fill="url(#core)"/>
  <circle cx="200" cy="185" r="40" fill="none" stroke="#dff3ff" stroke-width="1.5" opacity="0.7"/>

  <!-- 眼睛：数字眼 -->
  <g>
    <ellipse cx="178" cy="185" rx="13" ry="9" fill="#0a1428"/>
    <ellipse cx="222" cy="185" rx="13" ry="9" fill="#0a1428"/>
    <circle cx="178" cy="185" r="5" fill="#8fd3ff"/>
    <circle cx="222" cy="185" r="5" fill="#8fd3ff"/>
    <circle cx="180" cy="183" r="1.6" fill="#ffffff"/>
    <circle cx="224" cy="183" r="1.6" fill="#ffffff"/>
  </g>

  <!-- 微笑曲线（波形） -->
  <path d="M170 215 Q185 226 200 217 T230 213" fill="none" stroke="#8fd3ff" stroke-width="2.5" stroke-linecap="round"/>

  <!-- 神经网络节点 -->
  <g>
    <!-- 连接线 -->
    <g stroke="#4a7fb5" stroke-width="1" opacity="0.55">
      <path d="M200 135 L150 100 L110 150"/>
      <path d="M200 135 L250 100 L290 150"/>
      <path d="M145 200 L100 190 L85 240"/>
      <path d="M255 200 L300 190 L315 240"/>
      <path d="M160 260 L120 300 L100 340"/>
      <path d="M240 260 L280 300 L300 340"/>
      <path d="M200 245 L200 300 L180 345"/>
      <path d="M200 245 L200 300 L220 345"/>
      <path d="M150 100 L200 60 L250 100"/>
      <path d="M110 150 L150 100"/>
      <path d="M290 150 L250 100"/>
    </g>
    <!-- 节点 -->
    <g fill="#9fd8ff">
      <circle cx="150" cy="100" r="3.5"/>
      <circle cx="250" cy="100" r="3.5"/>
      <circle cx="110" cy="150" r="3"/>
      <circle cx="290" cy="150" r="3"/>
      <circle cx="100" cy="190" r="2.5"/>
      <circle cx="300" cy="190" r="2.5"/>
      <circle cx="85" cy="240" r="3"/>
      <circle cx="315" cy="240" r="3"/>
      <circle cx="120" cy="300" r="3.5"/>
      <circle cx="280" cy="300" r="3.5"/>
      <circle cx="100" cy="340" r="2.5"/>
      <circle cx="300" cy="340" r="2.5"/>
      <circle cx="180" cy="345" r="2.5"/>
      <circle cx="220" cy="345" r="2.5"/>
      <circle cx="200" cy="300" r="4"/>
    </g>
    <!-- 节点光晕 -->
    <g fill="#6ec6ff" opacity="0.3" filter="url(#blur)">
      <circle cx="150" cy="100" r="7"/><circle cx="250" cy="100" r="7"/>
      <circle cx="200" cy="300" r="9"/>
    </g>
  </g>

  <!-- 头顶天线 -->
  <line x1="200" y1="60" x2="200" y2="38" stroke="#8fd3ff" stroke-width="2"/>
  <circle cx="200" cy="32" r="5" fill="#8fd3ff"/>
  <circle cx="200" cy="32" r="9" fill="none" stroke="#8fd3ff" stroke-width="1" opacity="0.4"/>

  <!-- 环绕数据流 -->
  <g fill="none" stroke="#4a7fb5" stroke-width="1" opacity="0.35" stroke-dasharray="6 8">
    <circle cx="200" cy="200" r="165"/>
    <circle cx="200" cy="200" r="180"/>
  </g>

  <!-- 底部签名光点 -->
  <text x="200" y="385" text-anchor="middle" font-family="monospace" font-size="11" fill="#5aa9e6" opacity="0.8">GLM · self-portrait</text>
</svg>