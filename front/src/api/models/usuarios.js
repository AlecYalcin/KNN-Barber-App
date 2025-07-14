import { BASE_URL } from "..";

// Função de cadastro
export const registar_usuario = async (usuario) => {
  const response = await fetch(`${BASE_URL}/auth/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(usuario),
  });
  const data = await response.json();
  return data;
};

// Função de autenticação
export const autenticar_usuario = async (email, senha) => {
  const response = await fetch(`${BASE_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, senha }),
  });
  const data = await response.json();
  return data;
};

// Função de logout
export const logout = () => {
  localStorage.removeItem("usuario_token");
};

// Função de exclusão de usuário do sistema
export const remover_usuario = async (usuario_id) => {
  const response = await fetch(`${BASE_URL}/usuario/${usuario_id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};

// Função de edição de usuário do sistema
export const alterar_usuario = async (
  usuario_id,
  { nome, email, telefone }
) => {
  const response = await fetch(`${BASE_URL}/usuario/${usuario_id}`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
    body: JSON.stringify({
      nome,
      email,
      telefone,
    }),
  });
  const data = await response.json();
  return data;
};

// Função de consulta de usuário do sistema
export const consultar_usuario = async (usuario_id) => {
  const response = await fetch(`${BASE_URL}/usuario/${usuario_id}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};
