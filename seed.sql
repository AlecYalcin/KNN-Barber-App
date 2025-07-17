-- Script de Povoamento - Sistema de Barbearia
-- PostgreSQL

-- Limpar dados existentes (ordem importante por causa das FK)
DELETE FROM pagamento;
DELETE FROM servicos_do_agendamento;
DELETE FROM agendamento;
DELETE FROM horario_indisponivel;
DELETE FROM jornada;
DELETE FROM servico;
DELETE FROM usuario;

-- ====================================
-- USUÁRIOS (Clientes e Barbeiros)
-- ====================================

-- Barbeiros
INSERT INTO usuario (cpf, nome, senha, telefone, email, eh_barbeiro, created_at, updated_at) VALUES
('12345678901', 'João Silva', '$2b$12$hashedpassword1', '(83) 99999-1001', 'joao.silva@barbearia.com', TRUE, NOW(), NOW()),
('23456789012', 'Carlos Santos', '$2b$12$hashedpassword2', '(83) 99999-1002', 'carlos.santos@barbearia.com', TRUE, NOW(), NOW()),
('34567890123', 'Miguel Oliveira', '$2b$12$hashedpassword3', '(83) 99999-1003', 'miguel.oliveira@barbearia.com', TRUE, NOW(), NOW()),
('45678901234', 'Rafael Costa', '$2b$12$hashedpassword4', '(83) 99999-1004', 'rafael.costa@barbearia.com', TRUE, NOW(), NOW());

-- Clientes
INSERT INTO usuario (cpf, nome, senha, telefone, email, eh_barbeiro, created_at, updated_at) VALUES
('11122233344', 'Pedro Almeida', '$2b$12$hashedpassword5', '(83) 98888-2001', 'pedro.almeida@email.com', FALSE, NOW(), NOW()),
('22233344455', 'Lucas Ferreira', '$2b$12$hashedpassword6', '(83) 98888-2002', 'lucas.ferreira@email.com', FALSE, NOW(), NOW()),
('33344455566', 'Antonio Lima', '$2b$12$hashedpassword7', '(83) 98888-2003', 'antonio.lima@email.com', FALSE, NOW(), NOW()),
('44455566677', 'José Roberto', '$2b$12$hashedpassword8', '(83) 98888-2004', 'jose.roberto@email.com', FALSE, NOW(), NOW()),
('55566677788', 'Marcos Pereira', '$2b$12$hashedpassword9', '(83) 98888-2005', 'marcos.pereira@email.com', FALSE, NOW(), NOW()),
('66677788899', 'Gabriel Souza', '$2b$12$hashedpassword10', '(83) 98888-2006', 'gabriel.souza@email.com', FALSE, NOW(), NOW()),
('77788899000', 'Fernando Castro', '$2b$12$hashedpassword11', '(83) 98888-2007', 'fernando.castro@email.com', FALSE, NOW(), NOW()),
('88899000111', 'Ricardo Mendes', '$2b$12$hashedpassword12', '(83) 98888-2008', 'ricardo.mendes@email.com', FALSE, NOW(), NOW());

-- ====================================
-- SERVIÇOS
-- ====================================

INSERT INTO servico (id, nome, descricao, preco, duracao, created_at, updated_at) VALUES
('srv_001', 'Corte Masculino', 'Corte tradicional masculino com acabamento', 25.00, 30, NOW(), NOW()),
('srv_002', 'Corte + Barba', 'Corte masculino com aparar barba', 35.00, 45, NOW(), NOW()),
('srv_003', 'Barba Completa', 'Aparar e modelar barba completa', 20.00, 25, NOW(), NOW()),
('srv_004', 'Bigode', 'Aparar e modelar bigode', 10.00, 15, NOW(), NOW()),
('srv_005', 'Sobrancelha', 'Aparar sobrancelha masculina', 8.00, 10, NOW(), NOW()),
('srv_006', 'Corte Infantil', 'Corte para crianças até 12 anos', 20.00, 25, NOW(), NOW()),
('srv_007', 'Corte Degradê', 'Corte moderno com degradê', 30.00, 35, NOW(), NOW()),
('srv_008', 'Lavagem + Corte', 'Lavagem completa com corte', 35.00, 40, NOW(), NOW()),
('srv_009', 'Tratamento Capilar', 'Hidratação e tratamento do couro cabeludo', 40.00, 30, NOW(), NOW()),
('srv_010', 'Desenho Barba', 'Desenho artístico na barba', 25.00, 20, NOW(), NOW());

-- ====================================
-- JORNADAS DE TRABALHO
-- ====================================

-- João Silva - Segunda a Sexta
INSERT INTO jornada (id, ativa, horario_inicio, horario_pausa, horario_retorno, horario_fim, dia_da_semana, barbeiro_cpf, created_at, updated_at) VALUES
('jor_001', TRUE, '08:00:00', '12:00:00', '14:00:00', '18:00:00', 'SEGUNDA', '12345678901', NOW(), NOW()),
('jor_002', TRUE, '08:00:00', '12:00:00', '14:00:00', '18:00:00', 'TERCA', '12345678901', NOW(), NOW()),
('jor_003', TRUE, '08:00:00', '12:00:00', '14:00:00', '18:00:00', 'QUARTA', '12345678901', NOW(), NOW()),
('jor_004', TRUE, '08:00:00', '12:00:00', '14:00:00', '18:00:00', 'QUINTA', '12345678901', NOW(), NOW()),
('jor_005', TRUE, '08:00:00', '12:00:00', '14:00:00', '18:00:00', 'SEXTA', '12345678901', NOW(), NOW()),
('jor_006', TRUE, '08:00:00', NULL, NULL, '14:00:00', 'SABADO', '12345678901', NOW(), NOW());

-- Carlos Santos - Terça a Sábado
INSERT INTO jornada (id, ativa, horario_inicio, horario_pausa, horario_retorno, horario_fim, dia_da_semana, barbeiro_cpf, created_at, updated_at) VALUES
('jor_007', TRUE, '09:00:00', '13:00:00', '15:00:00', '19:00:00', 'TERCA', '23456789012', NOW(), NOW()),
('jor_008', TRUE, '09:00:00', '13:00:00', '15:00:00', '19:00:00', 'QUARTA', '23456789012', NOW(), NOW()),
('jor_009', TRUE, '09:00:00', '13:00:00', '15:00:00', '19:00:00', 'QUINTA', '23456789012', NOW(), NOW()),
('jor_010', TRUE, '09:00:00', '13:00:00', '15:00:00', '19:00:00', 'SEXTA', '23456789012', NOW(), NOW()),
('jor_011', TRUE, '09:00:00', '13:00:00', '15:00:00', '19:00:00', 'SABADO', '23456789012', NOW(), NOW());

-- Miguel Oliveira - Segunda a Sexta (meio período)
INSERT INTO jornada (id, ativa, horario_inicio, horario_pausa, horario_retorno, horario_fim, dia_da_semana, barbeiro_cpf, created_at, updated_at) VALUES
('jor_012', TRUE, '14:00:00', NULL, NULL, '20:00:00', 'SEGUNDA', '34567890123', NOW(), NOW()),
('jor_013', TRUE, '14:00:00', NULL, NULL, '20:00:00', 'TERCA', '34567890123', NOW(), NOW()),
('jor_014', TRUE, '14:00:00', NULL, NULL, '20:00:00', 'QUARTA', '34567890123', NOW(), NOW()),
('jor_015', TRUE, '14:00:00', NULL, NULL, '20:00:00', 'QUINTA', '34567890123', NOW(), NOW()),
('jor_016', TRUE, '14:00:00', NULL, NULL, '20:00:00', 'SEXTA', '34567890123', NOW(), NOW());

-- Rafael Costa - Fins de semana
INSERT INTO jornada (id, ativa, horario_inicio, horario_pausa, horario_retorno, horario_fim, dia_da_semana, barbeiro_cpf, created_at, updated_at) VALUES
('jor_017', TRUE, '08:00:00', '12:00:00', '14:00:00', '18:00:00', 'SABADO', '45678901234', NOW(), NOW()),
('jor_018', TRUE, '08:00:00', NULL, NULL, '16:00:00', 'DOMINGO', '45678901234', NOW(), NOW());

-- ====================================
-- HORÁRIOS INDISPONÍVEIS
-- ====================================

-- Algumas ausências pontuais
INSERT INTO horario_indisponivel (id, horario_inicio, horario_fim, justificativa, barbeiro_cpf, created_at, updated_at) VALUES
('hi_001', '2024-07-20 09:00:00', '2024-07-20 11:00:00', 'Consulta médica', '12345678901', NOW(), NOW()),
('hi_002', '2024-07-22 14:00:00', '2024-07-22 16:00:00', 'Reunião de capacitação', '23456789012', NOW(), NOW()),
('hi_003', '2024-07-25 08:00:00', '2024-07-25 12:00:00', 'Compromisso pessoal', '34567890123', NOW(), NOW()),
('hi_004', '2024-07-27 10:00:00', '2024-07-27 12:00:00', 'Curso de atualização', '45678901234', NOW(), NOW());

-- ====================================
-- AGENDAMENTOS
-- ====================================

-- Agendamentos para esta semana
INSERT INTO agendamento (id, horario_inicio, horario_fim, barbeiro_cpf, cliente_cpf, created_at, updated_at) VALUES
('age_001', '2024-07-17 08:30:00', '2024-07-17 09:00:00', '12345678901', '11122233344', NOW(), NOW()),
('age_002', '2024-07-17 09:00:00', '2024-07-17 09:45:00', '12345678901', '22233344455', NOW(), NOW()),
('age_003', '2024-07-17 10:00:00', '2024-07-17 10:25:00', '12345678901', '33344455566', NOW(), NOW()),
('age_004', '2024-07-17 14:00:00', '2024-07-17 14:35:00', '34567890123', '44455566677', NOW(), NOW()),
('age_005', '2024-07-17 15:00:00', '2024-07-17 15:30:00', '34567890123', '55566677788', NOW(), NOW()),
('age_006', '2024-07-18 09:30:00', '2024-07-18 10:00:00', '23456789012', '66677788899', NOW(), NOW()),
('age_007', '2024-07-18 10:30:00', '2024-07-18 11:15:00', '23456789012', '77788899000', NOW(), NOW()),
('age_008', '2024-07-18 14:30:00', '2024-07-18 15:00:00', '34567890123', '88899000111', NOW(), NOW()),
('age_009', '2024-07-19 08:00:00', '2024-07-19 08:30:00', '12345678901', '11122233344', NOW(), NOW()),
('age_010', '2024-07-19 16:00:00', '2024-07-19 16:45:00', '23456789012', '22233344455', NOW(), NOW()),
('age_011', '2024-07-20 08:00:00', '2024-07-20 08:30:00', '12345678901', '33344455566', NOW(), NOW()),
('age_012', '2024-07-20 09:00:00', '2024-07-20 09:45:00', '45678901234', '44455566677', NOW(), NOW()),
('age_013', '2024-07-20 15:00:00', '2024-07-20 15:25:00', '34567890123', '55566677788', NOW(), NOW()),
('age_014', '2024-07-21 10:00:00', '2024-07-21 10:35:00', '45678901234', '66677788899', NOW(), NOW()),
('age_015', '2024-07-21 14:00:00', '2024-07-21 14:30:00', '12345678901', '77788899000', NOW(), NOW());

-- ====================================
-- SERVIÇOS DOS AGENDAMENTOS
-- ====================================

-- Relacionar serviços com agendamentos
INSERT INTO servicos_do_agendamento (agendamento, servico, created_at, updated_at) VALUES
('age_001', 'srv_001', NOW(), NOW()), -- Corte Masculino
('age_002', 'srv_002', NOW(), NOW()), -- Corte + Barba
('age_003', 'srv_003', NOW(), NOW()), -- Barba Completa
('age_004', 'srv_007', NOW(), NOW()), -- Corte Degradê
('age_005', 'srv_001', NOW(), NOW()), -- Corte Masculino
('age_006', 'srv_001', NOW(), NOW()), -- Corte Masculino
('age_007', 'srv_002', NOW(), NOW()), -- Corte + Barba
('age_008', 'srv_001', NOW(), NOW()), -- Corte Masculino
('age_009', 'srv_001', NOW(), NOW()), -- Corte Masculino
('age_010', 'srv_002', NOW(), NOW()), -- Corte + Barba
('age_011', 'srv_001', NOW(), NOW()), -- Corte Masculino
('age_012', 'srv_002', NOW(), NOW()), -- Corte + Barba
('age_013', 'srv_003', NOW(), NOW()), -- Barba Completa
('age_014', 'srv_007', NOW(), NOW()), -- Corte Degradê
('age_015', 'srv_001', NOW(), NOW()); -- Corte Masculino

-- Alguns agendamentos com múltiplos serviços
INSERT INTO servicos_do_agendamento (agendamento, servico, created_at, updated_at) VALUES
('age_002', 'srv_005', NOW(), NOW()), -- Corte + Barba + Sobrancelha
('age_007', 'srv_005', NOW(), NOW()), -- Corte + Barba + Sobrancelha
('age_010', 'srv_010', NOW(), NOW()), -- Corte + Barba + Desenho Barba
('age_012', 'srv_005', NOW(), NOW()); -- Corte + Barba + Sobrancelha

-- ====================================
-- PAGAMENTOS
-- ====================================

-- Pagamentos para os agendamentos
INSERT INTO pagamento (id, valor, data, metodo, agendamento_id, created_at, updated_at) VALUES
('pag_001', 25.00, '2024-07-17 09:00:00', 'DINHEIRO', 'age_001', NOW(), NOW()),
('pag_002', 43.00, '2024-07-17 09:45:00', 'DINHEIRO', 'age_002', NOW(), NOW()), -- Corte + Barba + Sobrancelha
('pag_003', 20.00, '2024-07-17 10:25:00', 'PIX', 'age_003', NOW(), NOW()),
('pag_004', 30.00, '2024-07-17 14:35:00', 'PIX', 'age_004', NOW(), NOW()),
('pag_005', 25.00, '2024-07-17 15:30:00', 'DINHEIRO', 'age_005', NOW(), NOW()),
('pag_006', 25.00, '2024-07-18 10:00:00', 'PIX', 'age_006', NOW(), NOW()),
('pag_007', 43.00, '2024-07-18 11:15:00', 'DINHEIRO', 'age_007', NOW(), NOW()), -- Corte + Barba + Sobrancelha
('pag_008', 25.00, '2024-07-18 15:00:00', 'DINHEIRO', 'age_008', NOW(), NOW()),
('pag_009', 25.00, '2024-07-19 08:30:00', 'PIX', 'age_009', NOW(), NOW()),
('pag_010', 60.00, '2024-07-19 16:45:00', 'DINHEIRO', 'age_010', NOW(), NOW()), -- Corte + Barba + Desenho Barba
('pag_011', 25.00, '2024-07-20 08:30:00', 'DINHEIRO', 'age_011', NOW(), NOW()),
('pag_012', 43.00, '2024-07-20 09:45:00', 'PIX', 'age_012', NOW(), NOW()), -- Corte + Barba + Sobrancelha
('pag_013', 20.00, '2024-07-20 15:25:00', 'PIX', 'age_013', NOW(), NOW()),
('pag_014', 30.00, '2024-07-21 10:35:00', 'DINHEIRO', 'age_014', NOW(), NOW()),
('pag_015', 25.00, '2024-07-21 14:30:00', 'DINHEIRO', 'age_015', NOW(), NOW());

-- ====================================
-- QUERIES DE VERIFICAÇÃO
-- ====================================

-- Verificar dados inseridos
SELECT 'USUÁRIOS' as tabela, COUNT(*) as total FROM usuario
UNION ALL
SELECT 'BARBEIROS', COUNT(*) FROM usuario WHERE eh_barbeiro = TRUE
UNION ALL
SELECT 'CLIENTES', COUNT(*) FROM usuario WHERE eh_barbeiro = FALSE
UNION ALL
SELECT 'SERVIÇOS', COUNT(*) FROM servico
UNION ALL
SELECT 'JORNADAS', COUNT(*) FROM jornada
UNION ALL
SELECT 'HORÁRIOS INDISPONÍVEIS', COUNT(*) FROM horario_indisponivel
UNION ALL
SELECT 'AGENDAMENTOS', COUNT(*) FROM agendamento
UNION ALL
SELECT 'SERVIÇOS/AGENDAMENTOS', COUNT(*) FROM servicos_do_agendamento
UNION ALL
SELECT 'PAGAMENTOS', COUNT(*) FROM pagamento;

-- Verificar agendamentos com seus serviços
SELECT 
    a.id as agendamento_id,
    u_cliente.nome as cliente,
    u_barbeiro.nome as barbeiro,
    a.horario_inicio,
    a.horario_fim,
    s.nome as servico,
    s.preco,
    p.valor as valor_pago,
    p.metodo as metodo_pagamento
FROM agendamento a
JOIN usuario u_cliente ON a.cliente_cpf = u_cliente.cpf
JOIN usuario u_barbeiro ON a.barbeiro_cpf = u_barbeiro.cpf
JOIN servicos_do_agendamento sa ON a.id = sa.agendamento
JOIN servico s ON sa.servico = s.id
LEFT JOIN pagamento p ON a.id = p.agendamento_id
ORDER BY a.horario_inicio;