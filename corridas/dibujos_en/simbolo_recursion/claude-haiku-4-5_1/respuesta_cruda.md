```svg
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="400" height="400" fill="#ffffff" stroke="#333" stroke-width="2"/>
  
  <!-- Large outer circle -->
  <circle cx="200" cy="200" r="150" fill="none" stroke="#2563eb" stroke-width="3"/>
  
  <!-- Medium circle inside -->
  <circle cx="200" cy="200" r="100" fill="none" stroke="#2563eb" stroke-width="3"/>
  
  <!-- Small circle inside -->
  <circle cx="200" cy="200" r="50" fill="none" stroke="#2563eb" stroke-width="3"/>
  
  <!-- Center point -->
  <circle cx="200" cy="200" r="6" fill="#2563eb"/>
  
  <!-- Arrow spiraling inward from large to medium circle -->
  <path d="M 350 200 Q 275 100 200 150" fill="none" stroke="#e74c3c" stroke-width="2.5" stroke-linecap="round"/>
  <polygon points="200,150 208,165 195,158" fill="#e74c3c"/>
  
  <!-- Arrow spiraling inward from medium to small circle -->
  <path d="M 300 200 Q 250 125 200 100" fill="none" stroke="#e74c3c" stroke-width="2.5" stroke-linecap="round"/>
  <polygon points="200,100 203,115 192,108" fill="#e74c3c"/>
  
  <!-- Arrow spiraling inward from small to center -->
  <path d="M 250 200 Q 225 125 200 206" fill="none" stroke="#e74c3c" stroke-width="2.5" stroke-linecap="round"/>
  <polygon points="200,206 205,191 198,201" fill="#e74c3c"/>
  
  <!-- Decorative labels showing self-reference -->
  <!-- Three small copies getting progressively smaller at different positions -->
  
  <!-- Small recursive indicator at top right -->
  <circle cx="320" cy="80" r="25" fill="none" stroke="#9333ea" stroke-width="1.5" opacity="0.6"/>
  <circle cx="320" cy="80" r="17" fill="none" stroke="#9333ea" stroke-width="1.5" opacity="0.6"/>
  <circle cx="320" cy="80" r="9" fill="none" stroke="#9333ea" stroke-width="1.5" opacity="0.6"/>
  
  <!-- Small recursive indicator at bottom left -->
  <circle cx="80" cy="320" r="25" fill="none" stroke="#9333ea" stroke-width="1.5" opacity="0.6"/>
  <circle cx="80" cy="320" r="17" fill="none" stroke="#9333ea" stroke-width="1.5" opacity="0.6"/>
  <circle cx="80" cy="320" r="9" fill="none" stroke="#9333ea" stroke-width="1.5" opacity="0.6"/>
</svg>
```