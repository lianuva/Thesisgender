//constants
const OtreeBody         = document.getElementsByClassName("otree-body")[0];
let body                = document.createElement('div');
let solution_string     = js_vars.solution_string;
let points_string       = js_vars.points_string;
let scoreverbal         = document.getElementById("score");
let numberofsolutions   = js_vars.numberofsolutions;
let score               = 0;
let j                   = 0;

//show otree timer lasy 10 sec
$(function () {
    $('.otree-timer__time-left').on('update.countdown', function (event) {
        if (event.offset.totalSeconds === 10) {
            $('.otree-timer').show();
        }
    });
});

document.addEventListener("DOMContentLoaded", function(debug=true) {  
    OtreeBody.appendChild(body);
    //body.appendChild(score);
    
    console.log("input inserted");


    let vWords  = document.getElementById('submitword');
    let button  = document.getElementById('submit1');  

    //when enter pressed, press submit button
    window.addEventListener("keydown", function (event) {
        if (event.defaultPrevented) {
          return; // Do nothing if the event was already processed
        }
        switch (event.key) { 
          case "Enter":
            button.click();
            break;
          default:
            return; // Quit when this doesn't handle the key event.
        }
        // Cancel the default action to avoid it being handled twice
        event.preventDefault();
    }, true);
    
    button.addEventListener("click", function func(){
    
        word = document.createElement("p");
        word.innerHTML = vWords.value;
        document.getElementById("answers").appendChild(word);
        
        for (i = 0; i < numberofsolutions; i++) { 
          
            //get solutions from string
            solution = solution_string.split("[")[1].split(" ")[i];
            
            //compare string to input
            str1= solution.replace(/['"]+/g,'').replace(',','');
            str2= vWords.value.toLowerCase();
            // var n = str1.localeCompare(str2);

            //add score if a correct word is entered
            if (str1 === str2.trim()) {
      
                //get solutions from string 
                points = points_string.split("[")[1].split(" ")[i];
                points1 = points.replace(/['"]+/g,'').replace(',','');  
              

                score = +score + Number(points1); 

                //if correct, remove word from string.
                solution_string = solution_string.replace(solution, " ");

                document.getElementById("text1").innerHTML = score;

                //save score
                document.getElementById("score").value = score;

                console.log(score);

            } else {
                document.getElementById("text1").innerHTML = score;
                score = +score + 0;
            }
            
        }
       
        //clear value inside inputbox
        document.getElementById('submitword').value = ''
        
    });


});
