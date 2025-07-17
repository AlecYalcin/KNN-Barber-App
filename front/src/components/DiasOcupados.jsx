import { useState, useEffect } from "react";

// API
import { horario_ocupado, jwt_decoder } from "../api";

const DiasOcupados = () => {
  const [diasOcupados, setDiasOcupados] = useState([]);
  const [modalAberto, setModalAberto] = useState(false);
  const [formData, setFormData] = useState({
    id: null,
    horario_inicio: "",
    horario_fim: "",
    justificativa: "",
  });

  // Função para pesquisar lista atualizada de dias
  const fetchDias = async () => {
    const usuario = jwt_decoder(localStorage.getItem("usuario_token"));
    const data = await horario_ocupado.listar_horarios_ocupados_do_barbeiro(
      usuario.cpf
    );
    setDiasOcupados(data);
  };

  // Recuperando horários ocupados
  useEffect(() => {
    fetchDias();
  }, []);

  // Adicionando novos horários ocupados
  const abrirModalAdicionar = () => {
    setFormData({
      id: null,
      horario_inicio: "",
      horario_fim: "",
      justificativa: "",
    });
    setModalAberto(true);
  };

  // Editando um horário ocupado existente
  const abrirModalEditar = (dia) => {
    setFormData({
      id: dia.id,
      horario_inicio: dia.horario_inicio,
      horario_fim: dia.horario_fim,
      justificativa: dia.justificativa,
    });
    setModalAberto(true);
  };

  const fecharModal = () => {
    setModalAberto(false);
  };

  // Editando um horário ocupado existente
  const handleChange = (e) => {
    setFormData((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  // Adicionando novos horários ocupados
  const handleSubmit = async (e) => {
    e.preventDefault();
    const usuario = jwt_decoder(localStorage.getItem("usuario_token"));

    var data = {};
    if (formData.id) {
      data = await horario_ocupado.alterar_horario_ocupado(
        formData.id,
        formData.horario_inicio,
        formData.horario_fim,
        formData.justificativa
      );
    } else {
      data = await horario_ocupado.criar_horario_ocupado(
        usuario.cpf,
        formData.horario_inicio,
        formData.horario_fim,
        formData.justificativa
      );
    }

    if (data.mensagem) {
      alert(data.mensagem);
    }
    if (data.error) {
      return;
    }

    fetchDias();
    fecharModal();
  };

  // Removendo horários ocupados
  const handleExcluirHorario = async (horario_id) => {
    const data = await horario_ocupado.remover_horario_ocupado(horario_id);

    alert(data.mensagem);
    if (data.error) {
      alert(data.mensagem);
      return;
    }

    fetchDias();
  };

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
              <button
                className="text-blue-600 text-sm hover:underline"
                onClick={() => abrirModalEditar(dia)}
              >
                Editar
              </button>
              <button
                className="text-red-600 text-sm hover:underline"
                onClick={() => handleExcluirHorario(dia.id)}
              >
                Excluir
              </button>
            </div>
          </div>
        ))}
      </div>

      <div className="flex justify-end">
        <button
          className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 mt-6 text-sm"
          onClick={abrirModalAdicionar}
        >
          Adicionar dia ocupado
        </button>
      </div>

      {/* Modal */}
      {modalAberto && (
        <div className="fixed inset-0 flex items-center justify-center z-50 backdrop-blur-xs bg-opacity-30">
          <div className="bg-white rounded-lg p-6 w-full max-w-md shadow-lg">
            <h2 className="text-lg font-semibold mb-4">
              {formData.id ? "Editar Dia Ocupado" : "Adicionar Dia Ocupado"}
            </h2>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-sm mb-1">Horário Início</label>
                <input
                  type="datetime-local"
                  name="horario_inicio"
                  value={formData.horario_inicio}
                  onChange={handleChange}
                  className="w-full border rounded px-3 py-2 text-sm"
                  required
                />
              </div>
              <div>
                <label className="block text-sm mb-1">Horário Fim</label>
                <input
                  type="datetime-local"
                  name="horario_fim"
                  value={formData.horario_fim}
                  onChange={handleChange}
                  className="w-full border rounded px-3 py-2 text-sm"
                  required
                />
              </div>
              <div>
                <label className="block text-sm mb-1">Justificativa</label>
                <input
                  type="text"
                  name="justificativa"
                  value={formData.justificativa}
                  onChange={handleChange}
                  className="w-full border rounded px-3 py-2 text-sm"
                  required
                />
              </div>
              <div className="flex justify-end gap-3 pt-2">
                <button
                  type="button"
                  onClick={fecharModal}
                  className="px-4 py-2 text-sm text-gray-600 hover:underline"
                >
                  Cancelar
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 bg-blue-600 text-white rounded text-sm hover:bg-blue-700"
                >
                  Salvar
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default DiasOcupados;
