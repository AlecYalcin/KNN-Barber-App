-- Função 1: Listar Barbeiros Disponíveis
CREATE OR REPLACE FUNCTION listar_barbeiros_disponiveis(
    p_data DATE
) RETURNS TABLE (
    cpf VARCHAR(11),
    nome VARCHAR(100)
) AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT b.cpf, p.nome
    FROM barbeiros b
    JOIN pessoas p ON b.cpf = p.cpf
    JOIN jornadas j ON b.cpf = j.barbeiro_cpf
    WHERE j.data = p_data
    ORDER BY p.nome;
END;
$$ LANGUAGE plpgsql;

-- Função 2: Verificar Jornada Existente
CREATE OR REPLACE FUNCTION verificar_jornada_existente(
    p_cpf_barbeiro VARCHAR(11),
    p_data DATE
) RETURNS BOOLEAN AS $$
DECLARE
    v_existe BOOLEAN;
BEGIN
    SELECT EXISTS (
        SELECT 1 
        FROM jornadas 
        WHERE barbeiro_cpf = p_cpf_barbeiro
        AND data = p_data
    ) INTO v_existe;
    
    RETURN v_existe;
END;
$$ LANGUAGE plpgsql;

-- Procedimento 1: Listar Serviços por Barbeiro
CREATE OR REPLACE PROCEDURE listar_servicos_barbeiro(
    p_cpf_barbeiro VARCHAR(11),
    p_data DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_servico RECORD;
BEGIN
    RAISE NOTICE 'Serviços do barbeiro % para o dia %:', p_cpf_barbeiro, p_data;
    
    FOR v_servico IN 
        SELECT a.horario, s.descricao, p.nome as cliente
        FROM agendamentos a
        JOIN servicos s ON a.servico_id = s.id
        JOIN clientes c ON a.cliente_cpf = c.cpf
        JOIN pessoas p ON c.cpf = p.cpf
        WHERE a.barbeiro_cpf = p_cpf_barbeiro
        AND a.data = p_data
        ORDER BY a.horario
    LOOP
        RAISE NOTICE 'Horário: % - Serviço: % - Cliente: %', 
            v_servico.horario, 
            v_servico.descricao,
            v_servico.cliente;
    END LOOP;
END;
$$;

-- Procedimento 2: Mostrar Desempenho Diário
CREATE OR REPLACE PROCEDURE mostrar_desempenho_diario(
    p_cpf_barbeiro VARCHAR(11),
    p_data DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_total_servicos INTEGER;
    v_media_avaliacoes NUMERIC;
BEGIN
    -- Contar total de serviços
    SELECT COUNT(*)
    INTO v_total_servicos
    FROM agendamentos
    WHERE barbeiro_cpf = p_cpf_barbeiro
    AND data = p_data;
    
    -- Calcular média das avaliações
    SELECT COALESCE(AVG(nota), 0)
    INTO v_media_avaliacoes
    FROM avaliacoes
    WHERE barbeiro_cpf = p_cpf_barbeiro
    AND data = p_data;
    
    RAISE NOTICE 'Desempenho do barbeiro % para o dia %:', p_cpf_barbeiro, p_data;
    RAISE NOTICE 'Total de serviços realizados: %', v_total_servicos;
    RAISE NOTICE 'Média das avaliações: %', ROUND(v_media_avaliacoes, 2);
END;
$$;

-- Exemplos de uso:

-- Função 1
SELECT * FROM listar_barbeiros_disponiveis(CURRENT_DATE);

-- Função 2
SELECT verificar_jornada_existente('12345678900', CURRENT_DATE);

-- Procedimento 1
CALL listar_servicos_barbeiro('12345678900', CURRENT_DATE);

-- Procedimento 2
CALL mostrar_desempenho_diario('12345678900', CURRENT_DATE); 