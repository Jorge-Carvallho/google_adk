# 🤖 Google ADK - My Tool Agent

Este projeto é um **agente inteligente** criado com o [Google AI Developer Kit (ADK)](https://ai.google.dev/), utilizando o modelo **Gemini**.  
Ele foi desenvolvido para estudos e experimentação de integração com LLMs, ferramentas customizadas e automação.

---

## 🚀 Funcionalidades

- Integração com o modelo **Gemini 2.0 Flash**.
- Suporte a ferramentas customizadas (`@tool`) como:
  - ⏰ Obter hora atual (`get_time`)
  - 📅 Obter dia da semana (`get_weekday`)
- Execução via **linha de comando** ou interface web (`adk web`).
- Preparado para CI/CD com **GitHub Actions**.

---

## 🛠️ Estrutura do Projeto

googleAdk/
│── my_tool_agent/ # Código do agente
│ ├── init.py
│ ├── agent.py # Configuração do agente
│ ├── tools.py # Definição das ferramentas
│ └── .env # Chaves de API (ignorado no git)
│
├── .venv/ # Ambiente virtual (ignorado no git)
├── requirements.txt # Dependências do projeto
├── .gitignore
└── .github/workflows/
└── adk.yml # Pipeline do GitHub Actions

yaml
Copy code

---

## ⚙️ Instalação e Uso

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/googleAdk.git
cd googleAdk
2. Crie o ambiente virtual e instale dependências
bash
Copy code
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
3. Configure a chave da API
Crie um arquivo .env dentro de my_tool_agent/:

env
Copy code
GOOGLE_API_KEY=your_api_key_here
⚠️ Nunca suba esse .env para o Git. Ele já está no .gitignore.

4. Rodar o agente
bash
Copy code
adk web
ou

bash
Copy code
adk run my_tool_agent --once
✅ GitHub Actions
Este projeto possui um workflow de CI/CD que:

Instala dependências

Configura chave da API via secrets

Roda o agente/testes automaticamente

Arquivo: .github/workflows/adk.yml

📚 Referências
Google AI SDK Docs

Pydantic (validação de dados do agente)

GitHub Actions

👨‍💻 Autor: Jorge Carvalho
📌 Projeto criado para aprendizado e portfólio.