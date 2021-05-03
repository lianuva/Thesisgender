// get elements + eventlistener
let vButtons = document.getElementsByClassName('game-button');
        
//set vars
numberofclicks =0;
dSum =0;


// Create hidden input (Pressed Buttons)
//let correct        = document.createElement("input");
//correct.type       = 'hidden';
//correct.name       = 'correcttables';
//correct.id         = 'correcttables';
//correct.value      = '3';

//set counter 0

//load excel 

document.addEventListener("DOMContentLoaded", function(debug=true) {
    let body = document.getElementsByClassName("otree-body")[0];
    var correct = document.getElementById("correcttables");

    //Hidden Next Button
    let EndButton               = document.getElementsByClassName('otree-btn-next btn btn-primary')[0];
    EndButton.style.visibility  = 'hidden';

    //create vector

    //write table here 

    //right answer: counter + 1, go to new vector, use write table again

    //save right answer




    var correct = 0;

    for (i = 0; i < vButtons.length; i++) {
        let button = vButtons[i];
        button.addEventListener("click", function(){
            button.style.background='#696969';
            console.log(button.value)
            dSum = + dSum + Number(button.value);
            numberofclicks = numberofclicks +1;
                        
            if (numberofclicks==2){
                if (dSum==10) {
                    correct ++;
                    //document.getElementById("text1").innerHTML = "correct";
                    //document.getElementById("text2").innerHTML = dSum;  
                    document.getElementById("correcttables").value = correct;
                    console.log(document.getElementById("correcttables").value);
                    EndButton.click(); 

                } else {
                    //document.getElementById("text1").innerHTML = "incorrect";
                    //document.getElementById("text2").innerHTML = dSum;  
                    
                    //correct.value = +correct.value + 0;
                    
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
        
        });//end button click function

    } //end forloop

});