import { useState } from "react";
import BottomNav from "../../components/BottomNav";
import Sidebar from "../../components/SidebarClient";
import Header from "../../components/Header";

const DIAS = Array.from({ length: 31 }, (_, i) => (i + 1).toString());
const HORARIOS = [
  "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"
];

const ClienteAgendamento = () => {
  const [diaSelecionado, setDiaSelecionado] = useState("");
  const [horarioSelecionado, setHorarioSelecionado] = useState("");
  const [confirmado, setConfirmado] = useState(false);

  const handleSelecionarDia = (e) => {
    setDiaSelecionado(e.target.value);
    setHorarioSelecionado(""); // Limpa horário ao trocar o dia
    setConfirmado(false);
  };

  const handleSelecionarHorario = (e) => {
    setHorarioSelecionado(e.target.value);
    setConfirmado(false);
  };

  const handleConfirmar = () => {
    if (diaSelecionado && horarioSelecionado) {
      // Aqui você pode fazer uma requisição para salvar o agendamento
      setConfirmado(true);
      // Exemplo: await api.post('/agendamentos', { dia: diaSelecionado, horario: horarioSelecionado });
    }
  };

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

      <Header title="Agendamento" />

      <Sidebar />

      <main className="flex w-full md:items-center flex-col items-center lg:mt-10 p-6 lg:pl-69">
        <h1 className="text-2xl font-bold mt-20 flex justify-center text-gray-800">
          Selecione o Dia
        </h1>
        <div className="grid mt-5">
          <div className="grid grid-cols-7 rounded-2xl p-3 w-full h-full bg-blue-500 gap-2 lg:gap-4 shadow-lg">
            {DIAS.map((dia) => (
              <label key={dia} className="cursor-pointer">
                <input
                  type="radio"
                  name="dia"
                  value={dia}
                  checked={diaSelecionado === dia}
                  onChange={handleSelecionarDia}
                  className="hidden peer"
                />
                <div className={`peer-checked:bg-white h-10 w-10 lg:h-12 lg:w-12 lg:rounded-2xl lg:text-3x lg:text-4xl 2xl:h-15 2xl:w-15 2xl:rounded-3xl rounded-2xl border flex items-center justify-center text-2xl font-bold text-gray-800 hover:bg-white hover:text-blue-500 transition
                  ${diaSelecionado === dia ? "bg-white text-blue-500" : ""}
                `}>
                  {dia}
                </div>
              </label>
            ))}
          </div>
        </div>

        <div className="lg:mt-10">
          <h1 className="text-2xl font-bold mb-2 flex justify-center text-gray-800 mt-10 lg:mt-0">
            Horários Disponíveis
          </h1>

          <div className="w-full bg-gray-300 justify-center items-center rounded-lg shadow-lg">
            <ul className="grid grid-cols-5 gap-3 p-2 rounded-lg">
              {HORARIOS.map((hora) => (
                <label
                  key={hora}
                  className={`text-xl rounded-2xl border bg-white h-12 w-15 2xl:h-17 2xl:w-20 2xl:text-2xl text-gray-800 font-bold cursor-pointer
                    ${horarioSelecionado === hora ? " text-black border-blue-500 border-4": ""}
                  `}
                >
                  <input
                    type="radio"
                    name="horario"
                    value={hora}
                    checked={horarioSelecionado === hora}
                    onChange={handleSelecionarHorario}
                    className="hidden peer"
                    aria-label={`Selecionar horário ${hora}`}
                    disabled={!diaSelecionado}
                  />
                  <span className="h-full w-full flex items-center justify-center rounded-2xl transition"
                        onChange={handleSelecionarHorario}>
                    {hora}
                  </span>
                </label>
              ))}
            </ul>
            <div />
          </div>

          <div className="mt-6 mb-10">
            <button
              className={`w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition
                ${!(diaSelecionado && horarioSelecionado) ? "opacity-50 cursor-not-allowed" : ""}
              `}
              onClick={handleConfirmar}
              disabled={!(diaSelecionado && horarioSelecionado)}
            >
              Confirmar
            </button>
            {confirmado && (
              <div className="mt-4 text-green-600 text-center font-bold">
                Agendamento confirmado para dia {diaSelecionado} às {horarioSelecionado}!
              </div>
            )}
          </div>
        </div>
      </main>
      <BottomNav />
    </div>
  );
};

export default ClienteAgendamento;
