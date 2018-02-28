// function callAjax(url, callback)
// {
//     var xmlhttp;
//    // compatible with IE7+, Firefox, Chrome, Opera, Safari
//     xmlhttp = new XMLHttpRequest();
//     xmlhttp.onreadystatechange = function()
//     {
//         if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
//         {
//             callback(xmlhttp.responseText);
//         }
//     }
//     xmlhttp.open("GET", url, true);
//     xmlhttp.send();
// }
var margin = {
    top: 0.1 * window.innerWidth,
    right: 0.1 * window.innerWidth,
    bottom: 0.1 * window.innerWidth,
    left: 0.1 * window.innerWidth
}

var w = window.innerWidth - margin.right - margin.left;

var h = window.innerHeight - margin.bottom - margin.top;

// Set the ranges of axes
var x = d3.time.scale().range([0, w]);
var y = d3.scale.linear().range([h, 0]);

//Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom")

var yAxis = d3.svg.axis().scale(y)
    .orient("left")

//Parse the date / time 

var parseDate = d3.time.format("%Y-%m-%d %H:%M:%S").parse;


var svg = d3.select("body")
    .append("svg")
    .attr("width", w + margin.left + margin.right)
    .attr("height", h + margin.bottom + margin.top)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + (margin.top) + ")");


// Define the line
var valueline = d3.svg.line()
    .x(function (d) {
        return x(d.timestamp);
    })
    .y(function (d) {
        return y(d.reading);
    });


var drawChart = function (csvFile) {
    d3.csv(csvFile, function (d) {
            return {
                timestamp: parseDate(d.Timestamp),
                reading: parseFloat(d.Reading)
            };
        },
        function (error, data) {
            // data.forEach(function(d){
            //     d.Timestamp = parseDate(d.Timestamp);
            //     d.reading = parseFloat(d.Reading);
            // });
            // Scale the range of the data
            console.log(data);
            x.domain(d3.extent(data, function (d) {
                return d.timestamp;
            }));
            y.domain([0, d3.max(data, function (d) {
                return d.reading;
            })]);

            // Add the valueline path.
            svg.append("path")
                .attr("class", "line")
                .attr("d", valueline(data));

            // Add the X Axis
            svg.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + h + ")")
                .call(xAxis);

            // Add the Y Axis
            svg.append("g")
                .attr("class", "y axis")
                .call(yAxis);



        })

};

// drawChart("INC-17.csv");

d3.select("#data-picker").on("change", function on_change() {
    var val_string = this.value + ".csv";
    svg.selectAll("*").remove();
    drawChart(val_string);
});

d3.select("#button_download").on("click", function on_click() {
    var val_string = $("#data-picker").val() + ".csv";
    console.log(val_string)
    window.open(val_string);
});