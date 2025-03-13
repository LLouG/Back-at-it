/* const myArray = ["Haejoon", "Marie", "Eunyung", "Hara", "Minju", "Juwan"];

function filter(array) {
  let passed = [];
  for (let element of array) {
    if (element.length <= 5) {
      passed.push(element);
    }
  }
  return passed;
}

console.log(filter(myArray)); */

/* const myNumArray = [1, 2, 3, 4, 5];
function reduce(array, combine, start) {
  let current = start;
  for (let element of array) {
    current = combine(current, element);
  }
  return current;
}
console.log(reduce(myNumArray, (a, b) => a + b, 0)); */

/* console.log([1, 2, 3, 4, 5].reduce((a, b) => a * b));

let horseShoe = "🐴👟";
for (let item of horseShoe) {
  console.log(item.codePointAt(0));
}
console.log("\u128095"); */

function countBy(items, groupName) {
  let counts = [];
  for (let item of items) {
    let name = groupName(item);
    let known = counts.find((c) => c.name == name);
    if (!known) {
      counts.push({ name, count: 1 });
    } else {
      known.count++;
    }
  }
  return counts;
}
console.log(countBy([1, 2, 3, 4, 5], (n) => n > 2));
