import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import BottomNav from "../../components/BottomNav";
import Sidebar from "../../components/Sidebar";
import Header from "../../components/Header";
import { jwt_decoder } from "../../api";
import { consultar_agendamentos_por_cliente } from "../../api/models/agendamentos";

const ClienteAgendamentos = () => {
  const [agendamentos, setAgendamentos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [filtroData, setFiltroData] = useState("");
  const [filtroStatus, setFiltroStatus] = useState("todos");
  const [agendamentoSelecionado, setAgendamentoSelecionado] = useState(null);

  // Obter dados do usuário logado
  const usuario = jwt_decoder(localStorage.getItem("usuario_token"));

  // Carregar agendamentos do cliente
  useEffect(() => {
    const carregarAgendamentos = async () => {
      try {
        setLoading(true);
        setError("");

        const data = await consultar_agendamentos_por_cliente(usuario.cpf);
        setAgendamentos(data);
      } catch (error) {
        console.error("Erro ao carregar agendamentos:", error);
        setError("Erro ao carregar agendamentos. Tente novamente.");
      } finally {
        setLoading(false);
      }
    };

    carregarAgendamentos();
  }, [usuario.cpf]);

  // Filtrar agendamentos
  const agendamentosFiltrados = agendamentos.filter((agendamento) => {
    const dataAgendamento = new Date(agendamento.horario_inicio);
    const hoje = new Date();

    // Filtro por data
    if (filtroData === "hoje") {
      return dataAgendamento.toDateString() === hoje.toDateString();
    } else if (filtroData === "semana") {
      const umaSemana = new Date(hoje.getTime() + 7 * 24 * 60 * 60 * 1000);
      return dataAgendamento >= hoje && dataAgendamento <= umaSemana;
    } else if (filtroData === "mes") {
      const umMes = new Date(
        hoje.getFullYear(),
        hoje.getMonth() + 1,
        hoje.getDate()
      );
      return dataAgendamento >= hoje && dataAgendamento <= umMes;
    }

    // Filtro por status (passado/futuro)
    if (filtroStatus === "passados") {
      return dataAgendamento < hoje;
    } else if (filtroStatus === "futuros") {
      return dataAgendamento >= hoje;
    }

    return true;
  });

  // Formatar data e hora
  const formatarDataHora = (dataString) => {
    const data = new Date(dataString);
    return data.toLocaleString("pt-BR", {
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  // Formatar apenas data
  const formatarData = (dataString) => {
    const data = new Date(dataString);
    return data.toLocaleDateString("pt-BR");
  };

  // Formatar apenas hora
  const formatarHora = (dataString) => {
    const data = new Date(dataString);
    return data.toLocaleTimeString("pt-BR", {
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  // Calcular duração do agendamento
  const calcularDuracao = (inicio, fim) => {
    const inicioDate = new Date(inicio);
    const fimDate = new Date(fim);
    const diffMs = fimDate - inicioDate;
    const diffMins = Math.round(diffMs / 60000);
    return `${diffMins} min`;
  };

  // Verificar se o agendamento é hoje
  const ehHoje = (dataString) => {
    const data = new Date(dataString);
    const hoje = new Date();
    return data.toDateString() === hoje.toDateString();
  };

  // Verificar se o agendamento é passado
  const ehPassado = (dataString) => {
    const data = new Date(dataString);
    const agora = new Date();
    return data < agora;
  };

  // Calcular valor total dos serviços
  const calcularValorTotal = (servicos) => {
    return servicos.reduce((total, servico) => total + servico.preco, 0);
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <Sidebar />
      <Header title="Meus Agendamentos" />

      <main className="flex w-full md:items-center flex-col items-center lg:mt-10 p-6 lg:pl-69">
        {loading && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
            <div className="bg-white p-4 rounded-lg">
              <p>Carregando agendamentos...</p>
            </div>
          </div>
        )}

        {error && (
          <div className="w-full max-w-4xl mb-4 p-3 bg-red-100 text-red-800 rounded-lg text-center">
            {error}
          </div>
        )}

        {/* Filtros */}
        <div className="w-full max-w-4xl mb-6 flex flex-col sm:flex-row gap-4">
          <div className="flex-1">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Filtrar por período
            </label>
            <select
              value={filtroData}
              onChange={(e) => setFiltroData(e.target.value)}
              className="w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="">Todos os períodos</option>
              <option value="hoje">Hoje</option>
              <option value="semana">Próxima semana</option>
              <option value="mes">Próximo mês</option>
            </select>
          </div>

          <div className="flex-1">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Filtrar por status
            </label>
            <select
              value={filtroStatus}
              onChange={(e) => setFiltroStatus(e.target.value)}
              className="w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="todos">Todos</option>
              <option value="futuros">Futuros</option>
              <option value="passados">Passados</option>
            </select>
          </div>
        </div>

        {/* Estatísticas */}
        <div className="w-full max-w-4xl mb-6 grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="bg-white p-4 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-800">
              Total de Agendamentos
            </h3>
            <p className="text-2xl font-bold text-blue-600">
              {agendamentosFiltrados.length}
            </p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-800">
              Agendamentos Hoje
            </h3>
            <p className="text-2xl font-bold text-green-600">
              {
                agendamentosFiltrados.filter((a) => ehHoje(a.horario_inicio))
                  .length
              }
            </p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-800">
              Próximos Agendamentos
            </h3>
            <p className="text-2xl font-bold text-orange-600">
              {
                agendamentosFiltrados.filter(
                  (a) => !ehPassado(a.horario_inicio)
                ).length
              }
            </p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-800">Valor Total</h3>
            <p className="text-2xl font-bold text-purple-600">
              R${" "}
              {agendamentosFiltrados
                .reduce((total, a) => total + calcularValorTotal(a.servicos), 0)
                .toFixed(2)}
            </p>
          </div>
        </div>

        {/* Lista de Agendamentos */}
        <div className="w-full max-w-4xl">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-bold text-gray-800">
              Meus Agendamentos ({agendamentosFiltrados.length})
            </h2>
            <Link
              to="/cliente/agendamento"
              className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors duration-200 flex items-center gap-2"
            >
              <svg
                className="w-5 h-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                />
              </svg>
              Novo Agendamento
            </Link>
          </div>

          {agendamentosFiltrados.length === 0 ? (
            <div className="bg-white p-8 rounded-lg shadow text-center">
              <p className="text-gray-500 text-lg">
                {loading ? "Carregando..." : "Nenhum agendamento encontrado"}
              </p>
              {!loading && (
                <>
                  <p className="text-gray-400 text-sm mt-2 mb-4">
                    Faça seu primeiro agendamento para começar!
                  </p>
                  <Link
                    to="/cliente/agendamento"
                    className="inline-flex items-center px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors duration-200"
                  >
                    <svg
                      className="w-5 h-5 mr-2"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2}
                        d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                      />
                    </svg>
                    Fazer Primeiro Agendamento
                  </Link>
                </>
              )}
            </div>
          ) : (
            <div className="space-y-4">
              {agendamentosFiltrados
                .sort(
                  (a, b) =>
                    new Date(a.horario_inicio) - new Date(b.horario_inicio)
                )
                .map((agendamento) => (
                  <div
                    key={agendamento.id}
                    className={`bg-white p-6 rounded-lg shadow border-l-4 cursor-pointer hover:shadow-lg transition-shadow ${
                      ehHoje(agendamento.horario_inicio)
                        ? "border-green-500"
                        : ehPassado(agendamento.horario_inicio)
                        ? "border-gray-400"
                        : "border-blue-500"
                    }`}
                    onClick={() => setAgendamentoSelecionado(agendamento)}
                  >
                    <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between">
                      <div className="flex-1">
                        <div className="flex items-center gap-4 mb-3">
                          <div className="flex-shrink-0">
                            <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                              <span className="text-blue-600 font-semibold">
                                {formatarHora(agendamento.horario_inicio)}
                              </span>
                            </div>
                          </div>

                          <div className="flex-1">
                            <h3 className="text-lg font-semibold text-gray-800">
                              {agendamento.barbeiro.nome}
                            </h3>
                            <p className="text-sm text-gray-600">
                              {formatarDataHora(agendamento.horario_inicio)} -{" "}
                              {formatarHora(agendamento.horario_fim)}
                            </p>
                            <p className="text-sm text-gray-500">
                              Duração:{" "}
                              {calcularDuracao(
                                agendamento.horario_inicio,
                                agendamento.horario_fim
                              )}
                            </p>
                          </div>
                        </div>

                        {/* Serviços */}
                        <div className="mb-3">
                          <h4 className="text-sm font-medium text-gray-700 mb-2">
                            Serviços:
                          </h4>
                          <div className="flex flex-wrap gap-2">
                            {agendamento.servicos.map((servico) => (
                              <span
                                key={servico.id}
                                className="px-3 py-1 bg-blue-100 text-blue-800 text-sm rounded-full"
                              >
                                {servico.nome} - R$ {servico.preco.toFixed(2)}
                              </span>
                            ))}
                          </div>
                        </div>
                      </div>

                      <div className="mt-4 lg:mt-0 lg:ml-4">
                        <div className="flex flex-col gap-2">
                          <span
                            className={`px-3 py-1 text-sm rounded-full text-center ${
                              ehHoje(agendamento.horario_inicio)
                                ? "bg-green-100 text-green-800"
                                : ehPassado(agendamento.horario_inicio)
                                ? "bg-gray-100 text-gray-800"
                                : "bg-blue-100 text-blue-800"
                            }`}
                          >
                            {ehHoje(agendamento.horario_inicio)
                              ? "Hoje"
                              : ehPassado(agendamento.horario_inicio)
                              ? "Realizado"
                              : formatarData(agendamento.horario_inicio)}
                          </span>

                          <div className="text-right">
                            <p className="text-lg font-bold text-gray-800">
                              R${" "}
                              {calcularValorTotal(agendamento.servicos).toFixed(
                                2
                              )}
                            </p>
                          </div>

                          {!ehPassado(agendamento.horario_inicio) && (
                            <button
                              className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 text-sm"
                              onClick={(e) => {
                                e.stopPropagation();
                                // Aqui você pode implementar a lógica de cancelamento
                                alert(
                                  "Funcionalidade de cancelamento será implementada em breve!"
                                );
                              }}
                            >
                              Cancelar
                            </button>
                          )}
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
            </div>
          )}
        </div>
      </main>

      {/* Botão flutuante para novo agendamento (mobile) */}
      <div className="lg:hidden fixed bottom-20 right-4 z-40">
        <Link
          to="/cliente/agendamento"
          className="w-14 h-14 bg-blue-600 text-white rounded-full shadow-lg hover:bg-blue-700 transition-colors duration-200 flex items-center justify-center"
          aria-label="Novo agendamento"
        >
          <svg
            className="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M12 6v6m0 0v6m0-6h6m-6 0H6"
            />
          </svg>
        </Link>
      </div>

      {/* Modal de detalhes do agendamento */}
      {agendamentoSelecionado && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg shadow-lg max-w-md w-full max-h-[90vh] overflow-y-auto">
            <div className="p-6">
              <div className="flex justify-between items-start mb-4">
                <h2 className="text-xl font-bold text-gray-800">
                  Detalhes do Agendamento
                </h2>
                <button
                  onClick={() => setAgendamentoSelecionado(null)}
                  className="text-gray-500 hover:text-gray-700"
                >
                  <svg
                    className="w-6 h-6"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                </button>
              </div>

              <div className="space-y-4">
                <div>
                  <h3 className="text-sm font-medium text-gray-500">
                    Data e Hora
                  </h3>
                  <p className="text-gray-800">
                    {formatarDataHora(agendamentoSelecionado.horario_inicio)}
                  </p>
                </div>

                <div>
                  <h3 className="text-sm font-medium text-gray-500">
                    Barbeiro
                  </h3>
                  <p className="text-gray-800">
                    {agendamentoSelecionado.barbeiro.nome}
                  </p>
                  <p className="text-sm text-gray-600">
                    {agendamentoSelecionado.barbeiro.telefone}
                  </p>
                </div>

                <div>
                  <h3 className="text-sm font-medium text-gray-500">
                    Serviços
                  </h3>
                  <ul className="space-y-2">
                    {agendamentoSelecionado.servicos.map((servico) => (
                      <li key={servico.id} className="flex justify-between">
                        <span className="text-gray-800">{servico.nome}</span>
                        <span className="text-gray-600">
                          R$ {servico.preco.toFixed(2)}
                        </span>
                      </li>
                    ))}
                  </ul>
                </div>

                <div className="border-t pt-4">
                  <div className="flex justify-between items-center">
                    <h3 className="text-lg font-semibold text-gray-800">
                      Total
                    </h3>
                    <span className="text-xl font-bold text-gray-800">
                      R${" "}
                      {calcularValorTotal(
                        agendamentoSelecionado.servicos
                      ).toFixed(2)}
                    </span>
                  </div>
                </div>

                {!ehPassado(agendamentoSelecionado.horario_inicio) && (
                  <button
                    className="w-full mt-4 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700"
                    onClick={() => {
                      alert(
                        "Funcionalidade de cancelamento será implementada em breve!"
                      );
                      setAgendamentoSelecionado(null);
                    }}
                  >
                    Cancelar Agendamento
                  </button>
                )}
              </div>
            </div>
          </div>
        </div>
      )}

      <BottomNav />
    </div>
  );
};

export default ClienteAgendamentos;
