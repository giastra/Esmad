let numeros = [121, 123, 44, 456, 11, 90, 909, 22]
for (x = 0 ; x < numeros.length; x++){
    let oremun=numeros[x]
    oremun=oremun.toString()
    oremun=oremun.split('')
    oremun=oremun.reverse()
    oremun=oremun.join('')
    if (numeros[x]==oremun){
        console.log('O número '+numeros[x]+' é capicua.')
    }
        else{
            console.log('O número '+numeros[x]+' não é capicua.')
    }
}