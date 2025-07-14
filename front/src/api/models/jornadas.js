import { BASE_URL } from "..";

// Criar ou Editar Jornada
export const criar_ou_alterar_jornada = async (
  barbeiro_cpf,
  jornada_id,
  dia_da_semana,
  horario_inicio,
  horario_pausa,
  horario_retorno,
  horario_fim
) => {
  // Excluindo jornada já existente
  if (jornada_id) {
    const response = await fetch(`${BASE_URL}/jornada/${jornada_id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
      },
    });
    await response.json();
  }

  // Criando nova jornada
  const bodyData = {
    barbeiro_cpf,
    dia_da_semana,
    horario_inicio,
    horario_fim,
  };

  // Só adiciona se existir valor válido
  if (horario_pausa) {
    bodyData.horario_pausa = horario_pausa;
  }
  if (horario_retorno) {
    bodyData.horario_retorno = horario_retorno;
  }

  const response = await fetch(`${BASE_URL}/jornada/criar`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
    body: JSON.stringify(bodyData),
  });
  const data = await response.json();
  return data;
};

// Excluir Jornada
export const remover_jornada = async (jornada_id) => {
  const response = await fetch(`${BASE_URL}/jornada/${jornada_id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};

// Consultar Jornada do Barbeiro
export const consultar_jornada_de_trabalho = async (barbeiro_cpf) => {
  const response = await fetch(`${BASE_URL}/jornada/barbeiro/${barbeiro_cpf}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};

// Consultar JOrnada por ID
export const consultar_jornada = async (jornada_id) => {
  const response = await fetch(`${BASE_URL}/jornada/${jornada_id}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};
