function sendMessage() {
    const userInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    
    const userMessage = userInput.value;
    if (userMessage) {
        chatBox.innerHTML += `<div class="message user">${userMessage}</div>`;
        userInput.value = '';
        getBotResponse(userMessage);
    }
}

function getBotResponse(input) {
    const chatBox = document.getElementById('chat-box');
    let botMessage = "I don't understand that.";

    if (input.toLowerCase() === "hello") {
        botMessage = "Hi there!";
    } else if (input.toLowerCase() === "how are you?") {
        botMessage = "I'm just a bot, but thanks for asking!";
    }

    chatBox.innerHTML += `<div class="message bot">${botMessage}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
}
