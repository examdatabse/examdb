function Collapse(ID) {
    var dots = document.getElementById("dots_" + ID);
    var moreText = document.getElementById("more_" + ID);
    var btnText = document.getElementById("button_" + ID);

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "Read more";
        moreText.style.display = "none";
    } else {
        dots.style.display = "none";
        btnText.innerHTML = "Read less";
        moreText.style.display = "inline";
    }
}

var search_results = JSON.parse(document.getElementById("search_results_container").dataset.geocode);
if (search_results.length == 0){
    // do nothing
}
else if(search_results > 10){
    console.error("result data longer than ten questions.")
}
else{
    var i = 0;
    while(i < search_results.length && i < 10){
        var new_quesion = document.getElementById("questino_display_template").content.cloneNode(true);
        
    }
}
