/* hummus(1);


function hummus(factor) {
  const ingredient = function (amount, unit, name) {
    let ingredientAmount = amount * factor;
    if (ingredientAmount > 1) {
      unit += "s";
    }
    console.log(`${ingredientAmount} ${unit} ${name}`);
  };
  ingredient(1, "can", "chickpeas");
  ingredient(0.25, "cup", "tahini");
  ingredient(0.25, "cup", "lemon juice");
  ingredient(1, "clove", "garlic");
  ingredient(2, "tablespoon", "olive oil");
  ingredient(0.5, "teaspoon", "cumin");
} */

/* function multiplier(factorr) {
  return (number) => number * factorr;
}
let twice = multiplier(2);
console.log(twice(5)); */

/* function findSolution(target) {
  function find(current, history) {
    if (current == target) {
      return history;
    } else if (current > target) {
      return null;
    } else {
      return (
        find(current + 5, `(${history} + 5)`) ??
        find(current * 3, `(${history} * 3)`)
      );
    }
  }
  return find(1, "1");
}
console.log(findSolution(2)); */

/* function zeroPad(number, width) {
  let string = String(number);
  while (string.length < width) {
    string = "0" + string;
  }
  return string;
}
function printFarmInventory(cows, chickens, pigs) {
  console.log(`${zeroPad(cows, 3)} Cows`);
  console.log(`${zeroPad(chickens, 3)} Chickens`);
  console.log(`${zeroPad(pigs, 3)} Pigs`);
}
printFarmInventory(7, 16, 3); */

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
    return super.describe() + ` (${this.title})`;
  }
}

const loug = new Employee("Loug", "CTO");
console.log(loug.describe()); */

/* console.log(JSON.stringify({ first: "Jane", last: "Doe" }, null, 2)); */

/* let a = Number.parseInt(123.45);
console.log(a);

const obj = {};
obj["true"] = 123;
console.log(typeof obj.true);

console.log(Number(true));

console.log(Object.is(123, "123"));
console.log(Object.getPrototypeOf(Object.prototype));
console.log(/a/.exec("x"));
console.log(1 > 2 ? true : false); */

/* function func(x) {
  if (x === undefined) {
    throw new Error("Missing Parameter x");
  }
}

func(); */

/* const a = null ?? "hello";
console.log(a); */

/* function findMin(numbers) {
  let min = Infinity;
  for (const n of numbers) {
    if (n < min) min = n;
  }
  return min;
}
console.log(findMin([5, -1, 2, -92]), findMin([])); */

/* console.log(15 * 10 ** -1, 15 / 10 ** 1);
console.log(Number.MAX_SAFE_INTEGER);
console.log(Number.isSafeInteger(10));
console.log((1).toString().padStart(4, "0"));
console.log(Number.parseInt("abcd", 36)); */

/* let journal = [];

function addEntry(events, squirrel) {
  journal.push({ events, squirrel });
}

addEntry(["work", "touched tree", "pizza", "running", "television"], false);
addEntry(
  [
    "work",
    "ice cream",
    "cauliflower",
    "lasagna",
    "touched tree",
    "brushed teeth",
  ],
  false
);
addEntry(["weekend", "cycling", "break", "peanuts", "beer"], true);

function tableFor(event, journal) {
  let table = [0, 0, 0, 0];
  for (let i = 0; i < journal.length; i++) {
    let entry = journal[i],
      index = 0;
    if (entry.events.includes(event)) index += 1;
    if (entry.squirrel) index += 2;
    table[index] += 1;
  }
  return table;
}
console.log(tableFor("pizza", journal));

for (let entry of journal) {
  console.log(`${entry.events.length} events`);
}
function journalEvents(j) {
  let events = [];
  for (let entry of journal) {
    for (let event of entry.events) {
      if (!events.includes(event)) {
        events.push(event);
      }
    }
  }
  return events;
}
console.log(journalEvents(journal)); */

/* function remove(array, index) {
  return array.slice(0, index).concat(array.slice(index + 1));
}
console.log(remove(["a", "b", "c", "d", "e"], 2)); */

/* let string = JSON.stringify({
  squirrel: false,
  events: ["weekend"],
});
console.log(string);
console.log(JSON.parse(string).events); */

/* let myStr = `\Hi \u{1F642}`;
let myArr = Array.from(myStr);

for (const letters of myArr) {
  console.log(letters.padStart(3, "# "));
} */

/* console.log("F".charCodeAt(0).toString(16)); // Char code is the standard library’s name for code unit */

/* const regexp = /(?<year>[0-9]{4})-(?<month>[0-9]{2})/g;
const replacer = (...args) => {
  const groups = args.pop();
  return "|" + groups.year + "|";
};
console.log("a 1995-12 b".replaceAll(regexp, replacer)); */

/* const sLiteral = [`Hello, \n\t World!`];
console.log(sLiteral);
console.log(String.raw`Hello, \n\t World!`); */
