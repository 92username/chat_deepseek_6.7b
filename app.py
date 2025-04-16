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

# Removendo a lista de extensões permitidas e modificando a função is_allowed_file
def is_allowed_file(filename):
    return not is_blocked_file(filename)

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('file')
    user_message = request.form.get('message', '')

    if not files or len(files) == 0:
        return render_template('index.html', response="Nenhum arquivo selecionado.", error=True)
    if len(files) > 5:
        return render_template('index.html', response="Limite de 5 arquivos por vez.", error=True)

    file_contents = []
    for file in files:
        if is_blocked_file(file.filename):
            return render_template('index.html', response=f"Tipo de arquivo não permitido: {file.filename}", error=True)
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            file_contents.append((file.filename, content))
        except Exception as e:
            return render_template('index.html', response=f"Erro ao processar o arquivo {file.filename}: {str(e)}", error=True)

    # Monta o prompt com todos os arquivos e a mensagem do usuário
    prompt = f"O usuário enviou os seguintes arquivos e mensagem:\n\nMensagem: {user_message}\n\n"
    for fname, content in file_contents:
        prompt += f"Arquivo: {fname}\n========\n{content}\n========\n\n"

    response = send_to_model(prompt)
    return render_template('index.html', response=response, error=False)

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
        # Mensagem detalhada para usuário técnico
        return f"Erro ao conectar ao modelo: {str(e)}. Verifique se o servidor Ollama está ativo em {OLLAMA_API}"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
