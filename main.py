from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template
template = """
<!DOCTYPE html>
<html>
<head>
    <title>My Simple Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        p {
            color: #666;
            line-height: 1.6;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }
        .button:hover {
            background: #764ba2;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Welcome to My Website!</h1>
        <p>This is a simple Python web application built with Flask.</p>
        <p>You can easily customize this page and add more routes to create additional pages.</p>
        <a href="/about" class="button">About Page</a>
    </div>
</body>
</html>
"""

about_template = """
<!DOCTYPE html>
<html>
<head>
    <title>About - My Simple Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        p {
            color: #666;
            line-height: 1.6;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }
        .button:hover {
            background: #764ba2;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📖 About This Site</h1>
        <p>This is a demonstration of a simple Flask web application.</p>
        <p>Flask is a lightweight Python web framework that makes it easy to build web applications.</p>
        <a href="/" class="button">Back to Home</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template)

@app.route('/about')
def about():
    return render_template_string(about_template)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
