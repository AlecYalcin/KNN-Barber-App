import BottomNav from "../../components/BottomNav";
import Header from "../../components/Header";
import ServicosHorarios from "../../components/ScrollHome";
import Sidebar from "../../components/SidebarClient";

const ClienteHome = () => {
  return (
    <div className="mt-15 ml-5 lg:ml-0 mr-5">
      <div className="flex items-center ml-2 mt-2 mb-2 lg:hidden">
        <img
          className="w-30 h-30 rounded-full bg-gray-100 mb-3 overflow-hidden border-4 border-blue-100"
          src="https://cdn.creazilla.com/icons/3251108/person-icon-md.png"
          alt="Foto do cliente"
        />
        <h1 className="ml-6 mt-8 text-3xl text-gray-800">
          Olá,
          <br />
          <strong>João Pedro</strong>
        </h1>
      </div>

      <Header title="KNN Barber" />

      <Sidebar />

      <ServicosHorarios />

      <BottomNav />
    </div>
  );
};

export default ClienteHome;
