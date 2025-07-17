-- Script de inicialização do banco de dados da Barbearia KNN
-- Este script será executado automaticamente quando o container PostgreSQL for criado pela primeira vez

-- =====================================================
-- CRIAÇÃO DAS TABELAS
-- =====================================================

-- Criar enum para dia da semana
CREATE TYPE dia_da_semana AS ENUM ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo');

-- Criar enum para método de pagamento
CREATE TYPE metodo_pagamento AS ENUM ('Dinheiro', 'Cartão', 'PIX');

-- Tabela de usuários
CREATE TABLE IF NOT EXISTS usuario (
    cpf VARCHAR PRIMARY KEY,
    nome VARCHAR NOT NULL,
    senha VARCHAR NOT NULL,
    telefone VARCHAR,
    email VARCHAR NOT NULL UNIQUE,
    eh_barbeiro BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Tabela de serviços
CREATE TABLE IF NOT EXISTS servico (
    id VARCHAR PRIMARY KEY,
    nome VARCHAR NOT NULL,
    descricao VARCHAR,
    preco FLOAT NOT NULL,
    duracao INTEGER NOT NULL DEFAULT 30,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Tabela de jornadas
CREATE TABLE IF NOT EXISTS jornada (
    id VARCHAR PRIMARY KEY,
    ativa BOOLEAN DEFAULT TRUE,
    horario_inicio TIME NOT NULL,
    horario_pausa TIME,
    horario_retorno TIME,
    horario_fim TIME NOT NULL,
    dia_da_semana dia_da_semana NOT NULL,
    barbeiro_cpf VARCHAR REFERENCES usuario(cpf) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Tabela de horários indisponíveis
CREATE TABLE IF NOT EXISTS horario_indisponivel (
    id VARCHAR PRIMARY KEY,
    horario_inicio TIMESTAMP NOT NULL,
    horario_fim TIMESTAMP NOT NULL,
    justificativa VARCHAR,
    barbeiro_cpf VARCHAR REFERENCES usuario(cpf) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Tabela de agendamentos
CREATE TABLE IF NOT EXISTS agendamento (
    id VARCHAR PRIMARY KEY,
    horario_inicio TIMESTAMP NOT NULL,
    horario_fim TIMESTAMP NOT NULL,
    barbeiro_cpf VARCHAR REFERENCES usuario(cpf) ON DELETE SET NULL,
    cliente_cpf VARCHAR REFERENCES usuario(cpf) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Tabela de relacionamento entre agendamentos e serviços
CREATE TABLE IF NOT EXISTS servicos_do_agendamento (
    agendamento VARCHAR REFERENCES agendamento(id) ON DELETE CASCADE,
    servico VARCHAR REFERENCES servico(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (agendamento, servico)
);

-- Tabela de pagamentos
CREATE TABLE IF NOT EXISTS pagamento (
    id VARCHAR PRIMARY KEY,
    valor FLOAT NOT NULL,
    data TIMESTAMP NOT NULL,
    metodo metodo_pagamento NOT NULL,
    agendamento_id VARCHAR REFERENCES agendamento(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- =====================================================
-- VERIFICAÇÃO SE OS DADOS JÁ EXISTEM
-- =====================================================

DO $$
BEGIN
    -- Verifica se já existem usuários no banco
    IF EXISTS (SELECT 1 FROM usuario LIMIT 1) THEN
        RAISE NOTICE 'Dados já existem no banco. Pulando inserção.';
        RETURN;
    END IF;
END $$;

-- =====================================================
-- INSERÇÃO DE USUÁRIOS (CLIENTES E BARBEIROS)
-- =====================================================

-- Barbeiros
INSERT INTO usuario (cpf, nome, senha, telefone, email, eh_barbeiro, created_at, updated_at) VALUES
('12345678901', 'João Silva', '123456', '(11) 99999-1111', 'joao.silva@barbearia.com', true, NOW(), NOW()),
('23456789012', 'Pedro Santos', '123456', '(11) 99999-2222', 'pedro.santos@barbearia.com', true, NOW(), NOW()),
('34567890123', 'Carlos Oliveira', '123456', '(11) 99999-3333', 'carlos.oliveira@barbearia.com', true, NOW(), NOW()),
('45678901234', 'Roberto Costa', '123456', '(11) 99999-4444', 'roberto.costa@barbearia.com', true, NOW(), NOW());

-- Clientes
INSERT INTO usuario (cpf, nome, senha, telefone, email, eh_barbeiro, created_at, updated_at) VALUES
('56789012345', 'Lucas Mendes', '123456', '(11) 98888-1111', 'lucas.mendes@email.com', false, NOW(), NOW()),
('67890123456', 'Gabriel Alves', '123456', '(11) 98888-2222', 'gabriel.alves@email.com', false, NOW(), NOW()),
('78901234567', 'Rafael Lima', '123456', '(11) 98888-3333', 'rafael.lima@email.com', false, NOW(), NOW()),
('89012345678', 'Bruno Ferreira', '123456', '(11) 98888-4444', 'bruno.ferreira@email.com', false, NOW(), NOW()),
('90123456789', 'Thiago Rodrigues', '123456', '(11) 98888-5555', 'thiago.rodrigues@email.com', false, NOW(), NOW()),
('01234567890', 'Marcos Pereira', '123456', '(11) 98888-6666', 'marcos.pereira@email.com', false, NOW(), NOW()),
('11122233344', 'André Souza', '123456', '(11) 98888-7777', 'andre.souza@email.com', false, NOW(), NOW()),
('22233344455', 'Felipe Martins', '123456', '(11) 98888-8888', 'felipe.martins@email.com', false, NOW(), NOW());

-- =====================================================
-- INSERÇÃO DE SERVIÇOS
-- =====================================================

INSERT INTO servico (id, nome, descricao, preco, duracao, created_at, updated_at) VALUES
('corte-masculino', 'Corte Masculino', 'Corte tradicional masculino com acabamento', 35.00, 30, NOW(), NOW()),
('barba', 'Barba', 'Fazer a barba com navalha e produtos profissionais', 25.00, 20, NOW(), NOW()),
('corte-barba', 'Corte + Barba', 'Corte masculino completo com barba', 50.00, 45, NOW(), NOW()),
('pigmentacao', 'Pigmentação', 'Pigmentação de cabelo ou barba', 40.00, 60, NOW(), NOW()),
('hidratacao', 'Hidratação', 'Tratamento hidratante para cabelo', 30.00, 30, NOW(), NOW()),
('selagem', 'Selagem', 'Selagem capilar para cabelos crespos', 80.00, 90, NOW(), NOW()),
('luzes', 'Luzes', 'Aplicação de luzes no cabelo', 70.00, 75, NOW(), NOW()),
('sombrancelha', 'Sobrancelha', 'Design e manutenção de sobrancelha', 15.00, 15, NOW(), NOW());

-- =====================================================
-- INSERÇÃO DE JORNADAS DE TRABALHO
-- =====================================================

-- Jornadas do João Silva (Segunda a Sexta)
INSERT INTO jornada (id, ativa, horario_inicio, horario_pausa, horario_retorno, horario_fim, dia_da_semana, barbeiro_cpf, created_at, updated_at) VALUES
('jornada-joao-segunda', true, '08:00:00', '12:00:00', '13:00:00', '18:00:00', 'Segunda', '12345678901', NOW(), NOW()),
('jornada-joao-terca', true, '08:00:00', '12:00:00', '13:00:00', '18:00:00', 'Terça', '12345678901', NOW(), NOW()),
('jornada-joao-quarta', true, '08:00:00', '12:00:00', '13:00:00', '18:00:00', 'Quarta', '12345678901', NOW(), NOW()),
('jornada-joao-quinta', true, '08:00:00', '12:00:00', '13:00:00', '18:00:00', 'Quinta', '12345678901', NOW(), NOW()),
('jornada-joao-sexta', true, '08:00:00', '12:00:00', '13:00:00', '18:00:00', 'Sexta', '12345678901', NOW(), NOW()),
('jornada-joao-sabado', true, '08:00:00', NULL, NULL, '16:00:00', 'Sábado', '12345678901', NOW(), NOW());

-- Jornadas do Pedro Santos (Terça a Sábado)
INSERT INTO jornada (id, ativa, horario_inicio, horario_pausa, horario_retorno, horario_fim, dia_da_semana, barbeiro_cpf, created_at, updated_at) VALUES
('jornada-pedro-terca', true, '09:00:00', '12:00:00', '13:00:00', '19:00:00', 'Terça', '23456789012', NOW(), NOW()),
('jornada-pedro-quarta', true, '09:00:00', '12:00:00', '13:00:00', '19:00:00', 'Quarta', '23456789012', NOW(), NOW()),
('jornada-pedro-quinta', true, '09:00:00', '12:00:00', '13:00:00', '19:00:00', 'Quinta', '23456789012', NOW(), NOW()),
('jornada-pedro-sexta', true, '09:00:00', '12:00:00', '13:00:00', '19:00:00', 'Sexta', '23456789012', NOW(), NOW()),
('jornada-pedro-sabado', true, '09:00:00', NULL, NULL, '17:00:00', 'Sábado', '23456789012', NOW(), NOW());

-- Jornadas do Carlos Oliveira (Segunda a Sexta)
INSERT INTO jornada (id, ativa, horario_inicio, horario_pausa, horario_retorno, horario_fim, dia_da_semana, barbeiro_cpf, created_at, updated_at) VALUES
('jornada-carlos-segunda', true, '10:00:00', '14:00:00', '15:00:00', '20:00:00', 'Segunda', '34567890123', NOW(), NOW()),
('jornada-carlos-terca', true, '10:00:00', '14:00:00', '15:00:00', '20:00:00', 'Terça', '34567890123', NOW(), NOW()),
('jornada-carlos-quarta', true, '10:00:00', '14:00:00', '15:00:00', '20:00:00', 'Quarta', '34567890123', NOW(), NOW()),
('jornada-carlos-quinta', true, '10:00:00', '14:00:00', '15:00:00', '20:00:00', 'Quinta', '34567890123', NOW(), NOW()),
('jornada-carlos-sexta', true, '10:00:00', '14:00:00', '15:00:00', '20:00:00', 'Sexta', '34567890123', NOW(), NOW());

-- Jornadas do Roberto Costa (Quarta a Domingo)
INSERT INTO jornada (id, ativa, horario_inicio, horario_pausa, horario_retorno, horario_fim, dia_da_semana, barbeiro_cpf, created_at, updated_at) VALUES
('jornada-roberto-quarta', true, '11:00:00', '15:00:00', '16:00:00', '21:00:00', 'Quarta', '45678901234', NOW(), NOW()),
('jornada-roberto-quinta', true, '11:00:00', '15:00:00', '16:00:00', '21:00:00', 'Quinta', '45678901234', NOW(), NOW()),
('jornada-roberto-sexta', true, '11:00:00', '15:00:00', '16:00:00', '21:00:00', 'Sexta', '45678901234', NOW(), NOW()),
('jornada-roberto-sabado', true, '11:00:00', NULL, NULL, '19:00:00', 'Sábado', '45678901234', NOW(), NOW()),
('jornada-roberto-domingo', true, '10:00:00', NULL, NULL, '16:00:00', 'Domingo', '45678901234', NOW(), NOW());

-- =====================================================
-- INSERÇÃO DE HORÁRIOS INDISPONÍVEIS
-- =====================================================

-- João Silva - Férias
INSERT INTO horario_indisponivel (id, horario_inicio, horario_fim, justificativa, barbeiro_cpf, created_at, updated_at) VALUES
('ferias-joao-1', '2024-12-20 08:00:00', '2024-12-31 18:00:00', 'Férias de fim de ano', '12345678901', NOW(), NOW()),
('ferias-joao-2', '2024-07-15 08:00:00', '2024-07-30 18:00:00', 'Férias de julho', '12345678901', NOW(), NOW());

-- Pedro Santos - Consulta médica
INSERT INTO horario_indisponivel (id, horario_inicio, horario_fim, justificativa, barbeiro_cpf, created_at, updated_at) VALUES
('consulta-pedro', '2024-03-15 14:00:00', '2024-03-15 16:00:00', 'Consulta médica', '23456789012', NOW(), NOW()),
('ferias-pedro', '2024-08-10 09:00:00', '2024-08-25 19:00:00', 'Férias de agosto', '23456789012', NOW(), NOW());

-- Carlos Oliveira - Evento familiar
INSERT INTO horario_indisponivel (id, horario_inicio, horario_fim, justificativa, barbeiro_cpf, created_at, updated_at) VALUES
('evento-carlos', '2024-04-20 10:00:00', '2024-04-20 20:00:00', 'Casamento do irmão', '34567890123', NOW(), NOW()),
('ferias-carlos', '2024-09-05 10:00:00', '2024-09-20 20:00:00', 'Férias de setembro', '34567890123', NOW(), NOW());

-- Roberto Costa - Viagem
INSERT INTO horario_indisponivel (id, horario_inicio, horario_fim, justificativa, barbeiro_cpf, created_at, updated_at) VALUES
('viagem-roberto', '2024-05-10 11:00:00', '2024-05-15 21:00:00', 'Viagem de negócios', '45678901234', NOW(), NOW()),
('ferias-roberto', '2024-10-12 11:00:00', '2024-10-27 21:00:00', 'Férias de outubro', '45678901234', NOW(), NOW());

-- =====================================================
-- INSERÇÃO DE AGENDAMENTOS
-- =====================================================

-- Agendamentos para a próxima semana (exemplo)
INSERT INTO agendamento (id, horario_inicio, horario_fim, barbeiro_cpf, cliente_cpf, created_at, updated_at) VALUES
-- Segunda-feira
('agend-001', '2024-03-18 09:00:00', '2024-03-18 09:30:00', '12345678901', '56789012345', NOW(), NOW()),
('agend-002', '2024-03-18 10:00:00', '2024-03-18 10:45:00', '12345678901', '67890123456', NOW(), NOW()),
('agend-003', '2024-03-18 11:00:00', '2024-03-18 11:30:00', '12345678901', '78901234567', NOW(), NOW()),
('agend-004', '2024-03-18 14:00:00', '2024-03-18 14:45:00', '12345678901', '89012345678', NOW(), NOW()),
('agend-005', '2024-03-18 15:00:00', '2024-03-18 15:30:00', '12345678901', '90123456789', NOW(), NOW()),

-- Terça-feira
('agend-006', '2024-03-19 09:00:00', '2024-03-19 09:45:00', '23456789012', '01234567890', NOW(), NOW()),
('agend-007', '2024-03-19 10:00:00', '2024-03-19 10:30:00', '23456789012', '11122233344', NOW(), NOW()),
('agend-008', '2024-03-19 11:00:00', '2024-03-19 11:45:00', '23456789012', '22233344455', NOW(), NOW()),
('agend-009', '2024-03-19 14:00:00', '2024-03-19 14:30:00', '23456789012', '56789012345', NOW(), NOW()),
('agend-010', '2024-03-19 15:00:00', '2024-03-19 15:45:00', '23456789012', '67890123456', NOW(), NOW()),

-- Quarta-feira
('agend-011', '2024-03-20 10:00:00', '2024-03-20 10:30:00', '34567890123', '78901234567', NOW(), NOW()),
('agend-012', '2024-03-20 11:00:00', '2024-03-20 11:45:00', '34567890123', '89012345678', NOW(), NOW()),
('agend-013', '2024-03-20 14:00:00', '2024-03-20 14:30:00', '34567890123', '90123456789', NOW(), NOW()),
('agend-014', '2024-03-20 15:00:00', '2024-03-20 15:45:00', '34567890123', '01234567890', NOW(), NOW()),
('agend-015', '2024-03-20 16:00:00', '2024-03-20 16:30:00', '34567890123', '11122233344', NOW(), NOW()),

-- Quinta-feira
('agend-016', '2024-03-21 11:00:00', '2024-03-21 11:30:00', '45678901234', '22233344455', NOW(), NOW()),
('agend-017', '2024-03-21 12:00:00', '2024-03-21 12:45:00', '45678901234', '56789012345', NOW(), NOW()),
('agend-018', '2024-03-21 14:00:00', '2024-03-21 14:30:00', '45678901234', '67890123456', NOW(), NOW()),
('agend-019', '2024-03-21 15:00:00', '2024-03-21 15:45:00', '45678901234', '78901234567', NOW(), NOW()),
('agend-020', '2024-03-21 16:00:00', '2024-03-21 16:30:00', '45678901234', '89012345678', NOW(), NOW()),

-- Sexta-feira
('agend-021', '2024-03-22 08:00:00', '2024-03-22 08:30:00', '12345678901', '90123456789', NOW(), NOW()),
('agend-022', '2024-03-22 09:00:00', '2024-03-22 09:45:00', '12345678901', '01234567890', NOW(), NOW()),
('agend-023', '2024-03-22 10:00:00', '2024-03-22 10:30:00', '12345678901', '11122233344', NOW(), NOW()),
('agend-024', '2024-03-22 14:00:00', '2024-03-22 14:45:00', '12345678901', '22233344455', NOW(), NOW()),
('agend-025', '2024-03-22 15:00:00', '2024-03-22 15:30:00', '12345678901', '56789012345', NOW(), NOW()),

-- Sábado
('agend-026', '2024-03-23 08:00:00', '2024-03-23 08:30:00', '12345678901', '67890123456', NOW(), NOW()),
('agend-027', '2024-03-23 09:00:00', '2024-03-23 09:45:00', '12345678901', '78901234567', NOW(), NOW()),
('agend-028', '2024-03-23 10:00:00', '2024-03-23 10:30:00', '12345678901', '89012345678', NOW(), NOW()),
('agend-029', '2024-03-23 11:00:00', '2024-03-23 11:45:00', '12345678901', '90123456789', NOW(), NOW()),
('agend-030', '2024-03-23 12:00:00', '2024-03-23 12:30:00', '12345678901', '01234567890', NOW(), NOW()),
('agend-031', '2024-03-23 09:00:00', '2024-03-23 09:45:00', '23456789012', '11122233344', NOW(), NOW()),
('agend-032', '2024-03-23 10:00:00', '2024-03-23 10:30:00', '23456789012', '22233344455', NOW(), NOW()),
('agend-033', '2024-03-23 11:00:00', '2024-03-23 11:45:00', '23456789012', '56789012345', NOW(), NOW()),
('agend-034', '2024-03-23 12:00:00', '2024-03-23 12:30:00', '23456789012', '67890123456', NOW(), NOW()),
('agend-035', '2024-03-23 13:00:00', '2024-03-23 13:45:00', '23456789012', '78901234567', NOW(), NOW()),
('agend-036', '2024-03-23 11:00:00', '2024-03-23 11:30:00', '45678901234', '89012345678', NOW(), NOW()),
('agend-037', '2024-03-23 12:00:00', '2024-03-23 12:45:00', '45678901234', '90123456789', NOW(), NOW()),
('agend-038', '2024-03-23 13:00:00', '2024-03-23 13:30:00', '45678901234', '01234567890', NOW(), NOW()),
('agend-039', '2024-03-23 14:00:00', '2024-03-23 14:45:00', '45678901234', '11122233344', NOW(), NOW()),
('agend-040', '2024-03-23 15:00:00', '2024-03-23 15:30:00', '45678901234', '22233344455', NOW(), NOW());

-- =====================================================
-- INSERÇÃO DE SERVIÇOS DOS AGENDAMENTOS
-- =====================================================

-- Agendamentos com corte masculino
INSERT INTO servicos_do_agendamento (agendamento, servico, created_at, updated_at) VALUES
('agend-001', 'corte-masculino', NOW(), NOW()),
('agend-002', 'corte-barba', NOW(), NOW()),
('agend-003', 'corte-masculino', NOW(), NOW()),
('agend-004', 'corte-barba', NOW(), NOW()),
('agend-005', 'corte-masculino', NOW(), NOW()),
('agend-006', 'corte-barba', NOW(), NOW()),
('agend-007', 'corte-masculino', NOW(), NOW()),
('agend-008', 'corte-barba', NOW(), NOW()),
('agend-009', 'corte-masculino', NOW(), NOW()),
('agend-010', 'corte-barba', NOW(), NOW()),
('agend-011', 'corte-masculino', NOW(), NOW()),
('agend-012', 'corte-barba', NOW(), NOW()),
('agend-013', 'corte-masculino', NOW(), NOW()),
('agend-014', 'corte-barba', NOW(), NOW()),
('agend-015', 'corte-masculino', NOW(), NOW()),
('agend-016', 'corte-masculino', NOW(), NOW()),
('agend-017', 'corte-barba', NOW(), NOW()),
('agend-018', 'corte-masculino', NOW(), NOW()),
('agend-019', 'corte-barba', NOW(), NOW()),
('agend-020', 'corte-masculino', NOW(), NOW()),
('agend-021', 'corte-masculino', NOW(), NOW()),
('agend-022', 'corte-barba', NOW(), NOW()),
('agend-023', 'corte-masculino', NOW(), NOW()),
('agend-024', 'corte-barba', NOW(), NOW()),
('agend-025', 'corte-masculino', NOW(), NOW()),
('agend-026', 'corte-masculino', NOW(), NOW()),
('agend-027', 'corte-barba', NOW(), NOW()),
('agend-028', 'corte-masculino', NOW(), NOW()),
('agend-029', 'corte-barba', NOW(), NOW()),
('agend-030', 'corte-masculino', NOW(), NOW()),
('agend-031', 'corte-barba', NOW(), NOW()),
('agend-032', 'corte-masculino', NOW(), NOW()),
('agend-033', 'corte-barba', NOW(), NOW()),
('agend-034', 'corte-masculino', NOW(), NOW()),
('agend-035', 'corte-barba', NOW(), NOW()),
('agend-036', 'corte-masculino', NOW(), NOW()),
('agend-037', 'corte-barba', NOW(), NOW()),
('agend-038', 'corte-masculino', NOW(), NOW()),
('agend-039', 'corte-barba', NOW(), NOW()),
('agend-040', 'corte-masculino', NOW(), NOW());

-- Agendamentos com serviços adicionais
INSERT INTO servicos_do_agendamento (agendamento, servico, created_at, updated_at) VALUES
('agend-002', 'sombrancelha', NOW(), NOW()),
('agend-004', 'hidratacao', NOW(), NOW()),
('agend-006', 'sombrancelha', NOW(), NOW()),
('agend-008', 'hidratacao', NOW(), NOW()),
('agend-010', 'sombrancelha', NOW(), NOW()),
('agend-012', 'hidratacao', NOW(), NOW()),
('agend-014', 'sombrancelha', NOW(), NOW()),
('agend-016', 'hidratacao', NOW(), NOW()),
('agend-017', 'sombrancelha', NOW(), NOW()),
('agend-019', 'hidratacao', NOW(), NOW()),
('agend-022', 'sombrancelha', NOW(), NOW()),
('agend-024', 'hidratacao', NOW(), NOW()),
('agend-027', 'sombrancelha', NOW(), NOW()),
('agend-029', 'hidratacao', NOW(), NOW()),
('agend-031', 'sombrancelha', NOW(), NOW()),
('agend-033', 'hidratacao', NOW(), NOW()),
('agend-035', 'sombrancelha', NOW(), NOW()),
('agend-037', 'hidratacao', NOW(), NOW()),
('agend-039', 'sombrancelha', NOW(), NOW());

-- =====================================================
-- INSERÇÃO DE PAGAMENTOS
-- =====================================================

-- Pagamentos para os agendamentos (exemplo dos primeiros 20)
INSERT INTO pagamento (id, valor, data, metodo, agendamento_id, created_at, updated_at) VALUES
('pag-001', 35.00, '2024-03-18 09:30:00', 'PIX', 'agend-001', NOW(), NOW()),
('pag-002', 65.00, '2024-03-18 10:45:00', 'Cartão', 'agend-002', NOW(), NOW()),
('pag-003', 35.00, '2024-03-18 11:30:00', 'Dinheiro', 'agend-003', NOW(), NOW()),
('pag-004', 65.00, '2024-03-18 14:45:00', 'PIX', 'agend-004', NOW(), NOW()),
('pag-005', 35.00, '2024-03-18 15:30:00', 'Cartão', 'agend-005', NOW(), NOW()),
('pag-006', 50.00, '2024-03-19 09:45:00', 'Dinheiro', 'agend-006', NOW(), NOW()),
('pag-007', 35.00, '2024-03-19 10:30:00', 'PIX', 'agend-007', NOW(), NOW()),
('pag-008', 65.00, '2024-03-19 11:45:00', 'Cartão', 'agend-008', NOW(), NOW()),
('pag-009', 35.00, '2024-03-19 14:30:00', 'Dinheiro', 'agend-009', NOW(), NOW()),
('pag-010', 65.00, '2024-03-19 15:45:00', 'PIX', 'agend-010', NOW(), NOW()),
('pag-011', 35.00, '2024-03-20 10:30:00', 'Cartão', 'agend-011', NOW(), NOW()),
('pag-012', 65.00, '2024-03-20 11:45:00', 'Dinheiro', 'agend-012', NOW(), NOW()),
('pag-013', 35.00, '2024-03-20 14:30:00', 'PIX', 'agend-013', NOW(), NOW()),
('pag-014', 65.00, '2024-03-20 15:45:00', 'Cartão', 'agend-014', NOW(), NOW()),
('pag-015', 35.00, '2024-03-20 16:30:00', 'Dinheiro', 'agend-015', NOW(), NOW()),
('pag-016', 35.00, '2024-03-21 11:30:00', 'PIX', 'agend-016', NOW(), NOW()),
('pag-017', 65.00, '2024-03-21 12:45:00', 'Cartão', 'agend-017', NOW(), NOW()),
('pag-018', 35.00, '2024-03-21 14:30:00', 'Dinheiro', 'agend-018', NOW(), NOW()),
('pag-019', 65.00, '2024-03-21 15:45:00', 'PIX', 'agend-019', NOW(), NOW()),
('pag-020', 35.00, '2024-03-21 16:30:00', 'Cartão', 'agend-020', NOW(), NOW());

-- =====================================================
-- MENSAGEM DE CONFIRMAÇÃO
-- =====================================================

SELECT 'Banco de dados populado com sucesso!' as status; 