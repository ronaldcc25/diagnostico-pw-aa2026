from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://jsonplaceholder.typicode.com/users"

@app.route("/")
def index():
    usuarios = []

    try:
        respuesta = requests.get(API_URL, timeout=10)
        respuesta.raise_for_status()
        usuarios = respuesta.json()
    except requests.RequestException:
        usuarios = []

    return render_template("index.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
