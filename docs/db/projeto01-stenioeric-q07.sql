-- Consulta 07: Serviços Mais Vendidos
-- Por que é útil?
-- Ajuda a entender quais serviços são mais lucrativos e populares.

CREATE VIEW servicos_populares AS
SELECT
    s.nome,
    COUNT(*) AS vezes_realizado
FROM AGENDAMENTO a
JOIN SERVICO s ON s.id = a.servico_id
GROUP BY s.nome
ORDER BY vezes_realizado DESC;
