// chart2.js
function initializeSecondChart() {
    d3.json("modifiedData.json").then(function (data) {
        const studyFields = [...new Set(data.map(d => d.study_field))];

        const checkboxContainer = d3.select("#checkboxContainer2");
        studyFields.forEach(field => {
            checkboxContainer.append("input")
                .attr("type", "checkbox")
                .attr("id", field)
                .attr("value", field)
                .attr("checked", true)
                .on("change", updateChart2);

            checkboxContainer.append("label")
                .attr("for", field)
                .text(field);
            checkboxContainer.append("br");
        });

        const width = 800;
        const height = 400;
        const margin = { top: 20, right: 20, bottom: 170, left: 100 };

        const svg = d3.select("#chart2")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        const x = d3.scaleBand()
            .range([0, width])
            .padding(0.1);

        const y = d3.scaleLinear()
            .range([height, 0]);

        const sortOrderSelect = document.getElementById("sortOrder2");
        sortOrderSelect.addEventListener("change", updateChart2);

        const toggleStudyFieldsButton = document.getElementById("toggleStudyFields2");
        toggleStudyFieldsButton.addEventListener("click", toggleStudyFields2);

        const tooltip = d3.select(".tooltip2");


        function toggleStudyFields2() {
            const checkboxContainerDiv = document.getElementById("checkboxContainerDiv2");
            checkboxContainerDiv.style.display = checkboxContainerDiv.style.display === "none" ? "block" : "none";
        }

        function updateChart2() {
            const sortOrder = sortOrderSelect.value === "ascending" ? 1 : -1;

            const selectedFields = Array.from(document.querySelectorAll("#checkboxContainer2 input:checked"), input => input.value);
            const filteredData = data.filter(d => selectedFields.includes(d.study_field));

            const counts = selectedFields.map(field => ({
                field: field,
                count: filteredData.filter(d => d.study_field === field)
                    .reduce((acc, cur) => acc + cur.number_of_students, 0)
            }));

            counts.sort((a, b) => sortOrder * (a.count - b.count));

            x.domain(counts.map(d => d.field));
            y.domain([0, d3.max(counts, d => d.count)]).nice();

            svg.selectAll(".bar").remove();

            svg.selectAll(".bar")
                .data(counts)
                .enter().append("rect")
                .attr("class", "bar")
                .attr("x", d => x(d.field))
                .attr("width", x.bandwidth())
                .attr("y", d => y(d.count))
                .attr("height", d => height - y(d.count))
                .on("mouseover", function (event, d) {
                    d3.select(this).attr("fill", "lightblue");
                    tooltip.transition()
                        .duration(200)
                        .style("opacity", .9);
                    tooltip.html(`<strong>${d.field}</strong><br/>Broj studenata: ${d.count}`)
                        .style("left", (event.pageX) + "px")
                        .style("top", (event.pageY - 28) + "px");
                })
                .on("mouseout", function () {
                    d3.select(this).attr("fill", "steelblue");
                    tooltip.transition()
                        .duration(500)
                        .style("opacity", 0);
                })
                .transition()
                .duration(500)
                .attr("y", d => y(d.count))
                .attr("height", d => height - y(d.count));

            svg.selectAll(".x-axis").remove();
            svg.append("g")
                .attr("class", "x-axis")
                .attr("transform", `translate(0,${height})`)
                .call(d3.axisBottom(x))
                .selectAll("text")
                .attr("transform", "rotate(-45)")
                .attr("x", -9)
                .attr("y", 0)
                .style("text-anchor", "end")
                .text(d => d.substring(0, 12));

            svg.selectAll(".y-axis").remove();
            svg.append("g")
                .attr("class", "y-axis")
                .call(d3.axisLeft(y));

        }

        updateChart2();
    }).catch(function (error) {
        console.log("Došlo je do pogreške pri učitavanju podataka:", error);
    });
}

// Inicijalizacija drugog grafa
initializeSecondChart();
