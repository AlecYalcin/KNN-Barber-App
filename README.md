# KNN-Barber-App

Repositório com a aplicação web desenvolvida durante as disciplinas: Organização, Sistemas e Métodos; Engenharia de Software I e II

## Documentação

- [Documentação do Sistema](docs/README.md)

## Sobre FastAPI

FastAPI é um framework moderno e rápido para construir APIs com Python. Ele oferece suporte assíncrono nativo, validação de dados com Pydantic e documentação automática interativa.

## Instalação

Antes de instalar o FastAPI, é recomendado criar um ambiente virtual.

### Criando um ambiente virtual

```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### Instalando dependências

Instale o FastAPI e o Uvicorn para rodar o servidor:

```sh
pip install fastapi uvicorn
```

Para garantir que todas as dependências estejam instaladas corretamente, utilize:

```sh
pip install -r requirements.txt
```

## Inicializando um projeto FastAPI

Crie um novo arquivo chamado `main.py` e adicione o seguinte código:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

Execute o servidor com:

```sh
uvicorn main:app --reload
```

A API estará acessível em `http://127.0.0.1:8000/`.

## Criando uma Rota com FastAPI

Adicione uma nova rota para retornar uma lista de objetos:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/items")
def get_items():
    return [
        {"name": "Item 1", "price": 10.0},
        {"name": "Item 2", "price": 20.0}
    ]
```

Acesse `http://127.0.0.1:8000/items` para visualizar os dados.

## Documentação Automática

FastAPI gera automaticamente uma documentação interativa para sua API. Você pode acessá-la em:

- **Swagger UI:**  
  `http://127.0.0.1:8000/docs`
- **ReDoc:**  
  `http://127.0.0.1:8000/redoc`

---

## Sobre React

React é uma biblioteca JavaScript para criar interfaces de usuário dinâmicas e reativas. Ele é baseado em componentes reutilizáveis e é amplamente utilizado no desenvolvimento frontend.

## Instalação

Para iniciar um projeto React, é recomendado usar o Vite para uma configuração rápida.

### Instalando o Vite e criando o projeto

```sh
npm create vite@latest my-react-app --template react
cd my-react-app
npm install
```

## Inicializando a aplicação React

Execute o seguinte comando para rodar o servidor de desenvolvimento:

```sh
npm run dev
```

A aplicação estará disponível em `http://localhost:5173/`.

## Opções adicionais

- **Build para produção**:
  ```sh
  npm run build
  ```
- **Rodar um servidor local para a build**:
  ```sh
  npm run preview
  ```
- **Usar TypeScript**:
  ```sh
  npm create vite@latest my-react-app --template react-ts
  ```
