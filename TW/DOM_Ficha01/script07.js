let dc =document.getElementsByTagName('li')
for (x = 0;x<dc.length;x++){
    console.log(dc[x])
}
console.log(dc);

function addPrat(){
    let prato = prompt('o prato que quer adicionar:')
    document.getElementsByTagName('ul')[0].innerHTML+=`<li>${prato}</li>`
}
document.getElementById('addPrato').addEventListener('click',addPrat)

function mOver(){
    document.getElementsByTagName('h1')[0].innerHTML=`Seja bem-vindo, faça-nos uma 
visita.`
}

function mOut(){
    document.getElementsByTagName('h1')[0].innerHTML=`Menu do Karpazinha Lanches`
}

document.getElementById('titulo').addEventListener('mouseover',mOver)

document.getElementById('titulo').addEventListener('mouseout',mOut)