let ingrs = []

function add(){
    let addIngs = prompt('o igrediente que quer adicionar')
    if (ingrs.indexOf(addIngs)==-1){
        ingrs.push(addIngs)
        alert(addIngs+' foi adicionado a lista')
    }
    else    {
        alert('O ingrediente '+addIngs+' já está na lista')
    }
    console.log(ingrs)
}                                                           

function remove(){
    let redIng = prompt('o ingrediente que quer remover')
    if (ingrs.indexOf(redIng)==-1){
        alert('o igrediente '+redIng+' não está presente na lista')
    }
    else{
        let n = ingrs.indexOf(redIng)
        ingrs.pop(n)
        alert(redIng+' foi removido da lista')
    }
    console.log(ingrs)
}

function ver(){
    if (ingrs.length == 0){
        alert('o seu carrinho de compras está vazio')
    }
    else{
        alert('sua lista:\n'+ingrs)
    }
}