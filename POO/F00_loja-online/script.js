const produtos = [
  {
    nome: "Teclado Mecânico",
    preco: 89.99,
    stock: 14,
    emPromocao: true,
    descricao: "Teclado mecânico com switches de alta qualidade",
  },
  {
    nome: "Rato Sem Fios",
    preco: 34.5,
    stock: 2,
    emPromocao: false,
    descricao: "Rato sem fios ergonómico com sensor óptico",
  },
  {
    nome: 'Monitor 27"',
    preco: 349.0,
    stock: 0,
    emPromocao: true,
    descricao: "Monitor LED de 27 polegadas Full HD",
  },
  {
    nome: "Headset Gaming",
    preco: 59.9,
    stock: 28,
    emPromocao: false,
    descricao: "Headset gaming com som surround 7.1",
  },
  {
    nome: "Webcam HD",
    preco: 45.0,
    stock: 7,
    emPromocao: true,
    descricao: "Webcam HD 1080p com microfone integrado",
  },
];

let item=0

let nome= produtos[item].nome
let preco= produtos[item].preco
let stock= produtos[item].stock
let emPromocao= produtos[item].emPromocao
let desconto=produtos[item].desconto
console.log(typeof(nome));
console.log(typeof(preco));
console.log(typeof(stock));
console.log(typeof(emPromocao));
console.log(typeof(desconto));

let iva= 0.23
let preco_iva= (preco*iva+preco).toFixed(2)

console.log(`${nome} - ${preco_iva} (stock: ${stock})`);
 
function classificarStock(n){
    if (n == 0){
        desconto='Esgotado'
    }
    else if(n >=1 && n<=5){
        desconto='Stock critico'
    }
    else if(n >=6 && n<=20){
        desconto='Stock normal'
    }
    else if(n > 20){
        desconto='Stock elevado'
    }
    else{
        desconto='não classificado'
    }
    return desconto
}

console.log(classificarStock(0))
console.log(classificarStock(3))
console.log(classificarStock(14))
console.log(classificarStock(30))

let etiqueta= emPromocao == true ? 'Em promoção' : 'Preço normal' 

console.log(etiqueta);

for (item=0;item<produtos.length;item++){
    console.log(produtos[item].nome);
}

function calcularValorStock(lista){
    let total=0
    for (item=0;item<produtos.length;item++){
        s=produtos[item].stock
        p=produtos[item].preco
        total+=s*p
        console.log(total);
        
    }
    return `Valor total em stock: ${total}€`
}

console.log(calcularValorStock(produtos));


let produtosDisponiveis=[]
for (item=0;item<produtos.length;item++){
    let stock= produtos[item].stock
    if(stock>0){
        produtosDisponiveis.push(produtos[item])
    }
}
console.log(produtosDisponiveis);


console.log(produtosDisponiveis.length);
console.log(item-produtosDisponiveis.length);

function descricaoProduto(w){
    return(`${w.nome} - ${w.preco}€ - ${classificarStock(w.stock)} - ${etiqueta}`);
}


function renderizarProdutos(){
    for (item=0;item<produtos.length;item++){

    console.log(descricaoProduto(produtos[item]));
  
    document.getElementById("lista-produtos").innerHTML+=`<p>${descricaoProduto(produtos[item])}</p>`
}
}

renderizarProdutos();

let mostrar=false
let butao = document.getElementById('btn-disponiveis');
butao.addEventListener("click",function(){
    document.getElementById("lista-produtos").innerHTML=''
    if (mostrar==false){
    butao.innerHTML='Mostrar todos'
    mostrar=true
    for (item=0;produtosDisponiveis.length;item++){
        
        document.getElementById("lista-produtos").innerHTML+=`<p>${descricaoProduto(produtosDisponiveis[item])}</p>`
    }
    }

    else{
        mostrar=false
        butao.innerHTML='Mostrar disponíveis'
        renderizarProdutos()
        
    }
})

// arow function:
// let var = variavel => {return variavel}
// var(variavel)
// evitar botar funções muito variaveis
