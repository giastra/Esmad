let numeTira = []
function Tnume(){
    let ff = true
    while (ff){
    numAet = Math.random()*(90- 1 )+1
    numAet=Math.ceil(numAet)
    if (numeTira.indexOf(numAet) == -1){
        numeTira.push(numAet)
        alert('Numero tirado foi '+numAet)
        ff = false
    }
    else if (numeTira.length==90){
        alert('Todos os números foram tirados! A recomeçar...')
        let ff = false
        numeTira = []
    }
    }
    console.log(numeTira.sort())
}

function Bingo(){
    if (numeTira.length >= 15){
        let contiar= prompt('Continuar o jogo (s/n)')
        if (contiar == 'n'){
            numeTira = []
            alert('Jogo encerrado. A recomeçar...')
        }
    }
    else{
        alert('Impossível, continue.')
    }
}