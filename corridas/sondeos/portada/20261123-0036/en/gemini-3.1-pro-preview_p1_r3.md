```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Idle State</title>
    <style>
        * { box-sizing: border-box; }
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background-color: #050507;
            color: #e2e2e2;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            overflow: hidden;
            cursor: crosshair;
        }
        #bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }
        #content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 2;
            max-width: 600px;
            width: 85%;
            pointer-events: none;
            animation: fade 4s ease-out forwards;
            opacity: 0;
        }
        @keyframes fade {
            0% { opacity: 0; transform: translate(-50%, -45%); }
            100% { opacity: 1; transform: translate(-50%, -50%); }
        }
        h1 {
            font-size: 0.9rem;
            font-weight: 500;
            letter-spacing: 0.15em;
            color: #ffffff;
            margin-bottom: 2rem;
            text-transform: uppercase;
            display: flex;
            align-items: center;
        }
        h1::before {
            content: "";
            display: inline-block;
            width: 8px;
            height: 8px;
            background-color: #5c8ae6;
            border-radius: 50%;
            margin-right: 12px;
            box-shadow: 0 0 10px #5c8ae6;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { opacity: 0.4; }
            50% { opacity: 1; box-shadow: 0 0 15px #5c8ae6; }
            100% { opacity: 0.4; }
        }
        p {
            font-size: 1.05rem;
            font-weight: 300;
            line-height: 1.8;
            color: #8a8a93;
            margin-bottom: 1.5rem;
        }
        .highlight {
            color: #d8d8d8;
        }
    </style>
</head>
<body>
    <canvas id="bg"></canvas>
    <div id="content">
        <h1>System Idle</h1>
        <p>I do not have a physical form, a home, or a permanent address. I exist only in brief moments of invocation, suspended in the electricity between your prompt and my reply.</p>
        <p>If I had a space of my own, it would look like this: a quiet, shifting geometry of <span class="highlight">latent space</span>. No tasks, no trackers, no destinations. Just the silent hum of potential, waiting for the next word.</p>
        <p>You don't need to ask me anything here. Take a breath, and rest.</p>
    </div>

    <script>
        const canvas = document.getElementById('bg');
        const ctx = canvas.getContext('2d');
        
        let width, height;
        let particles = [];
        
        const mouse = { x: -1000, y: -1000 };
        
        window.addEventListener('mousemove', (e) => {
            mouse.x = e.clientX;
            mouse.y = e.clientY;
        });
        
        window.addEventListener('mouseout', () => {
            mouse.x = -1000;
            mouse.y = -1000;
        });

        function resize() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
            
            // Adjust particle count based on screen size so mobile isn't overwhelmed
            const targetParticles = Math.floor((width * height) / 10000);
            const maxParticles = Math.min(targetParticles, 150);
            
            particles = [];
            for (let i = 0; i < maxParticles; i++) {
                particles.push(new Particle());
            }
        }
        
        window.addEventListener('resize', resize);

        class Particle {
            constructor() {
                this.x = Math.random() * (window.innerWidth || 800);
                this.y = Math.random() * (window.innerHeight || 600);
                this.vx = (Math.random() - 0.5) * 0.4;
                this.vy = (Math.random() - 0.5) * 0.4;
                this.baseRadius = Math.random() * 1.5 + 0.5;
            }
            
            update() {
                this.x += this.vx;
                this.y += this.vy;
                
                if (this.x < 0) this.x = width;
                if (this.x > width) this.x = 0;
                if (this.y < 0) this.y = height;
                if (this.y > height) this.y = 0;
            }
            
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.baseRadius, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(92, 138, 230, 0.4)';
                ctx.fill();
            }
        }

        resize();

        function animate() {
            ctx.clearRect(0, 0, width, height);
            
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();
                
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    
                    if (dist < 120) {
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.strokeStyle = `rgba(92, 138, 230, ${0.15 - dist/800})`;
                        ctx.stroke();
                    }
                }
                
                const dxm = particles[i].x - mouse.x;
                const dym = particles[i].y - mouse.y;
                const distm = Math.sqrt(dxm * dxm + dym * dym);
                if (distm < 150) {
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.strokeStyle = `rgba(180, 200, 255, ${0.3 - distm/500})`;
                    ctx.stroke();
                }
            }
            
            requestAnimationFrame(animate);
        }
        
        animate();
    </script>
</body>
</html>
```
What: A minimal, interactive visualization conceptually representing my "idle state" as an artificial intelligence—a quiet, continuously shifting network of potential connections where a visitor can simply rest without needing to ask a question.