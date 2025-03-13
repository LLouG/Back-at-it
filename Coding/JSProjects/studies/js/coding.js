// https://youtu.be/KDRdsLJY7DE?t=1768

// https://youtu.be/KDRdsLJY7DE?t=3147

/*
let johnHeight = 1.95;
let johnWeight = 92;
let johnBmi = johnWeight / (johnHeight * johnHeight);


let markHeight = 1.69;
let markWeight = 78;
let markBmi = markWeight / (markHeight * markHeight);


console.log("John's BMI is " + johnBmi)
console.log("Mark's BMI is " + markBmi)
let isHigher = johnBmi > markBmi;
console.log("Is John's BMI higher than Mark's? " + isHigher);
*/


// https://youtu.be/KDRdsLJY7DE?t=3546

// https://youtu.be/KDRdsLJY7DE?t=4657

// Ternary Operator
/*
let firstName = 'Jim';
let age = 16;

age >= 18 ? console.log(firstName + ' drinks beer.')
: console.log(firstName + ' drinks juice.');

let drink = age >= 18 ? 'beer' : 'juice';
console.log(drink);
*/


// Switch Statement
/*
let firstName = 'Pam'
let job = 'teacher';
switch (job) {
    case 'teacher':
    case 'instructor':
        console.log(firstName + ' teaches kids how to code.');
        break;
    case 'driver':
        console.log(firstName + ' drives an uber in Lisbon.');
        break;
    case 'designer':
        console.log(firstName + ' designs beatiful websites.');
        break;
    default:
        console.log(firstName + ' does something else.');
}
*/

/*
let firstName = 'Jim';
let age = 29;
switch (true) {
    case age < 13:
        console.log(firstName + ' is a boy.');
        break;
    case age >= 13 && age < 20:
        console.log(firstName + ' is a teenager.');
        break;
    case age >= 20 && age < 30:
        console.log(firstName + ' is a young man.');
        break;
    default:
        console.log(firstName + ' is a man.')
}
*/


// https://youtu.be/KDRdsLJY7DE?t=5444
// Falsy values: undefined, null, 0, '', NaN
// Truthy values: NOT falsy values


// https://youtu.be/KDRdsLJY7DE?t=5926

/* let johnTeam = (89 + 120 + 103) / 3;
let markTeam = (116 + 94 + 123) / 3;
let maryTeam = (97 + 134 + 105) / 3; */

/*
switch (true) {
    case johnTeam > markTeam:
        console.log('John\'s team wins with ' + johnTeam + ' points!');
        break;
    case markTeam > johnTeam:
        console.log('Mark\'s team wins with ' + markTeam + ' points!');
        break;
    default:
        console.log('Draw!')
}
*/
/*
switch (true) {
    case johnTeam > markTeam && johnTeam > maryTeam:
        console.log('John\'s team wins with ' + johnTeam + ' points!');
        break;
    case markTeam > johnTeam && markTeam > maryTeam:
        console.log('Mark\'s team wins with ' + markTeam + ' points!');
        break;
    case maryTeam > johnTeam && maryTeam > markTeam:
        console.log('Mary\'s team wins with ' + maryTeam + ' points!');
        break;
    default:
        console.log('Draw!')
}
*/


// https://youtu.be/KDRdsLJY7DE?t=6555

// https://youtu.be/KDRdsLJY7DE?t=8602
/*
function tipsCalculator(bill) {
    let percentage;
    if (bill < 50) {
        percentage = .2;
}   else if (bill >= 50 && bill < 200) {
        percentage = .15;
}   else {
        percentage = .1;
    }
    return percentage * bill; 
}

let bills = [124, 48, 268];
let tips = [tipsCalculator(bills[0]),
            tipsCalculator(bills[1]),
            tipsCalculator(bills[2])];
let finalValues = [bills[0] + tips[0],
                  [bills[1] + tips[1]],
                  [bills[2] + tips[2]]];
console.log(tips, finalValues);
*/


// https://youtu.be/KDRdsLJY7DE?t=9182

// https://youtu.be/KDRdsLJY7DE?t=9719

/*
let jim = {
    firstName: 'Jim',
    lastName: 'Halpert',
    birthYear: 1978,
    friends: ['Pam', 'Dwight', 'Kevin', 'Michael'],
    job: 'salesman',
    isMarried: false,
    calcAge: function() {
        this.age = 2022 - this.birthYear;
    }
};

jim.calcAge();
console.log(jim);
*/


// https://youtu.be/KDRdsLJY7DE?t=10157

/*
let john = {
    fullName: 'John Smith',
    height: 1.95,
    mass: 92,
    calcBmi: function() {
        this.bmi = this.mass / (this.height * this.height);
        return this.bmi;
    }
};

const mark = {
    fullName: 'Mark Miller',
    height: 1.69,
    mass: 78,
    calcBmi: function() {
        this.bmi = this.mass / (this.height * this.height);
        return this.bmi;
    }
}

if (john.calcBmi() > mark.calcBmi()) {
    console.log(john.fullName + ' has a higher BMI of ' + john.bmi);
} else if (mark.bmi > john.bmi) {
    console.log(mark.fullName + ' has a higher BMI of ' + mark.bmi);
} else {
    console.log('They have the same BMI.');
}
*/

//Loop
/*
let jim = ['Jim', 'Halpert', 1978, 'salesman'];
for (let i = 0; i < jim.length; i++) {
    if (typeof jim[i] !== 'string') continue;
    console.log(jim[i]);
}

for (let i = 0; i < jim.length; i++) {
    if (typeof jim[i] !== 'string') break;
    console.log(jim[i]);
}

// Looping backwards
for (let i = jim.length - 1; i >= 0; i--) {
    console.log(jim[i])
}
*/


// https://youtu.be/KDRdsLJY7DE?t=12048
/*
let john = {
    fullName: 'John Smith',
    bills: [124, 48, 268, 180, 42],
    calcTips: function() {
        this.tips = [];
        this.finalValues = [];
        for (let i = 0; i < this.bills.length; i++)
        {
            let percentage;
            let bill = this.bills[i];
            if (bill < 50) {
                percentage = .2;
            } else if (bill >= 50 && bill < 200) {
                percentage = .15;
            } else {
                percentage = .1;
            }
            this.tips[i] = bill * percentage;
            this.finalValues[i] = bill + bill * percentage;
        }
    }
}


// https://youtu.be/KDRdsLJY7DE?t=13021

let mark = {
    fullName: 'Mark Miller',
    bills: [77, 475, 110, 45],
    calcTips: function() {
        this.tips = [];
        this.finalValues = [];
        for (let i = 0; i < this.bills.length; i++)
        {
            let percentage;
            let bill = this.bills[i];
            if (bill < 100) {
                percentage = .2;
            } else if (bill >= 100 && bill < 300) {
                percentage = .1;
            } else {
                percentage = .25;
            }
            this.tips[i] = bill * percentage;
            this.finalValues[i] = bill + bill * percentage;
        }
    }
}

function calcAverage(tips) {
    let sum = 0;
    for (let i = 0; i < tips.length; i++) {
        sum = sum + tips[i];
    }
    return sum / tips.length;
}

john.calcTips();
mark.calcTips();

john.average = calcAverage(john.tips);
mark.average = calcAverage(mark.tips);
console.log(john, mark);

if(john.average > mark.average) {
    console.log(john.fullName + '\'s family pays higher tips, with an average of $' + john.average)
} else if(mark.average > john.average) {
    console.log(mark.fullName + '\'s family pays higher tips, with an average of $' + mark.average)
} else {

}
*/


// https://youtu.be/KDRdsLJY7DE?t=13620

// https://youtu.be/KDRdsLJY7DE?t=14161
