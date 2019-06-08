var tages_counter = 0
var choice_conuter = 1


function add_tage() {
    var new_tag = prompt("Add tag:");
    if ('content' in document.createElement('template')) {
        var TagesList = document.getElementById("tagsList");
        var temp = document.getElementById("tag_template").content.cloneNode(true);
        temp.querySelector("span").innerHTML = new_tag;
        temp.querySelector("textarea").value = new_tag;
        temp.querySelector("li").setAttribute("id", "tag_" + tages_counter.toString(16));
        temp.querySelector("button").setAttribute("onclick", "deleteTages('tag_" + tages_counter.toString(16) + "')")
        TagesList.appendChild(temp);
        tages_counter++;
    } else {
        // Templates are not supported.
        console.log("Templates are not supported");
    }
}

function deleteTages(tag_id) {
    target_tag = document.getElementById(tag_id);
    target_tag.parentNode.removeChild(target_tag);
}

function add_choice() {
    choice_conuter++;
    var my_choices = document.getElementById("choices");
    var new_choice_labl = String.fromCharCode(64 + choice_conuter);
    console.log(document.getElementsByClassName("choices").length);//debug
    //new choice container
    var new_choice_div = document.createElement("div");
    new_choice_div.setAttribute("class", "each_choice");
    new_choice_div.setAttribute("id", "choice_" + new_choice_labl);
    //textarea element
    var new_choice_textarea = document.createElement("textarea");
    new_choice_textarea.setAttribute("name", "choice");
    new_choice_textarea.setAttribute("form", "question_form");
    //file upload element
    var new_choice_input = document.createElement("input");
    new_choice_input.setAttribute("type", "file");
    new_choice_input.setAttribute("name", "choice_image");
    new_choice_input.setAttribute("form", "question_form");
    //set up
    new_choice_div.innerHTML = new_choice_labl + ": ";
    new_choice_div.appendChild(new_choice_textarea);
    new_choice_div.innerHTML += "Upload Image: ";
    new_choice_div.appendChild(new_choice_input);
    my_choices.appendChild(new_choice_div);
}



