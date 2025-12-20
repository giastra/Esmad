let tasks = [
    {task: "do homework",
    category: "school"},

    {task: "clean the house",
    category: "chores"},
]

function lista(){
document.getElementById('list').innerHTML=`<div class="container text-center">`
for (de=0;de<tasks.length;de++)
    {
    document.getElementById('list').innerHTML+=`
    <div class="col w-100 mw-100 text-center">
    <button type="button" class="btn btn-success" onclick="ccd(${de})" data-bs-toggle="modal" data-bs-target="#registerModal">mark as complete</button> 
     ${tasks[de].task}......................${tasks[de].category}
    </div>
    </div>`
}
}

lista()
document.getElementById('buton').addEventListener("click",MoreTask)
function MoreTask(event){
    event.preventDefault()
    let txt = document.getElementById("task").value
    let cat = document.getElementById("category").value
    tasks.push({task:txt,category:cat})
    lista()
}
let numero = 0
function ccd(f){
    numero=f
}

function sim(ded){
    if (ded == true){
            tasks.splice(numero, 1) 
            lista()
    } 
}


