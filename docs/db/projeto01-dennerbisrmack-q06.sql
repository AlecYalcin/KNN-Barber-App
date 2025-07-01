-- Consulta 06: Horas Totais Trabalhadas por Barbeiro
-- Por que é útil?
-- Mostra o esforço e carga de trabalho real por barbeiro.

WITH duracao_agendamentos AS (
    SELECT
        barbeiro_email,
        SUM(EXTRACT(EPOCH FROM (horario_fim - horario_inicio))/3600) AS horas_trabalhadas
    FROM AGENDAMENTO
    GROUP BY barbeiro_email
)
SELECT
    u.nome,
    d.horas_trabalhadas
FROM duracao_agendamentos d
JOIN USUARIO u ON u.email = d.barbeiro_email
ORDER BY d.horas_trabalhadas DESC;
