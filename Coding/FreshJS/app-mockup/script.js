// Using terminal
// mkdir folder-name
// code file-name.extension-name

// Create an app to keep data on how the day went
// Then create graphs using that data and give scores

const btn1 = document.getElementById("btn-1")
const btn2 = document.getElementById("btn-2")
let county = 0

btn1.addEventListener("click", function(){
    county++
    let ct = document.getElementById("counter")
    ct.innerHTML = "Clicked: " + county + " times"
})

btn2.addEventListener("click", function(){
    county = 0
    document.getElementById("counter").innerHTML = "Clicked: 0 times"
})