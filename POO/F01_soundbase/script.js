// arow function:
// let var = variavel => {return variavel}
// var(variavel)
// evitar botar funções muito variaveis nos obijetos

// Para  formatDuration e greetArtist, use a sintaxe completa (com {} e return quando necessário).  
// Para isLongTrack e formatPlays, use retorno implícito (sem {} nem  return)

// Converts seconds to "m:ss" format
let formatDuration= seconds =>  {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return m + ":" + (s < 10 ? "0" + s : s);
}

console.log(formatDuration(1000)); //em segundos

// Returns true if the track is longer than 4 minutes
let isLongTrack= duration => duration > 240

console.log(isLongTrack(300)); //em segundos


// Logs a welcome message for an artist
let greetArtist = (name, genre) => console.log("Welcome to SoundBase, " + name + "! Your genre is " + genre + ".")

greetArtist("Gian","Metal")  //string


// Returns plays formatted with "k" suffix (e.g. 12500 -> "12.5k")
let formatPlays = plays =>  {
    if (plays >= 1000000) {
        return (plays / 1000000).toFixed(1) + "M";
    }
    else if (plays >= 1000) {
        return (plays / 1000).toFixed(1) + "k";
    }
    return plays.toString();
}

console.log(formatPlays(2000));  //inteiro


// Returns recives 2 or 3 argumes title,artist and genre, if genre='' return "Unknown"  "Title by artist [genre]"
let describeTrack = (title, artist, genre="Unknown") => `${title} by ${artist} [${genre}]`

console.log(describeTrack('Stranger in a Stranger Land','Iron Mainden','Metal'));
console.log(describeTrack('Stranger in a Stranger Land','Iron Mainden'));


// aceita um número indefinido de títulos de faixas ( ...titles) e os imprime na consola, numerados a partir de 1. P
let logTracks = (...titles) => {
    n=1
    for (title of titles){
        console.log(`${n}. ${title}`);
        n++
        
    }
}
logTracks('Stranger in a Stranger Land','Highway to Hell')


const track ={
    title:"Stranger in a Stranger Land",
    artist:"Iron Mainden",
    duration:347,
    genre:"Metal",
    plays:14647895,
    liked:false,

    }


track.play = function(){
    this.plays++
    console.log(`Now playing: ${this.title} by ${this.artist} (plays:${this.plays})`);    
}
track.play()
track.play()


track.like= function() {
    if (this.liked==true){
        this.liked=false
        console.log(`${this.title} unliked`);
    }
    else{
        this.liked=true
        console.log(`${this.title} liked`);
    }
        
}
track.like()
track.like()


track.getInfo=function(){
    return `${this.title} ${this.artist}|${formatDuration(this.duration)}|${this.genre}|${formatPlays(this.plays)} ` 
}
console.log(track.getInfo());

//nova propriedade album ao track
track.album={
    title:"Somewhere in TIme",
    year:1985,
    totalTracks:8
}


track.getAlbumInfo=function(){
    console.log(`${this.title} is from the album ${this.album.title} (${this.album.year}) - ${this.album.totalTracks} tracks`);
    
}
track.getAlbumInfo()

lsita=[]
n=0
for (info in track){
    if (typeof track[`${info}`] != 'function'){
        console.log( info,':', track[`${info}`]);
    }
}

//terminei na 10