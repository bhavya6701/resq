import openai
import google.generativeai as genai
import json
from datetime import datetime
import os
from dotenv import load_dotenv  # <-- Add this

# Load environment variables from .env file (local only)
load_dotenv()

gemini_prompt_file = open("gemini_prompt.txt", "r")

gemini_prompt = gemini_prompt_file.read()
openai_api_key = os.environ.get('openai_api_key')
gemini_api_key = os.environ.get('gemini_api_key')

openai_client = openai.Client(api_key=openai_api_key)
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


def transcribe_audio(audio_tuple):
    """
    Extracts text from the given audio file using Google Cloud Speech-to-Text API.

    Parameters:
    audio (str): Path to the audio file.

    Returns:
    str: Extracted text.
    """
    # Open the temporary file in binary read mode
    # audio_file = open(audio_file_path, "rb")
    
    # Transcribe the audio file using Whisper via OpenAI
    audio_transcription = openai_client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_tuple
    )
    
    # Store the extracted text
    transcription_text = audio_transcription.text
    
    return transcription_text


def process_transcription(transcription):
    """
    Process the transcription text to generate structured content.

    Parameters:
    transcription (str): Transcription text.

    Returns:
    dict: Structured content.
    """
    # Combine the Gemini prompt with the transcription text
    new_prompt = gemini_prompt + transcription

    # Generate structured content based on the new prompt
    response = model.generate_content(new_prompt)

    # Modify the response to match the expected format.
    # Replace "Caller" with "User" and extract the JSON substring.
    modified_response = response.text.replace("Caller", "User")
    modified_response = modified_response.replace("caller", "user")
    start_idx = modified_response.find("{")
    end_idx = modified_response.rfind("}")
    if start_idx == -1 or end_idx == -1:
        raise ValueError("Invalid response format")
    modified_response = modified_response[start_idx:end_idx+1]

    response_json = json.loads(modified_response)

    # If incident_timestamp is "not given", update it with the current datetime.
    if response_json.get("incident_timestamp", "not given") == "not given":
        response_json["incident_user_timestamp"] = datetime.now().isoformat()

    return response_json