var slider = document.getElementById("myRange")
var output = document.getElementById("demo")

output.innerHTML = slider.nodeValue;

slider.oninput() = function(){
    output.innerHTML = this.value;
}

