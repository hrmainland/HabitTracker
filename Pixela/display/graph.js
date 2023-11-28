// Make this an API call
stats = {
    Overview: [4, 3],
    Week: [5, 7],
    Month: [13, 18],
    "All Time": [101, 156],
}

const statsButtons = document.querySelectorAll(".stats")

const navLinks = document.querySelectorAll(".nav-link");
const statText = document.querySelector("#stat-text");

for (let statButton of statsButtons) {
    statButton.addEventListener("click", () => {
        const graph = statButton.parentElement.nextElementSibling
        otherSide = graph.nextElementSibling
        graph.classList.toggle("flipped");
        otherSide.classList.toggle("flipped");
        if (statButton.getAttribute("src").includes("Stats")) {
            statButton.setAttribute("src", "default_pix.png")
        }
        else {
            statButton.setAttribute("src", "Stats.png")
        }
        // Display text for overview tab when first flipped
        let grandparentSection = statButton.parentElement.parentElement;
        let firstNavLink = grandparentSection.querySelector(".nav-link");
        let statText = grandparentSection.querySelector("#stat-text");
        statText.innerText = `Best Streak: ${stats[firstNavLink.innerHTML][0]}`
    })
}

for (let link of navLinks) {
    link.addEventListener("click", () => {
        link.classList.add("active");
        // add logic here to only select the sibling nav links and then
        // loop over those
        for (let innerLink of navLinks) {
            if (innerLink === link) {
                continue;
            }
            innerLink.classList.remove("active")
        }
        statText.innerText = `Best Streak: ${stats[link.innerHTML][0]}`
    })
}

