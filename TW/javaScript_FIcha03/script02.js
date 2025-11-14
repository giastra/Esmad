// atividade 01
function nick(){
    let nome = prompt('introduza o seu primeiro nome')
    let apelido = prompt('introduza seu apelido')
    let numero = prompt('introduza um numero de 0 a 100')

    nome = nome.slice(0,3)
    apelido = apelido.slice(0,3)
    alert(nome+apelido+numero) 
}
// atividade 02
function escola (){
    let nota =  Math.ceil(Math.random() * (20 - 0 + 1)) + 0
    let res = ''
    if (nota <= 9){
        res = 'negativa'
    }
    else if (nota <= 13){
        res = 'Tem de ir a Prova Oral'
    }
    else if (nota <= 17){
        res = 'Positiva'
    }
    else{
        res='Exelente'
    }
    alert('O estudante teve '+nota+' valores, resultando em '+res)
}

// atividade 03
function vogais(){
    let palavra = prompt('Indroduza uma frase').toLowerCase()
    let Evog = palavra.split('e').length-1
    let Ivog = palavra.split('i').length-1
    let Ovog = palavra.split('o').length-1
    let Uvog = palavra.split('u').length-1
    let Avog = palavra.split('a').length-1
    alert(palavra+'\nnumero de A = '+Avog+' E = '+Evog+' I = '+Ivog+' O = '+Ovog+' U = '+Uvog)
}

// atividade 04
function ordNom(){
    let nome1 = prompt('Idroduza um nome ')
    let nome2= prompt('Introduza outro nome ')
    let nome3 = prompt('Introduza oultro nome ')
    let arr = [nome1,nome2,nome3]
    arr.sort()
    alert('nomes em ordem alfabetica: '+arr[0]+', '+arr[1]+' e '+arr[2])
}