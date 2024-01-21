# GeminiLLMApp

This is a basic Streamlit project that utilizes Gemini-Pro and Gemini-Vision-Pro for text and image generation. Follow the steps below to set up and run the project.

## Prerequisites

- Python 3.10
- Anaconda
- Git

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/hgarg97/GeminiLLMApp.git
   ```

2. Navigate to the project directory:

   ```bash
   cd GeminiLLMApp
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   conda create -n genAiEnv python==3.10 -y
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     conda activate genAiEnv
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Obtain API keys for Gemini from https://makersuite.google.com/app/apikey

2. Create a `.env` file in the project root and add the following:

   ```env
   GOOGLE_API_KEY=your_gemini_pro_api_key
   ```

   Replace `your_gemini_pro_api_key` with your actual API key.

   **Note:** Ensure that the `.env` file is listed in your `.gitignore` to avoid exposing sensitive information.

## Running the Application

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

   This will start the development server, and you can view the app in your browser at [http://localhost:8501](http://localhost:8501).

2. Interact with the app and explore text and image generations powered by Gemini-Pro and Gemini-Vision-Pro.
