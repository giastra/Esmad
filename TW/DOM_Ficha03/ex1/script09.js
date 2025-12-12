let num = prompt('Insira um numero') //cria uma variavel 
let seq = document.getElementById('seq') //puxa do html o id
let FB=[] //lista

for (let t=1;t<=num;t++){
    seq.innerHTML+=`<span> ${t} </span>`
}

function format(){
    for (let t=1; t<=num; t++){
        if(t%3 == 0 && t%5 != 0){
            FB.push('Fizz')
        }
        else if(t%5 == 0 && t%3 != 0){
            FB.push('Buzz')
        }
        else if(t%3 == 0 && t%5 == 0){
            FB.push('FizzBuzz')
        }
        else{
            FB.push(t)
        }
    }
    seq.innerHTML=''
    for(num of FB){
        seq.innerHTML+=`<span> ${num} </span>`
    }
}

let FizzBuzz=document.getElementById('FizzBuzz')
FizzBuzz.addEventListener('click',format)

