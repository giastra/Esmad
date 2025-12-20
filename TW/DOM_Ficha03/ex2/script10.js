let num = prompt('Insira um numero') //cria uma variavel 
let seq = document.getElementById('seq') //puxa do html o id
let FB=[] //lista
let par =0
let imp =0
for (let t=1;t<=num;t++){
    if (t%2==0){
        seq.innerHTML+=`<span style='color:blue'> ${t} </span>`
        par++
    }
    else{
        seq.innerHTML+=`<span style='color:red'> ${t} </span>`
        imp++
    }
}
seq.innerHTML+=`<p>a quantidade de numeros par: ${par}</p>`
seq.innerHTML+=`<p>a quantidade de numeros impar: ${imp}</p>`