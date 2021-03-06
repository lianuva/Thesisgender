//set vectors and constants
let numbers         = js_vars.sorted_string;
let vButtons        = document.getElementsByClassName('game-button');    
let round_number    = js_vars.round_number;
let numberofclicks  = 0;
let dSum            = 0;

if (round_number == 1) {
    var round   = 0;
    //if 0 matrices solved; score =0
    document.getElementById("correcttables").value = 0;
} else if (round_number == 2) {
    var round   = 15;
    document.getElementById("correcttables2").value = 0;
}

//show otree timer lasy 10 sec
$(function () {
    $('.otree-timer__time-left').on('update.countdown', function (event) {
        if (event.offset.totalSeconds === 10) {
            $('.otree-timer').show();
        }
    });
});

document.addEventListener("DOMContentLoaded", function(debug=true) {
    //define variables
    let body = document.getElementsByClassName("otree-body")[0];

    //Hidden Next Button
    let EndButton               = document.getElementsByClassName('otree-btn-next btn btn-primary')[0];
    EndButton.style.visibility  = 'hidden';   

    for (i = 0; i < vButtons.length; i++) {
        let button = vButtons[i];
     
        //set first round
        if (round_number == 1) {
            n1 = numbers.split("[")[1].split(",")[0];
            n2 = numbers.split("[")[2].split(",")[0];
            n3 = numbers.split("[")[3].split(",")[0];
            n4 = numbers.split("[")[4].split(",")[0];
            n5 = numbers.split("[")[5].split(",")[0];
            n6 = numbers.split("[")[6].split(",")[0];
            n7 = numbers.split("[")[7].split(",")[0];
            n8 = numbers.split("[")[8].split(",")[0];
            n9 = numbers.split("[")[9].split(",")[0];
            n10 = numbers.split("[")[10].split(",")[0];
            n11 = numbers.split("[")[11].split(",")[0];
            n12 = numbers.split("[")[12].split(",")[0];
        }  else if (round_number == 2) {
            n1 = numbers.split("[")[1].split(",")[15];
            n2 = numbers.split("[")[2].split(",")[15];
            n3 = numbers.split("[")[3].split(",")[15];
            n4 = numbers.split("[")[4].split(",")[15];
            n5 = numbers.split("[")[5].split(",")[15];
            n6 = numbers.split("[")[6].split(",")[15];
            n7 = numbers.split("[")[7].split(",")[15];
            n8 = numbers.split("[")[8].split(",")[15];
            n9 = numbers.split("[")[9].split(",")[15];
            n10 = numbers.split("[")[10].split(",")[15];
            n11 = numbers.split("[")[11].split(",")[15];
            n12 = numbers.split("[")[12].split(",")[15];
        } 

        //read values to table
        document.getElementById("button1").textContent = n1;
        document.getElementById("button2").textContent = n2;
        document.getElementById("button3").textContent = n3;
        document.getElementById("button4").textContent = n4;
        document.getElementById("button5").textContent = n5;
        document.getElementById("button6").textContent = n6;
        document.getElementById("button7").textContent = n7;
        document.getElementById("button8").textContent = n8;
        document.getElementById("button9").textContent = n9;
        document.getElementById("button10").textContent = n10;
        document.getElementById("button11").textContent = n11;
        document.getElementById("button12").textContent = n12;

        document.getElementById("button1").value = n1;
        document.getElementById("button2").value = n2;
        document.getElementById("button3").value = n3;
        document.getElementById("button4").value = n4;
        document.getElementById("button5").value = n5;
        document.getElementById("button6").value = n6;
        document.getElementById("button7").value = n7;
        document.getElementById("button8").value = n8;
        document.getElementById("button9").value = n9;
        document.getElementById("button10").value = n10;
        document.getElementById("button11").value = n11;
        document.getElementById("button12").value = n12;

        //define what happens when button is clicked
        button.addEventListener("click", function buttonfunction(){
            button.style.background='#696969';
            dSum = + dSum + Number(button.value);
            numberofclicks = numberofclicks +1;
            
            // liveSend({
            //     matrixround: round,
            // })

            //if 2 numbers are clicked, check if they sum to 10
            if (numberofclicks==2){
                if (dSum==10) {

                    //if numbers sum to 10, round +1
                    round ++;
                                             
                    //define table again
                    n1 = numbers.split("[")[1].split(",")[round]
                    n2 = numbers.split("[")[2].split(",")[round]
                    n3 = numbers.split("[")[3].split(",")[round]
                    n4 = numbers.split("[")[4].split(",")[round]
                    n5 = numbers.split("[")[5].split(",")[round]
                    n6 = numbers.split("[")[6].split(",")[round]
                    n7 = numbers.split("[")[7].split(",")[round]
                    n8 = numbers.split("[")[8].split(",")[round]
                    n9 = numbers.split("[")[9].split(",")[round]
                    n10 = numbers.split("[")[10].split(",")[round]
                    n11 = numbers.split("[")[11].split(",")[round]
                    n12 = numbers.split("[")[12].split(",")[round]
                        
                    document.getElementById("button1").textContent = n1;
                    document.getElementById("button2").textContent = n2;
                    document.getElementById("button3").textContent = n3;
                    document.getElementById("button4").textContent = n4;
                    document.getElementById("button5").textContent = n5;
                    document.getElementById("button6").textContent = n6;
                    document.getElementById("button7").textContent = n7;
                    document.getElementById("button8").textContent = n8;
                    document.getElementById("button9").textContent = n9;
                    document.getElementById("button10").textContent = n10;
                    document.getElementById("button11").textContent = n11;
                    document.getElementById("button12").textContent = n12;

                    document.getElementById("button1").value = n1;
                    document.getElementById("button2").value = n2;
                    document.getElementById("button3").value = n3;
                    document.getElementById("button4").value = n4;
                    document.getElementById("button5").value = n5;
                    document.getElementById("button6").value = n6;
                    document.getElementById("button7").value = n7;
                    document.getElementById("button8").value = n8;
                    document.getElementById("button9").value = n9;
                    document.getElementById("button10").value = n10;
                    document.getElementById("button11").value = n11;
                    document.getElementById("button12").value = n12;

                    //reset the button colors 
                    let x = document.getElementsByClassName("game-button");
                    for (j = 0; j < x.length; j++) {
                        x[j].style.background = "rgb(239, 239, 239)";
                    }

                    //save number of correct tables
                    if (round_number ==1){
                        document.getElementById("correcttables").value = round;
                    } else if (round_number ==2){
                        document.getElementById("correcttables2").value = (round-15);
                    }

                    // if (round_number ==1){
                    //     Matrix.create(player=player, document.getElementById("correcttables").value=round);
                    // } else if (round_number ==2){
                    //     Matrix.create(player=player, document.getElementById("correcttables").value=round);
                    // }
                    
                    //set numbers to 0 and continue to next round
                    numberofclicks = 0;
                    dSum = 0;

                    //if max rounds reached, continue to next page
                    if (round_number ==1 && round ==15) {
                        document.getElementsByClassName('otree-btn-next btn btn-primary')[0].click();
                    } else if (round_number ==2 && round ==30){
                        document.getElementsByClassName('otree-btn-next btn btn-primary')[0].click();
                    }
                    
                } else {
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

});