function checkDate() {
    var x = document.getElementById("dateform").value;
    var y = [...document.querySelectorAll("h6")].map(e=>e.innerHTML);
    document.getElementById("selectDate").innerHTML = x + y;
    var arrayLength = y.length
    for (var i = 0; i < arrayLength; i++) {
        if (x != y[i]) {
            document.getElementById("cust" + (i + 1)).style.display = "none";
        } else {
            document.getElementById("cust" + (i + 1)).style.display = "block";
        }  
        console.log("cust" + (i + 1));
        console.log(y[i]);
            }
}

function changeID() {
    var y = [...document.querySelectorAll("h6")].map(e=>e.innerHTML);
    var arrayLength = y.length
    for (var j = 0; j < arrayLength; j++) {
        if (element = document.getElementById("customersection")) {
            element.id = "cust" + (j + 1); 
        } 
    }   
  }
  
  let element = document.getElementById("customersection");
  changeID();
  



