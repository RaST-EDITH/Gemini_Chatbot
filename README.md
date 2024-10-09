# Gemini ChatBot 🤖

Welcome to the **Gemini ChatBot** project! This application utilizes the Gemini API to provide a conversational AI experience. You can ask questions and receive responses in real-time.

## Features ✨

- Interactive Q&A using Gemini's LLM (Large Language Model)
- Session-based chat history for a more engaging user experience
- Streamlit framework for easy deployment and use

## Prerequisites 🛠️

Before you begin, ensure you have the following installed:

- Python 3.7 or later
- Streamlit
- `python-dotenv` for environment variable management
- `google-generativeai` for accessing the Gemini API

## Setup Instructions 📋

1. **Clone the repository:**

   ```bash
   git clone https://github.com/RaST-EDITH/Gemini_Chatbot.git
   cd Gemini_Chatbot
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install streamlit python-dotenv google-generativeai
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root of the project directory and add your Google API key:

   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

   Replace `your_api_key_here` with your actual API key.

5. **Run the application:**

   Use Streamlit to run the application:

   ```bash
   streamlit run app.py
   ```

   This command will start a local server, and you can access the application in your web browser at `http://localhost:8501`.

## Usage 🗣️

- Enter your question in the input box and click "Ask the question".
- The bot will respond with the answer based on your input.
- The chat history will be maintained on the page for reference.

## Contribution 🤝

Contributions are welcome! If you'd like to improve the project or add features, feel free to open an issue or submit a pull request.
