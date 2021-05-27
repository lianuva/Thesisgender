//set vectors
// let numbers = js_vars.sorted_string;
let vButtons        = document.getElementsByClassName('game-button');    

//set constants
let practicecorrect = document.getElementById("correcttables");
let numberofclicks  = 0;
let dSum            = 0;
var round           = 0;

document.addEventListener("DOMContentLoaded", function(debug=true) {   
    //define variables
    let body = document.getElementsByClassName("otree-body")[0];
    
    //Hidden Next Button
    let EndButton               = document.getElementsByClassName('otree-btn-next btn btn-primary')[0];
    EndButton.style.visibility  = 'hidden';   

    for (i = 0; i < vButtons.length; i++) {
        let button = vButtons[i];

        //define what happens when button is clicked
        button.addEventListener("click", function buttonfunction(){
            button.style.background='#696969';
            dSum = + dSum + Number(button.value);
            numberofclicks = numberofclicks +1;

            //if 2 numbers are clicked, check if they sum to 10
            if (numberofclicks==2){
                if (dSum==10) {
                    
                    //if numbers sum to 10, correct =1 and round +1
                    if (practicecorrect ="") {
                        practicecorrect = +1;
                        
                    } else{
                    practicecorrect ++;
                    round ++;
                    }

                    //give feedback
                    document.getElementById("text1").innerHTML = "That is correct! Please click the button below to start the real task:";

                    //show button
                    // Endbutton.show();
                    EndButton.style.visibility  = 'visible';  

                    //save number of correct tables
                    document.getElementById("correcttablespractice").value = round;
                    
                    //set numbers to 0 and continue to next round
                    numberofclicks = 0;
                    dSum = 0;

                    // } 
                    
                } else {
                    document.getElementById("text1").innerHTML = "That is incorrect. The sum is " + dSum.toFixed(2) + " and should be 10. Please try again";

                    
                    //if numbers do not sum to 10, reset colors and start again                    
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


    var os1 = document.getElementById("os1").value;

    document.getElementById("os1").value = "unknown";

    function getOS() {
        var userAgent = window.navigator.userAgent,
            platform = window.navigator.platform,
            macosPlatforms = ["Macintosh", "MacIntel", "MacPPC", "Mac68K"],
            windowsPlatforms = ["Win32", "Win64", "Windows", "WinCE"],
            iosPlatforms = ["iPhone", "iPad", "iPod"],
            os1 = null;

        if (macosPlatforms.indexOf(platform) !== -1) {
        os1 = 'Mac OS';
        } else if (iosPlatforms.indexOf(platform) !== -1) {
        os1 = 'iOS';
        } else if (windowsPlatforms.indexOf(platform) !== -1) {
        os1 = 'Windows';
        } else if (/Android/.test(userAgent)) {
        os1 = 'Android';
        } else if (!os && /Linux/.test(platform)) {
        os1 = 'Linux';
        } 
        return os1;
    }

    // os1 = getOS();
    document.getElementById("os1").value = getOS();

});