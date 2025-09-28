# College Inquiry Chatbot 🤖

A full-stack, AI-powered chatbot designed to answer common questions for prospective college students. This project uses a Keras/TensorFlow model for Natural Language Processing (NLP) to understand user queries and provide instant, relevant responses. The application is built with a Python/Flask backend and features a modern, embeddable web interface.

---
## Demo

Here is a live demonstration of the chatbot running on a local machine:

**
**(To create a GIF, you can use a free tool like ScreenToGIF or GIPHY Capture to record your screen while you interact with the chatbot locally.)**

---
## Project Status
**Note on Deployment:** This application is fully functional but is currently not deployed live. The free hosting tiers (e.g., Render Free Tier) have memory limits (512MB RAM) that are insufficient for running TensorFlow/Keras models in production. The project is fully configured for deployment on a suitable paid plan. Please refer to the demo GIF above and the setup instructions to run it locally.

---
## Features
- **Intelligent Intent Recognition:** Uses a deep learning model to accurately classify user queries into categories like `admission_fees`, `course_inquiry`, etc.
- **Dynamic Web Interface:** A clean, responsive chat widget built with HTML, CSS, and JavaScript that can be embedded on any website.
- **Easily Extensible:** The chatbot's knowledge can be expanded by simply adding new intents to the `intents.json` file and retraining the model.
- **Production-Ready Backend:** Built with a Flask and Gunicorn backend, complete with a `build.sh` script for seamless deployment.

---
## Tech Stack
- **Backend:** Python, Flask, Gunicorn
- **ML/NLP:** TensorFlow, Keras, NLTK
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Configured for Render, Heroku (PaaS)

---
## Local Setup and Installation

Follow these steps to set up and run the project on your local machine.

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/akshgraju/college-chatbot.git](https://github.com/akshgraju/college-chatbot.git)
    cd college-chatbot
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---
## Usage

1.  **Train the Model:**
    Before running the app for the first time, or after updating `intents.json`, you must train the model.
    ```bash
    python train_chatbot.py
    ```

2.  **Run the Web Application:**
    ```bash
    python app.py
    ```
    Open your web browser and navigate to **`http://127.0.0.1:5000`**.
