# 🎧 Zuddl Clipsum

**Zuddl Clipsum** is a proof-of-concept (POC) Streamlit app that allows professionals to:

- Upload audio/video files
- Transcribe using OpenAI Whisper
- Summarize content using Hugging Face Transformers
- Ask custom questions and extract insights
- Generate a structured PDF report

This POC demonstrates product thinking and technical implementation for internal presentation.

---

## 🚀 Features

- 🎙️ Upload `.mp3`, `.mp4`, `.wav`, `.m4a`
- 🔍 Transcription with Whisper
- 🧠 Summarization using BART (Transformers)
- 💡 Custom Q&A over the transcript
- 📄 PDF report generation using FPDF

---

## 🧰 Tech Stack

| Purpose             | Tool/Library                      |
|---------------------|-----------------------------------|
| UI                  | Streamlit                         |
| Transcription       | OpenAI Whisper                    |
| Summarization/Q&A   | Hugging Face Transformers         |
| PDF Export          | FPDF                              |
| Platform            | Spyder (Anaconda), Streamlit Cloud|

---

## 📦 Setup Instructions

### 1. Clone or Extract the Project
Unzip or clone the project folder into your workspace.

### 2. Create a Conda Environment

```bash
conda create -n zuddl_env python=3.10
conda activate zuddl_env
