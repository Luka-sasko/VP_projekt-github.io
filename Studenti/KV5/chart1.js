var students_data1;

function updateChart1() {
    var selectedRegion = d3.select("#region1").property("value");
    var sortOrder = d3.select("#sort-order1").property("value");
    var topN = parseInt(d3.select("#top-n1").property("value"));
    var minStudents = parseInt(d3.select("#min-students1").property("value"));

    var filteredData = students_data1.filter(function(d) {
        return (selectedRegion === "all" || d.region === selectedRegion) &&
               d.number_of_students >= minStudents;
    });

    if (sortOrder === "asc") {
        filteredData.sort((a, b) => a.number_of_students - b.number_of_students);
    } else {
        filteredData.sort((a, b) => b.number_of_students - a.number_of_students);
    }

    // Take only top N items
    filteredData = filteredData.slice(0, topN);

    createChart1(filteredData);
}



function initializeFirstChart() {
    d3.json("modifiedData.json").then(function (data) {
        students_data1 = data;
        populateRegionDropdown(data, "#region1");
        createChart1(students_data1);

        d3.selectAll("input").on("input", function () {
            updateChart1();
        });

        d3.selectAll("select").on("change", function () {
            updateChart1();
        });
    }).catch(function (error) {
        console.log("Greška pri učitavanju JSON file-a:", error);
    });
}

function populateRegionDropdown(data, dropdownId) {
    var regions = Array.from(new Set(data.map(d => d.region)));
    var regionSelect = d3.select(dropdownId);
    regionSelect.selectAll("option").remove(); 
    regions.forEach(region => {
        regionSelect.append("option").text(region).attr("value", region);
    });
}

function createChart1(data) {
    d3.select("#chart1 svg").remove();

    var svgWidth = 1320;
    var svgHeight = 660;

    var color = d3.scaleOrdinal(d3.schemeCategory10);

    var svg = d3.select("#chart1").append("svg")
        .attr("width", svgWidth)
        .attr("height", svgHeight);

    var margin = { top: 20, right: 20, bottom: 200, left: 100 },
        width = svgWidth - margin.left - margin.right,
        height = svgHeight - margin.top - margin.bottom;

    var x = d3.scaleBand().rangeRound([0, width]).padding(0.6);
    var y = d3.scaleLinear().rangeRound([height, 0]);

    var g = svg.append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    x.domain(data.map(function (d) { return d.academic_name; }));
    y.domain([0, d3.max(data, function (d) { return d.number_of_students; })]);

    g.append("g")
    .attr("class", "axis axis-x")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).tickSizeOuter(0))
    .selectAll(".tick text")
    .attr("transform", "rotate(-60)")
    .attr("x", -15 )
    .attr("y", 6) 
    .style("text-anchor", "end")
    .text(d => d.substring(0, 25));


    g.append("g")
        .attr("class", "axis axis-y")
        .call(d3.axisLeft(y).ticks(10))
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", -60)
        
        .attr("dy", "0.71em")
        .attr("text-anchor", "end")
        .text("Broj studenata");

    g.selectAll(".bar")
        .data(data)
        .enter().append("rect")
        .attr("class", "bar")
        .attr("x", function (d) { return x(d.academic_name); })
        .attr("y", function (d) { return y(d.number_of_students); })
        .attr("width", x.bandwidth())
        .attr("height", function (d) { return height - y(d.number_of_students); })
        .attr("fill", function (d) { return color(d.academic_name); })
        .on("mouseover", function (event, d) {
            const tooltip = d3.select(".tooltip");
            tooltip.style("display", "block");
            tooltip.html(`<strong>${d.academic_name}</strong><br>${d.region}, Broj studenata: ${d.number_of_students}`)
                .style("left", (event.pageX - 185) + "px")
                .style("top", (event.pageY) + "px");
        })
        .on("mouseout", function () {
            const tooltip = d3.select(".tooltip");
            tooltip.style("display", "none");
        });

        
}

// Inicijalizacija prvog grafa
initializeFirstChart();