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


    let vWords  = document.getElementById('submitword');
    let button  = document.getElementById('submit1');  
    


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
            if (str1 === str2.trim() && str1.length === str2.trim().length) {
                console.log(str1.length);
                console.log(str2.length);
      
                //get solutions from string 
                points = points_string.split("[")[1].split(" ")[i];
                points1 = points.replace(/['"]+/g,'').replace(',','');  
                console.log(points1);

                score.value = +score.value + Number(points1); 

                //if correct, remove word from string.
                // if(vWords.value.length === str1) {
                //     solution_string = solution_string.replace(vWords.value, " ");
                // }
                

                solution_string = solution_string.replace(vWords.value, " ");


                document.getElementById("text1").innerHTML = score.value;
            } else {
                document.getElementById("text1").innerHTML = score.value;
                score.value = +score.value + 0;
            }
            
        }
        document.getElementById("score").value = score.value;

    });

});
