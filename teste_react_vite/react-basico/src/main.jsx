import React from "react"; //Importa a biblioteca React para usar JSX

//Importa ReactDOM para conectar React ao HTML
import ReactDOM from "react-dom/client";

//Importa nosso componente
import App from "./App.jsx";

//ReactDOM.createRoot(...) → cria o root React, depois pega o local do html e renderiza o JSX passado dentro do root.
ReactDOM.createRoot(document.getElementById("conteudo")).render(

    //<React.StrictMode> → modo de desenvolvimento.
    //<App /> → componente principal que vai aparecer na tela. obs:pode ser qualquer nome
    <React.StrictMode>
        <App />
    </React.StrictMode>
);





