-- Consulta 09: Gaps de Horários entre Agendamentos (por barbeiro)
-- Por que é útil?
-- Mostra espaços vagos entre atendimentos (possibilita encaixes).

WITH ags AS (
    SELECT
        a.barbeiro_email,
        a.horario_inicio,
        a.horario_fim,
        LEAD(a.horario_inicio) OVER (PARTITION BY a.barbeiro_email ORDER BY a.horario_inicio) AS proximo_inicio
    FROM AGENDAMENTO a
)
SELECT
    u.nome AS barbeiro,
    a.horario_fim AS fim_atual,
    a.proximo_inicio,
    EXTRACT(EPOCH FROM (a.proximo_inicio - a.horario_fim))/60 AS minutos_livres
FROM ags a
JOIN USUARIO u ON u.email = a.barbeiro_email
WHERE a.proximo_inicio IS NOT NULL
ORDER BY u.nome, a.horario_fim;
