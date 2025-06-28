const Sidebar = () => {
  return (
    <div className="hidden lg:flex lg:w-64 lg:flex-col p-6 fixed top-17 z-50 lg:h-full shadow-lg">
      <div className="flex flex-col items-center mb-8 mt-10">
        {/* Foto do perfil */}
        <div className="w-32 h-32 rounded-full bg-gray-200 mb-4 overflow-hidden border-4 border-blue-100">
          <img
            src="https://cdn.creazilla.com/icons/3251108/person-icon-md.png"
            alt="Foto do cliente"
            className="w-full h-full object-cover"
          />
        </div>
        <h2 className="text-2xl font-semibold bg-amer-400">Denner Biscate</h2>
      </div>

      <nav className="space-y-2 bg-ambr-600">
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
  );
}

export default Sidebar;