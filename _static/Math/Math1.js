//get elements + eventlistener
let vButtons = document.getElementsByClassName('game-button');
        
//set vars
numberofclicks =0;
dSum =0;

// Create hidden input (Pressed Buttons)
let correct        = document.createElement("input");
correct.type       = 'hidden';
correct.name       = 'correct';
correct.id         = 'correct';
correct.value      = '';

document.addEventListener("DOMContentLoaded", function(debug=true) {
    let body=document.getElementsByClassName("otree-body")[0];
    body.appendChild(correct);
    //console.log("input inserted");
});

for (i = 0; i < vButtons.length; i++) {
    let button = vButtons[i];
    button.addEventListener("click", function(){
        button.style.background='#696969';
        console.log(button.value)
        dSum = + dSum + Number(button.value);
        numberofclicks = numberofclicks +1;
        
        
        if (numberofclicks==2){
            if (dSum==10) {
                if (correct.value == ""){
                    correct.value = 1;
                } else {
                    correct.value = +correct.value + 1;
                }  
                document.getElementById("text1").innerHTML = "correct";
                document.getElementById("text2").innerHTML = dSum;  
                document.getElementsByClassName("otree-btn-next")[0].click(); 

            } else {
                document.getElementById("text1").innerHTML = "incorrect";
                document.getElementById("text2").innerHTML = dSum;    
                let x = document.getElementsByClassName("game-button");
                    for (j = 0; j < x.length; j++) {
                        x[j].style.background = "rgb(230, 230, 230)";
                    }
                numberofclicks = 0;
                dSum = 0;
            }                   
        } 
            
        console.log(correct.value);
        return correct
    });
}
