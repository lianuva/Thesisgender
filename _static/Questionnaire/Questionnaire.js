//constants
var slider  = document.getElementById("mathslider");
var output  = document.getElementById("slider_value");
var xValues = ["+5", "+4", "+3", "+2", "+1", "0", "+1", "+2", "+3", "+4", "+5"];
var yValue  = ["0", "1", "2", "3"];

new Chart("myChart", {
        type: "bar",
        data: {
            labels: xValues, yValue,
            datasets: [{
                backgroundColor: "blue",
                data: yValues = [0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0]
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
                        labelString: '< --                           Men                             -->    Equal     <--                         Women                        -->'
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
        yValues = [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2];
    } else if (this.value == 10) {
        yValues = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3];
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
                        labelString: '< --                           Men                             -->    Equal     <--                         Women                        -->'
                    }
                }]
            }
        }    
    });

}
