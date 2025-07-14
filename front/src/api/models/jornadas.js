import { BASE_URL } from "..";

// Criar ou Editar Jornada
export const alterar_jornada = async () => {};

// Excluir Jornada
export const remover_jornada = async () => {};

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
