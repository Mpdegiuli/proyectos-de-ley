<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <path id="spiral" d="M 200 200 C 300 150, 300 250, 200 200 C 100 250, 100 150, 200 200" />
    </defs>
    <g fill="none" stroke="black" stroke-width="5">
        <circle cx="200" cy="200" r="150" stroke="lightgray" fill="none" />
        <use href="#spiral" stroke="green" />
        <use href="#spiral" transform="rotate(90 200 200)" stroke="blue" />
        <use href="#spiral" transform="rotate(180 200 200)" stroke="orange" />
        <use href="#spiral" transform="rotate(270 200 200)" stroke="red" />
    </g>
    <circle cx="200" cy="200" r="10" fill="black" />
</svg>