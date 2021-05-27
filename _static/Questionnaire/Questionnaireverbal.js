//constants
var slider  = document.getElementById("verbalslider");
var output  = document.getElementById("slider_value");
var xValues = ["+100%", "+90%", "+80%", "+70%", "+60%", "+50%", "+40%", "+30%", "+20%", "+10%", "0", "+10%", "+20%", "+30%", "+40%", "+50%", "+60%", "+70%", "+80%", "+90%", "+100%"];
var yValue  = ["0", "1", "2", "3"];

new Chart("myChart", {
        type: "bar",
        data: {
            labels: xValues, yValue,
            datasets: [{
                backgroundColor: "blue",
                data: yValues = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0]
            }]
        },
        options: {
            events: [],
            legend: {display: false},
            title: {
                display: true,
                text: "Payoff"
            },
            scales: {
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Your potential payoff'
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: '< --                                                   Men                                                 -->   Equal   <--                                               Women                                                 -->'
                    }
                }]
            }
        }    
    });





slider.oninput = function() {

    if (this.value == 0) {
        yValues = [3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0];
    } else if (this.value == 1) {
        yValues = [2, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0];
    } else if (this.value == 2) {
        yValues = [1, 2, 3, 2, 1, 0, 0, 0, 0, 0, 0];
    } else if (this.value == 3) {
        yValues = [0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 0];
    } else if (this.value == 4) {
        yValues = [0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0];
    } else if (this.value == 5) {
        yValues = [0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0];
    } else if (this.value == 6) {
        yValues = [0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0];
    } else if (this.value == 7) {
        yValues = [0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0];
    } else if (this.value == 8) {
        yValues = [0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1];
    } else if (this.value == 9) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0];
    } else if (this.value == 10) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0];
    } else if (this.value == 11) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0];
    } else if (this.value == 12) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 0, 0];
    } else if (this.value == 13) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 0];
    } else if (this.value == 14) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0];
    } else if (this.value == 15) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0];
    } else if (this.value == 16) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0];
    } else if (this.value == 17) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0];
    } else if (this.value == 18) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1];
    } else if (this.value == 19) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2];
    } else if (this.value == 20) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3];
    }

    
    var barColors = "blue";

    new Chart("myChart", {
        type: "bar",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: barColors,
                data: yValues
            }]
        },
        options: {
            events: [],
            legend: {display: false},
            title: {
                display: true,
                text: "Payoff"
            },
            scales: {
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Your potential payoff'
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: '< --                                                   Men                                                 -->   Equal   <--                                               Women                                                 -->'
                    }
                }]
            }
        }    
    });


    if (this.value < 10) {
        document.getElementById("text1").innerHTML = "I expect men to perform " + (10 -this.value) + "0% better than women";
    } else if (this.value > 10) {
        document.getElementById("text1").innerHTML = "I expect women to perform " + (this.value -10) + "0% better than men";
    } else if (this.value = 10) {
        document.getElementById("text1").innerHTML = "I expect men and women to perform equally well";
    }
    

}
