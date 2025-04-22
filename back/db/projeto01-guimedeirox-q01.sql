--  Consulta 1: Serviços realizados por cada barbeiro, com total de agendamentos e valor recebido
-- Por que é interessante?
-- Porque te dá uma visão de desempenho por barbeiro — quais serviços ele mais executou e quanto faturou com isso. Útil para relatórios mensais, bonificações ou até análise de demanda.

SELECT
    u.nome AS barbeiro,
    s.nome AS servico,
    COUNT(a.id) AS total_agendamentos,
    COALESCE(SUM(p.valor), 0) AS total_recebido
FROM USUARIO u
JOIN AGENDAMENTO a ON u.email = a.barbeiro_email
JOIN SERVICO s ON a.servico_id = s.id
LEFT JOIN PAGAMENTO p ON p.agendamento_id = a.id
WHERE u.eh_barbeiro = TRUE
GROUP BY u.nome, s.nome
ORDER BY barbeiro, total_recebido DESC;

