// SCROLL HOME
import { useState } from "react";

function ServicosHorarios() {
  const [currentView] = useState("servicos");

  return (
    <div className="relative w-full lg:pl-69 lg:mt-30">
      {/* 🧭 Conteúdo com scroll lateral */}
      <div className="overflow-x-auto scroll-smooth p-4 space-x-8 bg-blue-500 rounded-2xl shadow-lg">
        {/* 🔹 Serviços */}
        <h2 className="py-8 md:px-4 text-2xl lg:text-5xl font-bold text-white ">
          Serviços Disponíveis
        </h2>
        <section className="w-full flex flex-col gap-4 md:p-4">
          {[
            {
              nome: "Corte Tradicional",
              descricao:
                "Corte clássico com tesoura e máquina, acompanhando o formato do rosto",
              valor: "R$ 50,00",
              tempo: "45 min",
            },
            {
              nome: "Barba",
              descricao:
                "Aparação e modelagem completa da barba com toalha quente e finalização",
              valor: "R$ 35,00",
              tempo: "30 min",
            },
            {
              nome: "Penteado",
              descricao:
                "Estilo personalizado com produtos profissionais para ocasiões especiais",
              valor: "R$ 65,00",
              tempo: "60 min",
            },
            {
              nome: "Bigode",
              descricao:
                "Aparação e modelagem do bigode com acabamento preciso",
              valor: "R$ 25,00",
              tempo: "20 min",
            },
          ].map((servico) => (
            <article
              key={servico.nome}
              className="bg-white rounded-2xl shadow p-6 hover:shadow-lg transition-shadow"
            >
              <div className="flex flex-col md:flex-row gap-4">
                <div className="flex-1">
                  <h3 className="text-xl font-semibold text-gray-800">
                    {servico.nome}
                  </h3>
                  <p className="text-gray-600 mt-2">{servico.descricao}</p>
                </div>
                <div className="flex flex-col items-start md:items-end">
                  <span className="text-lg font-bold text-blue-600">
                    {servico.valor}
                  </span>
                  <span className="text-sm text-gray-500 mt-1">
                    <i className="far fa-clock mr-1"></i> {servico.tempo}
                  </span>
                </div>
              </div>
            </article>
          ))}
        </section>
      </div>
    </div>
  );
}

export default ServicosHorarios;
