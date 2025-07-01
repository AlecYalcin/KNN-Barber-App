-- Barbeiros com mais indisponibilidades nesta semana
-- Por que é útil?
-- Ajuda a identificar barbeiros menos disponíveis e ajustar a escala.

WITH indis_semana AS (
    SELECT
        usuario_email,
        COUNT(*) AS total_indisponibilidades
    FROM HORARIO_INDISPONIVEL
    WHERE horario_inicio >= date_trunc('week', CURRENT_DATE)
    GROUP BY usuario_email
)
SELECT
    u.nome,
    i.total_indisponibilidades
FROM indis_semana i
JOIN USUARIO u ON u.email = i.usuario_email
WHERE u.eh_barbeiro = TRUE
ORDER BY i.total_indisponibilidades DESC;