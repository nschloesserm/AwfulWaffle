function checkDate() {
    var x = document.getElementById("dateform").value;
    var y = [...document.querySelectorAll("h6")].map(e=>e.innerHTML);
    document.getElementById("selectDate").innerHTML = x + y;
    var arrayLength = y.length
    for (var h = 0; h < arrayLength; h++) {
        
    }
    for (var i = 0; i < arrayLength; i++) {
        if (x != y[i]) {
            document.getElementsByClassName(y[i]).style.display = "none";
        } else {
            document.getElementsByClassName(y[i]).style.display = "block";
        }
    }
}