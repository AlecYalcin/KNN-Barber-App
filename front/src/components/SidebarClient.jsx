import { NavLink } from "react-router-dom";

const Sidebar = () => {
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
        <h2 className="text-2xl font-semibold text-gray-800">Denner Biscate</h2>
      </div>

      <nav className="space-y-2">
        <NavLink
          to="/cliente/home"
          className={({ isActive }) =>
            `w-full block text-left px-4 py-2 rounded-lg font-medium ${
              isActive ? "bg-gray-200" : "hover:bg-gray-100"
            }`
          }
          end
        >
          Início
        </NavLink>
        <NavLink
          to="/cliente/agendamento"
          className={({ isActive }) =>
            `w-full block text-left px-4 py-2 rounded-lg font-medium ${
              isActive ? "bg-gray-200" : "hover:bg-gray-100"
            }`
          }
        >
          Agendamentos
        </NavLink>
        <NavLink
          to="/pagamentos"
          className={({ isActive }) =>
            `w-full block text-left px-4 py-2 rounded-lg font-medium ${
              isActive ? "bg-gray-200" : "hover:bg-gray-100"
            }`
          }
        >
          Pagamentos
        </NavLink>
        <NavLink
          to="/cliente/perfil"
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