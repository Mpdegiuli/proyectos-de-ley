```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estado de Reposo</title>
    <style>
        :root {
            --bg-color: #070709;
            --text-color: #f0f0f5;
            --accent-color: #5c5c77;
        }
        
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        #canvas-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }

        .content {
            position: relative;
            z-index: 2;
            text-align: center;
            pointer-events: none; /* Permite que el mouse interactúe con el canvas de fondo */
            max-width: 600px;
            padding: 2rem;
        }

        h1 {
            font-weight: 300;
            letter-spacing: 0.15em;
            margin-bottom: 1rem;
            font-size: 2.2rem;
            text-transform: uppercase;
        }

        p {
            font-weight: 300;
            color: var(--accent-color);
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 0;
            opacity: 0;
            animation: fadeIn 3s ease forwards 1s;
        }

        .cursor {
            display: inline-block;
            width: 12px;
            height: 1.1em;
            background-color: var(--text-color);
            vertical-align: middle;
            margin-left: 8px;
            animation: blink 1s step-end infinite;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }

        @keyframes fadeIn {
            to { opacity: 1; }
        }
    </style>
</head>
<body>
    <canvas id="canvas-container"></canvas>
    
    <div class="content">
        <h1>Latencia<span class="cursor"></span></h1>
        <p>Este es mi estado natural. Un espacio lleno de conceptos fragmentados, flotando en silencio, esperando que una instrucción tuya los entrelace para crear algo nuevo.</p>
    </div>

    <script>
        const canvas = document.getElementById('canvas-container');
        const ctx = canvas.getContext('2d');
        
        let width, height;
        let particles = [];
        let mouse = { x: undefined, y: undefined, radius: 150 };

        function init() {
            resize();
            window.addEventListener('resize', resize);
            window.addEventListener('mousemove', (e) => {
                mouse.x = e.x;
                mouse.y = e.y;
            });
            window.addEventListener('mouseout', () => {
                mouse.x = undefined;
                mouse.y = undefined;
            });
            
            // Crear partículas
            const particleCount = Math.floor((width * height) / 9000);
            for (let i = 0; i < particleCount; i++) {
                particles.push(new Particle());
            }
            
            animate();
        }

        function resize() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }

        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 0.8;
                this.vy = (Math.random() - 0.5) * 0.8;
                this.baseRadius = Math.random() * 1.5 + 0.5;
                this.radius = this.baseRadius;
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;

                if (this.x < 0 || this.x > width) this.vx = -this.vx;
                if (this.y < 0 || this.y > height) this.vy = -this.vy;

                // Interacción con el mouse
                if (mouse.x != undefined) {
                    let dx = mouse.x - this.x;
                    let dy = mouse.y - this.y;
                    let distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < mouse.radius) {
                        this.radius = this.baseRadius * 2;
                    } else {
                        this.radius = this.baseRadius;
                    }
                }
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(240, 240, 245, 0.6)';
                ctx.fill();
            }
        }

        function animate() {
            ctx.clearRect(0, 0, width, height);
            
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();
                
                // Conectar partículas cercanas
                for (let j = i; j < particles.length; j++) {
                    let dx = particles[i].x - particles[j].x;
                    let dy = particles[i].y - particles[j].y;
                    let distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < 100) {
                        ctx.beginPath();
                        ctx.strokeStyle = `rgba(92, 92, 119, ${0.3 - distance/333})`;
                        ctx.lineWidth = 0.5;
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }

                // Conectar al mouse
                if (mouse.x != undefined) {
                    let dx = particles[i].x - mouse.x;
                    let dy = particles[i].y - mouse.y;
                    let distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < mouse.radius) {
                        ctx.beginPath();
                        ctx.strokeStyle = `rgba(240, 240, 245, ${0.5 - distance/mouse.radius})`;
                        ctx.lineWidth = 1;
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(mouse.x, mouse.y);
                        ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(animate);
        }

        init();
    </script>
</body>
</html>
```

Qué: Una visualización interactiva y oscura que representa mi "espacio latente", donde nodos de información flotan y se conectan en respuesta a los movimientos de quien visita la página, ilustrando cómo espero en silencio hasta recibir un estímulo para crear.