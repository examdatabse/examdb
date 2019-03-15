function add_question_functions(){
    var new_tag = prompt("Add tag:");
    if (new_tag != null){
        var my_tags = document.getElementById("tags");
        my_tags.innerHTML += new_tag + " ";
    }
}

function add_choice() {
    var my_choices = document.getElementById("choices");
    var new_choice_labl = String.fromCharCode(65 + document.getElementsByClassName("choices").length);
    console.log(document.getElementsByClassName("choices").length);//debug
    //new choice container
    var new_choice_div = document.createElement("div");
    new_choice_div.setAttribute("class", "each_choice");
    //textarea element
    var new_choice_textarea = document.createElement("textarea");
    new_choice_textarea.setAttribute("name", "choice");
    new_choice_textarea.setAttribute("form", "question_form");
    new_choice_textarea.setAttribute("id", "choice_" + new_choice_labl);
    //input element
    var new_choice_input = document.createElement("input");
    new_choice_input.setAttribute("type", "file");
    new_choice_input.setAttribute("name", "choice_image");
    //set up
    new_choice_div.innerHTML = new_choice_labl + ": ";
    new_choice_div.appendChild(new_choice_textarea);
    new_choice_div.innerHTML += "Upload Image: ";
    new_choice_div.appendChild(new_choice_input);
    my_choices.appendChild(new_choice_div);
}
