import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import BottomNav from "../../components/BottomNav";
import Header from "../../components/Header";
import Sidebar from "../../components/Sidebar";
import { jwt_decoder } from "../../api";
import { consultar_agendamentos_por_barbeiro } from "../../api/models/agendamentos";

const BarbeiroHome = () => {
  const [agendamentos, setAgendamentos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  
  // Obter dados do usuário logado
  const usuario = jwt_decoder(localStorage.getItem("usuario_token"));

  // Carregar agendamentos do barbeiro
  useEffect(() => {
    const carregarAgendamentos = async () => {
      try {
        setLoading(true);
        setError("");
        
        const data = await consultar_agendamentos_por_barbeiro(usuario.cpf);
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

  // Calcular estatísticas
  const hoje = new Date();
  const agendamentosHoje = agendamentos.filter(a => {
    const dataAgendamento = new Date(a.horario_inicio);
    return dataAgendamento.toDateString() === hoje.toDateString();
  });
  
  const agendamentosFuturos = agendamentos.filter(a => {
    const dataAgendamento = new Date(a.horario_inicio);
    return dataAgendamento > hoje;
  });

  const agendamentosPassados = agendamentos.filter(a => {
    const dataAgendamento = new Date(a.horario_inicio);
    return dataAgendamento < hoje;
  });

  // Formatar data e hora
  const formatarDataHora = (dataString) => {
    const data = new Date(dataString);
    return data.toLocaleString('pt-BR', {
      day: '2-digit',
      month: '2-digit',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  // Verificar se o agendamento é hoje
  const ehHoje = (dataString) => {
    const data = new Date(dataString);
    return data.toDateString() === hoje.toDateString();
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <Sidebar />
      <Header title="Dashboard" />
      
      <main className="flex w-full md:items-center flex-col items-center lg:mt-10 p-6 lg:pl-69">
        {loading && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
            <div className="bg-white p-4 rounded-lg">
              <p>Carregando...</p>
            </div>
          </div>
        )}

        {error && (
          <div className="w-full max-w-4xl mb-4 p-3 bg-red-100 text-red-800 rounded-lg text-center">
            {error}
          </div>
        )}

        {/* Boas-vindas */}
        <div className="w-full max-w-4xl mb-8">
          <div className="bg-gradient-to-r from-blue-600 to-blue-800 text-white p-6 rounded-lg shadow-lg">
            <h1 className="text-2xl font-bold mb-2">
              Olá, {usuario?.nome || "Barbeiro"}! 👋
            </h1>
            <p className="text-blue-100">
              Bem-vindo ao seu dashboard. Aqui você pode gerenciar seus agendamentos e serviços.
            </p>
          </div>
        </div>

        {/* Estatísticas */}
        <div className="w-full max-w-4xl mb-8 grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="bg-white p-6 rounded-lg shadow">
            <div className="flex items-center">
              <div className="p-3 bg-blue-100 rounded-full">
                <span className="text-blue-600 text-xl">📅</span>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Total</p>
                <p className="text-2xl font-bold text-gray-900">{agendamentos.length}</p>
              </div>
            </div>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <div className="flex items-center">
              <div className="p-3 bg-green-100 rounded-full">
                <span className="text-green-600 text-xl">🎯</span>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Hoje</p>
                <p className="text-2xl font-bold text-gray-900">{agendamentosHoje.length}</p>
              </div>
            </div>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <div className="flex items-center">
              <div className="p-3 bg-orange-100 rounded-full">
                <span className="text-orange-600 text-xl">⏰</span>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Futuros</p>
                <p className="text-2xl font-bold text-gray-900">{agendamentosFuturos.length}</p>
              </div>
            </div>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <div className="flex items-center">
              <div className="p-3 bg-gray-100 rounded-full">
                <span className="text-gray-600 text-xl">✅</span>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Realizados</p>
                <p className="text-2xl font-bold text-gray-900">{agendamentosPassados.length}</p>
              </div>
            </div>
          </div>
        </div>

        {/* Ações rápidas */}
        <div className="w-full max-w-4xl mb-8">
          <h2 className="text-xl font-bold mb-4 text-gray-800">Ações Rápidas</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <Link
              to="/barbeiro/agendamentos"
              className="bg-white p-6 rounded-lg shadow hover:shadow-lg transition-shadow duration-200 border-l-4 border-blue-500"
            >
              <div className="flex items-center">
                <span className="text-2xl mr-3">📅</span>
                <div>
                  <h3 className="font-semibold text-gray-800">Ver Agendamentos</h3>
                  <p className="text-sm text-gray-600">Visualizar todos os agendamentos</p>
                </div>
              </div>
            </Link>

            <Link
              to="/servicos/cadastrar"
              className="bg-white p-6 rounded-lg shadow hover:shadow-lg transition-shadow duration-200 border-l-4 border-green-500"
            >
              <div className="flex items-center">
                <span className="text-2xl mr-3">✂️</span>
                <div>
                  <h3 className="font-semibold text-gray-800">Cadastrar Serviços</h3>
                  <p className="text-sm text-gray-600">Adicionar novos serviços</p>
                </div>
              </div>
            </Link>

            <Link
              to="/barbeiro/perfil"
              className="bg-white p-6 rounded-lg shadow hover:shadow-lg transition-shadow duration-200 border-l-4 border-purple-500"
            >
              <div className="flex items-center">
                <span className="text-2xl mr-3">👤</span>
                <div>
                  <h3 className="font-semibold text-gray-800">Meu Perfil</h3>
                  <p className="text-sm text-gray-600">Gerenciar informações pessoais</p>
                </div>
              </div>
            </Link>
          </div>
        </div>

        {/* Próximos agendamentos */}
        <div className="w-full max-w-4xl">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-bold text-gray-800">Próximos Agendamentos</h2>
            <Link
              to="/barbeiro/agendamentos"
              className="text-blue-600 hover:text-blue-800 text-sm font-medium"
            >
              Ver todos →
            </Link>
          </div>
          
          {agendamentosFuturos.length === 0 ? (
            <div className="bg-white p-8 rounded-lg shadow text-center">
              <p className="text-gray-500 text-lg">Nenhum agendamento futuro</p>
              <p className="text-gray-400 text-sm mt-2">Seus próximos agendamentos aparecerão aqui</p>
            </div>
          ) : (
            <div className="space-y-4">
              {agendamentosFuturos
                .sort((a, b) => new Date(a.horario_inicio) - new Date(b.horario_inicio))
                .slice(0, 3)
                .map((agendamento) => (
                  <div
                    key={agendamento.id}
                    className={`bg-white p-4 rounded-lg shadow border-l-4 ${
                      ehHoje(agendamento.horario_inicio)
                        ? 'border-green-500'
                        : 'border-blue-500'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center">
                        <div className="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center mr-3">
                          <span className="text-blue-600 font-semibold text-sm">
                            {new Date(agendamento.horario_inicio).toLocaleTimeString('pt-BR', {
                              hour: '2-digit',
                              minute: '2-digit'
                            })}
                          </span>
                        </div>
                        <div>
                          <h3 className="font-semibold text-gray-800">
                            {agendamento.cliente.nome}
                          </h3>
                          <p className="text-sm text-gray-600">
                            {formatarDataHora(agendamento.horario_inicio)}
                          </p>
                          <p className="text-xs text-gray-500">
                            {agendamento.servicos.map(s => s.nome).join(', ')}
                          </p>
                        </div>
                      </div>
                      
                      <span
                        className={`px-2 py-1 text-xs rounded-full ${
                          ehHoje(agendamento.horario_inicio)
                            ? 'bg-green-100 text-green-800'
                            : 'bg-blue-100 text-blue-800'
                        }`}
                      >
                        {ehHoje(agendamento.horario_inicio) ? 'Hoje' : 'Futuro'}
                      </span>
                    </div>
                  </div>
                ))}
            </div>
          )}
        </div>
      </main>
      
      <BottomNav />
    </div>
  );
};

export default BarbeiroHome; 