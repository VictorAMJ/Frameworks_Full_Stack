async function imc() {
    var peso = parseFloat(document.getElementById('peso').value);
    var altura = parseFloat(document.getElementById('altura').value);

    var resultadoIMC = document.getElementById('resultadoIMC');


    var imc = peso / (altura * altura);

    var classes = "";
    if (imc < 18.5) {
        classes = "Abaixo do peso";
    } else if (imc < 24.9) {
        classes = "Peso normal";
    } else if (imc < 29.9) {
        classes = "Sobrepreso";
    } else {
        classes = "Obeso";
    }

    resultadoIMC.innerHTML = `Seu IMC é de ${imc.toFixed(2)} ${classes}`;
}


