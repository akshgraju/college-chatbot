# College Inquiry Chatbot 🤖

A simple, rule-based chatbot designed to answer common questions about a college. This project uses Natural Language Processing (NLP) to understand user queries and provides responses from a predefined knowledge base. The chatbot is built with Python and Flask and features a clean, web-based user interface.



## Features
- **Natural Language Understanding:** Uses NLTK and a Keras/TensorFlow model to understand user intent.
- **Web Interface:** A user-friendly chat widget built with HTML, CSS, and JavaScript.
- **Easily Trainable:** Add new patterns and responses by simply editing the `intents.json` file.
- **Ready for Deployment:** Built with a Flask/Gunicorn backend, ready to be hosted online.

## Tech Stack
- **Backend:** Python, Flask, Gunicorn
- **ML/NLP:** Keras (TensorFlow), NLTK
- **Frontend:** HTML, CSS, JavaScript

## Setup and Installation

Follow these steps to set up the project on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/your-repo-name.git](https://github.com/YourUsername/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Train the model:**
    Before running the app for the first time (or after you've updated `intents.json`), you need to train the model.
    ```bash
    python train_chatbot.py
    ```

2.  **Run the web application:**
    ```bash
    python app.py
    ```
    Open your browser and navigate to `http://127.0.0.1:5000`.

## Deployment
This application is deployed on Render and can be accessed live.

**Live URL:** [Add Your Render URL Here]