//get elements + eventlistener
let vButtons = document.getElementsByClassName('game-button');
                
//set vars
numberofclicks =0;
dSum =0;

//Hidden Next Button
//let EndButton               = document.createElement('button');
//EndButton.style.visibility  = 'hidden';
//EndButton.className         = 'otree-btn-next btn btn-primary';

// Create hidden input (Pressed Buttons)
let correct        = document.createElement("input");
correct.type       = 'hidden';
correct.name       = 'correct';
correct.id         = 'correct';
correct.value      = '';

document.addEventListener("DOMContentLoaded", function(debug=true) {
    let body=document.getElementsByClassName("otree-body")[0];
    body.appendChild(correct);
    body.append(EndButton);
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
                document.getElementsByClassName("otree-btn-next btn btn-primary")[0].click(); 

            } else {
                document.getElementById("text1").innerHTML = "incorrect";
                document.getElementById("text2").innerHTML = dSum;  
                
                setTimeout(function(){
                let x = document.getElementsByClassName("game-button");
                    for (j = 0; j < x.length; j++) {
                        x[j].style.background = "rgb(239, 239, 239)";
                    }
                },200);
                numberofclicks = 0;
                dSum = 0;
            }                   
        } 
            
        console.log(correct.value);
        return correct

    });//end button click function

}//end forloop
