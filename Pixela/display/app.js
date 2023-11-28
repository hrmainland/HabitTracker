username = "___"
token = "___"

const config = {
    headers: {
        "X-USER-TOKEN": "bigoldtoken",
    }
};


const url = "https://pixe.la/v1/users/hmainland/graphs";

async function getGraphs() {
    let data = await axios.get(url, config);
    console.log(data)
    return data
}

const graphRow = document.querySelector("#graph-row")


// Set this up so that you can fit exactly two rows on the screen
function createGraphSection(name, id) {
    let outerSection = document.createElement("section");
    // Does it look better to center odd numbered graphs?
    graphCollapse = null;
    if (graphs.length < 5) {
        graphCollapse = ["col-md-6"];
    }
    else {
        graphCollapse = ["col-md-6", "col-lg-4"];
    }
    outerSection.classList.add(...graphCollapse, "text-center", "graph-section");
    let graphHeader = document.createElement("div");
    graphHeader.setAttribute("class", "graph")
    let graphTitle = document.createElement("h2");
    graphTitle.innerText = name;
    graphTitle.classList.add("display-6");
    // add the title to the header
    graphHeader.append(graphTitle)
    let graphImage = document.createElement("img");
    graphImage.setAttribute("alt", "Pixela Graph");
    // Might not need this line with SVGs
    // graphImage.setAttribute("style", "width: 95%;");
    graphImage.setAttribute("src", `https://pixe.la/v1/users/hmainland/graphs/${id}?mode=short`);
    outerSection.append(graphHeader);
    outerSection.append(graphImage);
    return outerSection;
}


let graphs = null;

async function makeGraphs() {
    graphs = await getGraphs()
    graphs = graphs.data.graphs
    for (let graph of graphs) {
        console.log(graph.name, graph.id)
        graphRow.append(createGraphSection(graph.name, graph.id));
    }
}

makeGraphs()
