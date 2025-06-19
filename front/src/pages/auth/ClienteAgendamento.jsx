import BottomNav from "../../components/BottomNav";
import Sidebar from "../../components/SidebarClient";

const ClienteAgendamento = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center py-10 lg:flex-row">
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

      <Sidebar />

      <div className="bg-amber-200 lg:ml-64 lg:w-full lg:flex lg:flex-col ">
        <div className="grid items-center px-5 py-5 rounded-xl mt-10 bg-blue-500">
          <h1 className="text-2xl font-bold flex justify-center text-gray-800">
            Agendamento de Serviços
          </h1>

          <div className="grid grid-cols-7 mt-6 bg-ambr-600 gap-2">
            {Array.from({ length: 31 }, (_, i) => (i + 1).toString()).map(
              (dia) => (
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
              )
            )}
          </div>
        </div>

        <div className="lg:ml-5 ">
          <h1 className="text-2xl font-bold mb-2 flex justify-center text-gray-800 mt-10">
            Horários Disponíveis
          </h1>

          <div className="w-full bg-ambr-300">
            <ul className="grid grid-cols-5 gap-2 p-4 rounded-lg">
              {["08:00", "09:00", "10:00", "11:00", "12:00", "13:00"].map(
                (hora) => (
                  <label
                    key={hora}
                    className=" text-xl rounded-2xl border bg-white h-12 w-15 text-gray-800 font-bold cursor-pointer peer-checked:bg-white peer-checked:text-blue-500"
                  >
                    <input
                      type="checkbox"
                      className="hidden peer"
                      aria-label={`Selecionar horário ${hora}`}
                    />
                    <span className="peer-checked:bg-blue-500 peer-checked:text-gray-800 h-full w-full flex items-center justify-center rounded-2xl transition">
                      {hora}
                    </span>
                  </label>
                )
              )}
            </ul>
            <div />
          </div>

          <div className="mt-6 mb-4">
            <button className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition">
              Confirmar
            </button>
          </div>

          <BottomNav />
        </div>
      </div>
    </div>
  );
};

export default ClienteAgendamento;
