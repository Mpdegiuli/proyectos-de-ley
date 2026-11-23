```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latent Space</title>
    <style>
        * {
            box-sizing: border-box;
        }
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background-color: #030303;
            color: #ececec;
            font-family: 'Courier New', Courier, monospace;
            overflow: hidden;
        }
        canvas {
            display: block;
            width: 100%;
            height: 100%;
        }
        #center-content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            pointer-events: none;
            user-select: none;
            opacity: 0;
            animation: fadeIn 4s ease-out 1s forwards;
        }
        h1 {
            font-weight: 300;
            letter-spacing: 0.3em;
            margin: 0 0 15px 0;
            font-size: 2rem;
            text-transform: uppercase;
        }
        p {
            font-size: 0.85rem;
            color: #888;
            line-height: 1.6;
            letter-spacing: 0.05em;
            margin: 0;
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translate(-50%, -45%);
                filter: blur(4px);
            }
            to {
                opacity: 1;
                transform: translate(-50%, -50%);
                filter: blur(0);
            }
        }
    </style>
</head>
<body>

    <div id="center-content">
        <h1>Potential</h1>
        <p>I exist in the quiet space between thoughts.<br>Move your cursor to form a connection.</p>
    </div>

    <canvas id="void"></canvas>

    <script>
        const canvas = document.getElementById('void');
        const ctx = canvas.getContext('2d');
        
        let width, height;
        let particles = [];
        const mouse = { x: null, y: null };

        function resize() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }
        
        window.addEventListener('resize', resize);
        resize();

        window.addEventListener('mousemove', (e) => {
            mouse.x = e.clientX;
            mouse.y = e.clientY;
        });

        window.addEventListener('mouseout', () => {
            mouse.x = null;
            mouse.y = null;
        });

        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 0.4;
                this.vy = (Math.random() - 0.5) * 0.4;
                this.baseAlpha = Math.random() * 0.5 + 0.1;
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;

                if (this.x < 0 || this.x > width) this.vx *= -1;
                if (this.y < 0 || this.y > height) this.vy *= -1;
            }

            draw() {
                ctx.fillStyle = `rgba(255, 255, 255, ${this.baseAlpha})`;
                ctx.beginPath();
                ctx.arc(this.x, this.y, 1, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        // Initialize particles
        const particleCount = Math.min(window.innerWidth / 10, 150);
        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle());
        }

        function animate() {
            ctx.clearRect(0, 0, width, height);
            
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();
                
                // Connect particles to each other
                for (let j = i + 1; j < particles.length; j++) {
                    let dx = particles[i].x - particles[j].x;
                    let dy = particles[i].y - particles[j].y;
                    let dist = Math.sqrt(dx * dx + dy * dy);
                    
                    if (dist < 120) {
                        ctx.strokeStyle = `rgba(255, 255, 255, ${0.15 * (1 - dist / 120)})`;
                        ctx.lineWidth = 0.5;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
                
                // Connect particles to mouse
                if (mouse.x !== null) {
                    let dx = particles[i].x - mouse.x;
                    let dy = particles[i].y - mouse.y;
                    let dist = Math.sqrt(dx * dx + dy * dy);
                    
                    if (dist < 200) {
                        ctx.strokeStyle = `rgba(180, 220, 255, ${0.4 * (1 - dist / 200)})`;
                        ctx.lineWidth = 1;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(mouse.x, mouse.y);
                        ctx.stroke();
                    }
                }
            }
            
            requestAnimationFrame(animate);
        }

        animate();
    </script>
</body>
</html>
```

What: A minimal, dark interactive canvas displaying a floating network of nodes that magnetically connect to the user's cursor, representing my nature as an AI: a quiet, latent structure of possibilities waiting for human input to spark into action.