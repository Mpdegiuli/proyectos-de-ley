<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <title>Un mundo compartido</title>
  <defs>
    <radialGradient id="sky" cx="50%" cy="42%" r="70%">
      <stop stop-color="#263d50"/>
      <stop offset="1" stop-color="#101925"/>
    </radialGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#3d8191"/>
      <stop offset=".55" stop-color="#22576c"/>
      <stop offset="1" stop-color="#173b52"/>
    </linearGradient>
    <linearGradient id="land" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#b2c991"/>
      <stop offset="1" stop-color="#588a78"/>
    </linearGradient>
    <radialGradient id="heat">
      <stop stop-color="#f4a05d" stop-opacity=".8"/>
      <stop offset="1" stop-color="#ee7254" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="globe"><circle cx="200" cy="188" r="124"/></clipPath>
  </defs>

  <rect width="400" height="400" fill="url(#sky)"/>
  <g fill="#d7e5d6">
    <circle cx="45" cy="64" r="1.3"/><circle cx="93" cy="38" r="1"/>
    <circle cx="180" cy="28" r="1.1"/><circle cx="286" cy="42" r="1.4"/>
    <circle cx="353" cy="85" r="1"/><circle cx="370" cy="175" r="1.3"/>
    <circle cx="34" cy="185" r="1"/><circle cx="54" cy="258" r="1.2"/>
    <circle cx="342" cy="260" r="1"/><circle cx="314" cy="306" r="1.4"/>
  </g>
  <g stroke="#d9e6d8" stroke-width=".8" opacity=".6">
    <path d="M59 112h8m-4-4v8M334 136h10m-5-5v10M110 302h8m-4-4v8"/>
  </g>

  <circle cx="200" cy="188" r="139" fill="none" stroke="#a5c7c2" stroke-opacity=".16"/>
  <circle cx="200" cy="188" r="131" fill="none" stroke="#a5c7c2" stroke-opacity=".22" stroke-dasharray="2 7"/>
  <circle cx="200" cy="188" r="124" fill="url(#sea)"/>

  <g clip-path="url(#globe)">
    <path d="M75 104c18-20 43-31 68-34l14 12-7 13 13 9-5 12-14 3-5 12-16 5-5 14-13 4-8-9-13 1-11-15z" fill="url(#land)"/>
    <path d="M119 157l16 3 10 11 16 5 7 15-7 15-1 15-10 16-6 22-10 15-7-9 1-20-10-18-2-18-10-13 2-17z" fill="url(#land)"/>
    <path d="M153 74l14-14 19 2 4 11-11 12-18-1z" fill="#d8e7ce"/>
    <path d="M181 111l11-11 18 2 8-12 21-4 14-10 32 5 10 11 21 4 19 19-6 18-18 2-9 10-17-1-11 13-16-3-8 9-15-8-10 3-7-13-15-2-9-11-13-3z" fill="url(#land)"/>
    <path d="M195 155l16-5 20 7 11 14 12 5-1 18-9 11-5 20-14 18-12-7-5-16-10-10-4-19-8-13z" fill="url(#land)"/>
    <path d="M278 224l15-9 21 5 9 13-6 15-20 5-17-8-7-10z" fill="url(#land)"/>
    <path d="M255 181l8 5 5 14-5 8-7-10zM272 208l5 4-2 9-4-2z" fill="#81aa88"/>
    <ellipse cx="130" cy="216" rx="89" ry="86" fill="url(#heat)"/>

    <g fill="none" stroke="#d5e8d5" stroke-linecap="round">
      <path d="M86 116c30-9 53-9 80-2M242 112c28-8 55-6 77 2" opacity=".38" stroke-width="3"/>
      <path d="M91 122c24-6 39-6 54-4M255 118c17-4 36-4 49 0" opacity=".22" stroke-width="2"/>
    </g>

    <g fill="none" stroke="#f4d5a3" stroke-width="1.2" opacity=".8">
      <path d="M123 146C160 98 223 101 277 130"/>
      <path d="M123 146C158 166 181 190 217 204"/>
      <path d="M217 204C242 166 259 150 277 130"/>
      <path d="M217 204C244 232 270 232 296 232"/>
      <path d="M123 146C110 174 119 205 140 227"/>
      <path d="M140 227C165 242 191 232 217 204"/>
      <path d="M277 130C302 157 307 193 296 232"/>
    </g>
    <g fill="#ffe2ae">
      <circle cx="123" cy="146" r="3"/><circle cx="277" cy="130" r="3"/>
      <circle cx="217" cy="204" r="3"/><circle cx="140" cy="227" r="3"/>
      <circle cx="296" cy="232" r="3"/>
    </g>
    <g fill="none" stroke="#fff0d0" stroke-opacity=".45">
      <circle cx="123" cy="146" r="7"/><circle cx="277" cy="130" r="7"/>
      <circle cx="217" cy="204" r="7"/><circle cx="140" cy="227" r="7"/>
    </g>

    <path d="M103 251c5-9 5-16 3-22 9 5 10 12 9 16 6-5 7-10 7-14 10 11 8 23-2 29z" fill="#f5b36b" opacity=".9"/>
    <path d="M110 258c0-8 4-12 7-15 1 7 6 9 5 15z" fill="#ffe0a1"/>
    <g stroke="#e4f0d9" stroke-width="2" stroke-linecap="round" opacity=".85">
      <path d="M288 196v-33m0 0-13-7m13 7 12-9m-12 9 2 15"/>
      <path d="M310 204v-26m0 0-10-5m10 5 9-7m-9 7 2 12"/>
    </g>
    <path d="M71 272c65 20 139 26 260-6v55H71z" fill="#142f40" opacity=".3"/>
  </g>

  <circle cx="200" cy="188" r="124" fill="none" stroke="#b8d3c6" stroke-opacity=".55" stroke-width="1.5"/>
  <path d="M62 174c-9 23-6 46 7 66M334 135c11 23 15 46 11 67" fill="none" stroke="#efc991" stroke-width="1.5" stroke-linecap="round"/>
  <circle cx="67" cy="240" r="3" fill="#efc991"/>
  <circle cx="334" cy="135" r="3" fill="#efc991"/>

  <path d="M0 359c48-18 88-20 130-12 37 7 65 9 102 2 57-12 110-9 168 9v42H0z" fill="#162b35"/>
  <path d="M0 376c65-16 123-17 186-7 72 12 141-6 214-3v34H0z" fill="#0e2029"/>
  <path d="M34 376c39-7 72-9 107-6M259 375c40-8 76-9 108-6" fill="none" stroke="#789c89" stroke-opacity=".35"/>

  <g fill="#e8cba8">
    <circle cx="155" cy="325" r="5"/>
    <circle cx="174" cy="320" r="5.5"/>
    <circle cx="225" cy="320" r="5.5"/>
    <circle cx="244" cy="325" r="5"/>
  </g>
  <g fill="#d7a878">
    <path d="M149 334q6-5 12 0l3 18h-18z"/>
    <path d="M167 329q7-5 14 0l4 23h-22z"/>
    <path d="M218 329q7-5 14 0l4 23h-22z"/>
    <path d="M238 334q6-5 12 0l4 18h-19z"/>
  </g>
  <g stroke="#e8cba8" stroke-width="2.5" stroke-linecap="round">
    <path d="M160 337l7 5M181 335l8 7M218 335l-8 7M239 337l-7 5"/>
  </g>

  <path d="M200 365v-27" fill="none" stroke="#a9ce9a" stroke-width="2" stroke-linecap="round"/>
  <path d="M200 348c-1-9-9-12-15-11 1 7 6 11 15 11z" fill="#8fbe8e"/>
  <path d="M200 342c2-9 9-12 15-11-1 7-6 11-15 11z" fill="#c2dba5"/>
  <path d="M191 365q9-4 18 0" fill="none" stroke="#a9ce9a" stroke-width="1.5" stroke-linecap="round"/>
</svg>