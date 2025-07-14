import ButtonBack from "../../components/ButtonBack";
import BottomNav from "../../components/BottomNav";
import PhotoPerfil from "../../components/PhotoPerfil";
import { useState } from "react";
import Sidebar from "../../components/SidebarClient";
import Header from "../../components/Header";

const ClientePerfil = () => {
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
    console.log({ nome, email, telefone });
  };

  const handleDelete = () => {
    // lógica para excluir
    setEmail("");
    setTelefone("");
    setIsEditing(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 py-15 flex">
      <ButtonBack />
      <Header title={"Perfil"} />
      <Sidebar />
      <main className="flex w-full flex-col items-center p-6 lg:mt-10 lg:pl-69">
        <PhotoPerfil />

        <div className="w-full">
          <form onSubmit={handleSave} className="w-full">
            <div className="mb-4">
              <label className="block mb-1 font-medium">Nome</label>
              <input
                type="text"
                value={nome}
                onChange={(e) => setNome(e.target.value)}
                required
                disabled={!isEditing}
                className="w-full px-3 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
              />
            </div>
            <div className="mb-4">
              <label className="block mb-1 font-medium">Telefone</label>
              <input
                type="tel"
                value={telefone}
                onChange={(e) => setTelefone(e.target.value)}
                required
                disabled={!isEditing}
                className="w-full px-3 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
              />
            </div>
            <div className="mb-4">
              <label className="block mb-1 font-medium">E-mail</label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                disabled={!isEditing}
                className="w-full px-3 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
              />
            </div>
          </form>

          <div className="mt-6">
            <h2 className="text-lg font-bold mb-3 text-gray-800">
              Agendamentos
            </h2>
            <div className="bg-gray-50 rounded-lg p-3 border border-gray-200 min-h-20">
              <p className="text-sm text-gray-500">
                Nenhum agendamento recente
              </p>
            </div>
          </div>
        </div>

        <div className="flex lg:justify-end gap-2 w-full mt-5">
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
              onClick={handleSave}
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

        <BottomNav />
      </main>
    </div>
  );
};

export default ClientePerfil;
