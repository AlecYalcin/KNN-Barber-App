Claro, Guilherme! Abaixo está a explicação em **Markdown** sobre cada uma das funções e procedimentos PL/pgSQL que você escreveu:

---

# 📘 Funções e Procedimentos em PL/pgSQL

Este documento descreve o propósito e funcionamento de cada uma das funções e procedimentos definidos para um sistema de agendamento em uma barbearia. O banco de dados contém informações sobre clientes, agendamentos, barbeiros e horários disponíveis.

---

## 🔍 Função 1: `verificar_cliente_existente`

```sql
CREATE OR REPLACE FUNCTION verificar_cliente_existente(p_cpf VARCHAR(11)) RETURNS BOOLEAN
```

### 📌 Descrição:

Esta função verifica se um cliente com determinado CPF já está cadastrado no sistema.

### ✅ Parâmetro:

* `p_cpf` (`VARCHAR(11)`): CPF do cliente a ser verificado.

### 🔄 Retorno:

* `TRUE` se o CPF for encontrado na tabela `clientes`.
* `FALSE` caso contrário.

### 📥 Exemplo de uso:

```sql
SELECT verificar_cliente_existente('12345678900');
```

---

## 🔎 Função 2: `buscar_cliente_por_nome`

```sql
CREATE OR REPLACE FUNCTION buscar_cliente_por_nome(p_nome VARCHAR(100)) RETURNS TABLE (cpf VARCHAR(11))
```

### 📌 Descrição:

Busca todos os CPFs dos clientes cujo nome contenha o texto informado (sem considerar maiúsculas/minúsculas).

### ✅ Parâmetro:

* `p_nome` (`VARCHAR(100)`): Parte do nome do cliente a ser buscado.

### 🔄 Retorno:

* Uma tabela contendo os CPFs dos clientes cujo nome corresponde ao critério de busca.

### 📥 Exemplo de uso:

```sql
SELECT * FROM buscar_cliente_por_nome('João');
```

---

## 📋 Procedimento 1: `listar_clientes_dia`

```sql
CREATE OR REPLACE PROCEDURE listar_clientes_dia(p_data DATE)
```

### 📌 Descrição:

Lista os clientes agendados para um determinado dia, exibindo o CPF, nome e telefone. A listagem é feita diretamente no console (usando `RAISE NOTICE`).

### ✅ Parâmetro:

* `p_data` (`DATE`): Data dos agendamentos a serem listados.

### 🔄 Saída:

* Mensagens de log com os dados dos clientes.

### 📥 Exemplo de uso:

```sql
CALL listar_clientes_dia(CURRENT_DATE);
```

---

## ⏰ Procedimento 2: `mostrar_horarios_livres`

```sql
CREATE OR REPLACE PROCEDURE mostrar_horarios_livres(p_data DATE)
```

### 📌 Descrição:

Exibe todos os horários disponíveis para agendamento em um dia específico, junto ao nome do barbeiro correspondente. A exibição é feita via `RAISE NOTICE`.

### ✅ Parâmetro:

* `p_data` (`DATE`): Data para a qual se deseja verificar os horários disponíveis.

### 🔄 Saída:

* Mensagens no console informando o horário e o barbeiro responsável.

### 📥 Exemplo de uso:

```sql
CALL mostrar_horarios_livres(CURRENT_DATE);
```

