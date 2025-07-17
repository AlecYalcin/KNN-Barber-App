import { NavLink } from "react-router-dom";
// API
import { jwt_decoder } from "../api/index";

const Sidebar = () => {
  const usuario = jwt_decoder(localStorage.getItem("usuario_token"));
  return (
    <div className="hidden lg:flex lg:w-64 lg:flex-col p-6 fixed top-17 z-50 lg:h-full shadow-lg bg-white">
      <div className="flex flex-col items-center mb-8 mt-10">
        {/* Foto do perfil */}
        <div className="w-32 h-32 rounded-full bg-gray-200 mb-4 overflow-hidden border-4 border-blue-100">
          <img
            src="https://cdn.creazilla.com/icons/3251108/person-icon-md.png"
            alt="Foto do cliente"
            className="w-full h-full object-cover"
          />
        </div>
        <h2 className="text-2xl font-semibold text-gray-800 text-center">
          {usuario.nome}
        </h2>
      </div>

      <nav className="space-y-2">
        {usuario.eh_barbeiro ? (
          <div>
            <NavLink
              to="/barbeiro/home"
              className={({ isActive }) =>
                `w-full block text-left px-4 py-2 rounded-lg font-medium ${
                  isActive ? "bg-gray-200" : "hover:bg-gray-100"
                }`
              }
            >
              Dashboard
            </NavLink>
            <NavLink
              to="/barbeiro/agendamentos"
              className={({ isActive }) =>
                `w-full block text-left px-4 py-2 rounded-lg font-medium ${
                  isActive ? "bg-gray-200" : "hover:bg-gray-100"
                }`
              }
            >
              Agendamentos
            </NavLink>
            <NavLink
              to="/servicos/cadastrar"
              className={({ isActive }) =>
                `w-full block text-left px-4 py-2 rounded-lg font-medium ${
                  isActive ? "bg-gray-200" : "hover:bg-gray-100"
                }`
              }
            >
              Serviços
            </NavLink>
          </div>
        ) : (
          <div>
            <NavLink
              to="/home"
              className={({ isActive }) =>
                `w-full block text-left px-4 py-2 rounded-lg font-medium ${
                  isActive ? "bg-gray-200" : "hover:bg-gray-100"
                }`
              }
            >
              {" "}
              Início
            </NavLink>
            <NavLink
              to="/cliente/agendamentos"
              className={({ isActive }) =>
                `w-full block text-left px-4 py-2 rounded-lg font-medium ${
                  isActive ? "bg-gray-200" : "hover:bg-gray-100"
                }`
              }
            >
              {" "}
              Agendamentos
            </NavLink>
          </div>
        )}

        {/* Geral */}
        <NavLink
          to="/perfil"
          className={({ isActive }) =>
            `w-full block text-left px-4 py-2 rounded-lg font-medium ${
              isActive ? "bg-gray-200" : "hover:bg-gray-100"
            }`
          }
        >
          Perfil
        </NavLink>
      </nav>
    </div>
  );
};

export default Sidebar;
