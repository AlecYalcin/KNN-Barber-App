import { useState } from "react";
import BottomNav from "../../components/BottomNav";
import Sidebar from "../../components/Sidebar";
import Header from "../../components/Header";

const services = [
  { id: 1, name: "Corte de Cabelo", price: "R$ 30,00", value: 30 },
  { id: 2, name: "Barba", price: "R$ 20,00", value: 20 },
  { id: 3, name: "Sobrancelha", price: "R$ 15,00", value: 15 },
  { id: 4, name: "Hidratação", price: "R$ 25,00", value: 25 },
];

export default function ClienteServicos() {
  const [selected, setSelected] = useState([]);

  const handleSelect = (id) => {
    setSelected((prevSelected) => {
      const isAlreadySelected = prevSelected.includes(id);

      if (isAlreadySelected) {
        // Remove o id
        return prevSelected.filter((selectedId) => selectedId !== id);
      } else {
        // Adiciona o id
        return [...prevSelected, id];
      }
    });
  };

  const selectedServices = services.filter((s) => selected.includes(s.id));
  const total = selectedServices.reduce((sum, s) => sum + s.value, 0);

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

      <Header title="Serviços Disponíveis" />

      <Sidebar />

      <div className="w-full lg:pl-[22px] py-8 mt-4 grid ml-5 mr-5 lg:ml-64">
        <h1 className="text-2xl lg:hidden font-bold mb-5 flex justify-center text-gray-800">
          Serviços Disponíveis
        </h1>
        <div className="w-full space-y-4">
          {services.map((service) => (
            <div
              key={service.id}
              className="flex justify-between items-center bg-white rounded-lg shadow p-4 hover:bg-gray-50 transition"
            >
              <div className="grid">
                <span className="text-lg font-medium text-gray-700">
                  {service.name}
                </span>
                <span className="text-gray-500">{service.price}</span>
              </div>
              <input
                type="checkbox"
                className="ml-4 w-5 h-5 text-blue-600 rounded focus:ring-blue-500"
                aria-label={`Selecionar ${service.name}`}
                checked={selected.includes(service.id)}
                onChange={() => handleSelect(service.id)}
              />
            </div>
          ))}

          <div className="mt-6 grid justify-end items-center">
            <h2 className="text-xl font-semibold text-gray-800">Total</h2>
            <span className="bg-white p-4 rounded-lg shadow text-gray-700">
              R$ {total.toFixed(2).replace(".", ",")}
            </span>

            <button
              className={`w-50 bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition mt-6 mb-4 ${
                selected.length === 0 ? "opacity-50 cursor-not-allowed" : ""
              }`}
              disabled={selected.length === 0}
            >
              Próximo
            </button>
          </div>
        </div>
      </div>
      <BottomNav />
    </div>
  );
}
