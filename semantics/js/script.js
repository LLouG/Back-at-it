/* class Person {
  constructor(name) {
    this.name = name;
  }

  describe() {
    return `Person named ${this.name}`;
  }

  static logNames(persons) {
    for (const person of persons) {
      console.log(person.name);
    }
  }
}

class Employee extends Person {
  constructor(name, title) {
    super(name);
    this.title = title;
  }
  describe() {
    return super.describe() + ` ${this.title}`;
  }
}

const jane = new Employee("Jane", "(CTO)");
console.log(jane.describe()); */
/* class Book {
  constructor(book) {
    this.book = book;
  }

  description() {
    return `Book named ${this.book}`;
  }

  static logBooks(books) {
    for (const _book of books) {
      console.log(_book.book);
    }
  }
}

class Author extends Book {
  constructor(book, author) {
    super(book);
    this.author = author;
  }

  description() {
    return super.description() + ` writen by ${this.author}.`;
  }
}

const douglas = new Author("Hitchhiker's Guide to the Galaxy", "Douglas Adams");
console.log(douglas.description()); */

/* const titleEl = document.querySelector(".title");

titleEl.addEventListener("click", () => {
  titleEl.style.fontSize = "3rem";
}); */

/* function max(...numbers) {
  let result = -Infinity;
  for (let number of numbers) {
    if (number > result) {
      result = number;
    }
  }
  return result;
} */
/* function zeroPad(number, width) {
  let string = String(number);
  while (string.length < width) {
    string = "0" + string;
  }
  return string;
} */

/* function sumRange(n1, n2, step = 1) {
  let count = n1,
    result = 0;
  for (let i = 0; i <= n2 - n1; i++) {
    result += count;
    if (step > 1) {
      console.log(count);
      count += step;
      if (count > n2) {
        break;
      }
    } else {
      console.log(count);
      count++;
    }
  }
  return `Result: ${result}`;
}

console.log(sumRange(1, 10, 3)); */

class Student {
  constructor(firstName) {
    this.firstName = firstName;
  }

  describe() {
    return `Person named ${this.firstName}`;
  }

  static extractNames(students) {
    return students.map((student) => student.firstName);
  }
}

class StudentYear extends Student {
  constructor(student, year) {
    super(student);
    this.year = year;
  }

  describe() {
    return super.describe() + ` from class ${this.year}`;
  }
}

const eunyung = new StudentYear("Eunyung", "2-C");
const haejoon = new StudentYear("Haejoon", "1-B");

console.log(`${eunyung.describe()}\n${haejoon.describe()}`);
