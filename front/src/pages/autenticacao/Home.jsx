import { useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import BottomNav from "../../components/BottomNav";
import Header from "../../components/Header";
import ServicosHorarios from "../../components/ScrollHome";
import Sidebar from "../../components/SidebarClient";

// API
import { jwt_decoder } from "../../api/index";

const Home = () => {
  const navigate = useNavigate();
  const usuario = jwt_decoder(localStorage.getItem("usuario_token"));

  useEffect(() => {
    // Se o usuário é barbeiro, redireciona para a home do barbeiro
    if (usuario?.eh_barbeiro) {
      navigate("/barbeiro/home");
    }
  }, [usuario, navigate]);

  // Se não é barbeiro, mostra a home do cliente
  return (
    <div className="mt-15 ml-5 lg:ml-0 mr-5">
      <Header title="KNN Barber" />
      <Sidebar />
      
      {/* Botões de ação rápida */}
      <div className="lg:pl-69 lg:mt-30 mb-6">
        <div className="flex flex-col sm:flex-row gap-4 p-4">
          <Link
            to="/cliente/agendamento"
            className="flex-1 bg-blue-600 text-white p-4 rounded-lg hover:bg-blue-700 transition-colors duration-200 flex items-center justify-center gap-3"
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
            <span className="text-lg font-semibold">Fazer Agendamento</span>
          </Link>
          
          <Link
            to="/cliente/agendamentos"
            className="flex-1 bg-green-600 text-white p-4 rounded-lg hover:bg-green-700 transition-colors duration-200 flex items-center justify-center gap-3"
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
                d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
              />
            </svg>
            <span className="text-lg font-semibold">Meus Agendamentos</span>
          </Link>
        </div>
      </div>
      
      <ServicosHorarios />
      <BottomNav />
    </div>
  );
};

export default Home;
