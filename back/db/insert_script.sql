CREATE EXTENSION IF NOT EXISTS "pgcrypto";

INSERT INTO USUARIO (email, nome, senha, telefone, eh_barbeiro) VALUES
('joao@email.com', 'João Silva', '123456', '11999990001', TRUE),
('maria@email.com', 'Maria Lima', 'senha123', '11999990002', FALSE),
('carlos@email.com', 'Carlos Souza', 'abc123', '11999990003', TRUE),
('ana@email.com', 'Ana Oliveira', 'minhasenha', '11999990004', FALSE),
('lucas@email.com', 'Lucas Costa', 'lucas123', '11999990005', TRUE),
('beatriz@email.com', 'Beatriz Ramos', 'bea456', '11999990006', FALSE),
('paulo@email.com', 'Paulo Mendes', 'senha789', '11999990007', TRUE),
('julia@email.com', 'Julia Nunes', '123abc', '11999990008', FALSE),
('marcos@email.com', 'Marcos Dias', 'senha@2025', '11999990009', TRUE),
('larissa@email.com', 'Larissa Freitas', 'larissa789', '11999990010', FALSE);

INSERT INTO JORNADA_DE_TRABALHO (id, ativa, horario_inicio, horario_pausa, horario_retorno, horario_fim, usuario_email) VALUES
('2fb86a4d-3014-418a-a403-7223af1ef157', TRUE, '2025-04-21 09:00:00', '2025-04-21 12:00:00', '2025-04-21 13:00:00', '2025-04-21 18:00:00', 'joao@email.com'),
('1f4debc0-8890-44e9-84b0-e18d4b76b189', TRUE, '2025-04-21 10:00:00', '2025-04-21 13:00:00', '2025-04-21 14:00:00', '2025-04-21 19:00:00', 'carlos@email.com'),
('5e6806e1-04bf-4f3a-a60f-2775afca011e', TRUE, '2025-04-21 11:00:00', '2025-04-21 14:00:00', '2025-04-21 15:00:00', '2025-04-21 20:00:00', 'lucas@email.com'),
('d60ad931-fbdb-4c21-91e2-163712e7218b', TRUE, '2025-04-21 12:00:00', '2025-04-21 15:00:00', '2025-04-21 16:00:00', '2025-04-21 21:00:00', 'paulo@email.com'),
('b6adb894-4ee6-4505-a2e7-d50c3450b76c', TRUE, '2025-04-21 13:00:00', '2025-04-21 16:00:00', '2025-04-21 17:00:00', '2025-04-21 22:00:00', 'marcos@email.com'),
('605f8971-0900-41b7-85cb-50698df7c8a4', TRUE, '2025-04-21 14:00:00', '2025-04-21 17:00:00', '2025-04-21 18:00:00', '2025-04-21 23:00:00', 'joao@email.com'),
('ba435597-21e4-4ec4-a992-a347a203ea3a', TRUE, '2025-04-21 15:00:00', '2025-04-21 18:00:00', '2025-04-21 19:00:00', '2025-04-22 00:00:00', 'carlos@email.com'),
('31048944-e450-47c8-ba8b-e6541a2e5a45', TRUE, '2025-04-21 16:00:00', '2025-04-21 19:00:00', '2025-04-21 20:00:00', '2025-04-22 01:00:00', 'lucas@email.com'),
('2b1efae3-ab83-4c18-b921-ad7427f9aab6', TRUE, '2025-04-21 17:00:00', '2025-04-21 20:00:00', '2025-04-21 21:00:00', '2025-04-22 02:00:00', 'paulo@email.com'),
('ed1c617a-686a-4fa3-82aa-6acb9321586c', TRUE, '2025-04-21 18:00:00', '2025-04-21 21:00:00', '2025-04-21 22:00:00', '2025-04-22 03:00:00', 'marcos@email.com');

INSERT INTO DIA_DA_SEMANA (id, dia, jornada_id) VALUES ('183ae6cc-ca4e-4007-a12a-fc58a00e2b6b', 'Segunda-feira', (SELECT id FROM JORNADA_DE_TRABALHO LIMIT 1 OFFSET 0));
INSERT INTO DIA_DA_SEMANA (id, dia, jornada_id) VALUES ('1d0a58b0-6ba7-4b99-9c9c-ab53bddb2ead', 'Terça-feira', (SELECT id FROM JORNADA_DE_TRABALHO LIMIT 1 OFFSET 1));
INSERT INTO DIA_DA_SEMANA (id, dia, jornada_id) VALUES ('38e92018-e79c-4411-a777-7ab137021373', 'Quarta-feira', (SELECT id FROM JORNADA_DE_TRABALHO LIMIT 1 OFFSET 2));
INSERT INTO DIA_DA_SEMANA (id, dia, jornada_id) VALUES ('a1f012f8-c499-410a-8a25-177311ebd8db', 'Quinta-feira', (SELECT id FROM JORNADA_DE_TRABALHO LIMIT 1 OFFSET 3));
INSERT INTO DIA_DA_SEMANA (id, dia, jornada_id) VALUES ('f746d1d2-9508-4491-a0e1-256524d530d6', 'Sexta-feira', (SELECT id FROM JORNADA_DE_TRABALHO LIMIT 1 OFFSET 4));
INSERT INTO DIA_DA_SEMANA (id, dia, jornada_id) VALUES ('7e424a47-d224-4ece-ac6c-6af2d9d13d6e', 'Sábado', (SELECT id FROM JORNADA_DE_TRABALHO LIMIT 1 OFFSET 5));
INSERT INTO DIA_DA_SEMANA (id, dia, jornada_id) VALUES ('6171bb04-9dd4-43ee-8934-b1d949e9a7de', 'Domingo', (SELECT id FROM JORNADA_DE_TRABALHO LIMIT 1 OFFSET 6));
INSERT INTO DIA_DA_SEMANA (id, dia, jornada_id) VALUES ('01177f6b-cda2-4f65-a5de-1b8d2c0f6b39', 'Segunda-feira', (SELECT id FROM JORNADA_DE_TRABALHO LIMIT 1 OFFSET 7));
INSERT INTO DIA_DA_SEMANA (id, dia, jornada_id) VALUES ('c684a4e6-565a-4149-9d89-56437ca3d5ad', 'Terça-feira', (SELECT id FROM JORNADA_DE_TRABALHO LIMIT 1 OFFSET 8));
INSERT INTO DIA_DA_SEMANA (id, dia, jornada_id) VALUES ('51203285-fe9b-4a58-8c48-4fab89bdf9d2', 'Quarta-feira', (SELECT id FROM JORNADA_DE_TRABALHO LIMIT 1 OFFSET 9));

INSERT INTO HORARIO_INDISPONIVEL (id, horario_inicio, horario_fim, justificativa, usuario_email) VALUES
('b7fed385-8197-413a-b7fe-b40dd2f46b7d', '2025-04-22 10:00', '2025-04-22 12:00', 'Consulta médica', 'joao@email.com'),
('1cbe6228-77a1-40f8-8059-ea2065106389', '2025-04-23 10:00', '2025-04-23 12:00', 'Compromisso pessoal', 'lucas@email.com'),
('f0ab0d16-e48b-4323-be1b-9c8408286f03', '2025-04-24 10:00', '2025-04-24 12:00', 'Manutenção', 'paulo@email.com'),
('9d361b67-026a-4eac-a268-79b8db1e5c02', '2025-04-25 10:00', '2025-04-25 12:00', 'Reunião', 'marcos@email.com'),
('fa9755d2-aa90-4b2c-b587-68545f3abcfe', '2025-04-26 10:00', '2025-04-26 12:00', 'Viagem', 'carlos@email.com'),
('5e6b3aa6-8604-4b46-8bfc-570f9f1aaa08', '2025-04-27 10:00', '2025-04-27 12:00', 'Consulta médica', 'joao@email.com'),
('4e37496f-3303-4dbb-aabd-b7dc257a2f30', '2025-04-28 10:00', '2025-04-28 12:00', 'Compromisso pessoal', 'lucas@email.com'),
('92df846a-b1e3-4e34-a526-fc62d12901a7', '2025-04-29 10:00', '2025-04-29 12:00', 'Manutenção', 'paulo@email.com'),
('978a4ded-f901-4a16-847e-4e20ed878ec2', '2025-04-30 10:00', '2025-04-30 12:00', 'Reunião', 'marcos@email.com'),
('1f7c1361-0344-46f1-98e3-c791b8c854cb', '2025-05-01 10:00', '2025-05-01 12:00', 'Viagem', 'carlos@email.com');

INSERT INTO SERVICO (id, nome, descricao, preco, duracao) VALUES
('f209aaec-ee24-48c9-aedf-c2a6b1466308', 'Corte Masculino', 'Corte de cabelo padrão', 30.0, '00:30'),
('e212dcf6-fdb3-4006-85ce-e2c11d959ad9', 'Corte Feminino', 'Corte de cabelo para mulheres', 40.0, '00:45'),
('f42d10f6-d76c-4436-9e56-2e0aa80faed3', 'Barba', 'Modelagem de barba', 20.0, '00:20'),
('6c5a3332-358c-425a-9582-7cc0d6ba16f6', 'Sobrancelha', 'Design de sobrancelha', 15.0, '00:15'),
('0bd03406-72b3-4787-bbc5-f68f1fe09688', 'Luzes', 'Luzes no cabelo', 100.0, '01:30'),
('f991dcbc-a3f8-43a0-9c1d-5e4676c81cb0', 'Pintura', 'Pintura capilar', 80.0, '01:00'),
('9d08ab54-b68b-4576-865c-0f4eca6411cb', 'Hidratação', 'Hidratação capilar', 50.0, '00:40'),
('6020a5df-30ec-4444-8140-475b3fe59068', 'Escova', 'Escova progressiva', 120.0, '01:30'),
('36957d4b-e3e3-4d7a-aaf4-862e8f35a7f4', 'Alisamento', 'Alisamento definitivo', 150.0, '02:00'),
('4c55f23b-c78b-45f9-ad93-c9a225447e56', 'Corte Infantil', 'Corte para crianças', 25.0, '00:25');

INSERT INTO METODO_DE_PAGAMENTO (id, metodo) VALUES
(1, 'Dinheiro'),
(2, 'Cartão de Crédito'),
(3, 'Cartão de Débito'),
(4, 'PIX'),
(5, 'Boleto');

INSERT INTO AGENDAMENTO (id, horario_inicio, horario_fim, cliente_email, barbeiro_email, servico_id)
VALUES
(1, '2025-04-23 09:00:00', '2025-04-23 09:30:00', 'maria@email.com', 'joao@email.com', (SELECT id FROM SERVICO LIMIT 1 OFFSET 0)),
(2, '2025-04-23 10:00:00', '2025-04-23 10:30:00', 'ana@email.com', 'carlos@email.com', (SELECT id FROM SERVICO LIMIT 1 OFFSET 1)),
(3, '2025-04-23 11:00:00', '2025-04-23 11:30:00', 'beatriz@email.com', 'lucas@email.com', (SELECT id FROM SERVICO LIMIT 1 OFFSET 2)),
(4, '2025-04-23 12:00:00', '2025-04-23 12:30:00', 'julia@email.com', 'paulo@email.com', (SELECT id FROM SERVICO LIMIT 1 OFFSET 3)),
(5, '2025-04-23 13:00:00', '2025-04-23 13:30:00', 'larissa@email.com', 'marcos@email.com', (SELECT id FROM SERVICO LIMIT 1 OFFSET 4)),
(6, '2025-04-23 14:00:00', '2025-04-23 14:30:00', 'maria@email.com', 'joao@email.com', (SELECT id FROM SERVICO LIMIT 1 OFFSET 5)),
(7, '2025-04-23 15:00:00', '2025-04-23 15:30:00', 'ana@email.com', 'carlos@email.com', (SELECT id FROM SERVICO LIMIT 1 OFFSET 6)),
(8, '2025-04-23 16:00:00', '2025-04-23 16:30:00', 'beatriz@email.com', 'lucas@email.com', (SELECT id FROM SERVICO LIMIT 1 OFFSET 7)),
(9, '2025-04-23 17:00:00', '2025-04-23 17:30:00', 'julia@email.com', 'paulo@email.com', (SELECT id FROM SERVICO LIMIT 1 OFFSET 8)),
(10, '2025-04-23 18:00:00', '2025-04-23 18:30:00', 'larissa@email.com', 'marcos@email.com', (SELECT id FROM SERVICO LIMIT 1 OFFSET 9));

INSERT INTO PAGAMENTO (id, valor, data, metodo_id, agendamento_id)
VALUES
(1, 92.96, '2025-04-23 14:00:00', 1, 1),
(2, 52.02, '2025-04-23 15:00:00', 2, 2),
(3, 24.68, '2025-04-23 16:00:00', 3, 3),
(4, 141.65, '2025-04-23 17:00:00', 4, 4),
(5, 38.37, '2025-04-23 18:00:00', 5, 5),
(6, 70.1, '2025-04-23 19:00:00', 1, 6),
(7, 25.07, '2025-04-23 20:00:00', 2, 7),
(8, 53.66, '2025-04-23 21:00:00', 3, 8),
(9, 69.42, '2025-04-23 22:00:00', 4, 9),
(10, 86.47, '2025-04-23 23:00:00', 5, 10);
