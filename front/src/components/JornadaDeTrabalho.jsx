import { useState, useEffect } from "react";

// API
import { jwt_decoder, jornada } from "../api/index";

// Dias da semana fixos e ordenados
const DIAS_SEMANA = [
  "Segunda",
  "Terça",
  "Quarta",
  "Quinta",
  "Sexta",
  "Sábado",
  "Domingo",
];

const formatarHorario = (valor) => valor || "--:--";

export default function JornadaDeTrabalhoMobile() {
  const [jornadaDeTrabalho, setJornadaDeTrabalho] = useState({});

  // Função de edição para cada dia
  const handleEditar = (dia) => {
    alert(`Editar horários de ${dia}`);
    // aqui você pode abrir um modal, redirecionar, etc.
  };

  // Função para coletar jornadas atualizadas
  const fetchJornada = async () => {
    const usuario = jwt_decoder(localStorage.getItem("usuario_token"));
    const data = await jornada.consultar_jornada_de_trabalho(usuario.cpf);

    const jornadaDeTrabalhoAtualizada = {};
    data.forEach((jornada_atual) => {
      jornadaDeTrabalhoAtualizada[jornada_atual.dia_da_semana] = jornada_atual;
    });
    setJornadaDeTrabalho(jornadaDeTrabalhoAtualizada);
  };

  // Coletando todas as jornadas do dia assim que entra
  useEffect(() => {
    fetchJornada();
  }, []);

  return (
    <div className="p-4 space-y-4">
      {DIAS_SEMANA.map((dia) => {
        const info_jornada = jornadaDeTrabalho[dia] || {};

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
              <span>{formatarHorario(info_jornada.horario_inicio)}</span>
              <span className="font-medium">Pausa:</span>
              <span>{formatarHorario(info_jornada.horario_pausa)}</span>
              <span className="font-medium">Retorno:</span>
              <span>{formatarHorario(info_jornada.horario_retorno)}</span>
              <span className="font-medium">Fim:</span>
              <span>{formatarHorario(info_jornada.horario_fim)}</span>
            </div>
          </div>
        );
      })}
    </div>
  );
}
