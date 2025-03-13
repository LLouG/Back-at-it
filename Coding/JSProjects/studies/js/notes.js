/* console.log(Math.floor(Math.random() * 10) + 1); */

/* const anyName = "Sujeong";
console.log(anyName.charAt(Math.floor(Math.random() * anyName.length))); */

// Ternary operator
// condition ? ifTrue : ifFalse;
/* let soup = "Chicken Noodle Soup";
let response = soup ? "Yes, we have soup." : "Sorry, no soup today.";
console.log(response) */

/* let soup = "Chicken Noodle Soup";
let isCustomerBanned = false;
let souAccess = isCustomerBanned
    ? "Sorry, no soup for you!"
    : soup
    ? `Yes, we have ${soup} today"`
    : "Sorry, no soup today.";
console.log(souAccess); */

/* let testScore = 99;
let myGrade = 
    testScore > 89
        ? "A"
        : testScore > 79
        ? "B"
        : testScore > 69
        ? "C"
        : testScore > 59
        ? "D"
        : "F"
console.log(`My test grade is a ${myGrade}.`); */

/* let namae = prompt("Please enter your name.");
if (namae) {
    console.log(namae.length);
    console.log(namae.trim().length);
    console.log(namae.trim());
}   else {
    console.log("You didn't enter your name.");
} */

let playGame = confirm("Shall we play rock, paper, or scissors?");
if (playGame) {
    let playerChoice = prompt("Please enter rock, paper, or scissors.");
    if (playerChoice) {
        let playerOne = playerChoice.trim().toLowerCase();
        if (playerOne === "rock" || playerOne === "paper" || playerOne === "scissors") {
            let computerChoice = Math.floor(Math.random() * 3 + 1);
            let computer = computerChoice === 1 ? "rock"
                : computerChoice === 2 ? "paper"
                : "scissors";
            let result = 
            playerOne === computer
                ? "Tie game!"
                : playerOne === "rock" && computer === "paper"
                ? `playerOne: ${playerOne}\nComputer: ${computer}\nComputer wins!`
                : playerOne === "paper" && computer === "scissors"
                ? `playerOne: ${playerOne}\nComputer: ${computer}\nComputer wins!`
                : playerOne === "scissors" && computer === "rock"
                ? `playerOne: ${playerOne}\nComputer: ${computer}\nComputer wins!`
                : `playerOne: ${playerOne}\nComputer: ${computer}\nplayerOne wins!`;
            alert(result)
            let playAgain = confirm("Play again?");
            playAgain ? location.reload() : alert("Ok, thanks for playing!");
        } else {
            alert("You didn't enter rock, paper, or scissors.");
        }
    } else {
        alert("I guess you changed your mind. Maybe next time.");
    }
} else {
    alert("Ok, maybe next time.");
}