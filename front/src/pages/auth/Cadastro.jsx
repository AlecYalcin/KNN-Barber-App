import { React, useState } from "react";
import { useNavigate } from "react-router-dom";
import { usuario } from "../../api";

const Cadastro = () => {
  const [cpf, setCpf] = useState("");
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [telefone, setTelefone] = useState("");
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();

    // Verificando se email e senha foram digitados
    if (!cpf || !nome || !email || !senha || !telefone) {
      alert("Digite todos os dados cadastrais.");
      return;
    }

    // Realizando a requisição
    const data = await usuario.registar_usuario({
      cpf,
      nome,
      email,
      senha,
      telefone,
    });

    // Verificando erros
    if (data.error) {
      alert(data.mensagem);
      return;
    }

    // Adicionando o token
    localStorage.setItem("usuario_token", data.token);
    navigate("/cliente/home", { replace: true });
  };

  return (
    <div className="min-h-screen flex flex-col md:flex-row">
      {/* parte da esquerda (a imagem) - visivel apenas no desktop */}
      <div className="hidden md:flex md:w-1/2 bg-blue-600 items-center justify-center p-8 text-white">
        <div className="text-center max-w-md">
          <h1 className="text-4xl font-bold mb-6">Alguma Imagem</h1>
        </div>
      </div>

      {/* Parte Direita (o forms) */}
      <div className="w-full md:w-1/2 flex items-center justify-center p-4 bg-white registro-mobile">
        <a
          href="/cliente/login"
          className="hidden md: absolute top-4 left-4 md:top-8 md:right-8 text-gray-600 hover:text-blue-600 transition-colors"
          title="Voltar"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-8 w-8"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M10 19l-7-7m0 0l7-7m-7 7h18"
            />
          </svg>
        </a>
        <div className="w-full max-w-md mx-auto h-full flex flex-col justify-center">
          {/* Texto central */}
          <div className="text-center mb-6">
            <h1 className="text-4xl font-bold">Formulário de Cadastro</h1>
          </div>

          {/* formulário */}
          <form className="rounded-lg p-8" onSubmit={(e) => handleRegister(e)}>
            {/* Campo nome */}
            <div className="mb-6">
              <label className="block text-gray-700 text-sm font-bold mb-2">
                CPF
              </label>
              <input
                type="name"
                value={cpf}
                onChange={(e) => setCpf(e.target.value)}
                placeholder="000.000.000-00"
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            {/* Campo nome */}
            <div className="mb-6">
              <label className="block text-gray-700 text-sm font-bold mb-2">
                Nome
              </label>
              <input
                type="name"
                value={nome}
                onChange={(e) => setNome(e.target.value)}
                placeholder="informe seu nome"
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            {/* Campo email */}
            <div className="mb-6">
              <label className="block text-gray-700 text-sm font-bold mb-2">
                Email
              </label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="seuemail@gmail.com"
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            {/* Campo telefone */}
            <div className="mb-6">
              <label className="block text-gray-700 text-sm font-bold mb-2">
                Telefone
              </label>
              <input
                type="text"
                value={telefone}
                onChange={(e) => setTelefone(e.target.value)}
                placeholder="informe seu telefone"
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            {/* Campo senha */}
            <div className="mb-6">
              <label className="block text-gray-700 text-sm font-bold mb-2">
                Senha
              </label>
              <div className="relative">
                <input
                  type="password"
                  value={senha}
                  onChange={(e) => setSenha(e.target.value)}
                  placeholder="***************"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 pr-10"
                />
              </div>
            </div>

            {/* Botão Salvar */}
            <button
              type="submit"
              className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-4 px-4 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200"
            >
              Salvar
            </button>

            <div className="flex justify-center my-6 text-sm">
              <a href="/cliente/login" className="font-bold">
                Já está cadastrado ?{" "}
                <span className="text-blue-500 "> Faça Login </span>
              </a>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Cadastro;
