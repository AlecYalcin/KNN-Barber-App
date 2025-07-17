import { React, useState } from "react";
import { useNavigate } from "react-router-dom";
import { usuario } from "../../api";

const Login = () => {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    // Verificando se email e senha foram digitados
    if (!email || !senha) {
      alert("Digite um e-mail e senha válidos.");
      return;
    }

    // Realizando a requisição
    const data = await usuario.autenticar_usuario(email, senha);

    // Verificando erros
    if (data.error) {
      alert(data.mensagem);
      return;
    }

    // Adicionando o token
    localStorage.setItem("usuario_token", data.token);
    navigate("/home", { replace: true });
  };

  return (
    <div className="min-h-screen flex flex-col md:flex-row">
      {/* Parte esquerda */}
      <div className="w-full md:w-1/2 flex items-center justify-center p-4 bg-white login-mobile">
        <div className="w-full max-w-md">
          {/* Logo da barbearia */}
          <div className="text-center mb-8">
            <img
              src="/barbearia-kn.jpg"
              alt="Logo"
              className="mx-auto h-56 rounded-full"
            />
          </div>

          {/* Formulário */}
          <form className="rounded-lg p-8" onSubmit={(e) => handleLogin(e)}>
            {/* Campo Email */}
            <div className="mb-6">
              <label className="block text-gray-700 text-sm font-bold mb-2">
                Email
              </label>
              <input
                type="email"
                placeholder="seuemail@gmail.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            {/* Senha */}
            <div className="mb-6">
              <label className="block text-gray-700 text-sm font-bold mb-2">
                Senha
              </label>
              <div className="relative">
                <input
                  type="password"
                  placeholder="***************"
                  value={senha}
                  onChange={(e) => setSenha(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 pr-10"
                />
                {/* Ícone de olho (opcional) */}
                <button
                  type="button"
                  className="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-500 hover:text-gray-700"
                ></button>
              </div>
            </div>

            {/* Link abaixo do campo */}
            <div className="flex justify-end my-6 text-sm">
              <a
                href="/#"
                className="text-blue-500 hover:text-blue-700 font-bold"
              >
                Esqueceu seu senha?
              </a>
            </div>

            {/* Botão Entrar */}
            <button
              type="submit"
              className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-4 px-4 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200"
            >
              Entrar
            </button>

            {/* Link registrar */}
            <div className="flex justify-center my-6 text-sm">
              <a href="/cadastro" className="font-bold">
                Não possui uma conta ?{" "}
                <span className="text-blue-500 "> Registre-se </span>
              </a>
            </div>
          </form>
        </div>
      </div>

      {/* Imagem da tela de Login */}
      <div className="hidden md:flex md:w-1/2 ">
        <img className="" alt="imagem-login" src="public/login.png" />
      </div>
    </div>
  );
};

export default Login;
