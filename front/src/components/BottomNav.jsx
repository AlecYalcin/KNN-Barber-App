import { Link } from "react-router-dom";
import { jwt_decoder } from "../api";

export default function BottomNav() {
  const usuario = jwt_decoder(localStorage.getItem("usuario_token"));
  const isBarbeiro = usuario?.eh_barbeiro;

  return (
    <div className="lg:hidden bg-white border-t border-gray-200 p-3 fixed bottom-0 left-0 right-0">
      <nav
        className="flex justify-around"
        aria-label="Menu de navegação inferior"
      >
        {isBarbeiro ? (
          // Navegação para barbeiros
          <>
            <Link
              to="/barbeiro/home"
              className="flex flex-col items-center text-gray-500 hover:text-blue-600"
              aria-label="Dashboard"
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
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                />
              </svg>
              <span className="text-xs mt-1">Dashboard</span>
            </Link>

            <Link
              to="/barbeiro/agendamentos"
              className="flex flex-col items-center text-gray-500 hover:text-blue-600"
              aria-label="Meus agendamentos"
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
              <span className="text-xs mt-1">Agendamentos</span>
            </Link>

            <Link
              to="/servicos/cadastrar"
              className="flex flex-col items-center text-gray-500 hover:text-blue-600"
              aria-label="Cadastrar serviços"
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
              <span className="text-xs mt-1">Serviços</span>
            </Link>

            <Link
              to="/barbeiro/perfil"
              className="flex flex-col items-center text-gray-500 hover:text-blue-600"
              aria-label="Perfil do barbeiro"
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
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                />
              </svg>
              <span className="text-xs mt-1">Perfil</span>
            </Link>
          </>
        ) : (
          // Navegação para clientes
          <>
            <Link
              to="/home"
              className="flex flex-col items-center text-gray-500 hover:text-blue-600"
              aria-label="Página inicial"
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
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                />
              </svg>
              <span className="text-xs mt-1">Home</span>
            </Link>

            <Link
              to="/cliente/agendamento"
              className="flex flex-col items-center text-gray-500 hover:text-blue-600"
              aria-label="Agendar horário"
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
              <span className="text-xs mt-1">Agendar</span>
            </Link>

            <Link
              to="/cliente/agendamentos"
              className="flex flex-col items-center text-gray-500 hover:text-blue-600"
              aria-label="Meus agendamentos"
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
              <span className="text-xs mt-1">Agendamentos</span>
            </Link>

            <Link
              to="/pagamentos"
              className="flex flex-col items-center text-gray-500 hover:text-blue-600"
              aria-label="Página de pagamento"
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
                  d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"
                />
              </svg>
              <span className="text-xs mt-1">Pagar</span>
            </Link>

            <Link
              to="/perfil"
              className="flex flex-col items-center text-gray-500 hover:text-blue-600"
              aria-label="Perfil do usuário"
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
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                />
              </svg>
              <span className="text-xs mt-1">Perfil</span>
            </Link>
          </>
        )}
      </nav>
    </div>
  );
}
