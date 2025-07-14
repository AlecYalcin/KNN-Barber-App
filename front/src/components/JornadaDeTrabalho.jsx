import React from "react";

// Dias da semana fixos e ordenados
const DIAS_SEMANA = [
  "SEGUNDA",
  "TERÇA",
  "QUARTA",
  "QUINTA",
  "SEXTA",
  "SÁBADO",
  "DOMINGO",
];

// Dados simulados (você pode passar por props depois)
const jornada = {
  SEGUNDA: { inicio: "07:00", pausa: "11:00", retorno: "13:00", fim: "17:00" },
  TERÇA: {},
  QUARTA: { inicio: "07:00", fim: "11:00" },
  QUINTA: { inicio: "08:00", pausa: "12:00", retorno: "14:00", fim: "18:00" },
};

const formatarHorario = (valor) => valor || "--:--";

export default function JornadaDeTrabalhoMobile() {
  // Função de edição para cada dia
  const handleEditar = (dia) => {
    alert(`Editar horários de ${dia}`);
    // aqui você pode abrir um modal, redirecionar, etc.
  };

  return (
    <div className="p-4 space-y-4">
      {DIAS_SEMANA.map((dia) => {
        const horarios = jornada[dia] || {};

        return (
          <div
            key={dia}
            className="relative rounded-xl border border-gray-300 p-4 shadow-sm"
          >
            {/* Botão de edição */}
            <button
              onClick={() => handleEditar(dia)}
              className="absolute top-2 right-2 text-blue-600 hover:text-blue-800 text-sm"
              aria-label={`Editar ${dia}`}
              title={`Editar ${dia}`}
            >
              Editar
            </button>

            {/* Título do dia */}
            <h3 className="text-lg font-semibold mb-2">{dia}</h3>

            {/* Grade de horários */}
            <div className="grid grid-cols-2 gap-y-2 text-sm">
              <span className="font-medium">Início:</span>
              <span>{formatarHorario(horarios.inicio)}</span>
              <span className="font-medium">Pausa:</span>
              <span>{formatarHorario(horarios.pausa)}</span>
              <span className="font-medium">Retorno:</span>
              <span>{formatarHorario(horarios.retorno)}</span>
              <span className="font-medium">Fim:</span>
              <span>{formatarHorario(horarios.fim)}</span>
            </div>
          </div>
        );
      })}
    </div>
  );
}
