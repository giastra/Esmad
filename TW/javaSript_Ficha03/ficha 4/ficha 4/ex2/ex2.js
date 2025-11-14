let numeros = []
let estrelas = []

while (numeros.length < 5  || estrelas.length < 2 ){

    numAet = Math.random()*(50- 1 )+1
numAet=Math.ceil(numAet)

if (numeros.indexOf(numAet) == -1 && numeros.length<5){
    numeros.push(numAet)
}

numAet = Math.random()*(12- 1 )+1
numAet=Math.ceil(numAet)

if (estrelas.indexOf(numAet) == -1 && estrelas.length<2){
    estrelas.push(numAet)
}

}
console.log(numeros)
console.log(estrelas)