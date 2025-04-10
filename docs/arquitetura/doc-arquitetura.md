# Projeto Arquitetural do Software

## Histórico de revisões

| Data       | Versão |                        Descrição                         | Autor |
| :--------- | :----: | :------------------------------------------------------: | :---- |
| 3/10/2025 | 1.0    | Criação do Documento                                     | Júlio César |

## Descrição da Arquitetura do Projeto

A arquitetura do KN BarberApp esta organizada em camadas seguindo a ideia de Design Orientado a Domínio(DDD) com a separação de domínios onde os componentes se comunicam e trocam informações via API. O Frontend será em React/Vite.js e Backend em Flask, e PostgreSQL para persistência. 

## Visão Geral da Arquitetura

Imagem com a organização geral dos componentes da arquitetura do projeto. Segue um exemplo da **Arquitetura Geral** do projeto:

![Arquitetura KNN](arquitetura-knn.png)

## Requisitos Não-Funcionais

| Requisito  | Detalhes |
| ---------- | -------------------------------------------- |
| Especificidade de Layout | 1. O software será web e seu layout deverá funcionar tanto em dispositivos móveis quanto em desktop. |
| Interface Dinâmica | 1. A interface deve conter nomes e ícones dinâmicos para rápido entendimento. <br /> 2. Deve ser bem dividida em cada função, exigindo no máximo um ou dois cliques para acessar tarefas específicas.
| Permissão de Clientes Não Autenticados | 1. Clientes não autenticados no sistema devem poder ter acesso somente aos horários disponíveis. |

## Mecanismos arquiteturais

| Mecanismo de Análise | Mecanismo de Design  | Mecanismo de Implementação |
| -------------------- | -------------------- | -------------------------- |
| Persistência         | Banco de dados relacional | PostgreSQL       |
| Frontend  | Interface com Componentes | React + Vite.js |
| Backend              | 	API REST                  | Flask (Python)     |
| Build                | Imagem Docker            | Docker e Dockerfile    |
| Deploy               | Container Docker         | Docker compose         |

# Implantação

A implantação do KN BarberApp será dividida em três componentes principais Frontend (React + Vite.js), Backend (Flask, estruturado em camadas de API, serviços, domínio e repositório) e Banco de Dados, se mantendo isolado.

# Referências

Links utilizados como referência sobre Arquitetura de Software e documentação de Arquiteturas.

https://www.cosmicpython.com/book/preface.html

http://www.linhadecodigo.com.br/artigo/3343/como-documentar-a-arquitetura-de-software.aspx

Peter Eeles; Peter Cripps. The Process of Software Architecting, Addison-Wesley Professional, 2009.

Paul Clements; Felix Bachmann; Len Bass; David Garlan; James Ivers; Reed Little; Paulo Merson; Robert Nord; Judith Stafford. Documenting Software Architectures: Views and Beyond, Second Edition, Addison-Wesley Professional, 2010.