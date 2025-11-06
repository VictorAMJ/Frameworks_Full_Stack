"use client";
import { useEffect, useState} from "react";
import { useParams, useRouter } from "next/navigation";

export default function UpLivro() {
    const { id } = useParams();
    const router = useRouter();

    const [titulo, setTitulo] = useState("");
    const [autor, setAutor] = useState("");
    const [ano, setAno] = useState("");
    const [genero, setGenero] = useState("");
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        async function buscarLivro() {
            try{
                const res = await fetch(`http://127.0.0.1:5000/livros/${id}`);
                const data = await res.json();

                setTitulo(data.titulo);
                setAutor(data.autor);
                setAno(data.ano_publicacao);
                setGenero(data.genero);
            } catch (error) {
                console.error("Erro ao buscar livro: ", error)
            }
        }

        if (id) buscarLivro();
    }, [id]);


    const atualizarLivro = async (e) => {
        e.preventDefault();
        setLoading(true);

        if (!titulo || !autor || !ano || !genero) {
            alert("Preencha todos os campos!");
            setLoading(false);
            return;
        }

        try{
            const res = await fetch(`http://127.0.0.1:5000/livros/${id}`, {
                method: "PUT",
                headers: {"content-Type": "application/json"},
                body: JSON.stringify({
                    titulo,
                    autor,
                    ano_publicacao: ano,
                    genero,
                    disponivel: true,
                }),
            });

            if (res.ok){
                alert("Livro atualizado!");
                router.push("/livros");
            } else {
                alert("Erro ao atualizar o livro.");
            } 
        } catch (error) {
            console.error("Erro:", error);
            alert("Erro na requisição.");
        } finally {
            setLoading(false);
        }
    };


    return(
        <div className="bg-white rounded-xl shadow-md p-4 w-200">
            <form
                onSubmit={atualizarLivro}
                className="flex flex-col gap-4"
            >
                <label className="block mb-3">
                    <span className="font-semibold">Título:</span>
                    <input
                    type="text"
                    className="w-full border rounded-md px-3 py-2"
                    value={titulo}
                    onChange={(e) => setTitulo(e.target.value)}
                    />
                </label>

                <label className="block mb-3">
                    <span className="font-semibold">Autor:</span>
                    <input
                    type="text"
                    className="w-full border rounded-md px-3 py-2"
                    value={autor}
                    onChange={(e) => setAutor(e.target.value)}
                    />
                </label>

                <label className="block mb-3">
                    <span className="font-semibold">Ano de Publicação:</span>
                    <input
                    type="number"
                    className="w-full border rounded-md px-3 py-2"
                    value={ano}
                    onChange={(e) => setAno(e.target.value)}
                    />
                </label>

                <label className="block mb-4">
                    <span className="font-semibold">Gênero:</span>
                    <input
                    type="text"
                    className="w-full border rounded-md px-3 py-2"
                    value={genero}
                    onChange={(e) => setGenero(e.target.value)}
                    />
                </label>

                <div className="flex justify-center mt-1 mb-2">
                    <button
                        type="submit"
                        disabled={loading}
                        className={`bg-indigo-600 text-white px-4 py-2 rounded-lg font-semibold hover:bg-indigo-700 transition ${
                        loading ? "opacity-50 cursor-not-allowed" : ""
                        }`}
                    >
                        {loading ? "Salvando..." : "Atualizar Livro"}
                    </button>
                </div>
            </form>
        </div>
        
    )
}