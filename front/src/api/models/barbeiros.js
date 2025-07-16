import { BASE_URL } from "..";

// Listar todos os barbeiros
export const listar_barbeiros = async () => {
  const response = await fetch(`${BASE_URL}/usuario/barbeiros/listar`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};

// Consultar barbeiro por CPF
export const consultar_barbeiro = async (cpf) => {
  const response = await fetch(`${BASE_URL}/usuario/${cpf}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
}; 