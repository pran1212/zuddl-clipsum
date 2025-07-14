# -*- coding: utf-8 -*-

# utils/summarizer.py

from transformers import pipeline

# Load summarization pipeline once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_tokens=1000):
    """
    Split large text into chunks so the model can handle them.
    """
    sentences = text.split('. ')
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_tokens:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def summarize_text(transcript):
    """
    Summarize long transcript text using chunking + BART model.
    """
    chunks = chunk_text(transcript)
    summaries = []

    for chunk in chunks:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summaries.append(summary[0]["summary_text"])

    full_summary = "\n\n".join(summaries)
    return full_summary
