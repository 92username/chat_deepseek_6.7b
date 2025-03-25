from flask import Flask, request, jsonify, render_template 
import requests

app = Flask(__name__)
OLLAMA_API = "http://localhost:11434/api/generate"

# Rota para a página HTML (frontend)
@app.route('/')
def home():
    return render_template('index.html')  # Assume que index.html está em templates/

# Rota do chat (mantida igual)
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    data = {
        "model": "deepseek-coder:6.7b",
        "prompt": user_message,
        "stream": False
    }
    response = requests.post(OLLAMA_API, json=data)
    return jsonify({"response": response.json()['response']})

if __name__ == '__main__':
    app.run(port=5000, debug=True)