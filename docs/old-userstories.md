# Documento de User Stories

## Descrição

Este documento descreve os User Stories do projeto KNN Barber App, criado a partir da Lista de Requisitos no [Documento de Visão](doc-visao.md).

## Histórico de revisões

| Data       | Versão |      Descrição       | Autor           |
| :--------- | :----: | :------------------: | :-------------- |
| 02/12/2024 |  1.0   | Criação do Documento | Alec Can Yalcin |
| 02/12/2024 |  1.1   |         US01         | Alec Can Yalcin |
| 02/12/2024 |  1.2   |  US02, US03 e US04   | Denner Bismarck |
| 02/12/2024 |  1.3   |  US05, US06 e US07   | Júlio César     |

### User Story US01 - Manter Cliente

|               |                                                                                                                                                                                                                                       |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve manter um cadastro e autenticação de usuários que têm acesso ao sistema. Um usuário tem nome, senha, email e número de telefone. O usuário com uma conta já cadastrada pode realizar a autenticação com email e senha. |

| **Requisitos envolvidos** |                            |
| ------------------------- | :------------------------- |
| RF05                      | Criar Cliente              |
| RF06                      | Listar Clientes            |
| RF07                      | Atualizar Cliente          |
| RF08                      | Remover Cliente            |
| RF18                      | Criar Conta de Usuário     |
| RF19                      | Verificar Sessão           |
| RF20                      | Atualizar Conta de Usuário |
| RF21                      | Remover Conta de Usuário   |

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

#### Testes de Aceitação – US01 Manter Cliente

| Código  | Cenário                                               | Descrição                                                                                                                                                 |
| ------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA01.01 | Registro com dados válidos (RF05, RF18)               | O usuário informa nome, email, telefone e senha válidos no formulário de registro. Ao clicar em "Registrar", ele é redirecionado para a página principal. |
| TA01.02 | Registro com dados inválidos (RF05, RF18)             | O usuário informa dados inválidos ou incompletos no formulário de registro. Ao clicar em "Registrar", os campos inválidos exibem mensagens de erro.       |
| TA01.03 | Login com credenciais corretas (RF19)                 | O usuário com conta existente informa email e senha corretos no formulário de login. Ao clicar em "Entrar", é redirecionado para a página principal.      |
| TA01.04 | Login com credenciais incorretas (RF19)               | O usuário informa email ou senha incorretos. Ao clicar em "Entrar", o sistema exibe mensagem de erro sem redirecionar.                                    |
| TA01.05 | Verificação de sessão ativa (RF19)                    | Um usuário autenticado acessa uma página protegida. O sistema reconhece a sessão ativa e permite o acesso ao conteúdo restrito.                           |
| TA01.06 | Listagem de clientes cadastrados (RF06)               | Um usuário autenticado acessa a lista de clientes. O sistema exibe nome, email e telefone dos clientes cadastrados.                                       |
| TA01.07 | Atualização de dados do cliente (RF07)                | Um cliente autenticado acessa seu perfil, altera nome ou telefone e salva. O sistema atualiza os dados e exibe a nova informação ao recarregar a página.  |
| TA01.08 | Atualização de credenciais da conta de usuário (RF20) | O cliente acessa as configurações de conta, altera email ou senha e confirma. O sistema salva as alterações e permite login com os novos dados.           |
| TA01.09 | Remoção da conta de cliente (RF08, RF21)              | O cliente autenticado escolhe "Excluir minha conta", confirma a ação, e o sistema remove seus dados e redireciona para a tela de login.                   |
| TA01.10 | Tentativa de login após remoção da conta (RF21)       | Um usuário tenta fazer login após excluir a conta. O sistema exibe erro e impede o acesso.                                                                |

### User Story US02 - Manter Agenda

|               |                                                                                                                                                                                                                                                                                |
| ------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | O sistema deve disponibilizar a agenda de horários disponíveis para se marcar um atendimento. Essa agenda deve ter os horários e o barbeiro de cada horário, sinalizando com uma legenda qual é qual. Um usuário deve escolher um horário e serviço e aguardar para aprovação. |

| **Requisitos envolvidos** |                       |
| ------------------------- | :-------------------- |
| RF13                      | Criar Agendamento     |
| RF14                      | Listar Agendamentos   |
| RF15                      | Atualizar Agendamento |
| RF16                      | Remover Agendamento   |

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

#### Testes de Aceitação

| Código  | Cenário                                                      | Descrição                                                                                                                                                                                               |
| ------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA02.01 | Criação de agendamento com horário e serviço válidos (RF13)  | O usuário acessa a página de agendamentos, seleciona um horário disponível e um serviço. Ao confirmar, recebe a mensagem “Seu agendamento está sendo analisado pelo barbeiro.” e é redirecionado.       |
| TA02.02 | Tentativa de agendamento com horário recém-preenchido (RF13) | O usuário seleciona um horário que foi preenchido durante a navegação. Ao clicar em confirmar, recebe a mensagem: “O horário se tornou indisponível enquanto esteve em uso, por favor selecione outro.” |
| TA02.03 | Visualização da agenda com horários e barbeiros (RF14)       | O usuário acessa a página de agendamentos. O sistema exibe uma agenda com horários disponíveis, barbeiros associados e uma legenda indicando quem atende cada horário.                                  |
| TA02.04 | Edição de um agendamento existente (RF15)                    | O usuário acessa seus agendamentos pendentes ou futuros e altera o horário ou serviço. O sistema atualiza os dados e exibe uma confirmação.                                                             |
| TA02.05 | Remoção de um agendamento pendente (RF16)                    | O usuário acessa seus agendamentos e escolhe cancelar um deles. O sistema remove o agendamento e exibe uma mensagem de sucesso.                                                                         |
| TA02.06 | Tentativa de editar agendamento já confirmado (RF15)         | O usuário tenta alterar um agendamento já confirmado pelo barbeiro. O sistema exibe uma mensagem de erro informando que alterações não são mais permitidas.                                             |
| TA02.07 | Tentativa de remover agendamento já realizado (RF16)         | O usuário tenta excluir um agendamento que já ocorreu. O sistema exibe uma mensagem informando que esse tipo de agendamento não pode mais ser removido.                                                 |

### User Story US03 - Disponibilizar Horário

|               |                                                                                                                                                            |
| ------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | O sistema deve conter a funcionalidade de cada barbeiro disponibilizar seus horários de atendimento para que os clientes consigam agendar nestes horários. |

| **Requisitos envolvidos** |                       |
| ------------------------- | :-------------------- |
| RF10                      | Listar Barbeadores    |
| RF13                      | Criar Agendamento     |
| RF14                      | Listar Agendamentos   |
| RF15                      | Atualizar Agendamento |
| RF16                      | Remover Agendamento   |
| RF22                      | Criar Horário         |
| RF23                      | Listar Horários       |
| RF24                      | Atualizar Horário     |
| RF25                      | Remover Horário       |

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

#### Testes de Aceitação

| Código  | Cenário                                                    | Descrição                                                                                                                                                                                                  |
| ------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA03.01 | Barbeiro visualiza interface de criação de horários (RF22) | O barbeiro acessa a tela de disponibilizar horário. O sistema exibe uma grade de horários/dias. O barbeiro seleciona os horários desejados e clica em "Salvar". O sistema confirma a criação dos horários. |
| TA03.02 | Barbeiro lista seus horários disponíveis (RF23)            | O barbeiro acessa a área "Meus Horários". O sistema exibe a lista de todos os horários cadastrados, com data, hora e status (disponível/indisponível/agendado).                                            |
| TA03.03 | Barbeiro atualiza horário específico (RF24)                | O barbeiro edita um horário específico (ex: muda de 14:00 para 15:00). O sistema salva a alteração e exibe mensagem de sucesso.                                                                            |
| TA03.04 | Barbeiro remove horário sem agendamento (RF25)             | O barbeiro tenta remover um horário ainda não agendado. O sistema exclui o horário e exibe confirmação da remoção.                                                                                         |
| TA03.05 | Barbeiro tenta remover horário com agendamento (RF25)      | O barbeiro tenta remover um horário que já possui agendamento. O sistema bloqueia a remoção e exibe uma mensagem informando que é necessário reagendar ou cancelar o agendamento antes.                    |
| TA03.06 | Barbeiro tenta alterar horário com agendamento (RF24)      | O barbeiro tenta editar um horário já agendado. O sistema exibe mensagem informando que a alteração impactará um agendamento existente e solicita confirmação ou bloqueia a ação.                          |
| TA03.07 | Cliente tenta agendar em horário removido (RF13/RF25)      | O cliente seleciona um horário que acabou de ser removido. Ao clicar em agendar, o sistema exibe mensagem: “Este horário não está mais disponível. Por favor, escolha outro.”                              |
| TA03.08 | Cliente vê agenda apenas com horários disponíveis (RF23)   | O cliente acessa a agenda de agendamentos. O sistema exibe apenas os horários cadastrados como "disponíveis" pelos barbeiros, excluindo os já ocupados ou removidos.                                       |
| TA03.09 | Verificar barbeiros disponíveis para horários (RF10)       | O cliente acessa um horário específico e o sistema exibe quais barbeiros estão disponíveis naquele período, com base nos horários que cada um disponibilizou.                                              |

### User Story US04 - Manter Serviços

|               |                                                                                                   |
| ------------- | :------------------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve ter a opção de cadastrar, ver, editar e alterar serviços fornecidos pelo barbeiro. |

| **Requisitos envolvidos** |                   |
| ------------------------- | :---------------- |
| RF01                      | Criar Serviço     |
| RF02                      | Listar Serviços   |
| RF03                      | Atualizar Serviço |
| RF04                      | Remover Serviço   |

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

#### Testes de Aceitação

| Código  | Cenário                                                      | Descrição                                                                                                                                                                                   |
| ------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA04.01 | Barbeiro cadastra novo serviço (RF01)                        | O barbeiro acessa a aba de "Cadastrar Serviço", preenche os campos obrigatórios (nome, descrição e preço) e confirma. O sistema salva e exibe mensagem: "Serviço cadastrado com sucesso".   |
| TA04.02 | Barbeiro visualiza todos os serviços cadastrados (RF02)      | O barbeiro acessa a aba de "Meus Serviços". O sistema exibe todos os serviços em formato de tabela com nome, descrição e preço.                                                             |
| TA04.03 | Barbeiro edita um serviço existente (RF03)                   | O barbeiro acessa um serviço da lista e clica em "Editar". Após atualizar os dados e confirmar, o sistema exibe mensagem: "Serviço atualizado com sucesso".                                 |
| TA04.04 | Barbeiro remove um serviço (RF04)                            | O barbeiro acessa a lista de serviços e clica em "Remover" em um serviço específico. O sistema solicita confirmação e, ao aceitar, exibe mensagem: "Serviço removido com sucesso".          |
| TA04.05 | Cliente acessa lista de serviços disponíveis (RF02)          | O cliente acessa a aba de serviços. O sistema exibe todos os serviços cadastrados, com nome, descrição e preço. Cliente não vê botões de editar, remover ou criar.                          |
| TA04.06 | Cliente seleciona um serviço para agendamento (RF02)         | O cliente, ao marcar um horário, acessa a lista de serviços. Ele seleciona um serviço desejado, e o sistema associa esse serviço ao agendamento em andamento.                               |
| TA04.07 | Barbeiro tenta cadastrar serviço sem preencher campos (RF01) | O barbeiro tenta cadastrar um serviço deixando campos obrigatórios em branco. O sistema exibe mensagens de erro de validação e impede o cadastro até que todos os campos sejam preenchidos. |
| TA04.08 | Barbeiro tenta remover serviço já agendado (RF04)            | O barbeiro tenta excluir um serviço vinculado a um agendamento futuro. O sistema exibe mensagem de erro informando que é necessário desvincular o serviço antes de excluí-lo.               |

### User Story US05 - Aprovar agendamentos

|               |                                                                                                                                                                                              |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | O sistema deve exigir a aprovação dos horários que forem reservados pelo cliente, podendo recusar e pedir alterações ou aprovar o horário e, assim, o processo de agendamento ser concluído. |

| **Requisitos envolvidos** |                       |
| ------------------------- | :-------------------- |
| RF13                      | Criar Agendamento     |
| RF17                      | Confirmar Atendimento |

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

#### Testes de Aceitação

| Código  | Cenário                                                                 | Descrição                                                                                                                                                                                                                                                               |
| ------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA05.01 | Barbeiro visualiza agendamentos pendentes (RF17)                        | O sistema notifica o barbeiro sobre um novo agendamento pendente. Ao acessar a aba de aprovações, o barbeiro vê uma lista com nome do cliente, serviço solicitado, forma de pagamento e horário agendado.                                                               |
| TA05.02 | Barbeiro aprova agendamento (RF17)                                      | O barbeiro acessa a lista de pendentes e clica em “Aprovar” em um dos agendamentos. O sistema confirma a aprovação e exibe a mensagem: “Agendamento confirmado com sucesso.”                                                                                            |
| TA05.03 | Barbeiro altera dados do agendamento antes de aprovar (RF17)            | O barbeiro clica em “Editar” em um agendamento pendente, modifica os campos necessários (como horário ou serviço) e, em seguida, aprova. O sistema registra a alteração e confirma a aprovação com os novos dados.                                                      |
| TA05.04 | Barbeiro recusa agendamento (RF17)                                      | O barbeiro opta por recusar o agendamento. O sistema apresenta um campo de texto obrigatório para justificar a recusa. Após preenchido e confirmado, o sistema envia a resposta ao cliente com a justificativa: “Agendamento recusado. Motivo: [mensagem do barbeiro]”. |
| TA05.05 | Barbeiro tenta aprovar agendamento com conflito de horário (RF13, RF17) | O barbeiro tenta aprovar um agendamento que conflita com outro já confirmado. O sistema bloqueia a ação e exibe a mensagem: “Horário indisponível. Verifique outro horário ou entre em contato com o cliente.”                                                          |
|  |

### User Story US06 - Manter pagamento

|               |                                                                                            |
| ------------- | :----------------------------------------------------------------------------------------- |
| **Descrição** | O sistema deve conter os recursos necessários para realizar o pagamento de um agendamento. |

| **Requisitos envolvidos** |                     |
| ------------------------- | :------------------ |
| RF22                      | Criar Pagamento     |
| RF23                      | Listar Pagamentos   |
| RF24                      | Atualizar Pagamento |
| RF25                      | Remover Pagamento   |

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

#### Testes de Aceitação

| Código  | Cenário                                            | Descrição                                                                                                                                                                                                                                                                                    |
| ------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA06.01 | Cliente realiza pagamento de um agendamento (RF22) | O cliente acessa um agendamento pendente e realiza o pagamento. Após a transação, o sistema confirma a operação com a mensagem: “Pagamento realizado com sucesso”, registra a data do pagamento e altera o status do agendamento para “Pago”. Em seguida, redireciona para a tela principal. |
| TA06.02 | Cliente consulta listagem de pagamentos (RF23)     | O cliente acessa a aba “Pagamentos” e vê todos os registros organizados por data. Cada item mostra detalhes do serviço pago, incluindo valor, data de realização, nome do serviço e status do pagamento.                                                                                     |
| TA06.03 | Cliente atualiza um pagamento incorreto (RF24)     | O cliente percebe um erro nas informações de um pagamento e solicita edição. O sistema permite alteração de campos permitidos (como forma de pagamento) e salva a modificação, mantendo o histórico da atualização.                                                                          |
| TA06.04 | Cliente remove um pagamento cancelado (RF25)       | O cliente acessa a listagem de pagamentos e seleciona um pagamento marcado como cancelado. O sistema exibe uma confirmação para remoção e, após a ação, o registro é excluído do histórico de pagamentos.                                                                                    |

### User Story US07 - Manter Barbeiro

|               |                                                               |
| ------------- | :------------------------------------------------------------ |
| **Descrição** | O sistema deve manter o cadastro e autenticação de barbeiros. |

| **Requisitos envolvidos** |                            |
| ------------------------- | :------------------------- |
| RF09                      | Criar Barbeador            |
| RF10                      | Listar Barbeadores         |
| RF11                      | Atualizar Barbeador        |
| RF12                      | Remover Barbeador          |
| RF18                      | Criar Conta de Usuário     |
| RF19                      | Verificar Sessão           |
| RF20                      | Atualizar Conta de Usuário |
| RF21                      | Remover Conta de Usuário   |

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

#### Testes de Aceitação

| Código  | Cenário                                             | Descrição                                                                                                                                                                                                                                            |
| ------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA07.01 | Cadastro de barbeiro com dados válidos (RF09, RF18) | Um barbeiro já cadastrado acessa o formulário de cadastro de um novo barbeiro. Ele preenche todos os campos corretamente e clica em “Enviar”. O sistema aceita os dados, cria o cadastro, autentica o usuário e redireciona para a página principal. |
| TA07.02 | Cadastro de barbeiro com dados inválidos (RF09)     | Um barbeiro acessa o formulário de cadastro de um novo barbeiro, mas preenche dados inválidos. Ao clicar em “Enviar”, o sistema exibe uma mensagem em vermelho informando que os dados não foram aceitos e o cadastro não é realizado.               |
| TA07.03 | Login com dados corretos (RF19)                     | Um barbeiro acessa o formulário de login, insere dados válidos e clica em “Entrar”. O sistema valida a sessão, autentica o usuário e redireciona para a área de barbeiros.                                                                           |
| TA07.04 | Login com dados incorretos (RF19)                   | Um barbeiro acessa o formulário de login e informa dados incorretos. O sistema exibe uma mensagem de erro e o usuário permanece na tela principal, sem ser autenticado.                                                                              |
| TA07.05 | Atualizar perfil de barbeiro (RF11, RF20)           | Um barbeiro logado acessa a tela de edição do perfil, altera seus dados (nome, e-mail etc.) e clica em “Salvar”. O sistema valida os dados, atualiza o cadastro e confirma a alteração com uma mensagem de sucesso.                                  |
| TA07.06 | Remover barbeiro e conta associada (RF12, RF21)     | Um barbeiro logado acessa a opção de exclusão de conta, confirma a remoção e o sistema deleta tanto o registro do barbeiro quanto a conta de usuário associada, redirecionando-o para a tela inicial com uma mensagem de confirmação.                |

### User Story US08 - Extrato de Pagamento

|               |                                                                                       |
| ------------- | :------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve possuir uma função que exibe os valores ganhos em um período de tempo. |

| **Requisitos envolvidos** |                   |
| ------------------------- | :---------------- |
| RF23                      | Listar Pagamentos |

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

#### Testes de Aceitação

| Código  | Cenário                                              | Descrição                                                                                                                                                                                                                                               |
| ------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TA08.01 | Filtrar pagamentos por período e quantidade (RF23)   | O barbeiro acessa a página de Pagamentos e utiliza os filtros disponíveis (ex: data inicial, data final, limite de resultados). O sistema processa a requisição e retorna um relatório com os pagamentos realizados no período e quantidade informados. |
| TA08.02 | Filtro de tempo anterior à criação do sistema (RF23) | O barbeiro acessa a página de Pagamentos, define um intervalo de tempo que antecede o primeiro pagamento registrado no sistema e clica em “Produzir Relatório”. O sistema exibe a mensagem: “Filtro de tempo excedido” e não retorna nenhum dado.       |
