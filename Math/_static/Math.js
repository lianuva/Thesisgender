       //get elements + eventlistener
       let click1  = document.getElementById('button1').addEventListener("click", buttonfunction);
       let click2  = document.getElementById('button2').addEventListener("click", buttonfunction);
       let click3  = document.getElementById('button3').addEventListener("click", buttonfunction);
       let click4  = document.getElementById('button4').addEventListener("click", buttonfunction);
       let click5  = document.getElementById('button5').addEventListener("click", buttonfunction);
       let click6  = document.getElementById('button6').addEventListener("click", buttonfunction);
       let click7  = document.getElementById('button7').addEventListener("click", buttonfunction);
       let click8  = document.getElementById('button8').addEventListener("click", buttonfunction);
       let click9  = document.getElementById('button9').addEventListener("click", buttonfunction);
       let click10 = document.getElementById('button10').addEventListener("click", buttonfunction);
       let click11 = document.getElementById('button11').addEventListener("click", buttonfunction);
       let click12 = document.getElementById('button12').addEventListener("click", buttonfunction);
       let reset   = document.getElementById('reset').addEventListener("click", resetfunction);

       //set vars
       numberofclicks =0;
       dSum =0;

       function buttonfunction(e){
           if (e.target ==  document.getElementById('button1')){
               document.getElementById("button1").style.background='#696969';
           }
           else if (e.target == document.getElementById('button2')){
               document.getElementById("button2").style.background='#696969';
           }
           else if (e.target == document.getElementById('button3')){
               document.getElementById("button3").style.background='#696969';
           }
           else if (e.target == document.getElementById('button4')){
               document.getElementById("button4").style.background='#696969';
           }
           else if (e.target == document.getElementById('button5')){
               document.getElementById("button5").style.background='#696969';
           }
           else if (e.target == document.getElementById('button6')){
               document.getElementById("button6").style.background='#696969';
           }
           else if (e.target == document.getElementById('button7')){
               document.getElementById("button7").style.background='#696969';
           }
           else if (e.target == document.getElementById('button8')){
               document.getElementById("button8").style.background='#696969';
           }
           else if (e.target == document.getElementById('button9')){
               document.getElementById("button9").style.background='#696969';
           }
           else if (e.target == document.getElementById('button10')){
               document.getElementById("button10").style.background='#696969';
           }
           else if (e.target == document.getElementById('button11')){
               document.getElementById("button11").style.background='#696969';
           }
           else if (e.target == document.getElementById('button12')){
               document.getElementById("button12").style.background='#696969';
           }

           
           dSum = + dSum + Number($(this).val());
           numberofclicks = numberofclicks +1;
           
           
          
           if (numberofclicks==2){
               if (dSum==10) {
               document.getElementById("text").innerHTML = "correct";
               document.getElementById("text").innerHTML = dSum;
               } 
           else {
           document.getElementById("text").innerHTML = "incorrect";
           document.getElementById("text").innerHTML = dSum;
           }
           }
       };

       function resetfunction(){
           dSum = 0;
           numberofclicks = 0;
           document.getElementById("button1").style.background='#E6E6E6';
           document.getElementById("button2").style.background='#E6E6E6';
           document.getElementById("button3").style.background='#E6E6E6';
           document.getElementById("button4").style.background='#E6E6E6';
           document.getElementById("button5").style.background='#E6E6E6';
           document.getElementById("button6").style.background='#E6E6E6';
           document.getElementById("button7").style.background='#E6E6E6';
           document.getElementById("button8").style.background='#E6E6E6';
           document.getElementById("button9").style.background='#E6E6E6';
           document.getElementById("button10").style.background='#E6E6E6';
           document.getElementById("button11").style.background='#E6E6E6';
           document.getElementById("button12").style.background='#E6E6E6';
       }


       