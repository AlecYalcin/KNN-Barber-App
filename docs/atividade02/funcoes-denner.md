## Funções

1. **Verificar Horário Livre**

   - **Nome:** `verificar_horario_livre`
   - **Entrada:** CPF do barbeiro (`VARCHAR(11)`), data (`DATE`) e horário (`TIME`)
   - **Saída:** `BOOLEAN` (true se o horário estiver livre)
   - **Descrição:** Verifica se um determinado horário está livre para o barbeiro em uma data específica.

2. **Listar Horários do Dia**

   - **Nome:** `listar_horarios_dia`
   - **Entrada:** CPF do barbeiro (`VARCHAR(11)`) e data (`DATE`)
   - **Saída:** Tabela com colunas `horario (TIME)` e `disponivel (BOOLEAN)`
   - **Descrição:** Retorna todos os horários registrados na jornada do barbeiro para o dia informado, indicando se cada horário está disponível.

## Procedimentos

1. **Listar Agendamentos do Dia**

   - **Nome:** `listar_agendamentos_dia`
   - **Entrada:** Data (`DATE`)
   - **Ação:** Lista todos os agendamentos do dia especificado.
   - **Saída:** Exibe via `RAISE NOTICE` os dados de cada agendamento no formato: horário, nome do cliente e nome do barbeiro.

2. **Mostrar Barbeiros Disponíveis**

   - **Nome:** `mostrar_barbeiros_disponiveis`
   - **Entrada:** Data (`DATE`)
   - **Ação:** Lista os barbeiros com jornadas ativas na data informada.
   - **Saída:** Exibe via `RAISE NOTICE` o CPF e o nome de cada barbeiro disponível para o dia.
