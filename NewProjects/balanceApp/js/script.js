/* const calculateBalance = (income, expenses) => income - expenses;
const result = calculateBalance(5000, 2000);
console.log(result); */

/* const calculateBalance2 = (income) => income - 500;
const result2 = calculateBalance2(750);
console.log(result2); */

let balanceEl = document.querySelector(".balance-number");
balanceEl.addEventListener("click", () => {
  /* InnerHTML creates an element inside HTML */
  /* balanceEl.classList.add("balance-number--special"); */
  balanceEl.insertAdjacentHTML("afterend", "<p>Hi from JavaScript</p>");
});

/* const balance = 2000;
balance > 0 ? console.log(balance) : console.log("Insuficient funds"); */

const myArray = [50, 100, 200, 500];

myArray.forEach((item) => console.log(item * 2));

for (let i = 0; i <= myArray.length - 1; i++) {
  console.log(myArray[i]);
}
