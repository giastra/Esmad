let x = prompt('  1\n   ----\n2 |    | 3\n   ----\n   4\nO tamanho de um dos 4 lados do poligono, 1º lado')
let y = prompt('  1\n   ----\n2 |    | 3\n   ----\n   4\n2º lado')
let z = prompt('  1\n   ----\n2 |    | 3\n   ----\n   4\n3º lado')
let c = prompt('  1\n   ----\n2 |    | 3\n   ----\n   4\nO ultimo para fechar')
let cd1=false
let cd2=false
let cd3=false

if (x==z==y==c){
    alert('Esse poligono é uma quadrado')
}

else if (x==c && y==z){
    alert('Esse poligono é um retangulo')
}

else{
    alert('Isso é certamente um poligono')
}