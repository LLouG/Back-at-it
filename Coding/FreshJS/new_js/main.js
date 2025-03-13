let myArr = ["Pizza", "Lasagna", "막걸리"]

function theArr() {
    for (let i = 0; i < myArr.length; i++) {
        console.log(myArr[i])
    }
}

theArr()
myArr.push("소주")
console.log('==============')
theArr()