/* const logoEl = document.querySelector(".header__logo--a");
logoEl.addEventListener("click", () => {
  logoEl.style.color = "red";
}); */

/* class Color {
  constructor(myColor) {
    this.myColor = myColor;
  }

  describe() {
    return `${this.myColor}`;
  }

  static getColor(colors) {
    for (const color of colors) {
      console.log(this.colors);
    }
  }
}

class Book extends Color {
  constructor(book, myColor) {
    super(myColor);
    this.book = book;
  }

  describe() {
    return `The book ${this.book} is of color ` + super.describe();
  }
}

let myBook = new Book("Three Kingdoms", "Brown");
console.log(myBook.describe()); */

/* function noisy(f) {
  return (...args) => {
    console.log(`Calling with ${args}`);
    let result = f(...args);
    console.log(`Called with ${args}, returned ${result}`);
    return result;
  };
}
noisy(Math.min)(3, 7, 2, 8); */

/* function repeat(n, action) {
  for (let i = 0; i < n; i++) {
    action(i);
  }
}

let labels = [];
repeat(5, (j) => {
  labels.push(`Unit ${j + 1}`);
});

console.log(`${labels}`.split(",").join(" \n")); */

/* function repeat(n, action) {
  for (let i = 0; i < n; i++) {
    action(i);
  }
}

function unless(test, then) {
  if (!test) then();
}

repeat(3, (n) => {
  unless(n % 2 == 1, () => {
    console.log(n, "is even");
  });
}); */

/* ["A", "B"].forEach((l) => console.log(l)); */
