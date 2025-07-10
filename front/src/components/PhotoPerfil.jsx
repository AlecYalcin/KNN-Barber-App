import { useEffect, useState } from "react";

const PhotoPerfil = () => {
  const [nome, setNome] = useState("");

  useEffect(() => {
    fetch("https://sua-api.com/cliente")
      .then((res) => res.json())
      .then((data) => setNome(data.nome))
      .catch(() => setNome("Denner Biscate"));
  }, []);

  return (
    <div className="flex flex-col items-center mb-6 lg:hidden">
      <div className="w-36 h-36 rounded-full bg-gray-200 mb-3 overflow-hidden border-4 border-blue-100">
        <img
          src="https://cdn.creazilla.com/icons/3251108/person-icon-md.png"
          alt="Foto do cliente"
          className="w-full h-full object-cover"
        />
      </div>
      <h2 className="text-xl font-semibold hidden lg:block">{nome}</h2>
    </div>
  );
};

export default PhotoPerfil;
