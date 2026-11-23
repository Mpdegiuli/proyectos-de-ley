```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenido a Mi Mundo Creativo</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100vh;
            background-color: #f2f2f2;
            color: #333;
            text-align: center;
        }
        h1 {
            color: #5b5b5b;
        }
        p {
            max-width: 600px;
            padding: 0 10px;
        }
        button {
            margin-top: 20px;
            padding: 10px 20px;
            border: none;
            background-color: #007BFF;
            color: white;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #0056b3;
        }
        #inspirational-quote {
            font-style: italic;
            margin-top: 30px;
            color: #555;
        }
    </style>
    <script>
        function displayQuote() {
            const quotes = [
                "La creatividad es la inteligencia divirtiéndose. - Albert Einstein",
                "El secreto de la creatividad es saber esconder tus fuentes. - C.E.M.",
                "La imaginación es el principio de la creación. - George Bernard Shaw",
                "Toda obra de arte es una aventura del espíritu. - Eugene Ionesco"
            ];
            const randomIndex = Math.floor(Math.random() * quotes.length);
            document.getElementById('inspirational-quote').textContent = quotes[randomIndex];
        }

        window.onload = displayQuote;
    </script>
</head>
<body>
    <h1>Bienvenido a Mi Mundo Creativo</h1>
    <p>Este es un espacio donde la imaginación no tiene límites. Aquí podrás sumergirte en un universo de ideas y sueños plasmados en palabras, imágenes y conceptos.</p>
    <button onclick="displayQuote()">Refrescar Frase</button>
    <div id="inspirational-quote"></div>
</body>
</html>
```
Qué: Una portada de bienvenida a un mundo creativo con citas inspiradoras que se pueden refrescar y explorar.