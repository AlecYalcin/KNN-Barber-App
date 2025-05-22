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

-- Função 2: Lista de Horários do Dia
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
