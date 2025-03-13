/* let btn = document.querySelector(".btn")
btn.addEventListener('click', function() {
    console.log('hi')
})
console.log(btn.textContent)
const btn2 = document.querySelector(".btn")
btn2.style.color = 'red'
btn2.style.backgroundColor = 'blue' */

const display = document.querySelector("#display-input")
const btnNum = document.querySelectorAll(".num")
const btnDivide = document.querySelector(".divide")
const btnMultiply = document.querySelector(".multiply")
const btnPlus = document.querySelector(".plus")
const btnSubtract = document.querySelector(".subtract")
const btnEqual = document.querySelector(".equal")
const btnComma = document.querySelector(".comma")

let operacaoAtual = "";
let calculando = true

function atualizaDisplay() {
    display.value = operacaoAtual;
}

function insereNumero(evento) {
    if (calculando) {
        operacaoAtual = evento.target.textContent;
        calculando = false
    } else {
        operacaoAtual += evento.target.textContent;
    }

    atualizaDisplay();
}

function inserePonto() {
    if(operacaoAtual.indexOf(".") === -1) {
        operacaoAtual += "."
        atualizaDisplay()
    }
}

btnComma.addEventListener("click", inserePonto)
btnNum.forEach((botao) => botao.addEventListener("click", insereNumero))