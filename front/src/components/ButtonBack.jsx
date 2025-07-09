const ButtonBack = () => {
  return (
    <button
      className="fixed top-8 left-4 z-50 flex items-center text-blue-600 hover:text-blue-800 transition focus:outline-none lg:hidden"
      onClick={() => window.history.back()}
      aria-label="Voltar"
    >
  <svg
    className="w-6 h-6 mr-1"
    fill="none"
    stroke="currentColor"
    strokeWidth={2}
    viewBox="0 0 24 24"
  >
    <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
  </svg>
  Voltar
</button>
  );
}

export default ButtonBack;
