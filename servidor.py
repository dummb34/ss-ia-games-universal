from flask import Flask, request, jsonify
from openai import OpenAI
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def inicio():
    return "SS IA GAMES UNIVERSAL está online!"

@app.route("/perguntar", methods=["POST"])
def perguntar():
    dados = request.get_json()
    pergunta = dados.get("pergunta", "")

    if not pergunta:
        return jsonify({"erro": "Digite uma pergunta"}), 400

    try:
        cliente = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
        )

        resposta = cliente.responses.create(
            model="gpt-4.1-mini",
            instructions=(
                "Você é a SS IA GAMES UNIVERSAL, "
                "uma inteligência artificial especializada "
                "em jogos, computadores e programação. "
                "Responda em português de forma clara."
            ),
            input=pergunta
        )

        return jsonify({"resposta": resposta.output_text})

    except Exception as erro:
        return jsonify({"erro": "Não foi possível responder agora."}), 500

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=porta)
