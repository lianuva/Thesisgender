//constants
const OtreeBody         = document.getElementsByClassName("otree-body")[0];
let body                = document.createElement('div');
let round_number        = js_vars.round_number;
let contents            = js_vars.contents; //!
let score               = 0;
let wordcounter         = 0;
let rownumber           = 0;

if (round_number == 1) {
    var solution_string     = js_vars.solution_string;
    var points_string       = js_vars.points_string;
    var numberofsolutions   = js_vars.numberofsolutions;
} else if (round_number ==2) {
    var solution_string     = js_vars.solution_string2;
    var points_string       = js_vars.points_string2;
    var numberofsolutions   = js_vars.numberofsolutions2;
}

//predetermine score =0
document.getElementById("score").value = 0;
console.log(document.getElementById("score").value);

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
    
    //if button is clicked, the following happens:
    button.addEventListener("click", function func(){

        //words are displayed intro rows.
        var z = document.createElement("TD");
        var t = document.createTextNode(vWords.value);
        z.appendChild(t);
        document.getElementById("myTr" + rownumber).appendChild(z); //put td into row
       
        if (vWords.value == " ") {
            wordcounter == wordcounter;
        }  else {    
        wordcounter ++;  
        }    

        // if 5 words are entered, a new row is created
        remainder = (wordcounter % 5);
        if (remainder == 0) {
            rownumber ++;     
            var y = document.createElement("TR" + rownumber);
            y.setAttribute("id", "myTr" + rownumber);
            document.getElementById("myTable").appendChild(y); //print row to table
            br = document.createElement("br");
            document.getElementById("myTable").appendChild(br);
        } 

        //check if word entered is correct
        for (i = 0; i < numberofsolutions; i++) { 
          
            //get solutions from string
            solution = solution_string.split("[")[1].split(" ")[i];
            
            //compare string to input
            str1= solution.replace(/['"]+/g,'').replace(',','');
            str2= vWords.value.toLowerCase();
            // var n = str1.localeCompare(str2);

            //add score if a correct word is entered (trim=without spaces)
            if (str1 === str2.trim()) {
      
                //get solutions from string 
                points = points_string.split("[")[1].split(" ")[i];
                points1 = points.replace(/['"]+/g,'').replace(',','');  
            
                score = +score + Number(points1); 

                //if correct, remove word from string.
                solution_string = solution_string.replace(solution, " ");

                //save score
                document.getElementById("score").value = score;
               
                console.log(score);

            } else {
                score = +score + 0;
            }
            
        }
       
        //clear value inside inputbox
        document.getElementById('submitword').value = ''
        
    });


});
