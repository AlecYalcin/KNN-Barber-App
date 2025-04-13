# Documento de User Stories

## Descrição

Este documento descreve os User Stories do projeto KNN Barber App, criado a partir da Lista de Requisitos no [Documento de Visão](doc-visao.md).

## Histórico de revisões

| Data       | Versão |           Descrição           | Autor                 |
| :--------- | :----: | :---------------------------: | :-------------------- |
| 02/12/2024 |  1.0   |     Criação do Documento      | Alec Can Yalcin       |
| 02/12/2024 |  1.1   |             US01              | Alec Can Yalcin       |
| 02/12/2024 |  1.2   |       US02, US03 e US04       | Denner Bismarck       |
| 02/12/2024 |  1.3   |       US05, US06 e US07       | Júlio César           |
| 04/04/2025 |  2.0   |      Atualização de US's      | Júlio César           |
| 08/04/2025 |  2.1   | Adição de testes de aceitação | Guilherme de Medeiros |
| 13/04/2025 |  3.0   |      Refatoração de US's      | Alec Can Yalcin       |

### User Story US01 - Gerenciar Conta de Barbeiro

|               |                                                                                                                                               |
| ------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | Como proprietário do sistema, quero ser capaz de atualizar minhas informações pessoais para que meus clientes tenham acesso a dados corretos. |

| **Requisitos envolvidos** | **Descrição**                                                                                       |
| ------------------------- | :-------------------------------------------------------------------------------------------------- |
| RF01                      | Permitir que o usuário verifique seu status de sessão e visualize informações da conta autenticada. |
| RF02                      | Diferenciar as permissões de funcionalidades entre barbeiros e clientes.                            |
| RF06                      | Permitir o cadastro de um barbeiro com nome, número de contato e horários de atendimento.           |
| RF07                      | Permitir que o barbeiro edite suas informações pessoais.                                            |
| RF08                      | Permitir que o barbeiro exclua sua conta do sistema.                                                |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 5 h       |
| **Tempo Gasto (real):** | --        |
| **Tamanho Funcional**   | 5 PF      |
| **Analista**            | --        |
| **Testador**            | --        |
| **Desenvolvedor**       | --        |
| **Desenvolvedor**       | --        |

#### Testes de Aceitação – US01

| Código  | Cenário | Descrição |
| ------- | ------- | --------- |
| TA01.01 | --      | --        |

### User Story US02 - Gerenciar Jornada de Trabalho

|               |                                                                                                                                          |
| ------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | Como proprietário do sistema, quero poder alterar minha jornada de trabalho para me adaptar às necessidades do mês, da semana ou do dia. |

| **Requisitos envolvidos** | **Descrição**                                                                                          |
| ------------------------- | :----------------------------------------------------------------------------------------------------- |
| RF14                      | Permitir que o barbeiro defina dias da semana e horários de expediente.                                |
| RF15                      | Permitir que o barbeiro edite uma jornada cadastrada.                                                  |
| RF16                      | Permitir que o barbeiro desligue temporariamente sua jornada de trabalho.                              |
| RF17                      | Permitir ao barbeiro registrar horários em que estará indisponível, com data, horário e justificativa. |
| RF18                      | Permitir que o barbeiro edite um horário previamente registrado como indisponível.                     |
| RF19                      | Permitir que o barbeiro exclua um horário registrado como indisponível.                                |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 3 h       |
| **Tempo Gasto (real):** | --        |
| **Tamanho Funcional**   | 3 PF      |
| **Analista**            | --        |
| **Testador**            | --        |
| **Desenvolvedor**       | --        |
| **Desenvolvedor**       | --        |

#### Testes de Aceitação – US02

| Código  | Cenário | Descrição |
| ------- | ------- | --------- |
| TA02.01 | --      | --        |

### User Story US03 - Gerenciar Serviços Ofertados

|               |                                                                                                                        |
| ------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | Como proprietário do sistema, quero cadastrar e editar os serviços que ofereço, com informações sobre duração e preço. |

| **Requisitos envolvidos** | **Descrição**                                                               |
| ------------------------- | :-------------------------------------------------------------------------- |
| RF10                      | Permitir que o barbeiro registre um novo serviço com nome, preço e duração. |
| RF11                      | Permitir que o barbeiro atualize dados de um serviço existente.             |
| RF12                      | Permitir que o barbeiro exclua um serviço cadastrado.                       |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 2 h       |
| **Tempo Gasto (real):** | --        |
| **Tamanho Funcional**   | 2 PF      |
| **Analista**            | --        |
| **Testador**            | --        |
| **Desenvolvedor**       | --        |
| **Desenvolvedor**       | --        |

#### Testes de Aceitação – US03

| Código  | Cenário | Descrição |
| ------- | ------- | --------- |
| TA03.01 | --      | --        |

### User Story US04 - Realizar Agendamentos

|               |                                                                                                                               |
| ------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | Como cliente do sistema, quero marcar ou desmarcar meus agendamentos com base nos serviços escolhidos e horários disponíveis. |

| **Requisitos envolvidos** | **Descrição**                                                                                    |
| ------------------------- | :----------------------------------------------------------------------------------------------- |
| RF13                      | Permitir que o cliente visualize todos os serviços ativos.                                       |
| RF20                      | O cliente deve ser capaz de visualizar os horários não disponívesi para agendamento              |
| RF21                      | Verificar se o horário está dentro da jornada, não é um horário indisponível e não está ocupado. |
| RF22                      | Permitir que o cliente selecione um ou mais serviços para o agendamento.                         |
| RF23                      | Calcular automaticamente a duração do agendamento com base nos serviços escolhidos.              |
| RF24                      | Permitir que o cliente agende serviços em horários disponíveis.                                  |
| RF25                      | Permitir que o cliente ou barbeiro cancele um agendamento existente.                             |
| RF27                      | Marcar automaticamente como ocupado o horário agendado.                                          |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 10 h      |
| **Tempo Gasto (real):** | --        |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**            | --        |
| **Testador**            | --        |
| **Desenvolvedor**       | --        |
| **Desenvolvedor**       | --        |

#### Testes de Aceitação – US04

| Código  | Cenário | Descrição |
| ------- | ------- | --------- |
| TA04.01 | --      | --        |

### User Story US05 - Gerenciar Agendamentos

|               |                                                                                                                                          |
| ------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | Como proprietário do sistema, quero visualizar os agendamentos marcados, desmarcar quando necessário e justificar faltas ou emergências. |

| **Requisitos envolvidos** | **Descrição**                                                                                          |
| ------------------------- | :----------------------------------------------------------------------------------------------------- |
| RF17                      | Permitir ao barbeiro registrar horários em que estará indisponível, com data, horário e justificativa. |
| RF25                      | Permitir que o cliente ou barbeiro cancele um agendamento existente.                                   |
| RF26                      | Os usuários do sistema devem ser capazes de visualizar os agendamentos do sistema                      |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 5 h       |
| **Tempo Gasto (real):** | --        |
| **Tamanho Funcional**   | 5 PF      |
| **Analista**            | --        |
| **Testador**            | --        |
| **Desenvolvedor**       | --        |
| **Desenvolvedor**       | --        |

#### Testes de Aceitação – US05

| Código  | Cenário | Descrição |
| ------- | ------- | --------- |
| TA05.01 | --      | --        |

### User Story US06 - Visualizar Relatório Financeiro

|               |                                                                                                                                                |
| ------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | Como proprietário do sistema, quero visualizar o histórico completo de pagamentos realizados, com detalhes dos usuários e formas de pagamento. |

| **Requisitos envolvidos** | **Descrição**                                                               |
| ------------------------- | :-------------------------------------------------------------------------- |
| RF30                      | Permitir que o barbeiro confirme que o pagamento foi realizado.             |
| RF32                      | Permitir que o barbeiro veja todos os agendamentos e pagamentos realizados. |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Imporante |
| **Estimativa**          | 4 h       |
| **Tempo Gasto (real):** | --        |
| **Tamanho Funcional**   | 4 PF      |
| **Analista**            | --        |
| **Testador**            | --        |
| **Desenvolvedor**       | --        |
| **Desenvolvedor**       | --        |

#### Testes de Aceitação – US06

| Código  | Cenário | Descrição |
| ------- | ------- | --------- |
| TA06.01 | --      | --        |

### User Story US07 - Pagamentos do Sistema

|               |                                                                                                                                                    |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | Como Cliente que realizou um agendamento, eu quero ser capaz de ver o valor final, as formas de pagamentos disponíveis e selecionar qual eu desejo |

| **Requisitos envolvidos** | **Descrição**                                                                  |
| ------------------------- | :----------------------------------------------------------------------------- |
| RF28                      | Exibir ao cliente o valor total do agendamento após a seleção dos serviços.    |
| RF29                      | Permitir que o cliente escolha a forma de pagamento no momento do agendamento. |

|                         |            |
| ----------------------- | ---------- |
| **Prioridade**          | Importante |
| **Estimativa**          | 3 h        |
| **Tempo Gasto (real):** | --         |
| **Tamanho Funcional**   | 3 PF       |
| **Analista**            | --         |
| **Testador**            | --         |
| **Desenvolvedor**       | --         |
| **Desenvolvedor**       | --         |

#### Testes de Aceitação – US07

| Código  | Cenário | Descrição |
| ------- | ------- | --------- |
| TA07.01 | --      | --        |

### User Story US08 - Gerenciar Conta de Cliente

|               |                                                                                       |
| ------------- | :------------------------------------------------------------------------------------ |
| **Descrição** | Como cliente do sistema, quero alterar minhas informações pessoais salvas no sistema. |

| **Requisitos envolvidos** | **Descrição**                                                                                       |
| ------------------------- | :-------------------------------------------------------------------------------------------------- |
| RF01                      | Permitir que o usuário verifique seu status de sessão e visualize informações da conta autenticada. |
| RF02                      | Diferenciar as permissões de funcionalidades entre barbeiros e clientes.                            |
| RF03                      | Permitir o cadastro de um cliente com nome, CPF e número de contato.                                |
| RF04                      | Permitir que o cliente edite suas informações pessoais.                                             |
| RF05                      | Permitir que o cliente exclua sua conta do sistema.                                                 |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Desejável |
| **Estimativa**          | 2 h       |
| **Tempo Gasto (real):** | --        |
| **Tamanho Funcional**   | 2 PF      |
| **Analista**            | --        |
| **Testador**            | --        |
| **Desenvolvedor**       | --        |
| **Desenvolvedor**       | --        |

#### Testes de Aceitação – US08

| Código  | Cenário | Descrição |
| ------- | ------- | --------- |
| TA08.01 | --      | --        |

### User Story US09 - Consultar Histórico de Agendamentos e Pagamentos

|               |                                                                                                                     |
| ------------- | :------------------------------------------------------------------------------------------------------------------ |
| **Descrição** | Como usuário do sistema, quero visualizar o histórico de agendamentos realizados e os pagamentos associados a eles. |

| **Requisitos envolvidos** | **Descrição**                                                        |
| ------------------------- | :------------------------------------------------------------------- |
| RF31                      | Permitir que o cliente veja seus agendamentos e pagamentos passados. |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Desejável |
| **Estimativa**          | 3 h       |
| **Tempo Gasto (real):** | --        |
| **Tamanho Funcional**   | 3 PF      |
| **Analista**            | --        |
| **Testador**            | --        |
| **Desenvolvedor**       | --        |
| **Desenvolvedor**       | --        |

#### Testes de Aceitação – US09

| Código  | Cenário | Descrição |
| ------- | ------- | --------- |
| TA07.01 | --      | --        |
