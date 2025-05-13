import React from "react";

const BarbeiroLogin = () => {
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
          <form className="rounded-lg p-8">
            {/* Campo Email */}
            <div className="mb-6">
              <label className="block text-gray-700 text-sm font-bold mb-2">
                Email
              </label>
              <input
                type="email"
                placeholder="seuemail@gmail.com"
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
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 pr-10"
                />
                {/* Ícone de olho (opcional) */}
                <button
                  type="button"
                  className="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-500 hover:text-gray-700"
                  onClick={() => {}}
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
              type="button"
              className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-4 px-4 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200"
            >
              Entrar
            </button>

            {/* Link registrar */}
            <div className="flex justify-center my-6 text-sm">
              <a href="/barbeiro/cadastro" className="font-bold">
                Não possui uma conta ?{" "}
                <span className="text-blue-500 "> Registre-se </span>
              </a>
            </div>
          </form>
        </div>
      </div>

      {/* Imagem da tela de Login */}
      <div className="hidden md:flex md:w-1/2 bg-blue-600 items-center justify-center p-8 text-white">
        <div className="text-center max-w-md">
          <h1 className="text-4xl font-bold mb-6">Alguma Imagem</h1>
        </div>
      </div>
    </div>
  );
};

export default BarbeiroLogin;