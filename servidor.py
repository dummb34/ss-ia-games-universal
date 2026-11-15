from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    return "SS IA GAMES UNIVERSAL está funcionando na internet!"

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=porta)
