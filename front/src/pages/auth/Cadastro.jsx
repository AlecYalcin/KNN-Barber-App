import React from "react";

const Cadastro = () => {
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
          <form className="rounded-lg p-8">
            {/* Campo nome */}
            <div className="mb-6">
              <label className="block text-gray-700 text-sm font-bold mb-2">
                Nome
              </label>
              <input
                type="name"
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
                  placeholder="***************"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 pr-10"
                />
              </div>
            </div>

            {/* Botão Salvar */}
            <button
              type="button"
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
