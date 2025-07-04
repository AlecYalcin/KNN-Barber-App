import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ClienteLogin from "../pages/auth/ClienteLogin";
import ClienteCadastro from "../pages/auth/ClienteCadastro";
import BarbeiroLogin from "../pages/auth/BarbeiroLogin";
import BarbeiroCadastro from "../pages/auth/BarbeiroCadastro";
import ClientePerfil from "../pages/auth/ClientePerfil";
import BarbeiroPerfil from "../pages/auth/BarbeiroPerfil";
import ClienteHome from "../pages/auth/ClienteHome";
import ClienteServicos from "../pages/auth/ClienteServicos";
import ClienteAgendamento from "../pages/auth/ClienteAgendamento";
import BarbeiroServicos from "../pages/auth/BarbeiroServicos";
import BarbeiroAltServico from "../pages/auth/BarbeiroAltServico";
import AddBarbeiro from "../pages/auth/AddBarbeiro";
import ListBarbeiro from "../pages/auth/ListBarbeiro";

export default function AppRoutes() {
  return (  
    <Router>
      <Routes>
        <Route path="/cliente/login" element={<ClienteLogin />} />\
        <Route path="/cliente/cadastro" element={<ClienteCadastro />} />\
        <Route path="/cliente/home" element={<ClienteHome />} />\
        <Route path="/cliente/servicos" element={<ClienteServicos />} />\
        <Route path="/cliente/agendamento" element={<ClienteAgendamento />} />\
        <Route path="/cliente/perfil" element={<ClientePerfil />} />\
        <Route path="/barbeiro/login" element={<BarbeiroLogin />} />\
        <Route path="/barbeiro/cadastro" element={<BarbeiroCadastro />} />\
        <Route path="/barbeiro/servicos" element={<BarbeiroServicos />} />\
        <Route path="/barbeiro/alterarservico" element={<BarbeiroAltServico />} />\
        <Route path="/barbeiro/adicionar" element={<AddBarbeiro />} />\
        <Route path="/barbeiro/listar" element={<ListBarbeiro />} />\
        <Route path="/barbeiro/perfil" element={<BarbeiroPerfil />} />\
      </Routes>
    </Router>
  );
}