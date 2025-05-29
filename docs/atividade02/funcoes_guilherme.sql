-- Função 1: checagem de cliente existente
CREATE OR REPLACE FUNCTION verificar_cliente_existente(
    p_cpf VARCHAR(11)
) RETURNS BOOLEAN AS $$
DECLARE
    v_existe BOOLEAN;
BEGIN
    SELECT EXISTS (
        SELECT 1 
        FROM clientes 
        WHERE cpf = p_cpf
    ) INTO v_existe;
    
    RETURN v_existe;
END;
$$ LANGUAGE plpgsql;

-- Função 2: busca cliente por nome
CREATE OR REPLACE FUNCTION buscar_cliente_por_nome(
    p_nome VARCHAR(100)
) RETURNS TABLE (
    cpf VARCHAR(11)
) AS $$
BEGIN
    RETURN QUERY
    SELECT c.cpf
    FROM clientes c
    JOIN pessoas p ON c.cpf = p.cpf
    WHERE LOWER(p.nome) LIKE LOWER('%' || p_nome || '%');
END;
$$ LANGUAGE plpgsql;

-- Procedimento 1: listagem de clientes do dia
CREATE OR REPLACE PROCEDURE listar_clientes_dia(
    p_data DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_cliente RECORD;
BEGIN
    RAISE NOTICE 'Clientes agendados para o dia %:', p_data;
    
    FOR v_cliente IN 
        SELECT DISTINCT c.cpf, p.nome, p.telefone
        FROM agendamentos a
        JOIN clientes c ON a.cliente_cpf = c.cpf
        JOIN pessoas p ON c.cpf = p.cpf
        WHERE a.data = p_data
        ORDER BY p.nome
    LOOP
        RAISE NOTICE 'CPF: % - Nome: % - Telefone: %', 
            v_cliente.cpf, 
            v_cliente.nome,
            v_cliente.telefone;
    END LOOP;
END;
$$;

-- Procedimento 2: mostrar horarios lires
CREATE OR REPLACE PROCEDURE mostrar_horarios_livres(
    p_data DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_horario RECORD;
BEGIN
    RAISE NOTICE 'Horários livres para o dia %:', p_data;
    
    FOR v_horario IN 
        SELECT h.hora, b.nome as barbeiro
        FROM jornadas j
        JOIN horarios h ON j.id = h.jornada_id
        JOIN barbeiros b ON j.barbeiro_cpf = b.cpf
        JOIN pessoas p ON b.cpf = p.cpf
        WHERE j.data = p_data
        AND h.disponivel = true
        ORDER BY h.hora, p.nome
    LOOP
        RAISE NOTICE 'Horário: % - Barbeiro: %', 
            v_horario.hora, 
            v_horario.barbeiro;
    END LOOP;
END;
$$;

