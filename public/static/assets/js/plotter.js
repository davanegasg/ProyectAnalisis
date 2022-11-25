function plot(f_id, taget_graph) {
    var f = document.querySelector(f_id).value;
    var xMin = document.querySelector("#xMin").value;
    var xMax = document.querySelector("#xMax").value;
    var yMin = document.querySelector("#yMin").value;
    var yMax = document.querySelector("#yMax").value;
    
    functionPlot({
        target: taget_graph,
        data: [{
            fn: f,
        }],
        grid: true,
        yAxis: {
            domain: [yMin, yMax]
        },
        xAxis: {
            domain: [xMin, xMax]
        }
    }); 
}