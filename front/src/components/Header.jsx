const Header = ({ title }) => {

  function handleLogout() {
    localStorage.removeItem("usuario_token");
    window.location.href = "/login";
  }
  return (
    <header className="lg:flex justify-between hidden bg-blue-600 p-4 text-white fixed top-0 w-full z-50">
      <h1 className="text-3xl font-bold ml-2">{title}</h1>
      <button className="mr-4" onClick={handleLogout}>Sair</button>
    </header>
  );
}

export default Header;