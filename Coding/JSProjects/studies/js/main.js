const myArray = [];

myArray[0] = "Loug";
myArray[1] = "42";
myArray[2] = false;

myArray.splice(2, 2, "Yo");
console.log(myArray);
console.log(myArray[myArray.length - 1]);