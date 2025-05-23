import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ClienteLogin from "../pages/auth/ClienteLogin";
import ClienteCadastro from "../pages/auth/ClienteCadastro";
import BarbeiroLogin from "../pages/auth/BarbeiroLogin";
import BarbeiroCadastro from "../pages/auth/BarbeiroCadastro";
import ClientePerfil from "../pages/auth/ClientePerfil";
import BarbeiroPerfil from "../pages/auth/BarbeiroPerfil";

export default function AppRoutes() {
  return (
    <Router>
      <Routes>
        <Route path="/cliente/login" element={<ClienteLogin />} />\
        <Route path="/cliente/cadastro" element={<ClienteCadastro />} />\
        <Route path="/cliente/perfil" element={<ClientePerfil />} />\
        <Route path="/barbeiro/login" element={<BarbeiroLogin />} />\
        <Route path="/barbeiro/cadastro" element={<BarbeiroCadastro />} />\
        <Route path="/barbeiro/perfil" element={<BarbeiroPerfil />} />\
      </Routes>
    </Router>
  );
}
