let currentTime = document.querySelector('.current-time')
let dayOfWeek = document.querySelector('.week-day')
let img = document.querySelector('.image')
let date = new Date()
let minutes = (date.getMinutes() < 10 ? '0' : '') + date.getMinutes()

function hours() {
    if (date.getHours() <= 11 && date.getMinutes() <= 59) {
        currentTime.innerHTML = `Your local time is: ${date.getHours()}:${minutes} AM`
        } else {        
            currentTime.innerHTML = `Your local time is: ${date.getHours()}:${minutes} PM`
            img.src = 'images/hyojung-in-dun-dun-dance-mv-shoot-3840x2160.jpg'
        }
}

const weekDay = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
dayOfWeek.innerHTML = `Today is ${weekDay[date.getDay()]}`



/* switch(date.getDay()) {
    case 0:
        dayOfWeek.innerHTML = `Today is ${weekDay[date.getDay()]}`
        break 
    case 1:
        dayOfWeek.innerHTML = `Today is ${weekDay[date.getDay()]}`
        break
    case 2:
        dayOfWeek.innerHTML = `Today is ${weekDay[date.getDay()]}`
        break
    case 3:
        dayOfWeek.innerHTML = `Today is ${weekDay[date.getDay()]}`
        break
    case 4:
        dayOfWeek.innerHTML = `Today is ${weekDay[date.getDay()]}`
        break
    case 5:
        dayOfWeek.innerHTML = `Today is ${weekDay[date.getDay()]}`
        break
    case 6:
        dayOfWeek.innerHTML = `Today is ${weekDay[date.getDay()]}`
        break
} */
