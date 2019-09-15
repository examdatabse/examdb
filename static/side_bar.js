//show different option on side bar for different types of user
//0 = student, 1 = TA, 2 = Administer
const account_apps = [[], ["Bulk Upload"], ["Bulk Upload"]];
function side_bar_generator(){
    var account_type = 0;
    try{
        account_type = getCookie("account_type");
        if (account_type === "") throw "No 'account_type' found in cookie."
    } catch (error){
        console.error("Something went wrong when finding 'account_type' in cookie. -> " + error);
    }

    account_type = Number(account_type);/*force it into int*/
    let container = document.getElementsByClassName("side_menu")[0];
    let template = document.getElementById("side_bar_button_template");
    template = template.content.querySelector("button");

    let i;
    for (i in account_apps[account_type]){
        let temp = document.importNode(template, true);
        let Name = account_apps[account_type][i].toLowerCase().replace(" ", "_");
        temp.setAttribute("id", Name.concat("_button"));
        temp.setAttribute("onclick", "request_page('" + Name + "')");
        temp.innerHTML = account_apps[account_type][i];
        container.appendChild(temp);
    }

}

function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

/**
 * This function sends a GET request for a new page. The function also sends
 * the user name along with the get request to double check that the user
 * has the permission to use this function.
 * @param {string} func: The name of the wanted function/request
 */
function request_page(func){
    let url = "/" + func;
    window.location.href = url;
}