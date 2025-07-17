FROM python:3.11-slim

# Nome da pasta no container
WORKDIR /app

# Copiando requirements para instalação
COPY requirements.txt .

# Instalando os recursos no pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante dos arquivos
COPY . .

# Rodando o comando de inicialização do servidor
CMD ["uvicorn", "src.entrypoints.fastapi:app", "--host", "0.0.0.0", "--port", "8000"]