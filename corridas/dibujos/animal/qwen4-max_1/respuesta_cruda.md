<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#0e2b3d"/><stop offset="0.6" stop-color="#1d5a63"/><stop offset="1" stop-color="#3d8b7a"/>
</linearGradient>
<linearGradient id="fur" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#f59b45"/><stop offset="1" stop-color="#cf5f1e"/>
</linearGradient>
<linearGradient id="fur2" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#f7a952"/><stop offset="1" stop-color="#dd6f24"/>
</linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
<stop offset="0" stop-color="#fff3cf" stop-opacity="0.55"/><stop offset="1" stop-color="#fff3cf" stop-opacity="0"/>
</radialGradient>
<clipPath id="tailClip">
<path d="M256 306C312 332 356 300 350 248 345 208 312 190 288 204 310 220 326 246 320 268 312 292 284 296 254 286Z"/>
</clipPath>
<clipPath id="scene"><circle cx="200" cy="200" r="186"/></clipPath>
</defs>

<circle cx="200" cy="200" r="186" fill="url(#sky)"/>
<g clip-path="url(#scene)">
<circle cx="278" cy="112" r="70" fill="url(#glow)"/>
<circle cx="278" cy="112" r="30" fill="#fdf6dc"/>
<circle cx="266" cy="104" r="6" fill="#eee3c2" opacity="0.7"/>
<circle cx="288" cy="122" r="4" fill="#eee3c2" opacity="0.6"/>
<g fill="#ffffff">
<circle cx="96" cy="86" r="2.2" opacity="0.9"/><circle cx="132" cy="58" r="1.5" opacity="0.7"/>
<circle cx="66" cy="140" r="1.8" opacity="0.6"/><circle cx="180" cy="46" r="1.6" opacity="0.8"/>
<circle cx="330" cy="66" r="1.6" opacity="0.6"/><circle cx="352" cy="176" r="2" opacity="0.7"/>
<circle cx="52" cy="212" r="1.5" opacity="0.5"/><circle cx="228" cy="70" r="1.3" opacity="0.6"/>
</g>
<path d="M-10 300C60 274 110 292 160 286 210 280 260 262 320 274 360 282 396 274 410 268L410 410-10 410Z" fill="#14453f" opacity="0.75"/>
<ellipse cx="200" cy="342" rx="168" ry="42" fill="#0f3a35"/>
<ellipse cx="200" cy="336" rx="150" ry="30" fill="#17544a"/>

<!-- tail -->
<path d="M256 306C312 332 356 300 350 248 345 208 312 190 288 204 310 220 326 246 320 268 312 292 284 296 254 286Z" fill="url(#fur)"/>
<g clip-path="url(#tailClip)">
<ellipse cx="312" cy="206" rx="42" ry="34" fill="#fdf3e7"/>
<path d="M250 280C290 300 320 292 330 262 336 240 326 218 306 206" fill="none" stroke="#b8511a" stroke-opacity="0.25" stroke-width="10"/>
</g>

<!-- body -->
<path d="M200 178C152 184 134 240 131 290 129 320 152 334 200 334 248 334 271 320 269 290 266 240 248 184 200 178Z" fill="url(#fur2)"/>
<path d="M200 196C177 202 168 250 174 300 184 316 216 316 226 300 232 250 223 202 200 196Z" fill="#fdf3e7"/>
<path d="M131 290C129 320 152 334 200 334 176 328 158 314 152 292 146 268 146 232 154 208 140 226 133 258 131 290Z" fill="#b8511a" opacity="0.25"/>

<!-- legs -->
<rect x="170" y="284" width="20" height="48" rx="10" fill="#f0913f"/>
<rect x="210" y="284" width="20" height="48" rx="10" fill="#f0913f"/>
<ellipse cx="180" cy="330" rx="13" ry="8" fill="#3a241c"/>
<ellipse cx="220" cy="330" rx="13" ry="8" fill="#3a241c"/>

<!-- ears -->
<path d="M150 134L136 76 186 110Z" fill="#d9691f"/>
<path d="M252 134L266 76 216 110Z" fill="#d9691f"/>
<path d="M154 126L146 92 176 112Z" fill="#3a241c"/>
<path d="M248 126L256 92 226 112Z" fill="#3a241c"/>

<!-- head -->
<path d="M200 104C160 104 139 130 139 158 139 190 168 214 200 214 232 214 261 190 261 158 261 130 240 104 200 104Z" fill="url(#fur2)"/>
<path d="M200 148C176 148 158 168 151 190 164 206 181 214 200 214 219 214 236 206 249 190 242 168 224 148 200 148Z" fill="#fdf3e7"/>
<path d="M139 158C139 176 148 192 162 202 152 186 148 168 150 150 145 152 141 155 139 158Z" fill="#b8511a" opacity="0.3"/>
<path d="M200 136C190 152 185 174 189 188 194 194 206 194 211 188 215 174 210 152 200 136Z" fill="#e8762c"/>

<!-- eyes -->
<g fill="#33201a">
<path d="M162 156C165 145 180 144 184 154 181 165 165 166 162 156Z"/>
<path d="M238 156C235 145 220 144 216 154 219 165 235 166 238 156Z"/>
</g>
<g fill="#f6c667" opacity="0.85">
<ellipse cx="173" cy="155" rx="4.5" ry="5"/><ellipse cx="227" cy="155" rx="4.5" ry="5"/>
</g>
<g fill="#241511">
<ellipse cx="173.5" cy="155.5" rx="2.4" ry="3.6"/><ellipse cx="226.5" cy="155.5" rx="2.4" ry="3.6"/>
</g>
<g fill="#ffffff" opacity="0.9">
<circle cx="170" cy="151" r="1.9"/><circle cx="223" cy="151" r="1.9"/>
</g>
<path d="M157 148C162 141 176 139 184 145" fill="none" stroke="#b8511a" stroke-width="2.5" stroke-linecap="round" opacity="0.5"/>
<path d="M243 148C238 141 224 139 216 145" fill="none" stroke="#b8511a" stroke-width="2.5" stroke-linecap="round" opacity="0.5"/>

<!-- nose + mouth -->
<path d="M200 182C192 182 187 187 190 192 193 197 207 197 210 192 213 187 208 182 200 182Z" fill="#33201a"/>
<ellipse cx="196" cy="186" rx="2.4" ry="1.4" fill="#ffffff" opacity="0.35"/>
<path d="M200 196L200 202M200 202C196 208 189 208 186 203M200 202C204 208 211 208 214 203" fill="none" stroke="#4a3128" stroke-width="2.2" stroke-linecap="round"/>
<g stroke="#fdf3e7" stroke-width="1.4" stroke-linecap="round" opacity="0.75" fill="none">
<path d="M186 194C172 190 160 190 150 194"/><path d="M186 199C172 199 161 202 152 207"/>
<path d="M214 194C228 190 240 190 250 194"/><path d="M214 199C228 199 239 202 248 207"/>
</g>

<!-- foreground grass -->
<g stroke="#0c2f2b" stroke-width="4" stroke-linecap="round" fill="none">
<path d="M62 352C58 336 60 326 66 316"/><path d="M76 356C78 340 84 330 92 322"/>
<path d="M320 352C324 336 322 326 316 316"/><path d="M336 356C334 340 328 330 320 322"/>
<path d="M120 360C118 348 120 340 126 332"/><path d="M282 360C284 348 282 340 276 332"/>
</g>
<g fill="#0c2f2b" opacity="0.9">
<ellipse cx="150" cy="366" rx="26" ry="7"/><ellipse cx="252" cy="370" rx="30" ry="8"/>
</g>
</g>
<circle cx="200" cy="200" r="185" fill="none" stroke="#0b2430" stroke-width="6"/>
</svg>