--Função 1
CREATE OR REPLACE FUNCTION verificar_horario_livre(
    p_cpf_barbeiro VARCHAR(11),
    p_data DATE,
    p_horario TIME
) RETURNS BOOLEAN AS $$
DECLARE
    v_livre BOOLEAN;
BEGIN
    SELECT NOT EXISTS (
        SELECT 1 
        FROM agendamentos a
        WHERE a.barbeiro_cpf = p_cpf_barbeiro
        AND a.data = p_data
        AND a.horario = p_horario
    ) INTO v_livre;
    
    RETURN v_livre;
END;
$$ LANGUAGE plpgsql;

-- Função 2
CREATE OR REPLACE FUNCTION listar_horarios_dia(
    p_cpf_barbeiro VARCHAR(11),
    p_data DATE
) RETURNS TABLE (
    horario TIME,
    disponivel BOOLEAN
) AS $$
BEGIN
    RETURN QUERY
    SELECT h.hora as horario, h.disponivel
    FROM jornadas j
    JOIN horarios h ON j.id = h.jornada_id
    WHERE j.barbeiro_cpf = p_cpf_barbeiro
    AND j.data = p_data
    ORDER BY h.hora;
END;
$$ LANGUAGE plpgsql;

-- Procedimento 1
CREATE OR REPLACE PROCEDURE listar_agendamentos_dia(
    p_data DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_agendamento RECORD;
BEGIN
    RAISE NOTICE 'Agendamentos do dia %:', p_data;
    
    FOR v_agendamento IN 
        SELECT a.horario, p.nome as cliente, b.nome as barbeiro
        FROM agendamentos a
        JOIN clientes c ON a.cliente_cpf = c.cpf
        JOIN pessoas p ON c.cpf = p.cpf
        JOIN barbeiros b ON a.barbeiro_cpf = b.cpf
        WHERE a.data = p_data
        ORDER BY a.horario
    LOOP
        RAISE NOTICE 'Horário: % - Cliente: % - Barbeiro: %', 
            v_agendamento.horario, 
            v_agendamento.cliente,
            v_agendamento.barbeiro;
    END LOOP;
END;
$$;
