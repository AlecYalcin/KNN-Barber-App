-- Consulta 04: Faturamento Total por Método de Pagamento
-- Por que é útil?
-- Ajuda a entender a preferência dos clientes por método de pagamento.

WITH total_por_metodo AS (
    SELECT
        m.metodo,
        SUM(p.valor) AS total
    FROM PAGAMENTO p
    JOIN METODO_DE_PAGAMENTO m ON m.id = p.metodo_id
    GROUP BY m.metodo
)
SELECT * FROM total_por_metodo ORDER BY total DESC;