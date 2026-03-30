// Seletor  Descrição  

// #app-title 
// : Título principal da aplicação ( <h1>) 

// #track-count 
// : Parágrafo para mostrar o número de faixas  

// #search-input 
// : Campo de texto para pesquisa  

// #track-list 
// : Contentor <div> onde as faixas serão renderizadas 

// #add-track-form 
// : Formulário para adicionar uma nova faixa  

// #form-title, #form-art-ist, #form-duration, #form-genre 
// : Campos do formulário 
document.getElementById('app-title').innerHTML=`SoundBase`
let ler = document.querySelector('h1').innerHTML
console.log(ler);



function renderTrack(track) {
    return `
    <div class="track-card" data-title="${track.title}"> 
    <h3>${track.title}</h3> 
    <p>${track.artist}· ${track.genre} · ${formatDuration(track.duration)}</p> 
    <p class="plays">${formatPlays(track.plays)} plays</p> 
    <button class="btn-like">♡ Like</button> 
    <button class="btn-remove">Remover</button> 
    </div>`
}

function renderCatalogue(tracks){
    let todo = tracks.map(track => renderTrack(track))
   todo=todo.join('');
   document.getElementById('track-list').innerHTML=todo
   let n=0
    for (i of catalogue){
    n++
    }

    document.getElementById('track-count').innerHTML=`${n} faixas disponíveis`

}
renderCatalogue(catalogue)
 
document.getElementById('search-input').addEventListener('input',function(){
    console.log(event.target.value);
})

let numeroANt=document.getElementById('track-count').innerHTML
numeroANt=Number(numeroANt.charAt(0))
nn=0

document.getElementById('track-list').addEventListener('click',function(){
    let click=(event.target);
    let nome=event.target.closest(".track-card")
    title=nome.getAttribute('data-title')

    if (click.classList.contains('btn-like')) {    
        console.log(`Like clicado: [${title}]`);        
    }

    else if (click.classList.contains('btn-remove')){
         nome.remove()
         nn+=1
        document.getElementById('track-count').innerHTML=`${numeroANt-nn} faixas disponíveis`


    //     let nome=event.target.closest(".track-card")
    // nome=nome.getAttribute('data-title')
    //     console.log(`Remover clicado: [${nome}]`);
    //     let txt=[]
    //     for (i of catalogue){
    //         txt.push(i.title)
    //     }
    //     console.log(txt);
        
    //     console.log(txt.indexOf(nome)+1);
        
    //     console.log( catalogue.splice(txt.indexOf(nome),1))
    //     console.log(catalogue);
    //     renderCatalogue(catalogue)

        }
    })

// document.getElementById('add-track-from').addEventListener('submit', function(){
//     event.preventDefault()
// })
