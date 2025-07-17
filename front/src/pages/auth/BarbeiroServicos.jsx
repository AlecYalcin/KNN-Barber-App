import { useState } from "react";
import BottomNav from "../../components/BottomNav";
import ButtonBack from "../../components/ButtonBack";
import Header from "../../components/Header";
import Sidebar from "../../components/Sidebar";

const BarbeiroServicos = () => {
  // Estado para controlar o modal
  const [isModalOpen, setIsModalOpen] = useState(false);

  // Estado para o formulário
  const [formData, setFormData] = useState({
    nome: "",
    descricao: "",
    preco: "",
    duracao: "",
  });

  // Lista de serviços inicial
  const [servicos, setServicos] = useState([
    {
      id: 1,
      nome: "Corte de Cabelo",
      descricao: "Corte profissional com técnicas modernas",
      preco: 50.0,
      duracao: 30,
    },
    {
      id: 2,
      nome: "Barba Completa",
      descricao: "Aparo e modelagem de barba com toalha quente",
      preco: 35.0,
      duracao: 25,
    },
    {
      id: 3,
      nome: "Pigmentação",
      descricao: "Técnica para disfarçar falhas na barba",
      preco: 70.0,
      duracao: 45,
    },
  ]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Criar novo serviço
    const novoServico = {
      id: servicos.length + 1,
      nome: formData.nome,
      descricao: formData.descricao,
      preco: parseFloat(formData.preco),
      duracao: parseInt(formData.duracao),
    };

    // Adicionar à lista de serviços
    setServicos([...servicos, novoServico]);

    // Fechar modal e resetar formulário
    setIsModalOpen(false);
    setFormData({
      nome: "",
      descricao: "",
      preco: "",
      duracao: "",
    });
  };

  return (
    <div className="min-h-screen bg-gray-100 py-10 flex">
      <ButtonBack />
      <Header title="Serviços Disponíveis" />
      <Sidebar />

      <main className="flex w-full flex-col items-center p-6 lg:pl-[22px] lg:ml-64">
        <h1 className="text-2xl font-bold mt-10 flex justify-center text-gray-800 lg:hidden">
          Serviços Disponíveis
        </h1>
        <div className="w-full py-8 mt-4 grid ml-5 mr-5">
          <ul className="w-full space-y-4">
            {servicos.map((servico) => (
              <li
                key={servico.id}
                className="flex items-center bg-blue-500 rounded-lg shadow p-4 text-white hover:bg-blue-600 transition"
              >
                <div className="flex-1">
                  <div className="flex justify-between items-center">
                    <span className="text-lg font-medium text-white">
                      {servico.nome}
                    </span>
                    <span className="text-white">
                      R$ {servico.preco.toFixed(2)}
                    </span>
                  </div>
                  <p className="text-sm text-blue-100 mt-1">
                    {servico.descricao}
                  </p>
                  <p className="text-xs text-blue-200 mt-1">
                    Duração: {servico.duracao} minutos
                  </p>
                </div>
              </li>
            ))}
          </ul>
          <div className="mt-6 flex justify-end">
            <button
              onClick={() => setIsModalOpen(true)}
              className="mt-6 bg-blue-600 flex justify-center items-center text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition"
            >
              Adicionar Serviço
            </button>
          </div>
        </div>
      </main>
      <BottomNav />

      {/* Modal Popup */}
      {isModalOpen && (
        <div className="fixed inset-0 backdrop-blur-xs bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-lg shadow-xl w-full max-w-md animate-fade-in">
            <div className="p-6">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-2xl font-bold text-gray-800">
                  Adicionar Novo Serviço
                </h2>
                <button
                  onClick={() => setIsModalOpen(false)}
                  className="text-gray-500 hover:text-gray-700"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
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

              <form onSubmit={handleSubmit}>
                <div className="mb-4">
                  <label
                    htmlFor="nome"
                    className="block text-sm font-medium text-gray-700 mb-1"
                  >
                    Nome do Serviço
                  </label>
                  <input
                    type="text"
                    id="nome"
                    name="nome"
                    value={formData.nome}
                    onChange={handleInputChange}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                  />
                </div>

                <div className="mb-4">
                  <label
                    htmlFor="descricao"
                    className="block text-sm font-medium text-gray-700 mb-1"
                  >
                    Descrição
                  </label>
                  <textarea
                    id="descricao"
                    name="descricao"
                    value={formData.descricao}
                    onChange={handleInputChange}
                    rows="3"
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                  ></textarea>
                </div>

                <div className="grid grid-cols-2 gap-4 mb-4">
                  <div>
                    <label
                      htmlFor="preco"
                      className="block text-sm font-medium text-gray-700 mb-1"
                    >
                      Preço (R$)
                    </label>
                    <input
                      type="number"
                      id="preco"
                      name="preco"
                      value={formData.preco}
                      onChange={handleInputChange}
                      min="0"
                      step="0.01"
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                      required
                    />
                  </div>
                  <div>
                    <label
                      htmlFor="duracao"
                      className="block text-sm font-medium text-gray-700 mb-1"
                    >
                      Duração (minutos)
                    </label>
                    <input
                      type="number"
                      id="duracao"
                      name="duracao"
                      value={formData.duracao}
                      onChange={handleInputChange}
                      min="1"
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                      required
                    />
                  </div>
                </div>

                <div className="flex justify-end space-x-3 mt-6">
                  <button
                    type="button"
                    onClick={() => setIsModalOpen(false)}
                    className="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-100 transition"
                  >
                    Cancelar
                  </button>
                  <button
                    type="submit"
                    className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition"
                  >
                    Salvar Serviço
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default BarbeiroServicos;
