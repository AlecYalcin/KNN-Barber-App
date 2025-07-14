import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Perfil from "../pages/autenticacao/Perfil";
import Home from "../pages/autenticacao/Home";
import ClienteServicos from "../pages/auth/ClienteServicos";
import ClienteAgendamento from "../pages/auth/ClienteAgendamento";
import BarbeiroServicos from "../pages/auth/BarbeiroServicos";
import BarbeiroAltServico from "../pages/auth/BarbeiroAltServico";
import AddBarbeiro from "../pages/auth/AddBarbeiro";
import ListBarbeiro from "../pages/auth/ListBarbeiro";
import Cadastro from "../pages/autenticacao/Cadastro";
import Login from "../pages/autenticacao/Login";

export default function AppRoutes() {
  return (
    <Router>
      <Routes>
        {/* Autenticação */}
        <Route path="/login" element={<Login />} />
        <Route path="/cadastro" element={<Cadastro />} />

        {/* Geral */}
        <Route path="/home" element={<Home />} />
        <Route path="/perfil" element={<Perfil />} />

        {/* Serviços */}
        <Route path="/servicos/cadastrar" element={<BarbeiroServicos />} />
        <Route path="/servicos/alterar/:id:" element={<BarbeiroAltServico />} />
        <Route path="/servicos/listar" element={<ClienteServicos />} />

        {/* Jornada de Trabalho */}

        {/* Horário Indisponível */}

        {/* Agendamento */}
        <Route path="/cliente/agendamento" element={<ClienteAgendamento />} />
        <Route path="/barbeiro/adicionar" element={<AddBarbeiro />} />
        <Route path="/barbeiro/listar" element={<ListBarbeiro />} />

        {/* Avaliação */}
      </Routes>
    </Router>
  );
}
