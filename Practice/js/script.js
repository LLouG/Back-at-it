const btnEl = document.querySelector(".btn");
const divBtnEl = document.querySelector(".div-btn");
const btnResetEl = document.querySelector(".btn-reset");
const previousCountEl = document.querySelector(".previous-count");
let count = 0;
let countHistory = [];

btnEl.addEventListener("click", () => {
  count++;
  divBtnEl.innerHTML = `The current click count is  ${count}`;
});

btnResetEl.addEventListener("click", () => {
  divBtnEl.innerHTML = "The current click count is 0";
  countHistory += `${count} `;
  previousCountEl.innerHTML = `The previous click count is ${countHistory}`;
  if (countHistory.length > 8) {
    countHistory = "";
  }
  count = 0;
});
