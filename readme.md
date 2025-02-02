# ResQ Backend

ResQ is a backend service designed to record emergency services data, process and analyze the information, and promptly notify the appropriate administrators. This service accepts both audio and text inputs, transcribes audio using OpenAI's Whisper, and processes the transcriptions with Google Generative AI to generate structured data. All data is stored in a Firebase Realtime Database for easy retrieval and updates.

## Overview

The ResQ backend is built with Flask and provides a set of RESTful API endpoints to:

- Record emergency responses (via audio or text).
- Transcribe and process the emergency information.
- Store and manage responses using Firebase Realtime Database.
- Enable rapid notification and analysis for timely admin intervention.

## Features

- **Audio Transcription:** Uses OpenAI's Whisper API to transcribe audio recordings.
- **Structured Data Generation:** Leverages a Gemini prompt with Google Generative AI to process and format transcriptions.
- **Firebase Integration:** Stores, updates, and deletes emergency response records in Firebase Realtime Database.
- **RESTful API Endpoints:** Provides endpoints for creating, reading, updating, and deleting responses.
- **CORS Enabled:** Configured to support cross-origin requests, facilitating integration with front-end applications.

## Architecture

The project is organized into several key modules:

- **`main.py`:**  
  Initializes the Flask app, loads configuration, enables CORS, and registers API routes.

- **`routes.py`:**  
  Contains API endpoints for:
  - Testing the API.
  - Fetching all responses.
  - Adding a new response.
  - Updating an existing response.
  - Deleting a response.

- **`helper_functions.py`:**  
  Provides functions to:
  - Transcribe audio files using OpenAI's Whisper.
  - Process transcriptions with a Gemini prompt to generate structured JSON data.

- **`firebase_helper.py`:**  
  Handles all interactions with the Firebase Realtime Database, including:
  - Retrieving the database reference.
  - Inserting new records.
  - Updating existing records.

- **`Config.py`:**  
  Manages application configuration, including:
  - Secret keys.
  - Firebase credentials and database URL.
  - Other environment-specific settings.

- **`requirements.txt`:**  
  Lists all Python dependencies for the project.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/resq-backend. git
    cd resq-backend
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Environment Variables:**
Create a .env file in the project root and add the following variables:

    ```bash
    SECRET_KEY=your_secret_key
    FIREBASE_CREDENTIALS=./path-to-your-firebase-credentials.json
    FIREBASE_DATABASE_URL=https://your-firebase-database-url.firebaseio.com/
    openai_api_key=your_openai_api_key
    gemini_api_key=your_gemini_api_key
    ```

2. **Gemini Prompt:**
Ensure you have a gemini_prompt.txt file in the project root. This file contains the prompt that guides the processing of transcriptions.
<br \>

3. **Firebase Setup:**

    - Obtain your Firebase service account key JSON file.
    - Set the FIREBASE_CREDENTIALS environment variable to the path of this file.
    - Set the FIREBASE_DATABASE_URL to your Firebase Realtime Database URL.

## Usage

- You can start the Flask application by running: `python main.py`

- The application will run in debug mode on the default port (5000). For production deployments, consider using a WSGI server like Gunicorn: `gunicorn main:app`

- Test the API by sending requests to the available endpoints. You can use tools like Postman or cURL to interact with the API.
