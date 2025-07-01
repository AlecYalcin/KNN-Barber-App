-- Consulta 3: Agenda Completa dos Barbeiros
-- Por que é útil?
-- Permite consultar rapidamente a agenda completa de qualquer barbeiro com cliente e serviço.

CREATE VIEW agenda_barbeiros AS
SELECT
    u.nome AS barbeiro,
    a.horario_inicio,
    a.horario_fim,
    s.nome AS servico,
    cli.nome AS cliente
FROM AGENDAMENTO a
JOIN USUARIO u ON u.email = a.barbeiro_email
JOIN USUARIO cli ON cli.email = a.cliente_email
JOIN SERVICO s ON s.id = a.servico_id
WHERE u.eh_barbeiro = TRUE;
