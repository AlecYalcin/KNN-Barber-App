const ClienteAgendamento = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center py-10">
      <button
        className="absolute top-8 left-4 flex items-center text-blue-600 hover:text-blue-800 transition focus:outline-none"
        onClick={() => window.history.back()}
        aria-label="Voltar"
      >
        <svg
          className="w-6 h-6 mr-1"
          fill="none"
          stroke="currentColor"
          strokeWidth={2}
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M15 19l-7-7 7-7"
          />
        </svg>
        Voltar
      </button>

      <div className="grid items-center px-5 py-5 rounded-xl mt-10 bg-blue-500">
        <h1 className="text-2xl font-bold flex justify-center text-gray-800">
          Agendamento de Serviços
        </h1>

        <div className="grid grid-cols-7 mt-6 bg-ambr-600 gap-2">
          {Array.from({ length: 31 }, (_, i) => (i + 1).toString()).map((dia) => (
            <label key={dia} className="cursor-pointer">
              <input
                type="radio"
                name="dia"
                value={dia}
                className="hidden peer"
              />
              <div className="peer-checked:bg-white h-10 w-10 rounded-2xl border flex items-center justify-center text-2xl font-bold text-gray-800 hover:bg-white hover:text-blue-500 transition">
                {dia}
              </div>
            </label>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ClienteAgendamento;
