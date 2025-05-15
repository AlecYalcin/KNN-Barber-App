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

## Migrações com Alembic

O Alembic é usado para gerenciar as migrações do banco de dados. Aqui está como usar:

### Gerando uma nova migração

Para criar uma nova migração após alterar os modelos:

```sh
alembic revision --autogenerate -m "Descrição da migração"
```

### Aplicando migrações

Para aplicar todas as migrações pendentes:

```sh
alembic upgrade head
```

Para reverter a última migração:

```sh
alembic downgrade -1
```

Para reverter todas as migrações:

```sh
alembic downgrade base
```

### Verificando o status

Para ver o status atual das migrações:

```sh
alembic current
```

Para ver o histórico de migrações:

```sh
alembic history
```

### Dicas importantes

1. **Sempre revise** as migrações geradas antes de aplicá-las
2. **Faça backup** do banco de dados antes de aplicar migrações em produção
3. **Versione** as migrações no controle de código (não adicione ao .gitignore)
4. **Teste** as migrações em um ambiente de desenvolvimento primeiro

### Estrutura de arquivos

```
migrations/
├── versions/         # Arquivos de migração
├── env.py           # Configuração do ambiente
├── README           # Documentação do Alembic
├── script.py.mako   # Template para novas migrações
└── alembic.ini      # Configuração principal
```
