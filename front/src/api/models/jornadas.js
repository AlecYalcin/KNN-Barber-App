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
  // Se há jornada existente, remove ela
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

  // Se todos os horários estão vazios, nem cria nova jornada
  if (!horario_inicio && !horario_pausa && !horario_retorno && !horario_fim) {
    return { mensagem: "Horário excluído com sucesso!" };
  }

  // Monta dinamicamente o corpo da requisição
  const bodyData = {
    barbeiro_cpf,
    dia_da_semana,
  };

  if (horario_inicio) bodyData.horario_inicio = horario_inicio;
  if (horario_fim) bodyData.horario_fim = horario_fim;
  if (horario_pausa) bodyData.horario_pausa = horario_pausa;
  if (horario_retorno) bodyData.horario_retorno = horario_retorno;

  // Envia para o backend
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
