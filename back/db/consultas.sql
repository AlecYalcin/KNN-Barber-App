-- Agenda diária de um barbeiro
-- Esta consulta retorna todos os agendamentos de um barbeiro específico em uma data específica, incluindo informações sobre o cliente, serviço e forma de pagamento.

SELECT 
    a.horario_inicio,
    a.horario_fim,
    u.nome AS cliente,
    s.nome AS servico,
    s.preco,
    m.metodo AS forma_pagamento
FROM AGENDAMENTO a
JOIN USUARIO u ON a.cliente_email = u.email
JOIN SERVICO s ON a.servico_id = s.id
LEFT JOIN PAGAMENTO p ON a.id = p.agendamento_id
LEFT JOIN METODO_DE_PAGAMENTO m ON p.metodo_id = m.id
WHERE a.barbeiro_email = 'joao@email.com'
  AND DATE(a.horario_inicio) = '2025-04-23'
ORDER BY a.horario_inicio;


-- Agenda de um cliente
-- Esta consulta retorna todos os agendamentos de um cliente específico, incluindo informações sobre o barbeiro, serviço e forma de pagamento.
-- A consulta filtra os agendamentos pelo email do cliente e ordena os resultados pela data e hora de início do agendamento.
-- A consulta também inclui informações sobre o pagamento, se houver, e a forma de pagamento utilizada.

SELECT 
    a.horario_inicio,
    u.nome AS barbeiro,
    s.nome AS servico,
    s.preco,
    p.valor AS valor_pago,
    m.metodo AS forma_pagamento
FROM AGENDAMENTO a
JOIN USUARIO u ON a.barbeiro_email = u.email
JOIN SERVICO s ON a.servico_id = s.id
LEFT JOIN PAGAMENTO p ON a.id = p.agendamento_id
LEFT JOIN METODO_DE_PAGAMENTO m ON p.metodo_id = m.id
WHERE a.cliente_email = 'maria@email.com'
ORDER BY a.horario_inicio DESC;


-- Serviços mais populares
-- Esta consulta retorna os 5 serviços mais populares de um barbeiro específico em um determinado período, com base no número de agendamentos realizados.
-- A consulta filtra os agendamentos pelo email do barbeiro e pelo intervalo de datas especificado.
-- Os resultados são agrupados pelo nome do serviço, e a soma dos preços dos serviços é calculada para determinar a receita total gerada.

SELECT 
    s.nome,
    COUNT(*) AS total_agendamentos,
    SUM(s.preco) AS receita_total
FROM AGENDAMENTO a
JOIN SERVICO s ON a.servico_id = s.id
WHERE a.barbeiro_email = 'joao@email.com'
  AND a.horario_inicio BETWEEN '2025-04-01' AND '2025-04-30'
GROUP BY s.nome
ORDER BY total_agendamentos DESC
LIMIT 5;


-- Clientes mais frequentes
-- Esta consulta retorna os 10 clientes mais frequentes de um barbeiro específico, com base no número total de agendamentos realizados.
-- A consulta filtra os agendamentos pelo email do barbeiro e agrupa os resultados pelo nome e telefone do cliente.
-- A soma dos valores pagos pelos clientes também é calculada.

SELECT 
    u.nome,
    u.telefone,
    COUNT(*) AS total_agendamentos,
    SUM(p.valor) AS total_gasto
FROM AGENDAMENTO a
JOIN USUARIO u ON a.cliente_email = u.email
JOIN PAGAMENTO p ON a.id = p.agendamento_id
WHERE a.barbeiro_email = 'joao@email.com'
GROUP BY u.nome, u.telefone
ORDER BY total_agendamentos DESC
LIMIT 10;


-- Jornada de trabalho
-- Esta consulta retorna a jornada de trabalho de um barbeiro específico, incluindo os horários de início, pausa, retorno e fim de cada dia da semana.
-- A consulta filtra os resultados pelo email do barbeiro e ordena os dias da semana.

SELECT 
    d.dia,
    j.horario_inicio::time AS inicio,
    j.horario_pausa::time AS pausa,
    j.horario_retorno::time AS retorno,
    j.horario_fim::time AS fim
FROM JORNADA_DE_TRABALHO j
JOIN DIA_DA_SEMANA d ON j.id = d.jornada_id
WHERE j.usuario_email = 'joao@email.com'
ORDER BY 
    CASE d.dia
        WHEN 'Segunda-feira' THEN 1
        WHEN 'Terça-feira' THEN 2
        WHEN 'Quarta-feira' THEN 3
        WHEN 'Quinta-feira' THEN 4
        WHEN 'Sexta-feira' THEN 5
        WHEN 'Sábado' THEN 6
        WHEN 'Domingo' THEN 7
    END;


-- Métodos de pagamento mais utilizados
-- Esta consulta retorna os métodos de pagamento mais utilizados por um barbeiro específico, com base no número total de utilizações e o valor total recebido.
-- A consulta filtra os pagamentos pelo email do barbeiro e agrupa os resultados pelo método de pagamento.

SELECT 
    m.metodo,
    COUNT(*) AS total_utilizacoes,
    SUM(p.valor) AS valor_total
FROM PAGAMENTO p
JOIN METODO_DE_PAGAMENTO m ON p.metodo_id = m.id
JOIN AGENDAMENTO a ON p.agendamento_id = a.id
WHERE a.barbeiro_email = 'joao@email.com'
GROUP BY m.metodo
ORDER BY total_utilizacoes DESC;