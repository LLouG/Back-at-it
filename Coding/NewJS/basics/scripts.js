/* const sum = (a, b) => a + b
console.log(sum(3, 4))

const sqrt = (num) => num * num
console.log(sqrt(3)) */

/* let n1 = 1545.5.toFixed(2).replace('.', ',')
console.log(n1.toLocaleString('pt-BR', {style: 'currency', currency: 'EUR'}))
*/



const a = document.querySelector('.the-h1')
a.addEventListener('click', clicked)
a.addEventListener('mouseenter', enter)
a.addEventListener('mouseout', leave)
function clicked() {
    a.innerHTML = "Clicked"
    a.style.background = 'red'
}
function enter() {
    a.innerHTML = "Entered"
}
function leave() {
    a.innerHTML = "Left"
}


let n1 = document.querySelector("#n1")
let n2 = document.querySelector("#n2")
let sub = document.querySelector('#sub')
let result = document.querySelector('#result')
sub.addEventListener('click', res)

function res() {
    let sum = Number(n1.value) + Number(n2.value)
    result.innerHTML += sum
}