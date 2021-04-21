//get elements

var click1 = document.getElementById("button1");
var click2 = document.getElementById("button2");
var click3 = document.getElementById("button3");

//eventlistener
click1.addEventListener("click", buttonfunction, false);
click2.addEventListener("click", buttonfunction, false);
click3.addEventListener("click", buttonfunction, false);

//set vars
//numberofclicks =0;
//dSum =0;

function buttonfunction(){
    //numberofclicks = numberofclicks +1;
    //dSum = + dSum + button2.value + button1.value;
    alert('hello');
}

