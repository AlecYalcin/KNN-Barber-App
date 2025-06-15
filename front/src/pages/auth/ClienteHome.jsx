import BottomNav from "../../components/BottomNav";
import ServicosHorarios from "../../components/ScrollHome";

const ClienteHome = () => {
  return (
    <div className="mt-15 ml-5 mr-5">
      <div className="flex ml-2 mt-2 mb-">
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

      <ServicosHorarios />

      <BottomNav />
      
    </div>
  );
};

export default ClienteHome;
