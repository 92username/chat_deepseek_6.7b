# Chat DeepSeek 6.7B

Este repositório contém um aplicativo web simples que permite interagir com o modelo **DeepSeek 6.7B** através de uma interface de chat. O aplicativo utiliza **Flask** no backend e HTML/JavaScript no frontend para criar uma experiência de chat local.

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Bibliotecas Python**:
  - Flask
  - requests
  - Blinker
  - Certifi
  - Charset Normalizer
  - Click
  - Werkzeug
  - Jinja2
- **Modelo de IA**: DeepSeek 6.7B (via API local)

## Como Utilizar

Siga os passos abaixo para configurar e executar o aplicativo:

### Pré-requisitos

1. **Python 3.12** ou superior instalado.
2. **Virtualenv** para criar um ambiente virtual Python.
3. O modelo **DeepSeek 6.7B** deve estar configurado e acessível via a API local em `http://localhost:11434/api/generate`.

### Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd chat_deepseek_6.7b

Collecting workspace information```markdown
# Chat DeepSeek 6.7B

Este repositório contém um aplicativo web simples que permite interagir com o modelo **DeepSeek 6.7B** através de uma interface de chat. O aplicativo utiliza **Flask** no backend e HTML/JavaScript no frontend para criar uma experiência de chat local.

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Bibliotecas Python**:
  - Flask
  - requests
  - Blinker
  - Certifi
  - Charset Normalizer
  - Click
  - Werkzeug
  - Jinja2
- **Modelo de IA**: DeepSeek 6.7B (via API local)

## Como Utilizar

Siga os passos abaixo para configurar e executar o aplicativo:

### Pré-requisitos

1. **Python 3.12** ou superior instalado.
2. **Virtualenv** para criar um ambiente virtual Python.
3. O modelo **DeepSeek 6.7B** deve estar configurado e acessível via a API local em `http://localhost:11434/api/generate`.

### Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd chat_deepseek_6.7b
   ```

2. **Crie e ative o ambiente virtual**:
   ```bash
   python3 -m venv deepseek
   source deepseek/bin/activate  # Linux/Mac
   deepseek\Scripts\activate    # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o modelo DeepSeek**:
   Certifique-se de que o modelo **DeepSeek 6.7B** está rodando localmente e acessível na URL `http://localhost:11434/api/generate`.

5. **Inicie o servidor Flask**:
   ```bash
   python app.py
   ```

6. **Acesse o aplicativo**:
   Abra o navegador e vá para `http://localhost:5000`.

### Como Usar o Chat

1. Digite sua mensagem no campo de entrada.
2. Clique no botão "Enviar" ou pressione "Enter".
3. A resposta do modelo será exibida no chat.

## Licença

Este projeto está licenciado sob a **GNU General Public License v3.0**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
```