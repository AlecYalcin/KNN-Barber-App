-- Consulta 2: Barbeiros que possuem horários indisponíveis nas próximas 24 horas
-- Por que é interessante?
-- Porque te ajuda a antecipar indisponibilidades para reagendamento e controle de operação, evitando falhas no atendimento.

WITH indisponiveis_proximas AS (
    SELECT
        usuario_email,
        horario_inicio,
        horario_fim
    FROM HORARIO_INDISPONIVEL
    WHERE horario_inicio BETWEEN NOW() AND NOW() + INTERVAL '24 hours'
)
SELECT
    u.nome AS barbeiro,
    h.horario_inicio,
    h.horario_fim,
    h.justificativa
FROM indisponiveis_proximas h
JOIN USUARIO u ON u.email = h.usuario_email
WHERE u.eh_barbeiro = TRUE
ORDER BY h.horario_inicio;

