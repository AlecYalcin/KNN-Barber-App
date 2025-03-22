# KNN-Barber-App
Repositório com a aplicação web desenvolvida durante as disciplinas: Organização, Sistemas e Métodos; Engenharia de Software I e II 



## Sobre DRF

Django Rest Framework (DRF) é uma poderosa biblioteca para construir APIs RESTful usando Django. Ele fornece recursos como autenticação, permissões e serialização de dados. Neste projeto, utilizaremos apenas o DRF para construir a API, sem o uso do Django tradicional para renderização de templates.

## Instalação

Antes de instalar o DRF, é recomendado criar um ambiente virtual.

### Criando um ambiente virtual

```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### Instalando dependências

Instale o Django Rest Framework e outras dependências necessárias:

```sh
pip install djangorestframework
```

Para garantir que todas as dependências estejam instaladas corretamente, utilize:

```sh
pip install -r requirements.txt
```

## Inicializando um projeto DRF

Crie um novo projeto Django e um aplicativo:

```sh
django-admin startproject backend
cd backend
django-admin startapp api
```

Adicione `rest_framework` ao `INSTALLED_APPS` em `settings.py`:

```python
INSTALLED_APPS = [
    'rest_framework',
    'api',
]
```

Crie um serializer (`api/serializers.py`):

```python
from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
```

Crie uma view baseada em APIView (`api/views.py`):

```python
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelView(APIView):
    def get(self, request):
        objects = MyModel.objects.all()
        serializer = MyModelSerializer(objects, many=True)
        return Response(serializer.data)
```

Mapeie a view para uma URL (`api/urls.py`):

```python
from django.urls import path
from .views import MyModelView

urlpatterns = [
    path('mymodel/', MyModelView.as_view(), name='mymodel-list')
]
```

Adicione ao `urls.py` do projeto:

```python
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
]
```

Rode as migrações e inicie o servidor:

```sh
python manage.py migrate
python manage.py runserver
```

A API estará acessível em `http://127.0.0.1:8000/api/mymodel/`.

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

