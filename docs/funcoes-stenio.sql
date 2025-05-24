-- Função 1: Contagem de Clientes por Barbeiro
CREATE OR REPLACE FUNCTION contar_clientes_barbeiro(
    p_cpf_barbeiro VARCHAR(11),
    p_mes INTEGER,
    p_ano INTEGER
) RETURNS INTEGER AS $$
DECLARE
    v_total INTEGER;
BEGIN
    SELECT COUNT(DISTINCT a.cliente_cpf)
    INTO v_total
    FROM agendamentos a
    WHERE a.barbeiro_cpf = p_cpf_barbeiro
    AND EXTRACT(MONTH FROM a.data) = p_mes
    AND EXTRACT(YEAR FROM a.data) = p_ano;
    
    RETURN v_total;
END;
$$ LANGUAGE plpgsql;

-- Função 2: Busca de Cliente por Telefone
CREATE OR REPLACE FUNCTION buscar_cliente_por_telefone(
    p_telefone VARCHAR(20)
) RETURNS VARCHAR(11) AS $$
DECLARE
    v_cpf VARCHAR(11);
BEGIN
    SELECT c.cpf INTO v_cpf
    FROM clientes c
    JOIN pessoas p ON c.cpf = p.cpf
    WHERE p.telefone = p_telefone;
    
    RETURN v_cpf;
END;
$$ LANGUAGE plpgsql;

-- Procedimento 1: Listar Serviços do Dia
CREATE OR REPLACE PROCEDURE listar_servicos_dia(
    p_data DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_servico RECORD;
BEGIN
    RAISE NOTICE 'Serviços agendados para o dia %:', p_data;
    
    FOR v_servico IN 
        SELECT a.horario, p.nome as cliente, b.nome as barbeiro, s.descricao
        FROM agendamentos a
        JOIN clientes c ON a.cliente_cpf = c.cpf
        JOIN pessoas p ON c.cpf = p.cpf
        JOIN barbeiros b ON a.barbeiro_cpf = b.cpf
        JOIN servicos s ON a.servico_id = s.id
        WHERE a.data = p_data
        ORDER BY a.horario
    LOOP
        RAISE NOTICE 'Horário: % - Cliente: % - Barbeiro: % - Serviço: %', 
            v_servico.horario, 
            v_servico.cliente,
            v_servico.barbeiro,
            v_servico.descricao;
    END LOOP;
END;
$$;

-- Procedimento 2: Mostrar Avaliações do Dia
CREATE OR REPLACE PROCEDURE mostrar_avaliacoes_dia(
    p_data DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_avaliacao RECORD;
BEGIN
    RAISE NOTICE 'Avaliações do dia %:', p_data;
    
    FOR v_avaliacao IN 
        SELECT a.nota, p.nome as cliente, b.nome as barbeiro, a.comentario
        FROM avaliacoes a
        JOIN clientes c ON a.cliente_cpf = c.cpf
        JOIN pessoas p ON c.cpf = p.cpf
        JOIN barbeiros b ON a.barbeiro_cpf = b.cpf
        WHERE a.data = p_data
        ORDER BY a.nota DESC
    LOOP
        RAISE NOTICE 'Nota: % - Cliente: % - Barbeiro: % - Comentário: %', 
            v_avaliacao.nota, 
            v_avaliacao.cliente,
            v_avaliacao.barbeiro,
            v_avaliacao.comentario;
    END LOOP;
END;
$$;

-- Exemplos de uso:

-- Função 1
SELECT contar_clientes_barbeiro('12345678900', 
    EXTRACT(MONTH FROM CURRENT_DATE)::INTEGER,
    EXTRACT(YEAR FROM CURRENT_DATE)::INTEGER);

-- Função 2
SELECT buscar_cliente_por_telefone('(11) 99999-9999');

-- Procedimento 1
CALL listar_servicos_dia(CURRENT_DATE);

-- Procedimento 2
CALL mostrar_avaliacoes_dia(CURRENT_DATE); 