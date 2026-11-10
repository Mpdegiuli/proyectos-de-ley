<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="ab" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#1565c0"/>
    </marker>
    <marker id="ag" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#2e7d32"/>
    </marker>
  </defs>

  <rect x="0" y="0" width="400" height="400" fill="#ffffff"/>

  <!-- Self-similar nested structure -->
  <rect x="30"  y="30"  width="340" height="340" rx="22" fill="none" stroke="#263238" stroke-width="5"/>
  <rect x="84"  y="84"  width="232" height="232" rx="16" fill="none" stroke="#37474f" stroke-width="4"/>
  <rect x="121" y="121" width="158" height="158" rx="11" fill="none" stroke="#455a64" stroke-width="3.2"/>
  <rect x="146" y="146" width="108" height="108" rx="8"  fill="none" stroke="#546e7a" stroke-width="2.6"/>
  <rect x="164" y="164" width="72"  height="72"  rx="6"  fill="none" stroke="#607d8b" stroke-width="2"/>

  <!-- Calls going inward (left side) -->
  <line x1="37"  y1="200" x2="74"  y2="200" stroke="#1565c0" stroke-width="4"   marker-end="url(#ab)"/>
  <line x1="91"  y1="200" x2="112" y2="200" stroke="#1565c0" stroke-width="3.2" marker-end="url(#ab)"/>
  <line x1="127" y1="200" x2="138" y2="200" stroke="#1565c0" stroke-width="2.6" marker-end="url(#ab)"/>
  <line x1="151" y1="200" x2="157" y2="200" stroke="#1565c0" stroke-width="2"   marker-end="url(#ab)"/>

  <!-- Returns coming back outward (right side) -->
  <line x1="243" y1="200" x2="249" y2="200" stroke="#2e7d32" stroke-width="2"   marker-end="url(#ag)"/>
  <line x1="262" y1="200" x2="273" y2="200" stroke="#2e7d32" stroke-width="2.6" marker-end="url(#ag)"/>
  <line x1="288" y1="200" x2="309" y2="200" stroke="#2e7d32" stroke-width="3.2" marker-end="url(#ag)"/>
  <line x1="326" y1="200" x2="363" y2="200" stroke="#2e7d32" stroke-width="4"   marker-end="url(#ag)"/>

  <!-- Base case at the center -->
  <circle cx="200" cy="200" r="9" fill="#c62828"/>

  <!-- Self-reference loop on the outer frame -->
  <path d="M 170 30 A 30 30 0 1 1 182 10" fill="none" stroke="#1565c0" stroke-width="4" marker-end="url(#ab)"/>
</svg>