-- Função 1: Contagem de Agendamentos por Dia
CREATE OR REPLACE FUNCTION contar_agendamentos_dia(
    p_cpf_barbeiro VARCHAR(11),
    p_data DATE
) RETURNS INTEGER AS $$
DECLARE
    v_total INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO v_total
    FROM agendamentos a
    WHERE a.barbeiro_cpf = p_cpf_barbeiro
    AND a.data = p_data;
    
    RETURN v_total;
END;
$$ LANGUAGE plpgsql;

-- Função 2: Verificação de Barbeiro Ativo
CREATE OR REPLACE FUNCTION verificar_barbeiro_ativo(
    p_cpf VARCHAR(11)
) RETURNS BOOLEAN AS $$
DECLARE
    v_ativo BOOLEAN;
BEGIN
    SELECT EXISTS (
        SELECT 1 
        FROM barbeiros b
        JOIN pessoas p ON b.cpf = p.cpf
        WHERE b.cpf = p_cpf
    ) INTO v_ativo;
    
    RETURN v_ativo;
END;
$$ LANGUAGE plpgsql;

-- Procedimento 1: Listar Horários do Dia
CREATE OR REPLACE PROCEDURE listar_horarios_dia(
    p_cpf_barbeiro VARCHAR(11),
    p_data DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_horario RECORD;
BEGIN
    RAISE NOTICE 'Horários do dia % para o barbeiro %:', p_data, p_cpf_barbeiro;
    
    FOR v_horario IN 
        SELECT h.hora, h.disponivel
        FROM jornadas j
        JOIN horarios h ON j.id = h.jornada_id
        WHERE j.barbeiro_cpf = p_cpf_barbeiro
        AND j.data = p_data
        ORDER BY h.hora
    LOOP
        RAISE NOTICE 'Horário: % - Disponível: %', 
            v_horario.hora, 
            CASE WHEN v_horario.disponivel THEN 'Sim' ELSE 'Não' END;
    END LOOP;
END;
$$;

-- Procedimento 2: Mostrar Clientes do Dia
CREATE OR REPLACE PROCEDURE mostrar_clientes_dia(
    p_cpf_barbeiro VARCHAR(11),
    p_data DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_cliente RECORD;
BEGIN
    RAISE NOTICE 'Clientes agendados para o dia % com o barbeiro %:', p_data, p_cpf_barbeiro;
    
    FOR v_cliente IN 
        SELECT a.horario, p.nome, c.cpf
        FROM agendamentos a
        JOIN clientes c ON a.cliente_cpf = c.cpf
        JOIN pessoas p ON c.cpf = p.cpf
        WHERE a.barbeiro_cpf = p_cpf_barbeiro
        AND a.data = p_data
        ORDER BY a.horario
    LOOP
        RAISE NOTICE 'Horário: % - Cliente: % (CPF: %)', 
            v_cliente.horario, 
            v_cliente.nome, 
            v_cliente.cpf;
    END LOOP;
END;
$$;

-- Exemplos de uso:

-- Função 1
SELECT contar_agendamentos_dia('12345678900', CURRENT_DATE);

-- Função 2
SELECT verificar_barbeiro_ativo('12345678900');

-- Procedimento 1
CALL listar_horarios_dia('12345678900', CURRENT_DATE);

-- Procedimento 2
CALL mostrar_clientes_dia('12345678900', CURRENT_DATE); 