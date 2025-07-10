import React from "react";
import BottomNav from "../../components/BottomNav";

const ClientePerfil = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="md:hidden flex flex-col min-h-screen">
        <div className="flex-1 p-4 bg-white">
          {/* foto e informacoes */}
          <div className="flex flex-col justify-center perfil-mobile">
            <div className="flex flex-col items-center mb-6">
              <div className="w-36 h-36 rounded-full bg-gray-200 mb-3 overflow-hidden border-4 border-blue-100">
                <img
                  src="https://cdn.creazilla.com/icons/3251108/person-icon-md.png"
                  alt="Foto do cliente"
                  className="w-full h-full object-cover"
                />
              </div>
              <h2 className="text-xl font-semibold">Nome do cliente</h2>
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

            {/* Agendamentos */}
            <div className="mb-6">
              <h2 className="text-lg font-bold mb-3 text-gray-800">
                Agendamentos
              </h2>
              <div className="bg-gray-50 rounded-lg p-3 border border-gray-200 min-h-20">
                <p className="text-sm text-gray-500">
                  Nenhum agendamento recente
                </p>
              </div>
            </div>

            {/* açoes */}
            <div className="flex justify-end space-x-3 mb-16">
              <button className="px-4 py-2 border border-red-500 text-red-500 rounded-lg hover:bg-red-50 text-sm">
                Excluir Perfil
              </button>
              <button className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm">
                Editar Perfil
              </button>
            </div>
          </div>
        </div>

        <BottomNav  />
      </div>
    </div>
  );
};

export default ClientePerfil;
