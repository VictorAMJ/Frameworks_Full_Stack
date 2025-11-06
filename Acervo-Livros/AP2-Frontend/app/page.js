export default function Home() {
  return (
    <main className="flex flex-col items-center min-h-screen bg-gradient-to-b from-indigo-100 to-indigo-300 text-gray-800">
      <h1 className="text-4xl font-bold mt-20 mb-30 text-indigo-700">
        📚 Bem-vindo ao Acervo de Livros
      </h1>
      <p className="text-lg text-center max-w-lg mb-30">
        Tenha sua coleção de livros em um só lugar, cadastre novos títulos e mantenha seu acervo sempre atualizado!
      </p>

      <div className="flex flex-col sm:flex-row gap-4">
        <a
        href="/livros"
        className="mt-6 bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 transition"
      >
        Ver Livros
      </a>
      <a
        href="/novo"
        className="mt-6 bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 transition"
      >
        Novo Livro
      </a>
      </div>
    </main>
  );
}