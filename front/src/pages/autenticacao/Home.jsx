import BottomNav from "../../components/BottomNav";
import Header from "../../components/Header";
import ServicosHorarios from "../../components/ScrollHome";
import Sidebar from "../../components/SidebarClient";

// API
import { jwt_decoder } from "../../api/index";

const ClienteHome = () => {
  const usuario = jwt_decoder(localStorage.getItem("usuario_token"));
  return (
    <div className="mt-15 ml-5 lg:ml-0 mr-5">

      <Header title="KNN Barber" />
      <Sidebar />
      <ServicosHorarios />
      <BottomNav />
    </div>
  );
};

export default ClienteHome;
