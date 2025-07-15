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
  const [modalAberto, setModalAberto] = useState(false);
  const [diaSelecionado, setDiaSelecionado] = useState("");
  const [formData, setFormData] = useState({
    jornada_id: "",
    dia_da_semana: "",
    horario_inicio: "",
    horario_pausa: "",
    horario_retorno: "",
    horario_fim: "",
  });

  const handleEditar = (dia) => {
    const info = jornadaDeTrabalho[dia] || {};
    setDiaSelecionado(dia);
    setFormData({
      jornada_id: info.id || "",
      dia_da_semana: dia,
      horario_inicio: info.horario_inicio || "",
      horario_pausa: info.horario_pausa || "",
      horario_retorno: info.horario_retorno || "",
      horario_fim: info.horario_fim || "",
    });
    setModalAberto(true);
  };

  const handleChange = (e) => {
    setFormData((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSalvar = async () => {
    // Recuperando Usuário
    const usuario = jwt_decoder(localStorage.getItem("usuario_token"));

    // Realizar salvamento/alteração
    const data = await jornada.criar_ou_alterar_jornada(
      usuario.cpf,
      formData.jornada_id,
      formData.dia_da_semana,
      formData.horario_inicio,
      formData.horario_pausa,
      formData.horario_retorno,
      formData.horario_fim
    );

    alert(data.mensagem);
    if (data.error) {
      return;
    }

    fetchJornada();
    setModalAberto(false);
  };

  const handleLimpar = () => {
    setFormData({
      ...formData,
      horario_inicio: "",
      horario_pausa: "",
      horario_retorno: "",
      horario_fim: "",
    });
  };

  const fetchJornada = async () => {
    const usuario = jwt_decoder(localStorage.getItem("usuario_token"));
    const data = await jornada.consultar_jornada_de_trabalho(usuario.cpf);
    const jornadaDeTrabalhoAtualizada = {};
    data.forEach((jornada_atual) => {
      jornadaDeTrabalhoAtualizada[jornada_atual.dia_da_semana] = jornada_atual;
    });
    setJornadaDeTrabalho(jornadaDeTrabalhoAtualizada);
  };

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
            <button
              onClick={() => handleEditar(dia)}
              className="absolute top-2 right-2 text-blue-600 hover:text-blue-800 text-sm"
            >
              Editar
            </button>

            <h3 className="text-lg font-semibold mb-2">{dia}</h3>

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

      {/* Modal */}
      {modalAberto && (
        <div className="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-40">
          <div className="bg-white rounded-xl p-6 w-[90%] max-w-md shadow-lg relative">
            <h2 className="text-lg font-bold mb-4">
              Editar jornada de {diaSelecionado}
            </h2>

            <div className="grid grid-cols-2 gap-4 mb-4 text-sm">
              <label className="flex flex-col">
                Início
                <input
                  type="time"
                  name="horario_inicio"
                  value={formData.horario_inicio}
                  onChange={handleChange}
                  className="border rounded px-2 py-1 mt-1"
                />
              </label>
              <label className="flex flex-col">
                Pausa
                <input
                  type="time"
                  name="horario_pausa"
                  value={formData.horario_pausa}
                  onChange={handleChange}
                  className="border rounded px-2 py-1 mt-1"
                />
              </label>
              <label className="flex flex-col">
                Retorno
                <input
                  type="time"
                  name="horario_retorno"
                  value={formData.horario_retorno}
                  onChange={handleChange}
                  className="border rounded px-2 py-1 mt-1"
                />
              </label>
              <label className="flex flex-col">
                Fim
                <input
                  type="time"
                  name="horario_fim"
                  value={formData.horario_fim}
                  onChange={handleChange}
                  className="border rounded px-2 py-1 mt-1"
                />
              </label>
            </div>

            <div className="flex justify-between items-center mt-6">
              <button
                onClick={handleLimpar}
                className="text-red-600 hover:text-red-800 text-sm"
              >
                Limpar
              </button>
              <div className="space-x-2">
                <button
                  onClick={() => setModalAberto(false)}
                  className="px-4 py-1 border rounded text-gray-700"
                >
                  Cancelar
                </button>
                <button
                  onClick={handleSalvar}
                  className="px-4 py-1 bg-blue-600 text-white rounded hover:bg-blue-700"
                >
                  Salvar
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
