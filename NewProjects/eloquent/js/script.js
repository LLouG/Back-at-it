let code = document.querySelector("code");
let count = 1,
  total = 0;

while (count <= 10) {
  total += count;
  console.log(total);
  count++;
}

code.innerHTML += `let count = 1, total = 0;
        while(count <= 10) {
        total += count;
        count++;
        }`;
