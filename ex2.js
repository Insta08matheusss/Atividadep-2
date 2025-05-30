const readline = require('readline-sync')

const num1 = readline.questionInt("Digite o um numero: ")

if (num1 % 2 === 0){

    console.log(`${num1} é par`)
}else{
    console.log(`${num1} é impar`)
}
