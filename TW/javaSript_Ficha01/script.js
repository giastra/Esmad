// atividade 1
// let numero1 = +prompt('escolha um numero: ') 
// let numero2 = +prompt('escolha um numero: ')
// if( numero1 > numero2){
//     alert(numero1 + ' é maior que ' + numero2)
// }else if (numero1 < numero2){
//     alert(numero1 + ' é menor que '+ numero2)
// }
// else{alert('Os valores são iguais')}

// // atividade 2
// let numero1 = +prompt('escolha um numero: ')
// if( numero1%2 == 0){
//     alert(numero1 + ' é par ')}
// else{alert(numero1+' é impar')}

// âtividade 3
// let peso = +prompt('itroduza o peso em kg : ') 
// let altura = +prompt('introduza a altura em m : ')
// let imc = +peso/(altura*altura)

// if (imc < 18.5){
//     alert('IMC de '+imc+' se colocando na magreza')
// }
// else if (imc < 24.9){
//     alert('IMC de '+imc+' se colocando no normal')
// }

// else if (imc < 24.9){
//     alert('IMC de '+imc+' se colocando no sobrepeso')
// }

// else if (imc < 34.9){
//     alert('IMC de '+imc+' se colocando no obesidade grau I')
// }

// else if (imc < 39.9){
//     alert('IMC de '+imc+' se colocando no obesidade grau II')
// }

// else{
//     alert('IMC de '+imc+' se colocando no obesidade grau III')
// }

// atividade 4
let escolha= prompt('Introduza o tipo de operação desejada : \n S = Soma, Sub = Subtração, M = Multiplicação, D = Divisão').toUpperCase()
let numero1= +prompt('Primeiro numero')
let numero2= +prompt('Segundo numero')
switch (escolha){
    case "S":
        resultado = numero1 + numero2
        alert(numero1+' + '+numero2+' = '+resultado)
    case "SUB":
        resultado = numero1 - numero2
        alert(numero1+' - '+numero2+' = '+resultado)
    case "M":
        resultado = numero1 * numero2
        alert(numero1+' * '+numero2+' = '+resultado)
    case "D":
        resultado = numero1 / numero2
        alert(numero1+' / '+numero2+' = '+resultado)
} 



