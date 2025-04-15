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

| Código  | Cenário                                             | Descrição                                                                                                                                                                                                                                            |
| ------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA01.01 | Cadastro de barbeiro com dados válidos              | O barbeiro preenche todos os campos do formulário corretamente (nome, contato, horários) e submete. O sistema valida os dados, cria o cadastro e redireciona para a página principal com uma mensagem de sucesso.                                     |
| TA01.02 | Cadastro com dados inválidos                        | O barbeiro tenta submeter o formulário com dados inválidos ou incompletos. O sistema exibe mensagens de erro específicas para cada campo inválido e não permite o cadastro.                                                                           |
| TA01.03 | Atualização de dados do perfil                      | Um barbeiro logado acessa seu perfil, altera informações pessoais e salva. O sistema atualiza os dados e exibe mensagem de confirmação.                                                                                                              |
| TA01.04 | Verificação de permissões                          | O sistema identifica corretamente o usuário como barbeiro e exibe apenas as funcionalidades permitidas para seu perfil.                                                                                                                               |
| TA01.05 | Remoção de conta                                    | Um barbeiro logado solicita a exclusão de sua conta, confirma a ação, e o sistema remove seus dados após verificar que não há agendamentos pendentes.                                                                                                |

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

| Código  | Cenário                                                | Descrição                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA02.01 | Definição de jornada semanal                           | O barbeiro define seus dias e horários de trabalho da semana. O sistema salva a jornada e passa a exibir apenas estes horários como disponíveis para agendamento.                                              |
| TA02.02 | Registro de indisponibilidade                          | O barbeiro registra um período específico como indisponível, incluindo data, horário e justificativa. O sistema bloqueia estes horários para agendamentos.                                                     |
| TA02.03 | Edição de horário indisponível                         | O barbeiro edita um horário previamente marcado como indisponível. O sistema atualiza o registro e ajusta a disponibilidade.                                                                                   |
| TA02.04 | Desativação temporária da jornada                      | O barbeiro desativa temporariamente sua jornada de trabalho. O sistema bloqueia novos agendamentos até a reativação.                                                                                           |
| TA02.05 | Tentativa de edição com agendamentos existentes        | O barbeiro tenta alterar um horário que já possui agendamentos. O sistema exibe um alerta e só permite a alteração após a resolução dos conflitos.                                                             |

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

| Código  | Cenário                                                      | Descrição                                                                                                                                                                                   |
| ------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA03.01 | Cadastro de novo serviço                                      | O barbeiro cadastra um novo serviço com nome, preço e duração. O sistema salva e exibe mensagem: "Serviço cadastrado com sucesso".                                                          |
| TA03.02 | Cadastro de serviço com dados incompletos                     | O barbeiro tenta cadastrar um serviço deixando campos obrigatórios em branco. O sistema exibe mensagens de erro de validação e impede o cadastro.                                           |
| TA03.03 | Atualização de serviço existente                             | O barbeiro edita as informações de um serviço cadastrado. O sistema atualiza os dados e exibe mensagem de confirmação.                                                                      |
| TA03.04 | Remoção de serviço sem agendamentos                          | O barbeiro remove um serviço que não possui agendamentos futuros. O sistema exclui o registro e confirma a operação.                                                                        |
| TA03.05 | Tentativa de remoção de serviço com agendamentos pendentes    | O barbeiro tenta excluir um serviço vinculado a agendamentos futuros. O sistema bloqueia a operação e exibe mensagem informando sobre a necessidade de resolver os agendamentos primeiro.   |

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

| Código  | Cenário                                                    | Descrição                                                                                                                                                                                               |
| ------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA04.01 | Seleção de serviços para agendamento                       | O cliente seleciona múltiplos serviços da lista disponível. O sistema calcula automaticamente a duração total e o valor final do agendamento.                                                            |
| TA04.02 | Visualização de horários disponíveis                        | O cliente acessa a agenda e visualiza apenas os horários disponíveis dentro da jornada do barbeiro, excluindo períodos indisponíveis e já agendados.                                                    |
| TA04.03 | Agendamento com sucesso                                     | O cliente seleciona serviços e um horário disponível. O sistema registra o agendamento, marca o horário como ocupado e envia confirmação.                                                               |
| TA04.04 | Tentativa de agendamento em horário ocupado                | O cliente tenta agendar em um horário que acabou de ser preenchido. O sistema exibe mensagem: "Horário não está mais disponível" e solicita nova seleção.                                              |
| TA04.05 | Cancelamento de agendamento pelo cliente                    | O cliente cancela um agendamento futuro. O sistema remove o registro e libera o horário para nova marcação.                                                                                             |
| TA04.06 | Tentativa de agendamento fora da jornada                   | O cliente tenta agendar em um horário fora da jornada do barbeiro. O sistema impede a operação e exibe mensagem informativa.                                                                           |

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

| Código  | Cenário                                                | Descrição                                                                                                                                                                                           |
| ------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA05.01 | Visualização de agendamentos do dia                    | O barbeiro acessa a lista de agendamentos e visualiza todos os horários marcados, com detalhes dos clientes e serviços selecionados.                                                                |
| TA05.02 | Registro de indisponibilidade emergencial              | O barbeiro registra uma indisponibilidade não prevista, fornecendo justificativa. O sistema notifica os clientes afetados sobre o cancelamento.                                                     |
| TA05.03 | Cancelamento de agendamento pelo barbeiro              | O barbeiro cancela um agendamento futuro, fornece justificativa. O sistema notifica o cliente e libera o horário.                                                                                   |
| TA05.04 | Visualização de histórico de agendamentos             | O barbeiro consulta o histórico completo de agendamentos, podendo filtrar por período e status (realizados, cancelados, etc.).                                                                      |
| TA05.05 | Gestão de conflitos de horário                        | O barbeiro tenta registrar uma indisponibilidade em horário com agendamentos. O sistema alerta sobre os conflitos e solicita resolução antes de confirmar.                                          |

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

| Código  | Cenário                                            | Descrição                                                                                                                                                                               |
| ------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA06.01 | Visualização de relatório por período              | O barbeiro seleciona um período específico e visualiza todos os pagamentos realizados, com detalhes de serviços, clientes e formas de pagamento.                                        |
| TA06.02 | Confirmação de pagamentos recebidos                | O barbeiro marca como recebido o pagamento de um agendamento realizado. O sistema atualiza o status do pagamento no histórico.                                                          |
| TA06.03 | Filtragem de relatório por forma de pagamento      | O barbeiro filtra o relatório por forma de pagamento específica. O sistema exibe apenas os registros correspondentes.                                                                   |
| TA06.04 | Exportação de relatório financeiro                 | O barbeiro solicita a exportação do relatório filtrado. O sistema gera um arquivo com os dados selecionados.                                                                            |
| TA06.05 | Visualização de métricas financeiras               | O barbeiro acessa o dashboard financeiro e visualiza métricas como total recebido, média por período e serviços mais lucrativos.                                                        |

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

| Código  | Cenário                                                | Descrição                                                                                                                                                                               |
| ------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA07.01 | Cálculo do valor total                                 | Após o cliente selecionar múltiplos serviços, o sistema exibe automaticamente o valor total do agendamento.                                                                              |
| TA07.02 | Seleção de forma de pagamento                          | O cliente visualiza as formas de pagamento disponíveis e seleciona uma opção. O sistema registra a escolha junto ao agendamento.                                                         |
| TA07.03 | Alteração da forma de pagamento                        | O cliente tenta alterar a forma de pagamento de um agendamento futuro. O sistema permite a mudança e atualiza o registro.                                                               |
| TA07.04 | Tentativa de seleção de pagamento indisponível        | O cliente tenta selecionar uma forma de pagamento temporariamente indisponível. O sistema exibe mensagem informativa e solicita outra opção.                                            |
| TA07.05 | Confirmação dos detalhes do pagamento                  | Antes de finalizar o agendamento, o sistema exibe um resumo com valor total e forma de pagamento para confirmação do cliente.                                                           |

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

| Código  | Cenário                                               | Descrição                                                                                                                                                                           |
| ------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA08.01 | Cadastro de cliente com dados válidos                 | O cliente preenche corretamente nome, CPF e contato no formulário de cadastro. O sistema valida os dados e cria a conta com sucesso.                                                |
| TA08.02 | Cadastro com dados inválidos                          | O cliente tenta cadastrar com dados inválidos ou incompletos. O sistema exibe mensagens de erro específicas para cada campo inválido.                                               |
| TA08.03 | Atualização de informações pessoais                   | O cliente logado acessa seu perfil, atualiza suas informações e salva. O sistema confirma as alterações com uma mensagem de sucesso.                                               |
| TA08.04 | Verificação de permissões de cliente                  | O sistema identifica corretamente o usuário como cliente e exibe apenas as funcionalidades permitidas para seu perfil.                                                              |
| TA08.05 | Exclusão de conta de cliente                          | O cliente solicita a exclusão de sua conta, confirma a ação, e o sistema remove seus dados após verificar que não há agendamentos pendentes.                                        |

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

| Código  | Cenário                                                | Descrição                                                                                                                                                                           |
| ------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA09.01 | Visualização de histórico completo                     | O cliente acessa seu histórico e visualiza todos os agendamentos passados, com detalhes de serviços, valores e status de pagamento.                                                 |
| TA09.02 | Filtragem de histórico por período                     | O cliente filtra seu histórico por um período específico. O sistema exibe apenas os registros dentro do intervalo selecionado.                                                      |
| TA09.03 | Visualização de detalhes do agendamento                | O cliente seleciona um agendamento específico do histórico. O sistema exibe todos os detalhes, incluindo serviços realizados, valor pago e forma de pagamento.                     |
| TA09.04 | Busca por tipo de serviço                              | O cliente filtra seu histórico por um tipo específico de serviço. O sistema exibe apenas os agendamentos que incluem o serviço selecionado.                                        |
| TA09.05 | Exportação do histórico                                | O cliente solicita exportação de seu histórico de agendamentos. O sistema gera um arquivo com os dados selecionados.                                                                |
