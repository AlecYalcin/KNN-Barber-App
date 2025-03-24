# Documento de User Stories

## Descrição
Este documento descreve os User Stories do projeto KNN Barber App, criado a partir da Lista de Requisitos no [Documento de Visão](doc-visao.md).

## Histórico de revisões

| Data       | Versão    | Descrição             | Autor         |
| :--------- | :-------: | :-------------------: | :------------ |
| 02/23/2025 | 0.0.1     | Descrição do documento e detalhamento do User Story US01 | Júlio

### User Story US01 - Manter Cliente

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um cadastro e autenticação de usuários que têm acesso ao sistema. Um usuário tem nome, senha, email e número de telefone. O usuário com uma conta já cadastrada pode realizar a autenticação com email e senha. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF02          | Manter Clientes  |
| RF06          | Sistema de autenticação e login        |


|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 5 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Stênio                            | 
| **Desenvolvedor**         | Denner                                 | 
| **Testador**              | Júlio                               | 
| **Desenvolvedor**         | Guilherme                                  | 

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | O usuário informa, no formulário de registro, todos os dados corretos para ser cadastrado. Ao clicar em enviar, ele é redirecionado para a página principal. |
| **TA01.02** | O usuário informa, no formulário de registro, todos os dados incorretos para ser cadastrado. Ao clicar em enviar, os campos do formulário informam, em vermelho, os dados incorretos. |
| **TA01.03** | O usuário informa, no formulário de login, todos os dados corretos de uma conta. Ao clicar em enviar, ele é redirecionado para a página principal. |
| **TA01.04** | O usuário informa, no formulário de login, todos os dados incorretos de uma conta. Ao clicar em enviar, os campos do formulário informam, em vermelho, os dados incorretos. |
