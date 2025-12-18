let tasks = [
    {task: "do homework",
    category: "school"},

    {task: "clean the house",
    category: "chores"},
]

tasks[0].task
document.getElementById('list').innerHTML+=`<div class="container text-center">`
for (de=0;de<tasks.length;de++)
    {
    document.getElementById('list').innerHTML+=`
    <div class="col w-100 mw-100 text-center">
    <button type="button" class="btn btn-success">mark as complete</button> 
    ${tasks[de].task}......................${tasks[de].category}
    </div>
    </div>`
}

document.getElementById('buton').addEventListener("click",MoreTask)
function MoreTask(event){
    event.preventDefault()
    let txt = document.getElementById("task").innerHTML
    alert(txt)
}