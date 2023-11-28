// This would come from an API
const stats = {
    names: ["Meditate", "Read", "Run", "Eat", "Pray"],
    ids: ["med", "read", "run"],
    length: 5,
}

const graphRow = document.querySelector("#graph-row")


// Set this up so that you can fit exactly two rows on the screen
function createGraphSection(name, id) {
    let outerSection = document.createElement("section");
    // Does it look better to center odd numbered graphs?
    graphCollapse = null;
    if (stats.length < 5) {
        graphCollapse = ["col-md-6"];
    }
    else {
        graphCollapse = ["col-md-6", "col-lg-4"];
    }
    outerSection.classList.add(...graphCollapse, "text-center");
    // outerSection.classList.add("col-md-6", "col-lg-4", "text-center");
    let graphHeading = document.createElement("h2");
    graphHeading.innerText = name;
    graphHeading.classList.add("display-6");
    let graphImage = document.createElement("img");
    graphImage.setAttribute("alt", "Pixela Graph");
    // Might not need this line with SVGs
    graphImage.setAttribute("style", "width: 95%;");
    graphImage.setAttribute("src", "default_pix.png");
    outerSection.append(graphHeading);
    outerSection.append(graphImage);
    return outerSection;
}

for (let name of stats.names) {
    graphRow.append(createGraphSection(name, "id"));
}

// async function getGraphs(){

// }