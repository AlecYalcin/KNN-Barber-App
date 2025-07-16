import { useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { jwt_decoder } from "../api";

const SidebarBarbeiro = () => {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();
  const usuario = jwt_decoder(localStorage.getItem("usuario_token"));

  const menuItems = [
    {
      path: "/barbeiro/home",
      label: "Dashboard",
      icon: "🏠",
    },
    {
      path: "/barbeiro/agendamentos",
      label: "Meus Agendamentos",
      icon: "📅",
    },
    {
      path: "/servicos/cadastrar",
      label: "Cadastrar Serviços",
      icon: "✂️",
    },
    {
      path: "/barbeiro/perfil",
      label: "Perfil",
      icon: "👤",
    },
  ];

  const isActive = (path) => {
    return location.pathname === path;
  };

  return (
    <>
      {/* Botão do menu mobile */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="lg:hidden fixed top-4 left-4 z-50 p-2 bg-blue-600 text-white rounded-lg"
      >
        {isOpen ? "✕" : "☰"}
      </button>

      {/* Overlay para mobile */}
      {isOpen && (
        <div
          className="lg:hidden fixed inset-0 bg-black bg-opacity-50 z-40"
          onClick={() => setIsOpen(false)}
        />
      )}

      {/* Sidebar */}
      <div
        className={`fixed top-0 left-0 h-full w-64 bg-white shadow-lg transform transition-transform duration-300 ease-in-out z-40 lg:translate-x-0 ${
          isOpen ? "translate-x-0" : "-translate-x-full"
        }`}
      >
        <div className="p-6">
          {/* Header do sidebar */}
          <div className="flex items-center mb-8">
            <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mr-3">
              <span className="text-blue-600 font-bold text-lg">B</span>
            </div>
            <div>
              <h2 className="text-lg font-semibold text-gray-800">
                {usuario?.nome || "Barbeiro"}
              </h2>
              <p className="text-sm text-gray-600">Barbeiro</p>
            </div>
          </div>

          {/* Menu de navegação */}
          <nav className="space-y-2">
            {menuItems.map((item) => (
              <Link
                key={item.path}
                to={item.path}
                onClick={() => setIsOpen(false)}
                className={`flex items-center px-4 py-3 rounded-lg transition-colors duration-200 ${
                  isActive(item.path)
                    ? "bg-blue-100 text-blue-700 border-r-4 border-blue-600"
                    : "text-gray-700 hover:bg-gray-100"
                }`}
              >
                <span className="mr-3 text-lg">{item.icon}</span>
                <span className="font-medium">{item.label}</span>
              </Link>
            ))}
          </nav>

          {/* Seção de informações rápidas */}
          <div className="mt-8 p-4 bg-gray-50 rounded-lg">
            <h3 className="text-sm font-semibold text-gray-700 mb-2">
              Informações Rápidas
            </h3>
            <div className="space-y-1 text-xs text-gray-600">
              <p>📧 {usuario?.email || "email@exemplo.com"}</p>
              <p>📱 {usuario?.telefone || "(00) 00000-0000"}</p>
            </div>
          </div>

          {/* Botão de logout */}
          <div className="mt-8">
            <button
              onClick={() => {
                localStorage.removeItem("usuario_token");
                window.location.href = "/login";
              }}
              className="w-full flex items-center px-4 py-3 text-red-600 hover:bg-red-50 rounded-lg transition-colors duration-200"
            >
              <span className="mr-3">🚪</span>
              <span className="font-medium">Sair</span>
            </button>
          </div>
        </div>
      </div>

      {/* Espaçamento para desktop */}
      <div className="hidden lg:block w-64" />
    </>
  );
};

export default SidebarBarbeiro; 