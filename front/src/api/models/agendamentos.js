import { BASE_URL } from "..";

// Criar Agendamento
export const criar_agendamento = async (
  barbeiro_cpf,
  cliente_cpf,
  servicos_id,
  horario_inicio,
  horario_fim
) => {
  const response = await fetch(`${BASE_URL}/agendamento/criar`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
    body: JSON.stringify({
      barbeiro_cpf,
      cliente_cpf,
      servicos_id,
      horario_inicio,
      horario_fim,
    }),
  });
  
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.mensagem || `Erro ${response.status}: ${response.statusText}`);
  }
  
  const data = await response.json();
  return data;
};

// Função para consultar agendamentos por barbeiro
export const consultar_agendamentos_por_barbeiro = async (barbeiro_cpf) => {
  const response = await fetch(`${BASE_URL}/agendamento/barbeiro/${barbeiro_cpf}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};

// Função para consultar agendamentos por cliente
export const consultar_agendamentos_por_cliente = async (cliente_cpf) => {
  const response = await fetch(`${BASE_URL}/agendamento/cliente/${cliente_cpf}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};

// Função para consultar agendamentos por horário
export const consultar_agendamentos_por_horario = async (horario_inicio, horario_fim) => {
  const response = await fetch(
    `${BASE_URL}/agendamento/horario?horario_inicio=${horario_inicio}&horario_fim=${horario_fim}`,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
      },
    }
  );
  const data = await response.json();
  return data;
};

// Função para listar todos os agendamentos
export const listar_agendamentos = async () => {
  const response = await fetch(`${BASE_URL}/agendamento/listar`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};

// Função para consultar agendamento por ID
export const consultar_agendamento = async (id) => {
  const response = await fetch(`${BASE_URL}/agendamento/${id}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};

// Função para remover agendamento
export const remover_agendamento = async (id) => {
  const response = await fetch(`${BASE_URL}/agendamento/${id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
}; 