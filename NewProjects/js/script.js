let button = document.querySelector(".btn");
let buttonReset = document.querySelector(".btn-reset");
let clicks = document.querySelector(".clicks");
let count = 0;

button.addEventListener("click", () => {
  count++;
  if (count === 1) {
    clicks.innerHTML = "Clicked: " + count + " time";
  } else {
    clicks.innerHTML = "Clicked: " + count + " times";
  }
});

buttonReset.addEventListener("click", () => {
  count = 0;
  clicks.innerHTML = "";
});

let c = 1,
  total = 0;
while (c <= 10) {
  total += c;
  c++;
}

console.log(total);
