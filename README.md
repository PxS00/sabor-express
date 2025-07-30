# 🍽️ Sabor Express

Projeto desenvolvido ao longo da formação **"Aprenda a programar em Python com Orientação a Objetos"** da Alura.  
Explora desde conceitos básicos de funções até a criação de APIs com FastAPI, organizando os aprendizados em três etapas evolutivas.

---

## 📚 Sobre o Projeto

O **Sabor Express** é um sistema de gerenciamento de restaurantes e cardápios. Ao longo da formação, foram desenvolvidos três projetos com o mesmo tema, porém com abordagens diferentes:

| Curso | Conteúdo Principal | Pasta |
|-------|--------------------|-------|
| Curso 1 | Funções e listas | `curso-1-funcoes/` |
| Curso 2 | Programação Orientada a Objetos | `curso-2-poo/` |
| Curso 3 | Criação de APIs com FastAPI | `curso-3-api/` |

---

## 🚀 O que foi aprendido

- ✅ Fundamentos da linguagem Python  
- ✅ Funções e estruturas condicionais  
- ✅ Criação e uso de classes e objetos  
- ✅ Herança, métodos especiais, `super()`  
- ✅ Métodos abstratos e organização em módulos  
- ✅ Ambientes virtuais com `venv`  
- ✅ FastAPI: criação de rotas e documentação automática  
- ✅ Requisições HTTP e consumo de APIs externas  
- ✅ Estruturação e leitura de arquivos `.json`

---

## 🗂️ Estrutura de Pastas

```bash
sabor-express/
├── curso-1-funcoes/
│   └── old-app.py
├── curso-2-poo/
│   ├── app.py
│   └── models/
│       ├── menu/
│       │   ├── dish.py
│       │   ├── drink.py
│       │   └── dessert.py
│       ├── rating.py
│       └── restaurant.py
├── curso-3-api/
│   ├── api.py
│   ├── main.py
│   └── data/
│       ├── Burger King.json
│       ├── KFC.json
│       ├── McDonald's.json
│       ├── Pizza Hut.json
│       ├── Taco Bell.json
│       └── Wendy's.json
├── requirements.txt
└── .gitignore
```

---

## 🧪 Como executar

```bash
1. **Clone o repositório**

git clone https://github.com/PxS00/sabor-express
cd sabor-express

2. **Crie e ative o ambiente virtual**

python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

3. **Instale as dependências**

pip install -r requirements.txt
```

---

## ▶️ Como rodar cada projeto

📘 Curso 1 — Funções
```bash
python curso-1-funcoes/old-app.py
```
📙 Curso 2 — Orientação a Objetos
```bash
python curso-2-poo/app.py
```
📗 Curso 3 — API com FastAPI
```bash
uvicorn curso-3-api.main:app --reload
```
Acesse: http://127.0.0.1:8000/docs para visualizar a documentação interativa.

---

## 🌐 Rotas da API
- GET /api/hello — Retorna uma mensagem simples do mundo da programação.

- GET /api/restaurants/?restaurant=Pizza Hut — Retorna os itens de um restaurante específico a partir da API externa.

---

## ⚙️ Tecnologias utilizadas

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-0E7C61?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-blueviolet)](https://www.uvicorn.org/)
[![Requests](https://img.shields.io/badge/Requests-HTTP-orange)](https://docs.python-requests.org/)
[![JSON](https://img.shields.io/badge/JSON-Dados-informational)](https://www.json.org/)
[![venv](https://img.shields.io/badge/venv-Ambiente%20Virtual-9cf)](https://docs.python.org/3/library/venv.html)

<br>

- **Python 3.13** — Linguagem de programação principal
- **FastAPI** — Framework moderno para criação de APIs RESTful
- **Requests** — Biblioteca para requisições HTTP
- **Uvicorn** — Servidor ASGI para aplicações FastAPI
- **venv** — Gerenciamento de ambientes virtuais Python
- **JSON** — Estrutura para dados dos cardápios e respostas das APIs
- **Paradigma Orientado a Objetos** — Organização do código usando classes, herança e polimorfismo

---

## 👨‍💻 Autor

Desenvolvido por Lucas Rossoni Dieder  
GitHub: [@PxS00](https://github.com/PxS00)
Linkedin: [lucasrossoni](linkedin.com/in/lucasrossoni)

Projeto desenvolvido com fins educacionais através da plataforma Alura.