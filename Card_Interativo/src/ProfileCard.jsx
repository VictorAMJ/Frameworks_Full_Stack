import React from "react";
import './ProfileCard.css';

function Card({ name, age, isStudent }) {
    return (
        <div className="cartao">
            <p>👤 {name} - {age} anos</p>
            <p> {isStudent ? "É estudante" : "Não é estudante"} </p>
            <button onClick={() => alert(name)}>Ver nome</button>
        </div>
    )
}

export default Card