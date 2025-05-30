const readline = require('readline-sync')

const num1 = readline.questionInt("Digite o primeiro numero: ")
const num2 = readline.questionInt("Digite o segundo número: ")
const num3 = readline.question("Digite o terceiro núnmero: ")

if (num1 + num2 > num3){
    console.log(`${num1} + ${num2} é maior que ${num3}`)
} else if (num1 + num2 === (num3)){
    console.log("São iguais")
}else{
    console.log(`${num1} + ${num2} é menor que ${num3}`)
}
