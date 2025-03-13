/* let nome = "Loug";
for (let i = 0; i < nome.length; i++) {
    console.log(nome.charAt(i));
} */

/* let nome = "Loug";
let counter = 0;
let myLetter;
while (counter <= 3) {
    myLetter = nome[counter];
    console.log(myLetter);
    if (counter === 1) {
        counter += 2;
        continue;
    }
    if (myLetter === "u") break;
    counter++;

}
console.log(counter); */

/* function sum(num1, num2) {
    if (num2 === undefined) {
        return num1 + num1;
    }
    return num1 + num2;
}
console.log(sum(2, 4)); */

/* function getUserNameFromEmail(email) {
    return email.slice(0, email.indexOf("@"));
}
console.log(getUserNameFromEmail("playerOne@SomeRandomEmail.com")); */

/* const getUserNameFromEmail = (email) => {
    return email.slice(0, email.indexOf("@"));
};
console.log(getUserNameFromEmail("loug@lougsdomain.com")); */

const toProperCase = (nome) => {
    return nome.charAt(0).toUpperCase() + nome.slice(1).toLowerCase();
};
console.log(toProperCase("sepTemBer"));