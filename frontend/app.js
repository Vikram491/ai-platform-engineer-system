async function generateApp() {

    const prompt = document.getElementById("prompt").value;

    const resultBox = document.getElementById("result");

    // -----------------------------------
    // Validate Input
    // -----------------------------------

    if (!prompt.trim()) {

        resultBox.innerText = "Please enter a prompt.";

        return;
    }

    // -----------------------------------
    // Loading State
    // -----------------------------------

    resultBox.innerText = "Generating application...";

    try {

        // -----------------------------------
        // API Request
        // -----------------------------------

        const response = await fetch(
            `https://ai-platform-backend-a8w1.onrender.com/generate?prompt=${encodeURIComponent(prompt)}`,
            {
                method: "POST"
            }
        );

        // -----------------------------------
        // Parse Response
        // -----------------------------------

        const data = await response.json();

        // -----------------------------------
        // Display Pretty JSON
        // -----------------------------------

        resultBox.innerText = JSON.stringify(
            data,
            null,
            2
        );

    } catch (error) {

        // -----------------------------------
        // Error Handling
        // -----------------------------------

        resultBox.innerText =
            "Error connecting to backend:\n\n" + error;
    }
}