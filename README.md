# Chat DeepSeek 6.7B

Este repositório contém um aplicativo web simples que permite interagir com o modelo **DeepSeek 6.7B** através de uma interface de chat. O aplicativo utiliza **Flask** no backend e HTML/JavaScript no frontend para criar uma experiência de chat local.

## Hardware

![nVIDIA](https://img.shields.io/badge/nVIDIA-%2376B900.svg?style=for-the-badge&logo=nVIDIA&logoColor=white) ![nVIDIA](https://img.shields.io/badge/cuda-000000.svg?style=for-the-badge&logo=nVIDIA&logoColor=green) 

- **GPU**: NVIDIA GeForce RTX 3060 12GB with CUDA

## Tecnologias Utilizadas

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Modelo de IA**: DeepSeek 6.7B - Coder (via API local)

## Como Utilizar

Siga os passos abaixo para configurar e executar o aplicativo:

### Pré-requisitos

1. **Python 3.12** ou superior instalado.NVIDIA GeForce RTX 3060
2. **Virtualenv** para criar um ambiente virtual Python.
3. O modelo **DeepSeek 6.7B** deve estar configurado e acessível, consulte como preparar seu sistema operacional para receber uma LLM em https://github.com/92username/ia_local_install
4. **GPU NVIDIA RTX 3060** ou superior, com **CUDA**.

### Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/92username/chat_deepseek_6.7b
   cd chat_deepseek_6.7b
   ```

2. **Crie e ative o ambiente virtual**:
   ```bash
   python3 -m venv deepseek
   source deepseek/bin/activate  # Linux/Mac
   ```

3. **Ative e rode o modelo LLM**:
   Certifique-se de que o modelo **DeepSeek 6.7B - Coder** está configurado corretamente. Para iniciar o servidor do modelo, utilize o comando abaixo em um terminal separado:

   ```bash
   ollama serve
   ```

   ![Terminal](img/ollama_serve.png)

   Isso iniciará o servidor local para o modelo, permitindo que o aplicativo Flask se conecte a ele.
3.1 **Verifique se a LLM está rodando**:  
   Antes de iniciar o servidor Flask, certifique-se de que o modelo está ativo utilizando o comando abaixo:  

   ```bash
   ollama list
   ```  

   ![$ ollama list](img/ollama_list.png)

   Isso exibirá uma lista de modelos disponíveis e seus status.

3.2 **Verifique o endereço do servidor**:  
   Após confirmar que o modelo está ativo, você pode acessar o endereço do servidor nonavegador para verificar se a LLM está rodando:  

      
   http://localhost:11434/
      

   Você verá a mensagem **"Ollama is running"**, indicando que o servidor está funcionando corretamente.

   ![Ollama is Running! ](img/ollama_is_running.png)

4. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```
   
5. **Inicie o servidor Flask**:
   ```bash
   python app.py
   ```

6. **Acesse o aplicativo**:
   Abra o navegador e vá para `http://localhost:5000`.

   ![Front End](img/chat_fe.png)

## Licença

Este projeto está licenciado sob a **GNU General Public License v3.0**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
