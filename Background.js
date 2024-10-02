function search(){
    window.location.href = "ResultsPage.html"

    function displayResults(results) {
        const resultContainer = document.getElementById("resultContainer");
        resultContainer.innerHTML = "";
        if (results.length > 0) {
            results.forEach(result => {
                resultContainer.innerHTML += `<p>${result["SITE ADDRESS"]}</p>`;
            });
        } else {
            resultContainer.innerHTML = "<p>No results found.</p>";
        }
    }

}