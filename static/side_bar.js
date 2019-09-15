//show different option on side bar for different types of user
//0 = student, 1 = TA, 2 = Administer
const account_apps = [[], ["Bulk Upload", "Add Question"], ["Bulk Upload",
    "Add Question"]];
function side_bar_generator(type_int){
    let container = document.getElementsByClassName("side_menu")[0];
    let template = document.getElementById("side_bar_button_template");
    template = template.content.querySelector("button");
    if (type_int == -1 ){
        console.error("account permission type undefined");
    }
    else{
        let i;
        for (i in account_apps[type_int]){
            let temp = document.importNode(template, true);
            let Name = account_apps[type_int][i].toLowerCase().replace(" ", "_");
            temp.setAttribute("id", Name.concat("_button"));
            temp.setAttribute("onclick", "request_page('" + Name + "')");
            temp.innerHTML = account_apps[type_int][i];
            container.appendChild(temp);
        }
    }
}

/**
 * This function sends a GET request for a new page. The function also sends
 * the user name along with the get request to double check that the user
 * has the permission to use this function.
 * @param {string} func: The name of the wanted function/request
 */
function request_page(func){
    /*
    if (user_name === "undefined"){
        console.error("user_name is undefined");
    }
    else{
        var xhttp = new XMLHttpRequest();
        let url = "/" + func + "?user_name=" + user_name;
        xhttp.open("GET", url, true);
        xhttp.send();
    }
    */
    let url = "/" + func;
    window.location.href = url;

}