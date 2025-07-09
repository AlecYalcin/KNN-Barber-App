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
    localStorage.removeItem("user_token");
}