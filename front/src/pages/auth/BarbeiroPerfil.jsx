import React from "react";

const BarbeiroPerfil = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <div className="lg:flex justify-between hidden md:flex bg-blue-600 p-4 text-white">
        <h1 className="text-3xl font-bold ml-2">Perfil</h1>
        <button className="mr-4">Sair</button>
      </div>
      {/* Layout Desktop (md para cima) */}
      <div className="hidden md:block min-h-screen">
        <div className="max-w mx-auto bg-white overflow-hidden">
          <div className="flex flex-col md:flex-row h-screen">
            {/* Sidebar */}
            <div className="w-full md:w-64 bg-gray-50 p-6">
              <div className="flex flex-col items-center mb-8">
                {/* Foto do perfil */}
                <div className="w-32 h-32 rounded-full bg-gray-200 mb-4 overflow-hidden border-4 border-blue-100">
                  <img
                    src="https://cdn.creazilla.com/icons/3251108/person-icon-md.png"
                    alt="Foto do cliente"
                    className="w-full h-full object-cover"
                  />
                </div>
                <h2 className="text-2xl font-semibold">Nome do barbeiro</h2>
              </div>

              <nav className="space-y-2">
                <button className="w-full text-left px-4 py-2 rounded-lg font-medium hover:bg-gray-200">
                  Início
                </button>
                <button className="w-full text-left px-4 py-2 rounded-lg hover:bg-gray-200">
                  Agendamentos
                </button>
                <button className="w-full text-left px-4 py-2 rounded-lg hover:bg-gray-200">
                  Pagamentos
                </button>
                <button className="w-full text-left px-4 py-2 rounded-lg bg-gray-200 font-medium">
                  Perfil
                </button>
              </nav>
            </div>

            {/* conteudo principal */}
            <div className="flex-1 p-8">
              <div className="mb-8">
                <h2 className="text-3xl font-bold mb-6">
                  Informações Pessoais
                </h2>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Telefone
                    </label>
                    <div className="p-3 bg-gray-50 rounded-lg border border-gray-200">
                      <p className="text-gray-500">+55 00 00000-0000</p>
                    </div>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      E-mail
                    </label>
                    <div className="p-3 bg-gray-50 rounded-lg border border-gray-200">
                      <p className="text-gray-500">emailcliente@gmail.com</p>
                    </div>
                  </div>
                </div>
              </div>
              {/* jornada */}
              <div className="mb-8">
                <div className="flex justify-between items-center mb-4">
                  <h2 className="text-3xl font-bold">Jornada</h2>
                </div>

                <div className="bg-gray-50 rounded-xl p-4 border border-gray-200">
                  <p className="text-gray-500">Nenhuma jornada adicionanda</p>
                </div>
                <div className="flex justify-end">
                  <button className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 mt-6">
                    Adicionar Jornada
                  </button>
                </div>
              </div>

              {/* dias ocupados */}
              <div className="mb-8">
                <div className="flex justify-between items-center mb-4">
                  <h2 className="text-3xl font-bold">Dias Ocupados</h2>
                </div>

                <div className="bg-gray-50 rounded-xl p-4 border border-gray-200">
                  <p className="text-gray-500">
                    Nenhum dia ocupado adicionando
                  </p>
                </div>
                <div className="flex justify-end">
                  <button className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 mt-6 ">
                    Adicionar Dia Ocupado
                  </button>
                </div>
              </div>

              <div className="flex justify-end space-x-4">
                <button className="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700">
                  Adicionar Barbeiro
                </button>
                <button className="px-6 py-2 bg-yellow-600 text-white rounded-lg hover:bg-yellow-700">
                  Listar Barbeiro
                </button>
                <button className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
                  Editar Perfil
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* versao mobile*/}
      <div className="md:hidden flex flex-col min-h-screen">
        <div className="flex-1 p-4 bg-white">
          {/* foto e informacoes */}
          <div className="flex flex-col justify-center">
            <div className="flex flex-col items-center mb-6">
              <div className="w-36 h-36 rounded-full bg-gray-200 mb-3 overflow-hidden border-4 border-blue-100">
                <img
                  src="https://cdn.creazilla.com/icons/3251108/person-icon-md.png"
                  alt="Foto do cliente"
                  className="w-full h-full object-cover"
                />
              </div>
              <h2 className="text-xl font-semibold">Nome do barbeiro</h2>
            </div>

            {/* informaçoes pessoais */}
            <div className="mb-6">
              <h2 className="text-lg font-bold mb-3 text-gray-800">
                Informações
              </h2>

              <div className="space-y-3">
                <div>
                  <label className="block text-xs font-medium text-gray-500 mb-1">
                    Telefone
                  </label>
                  <div className="p-2 bg-gray-50 rounded-lg border border-gray-200">
                    <p className="text-sm text-gray-500">+55 00 00000-0000</p>
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-medium text-gray-500 mb-1">
                    E-mail
                  </label>
                  <div className="p-2 bg-gray-50 rounded-lg border border-gray-200">
                    <p className="text-sm text-gray-500">
                      emailcliente@gmail.com
                    </p>
                  </div>
                </div>
              </div>
            </div>

            {/* jornada */}
            <div className="mb-8">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-2xl font-bold">Jornada</h2>
              </div>

              <div className="bg-gray-50 rounded-xl p-4 border border-gray-200">
                <p className="text-gray-500">Nenhuma jornada adicionanda</p>
              </div>
              <div className="flex justify-end">
                <button className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 mt-6 text-sm">
                  Adicionar Jornada
                </button>
              </div>
            </div>

            {/* dias ocupados */}
            <div className="mb-16">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-2xl font-bold">Dias Ocupados</h2>
              </div>

              <div className="bg-gray-50 rounded-xl p-4 border border-gray-200">
                <p className="text-gray-500">Nenhum dia ocupado adicionando</p>
              </div>
              <div className="flex justify-end">
                <button className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 mt-6 text-sm">
                  Adicionar Dia Ocupado
                </button>
              </div>
            </div>

            {/* açoes */}
            <div className="flex justify-end space-x-3 mb-6">
              <button className="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 text-sm">
                Adicionar Barbeiro
              </button>
              <button className="px-6 py-2 bg-yellow-600 text-white rounded-lg hover:bg-yellow-700 text-sm">
                Listar Barbeiro
              </button>
            </div>
            <div className="flex justify-end space-x-3 mb-16">
              <button className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm">
                Editar Perfil
              </button>
            </div>
          </div>
        </div>

        {/* Menu inferior - Mobile */}
        <div className="bg-white border-t border-gray-200 p-3 fixed bottom-0 left-0 right-0">
          <nav className="flex justify-around">
            <button className="flex flex-col items-center text-gray-500 hover:text-blue-600">
              <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                />
              </svg>
              <span className="text-xs mt-1">Início</span>
            </button>
            <button className="flex flex-col items-center text-gray-500 hover:text-blue-600">
              <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                />
              </svg>
              <span className="text-xs mt-1">Agendamentos</span>
            </button>
            <button className="flex flex-col items-center text-gray-500 hover:text-blue-600">
              <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"
                />
              </svg>
              <span className="text-xs mt-1">Pagamentos</span>
            </button>
            <button className="flex flex-col items-center">
              <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                />
              </svg>
              <span className="text-xs mt-1">Perfil</span>
            </button>
          </nav>
        </div>
      </div>
    </div>
  );
};

export default BarbeiroPerfil;
