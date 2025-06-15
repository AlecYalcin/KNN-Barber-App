import { useRef, useEffect, useState } from "react";

function ServicosHorarios() {
  const containerRef = useRef(null);
  const [currentView, setCurrentView] = useState("servicos");

  const handleScroll = () => {
    const scrollLeft = containerRef.current.scrollLeft;
    const width = containerRef.current.offsetWidth;

    if (scrollLeft > width / 4) {
      setCurrentView("horarios");
    } else {
      setCurrentView("servicos");
    }
  };

  const scrollTo = (direction) => {
    const container = containerRef.current;
    const width = container.offsetWidth;

    if (direction === "next") {
      container.scrollTo({
        left: width,
        behavior: "smooth",
      });
    } else {
      container.scrollTo({
        left: 0,
        behavior: "smooth",
      });
    }
  };

  useEffect(() => {
    const container = containerRef.current;
    container.addEventListener("scroll", handleScroll);

    return () => {
      container.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <div className="min-w-full">
      {/* Título */}
      <h2 className="text-2xl text-gray-800 font-semibold ml-5 mt-7">
        {currentView === "servicos" ? "Serviços" : "Horários Disponíveis"}
      </h2>

      {/* Botões de Navegação */}
      {currentView === "horarios" && (
        <button
          onClick={() => scrollTo("prev")}
          className="mt-50 absolute left-2 top-1/2 transform -translate-y-1/2 bg-blue-500 border border-gray-300 rounded-full p-2 shadow hover:bg-gray-100"
        >
          ⬅️
        </button>
      )}

      {currentView === "servicos" && (
        <button
          onClick={() => scrollTo("next")}
          className="mt-50 absolute right-2 top-1/2 transform -translate-y-1/2 bg-blue-500 border border-gray-300 rounded-full p-2 shadow hover:bg-gray-100"
        >
          ⬅️
        </button>
      )}

      {/* Container com scroll */}
      <div
        ref={containerRef}
        className="flex overflow-x-auto scroll-smooth m-4 p-4 space-x-8 bg-blue-500 rounded-2xl shadow-lg "
      >
        {/* Section de Serviços */}
        <section className="min-w-full grid grid-cols-2 gap-4">
          {["Completo", "Barba", "Penteado", "Bigode"].map((item) => (
            <article
              key={item}
              className="bg-white shadow-md rounded-2xl flex items-center justify-center h-35"
            >
              <h3 className="text-xl font-semibold">{item}</h3>
            </article>
          ))}
        </section>

        {/* Section de Horários */}
        <section className="min-w-full grid grid-cols-3 gap-4">
          {["08:00", "09:00", "10:00", "11:00","13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00","20:00"].map((hora) => (
            <article
              key={hora}
              className="bg-white shadow-md rounded-2xl flex items-center justify-center px-6">
              <h3 className="text-xl font-semibold">{hora}</h3>
            </article>
          ))}
        </section>
      </div>
    </div>
  );
}

export default ServicosHorarios;
