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
