-- Consulta 05: Clientes Frequentes (mais de 1 agendamento)
-- Por que é útil?
-- Permite identificar e fidelizar clientes mais ativos.

CREATE VIEW clientes_frequentes AS
SELECT
    u.nome,
    u.email,
    COUNT(*) AS total_agendamentos
FROM AGENDAMENTO a
JOIN USUARIO u ON u.email = a.cliente_email
GROUP BY u.nome, u.email
HAVING COUNT(*) > 1;