const entry = document.querySelector("#entry")
const submitButton = document.querySelector(".submit-btn")
const form = document.querySelector("form")
const alert = document.querySelector(".alert")
const todosList = document.querySelector("#todo-list")

async function retrieveFromLocalStorage() {
    // const data = localStorage.getItem("items") 

    // const todos = JSON.parse(data) 
    // for(let todo of todos) {
    //     addNote(todo.text , todo.status)
    // }
    alert.innerText = "Loadind ... "
    const repsonse = await fetch("http://localhost:3000/todos") 

    const data = await repsonse.json() 

      for(let todo of data) {
        addNote(todo.text , todo.status , `note_${todo.id}`)
    }

    alert.innerText = ""

}

retrieveFromLocalStorage()


function storeInLocalStorage() {
    const todos = todosList.children

    const data = [] 
    for (let todo of todos) {

        const testElement = todo.querySelector(".text")
        const value = testElement.innerText 
        const checked = todo.classList.contains("liChecked") 
        data.push({
            text : value , 
            status : checked
        })
    }
    const dataToBeStored = JSON.stringify(data)
    localStorage.setItem("items" , dataToBeStored)
}


function displayAlert(message , className){
    alert.innerText =  message
    alert.classList.add(className)

    setTimeout(()=>{
        alert.innerText = ""
        alert.classList.remove(className)
    } , 2000)

}


form.addEventListener("submit" ,async (e)=>{
    e.preventDefault()

    if (entry.value.trim() == "") {
        displayAlert("Please, add a value" , "alert-danger")
        entry.value = ""

        return 
    }

    const response = await fetch("http://localhost:3000/todos" , {
        method : "POST" , 
        body : JSON.stringify({
            text : entry.value , 
            status : false 
        })
    } )

    const data = await response.json() 

    addNote(data.text , data.status , `note_${data.id}`)
 
    
    displayAlert("Created Successfully" , "alert-success")

   
})


function addNote(text , status , id){
 const li = document.createElement("li")
    // li.className = "list-item"
    li.classList.add("list-item")
    li.id = id
    if (status == true) {
        li.classList.add("liChecked")
    }
    //  <p class="text">Lorem ipsum dolor sit.</p>
    const p = document.createElement("p")
    p.className = "text" 
    p.innerText = text

    // <i class='bx bx-edit '>edit</i>
    const editIcon = document.createElement("i")
    editIcon.className = "bx bx-edit"
    editIcon.innerText = "edit"
    if(status == true) {
        editIcon.classList.add("d-none")

    }

    // <i class='bx bx-check '>check</i>
    const checkIcon = document.createElement("i")
    checkIcon.className = "bx bx-check"
    if(status == true) {
        checkIcon.innerText = "unCheck" 
    }else{
        checkIcon.innerText = "check" 
    }


    checkIcon.addEventListener("click" , async ()=>{

        
        const response = await fetch(`http://localhost:3000/todos/${id.replace("note_" , "")}` , {
            method : "PATCH" ,
            body : JSON.stringify({
                status : ! li.classList.contains("liChecked")
            })
        })
        if (response.ok) {
            const checked = li.classList.toggle("liChecked")
            editIcon.classList.toggle("d-none")
            if (checked){
                checkIcon.innerText = "unCheck"
            }else{
                checkIcon.innerText = "check"
            }
            displayAlert("updated successfully" , "alert-success")
        }else{
            displayAlert("error happen" , 'alert-danger')
        }



        // storeInLocalStorage()

    })

    //<i class='bx bxs-trash '>delete</i>
    const trashIcon = document.createElement("i")
    trashIcon.className = "bx bxs-trash"
    trashIcon.innerText = "delete" 

    trashIcon.addEventListener("click" , async ()=>{

        const repsonse = await fetch(`http://localhost:3000/todos/${id.replace("note_" , "")}` , {
            method:"DELETE"
        })
        if(repsonse.ok) {
            li.remove()
            displayAlert("Deleted Successfully" , "alert-success")
            
        }else{
            console.log(repsonse)
            displayAlert("error happen" , "alert-danger")
        }

        // storeInLocalStorage()
    })

    li.append(p)
    li.append(editIcon)
    li.append(checkIcon)
    li.append(trashIcon)

    todosList.append(li)

    entry.value = ""

    // storeInLocalStorage()
}