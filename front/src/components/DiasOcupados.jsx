import { useState, useEffect } from "react";

// API
import { horario_ocupado, jwt_decoder } from "../api";

const DiasOcupados = () => {
  const [diasOcupados, setDiasOcupados] = useState([]);

  // Recuperando horários ocupados
  useEffect(() => {
    const fetchDias = async () => {
      // Reconhecendo usuário atual de barbeiro
      const usuario = jwt_decoder(localStorage.getItem("usuario_token"));

      // Recuperando horários ocupados desse barbeiro
      const data = await horario_ocupado.listar_horarios_ocupados_do_barbeiro(
        usuario.cpf
      );

      setDiasOcupados(data);
    };
    fetchDias();
  }, []);

  return (
    <div className="mt-6">
      <div className="bg-gray-50 rounded-lg p-3 border border-gray-200 min-h-20 max-h-48 overflow-y-auto space-y-3">
        {diasOcupados.map((dia) => (
          <div
            key={dia.id}
            className="flex justify-between items-center bg-white px-3 py-2 rounded shadow-sm border border-gray-100"
          >
            <span className="text-sm text-gray-700">
              ({dia.horario_inicio} - {dia.horario_fim}) {dia.justificativa}
            </span>
            <div className="flex gap-2">
              <button className="text-blue-600 text-sm hover:underline">
                Editar
              </button>
              <button className="text-red-600 text-sm hover:underline">
                Excluir
              </button>
            </div>
          </div>
        ))}
      </div>

      <div className="flex justify-end">
        <button className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 mt-6 text-sm">
          Adicionar dia ocupado
        </button>
      </div>
    </div>
  );
};

export default DiasOcupados;
