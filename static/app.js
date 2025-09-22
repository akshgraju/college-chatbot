// static/app.js

// DOM Elements
const chatToggleButton = document.getElementById('chat-toggle');
const chatPopup = document.getElementById('chat-popup');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const chatMessagesContainer = document.getElementById('chat-messages');

// Toggle chat popup visibility
chatToggleButton.addEventListener('click', () => {
    chatPopup.classList.toggle('show');
});

// Function to add a message to the chat container
function addMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
    messageElement.textContent = message;
    chatMessagesContainer.appendChild(messageElement);
    
    // Auto-scroll to the latest message
    chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
}

// Function to handle sending a message
function sendMessage() {
    const message = messageInput.value.trim();
    if (message === '') return;

    addMessage(message, 'user');
    messageInput.value = '';

    // Send message to the backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        addMessage(data.answer, 'bot');
    })
    .catch(error => {
        console.error('Error:', error);
        addMessage('Sorry, something went wrong. Please try again.', 'bot');
    });
}

// Event Listeners
sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keyup', (event) => {
    // Send message on 'Enter' key press
    if (event.key === 'Enter') {
        sendMessage();
    }
});

// Initial greeting from the bot
window.onload = () => {
    addMessage("Hello! How can I help you with college information today?", "bot");
};