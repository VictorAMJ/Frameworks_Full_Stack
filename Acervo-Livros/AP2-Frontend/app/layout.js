import Link from "next/link";
import "./globals.css";

export const metadata = {
  title: "Acervo de Livros",
  description: "Gerencie e descubra livros incríveis 📚",
};

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body className="bg-gray-50 text-gray-900 min-h-screen flex flex-col">
        {/* HEADER */}
        <header className="bg-indigo-600 text-white p-5 shadow-md">
          <nav className="max-w-8xl mx-auto flex justify-between items-center">
            <h1 className="text-xl font-semibold">📚 Acervo de Livros</h1>
            <div className="flex gap-10">
              <Link href="/" className="hover:underline">Início</Link>
              <Link href="/livros" className="hover:underline">Livros</Link>
              <Link href="/novo" className="hover:underline">Adicionar livro</Link>
            </div>
          </nav>
        </header>

        {/* CONTEÚDO */}
        <main className="flex-1 max-w-8xl mx-auto w-full">{children}</main>

      </body>
    </html>
  );
}