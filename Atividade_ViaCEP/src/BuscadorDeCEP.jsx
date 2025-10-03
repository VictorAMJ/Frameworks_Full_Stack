import { useState, useEffect } from "react";

function BuscaCEP(){
    const [cep, setCep] = useState("");
    const [dados, setDados] = useState(null);
    const [erro, setErro] = useState("");

    const buscar = async () => {
        try {
            if(cep.length !== 8){
                setErro("Digite um CEP válido com 8 Números.");
                setDados(null);
                return;
            }

            setErro("");

            const resposta = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
            const data = await resposta.json();

            if (data.erro){
                setErro("CEP não encontrado!");
                setDados(null);
            } else {
                setDados(data);
            } 
            
        } catch (e) {
            setErro("Erro ao buscar CEP!");
            setDados(null);
        }
    };

    const limpar = () => {
        setCep("");
        setDados(null);
        setErro("");
    };


    return (
        <div className="container">
            <h2 className="titulo">Buscador de CEP</h2>

            <input type="text" placeholder="Digite o CEP(apenas números)" value={cep} onChange={(e) => {
                const valor = e.target.value;
                //verifica se não tem letra:
                if (/^\d*$/.test(valor)){
                    setCep(valor);
                }
            }}
            maxLength={8}
            className="inputCep"
        />
        
        <div className="botoes">
            <button onClick={buscar} className="Bbuscar">Buscar</button>
            <button onClick={limpar} className="Blimpar">Limpar</button>
        </div>
            
        {erro && <p style={{color: "red"}}>{erro}</p>}

        {dados && (
            <div className="resultado">
                <h2>Resultado:</h2>
                <p><strong>Rua: </strong>{dados.logradouro}</p>
                <p><strong>Bairro: </strong>{dados.bairro}</p>
                <p><strong>Cidade: </strong>{dados.localidade}</p>
                <p><strong>Estado: </strong>{dados.uf}</p>
            </div>
        )}
        </div>
    )
}

export default BuscaCEP;