# app/qa_model.py
from transformers import pipeline

# Use a multilingual capable generative QA model
qa_pipeline = pipeline("text2text-generation", model="MBZUAI/LaMini-Flan-T5-783M")

def get_answer(question: str, context: str) -> str:
    # Directly include both question and context
    prompt = f"Context:\n{context}\n\nQuestion:\n{question}"
    result = qa_pipeline(prompt, max_length=512, do_sample=False)
    return result[0]['generated_text']
