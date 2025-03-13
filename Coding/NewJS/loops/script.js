const started = document.querySelector('.input-start')
const ended = document.querySelector('.input-end')
const step = document.querySelector('.input-step')
let res = document.querySelector('.res')


function didIt() {
    let s = Number(started.value)
    let e = Number(ended.value)
    let t = Number(step.value)
    
    if(started.value == 0 || ended.value == 0 || step.value == 0) {
        res.innerHTML = "Result: "
        } else {
        if (s < e) {
            for(let i = s; i <= e; i += t) {
                res.innerHTML += `${i} \u{1F896} `
            }
        } else {
            for(let i = s; i >= e; i -= t) {
                res.innerHTML += `${i} \u{1F896}`
            }
        }
        res.innerHTML += `\u{1F3C1}`
    }
}