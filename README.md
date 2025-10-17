# Name :** SARANYA AV**
# Dept : **CSE**
# Reg No : **212224040297**

# 🤖 Intelligent Enterprise Assistant
### *Enhancing Organizational Efficiency through AI-driven Chatbot Integration*  
**Problem ID:** SIH1706  

---

## 📘 Problem Statement

Develop a chatbot using **Deep Learning** and **Natural Language Processing (NLP)** to accurately understand and respond to queries from employees of a **large public sector organization**.  

The chatbot should handle diverse questions related to:
- HR Policies  
- IT Support  
- Company Events  
- Other organizational matters  

It should also support **document processing** (upload, text extraction, summarization, keyword extraction) and be capable of handling at least **5 users concurrently**, maintaining a **response time ≤ 5 seconds**.  

Additional requirements:
- **2-Factor Authentication (2FA)** using email ID  
- **Profanity filtering** using a system-maintained dictionary  
- **Scalable architecture** with optimized response handling  

---

## 🎯 Objective

To create an **AI-powered conversational assistant** that improves internal efficiency, reduces repetitive HR/IT workloads, and enables seamless document analysis and information retrieval for employees.

---

## 🧩 Key Features

✅ **Natural Language Understanding (NLU)** – Understands user intent and context  
✅ **Multi-Domain Support** – HR, IT, Events, Policies, etc.  
✅ **Document Intelligence** – Extracts, summarizes, and retrieves document insights  
✅ **2FA Security** – Email-based One-Time Password verification  
✅ **Profanity Filter** – Detects and removes inappropriate language  
✅ **Scalable Architecture** – Supports 5+ concurrent users with sub-5s responses  
✅ **User-Friendly UI** – Intuitive and responsive chat interface  
✅ **Contextual Memory** – Maintains session history for intelligent responses  

---

+-----------------------+

Implementation Code

app.py

```
import torch
from transformers import pipeline
import re

# Bad word filter
bad_words = ["badword1", "badword2"]

# Load QA pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def clean_input(user_input):
    for word in bad_words:
        user_input = re.sub(word, "***", user_input, flags=re.IGNORECASE)
    return user_input

def get_response(user_input, context=""):
    user_input = clean_input(user_input)
    if context:
        result = qa_pipeline(question=user_input, context=context)
        return result['answer']
    else:
        return "Sorry, I need more info to answer."
```

chatbot.py
```
import torch 
from transformers import pipeline
import re

# Load a simple QA pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Bad word filter dictionary
bad_words = ["badword1", "badword2"]

def clean_input(user_input):
    for word in bad_words:
        user_input = re.sub(word, "***", user_input, flags=re.IGNORECASE)
    return user_input

def get_response(user_input, context=""):
    user_input = clean_input(user_input)
    if context:
        result = qa_pipeline(question=user_input, context=context)
        return result['answer']
    else:
        return "Sorry, I need more info to answer."
```

email_module.py
```
# email.py
import random
import smtplib
from email.message import EmailMessage

def send_otp(email_address):
    otp = str(random.randint(100000, 999999))
    msg = EmailMessage()
    msg.set_content(f"Your OTP is: {otp}")
    msg['Subject'] = 'Chatbot 2FA Verification'
    msg['From'] = 'your_email@gmail.com'   # replace with your email
    msg['To'] = email_address

    # Send email via Gmail SMTP
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('your_email@gmail.com', 'app_password')  # use App Password
    server.send_message(msg)
    server.quit()
    return otp
```
doc.py
```
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
```
index.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Enterprise Chatbot</title>
</head>
<body>
    <h1>Enterprise Chatbot</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="document">
        <br><br>
        <input type="text" name="question" placeholder="Ask your question">
        <button type="submit">Ask</button>
    </form>
    <h2>Answer:</h2>
    <p>{{ answer }}</p>
</body>
</html>
```
OUTPUT

<img width="419" height="292" alt="image" src="https://github.com/user-attachments/assets/744ffee1-8a08-4d30-88eb-b92935f55c74" />


RESULT:

Thus the chatbot is created successfully.
