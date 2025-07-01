-- Consulta 08: Barbeiros com Jornadas Ativas Hoje
-- Por que é útil?
-- Permite identificar quem está trabalhando hoje.

WITH hoje AS (
    SELECT CURRENT_DATE AS data_hoje
)
SELECT
    u.nome AS barbeiro,
    j.horario_inicio,
    j.horario_fim
FROM JORNADA_DE_TRABALHO j
JOIN USUARIO u ON u.email = j.usuario_email
WHERE j.ativa = TRUE
AND DATE(j.horario_inicio) = (SELECT data_hoje FROM hoje);
