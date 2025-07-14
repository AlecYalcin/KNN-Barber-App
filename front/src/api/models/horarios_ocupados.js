import { BASE_URL } from "..";

// Criar Horário Ocupado
export const criar_horario_ocupado = async (
  barbeiro_cpf,
  horario_inicio,
  horario_fim,
  justificativa
) => {
  const response = await fetch(`${BASE_URL}/horario-indisponivel/criar`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
    body: JSON.stringify({
      barbeiro_cpf,
      horario_inicio,
      horario_fim,
      justificativa,
    }),
  });
  const data = await response.json();
  return data;
};

// Alterar Horário Ocupado
export const alterar_horario_ocupado = async () => {};

// Remover Horário Ocupado
export const remover_horario_ocupado = async () => {};

// Listar Horários Ocupados
export const listar_horarios_ocupados_do_barbeiro = async (CPF) => {
  const response = await fetch(
    `${BASE_URL}/horario-indisponivel/pesquisar-horarios?barbeiro_cpf=${CPF}`,
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
