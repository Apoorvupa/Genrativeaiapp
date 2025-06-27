import requests
import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Token check for debugging
api_key = os.getenv("HF_API_KEY")
if api_key:
    print("✅ HuggingFace API key loaded successfully.")
else:
    print("❌ API key not found. Please check your .env file.")

# ✅ Correct API URL for Mistral 7B Instruct v0.3
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
headers = {"Authorization": f"Bearer {api_key}"}

def generate_llm_response(prompt: str) -> str:
    try:
        payload = {
            "inputs": f"[INST] {prompt} [/INST]",
            "parameters": {
                "max_new_tokens": 150,
                "temperature": 0.7
            }
        }
        print("📡 Sending request to Hugging Face API...")
        response = requests.post(API_URL, headers=headers, json=payload)

        print("📥 Raw Response:", response.text)
        print("📦 Status Code:", response.status_code)

        if not response.text.strip():
            return "❌ Error: Empty response from Hugging Face API"

        result = response.json()

        if isinstance(result, list) and 'generated_text' in result[0]:
            return result[0]['generated_text'].replace(f"[INST] {prompt} [/INST]", "").strip()
        else:
            return f"❌ HuggingFace Error: {result.get('error', 'Unknown error')}"
    except Exception as e:
        return f"❌ Exception: {str(e)}"
