let ingrs = []

function add(){
    let addIngs = prompt('o igrediente que quer adicionar')
    if (ingrs.find(i => i == addIngs))
        alert('O ingrediente '+addIngs+'já está na lista')
}