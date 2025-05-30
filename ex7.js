console.clear()
const readline = require('readline-sync')

const nota = []

const nota1 = readline.questionInt("Digite a primeira nota: ")
const nota2 = readline.questionInt("Digite a segunda nota: ")
const nota3 = readline.questionInt("Digite a terceira nota: ")

media = [nota1 + nota2 + nota3] / 3

console.log(nota1)
console.long(nota2)
console.long(nota3)
console.log(`Sua nédia é ${media}`)
console.log(nota)

