# Documento de Visão

### Descrição do Projeto

O sistema de informação desenvolvido tem como foco ser utilizado pela Barbearia KN, no formato de um aplicativo de agendamento de horários. O software busca acima de tudo trazer a simplicidade para que o usuário, de forma intuitiva, consiga agendar os horários e o tipo de serviço que deseja dentre os oferecidos pela empresa.

Dentro da ideia de agendamento de horários, é importante destacar as funcionalidades principais deste módulo. Além da criação do horário de atendimento com nome e descrição, há a possibilidade de modificar os agendamentos manualmente ou até mesmo desmarcá-los caso haja necessidade. Por fim, os horários seguirão o padrão de Brasília, para evitar conflitos de fuso horário.

Ademais, o software pode ser uma ponte para uma nova forma de controle de pagamentos online, gerando também um relatório de contas referente aos lucros do mês com base em dados de clientes atendidos, assim facilitando a análise dos empresários sobre o empreendimento e as possíveis estratégias futuras.

****

### Histórico de Revisões

| Data       | Versão | Descrição               | Autor               |
|------------|--------|-------------------------|---------------------|
| 02/12/2024 | 1.0    | Criação do Documento    | Alec Can Yalcin     |
| 02/12/2024 | 1.1    | Definição de Equipe     | Júlio César         |
| 02/12/2024 | 1.2    | Definição dos Riscos    | Stênio Eric         |

****

### Equipe e Definição de Papéis

| Equipe            | Papel        | E-mail                     |
|-------------------|-------------|-----------------------------|
| Alec Can Yalcin  | Gerente, Desenvolvedor| alecyalcin@gmail.com       |
| Denner Bismarck  | Analista, Desenvolvedor| dennerbismarck@gmail.com  |
| Júlio César      | Desenvolvedor, Analista| juliocosta10@gmail.com    |
| Stênio Eric      | Testador, Analista| stenioeric1@gmail.com     |
| Guilherme Medeiros| Testador, Analista| guilherme.medeiros.706@ufrn.edu.br |

****

### Matriz de Competências

| Equipe            | Competências                                          |
|-------------------|-------------------------------------------------------|
| Alec Can Yalcin  | Desenvolvedor full-stack com Laravel, Django e Vue.js |
| Denner Bismarck  | Desenvolvedor back-end com Django, Node.js e PHP      |
| Júlio César      | Desenvolvedor front-end com Django, Vue.js e React    |
| Stênio Eric      | Desenvolvedor front-end com React, Node.js e Tailwind |
| Guilherme Medeiros  | Desenvolvedor back-end com Django, Java e PHP      |

---

## 3. Descrição Geral

### 3.1 Requisitos Funcionais

| Cod.  | Nome                  | Descrição                                                            | Categoria   |
|-------|------------------------|------------------------------------------------------------------------|------------|
| RF01  | Manter Serviços        | Funções de “CRUD” para serviços – Nome, Descrição, Média de preços.   | Essencial  |
| RF02  | Manter Cliente         | Funções de “CRUD” para clientes – Nome, CPF, Número.                  | Essencial  |
| RF03  | Manter Barbeador       | Funções de “CRUD” para Barbeadores - Nome, Número, horários de atendimento | Essencial  |
| RF04  | Manter Agendamentos    | Funções de “CRUD” para Agendamentos – Horário, Cliente, Serviço. Possibilidade de reagendamento. | Essencial  |
| RF05  | Confirmar Atendimento  | Sistema de aprovação e verificação dos atendimentos realizados ao dia, registrando se os pagamentos foram realizados ou não para cada atendimento. | Importante  |
| RF06  | Sistema de autenticação e login | Sistema de login para segurança. | Importante  |

### 3.2 Requisitos Não Funcionais

| Cod.  | Nome                    | Descrição |
|-------|-------------------------|-----------|
| RNF01 | Especificidade de layout | O software será web e seu layout deverá funcionar tanto em dispositivos móveis quanto em desktop. |
| RNF02 | Interface auto explicativa | Sua interface deverá conter “widgets” com nomes e ícones auto explicativos o suficiente para rápido entendimento. |
| RNF03 | Interface de uso rápido | Sua interface, principalmente para o administrador, deverá ser muito bem dividida em cada função, sendo suficiente apertar um ou dois botões para acessar cada tarefa. |
| RNF04 | Permissão de clientes não logados | Clientes não logados no sistema devem poder ter acesso somente aos horários disponíveis. |

---

## 3.3 Perfis de Usuário

| Perfil   | Descrição |
|----------|-----------|
| **Cliente**  | Usuário que utiliza os serviços do aplicativo. Pode ter diferentes níveis de familiaridade com tecnologia, então a interface deve ser intuitiva e de fácil uso. |
| **Barbeiro** | Atua como administrador da aplicação, podendo gerenciar serviços e acessar dados financeiros. Assim como o cliente, pode ter pouca experiência com tecnologia, então a usabilidade deve ser priorizada. |

---

## 3.4 Riscos

A tabela abaixo apresenta os riscos identificados para o início do projeto. Essa tabela será atualizada ao final de cada iteração na reunião de acompanhamento.  

| Data       | Risco                                                | Prioridade | Responsável  | Status      | Providência/Solução |
|------------|------------------------------------------------------|------------|--------------|------------|---------------------------------------------|
| 02/12/2024 | Dificuldade dos usuários em compreender a interface do aplicativo | Alta       | Desenvolvedor | Vigente    | Realizar testes de usabilidade com clientes da barbearia e ajustar a interface com base no feedback. |
| 02/12/2024 | Relatórios financeiros com dados inconsistentes ou atrasados | Média      | Desenvolvedor | Não iniciado | Validar a lógica de geração de relatórios e realizar testes com cenários reais de entrada antes da implantação. |
| 02/12/2024 | Resistência dos clientes à adoção do aplicativo | Baixa      | Cliente      | Não iniciado | Criar campanhas de conscientização e guias explicativos para os clientes sobre os benefícios do aplicativo. |

---

## 4. Referências

### Livros e Artigos Acadêmicos  
1. PRESSMAN, Roger S. **Engenharia de Software: uma abordagem profissional**. McGraw Hill Brasil, 2016.  
2. SOMMERVILLE, Ian. **Engenharia de Software**. Pearson, 2019.  
3. KRUG, Steve. **Não me faça pensar: Uma abordagem de bom senso à usabilidade na web e mobile**. Alta Books, 2014.  

### Normas e Diretrizes  
4. ISO 9241-210:2019. **Ergonomia da interação humano-sistema – Parte 210: Design centrado no ser humano para sistemas interativos**.  
5. IEEE 830-1998. **Recommended Practice for Software Requirements Specifications**.  

### Artigos e Materiais Online  
6. NIELSEN, Jakob. **10 Usability Heuristics for User Interface Design**. Nielsen Norman Group, 1994.  
   Disponível em: [https://www.nngroup.com/articles/ten-usability-heuristics/](https://www.nngroup.com/articles/ten-usability-heuristics/)  
7. PREECE, Jenny; ROGERS, Yvonne; SHARP, Helen. **Design de Interação: Além da interação humano-computador**. Bookman, 2013.  


