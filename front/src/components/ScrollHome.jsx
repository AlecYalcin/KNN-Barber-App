// SCROLL HOME

import { useRef, useEffect, useState, useCallback } from "react";

function ServicosHorarios() {
  const containerRef = useRef(null);
  const [currentView, setCurrentView] = useState("servicos");
  const scrollTimeout = useRef();

  // 🗓️ Pega o dia atual formatado (ex: 10/06/2024)
  const today = new Date();
  const formattedDate = today.toLocaleDateString("pt-BR", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
  });

  // ⚙️ Detecta o scroll e muda de seção ao passar 20%
  const handleScroll = useCallback(() => {
    if (!containerRef.current) return;
    if (scrollTimeout.current) cancelAnimationFrame(scrollTimeout.current);

    scrollTimeout.current = requestAnimationFrame(() => {
      const container = containerRef.current;
      const scrollLeft = container.scrollLeft;
      const width = container.offsetWidth;

      setCurrentView(scrollLeft >= width * 0.2 ? "horarios" : "servicos");
    });
  }, []);

  // 🔄 Faz o scroll manual com botão
  const scrollTo = useCallback((direction) => {
    const container = containerRef.current;
    if (!container) return;
    const width = container.offsetWidth;

    container.scrollTo({
      left: direction === "next" ? width : 0,
      behavior: "smooth",
    });
  }, []);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;
    container.addEventListener("scroll", handleScroll, { passive: true });

    return () => {
      container.removeEventListener("scroll", handleScroll);
      if (scrollTimeout.current) cancelAnimationFrame(scrollTimeout.current);
    };
  }, [handleScroll]);

  // SVG minimalista para seta
  const ArrowRight = (
    <svg width="24" height="24" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M8 5l8 7-8 7" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
  const ArrowLeft = (
    <svg width="24" height="24" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M16 5l-8 7 8 7" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );

  return (
    <div className="relative w-full lg:pl-69 lg:mt-30">
      {/* 🔥 Título dinâmico */}
      <h2 className="text-2xl text-gray-800 font-semibold mt-10 flex justify-center items-center">
        {currentView === "servicos"
          ? "Serviços"
          : (
            <>
              Horários
              <span className="text-base text-gray-500 font-normal bg-white px-3 py-1 rounded-lg shadow ml-2">
                {formattedDate}
              </span>
            </>
          )
        }
      </h2>

      {/* 🔽 Botões de navegação */}
      <div className="flex items-center justify-between w-full px-5 mt-1  mb-2 absolute left-0 top-0 pointer-events-none z-10">
        <div className=" flex justify-start">
          {currentView === "horarios" && (
            <button
              onClick={() => scrollTo("prev")}
              className="bg-blue-500 text-white p-2 rounded-full shadow flex items-center justify-center pointer-events-auto lg:ml-69"
              aria-label="Anterior"
              type="button"
            >
              {ArrowLeft}
            </button>
          )}
        </div>
        <div className="flex-1 flex justify-end">
          {currentView === "servicos" && (
            <button
              onClick={() => scrollTo("next")}
              className="bg-blue-500 text-white p-2 rounded-full shadow flex items-center justify-center pointer-events-auto"
              aria-label="Próximo"
              type="button"
            >
              {ArrowRight}
            </button>
          )}
        </div>
      </div>
      {/* 🧭 Conteúdo com scroll lateral */}
      <div
        ref={containerRef}
        className="flex overflow-x-auto scroll-smooth m-4 p-4 space-x-8 bg-blue-500 rounded-2xl shadow-lg"
      >
        {/* 🔹 Serviços */}
        <section className="min-w-full grid grid-cols-2 gap-4">
          {["Completo", "Barba", "Penteado", "Bigode"].map((item) => (
            <article
              key={item}
              className="bg-white h-45 rounded-2xl shadow flex items-center justify-center"
            >
              <h3 className="text-xl font-semibold">{item}</h3>
            </article>
          ))}
        </section>

        {/* 🔸 Horários */}
        <section className="min-w-full grid grid-cols-3 gap-4">
          {[
            "08:00", "09:00", "10:00", "11:00", "13:00", "14:00",
            "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"
          ].map((hora) => (
            <article
              key={hora}
              className="bg-white h-20 rounded-2xl shadow flex items-center justify-center"
            >
              <h3 className="text-xl font-semibold">{hora}</h3>
            </article>
          ))}
        </section>
      </div>
    </div>
  );
}

export default ServicosHorarios;
