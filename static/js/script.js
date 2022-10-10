function checkDate() {
    var x = document.getElementById("dateform").value;
    /* var y = document.getElementById("{{customer.resdate}}").innerHTML; */
    document.getElementById("selectDate").innerHTML = x;
    /* if (x != y) {
        document.getElementById("customer{{customer.id}}").style.display = "none";
    } else {
        document.getElementById("customer{{customer.id}}").style.display = "block";
    } */
}