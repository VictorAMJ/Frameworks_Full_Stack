'use client';

import { useEffect, useState } from "react";
import CardLivro from "../components/CardLivros";

export default function LivrosPage() {
  const [livros, setLivros] = useState([]);

  useEffect(() => {
    async function fetchLivros(){
      try{
        const res = await fetch("http://127.0.0.1:5000/livros");
        const data = await res.json();
        setLivros(data);
      } catch (error){
        console.error("Erro ao buscar livros:", error);
      }
    }
    fetchLivros();
  }, []);
  

  const deletarLivro = async (id) => {
  try {
    const res = await fetch(`http://127.0.0.1:5000/livros/${id}`, {
      method: "DELETE",
    });

    if (res.ok) {
      alert("Livro deletado com sucesso!");
      setLivros((prev) => prev.filter((livro) => livro.id !== id)); //atualiza sem recarregar pag
    } else {
      alert("Erro ao deletar o livro");
    }
  }catch (error) {
    console.error("Erro:", error);
    alert("Erro na requisição");
  }};


  const atualizarLivro = (id) => {
    window.location.href = `/livros/atualizar/${id}`;
  }


  return (
    <section className="flex flex-col items-center min-h-screen bg-gradient-to-b from-indigo-100 to-indigo-300 text-gray-800">

      <h1 className="text-4xl font-bold mt-20 mb-30 text-indigo-700">
        📚 Seus Livros
      </h1>

      <div className="flex flex-wrap justify-center w-250 gap-2 mb-30">
        {livros.map((livro) => (
          <CardLivro key={livro.id} {...livro} 
          onDelete={deletarLivro}
          onUpdate={atualizarLivro}
          />

        ))}
      </div>
    </section>
  );
}