async function generateApp() {

    const prompt = document.getElementById("prompt").value;

    const resultBox = document.getElementById("result");

    resultBox.innerText = "Generating...";

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/generate?prompt=${encodeURIComponent(prompt)}`,
            {
                method: "POST"
            }
        );

        const data = await response.json();

        resultBox.innerText = JSON.stringify(data, null, 2);

    } catch (error) {

        resultBox.innerText = "Error: " + error;
    }
}