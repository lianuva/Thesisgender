//constants
const OtreeBody         = document.getElementsByClassName("otree-body")[0];
let body                = document.createElement('div');
let solution_string     = js_vars.solution_string;
let points_string       = js_vars.points_string;
let score               = document.getElementById("score");
let numberofsolutions   = js_vars.numberofsolutions;

document.addEventListener("DOMContentLoaded", function(debug=true) {
    //!if enter pressed, form submitted.
    
    // document.addEventListener("keyup", function(event) {
    //     if (event.keyCode === 13) {
    //         alert('Enter is pressed!');
    //     }
    // });    
    
    OtreeBody.appendChild(body);
    body.appendChild(score);
    console.log("input inserted");


    let vWords  = document.getElementById('submitword').trim();
    let button  = document.getElementById('submit1');  
    
    console.log(vWords);


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
            var n = str1.localeCompare(str2);

            //add score if a correct word is entered
            if (n == 0) {
      
                //get solutions from string 
                points = points_string.split("[")[1].split(" ")[i];
                points1 = points.replace(/['"]+/g,'').replace(',','');  

                score.value = +score.value + Number(points1); 
                
                //if correct, remove word from string.
                solution_string = solution_string.replace(vWords.value, "");

                document.getElementById("text1").innerHTML = score.value;
            } else {
                document.getElementById("text1").innerHTML = score.value;
                score.value = +score.value + 0;
            }
            
        }

       

        console.log(score.value); 
        document.getElementById("score").value = score.value;

    });

});
