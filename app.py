# app.py

from flask import Flask, render_template, request, jsonify
from chatbot_logic import chatbot_response  # Import the function

app = Flask(__name__)

@app.route("/")
def index():
    # This will serve the main HTML file for the chat widget
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the message from the POST request
    text = request.get_json().get("message")
    # TODO: You can add validation here to ensure text is not empty
    
    # Get the response from the chatbot
    response = chatbot_response(text)
    
    # Create a JSON response
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)