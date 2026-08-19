function addNotes(){

  const entry = document.querySelector("#entry")
  const form = document.querySelector("form")
  const alertBox = document.querySelector(".alert")
  const todoList = document.querySelector("#todo-list")

  const alert = (message , type)=>{
    alertBox.innerText = message
    alertBox.classList.remove("alert-danger" , "alert-success")
    if (type === "danger"){
      alertBox.classList.add("alert-danger")
    }else{
      alertBox.classList.add("alert-success")
    }
    setTimeout(()=>{
      alertBox.innerText = ""
      alertBox.classList.remove("alert-danger" , "alert-success")
    } , 2000)
  }

  form.addEventListener("submit" , (e)=>{
    e.preventDefault()

    if (entry.value.trim() == ""){
      alert("please add a value" , "danger")
      entry.value = ""
      return
    }

    const li = document.createElement("li")
    li.classList.add("list-item")

    const p = document.createElement("p")
    p.classList.add("text")
    p.innerText = entry.value

    const editIcon = document.createElement("i")
    editIcon.className = "bx bx-edit"
    editIcon.innerText = "edit"

    const checkIcon = document.createElement("i")
    checkIcon.className ="bx bx-check"
    checkIcon.innerText = "check"

    const trashIcon = document.createElement("i")
    trashIcon.className = "bx bx-trash"
    trashIcon.innerText = "delete"

    li.append(p)
    li.append(editIcon)
    li.append(checkIcon)
    li.append(trashIcon)

    todoList.append(li)
    entry.value = ""

    alert("Created Successfully" , "success")
  })

  todoList.addEventListener("click" , (e)=>{
    const target = e.target
    const li = target.closest("li")
    if (!li) return

    if (target.classList.contains("bx-edit")){
      const textEl = li.querySelector(".text")
      const newValue = prompt("edit note" , textEl.innerText || "")
      if (newValue !== null){
        if (newValue.trim() == ""){
          alert("empty value not allowed" , "danger")
        }else{
          textEl.innerText = newValue
          alert("Updated Successfully" , "success")
        }
      }
    }

    if (target.classList.contains("bx-check") || target.classList.contains("bx-undo")){
      const textEl = li.querySelector(".text")

      if (target.classList.contains("bx-check")){
        textEl.style.textDecoration = "line-through"
        li.classList.add("completed")
        target.classList.remove("bx-check")
        target.classList.add("bx-undo")
        target.innerText = "uncheck"
        alert("Marked as done" , "success")
      }else{
        textEl.style.textDecoration = "none"
        li.classList.remove("completed")
        target.classList.remove("bx-undo")
        target.classList.add("bx-check")
        target.innerText = "check"
        alert("Marked as undone" , "success")
      }
    }

    if (target.classList.contains("bx-trash")){
      li.remove()
      alert("Deleted Successfully" , "success")
    }
  })

}

addNotes()
