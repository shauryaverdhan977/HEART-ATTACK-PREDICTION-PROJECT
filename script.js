function showLoader() {
    document.getElementById("loader").classList.remove("hidden");
}

// Result logic
function updateUI(prob) {
    const bar = document.getElementById("progressBar");
    const box = document.getElementById("resultBox");
    const riskText = document.getElementById("riskText");

    if (bar) {
        bar.style.width = (prob * 100) + "%";
        if (prob > 0.6) {
            box.classList.add("high");
            riskText.innerText = "⚠ High Risk - Consult a doctor";
        } else {
            box.classList.add("low");
            riskText.innerText = "✅ Low Risk - Maintain healthy lifestyle";
        }
    }
}
