"use client";
import { useState} from "react";

export default function AddLivro() {
    const [titulo, setTitulo] = useState("");
    const [autor, setAutor] = useState("");
    const [ano, setAno] = useState("");
    const [genero, setGenero] = useState("");
    const [loading, setLoading] = useState(false);

    const mandarLivro = async (e) => {
        e.preventDefault();
        setLoading(true);

        if (!titulo || !autor || !ano || !genero) {
            alert("Preencha todos os campos!");
            setLoading(false);
            return;
        }

        try{
            const res = await fetch("http://127.0.0.1:5000/livro", {
                method: "POST",
                headers: {"content-Type": "application/json"},
                body: JSON.stringify({
                    titulo,
                    autor,
                    ano_publicacao: ano,
                    genero,
                    disponivel: true,
                }),
            });

            if (res.ok) {
                alert("Livro cadastrado com sucesso!")
                setTitulo("");
                setAutor("");
                setAno("");
                setGenero("");
            } else {
                alert("Erro ao cadastrar o livro.");
            }
        } catch (error) {
            console.error("Erro:", error);
            alert("Erro na requisição.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-white rounded-xl shadow-md p-4 w-200">

            <form onSubmit={mandarLivro} className="flex flex-col gap-4">
                <input type="text" placeholder="Título" value={titulo} onChange={(e) => setTitulo(e.target.value)}className="border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
                />

                <input type="text" placeholder="Autor" value={autor} onChange={(e) => setAutor(e.target.value)} className="border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
                />

                <input type="number" placeholder="Ano de Publicação" value={ano} onChange={(e) => setAno(e.target.value)} className="border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
                />

                <input type="text" placeholder="Gênero" value={genero} onChange={(e) => setGenero(e.target.value)} className="border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
                />

                <div className="flex justify-center mt-1 mb-2">
                    <button
                        type="submit"
                        disabled={loading}
                        className={`bg-indigo-600 text-white w-32 py-2 rounded-lg font-semibold shadow-md hover:bg-indigo-700 transition ${
                        loading ? "opacity-50 cursor-not-allowed" : ""
                        }`}
                    >
                        {loading ? "Salvando..." : "Adicionar Livro"}
                    </button>
                </div>
                
            </form>
        </div>
    )
}