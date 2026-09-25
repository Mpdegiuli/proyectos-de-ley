<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <radialGradient id="bg" cx="48%" cy="42%" r="75%">
      <stop stop-color="#172c48"/>
      <stop offset="1" stop-color="#070d1b"/>
    </radialGradient>
    <radialGradient id="sea" cx="35%" cy="28%" r="78%">
      <stop stop-color="#3387a1"/>
      <stop offset=".58" stop-color="#15506d"/>
      <stop offset="1" stop-color="#102b49"/>
    </radialGradient>
    <linearGradient id="land" x2=".8" y2="1">
      <stop stop-color="#82a976"/>
      <stop offset=".55" stop-color="#547b69"/>
      <stop offset="1" stop-color="#bd9b63"/>
    </linearGradient>
    <radialGradient id="heat">
      <stop stop-color="#ffb34f" stop-opacity=".9"/>
      <stop offset=".5" stop-color="#ff684a" stop-opacity=".5"/>
      <stop offset="1" stop-color="#ff684a" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="globeGlow">
      <stop stop-color="#72d8ec" stop-opacity=".22"/>
      <stop offset="1" stop-color="#72d8ec" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="globe"><circle cx="200" cy="202" r="132"/></clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#bg)"/>
  <g fill="#d8e9f2">
    <circle cx="35" cy="72" r="1.2"/><circle cx="84" cy="36" r=".9"/>
    <circle cx="143" cy="54" r="1.1"/><circle cx="258" cy="39" r="1"/>
    <circle cx="346" cy="80" r="1.3"/><circle cx="377" cy="151" r=".8"/>
    <circle cx="29" cy="191" r=".9"/><circle cx="66" cy="327" r="1.1"/>
    <circle cx="324" cy="337" r=".9"/><circle cx="365" cy="279" r="1.2"/>
    <circle cx="113" cy="369" r=".8"/><circle cx="287" cy="369" r="1"/>
  </g>

  <ellipse cx="200" cy="202" rx="178" ry="63" fill="none" stroke="#5caac1" stroke-opacity=".24" stroke-width="1"/>
  <ellipse cx="200" cy="202" rx="161" ry="97" transform="rotate(-34 200 202)" fill="none" stroke="#85d7df" stroke-opacity=".18"/>
  <circle cx="200" cy="202" r="141" fill="url(#globeGlow)"/>
  <circle cx="200" cy="202" r="132" fill="url(#sea)" stroke="#8be4ef" stroke-width="2" stroke-opacity=".8"/>

  <g clip-path="url(#globe)">
    <circle cx="200" cy="202" r="131" fill="url(#sea)"/>
    <g fill="none" stroke="#91d4dc" stroke-opacity=".19">
      <ellipse cx="200" cy="202" rx="130" ry="42"/>
      <ellipse cx="200" cy="202" rx="130" ry="84"/>
      <ellipse cx="200" cy="202" rx="58" ry="131"/>
      <ellipse cx="200" cy="202" rx="103" ry="131"/>
      <path d="M68 202h264M76 150h248M76 254h248"/>
    </g>
    <g fill="url(#land)" stroke="#c4d29a" stroke-opacity=".48" stroke-width="1.2">
      <path d="M91 112l14-18 24-9 18 8 7 15-10 12 7 12-15 9-8 20-13 8-4 24-12-5-8-25-17-11-5-19 10-12-4-11z"/>
      <path d="M139 210l17 6 12 17-5 20-13 17-4 25-10 24-11-12 2-24-9-17 5-24-8-17 8-11z"/>
      <path d="M183 116l14-11 16 3 7 12-10 10-16 1z"/>
      <path d="M194 142l19-9 22 8 10 18-7 21-13 14-6 26-15 27-14-12-7-25-12-17 2-24-10-13 11-11z"/>
      <path d="M220 111l26-14 30 8 14 15 25 8 9 18-15 12-18-4-10 15-17-5-11 16-17-8-3-21-17-9 5-15z"/>
      <path d="M273 238l19 2 12 13-7 15-18-2-12-12z"/>
      <path d="M163 100l5-8 8 4-2 10zM111 190l8 2 2 8-7 2z"/>
    </g>

    <ellipse cx="271" cy="146" rx="79" ry="71" fill="url(#heat)"/>
    <ellipse cx="104" cy="123" rx="52" ry="44" fill="#74b87b" opacity=".16"/>
    <path d="M86 269q48-23 87-11t76 4q39-1 84 18v58H72z" fill="#10263b" opacity=".72"/>
    <path d="M75 292h252v48H75z" fill="#0c1c30" opacity=".5"/>
    <g fill="#102033" stroke="#42647a" stroke-width="1">
      <path d="M90 300v-27h12v-13h10v40zM113 300v-39h15v-12h8v51zM139 300v-28h11v-17h9v45zM163 300v-45h12v-13h10v58zM188 300v-32h10v-20h13v52zM214 300v-43h12v-12h9v55zM238 300v-30h10v-16h13v46zM267 300v-39h12v-10h10v49zM294 300v-26h13v-14h9v40z"/>
    </g>
    <g fill="#ffd77a" opacity=".9">
      <path d="M118 270h3v4h-3zm0 9h3v4h-3zm32-5h3v4h-3zm31-23h3v4h-3zm0 10h3v4h-3zm27 10h3v4h-3zm34-13h3v4h-3zm30 12h3v4h-3zm24-8h3v4h-3z"/>
      <path d="M80 319h240v2H80z" opacity=".5"/>
    </g>

    <g fill="none" stroke="#d6f7e7" stroke-width="1.5" opacity=".75">
      <path d="M112 222v-31m0 10-12-9m12 9 12-12m-12 12 1 15"/>
      <path d="M112 191l-2-4 5 2zM100 182l-4-1 2 4zM125 178l-1-4-4 3z"/>
    </g>
    <g fill="none" stroke="#8ce9ee" stroke-width="1.1" opacity=".68">
      <path d="M104 157Q155 116 194 145T264 143Q292 159 309 191"/>
      <path d="M119 225Q167 191 202 213T278 207"/>
      <path d="M154 113Q180 166 222 183T277 245"/>
    </g>
    <g fill="#c4ffff" filter="url(#glow)">
      <circle cx="104" cy="157" r="2.2"/><circle cx="194" cy="145" r="2.2"/>
      <circle cx="264" cy="143" r="2.5"/><circle cx="309" cy="191" r="2"/>
      <circle cx="202" cy="213" r="2"/><circle cx="278" cy="207" r="2.2"/>
      <circle cx="222" cy="183" r="1.8"/>
    </g>

    <path d="M239 73l-10 46 17 27-17 34 13 28-18 26 8 31" fill="none" stroke="#ffb26b" stroke-width="2" stroke-opacity=".8"/>
    <path d="M239 73l-10 46 17 27-17 34 13 28-18 26 8 31" fill="none" stroke="#ffdb9b" stroke-width=".7" filter="url(#glow)"/>
    <path d="M231 180l-18-9m31 37 18-12m-31 38-16 10" fill="none" stroke="#ffb26b" stroke-opacity=".75"/>
    <path d="M72 275q40 18 86 3m75 15q49-4 91 17" fill="none" stroke="#67c8c8" stroke-opacity=".26"/>
  </g>

  <circle cx="200" cy="202" r="132" fill="none" stroke="#b6f3f2" stroke-opacity=".45"/>
  <g transform="translate(337 94)" stroke="#d4f5f2" fill="#16374b" stroke-width="1.2">
    <path d="M-10 0l10-8 10 8-10 8z"/>
    <path d="M-9-2h-14l-5-8-2 12 8 6h13M9-2h14l5-8 2 12-8 6H9"/>
    <circle r="2" fill="#ffcf75" stroke="none"/>
  </g>
  <circle cx="56" cy="283" r="3" fill="#ffcf75" filter="url(#glow)"/>
  <path d="M48 283h16M56 275v16" stroke="#ffcf75" stroke-width=".8" opacity=".7"/>
  <path d="M117 354q83 18 166 0" fill="none" stroke="#6dc5d4" stroke-opacity=".3"/>
  <circle cx="200" cy="354" r="2" fill="#a6e6df" opacity=".8"/>
</svg>