import { Link } from 'react-router-dom';
import ButtonBack from '../../components/ButtonBack';
import BottomNav from '../../components/BottomNav';
import Sidebar from '../../components/SidebarClient';

// Exemplo de dados de barbeiros
const barbeiros = [
  { id: 1, nome: 'João Silva' },
  { id: 2, nome: 'Carlos Souza' },
  { id: 3, nome: 'Pedro Santos' },
];

const ListBarbeiro = () => {
  return (
    <div className="min-h-screen bg-gray-100 py-10 flex">
      <ButtonBack/>

      <header className="lg:flex justify-between hidden bg-blue-600 p-4 text-white fixed top-0 w-full z-50">
        <h1 className="text-3xl font-bold ml-2">Barbeiros</h1>
        <button className="mr-4">Sair</button>
      </header>

      <Sidebar />

      <main className='w-full p-5 mt-10 lg:pl-69'>
        <h2 className="text-2xl font-bold mb-6 text-center lg:hidden">Barbeiros Cadastrados</h2>
        <ul className="divide-y divide-gray-200">
          {barbeiros.map((barbeiro) => (
            <li key={barbeiro.id} className="flex items-center py-4">
              <span className="flex-1 text-base">{barbeiro.nome}</span>
              <Link to={`/barbeiro/adicionar/${barbeiro.id}`} className="ml-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-6 w-6 text-blue-600 hover:text-blue-800"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M12 2a10 10 0 100 20 10 10 0 000-20z" />
                </svg>
              </Link>
            </li>
          ))}
        </ul>
        <div className="mt-8 flex justify-center">
          <Link to="/barbeiro/adicionar">
            <button className="px-6 py-2 bg-green-600 text-white rounded hover:bg-green-700 font-semibold">
              Novo Barbeiro
            </button>
          </Link>
        </div>
      </main>
      <BottomNav/>
    </div>
  );
};

export default ListBarbeiro;