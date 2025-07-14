import React, { useState } from "react";
import ButtonBack from "../../components/ButtonBack";
import BottomNav from "../../components/BottomNav";
import Sidebar from "../../components/SidebarClient";
import Header from "../../components/Header";

const AlterarServico = () => {
  const [nome, setNome] = useState("");
  const [descricao, setDescricao] = useState("");
  const [valor, setValor] = useState("");
  const [imagem, setImagem] = useState(null);
  const [isEditing, setIsEditing] = useState(false);

  const handleImagemChange = (e) => {
    setImagem(e.target.files[0]);
  };

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
    setDescricao("");
    setValor("");
    setImagem(null);
    setIsEditing(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 py-10 flex">
      <ButtonBack />

      <Header title="Info Serviços" />

      <Sidebar />

      <main className="flex w-full flex-col items-center p-6 lg:mt-10 lg:pl-69">
        <h2 className="text-center text-2xl font-bold mb-6 mt-10 lg:hidden">
          Cadastrar Serviço
        </h2>
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
            <label className="block mb-1 font-medium">Descrição</label>
            <textarea
              value={descricao}
              onChange={(e) => setDescricao(e.target.value)}
              required
              rows={3}
              disabled={!isEditing}
              className="w-full px-3 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-vertical disabled:bg-gray-100"
            />
          </div>
          <div className="mb-4">
            <label className="block mb-1 font-medium">Valor (R$)</label>
            <input
              type="number"
              value={valor}
              onChange={(e) => setValor(e.target.value)}
              required
              min="0"
              step="0.01"
              disabled={!isEditing}
              className="w-full px-3 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
            />
          </div>
          <div className="mb-6 rounded-md">
            <label className="flex font-medium mb-2">Imagem</label>

            <div className="flex items-center gap-3 bg-gray-400 py-10 rounded-md justify-center">
              <label
                htmlFor="imagem-upload"
                className={`flex items-center gap-2 px-4 py-2 border rounded-md transition-colors
                ${
                  isEditing
                    ? "bg-gray-100 border-gray-300 hover:bg-gray-200 cursor-pointer"
                    : "bg-gray-200 opacity-60 cursor-not-allowed"
                }`}
                style={{ pointerEvents: isEditing ? "auto" : "none" }}
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5 text-blue-500"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M4 16v2a2 2 0 002 2h12a2 2 0 002-2v-2M7 10l5-5m0 0l5 5m-5-5v12"
                  />
                </svg>
                <span>{imagem ? imagem.name : "Selecionar imagem"}</span>
                <input
                  id="imagem-upload"
                  type="file"
                  accept="image/*"
                  onChange={handleImagemChange}
                  disabled={!isEditing}
                  className="hidden"
                />
              </label>

              {imagem && (
                <img
                  src={URL.createObjectURL(imagem)}
                  alt="Preview"
                  className="h-10 w-10 object-cover rounded-md border"
                />
              )}
            </div>
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
      </main>
      <BottomNav />
    </div>
  );
};

export default AlterarServico;
