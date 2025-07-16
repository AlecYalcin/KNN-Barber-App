import { useState, useEffect, useRef } from "react";
import BottomNav from "../../components/BottomNav";
import Sidebar from "../../components/SidebarClient";
import Header from "../../components/Header";
import { usePDF } from "react-to-pdf";
import { jwt_decoder } from "../../api/index";

// Dados mockados de agendamentos
const mockAppointments = [
  {
    id: 1,
    date: "2023-05-15",
    services: ["Corte de Cabelo", "Barba"],
    total: 50.0,
    paymentStatus: "Pago",
    paymentMethod: "Cartão de Crédito",
    professional: "João Silva",
    details: "Corte social com degradê e barba feita com toalha quente",
  },
  {
    id: 1,
    date: "2023-05-15",
    services: ["Corte de Cabelo", "Barba"],
    total: 50.0,
    paymentStatus: "Pago",
    paymentMethod: "Cartão de Crédito",
    professional: "João Silva",
    details: "Corte social com degradê e barba feita com toalha quente",
  },
  {
    id: 1,
    date: "2023-05-15",
    services: ["Corte de Cabelo", "Barba"],
    total: 50.0,
    paymentStatus: "Pago",
    paymentMethod: "Cartão de Crédito",
    professional: "João Silva",
    details: "Corte social com degradê e barba feita com toalha quente",
  },
  {
    id: 1,
    date: "2023-05-15",
    services: ["Corte de Cabelo", "Barba"],
    total: 50.0,
    paymentStatus: "Pago",
    paymentMethod: "Cartão de Crédito",
    professional: "João Silva",
    details: "Corte social com degradê e barba feita com toalha quente",
  },
  {
    id: 1,
    date: "2023-05-15",
    services: ["Corte de Cabelo", "Barba"],
    total: 50.0,
    paymentStatus: "Pago",
    paymentMethod: "Cartão de Crédito",
    professional: "João Silva",
    details: "Corte social com degradê e barba feita com toalha quente",
  },
  // Adicione mais agendamentos conforme necessário
];

// Tipos de serviços disponíveis para filtro
const serviceTypes = [
  "Todos",
  "Corte de Cabelo",
  "Barba",
  "Sobrancelha",
  "Hidratação",
];

export default function ClientePagamentos() {
  const usuario = jwt_decoder(localStorage.getItem("usuario_token"));
  const [appointments] = useState(mockAppointments);
  const [filteredAppointments, setFilteredAppointments] =
    useState(mockAppointments);
  const [selectedAppointment, setSelectedAppointment] = useState(null);
  const [selectedService, setSelectedService] = useState("Todos");
  const [dateRange, setDateRange] = useState({ start: "", end: "" });

  // Configuração do PDF
  const { toPDF, targetRef } = usePDF({
    filename: "historico-agendamentos.pdf",
    page: { margin: 20 },
  });

  // Filtra os agendamentos quando os critérios mudam
  useEffect(() => {
    let filtered = [...appointments];

    // Filtro por tipo de serviço
    if (selectedService !== "Todos") {
      filtered = filtered.filter((appointment) =>
        appointment.services.includes(selectedService)
      );
    }

    // Filtro por período
    if (dateRange.start && dateRange.end) {
      filtered = filtered.filter((appointment) => {
        const appointmentDate = new Date(appointment.date);
        const startDate = new Date(dateRange.start);
        const endDate = new Date(dateRange.end);

        return appointmentDate >= startDate && appointmentDate <= endDate;
      });
    }

    setFilteredAppointments(filtered);
  }, [selectedService, dateRange, appointments]);

  // Formata data para exibição
  const formatDate = (dateString) => {
    const options = { day: "2-digit", month: "2-digit", year: "numeric" };
    return new Date(dateString).toLocaleDateString("pt-BR", options);
  };

  return (
    <div className="min-h-screen bg-gray-100 py-10 flex">
      <button
        className="absolute top-8 left-4 flex items-center text-blue-600 hover:text-blue-800 transition focus:outline-none"
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

      <Header title="Histórico de Agendamentos" />

      <Sidebar />

      <div className="w-full lg:pl-[22px] py-8 mt-4 grid ml-5 mr-5 lg:ml-64">
        <h1 className="text-2xl lg:hidden font-bold mb-5 flex justify-center text-gray-800">
          Histórico de Agendamentos
        </h1>

        {/* Filtros */}
        <div className="bg-white rounded-lg shadow p-4 mb-6">
          <h2 className="text-lg font-semibold mb-4 text-gray-700">
            Filtrar Histórico
          </h2>

          <div className="grid md:grid-cols-3 gap-4">
            {/* Filtro por tipo de serviço */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Tipo de Serviço
              </label>
              <select
                className="w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                value={selectedService}
                onChange={(e) => setSelectedService(e.target.value)}
              >
                {serviceTypes.map((service) => (
                  <option key={service} value={service}>
                    {service}
                  </option>
                ))}
              </select>
            </div>

            {/* Filtro por período */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Data Inicial
              </label>
              <input
                type="date"
                className="w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                value={dateRange.start}
                onChange={(e) =>
                  setDateRange({ ...dateRange, start: e.target.value })
                }
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Data Final
              </label>
              <input
                type="date"
                className="w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                value={dateRange.end}
                onChange={(e) =>
                  setDateRange({ ...dateRange, end: e.target.value })
                }
              />
            </div>
          </div>

          {/* Botão para limpar filtros */}
          <button
            className="mt-4 text-blue-600 hover:text-blue-800 text-sm font-medium"
            onClick={() => {
              setSelectedService("Todos");
              setDateRange({ start: "", end: "" });
            }}
          >
            Limpar Filtros
          </button>
        </div>

        {/* Botão de exportação para PDF */}
        <div className="flex justify-end mb-4">
          <button
            onClick={() => toPDF()}
            className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition"
          >
            Exportar para PDF
          </button>
        </div>

        {/* Área que será convertida para PDF */}
        <div ref={targetRef} className="bg-white p-4 rounded-lg shadow">
          <h1 className="text-2xl font-bold mb-4 text-center">
            Histórico de Agendamentos do Cliente {usuario.nome}
          </h1>

          {/* Informações de filtro */}
          <div className="mb-4 text-sm">
            {selectedService !== "Todos" && (
              <p>
                <strong>Serviço:</strong> {selectedService}
              </p>
            )}
            {dateRange.start && dateRange.end && (
              <p>
                <strong>Período:</strong> {formatDate(dateRange.start)} até{" "}
                {formatDate(dateRange.end)}
              </p>
            )}
          </div>

          {/* Tabela de agendamentos */}
          <table className="w-full border-collapse mb-4">
            <thead>
              <tr className="bg-gray">
                <th className="p-2 border text-left">Data</th>
                <th className="p-2 border text-left">Serviços</th>
                <th className="p-2 border text-left">Profissional</th>
                <th className="p-2 border text-left">Valor</th>
                <th className="p-2 border text-left">Status</th>
              </tr>
            </thead>
            <tbody>
              {filteredAppointments.map((appointment) => (
                <tr key={appointment.id}>
                  <td className="p-2 border">{formatDate(appointment.date)}</td>
                  <td className="p-2 border">
                    {appointment.services.join(", ")}
                  </td>
                  <td className="p-2 border">{appointment.professional}</td>
                  <td className="p-2 border">
                    R$ {appointment.total.toFixed(2)}
                  </td>
                  <td className="p-2 border">
                    <span
                      className={`px-2 py-1 text-xs rounded-full ${
                        appointment.paymentStatus === "Pago"
                          ? "bg-green text-green"
                          : "bg-yellow text-yellow"
                      }`}
                    >
                      {appointment.paymentStatus}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          {/* Resumo */}
          <div className="text-right">
            <p>
              <strong>Total de agendamentos:</strong>{" "}
              {filteredAppointments.length}
            </p>
            <p>
              <strong>Valor total:</strong> R${" "}
              {filteredAppointments
                .reduce((sum, a) => sum + a.total, 0)
                .toFixed(2)}
            </p>
          </div>
        </div>

        {/* Lista de agendamentos (para visualização na tela) */}
        <div className="space-y-4 mt-6">
          {filteredAppointments.length === 0 ? (
            <div className="bg-white rounded-lg shadow p-6 text-center text-gray-500">
              Nenhum agendamento encontrado com os filtros selecionados.
            </div>
          ) : (
            filteredAppointments.map((appointment) => (
              <div
                key={appointment.id}
                className="bg-white rounded-lg shadow p-4 hover:bg-gray-50 transition cursor-pointer"
                onClick={() => setSelectedAppointment(appointment)}
              >
                <div className="flex justify-between items-start">
                  <div>
                    <h3 className="text-lg font-medium text-gray-700">
                      {formatDate(appointment.date)}
                    </h3>
                    <p className="text-gray-600">
                      {appointment.services.join(", ")}
                    </p>
                  </div>
                  <div className="text-right">
                    <span className="block font-semibold text-gray-700">
                      R$ {appointment.total.toFixed(2).replace(".", ",")}
                    </span>
                    <span
                      className={`inline-block px-2 py-1 text-xs rounded-full ${
                        appointment.paymentStatus === "Pago"
                          ? "bg-green-100 text-green-800"
                          : "bg-yellow-100 text-yellow-800"
                      }`}
                    >
                      {appointment.paymentStatus}
                    </span>
                  </div>
                </div>
              </div>
            ))
          )}
        </div>

        {/* Modal de detalhes do agendamento */}
        {selectedAppointment && (
          <div className="fixed inset-0 backdrop-blur-xs bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg shadow-lg max-w-md w-full max-h-[90vh] overflow-y-auto">
              <div className="p-6">
                <div className="flex justify-between items-start mb-4">
                  <h2 className="text-xl font-bold text-gray-800">
                    Detalhes do Agendamento
                  </h2>
                  <button
                    onClick={() => setSelectedAppointment(null)}
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
                    <h3 className="text-sm font-medium text-gray-500">Data</h3>
                    <p className="text-gray-800">
                      {formatDate(selectedAppointment.date)}
                    </p>
                  </div>

                  <div>
                    <h3 className="text-sm font-medium text-gray-500">
                      Profissional
                    </h3>
                    <p className="text-gray-800">
                      {selectedAppointment.professional}
                    </p>
                  </div>

                  <div>
                    <h3 className="text-sm font-medium text-gray-500">
                      Serviços
                    </h3>
                    <ul className="list-disc pl-5 text-gray-800">
                      {selectedAppointment.services.map((service, index) => (
                        <li key={index}>{service}</li>
                      ))}
                    </ul>
                  </div>

                  <div>
                    <h3 className="text-sm font-medium text-gray-500">
                      Detalhes
                    </h3>
                    <p className="text-gray-800">
                      {selectedAppointment.details}
                    </p>
                  </div>

                  <div>
                    <h3 className="text-sm font-medium text-gray-500">
                      Valor Total
                    </h3>
                    <p className="text-gray-800">
                      R${" "}
                      {selectedAppointment.total.toFixed(2).replace(".", ",")}
                    </p>
                  </div>

                  <div>
                    <h3 className="text-sm font-medium text-gray-500">
                      Status do Pagamento
                    </h3>
                    <p
                      className={`inline-block px-2 py-1 rounded-full ${
                        selectedAppointment.paymentStatus === "Pago"
                          ? "bg-green-100 text-green-800"
                          : "bg-yellow-100 text-yellow-800"
                      }`}
                    >
                      {selectedAppointment.paymentStatus}
                    </p>
                  </div>

                  <div>
                    <h3 className="text-sm font-medium text-gray-500">
                      Forma de Pagamento
                    </h3>
                    <p className="text-gray-800">
                      {selectedAppointment.paymentMethod}
                    </p>
                  </div>
                </div>

                <div className="mt-6 flex justify-end">
                  <button
                    onClick={() => setSelectedAppointment(null)}
                    className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition"
                  >
                    Fechar
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      <BottomNav />
    </div>
  );
}
