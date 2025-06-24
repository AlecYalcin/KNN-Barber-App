import { useRef, useEffect, useState } from "react";

function ServicosHorarios() {
  const containerRef = useRef(null);
  const [currentView, setCurrentView] = useState("servicos");

  // ⚙️ Detecta o scroll e muda de seção ao passar 20%
  const handleScroll = () => {
    const container = containerRef.current;
    const scrollLeft = container.scrollLeft;
    const width = container.offsetWidth;

    if (scrollLeft >= width * 0.2) {
      setCurrentView("horarios");
    } else {
      setCurrentView("servicos");
    }
  };

  // 🔄 Faz o scroll manual com botão
  const scrollTo = (direction) => {
    const container = containerRef.current;
    const width = container.offsetWidth;

    container.scrollTo({
      left: direction === "next" ? width : 0,
      behavior: "smooth",
    });
  };

  useEffect(() => {
    const container = containerRef.current;
    container.addEventListener("scroll", handleScroll);

    return () => container.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <div className="relative w-full">
      {/* 🔥 Título dinâmico */}
      <h2 className="text-2xl text-gray-800 font-semibold ml-5 mt-7">
        {currentView === "servicos" ? "Serviços" : "Horários Disponíveis"}
      </h2>

      {/* 🔽 Botões de navegação */}
      {currentView === "servicos" && (
        <button
          onClick={() => scrollTo("next")}
          className="absolute right-3 top-1/2 -translate-y-1/2 bg-blue-500 text-white p-2 rounded-full shadow"
        >
          ➡️
        </button>
      )}
      {currentView === "horarios" && (
        <button
          onClick={() => scrollTo("prev")}
          className="absolute left-3 top-1/2 -translate-y-1/2 bg-blue-500 text-white p-2 rounded-full shadow"
        >
          ⬅️
        </button>
      )}

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
          {["08:00", "09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"].map((hora) => (
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
