function add_question_functions(){
    var new_tag = prompt("Add tag:");
    if (new_tag != null){
        var my_tags = document.getElementById("tags");
        my_tags.innerHTML += new_tag + " ";
    }
}

var choice_conuter = 1
function add_choice() {
    choice_conuter ++;
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
