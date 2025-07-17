import { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Cadastro from "../pages/autenticacao/Cadastro";
import Perfil from "../pages/autenticacao/Perfil";
import Login from "../pages/autenticacao/Login";
import Home from "../pages/autenticacao/Home";
import BarbeiroAgendamentos from "../pages/agendamento/BarbeiroAgendamentos";
import ClienteAgendamentos from "../pages/agendamento/ClienteAgendamentos";
import ClienteAgendamento from "../pages/agendamento/ClienteAgendamento";
import BarbeiroServicos from "../pages/barbeiro/BarbeiroServicos";
import BarbeiroHome from "../pages/barbeiro/BarbeiroHome";

// API
import { jwt_decoder, usuario } from "../api";

export default function AppRoutes() {
  const [authenticated, setAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  // Verificando usuário
  useEffect(() => {
    // Recuperando Token Salvo
    const token = localStorage.getItem("usuario_token");

    // Não tem token? Não está autenticado.
    if (!token) {
      setAuthenticated(false);
      setLoading(false);
      return;
    }

    // O Token não é válido? Não está autenticado.
    var usuario_recuperado = {};
    try {
      usuario_recuperado = jwt_decoder(token);
    } catch {
      localStorage.removeItem("usuario_token");
      setAuthenticated(false);
      setLoading(false);
      return;
    }

    // Verificando se esse token e usuário estão batendo
    const fetchUsuario = async () => {
      const data = await usuario.consultar_usuario(usuario_recuperado.cpf);
      if (data.error) {
        localStorage.removeItem("usuario_token");
        setAuthenticated(false);
        setLoading(false);
        return;
      }
    };

    fetchUsuario();
    setAuthenticated(true);
    setLoading(false);
  }, []);

  if (loading) {
    return <h1>Carregando informações...</h1>;
  }

  return (
    <Router>
      <Routes>
        {/* Rota Padrão */}
        <Route path="/" element={authenticated ? <Home /> : <Login />} />

        {/* Autenticação */}
        <Route path="/login" element={<Login />} />
        <Route path="/cadastro" element={<Cadastro />} />

        {/* Geral */}
        <Route path="/home" element={<Home />} />
        <Route path="/perfil" element={<Perfil />} />

        {/* Serviços */}
        <Route path="/servicos/cadastrar" element={<BarbeiroServicos />} />

        {/* Agendamento */}
        <Route path="/cliente/agendamento" element={<ClienteAgendamento />} />
        <Route path="/cliente/agendamentos" element={<ClienteAgendamentos />} />
        <Route path="/barbeiro/home" element={<BarbeiroHome />} />
        <Route
          path="barbeiro/agendamentos"
          element={<BarbeiroAgendamentos />}
        />
      </Routes>
    </Router>
  );
}
