import { useState } from "react";
import BottomNav from "../../components/BottomNav";
import Sidebar from "../../components/SidebarClient";
import Header from "../../components/Header";
import { DayPicker } from "react-day-picker";
import { ptBR } from "date-fns/locale";
import "react-day-picker/dist/style.css";

const HORARIOS = [
  "08:00",
  "09:00",
  "10:00",
  "11:00",
  "12:00",
  "13:00",
  "14:00",
  "15:00",
];

const ClienteAgendamento = () => {
  const [selectedDate, setSelectedDate] = useState(null);
  const [horarioSelecionado, setHorarioSelecionado] = useState("");
  const [confirmado, setConfirmado] = useState(false);

  const handleSelecionarHorario = (e) => {
    setHorarioSelecionado(e.target.value);
    setConfirmado(false);
  };

  const handleConfirmar = () => {
    if (selectedDate && horarioSelecionado) {
      setConfirmado(true);
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

        <div className="mt-5 bg-blue-400 p-4 rounded-lg shadow-lg">
          <DayPicker
            mode="single"
            selected={selectedDate}
            onSelect={setSelectedDate}
            fromDate={new Date()}
            locale={ptBR}
            modifiers={{
              disabled: { before: new Date() },
            }}
            formatters={{
              formatCaption: (date, options) => {
                return new Intl.DateTimeFormat("pt-BR", {
                  month: "long",
                  year: "numeric",
                })
                  .format(date)
                  .replace(/^\w/, (c) => c.toUpperCase());
              },
            }}
          />

          {selectedDate && (
            <p className="text-center mt-2 text-gray-700">
              Selecionado:{" "}
              {selectedDate
                .toLocaleDateString("pt-BR", {
                  weekday: "long",
                  day: "2-digit",
                  month: "long",
                  year: "numeric",
                })
                .replace(/^\w/, (c) => c.toUpperCase())}
            </p>
          )}
        </div>

        <div className="lg:mt-10 w-full max-w-md">
          <h1 className="text-2xl font-bold mb-2 flex justify-center text-gray-800 mt-10 lg:mt-0">
            Horários Disponíveis
          </h1>

          <div className="w-full bg-gray-100 p-4 justify-center items-center rounded-lg shadow-lg">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
              {HORARIOS.map((hora) => (
                <label
                  key={hora}
                  className={`text-xl rounded-lg border-2 bg-white h-12 flex items-center justify-center text-gray-800 font-bold cursor-pointer transition-colors
                    ${
                      horarioSelecionado === hora
                        ? "border-blue-500 text-blue-600 bg-blue-50"
                        : "border-gray-200 hover:border-blue-300"
                    }
                    ${!selectedDate ? "opacity-50 cursor-not-allowed" : ""}
                  `}
                >
                  <input
                    type="radio"
                    name="horario"
                    value={hora}
                    checked={horarioSelecionado === hora}
                    onChange={handleSelecionarHorario}
                    className="hidden"
                    disabled={!selectedDate}
                  />
                  {hora}
                </label>
              ))}
            </div>
          </div>

          <div className="mt-6 mb-10 w-full">
            <button
              className={`w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition
                ${
                  !(selectedDate && horarioSelecionado)
                    ? "opacity-50 cursor-not-allowed"
                    : ""
                }
              `}
              onClick={handleConfirmar}
              disabled={!(selectedDate && horarioSelecionado)}
            >
              Confirmar Agendamento
            </button>
            {confirmado && (
              <div className="mt-4 p-3 bg-green-100 text-green-800 rounded-lg text-center font-bold">
                Agendamento confirmado para{" "}
                {selectedDate.toLocaleDateString("pt-BR")} às{" "}
                {horarioSelecionado}!
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
