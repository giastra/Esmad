// atividade 01
// let numero = prompt ('Introdusa um numero para ser calculada a tabuada dele: ')
// for (let sequencia = 1; sequencia <=10 ; sequencia++){
//     console.log(`${numero} * ${sequencia} = ${numero*sequencia}`)
// }

// atividade 02
// let numero = prompt ('Introdusa um numero para ser verificado se é primo')
// function nPrimo(numero){    
//     if (numero%2 == 0 && numero != 2 ){
//         return false
//     }
//     else if (numero%3 == 0 && numero != 3 ){
//         return false
//     }
//     else if (numero%5 == 0 && numero != 5 ){
//         return false
//     }
//     else if (numero%11 == 0 && numero != 11 ){
//         return false
//     }
//     else if (numero%17 == 0 && numero != 17 ){
//         return false
//     }
//     else{
//         return true
//     }
// }
// if (nPrimo(numero)==true){
//     alert(numero+' é primo')
// }
// else{
//     alert(numero+ ' não é primo')
// }

// atividade 03
// function par(numero){
//     if (numero%2 == 0){
//         return true
//     }
//     else{
//         return false
//     }
// }

// for (let numero = 1; numero<=10; numero ++){
//     if (par(numero)==true){
//         console.log(`O numero ${numero} é par`)
//     }
    
// }

// atividade 04

let loop=true
let tents = 0
let num = prompt('escolha um numero de 1 a 10')

let numAet = 0
while (loop){
    tents ++
    console.log('tentativas: '+tents)
    numAet = Math.random()*(10- 1 )+1
    numAet=Math.ceil(numAet)
    console.log('numero: '+numAet)
    if (num == numAet){
        loop = false
    }
}
if (tents == 1){
    alert('Parabens o numero foi igual na 1ª tentativa')
}

alert('foram necessarias  '+tents+' para acertar o numero escolhido\n f12 para ver o caminho feito')