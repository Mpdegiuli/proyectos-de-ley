```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to My World</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f8ff;
            color: #333;
            text-align: center;
        }
        header {
            background-color: #007acc;
            color: white;
            padding: 20px;
        }
        h1 {
            font-size: 3em;
            margin: 0;
        }
        p {
            font-size: 1.5em;
            margin: 20px 0;
        }
        footer {
            margin-top: 50px;
            padding: 20px;
            background-color: #007acc;
            color: white;
        }
        button {
            padding: 10px 20px;
            font-size: 1em;
            color: white;
            background-color: #ff5733;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #c70039;
        }
    </style>
    <script>
        function displayMessage() {
            alert("Welcome to my creative space!");
        }
    </script>
</head>
<body>
    <header>
        <h1>My Creative Space</h1>
    </header>
    <main>
        <p>Explore the wonders of imagination and inspiration.</p>
        <button onclick="displayMessage()">Click Me</button>
    </main>
    <footer>
        <p>Created with love & passion.</p>
    </footer>
</body>
</html>
```
What: A welcoming webpage featuring a vibrant header, an inspirational message, and an interactive button.