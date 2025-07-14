# -*- coding: utf-8 -*-

# utils/transcription.py

import whisper
import tempfile
import os

# Load Whisper model once
model = whisper.load_model("base")

def transcribe_audio(uploaded_file):
    """
    Takes an uploaded audio/video file (BytesIO),
    saves it temporarily, and returns the transcript as text.
    """
    # Save to a temporary file
    suffix = "." + uploaded_file.name.split('.')[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_filepath = tmp_file.name

    try:
        result = model.transcribe(tmp_filepath)
        return result["text"]
    finally:
        os.remove(tmp_filepath)
