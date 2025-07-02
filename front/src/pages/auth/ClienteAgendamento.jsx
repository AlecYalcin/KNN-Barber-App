import BottomNav from "../../components/BottomNav";
import Sidebar from "../../components/SidebarClient";

const ClienteAgendamento = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <button
        className="fixed top-8 left-4 z-50 flex items-center text-blue-600 hover:text-blue-800 transition focus:outline-none lg:hidden"
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

      <header className="lg:flex justify-between hidden bg-blue-600 p-4 text-white fixed top-0 w-full z-50">
        <h1 className="text-3xl font-bold ml-2">Agendamentos</h1>
        <button className="mr-4">Sair</button>
      </header>

      <Sidebar />

      <main className="flex w-full  flex-col items-center p-6">
        <h1 className="text-2xl font-bold mt-20 flex justify-center text-gray-800">
          Selecione o Dia
        </h1>
        <div className="grid mt-5">
          <div className="grid grid-cols-7 rounded-2xl p-3 w-full h-full bg-blue-500 gap-2 lg:gap-4 shadow-lg">
            {Array.from({ length: 31 }, (_, i) => (i + 1).toString()).map(
              (dia) => (
                <label key={dia} className="cursor-pointer">
                  <input
                    type="radio"
                    name="dia"
                    value={dia}
                    className="hidden peer"
                  />
                  <div className="peer-checked:bg-white h-10 w-10 lg:h-12 lg:w-12 lg:rounded-2xl lg:text-3x lg:text-4xl 2xl:h-15 2xl:w-15 2xl:rounded-3xl rounded-2xl border flex items-center justify-center text-2xl font-bold text-gray-800 hover:bg-white hover:text-blue-500 transition">
                    {dia}
                  </div>
                </label>
              )
            )}
          </div>
        </div>

        <div className="lg:mt-10">
          <h1 className="text-2xl font-bold mb-2 flex justify-center text-gray-800 mt-10 lg:mt-0">
            Horários Disponíveis
          </h1>

          <div className="w-full bg-gray-300 justify-center items-center rounded-lg shadow-lg">
            <ul className="grid grid-cols-5 gap-3 p-2 rounded-lg">
              {["08:00", "09:00", "10:00", "11:00", "12:00", "13:00","14:00","15:00"].map(
                (hora) => (
                  <label
                    key={hora}
                    className=" text-xl rounded-2xl border bg-white h-12 w-15 2xl:h-17 2xl:w-20 2xl:text-2xl text-gray-800 font-bold cursor-pointer peer-checked:bg-white peer-checked:text-blue-500"
                  >
                    <input
                      type="checkbox"
                      className="hidden peer"
                      aria-label={`Selecionar horário ${hora}`}
                    />
                    <span className="peer-checked:bg-blue-500 peer-checked:text-gray-800 h-full w-full flex items-center justify-center rounded-2xl transition lg:">
                      {hora}
                    </span>
                  </label>
                )
              )}
            </ul>
            <div />
          </div>

          <div className="mt-6 mb-10">
            <button className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition">
              Confirmar
            </button>
          </div>
        </div>
      </main>
      <BottomNav />
    </div>
  );
};

export default ClienteAgendamento;
