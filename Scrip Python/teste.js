function randint(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
  }

let num = [];
let compar = [];
let d = 0;
let n = 0;
for (let c = 0; c < 6; c++) {
  n = randint(1, 6);
  if (c > 0) {
    num.push(n);
    console.log("-------------------------")
    console.log("vetor :", num)
  }
  if (num.length >= 2) {
    compar = num.slice(0, c - 1);
    console.log("vetor2:", compar)
    while (compar.includes(n)) {
      d = num.indexOf(n);
      n = randint(1, 5);
      console.log("n modificado: ", n)
      num[d] = n;
    }
  }
}
console.log("Valor abaixo: ")
num.sort(function (a, b) {return a - b;});
console.log(num)
