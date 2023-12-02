document.addEventListener('DOMContentLoaded', function() {

    const websocketClient = new WebSocket("ws://localhost:12345");
    
    const messageContainer = document.getElementById("message_container");
    const messageInput = document.querySelector("[name='message_input']");
    const sendButton = document.querySelector("[name='send_message_button']");
    
    websocketClient.onopen = function() {
        console.log("Connection established!");

        sendButton.onclick = function() {
            websocketClient.send(messageInput.value);
        };
    };

    websocketClient.onmessage = function(message) {
        const newMessage = document.createElement("div");
        newMessage.innerText = message.data;
        messageContainer.appendChild(newMessage);
    };


},false);