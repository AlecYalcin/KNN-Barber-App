# Documento de User Stories

## Descrição

Este documento descreve os User Stories do projeto KNN Barber App, criado a partir da Lista de Requisitos no [Documento de Visão](doc-visao.md).

## Histórico de revisões

| Data       | Versão |                        Descrição                         | Autor |
| :--------- | :----: | :------------------------------------------------------: | :---- |
| 02/12/2024 | 1.0    | Criação do Documento                                     | Alec Can Yalcin |
| 02/12/2024 | 1.1    | US01                                                     | Alec Can Yalcin |
| 02/12/2024 | 1.2    | US02, US03 e US04                                        | Denner Bismarck |
| 02/12/2024 | 1.3    | US05, US06 e US07                                        | Júlio César     |


### User Story US01 - Manter Cliente

|               |                                                                                                                                                                                                                                       |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve manter um cadastro e autenticação de usuários que têm acesso ao sistema. Um usuário tem nome, senha, email e número de telefone. O usuário com uma conta já cadastrada pode realizar a autenticação com email e senha. |

| **Requisitos envolvidos** |                                 |
| ------------------------- | :------------------------------ |
| RF05                      | Criar Cliente                   |
| RF06                      | Listar Clientes                 |
| RF07                      | Atualizar Cliente               |
| RF08                      | Remover Cliente                 |
| RF18                      | Criar Conta de Usuário          |
| RF19                      | Verificar Sessão                |
| RF20                      | Atualizar Conta de Usuário      |
| RF21                      | Remover Conta de Usuário        |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 5 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**            | Stênio    |
| **Desenvolvedor**       | Denner    |
| **Testador**            | Júlio     |
| **Desenvolvedor**       | Guilherme |

| Testes de Aceitação (TA) |                                                                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código**               | **Descrição**                                                                                                                                                                         |
| **TA01.01**              | O usuário informa, no formulário de registro, todos os dados corretos para ser cadastrado. Ao clicar em enviar, ele é redirecionado para a página principal.                          |
| **TA01.02**              | O usuário informa, no formulário de registro, todos os dados incorretos para ser cadastrado. Ao clicar em enviar, os campos do formulário informam, em vermelho, os dados incorretos. |
| **TA01.03**              | O usuário informa, no formulário de login, todos os dados corretos de uma conta. Ao clicar em enviar, ele é redirecionado para a página principal.                                    |
| **TA01.04**              | O usuário informa, no formulário de login, todos os dados incorretos de uma conta. Ao clicar em enviar, os campos do formulário informam, em vermelho, os dados incorretos.           |

### User Story US02 - Manter Agenda

|               |                                                                                                                                                                                                                                       |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve disponibilizar a agenda de horários disponíveis para se marcar um atendimento. Essa agenda deve ter os horários e o barbeiro de cada horário, sinalizando com uma legenda qual é qual. Um usuário deve escolher um horário e serviço e aguardar para aprovação. |

| **Requisitos envolvidos** |                                 |
| ------------------------- | :------------------------------ |
| RF13                      | Criar Agendamento               | 
| RF14                      | Listar Agendamentos             | 
| RF15                      | Atualizar Agendamento           | 
| RF16                      | Remover Agendamento             |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 7 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**            | Stênio    |
| **Desenvolvedor**       | Denner    |
| **Testador**            | Júlio     |
| **Desenvolvedor**       | Guilherme |

| Testes de Aceitação (TA) |                                                                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código**               | **Descrição**                                                                                                                                                                         |
| **TA01.01**              | O usuário, na página de agendamentos, seleciona um horário disponível e um serviço oferecido. Ao clicar em confirmar, o usuário recebe uma mensagem na tela e um redirecionamento para a página principal. Mensagem: “Seu agendamento está sendo analisado pelo barbeiro.”                          |
| **TA01.02**              | O usuário, na página de agendamentos, seleciona um horário recentemente preenchido. Ao clicar em confirmar, o usuário recebe uma mensagem na tela. Mensagem: “O horário se tornou indisponível enquanto esteve em uso, por favor selecione outro.” |

### User Story US03 - Disponibilizar Horário

|               |                                                                                                                                                                                                                                       |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve conter a funcionalidade de cada barbeiro disponibilizar seus horários de atendimento para que os clientes consigam agendar nestes horários. |

| **Requisitos envolvidos** |                                 |
| ------------------------- | :------------------------------ |
| RF10                      | Listar Barbeadores              |
| RF13                      | Criar Agendamento               |
| RF14                      | Listar Agendamentos             |
| RF15                      | Atualizar Agendamento           |
| RF16                      | Remover Agendamento             |
| RF22                      | Criar Horário                   |
| RF23                      | Listar Horários                 |
| RF24                      | Atualizar Horário               |
| RF25                      | Remover Horário                 |


|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 5 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**            | Stênio    |
| **Desenvolvedor**       | Denner    |
| **Testador**            | Júlio     |
| **Desenvolvedor**       | Guilherme |

| Testes de Aceitação (TA) |                                                                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código**               | **Descrição**                                                                                                                                                                         |
| **TA01.01**              | O barbeiro entrará na tela de disponibilizar horário. O sistema exibe uma tela com uma representação visual de dias e horas. O barbeiro deverá selecionar os horários que deseja disponibilizar para agendamento.                          |
| **TA02.01**              | Alteração de disponibilidade: O barbeiro deverá selecionar os horários que deseja alterar a disponibilidade, tirando-os. O sistema deve informar (Se existir) a quantidade de agendamentos marcados para aquele horário. |

### User Story US04 - Manter Serviços

|               |                                                                                                                                                                                                                                       |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve ter a opção de cadastrar, ver, editar e alterar serviços fornecidos pelo barbeiro. |

| **Requisitos envolvidos** |                                 |
| ------------------------- | :------------------------------ |
| RF01                      | Criar Serviço                   |
| RF02                      | Listar Serviços                 |
| RF03                      | Atualizar Serviço               |
| RF04                      | Remover Serviço                 |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 5 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**            | Stênio    |
| **Desenvolvedor**       | Denner    |
| **Testador**            | Júlio     |
| **Desenvolvedor**       | Guilherme |

| Testes de Aceitação (TA) |                                                                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código**               | **Descrição**                                                                                                                                                                         |
| **TA01.01**              | Os atores entrarão na aba de consultas de serviços. O sistema disponibiliza uma tabela com todos os serviços disponíveis, com nome, descrição e preço.                          |
| **TA02.01**              | Marcar horários: O cliente escolhe o serviço desejado. |
| **TA02.02**              | Alterar ou excluir serviços: O barbeiro escolhe o serviço que deseja alterar ou excluir. O sistema informa,recebe e avalia todas as alterações do barbeiro.                                    |
| **TA03.01**              | Ao abrir a aba de serviços, o cliente só terá a opção de vê-los, sem poder editar ou criar novos.           |

### User Story US05 - Aprovar agendamentos

|               |                                                                                                                                                                                                                                       |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve exigir a aprovação dos horários que forem reservados pelo cliente, podendo recusar e pedir alterações ou aprovar o horário e, assim, o processo de agendamento ser concluído. |

| **Requisitos envolvidos** |                                 |
| ------------------------- | :------------------------------ |
| RF13                      | Criar Agendamento               |
| RF17                      | Confirmar Atendimento           |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 5 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**            | Stênio    |
| **Desenvolvedor**       | Denner    |
| **Testador**            | Júlio     |
| **Desenvolvedor**       | Guilherme |

| Testes de Aceitação (TA) |                                                                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código**               | **Descrição**                                                                                                                                                                         |
| **TA01.01**              | O sistema notifica o barbeiro que existe um agendamento pendente de aprovação. O sistema mostra uma listagem com todos os agendamentos ainda não aprovados, com o nome do cliente, serviço, forma de pagamento e horário. O barbeiro seleciona a opção para aprovar.                          |
| **TA02.01**              | O barbeiro fará a alteração dos campos que achar necessário. |
| **TA02.02**              | O barbeiro recusa o agendamento. O sistema disponibiliza uma caixa em texto para esclarecer os motivos da recusa. O barbeiro descreve a motivação para a recusa.                                    |

### User Story US06 - Manter pagamento

|               |                                                                                                                                                                                                                                       |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve conter os recursos necessários para realizar o pagamento de um agendamento. |

| **Requisitos envolvidos** |                                 |
| ------------------------- | :------------------------------ |
| RF22                      | Criar Pagamento                 |
| RF23                      | Listar Pagamentos               |
| RF24                      | Atualizar Pagamento             |
| RF25                      | Remover Pagamento               |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 5 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**            | Stênio    |
| **Desenvolvedor**       | Denner    |
| **Testador**            | Júlio     |
| **Desenvolvedor**       | Guilherme |

| Testes de Aceitação (TA) |                                                                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código**               | **Descrição**                                                                                                                                                                         |
| **TA01.01**              | O cliente realiza o pagamento de um agendamento pendente. Após concluir, ele vê a confirmação do pagamento e é redirecionado para a tela principal. O sistema salva a data do pagamento e o status do agendamento fica como "Pago".                          |
| **TA01.02**              | O cliente acessa a listagem de pagamentos realizados e vê os registros organizados por data. Em Pagamentos há um detalhamento de informações sobre o serviço, como a data, o valor e serviço prestado. |

### User Story US07 - Manter Barbeiro

|               |                                                                                                                                                                                                                                       |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve manter o cadastro e autenticação de barbeiros. |

| **Requisitos envolvidos** |                                 |
| ------------------------- | :------------------------------ |
| RF09                      | Criar Barbeador                 | 
| RF10                      | Listar Barbeadores              | 
| RF11                      | Atualizar Barbeador             | 
| RF12                      | Remover Barbeador               |
| RF18                      | Criar Conta de Usuário          | 
| RF19                      | Verificar Sessão                | 
| RF20                      | Atualizar Conta de Usuário      | 
| RF21                      | Remover Conta de Usuário        |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 5 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**            | Stênio    |
| **Desenvolvedor**       | Denner    |
| **Testador**            | Júlio     |
| **Desenvolvedor**       | Guilherme |

| Testes de Aceitação (TA) |                                                                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código**               | **Descrição**                                                                                                                                                                         |
| **TA01.01**              | Um barbeiro já cadastrado, inicia o cadastro de um novo barbeiro, e informa os dados no formulário de registro. Ele informa os dados de maneira correta para ser enviado, Ao clicar em “enviar”, os dados são aceitos pelo sistema, e o novo barbeiro passa a possuir um cadastro, e é redirecionado para a página principal.                          |
| **TA01.02**              | Um barbeiro já cadastrado, inicia o cadastro de um novo barbeiro, e informa os dados no formulário de registro. Ele informa os dados de maneira incorreta para ser enviado, Ao clicar em “enviar”, os dados são negados pelo sistema, e é mostrado um texto em vermelho que os dados não são aceitos. |
| **TA01.03**              | O barbeiro, no formulário de login, informa os dados de maneira correta, e é redirecionado para a página do barbeiro. |
| **TA01.04**              | O barbeiro, no formulário de login, informa os dados de maneira incorreta, e é redirecionado para a página principal. |

### User Story US08 - Extrato de Pagamento

|               |                                                                                                                                                                                                                                       |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve possuir uma função que exibe os valores ganhos em um período de tempo. |

| **Requisitos envolvidos** |                                 |
| ------------------------- | :------------------------------ |
| RF23                      | Listar Pagamentos               |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 5 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**            | Stênio    |
| **Desenvolvedor**       | Denner    |
| **Testador**            | Júlio     |
| **Desenvolvedor**       | Guilherme |

| Testes de Aceitação (TA) |                                                                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código**               | **Descrição**                                                                                                                                                                         |
| **TA01.01**              | O barbeiro irá acessar a página de Pagamentos e poderá filtrar as informações de pagamentos baseado em tempo e quantidade, e o sistema deve produzir um relatório de acordo com que foi filtrado pelo barbeiro.                          |
| **TA01.02**              | O barbeiro na página de Pagamentos, ao colocar um filtro de tempo anterior a criação do do primeiro pagamento, ao a criação do aplicativo, ao selecionar “Produzir Relatório”, o sistema irá exibir a mensagem: “Filtro de tempo excedido”. |