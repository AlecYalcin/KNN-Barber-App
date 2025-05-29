# Funções e Procedimentos do KNN Barber App

## Funções

### 1. Listar Barbeiros Disponíveis

- **Entrada:** `data` (DATE)
- **Saída:** Tabela com `cpf` (VARCHAR) e `nome` (VARCHAR)
- **Descrição:** Retorna uma lista de barbeiros que possuem jornada cadastrada para a data informada.

### 2. Verificar Jornada Existente

- **Entrada:** `cpf_barbeiro` (VARCHAR) e `data` (DATE)
- **Saída:** Boolean (`true`/`false`)
- **Descrição:** Verifica se existe uma jornada cadastrada para o barbeiro na data informada.

---

## Procedimentos

### 1. Listar Serviços por Barbeiro

- **Entrada:** `cpf_barbeiro` (VARCHAR) e `data` (DATE)
- **Ação:** Lista os serviços agendados para o barbeiro no dia especificado.
- **Saída:** Exibe os serviços via `RAISE NOTICE`, incluindo:
  - Horário do agendamento
  - Descrição do serviço
  - Nome do cliente

### 2. Mostrar Desempenho Diário

- **Entrada:** `cpf_barbeiro` (VARCHAR) e `data` (DATE)
- **Ação:** Exibe o desempenho diário do barbeiro.
- **Saída:** Exibe via `RAISE NOTICE`:
  - Total de serviços realizados
  - Média das avaliações recebidas no dia
