import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Ultimate BATTLESHIPS</h1>
    <p>Bienvenue sur la version web de votre jeu.</p>
    <p>Pour y jouer en CLI, lancez :</p>
    <pre>heroku run python battlefield.py</pre>
    """

if __name__ == '__main__':
    # Heroku injecte le port dans la variable d'env PORT
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
