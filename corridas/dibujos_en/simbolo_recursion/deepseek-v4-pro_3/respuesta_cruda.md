```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="recursiveGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00C9FF" />
      <stop offset="100%" stop-color="#92FE9D" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="400" height="400" fill="#0D1117" rx="20" />

  <g fill="url(#recursiveGrad)" filter="url(#glow)">
    <!-- Depth 0 -->
    <polygon points="200,162.16 80,370 320,370" />

    <!-- Depth 1 -->
    <polygon points="200,162.16 140,266.08 260,266.08" />
    <polygon points="140,266.08 80,370 200,370" />
    <polygon points="260,266.08 200,370 320,370" />

    <!-- Depth 2 -->
    <polygon points="200,162.16 170,214.24 230,214.24" />
    <polygon points="170,214.24 140,266.08 200,266.08" />
    <polygon points="230,214.24 200,266.08 260,266.08" />
    <polygon points="140,266.08 110,318.04 170,318.04" />
    <polygon points="110,318.04 80,370 140,370" />
    <polygon points="170,318.04 140,370 200,370" />
    <polygon points="260,266.08 230,318.04 290,318.04" />
    <polygon points="230,318.04 200,370 260,370" />
    <polygon points="290,318.04 260,370 320,370" />

    <!-- Depth 3 -->
    <polygon points="200,162.16 185,188.29 215,188.29" />
    <polygon points="185,188.29 170,214.24 200,214.24" />
    <polygon points="215,188.29 200,214.24 230,214.24" />
    <polygon points="170,214.24 155,240.13 185,240.13" />
    <polygon points="155,240.13 140,266.08 170,266.08" />
    <polygon points="185,240.13 170,266.08 200,266.08" />
    <polygon points="230,214.24 215,240.13 245,240.13" />
    <polygon points="215,240.13 200,266.08 230,266.08" />
    <polygon points="245,240.13 230,266.08 260,266.08" />
    <polygon points="140,266.08 125,292.06 155,292.06" />
    <polygon points="125,292.06 110,318.04 140,318.04" />
    <polygon points="155,292.06 140,318.04 170,318.04" />
    <polygon points="110,318.04 95,344.02 125,344.02" />
    <polygon points="95,344.02 80,370 110,370" />
    <polygon points="125,344.02 110,370 140,370" />
    <polygon points="170,318.04 155,344.02 185,344.02" />
    <polygon points="155,344.02 140,370 170,370" />
    <polygon points="185,344.02 170,370 200,370" />
    <polygon points="260,266.08 245,292.06 275,292.06" />
    <polygon points="245,292.06 230,318.04 260,318.04" />
    <polygon points="275,292.06 260,318.04 290,318.04" />
    <polygon points="230,318.04 215,344.02 245,344.02" />
    <polygon points="215,344.02 200,370 230,370" />
    <polygon points="245,344.02 230,370 260,370" />
    <polygon points="290,318.04 275,344.02 305,344.02" />
    <polygon points="275,344.02 260,370 290,370" />
    <polygon points="305,344.02 290,370 320,370" />

    <!-- Depth 4 -->
    <polygon points="200,162.16 192.5,175.23 207.5,175.23" />
    <polygon points="192.5,175.23 185,188.29 200,188.29" />
    <polygon points="207.5,175.23 200,188.29 215,188.29" />
    <polygon points="185,188.29 177.5,201.27 192.5,201.27" />
    <polygon points="177.5,201.27 170,214.24 185,214.24" />
    <polygon points="192.5,201.27 185,214.24 200,214.24" />
    <polygon points="215,188.29 207.5,201.27 222.5,201.27" />
    <polygon points="207.5,201.27 200,214.24 215,214.24" />
    <polygon points="222.5,201.27 215,214.24 230,214.24" />
    <polygon points="170,