import { BASE_URL } from "..";

// Listar todos os serviços
export const listar_servicos = async (nome = null) => {
  const url = nome 
    ? `${BASE_URL}/servico/listar?nome=${encodeURIComponent(nome)}`
    : `${BASE_URL}/servico/listar`;
    
  const response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};

// Consultar serviço por ID
export const consultar_servico = async (id) => {
  const response = await fetch(`${BASE_URL}/servico/${id}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
  });
  const data = await response.json();
  return data;
};

// Criar serviço (apenas para barbeiros)
export const criar_servico = async (nome, descricao, preco, duracao) => {
  const response = await fetch(`${BASE_URL}/servico/criar`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("usuario_token")}`,
    },
    body: JSON.stringify({
      nome,
      descricao,
      preco,
      duracao,
    }),
  });
  const data = await response.json();
  return data;
}; 