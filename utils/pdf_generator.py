# utils/pdf_generator.py

from fpdf import FPDF
import tempfile
import os
import datetime
import re

# Utility to remove emojis and non-latin characters (for FPDF safety)
def remove_unicode(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Zuddl Clipsum - Audio Summary Report", ln=1, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_fill_color(230, 230, 250)
        self.cell(0, 10, title, ln=1, fill=True)
        self.ln(2)

    def chapter_body(self, text):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, text)
        self.ln()

def generate_report(filename, transcript, summary, questions=None, answers=None):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Clean all content before inserting
    filename = remove_unicode(filename)
    transcript = remove_unicode(transcript)
    summary = remove_unicode(summary)

    pdf.chapter_title("File Name")
    pdf.chapter_body(filename)

    pdf.chapter_title("Transcript")
    pdf.chapter_body(transcript if transcript else "No transcript available.")

    pdf.chapter_title("Summary")
    pdf.chapter_body(summary if summary else "No summary generated.")

    if questions and answers:
        pdf.chapter_title("Custom Q&A")
        for question in questions:
            clean_q = remove_unicode(question)
            clean_a = remove_unicode(answers.get(question, 'No answer found.'))

            pdf.set_font("Arial", "B", 11)
            pdf.cell(0, 8, f"Q: {clean_q}", ln=1)
            pdf.set_font("Arial", "", 11)
            pdf.multi_cell(0, 8, f"A: {clean_a}")
            pdf.ln(2)

    # Save PDF to temp location
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_file_path = os.path.join(tempfile.gettempdir(), f"zuddl_report_{timestamp}.pdf")
    pdf.output(pdf_file_path)

    return pdf_file_path
