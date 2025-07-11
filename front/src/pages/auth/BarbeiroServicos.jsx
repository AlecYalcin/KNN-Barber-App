import BottomNav from "../../components/BottomNav";
import ButtonBack from "../../components/ButtonBack";
import Header from "../../components/Header";
import Sidebar from "../../components/SidebarClient";

const BarbeiroServicos = () => {
  return (
    <div className="min-h-screen bg-gray-100 py-10 flex">
      
      <ButtonBack/>

      <Header title="Serviços Disponíveis" />

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
