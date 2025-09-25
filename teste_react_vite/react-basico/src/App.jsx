import React from "react"
import "./App.css" // importa o CSS

// Componente App: função que retorna o conteúdo da interface
function App() {
    return (
        <div>
            <h1>Olá, React feito do zero!</h1>
            <h2>Consegui fazer funcionar hehe</h2>
            <p>XDDDDDD</p>
        </div>
    )
}

export default App
// Exporta o componente App para ser usado em main.jsx




/*

O que é: O componente principal da sua aplicação React.

Função: Serve como “container” para todos os outros componentes. Geralmente, tudo que você vê na tela (header, cards, botões) passa por <App />.

Por que é necessário: Ele organiza a estrutura da interface. Sem ele, o React não teria um componente raiz para renderizar na tela.

*/