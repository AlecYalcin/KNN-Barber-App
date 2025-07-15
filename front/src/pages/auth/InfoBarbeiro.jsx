import ButtonBack from "../../components/ButtonBack";
import BottomNav from "../../components/BottomNav";

const InfoBarbeiro = ({ barbeiro }) => {
  const dados = barbeiro || {
    nome: "João da Silva",
    email: "joao.barbeiro@email.com",
    telefone: "(11) 91234-5678",
  };

  return (
    <div className="min-h-screen bg-gray-100 py-10 flex">
      <ButtonBack />
      <main className="flex w-full flex-col items-center p-6 lg:mt-10 lg:pl-69 mt-10">
        <div className="w-24 h-24 rounded-full bg-gradient-to-tr from-blue-700 to-green-300 flex items-center justify-center mb-6 shadow">
          <span className="text-4xl font-bold text-white">
            {dados.nome[0].toUpperCase()}
          </span>
        </div>
        <h2 className="text-2xl font-bold mb-4 text-gray-900">
          Informações do Barbeiro
        </h2>
        <ul className="w-full space-y-6 bg-blue-400 p-3 rounded-lg">
          <li className="flex items-center justify-between bg-gray-100 rounded-lg px-4 py-2">
            <span className="font-medium text-gray-600">Nome:</span>
            <span className="text-gray-900">{dados.nome}</span>
          </li>
          <li className="flex items-center justify-between bg-gray-100 rounded-lg px-4 py-2">
            <span className="font-medium text-gray-600">Email:</span>
            <span className="text-gray-900">{dados.email}</span>
          </li>
          <li className="flex items-center justify-between bg-gray-100 rounded-lg px-4 py-2">
            <span className="font-medium text-gray-600">Telefone:</span>
            <span className="text-gray-900">{dados.telefone}</span>
          </li>
        </ul>
      </main>
      <BottomNav />
    </div>
  );
};

export default InfoBarbeiro;
