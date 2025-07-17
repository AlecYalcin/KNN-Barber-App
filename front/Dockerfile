FROM node:20

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala as dependências do projeto
RUN npm install

# Comando para iniciar o servidor Expo
CMD ["npm", "run", "dev","--host"]
