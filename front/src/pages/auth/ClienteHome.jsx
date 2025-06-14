const ClienteHome = () => {
  return (
    <div className="mt-15 ml-10 mr-10">
      <div className="flex ">
        <div className="w-30 h-30 rounded-full bg-gray-200 mb-3 overflow-hidden border-4 border-blue-100">
          <img
            src="https://cdn.creazilla.com/icons/3251108/person-icon-md.png"
            alt="Foto do cliente"
          />
        </div>
        <div className="ml-6 mt-8">
          <h1 className="text-3xl text-gray-800">
            Olá,
            <br />
            <strong>João Pedro</strong>
          </h1>
        </div>
      </div>

      <div className="mt-10">
        <h2 className="text-2xl text-gray-800 mb-4">Serviços</h2>
      </div>
      <section className="grid grid-cols-2 gap-4">
        <article className="bg-red-100 shadow-md h-36 rounded-2xl flex items-center justify-center">
          <h3 className="text-xl font-semibold">Completo</h3>
        </article>

        <article className="bg-red-100 shadow-md h-36 rounded-2xl flex items-center justify-center">
          <h3 className="text-xl font-semibold">Barba</h3>
        </article>

        <article className="bg-red-100 shadow-md h-36 rounded-2xl flex items-center justify-center">
          <h3 className="text-xl font-semibold">Penteado</h3>
        </article>

        <article className="bg-red-100 shadow-md h-36 rounded-2xl flex items-center justify-center">
          <h3 className="text-xl font-semibold">Bigode</h3>
        </article>
      </section>
    </div>
  );
};

export default ClienteHome;
