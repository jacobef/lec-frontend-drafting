const navbar = document.getElementById("nav")
const switch_perm = document.getElementById('switch-perm')
const notif_btn = document.getElementById("notif-btn");
const notif_body = document.getElementById("notif-body")
let admin_items = navbar.getElementsByClassName("admin-item")
let parent_items = navbar.getElementsByClassName("parent-item")
let is_parent = false
let parent_class;
let admin_class;

switch_perm.addEventListener("click", changeUserType)
notif_btn.addEventListener("click", showNotifs)

changeUserType()

function changeUserType(){
    is_parent = !is_parent;

    if (is_parent == true){
        parent_class = "active"
        admin_class = "inactive"
    }
    if (is_parent == false)
    {
        parent_class = "inactive"
        admin_class = "active"        
    }

    // For parents
    for (let i = 0; i < parent_items.length; i++){
        parent_items[i].classList.add(parent_class);
        parent_items[i].classList.remove(admin_class);
    }

    // For admin
    for (let i = 0; i < admin_items.length; i++){
        admin_items[i].classList.add(admin_class);
        admin_items[i].classList.remove(parent_class);
    }
}

function showNotifs(){
    notif_body.classList.toggle("inactive")
}