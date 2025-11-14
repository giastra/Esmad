let lista = []
while (lista.length<15){
let numAet = Math.random()*(101- 1 )+1
numAet=Math.ceil(numAet)
numAet=numAet-50
if (lista.indexOf(numAet)==-1){
    lista.push(numAet)
}
}
let pisitivo = 0
let negativo = 0
for (let numero = 0; numero<lista.length; numero ++)
    if (lista[numero]>0){
        pisitivo ++
    }
    else if (lista[numero]<0){
        negativo ++
    }
console.log(lista.sort())
console.log(pisitivo)
console.log(negativo)
alert('A lista contia '+lista+'\nnumeros positivos '+pisitivo+'\nnumeros negativos '+negativo)