import ButtonBack from "../../components/ButtonBack";
import BottomNav from "../../components/BottomNav";
import PhotoPerfil from "../../components/PhotoPerfil";

const ClientePerfil = () => {
  return (
    <div className="min-h-screen bg-gray-100 py-15 flex">
      <ButtonBack />

      <main className="flex w-full flex-col items-center p-6 lg:mt-10 lg:pl-69">
        <PhotoPerfil />

        <h2 className="text-lg font-bold mb-3 text-gray-800">Informações</h2>

        <div className="w-full">
          <form className="space-y-3">
            <div>
              <label className="block text-xs font-medium text-gray-500 mb-1">
                Telefone
              </label>
              <div className="p-2 bg-gray-50 rounded-lg border border-gray-200">
                <p className="text-sm text-gray-500">+55 00 00000-0000</p>
              </div>
            </div>

            <div>
              <label className="block text-xs font-medium text-gray-500 mb-1">
                E-mail
              </label>
              <div className="p-2 bg-gray-50 rounded-lg border border-gray-200">
                <p className="text-sm text-gray-500">emailcliente@gmail.com</p>
              </div>
            </div>
          </form>

          <div className="mt-6">
            <h2 className="text-lg font-bold mb-3 text-gray-800">
              Agendamentos
            </h2>
            <div className="bg-gray-50 rounded-lg p-3 border border-gray-200 min-h-20">
              <p className="text-sm text-gray-500">
                Nenhum agendamento recente
              </p>
            </div>
          </div>
        </div>

        

        <BottomNav />
      </main>
    </div>
  );
};

export default ClientePerfil;
