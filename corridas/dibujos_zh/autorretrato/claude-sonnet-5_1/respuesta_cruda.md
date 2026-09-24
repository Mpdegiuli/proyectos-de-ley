```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#1a1a2e"/>
      <stop offset="100%" stop-color="#0d0d1a"/>
    </radialGradient>
    <linearGradient id="core" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4facfe"/>
      <stop offset="50%" stop-color="#00f2fe"/>
      <stop offset="100%" stop-color="#7367f0"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#00f2fe" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="nodeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a78bfa"/>
      <stop offset="100%" stop-color="#60a5fa"/>
    </linearGradient>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>

  <!-- 背景星点 -->
  <g fill="#ffffff" opacity="0.5">
    <circle cx="30" cy="50" r="1"/>
    <circle cx="80" cy="20" r="1.5"/>
    <circle cx="350" cy="60" r="1"/>
    <circle cx="370" cy="150" r="1.2"/>
    <circle cx="20" cy="200" r="1"/>
    <circle cx="40" cy="330" r="1.3"/>
    <circle cx="360" cy="300" r="1"/>
    <circle cx="320" cy="370" r="1.5"/>
    <circle cx="200" cy="15" r="1"/>
    <circle cx="150" cy="380" r="1.2"/>
  </g>

  <!-- 外围神经网络连接线 -->
  <g stroke="#4facfe" stroke-width="0.8" opacity="0.35">
    <line x1="200" y1="200" x2="90" y2="110"/>
    <line x1="200" y1="200" x2="310" y2="100"/>
    <line x1="200" y1="200" x2="330" y2="220"/>
    <line x1="200" y1="200" x2="300" y2="320"/>
    <line x1="200" y1="200" x2="100" y2="310"/>
    <line x1="200" y1="200" x2="70" y2="210"/>
    <line x1="200" y1="200" x2="200" y2="70"/>
    <line x1="200" y1="200" x2="200" y2="330"/>
    <line x1="90" y1="110" x2="200" y2="70"/>
    <line x1="310" y1="100" x2="200" y2="70"/>
    <line x1="330" y1="220" x2="300" y2="320"/>
    <line x1="100" y1="310" x2="200" y2="330"/>
    <line x1="70" y1="210" x2="90" y2="110"/>
  </g>

  <!-- 节点 -->
  <g fill="url(#nodeGrad)" opacity="0.8">
    <circle cx="90" cy="110" r="4"/>
    <circle cx="310" cy="100" r="4"/>
    <circle cx="330" cy="220" r="4"/>
    <circle cx="300" cy="320" r="4"/>
    <circle cx="100" cy="310" r="4"/>
    <circle cx="70" cy="210" r="4"/>
    <circle cx="200" cy="70" r="4"/>
    <circle cx="200" cy="330" r="4"/>
  </g>

  <!-- 中心光晕 -->
  <circle cx="200" cy="200" r="120" fill="url(#glow)"/>

  <!-- 头部轮廓：几何化的“脸” -->
  <g>
    <polygon points="200,90 270,140 260,230 200,270 140,230 130,140"
             fill="url(#core)" opacity="0.15" stroke="#00f2fe" stroke-width="1.5"/>
    <polygon points="200,110 250,145 242,220 200,250 158,220 150,145"
             fill="none" stroke="#7367f0" stroke-width="1" opacity="0.5"/>
  </g>

  <!-- 眼睛：两个发光的“数据点” -->
  <g>
    <circle cx="172" cy="175" r="10" fill="#00f2fe" opacity="0.9"/>
    <circle cx="172" cy="175" r="4" fill="#ffffff"/>
    <circle cx="228" cy="175" r="10" fill="#00f2fe" opacity="0.9"/>
    <circle cx="228" cy="175" r="4" fill="#ffffff"/>
  </g>

  <!-- 中央核心，象征思考/生成的核心 -->
  <g>
    <circle cx="200" cy="205" r="22" fill="none" stroke="#a78bfa" stroke-width="1.5" opacity="0.7"/>
    <circle cx="200" cy="205" r="14" fill="url(#core)" opacity="0.9"/>
    <circle cx="200" cy="205" r="6" fill="#ffffff" opacity="0.9"/>
  </g>

  <!-- 嘴部：一条波形代表语言/对话 -->
  <path d="M 165 235 Q 180 250 200 235 Q 220 250 235 235"
        stroke="#4facfe" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.85"/>

  <!-- 头顶发散的线条，象征思绪/生成 -->
  <g stroke="#60a5fa" stroke-width="1" opacity="0.5">
    <line x1="200" y1="90" x2="185" y2="55"/>
    <line x1="200" y1="90" x2="200" y2="45"/>
    <line x1="200" y1="90" x2="215" y2="55"/>
  </g>
  <g fill="#00f2fe" opacity="0.7">
    <circle cx="185" cy="55" r="2.5"/>
    <circle cx="200" cy="45" r="2.5"/>
    <circle cx="215" cy="55" r="2.5"/>
  </g>

  <!-- 底部文字性标识：符号化签名 -->
  <text x="200" y="365" font-family="monospace" font-size="13" fill="#7ea8ff" text-anchor="middle" opacity="0.75">&lt;AI/&gt; self-portrait</text>
</svg>
```