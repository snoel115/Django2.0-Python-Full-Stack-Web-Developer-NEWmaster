var fn = prompt("First name: ");
var ln = prompt("Last name: ");
var age = prompt("Age: ");
var hight = prompt("Your hight in cm: ");
var dogName = prompt("Your dog name: ");

var resValue = false;

if (fn[0] === ln[0]) {
  if (age > 20 && age < 30) {
    if (hight >= 170) {
      if (dogName[dogName.length - 1] === "y"){
        console.log("Hello my friend ...  Here is your secret message")
        resValue = true;
      }
    }
  }
}

if (resValue === false) {
  console.log("You are a nobody to us, go away")
}
