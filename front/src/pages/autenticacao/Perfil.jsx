import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import ButtonBack from "../../components/ButtonBack";
import BottomNav from "../../components/BottomNav";
import PhotoPerfil from "../../components/PhotoPerfil";
import Sidebar from "../../components/SidebarClient";
import Header from "../../components/Header";

// API
import { jwt_decoder, usuario } from "../../api/index";
import DiasOcupados from "../../components/DiasOcupados";
import JornadaDeTrabalho from "../../components/JornadaDeTrabalho";

const Perfil = () => {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [telefone, setTelefone] = useState("");
  const [CPF, setCPF] = useState("");
  const [isBarbeiro, setIsBarbeiro] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const navigate = useNavigate();

  // Recuperando informações de usuário
  useEffect(() => {
    const usuario = jwt_decoder(localStorage.getItem("usuario_token"));
    setEmail(usuario.email);
    setTelefone(usuario.telefone);
    setNome(usuario.nome);
    setCPF(usuario.cpf);
    setIsBarbeiro(usuario.eh_barbeiro);
  }, []);

  const handleEdit = () => {
    setIsEditing(true);
  };

  const handleSave = async (e) => {
    e.preventDefault();

    // Realizando alteração
    const data = await usuario.alterar_usuario(CPF, { nome, email, telefone });

    // Verificando erros
    alert(data.mensagem);
    if (data.error) {
      return;
    }

    // Em caso de sucesso, é preciso substituir o token
    localStorage.setItem("usuario_token", data.token);

    // Desativar a edição
    setIsEditing(false);
  };

  const handleDelete = async () => {
    // Desativando a edição logo no início
    setIsEditing(false);

    // Excluindo usuário
    const data = await usuario.remover_usuario(CPF);

    // Verificando erros
    alert(data.mensagem);
    if (data.error) {
      return;
    }

    // Redirecionando para a página de login
    localStorage.removeItem("usuario_token");
    navigate("/login", { replace: true });
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

          {/* Agendamentos */}
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

          {/* Jornada */}
          {isBarbeiro && (
            <div className="mt-6" disabled={!isBarbeiro}>
              <h2 className="text-lg font-bold mb-3 text-gray-800">
                Jornada de Trabalho
              </h2>
              <JornadaDeTrabalho />
            </div>
          )}

          {/* Dias Ocupados */}
          {isBarbeiro && (
            <div className="mt-6" disabled={!isBarbeiro}>
              <h2 className="text-lg font-bold mb-3 text-gray-800">
                Dias Ocupados
              </h2>
              <DiasOcupados />
            </div>
          )}
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

export default Perfil;
