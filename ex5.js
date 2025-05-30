console.clear()
const readline = require('readline-sync')


const num1 = readline.questionInt("Digite a primeira nota: ")
const num2 = readline.questionInt("Digite a segunda nota: ")

function media(num1 , num2){
    media = (num1 + num2) / 2
    console.log(`A média é ${media}`)
}

media(num1,num2)





