"use client";

export default function CardLivro({ id, titulo, autor, ano_publicacao, genero, onDelete, onUpdate}) {
  return (
    <div className="bg-white rounded-xl shadow-md p-4 w-200 hover:scale-105 transition">

      <h2 className="text-lg font-semibold text-indigo-700">{titulo}</h2>
      <h3 className="text-gray-700">Autor: {autor}</h3>
      <h3 className="text-gray-700">Gênero: {genero}</h3>
      <h3 className="text-gray-500">Ano de publicação: {ano_publicacao}</h3>

      <div className=" mt-4 flex justify-center gap-5">
        <button onClick={() => onDelete(id)} className="bg-red-400 text-gray-700 px-4 py-2 rounded-lg hover:bg-red-500 transition" >Deletar</button>
         <button onClick={() => onUpdate(id)} className="bg-green-400 text-gray-700 px-4 py-2 rounded-lg hover:bg-green-500 transition" >Atualizar</button>
      </div>
    </div>
  );
}