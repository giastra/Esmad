const tracks=catalogue.map(cat => Track.fromObject(cat)) //map é basicamente um loop que faz uma lista para cada elemento e => converte no posterior
console.log(tracks[0].getInfo())

let myPlaylist = new Playlist("My  Playlist","soundbase_user")
console.log(myPlaylist.size)

function renderCard(track) {
   let html=(`
    <div class="track-card" data-id=${track.id}> 
  <div class="card-header"> 
    <h3>${track.title}</h3> 
    <span class="genre-tag">${track.genre}</span> 
  </div> 
  <p class="artist">${track.artist}</p> 
  <p class="meta">${formatDuration(track.duration)} · ${formatPlays(track.plays)} plays</p> 
  <div class="card-actions"> 
    <button class="btn-play" data-id="${track.id}" aria-label="Play ${track.title}">▶ Play</button> 
    <button class="btn-details" data-id="${track.id}" aria-label="Details for ${track.title}">Details</button> 
  </div> 
</div>
`)
return html
}

function renderCards(tracks) {
    const htmlFormat=tracks.map(track => renderCard(track))
    let htmlJoind = htmlFormat.join('')
    
    document.getElementById('catalogue-grid').innerHTML=htmlJoind
}
renderCards(tracks)

function renderRow(track) {
    let row=`<tr data-id=${track.id}>${track.title}, ${track.artist}, ${track.genre}, ${formatDuration(track.duration)}, ${formatPlays(track.plays)} </tr>`
    return row
}

function renderTable(tracks) {
    const htmlFormat=tracks.map(track => renderRow(track))
    let htmlJoind = htmlFormat.join('')
    
    document.getElementById('catalogue-table-container').innerHTML=`
    <table>
      <thead>
        <tr>
          <th>Title</th>
          <th>Artist</th>
          <th>Genre</th>
          <th>Duration</th>
          <th>Plays</th>
        </tr>
      </thead>

      <tbody>
        ${htmlJoind}
      </tbody>
    </table>
    `}

document.getElementById('filter-controls').addEventListener('click',function(){
    if (event.target.classList.value == 'btn-filter'){
        let GeneroEvento =event.target.dataset.genre

        // dentro do documento seleciona toda a classe btn-filter e para cada dentro da classList remove o ativo
        document.querySelectorAll(".btn-filter").forEach(d => d.classList.remove("active"))
        console.log(document.getElementsByClassName('btn-filter active'));
    
        if (GeneroEvento != 'all'){
            
            const Tracks2 = []
            for (const track of tracks) {
                if (track.genre == GeneroEvento){
                    Tracks2.push(track)
                }
            }
            renderCards(Tracks2)
            event.target.classList.value='btn-filter active'
            
        }
        else{
            renderCards(tracks)
             event.target.classList.value='btn-filter active'
            
        }
    }
    
})

function renderModal(track) {
    return `<div class="modal-card"> 
                <button class="btn-close" aria-label="Close modal">✕</button> 
                <h2>${track.title}</h2> 
                <p>Artist: ${track.artist}</p> 
                <p>Genre: ${track.genre}</p> 
                <p>Duration: ${formatDuration(track.duration)}</p> 
                <p>Plays: ${formatPlays(track.plays)}</p> 
                <p>Liked: ${track.liked}</p> 
            </div> `
}

document.getElementById('catalogue-grid').addEventListener('click',function(){
    if (event.target.classList.value == 'btn-details'){
        const idTrack =   event.target.dataset.id
        const track = tracks.find(t => t.id == idTrack)
        document.querySelector('#modal-content').innerHTML=renderModal(track)
        document.querySelector("#modal-overlay").classList.remove("hidden")
        document.querySelector(".btn-close").addEventListener('click',function(){
            document.querySelector('#modal-overlay').classList.add('hidden')
        })
    }
})