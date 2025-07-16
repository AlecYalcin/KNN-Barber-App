import { useState, useEffect } from "react";
import BottomNav from "../../components/BottomNav";
import Sidebar from "../../components/SidebarClient";
import Header from "../../components/Header";
import { DayPicker } from "react-day-picker";
import { ptBR } from "date-fns/locale";
import "react-day-picker/dist/style.css";
import { agendamento, servico, barbeiro, jwt_decoder } from "../../api";

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
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  
  // Estados para dados do backend
  const [barbeiros, setBarbeiros] = useState([]);
  const [servicos, setServicos] = useState([]);
  const [barbeiroSelecionado, setBarbeiroSelecionado] = useState("");
  const [servicosSelecionados, setServicosSelecionados] = useState([]);
  const [horariosDisponiveis, setHorariosDisponiveis] = useState(HORARIOS);
  
  // Obter dados do usuário logado
  const usuario = jwt_decoder(localStorage.getItem("usuario_token"));

  // Carregar dados iniciais
  useEffect(() => {
    const carregarDados = async () => {
      try {
        setLoading(true);
        const [barbeirosData, servicosData] = await Promise.all([
          barbeiro.listar_barbeiros(),
          servico.listar_servicos()
        ]);
        setBarbeiros(barbeirosData);
        setServicos(servicosData);
      } catch (error) {
        console.error("Erro ao carregar dados:", error);
        setError("Erro ao carregar dados. Tente novamente.");
      } finally {
        setLoading(false);
      }
    };
    
    carregarDados();
  }, []);

  // Verificar horários disponíveis quando data e barbeiro são selecionados
  useEffect(() => {
    if (selectedDate && barbeiroSelecionado) {
      verificarHorariosDisponiveis();
    }
  }, [selectedDate, barbeiroSelecionado]);

  const verificarHorariosDisponiveis = async () => {
    try {
      // Aqui você pode implementar a lógica para verificar horários ocupados
      // Por enquanto, vamos usar todos os horários
      setHorariosDisponiveis(HORARIOS);
    } catch (error) {
      console.error("Erro ao verificar horários:", error);
    }
  };

  const handleSelecionarHorario = (e) => {
    setHorarioSelecionado(e.target.value);
    setConfirmado(false);
  };

  const handleSelecionarBarbeiro = (e) => {
    setBarbeiroSelecionado(e.target.value);
    setHorarioSelecionado("");
    setConfirmado(false);
  };

  const handleSelecionarServico = (servicoId) => {
    setServicosSelecionados(prev => {
      const isSelected = prev.includes(servicoId);
      if (isSelected) {
        return prev.filter(id => id !== servicoId);
      } else {
        return [...prev, servicoId];
      }
    });
    setConfirmado(false);
  };

  const handleConfirmar = async () => {
    if (!selectedDate || !horarioSelecionado || !barbeiroSelecionado || servicosSelecionados.length === 0) {
      setError("Por favor, preencha todos os campos obrigatórios.");
      return;
    }

    try {
      setLoading(true);
      setError("");
      
      // Criar data e hora de início
      const [hora, minuto] = horarioSelecionado.split(":");
      const horarioInicio = new Date(selectedDate);
      horarioInicio.setHours(parseInt(hora), parseInt(minuto), 0, 0);
      
      // Calcular horário de fim (assumindo 1 hora por agendamento)
      const horarioFim = new Date(horarioInicio);
      horarioFim.setHours(horarioInicio.getHours() + 1);

      // Formatar datas sem timezone para evitar problemas de comparação
      const formatarData = (data) => {
        return data.getFullYear() + '-' + 
               String(data.getMonth() + 1).padStart(2, '0') + '-' + 
               String(data.getDate()).padStart(2, '0') + 'T' + 
               String(data.getHours()).padStart(2, '0') + ':' + 
               String(data.getMinutes()).padStart(2, '0') + ':' + 
               String(data.getSeconds()).padStart(2, '0');
      };

      console.log("Dados do agendamento:", {
        barbeiro_cpf: barbeiroSelecionado,
        cliente_cpf: usuario.cpf,
        servicos_id: servicosSelecionados,
        horario_inicio: formatarData(horarioInicio),
        horario_fim: formatarData(horarioFim)
      });

      const resultado = await agendamento.criar_agendamento(
        barbeiroSelecionado,
        usuario.cpf,
        servicosSelecionados,
        formatarData(horarioInicio),
        formatarData(horarioFim)
      );

      if (resultado.mensagem) {
        setSuccess("Agendamento realizado com sucesso!");
        setConfirmado(true);
        // Limpar formulário
        setSelectedDate(null);
        setHorarioSelecionado("");
        setBarbeiroSelecionado("");
        setServicosSelecionados([]);
      }
    } catch (error) {
      console.error("Erro ao criar agendamento:", error);
      setError(error.message || "Erro ao criar agendamento. Tente novamente.");
    } finally {
      setLoading(false);
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
        {loading && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
            <div className="bg-white p-4 rounded-lg">
              <p>Carregando...</p>
            </div>
          </div>
        )}

        {error && (
          <div className="w-full max-w-md mb-4 p-3 bg-red-100 text-red-800 rounded-lg text-center">
            {error}
          </div>
        )}

        {success && (
          <div className="w-full max-w-md mb-4 p-3 bg-green-100 text-green-800 rounded-lg text-center">
            {success}
          </div>
        )}

        <h1 className="text-2xl font-bold mt-20 flex justify-center text-gray-800">
          Selecione o Barbeiro
        </h1>

        <div className="w-full max-w-md mt-5">
          <select
            value={barbeiroSelecionado}
            onChange={handleSelecionarBarbeiro}
            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            disabled={loading}
          >
            <option value="">Selecione um barbeiro</option>
            {barbeiros.map((barbeiro) => (
              <option key={barbeiro.cpf} value={barbeiro.cpf}>
                {barbeiro.nome}
              </option>
            ))}
          </select>
        </div>

        <h1 className="text-2xl font-bold mt-10 flex justify-center text-gray-800">
          Selecione os Serviços
        </h1>

        <div className="w-full max-w-md mt-5">
          <div className="bg-gray-100 p-4 rounded-lg shadow-lg">
            <div className="space-y-3">
              {servicos.map((servico) => (
                <label
                  key={servico.id}
                  className={`flex items-center justify-between p-3 rounded-lg border-2 cursor-pointer transition-colors
                    ${
                      servicosSelecionados.includes(servico.id)
                        ? "border-blue-500 bg-blue-50"
                        : "border-gray-200 bg-white hover:border-blue-300"
                    }
                  `}
                >
                  <div>
                    <span className="font-medium text-gray-800">{servico.nome}</span>
                    <p className="text-sm text-gray-600">{servico.descricao}</p>
                    <span className="text-sm font-semibold text-blue-600">
                      R$ {servico.preco.toFixed(2).replace(".", ",")}
                    </span>
                  </div>
                  <input
                    type="checkbox"
                    checked={servicosSelecionados.includes(servico.id)}
                    onChange={() => handleSelecionarServico(servico.id)}
                    className="w-5 h-5 text-blue-600 rounded focus:ring-blue-500"
                    disabled={loading}
                  />
                </label>
              ))}
            </div>
          </div>
        </div>

        <h1 className="text-2xl font-bold mt-10 flex justify-center text-gray-800">
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
              {horariosDisponiveis.map((hora) => (
                <label
                  key={hora}
                  className={`text-xl rounded-lg border-2 bg-white h-12 flex items-center justify-center text-gray-800 font-bold cursor-pointer transition-colors
                    ${
                      horarioSelecionado === hora
                        ? "border-blue-500 text-blue-600 bg-blue-50"
                        : "border-gray-200 hover:border-blue-300"
                    }
                    ${!selectedDate || !barbeiroSelecionado || servicosSelecionados.length === 0 ? "opacity-50 cursor-not-allowed" : ""}
                  `}
                >
                  <input
                    type="radio"
                    name="horario"
                    value={hora}
                    checked={horarioSelecionado === hora}
                    onChange={handleSelecionarHorario}
                    className="hidden"
                    disabled={!selectedDate || !barbeiroSelecionado || servicosSelecionados.length === 0}
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
                  !(selectedDate && horarioSelecionado && barbeiroSelecionado && servicosSelecionados.length > 0)
                    ? "opacity-50 cursor-not-allowed"
                    : ""
                }
              `}
              onClick={handleConfirmar}
              disabled={!(selectedDate && horarioSelecionado && barbeiroSelecionado && servicosSelecionados.length > 0) || loading}
            >
              {loading ? "Processando..." : "Confirmar Agendamento"}
            </button>
            {confirmado && selectedDate && (
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
