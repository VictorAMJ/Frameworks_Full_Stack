'use client';

import UpLivro from "../../../components/atualizarLivro";

export default function NovoLivroPage(){
    return (
        <section className="flex flex-col items-center min-h-screen bg-gradient-to-b from-indigo-100 to-indigo-300 text-gray-800">

            <h1 className="text-4xl font-bold mt-20 mb-30 text-indigo-700">
                📚 Atualizar Livro
            </h1>
            <div className="flex flex-wrap justify-center gap-2">
                <UpLivro/>
            </div>
        </section>
        
  );
}