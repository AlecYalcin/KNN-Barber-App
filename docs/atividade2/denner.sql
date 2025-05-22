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