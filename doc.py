# doc.py
import PyPDF2
from docx import Document
from transformers import pipeline

# Function to read PDF from file-like object
def read_pdf(file_obj):
    text = ""
    reader = PyPDF2.PdfReader(file_obj)  # pass FileStorage object directly
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to read DOCX from file-like object
def read_docx(file_obj):
    doc = Document(file_obj)  # pass FileStorage object directly
    return "\n".join([p.text for p in doc.paragraphs])

# Function to summarize text
summarizer = pipeline("summarization")  # load once globally

def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']
