let egg1=0
let egg2=0
let achados=0
let clics =0

while (egg1 == egg2) { 
egg1= Math.floor(12* Math.random()+1 )
egg2= Math.floor(12* Math.random()+1 )
}

console.log(egg1,egg2);
    
let elemento = ''
function evet(i) {
    document.getElementById(i).addEventListener('mouseover',function() {
     document.getElementById(i).setAttribute('style',"border: 4px solid red; ")
    })
    document.getElementById(i).addEventListener('mouseout',function() {
     document.getElementById(i).setAttribute('style',"border: ; ")
    })
    document.getElementById(i).addEventListener('click',function() {
        if (achados < 3){clics++}
        
        

     if ((i == egg1 || i == egg2) ){
        
        if (achados == 2 && elemento!=document.getElementById(i) ){
            document.getElementById(i).innerHTML=`<img src='Images/Ovo.png'>`
        document.getElementById('fim').innerHTML+='Parabéns, encontraste os Ovos de Páscoa'
        achados++
        document.getElementById('cabeca').innerHTML+=` <button id="clicls" onclick="clicks()" >Clicks</button > `
        }

        else if (achados <1){
            document.getElementById(i).innerHTML=`<img src='Images/Ovo.png'>`
            setTimeout(() => {
                document.getElementById(i).innerHTML='<img src="Images/DiscoverEggs.png"></img>'
            }, 2000)
            elemento = document.getElementById(i)
            achados++
            
        }

        else if (achados >0 && elemento != document.getElementById(i)){
            achados++
            document.getElementById(i).innerHTML=`<img src='Images/Ovo.png'>`
            elemento = document.getElementById(i)
        }
    }
    })

}

for (let i = 1; i < 13; i++) {
    evet(i)
}

function clicks() {
    alert(`Número de clickes usados: ${clics}`)
}
