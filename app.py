from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

OLLAMA_API = "http://localhost:11434/api/generate"

# Página principal (HTML)
@app.route('/')
def home():
    return render_template('index.html')

# Chat com entrada manual
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = send_to_model(user_message)
    return jsonify({"response": response})

# Upload de arquivos e envio do conteúdo como prompt
# Tipos de arquivos que NÃO serão processados
BLOCKED_EXTENSIONS = {'.pdf', '.docx', '.xlsx', '.jpg', '.jpeg', '.png', '.zip'}

def is_blocked_file(filename):
    return os.path.splitext(filename)[1].lower() in BLOCKED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not file or file.filename == '':
        return render_template('index.html')  # Pode melhorar com uma mensagem
    if is_blocked_file(file.filename):
        return render_template('index.html', response="Este tipo de arquivo não é suportado para análise.")

    # Salvar o arquivo
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Ler conteúdo e montar prompt
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        prompt = f"""
O usuário enviou este arquivo. Analise o conteúdo e diga o que o código faz ou aponte problemas:

========
{content}
========
"""
        response = send_to_model(prompt)
        return render_template('index.html', response=response)

    except Exception as e:
        return render_template('index.html', response=f"Erro ao processar o arquivo: {str(e)}")

# Função de envio para o modelo
def send_to_model(prompt):
    data = {
        "model": "deepseek-coder:6.7b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API, json=data)
        return response.json().get('response', 'Erro: Sem resposta do modelo.')
    except Exception as e:
        return f"Erro ao conectar com o modelo: {str(e)}"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
