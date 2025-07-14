

# app.py

import streamlit as st
from utils.transcription import transcribe_audio
from utils.summarizer import summarize_text
from utils.qa import answer_questions
from utils.pdf_generator import generate_report

st.set_page_config(page_title="Zuddl Clipsum", layout="centered")

st.title("🎧 Zuddl Clipsum")
st.markdown("Upload podcasts, webinars, or meeting recordings — get a transcript, summary, insights, and a downloadable report.")

uploaded_file = st.file_uploader("📁 Upload audio/video", type=["mp3", "mp4", "wav", "m4a"])

if uploaded_file:
    st.success(f"Uploaded: `{uploaded_file.name}`")
    
    if st.button("🔍 Transcribe"):
        with st.spinner("Transcribing..."):
            transcript = transcribe_audio(uploaded_file)
            st.session_state["transcript"] = transcript
            st.success("✅ Transcription complete!")
            st.text_area("📝 Transcript", transcript, height=300)

    if "transcript" in st.session_state:
        if st.button("📄 Summarize"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(st.session_state["transcript"])
                st.session_state["summary"] = summary
                st.success("✅ Summary ready!")
                st.text_area("🧠 Summary", summary, height=200)

        st.markdown("---")
        st.subheader("💡 Ask Custom Questions")
        questions = st.text_area("Type 1–3 questions (one per line)", height=100)

        if st.button("❓ Get Answers"):
            with st.spinner("Answering your questions..."):
                answers = answer_questions(st.session_state["transcript"], questions.splitlines())
                st.session_state["questions"] = questions.splitlines()
                st.session_state["answers"] = answers
                st.success("✅ Answers ready!")
                for q, a in answers.items():
                    st.markdown(f"**Q:** {q}\n\n**A:** {a}\n")

        st.markdown("---")
        if st.button("📥 Generate PDF Report"):
            with st.spinner("Generating PDF..."):
                pdf_path = generate_report(
                    filename=uploaded_file.name,
                    transcript=st.session_state.get("transcript", ""),
                    summary=st.session_state.get("summary", ""),
                    questions=st.session_state.get("questions", []),
                    answers=st.session_state.get("answers", {})
                )
                with open(pdf_path, "rb") as f:
                    st.download_button("📎 Download Report", f, file_name="zuddl_report.pdf")
