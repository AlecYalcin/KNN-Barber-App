import BottomNav from "../../components/BottomNav";
import Sidebar from "../../components/SidebarClient";

const BarbeiroServicos = () => {
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

      <header className="lg:flex justify-between hidden bg-blue-600 p-4 text-white fixed top-0 w-full z-50">
        <h1 className="text-3xl font-bold ml-2">Serviços Disponíveis</h1>
        <button className="mr-4">Sair</button>
      </header>

      <Sidebar/>

      <main className="flex w-full flex-col items-center p-6 lg:pl-[22px] lg:ml-64">
        <h1 className="text-2xl font-bold mt-10 flex justify-center text-gray-800 lg:hidden">
          Serviços Disponíveis
        </h1>
        <div className="w-full py-8 mt-4 grid ml-5 mr-5">
          <ul className="w-full space-y-4">
            {/* Example service item */}
            <li className="flex items-center bg-blue-500 rounded-lg shadow p-4 text-white hover:bg-blue-600 transition">
              <img
                src="https://www.temmeutamanho.com/wp-content/uploads/2024/08/cacheado-com-undercut-corte-rosto-redondo-10.webp"
                alt="Corte de Cabelo"
                className="w-16 h-16 rounded-full mr-4"
              />
              <div className="flex justify-between items-center w-full">
                <span className="text-lg font-medium text-white">
                  Corte de Cabelo
                </span>
                <span className="text-white">R$ 50,00</span>
              </div>
            </li>
            <li className="flex items-center bg-blue-500 rounded-lg shadow p-4 text-white hover:bg-blue-600 transition">
              <img
                src="https://www.temmeutamanho.com/wp-content/uploads/2024/08/cacheado-com-undercut-corte-rosto-redondo-10.webp"
                alt="Corte de Cabelo"
                className="w-16 h-16 rounded-full mr-4"
              />
              <div className="flex justify-between items-center w-full">
                <span className="text-lg font-medium text-white">
                  Corte de Cabelo
                </span>
                <span className="text-white">R$ 50,00</span>
              </div>
            </li>
            <li className="flex items-center bg-blue-500 rounded-lg shadow p-4 text-white hover:bg-blue-600 transition">
              <img
                src="https://www.temmeutamanho.com/wp-content/uploads/2024/08/cacheado-com-undercut-corte-rosto-redondo-10.webp"
                alt="Corte de Cabelo"
                className="w-16 h-16 rounded-full mr-4"
              />
              <div className="flex justify-between items-center w-full">
                <span className="text-lg font-medium text-white">
                  Corte de Cabelo
                </span>
                <span className="text-white">R$ 50,00</span>
              </div>
            </li>
          </ul>
          <div className="mt-6 flex justify-end">
            <button className="mt-6 bg-blue-600 flex justify-center items-center text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition">
              Adicionar Serviço
            </button>
          </div>
        </div>
      </main>
      <BottomNav />
    </div>
  );
};

export default BarbeiroServicos;
