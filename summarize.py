import PyPDF2
from transformers import pipeline

summarizer = pipeline("summarization")

with open("sample.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

summary = summarizer(text[:1000], max_length=120, min_length=30, do_sample=False)[0]["summary_text"]
print("Summary:\n", summary)
