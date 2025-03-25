from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
OLLAMA_API = "http://localhost:11434/api/generate"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    data = {
        "model": "deepseek-coder:6.7b",
        "prompt": user_message,
        "stream": False  # Para respostas completas de uma vez
    }
    response = requests.post(OLLAMA_API, json=data)
    return jsonify({"response": response.json()['response']})

if __name__ == '__main__':
    app.run(port=5000, debug=True)