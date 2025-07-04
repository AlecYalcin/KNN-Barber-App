import { useState } from 'react';
import ButtonBack from '../../components/ButtonBack';
import BottomNav from '../../components/BottomNav';


const AddBarbeiro = () => {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [telefone, setTelefone] = useState("");
  const [isEditing, setIsEditing] = useState(false);
  

  const handleEdit = () => {
    setIsEditing(true);
  };

  const handleSave = (e) => {
    e.preventDefault();
    setIsEditing(false);
    // lógica para salvar
    console.log({ nome, descricao, valor, imagem });
  };

  const handleDelete = () => {
    // lógica para excluir
    setNome("");
    setEmail("");
    setTelefone("");
    setIsEditing(false);
  };

  return (
    <div className="flex flex-col items-center min-h-screen bg-gray-100 py-10">
      <ButtonBack/>
      <main className="w-full max-w-md p-5 mt-10">
        <h2 className="text-2xl font-bold mb-8 text-center text-gray-800">Adicionar Barbeiro</h2>
        <form onSubmit={handleSave} className="w-full">
          <div className="mb-6">
            <label className="block text-gray-700 font-semibold mb-2">Nome:</label>
            <input
              type="text"
              name="nome"
              value={nome}
              onChange={(e) => setNome(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
              placeholder="Digite o nome"
              disabled={!isEditing}
            />
          </div>
          <div className="mb-6">
            <label className="block text-gray-700 font-semibold mb-2">Email:</label>
            <input
              type="email"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
              placeholder="Digite o email"
              disabled={!isEditing}
            />
          </div>
          <div className="mb-8">
            <label className="block text-gray-700 font-semibold mb-2">Telefone:</label>
            <input
              type="tel"
              name="telefone"
              value={telefone}
              onChange={(e) => setTelefone(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
              placeholder="Digite o telefone"
              disabled={!isEditing}
            />
          </div>
          <div className="flex lg:justify-end gap-2 w-full">
            {!isEditing && (
              <button
                type="button"
                onClick={handleEdit}
                className="w-full py-3 bg-blue-600 text-white rounded-md font-bold text-lg hover:bg-blue-700 transition-colors lg:flex lg:justify-center lg:w-30"
              >
                Editar
              </button>
            )}
            {isEditing && (
              <button
                type="submit"
                className="w-full py-3 bg-green-600 text-white rounded-md font-bold text-lg hover:bg-green-700 transition-colors lg:flex lg:justify-center lg:w-30"
              >
                Salvar
              </button>
            )}
            <button
              type="button"
              onClick={handleDelete}
              className="w-full py-3 bg-red-600 text-white rounded-md font-bold text-lg hover:bg-red-700 transition-colors lg:flex lg:justify-center lg:w-30"
            >
              Excluir
            </button>
          </div>
        </form>
        <BottomNav/>
      </main>
    </div>
  );
};

export default AddBarbeiro;