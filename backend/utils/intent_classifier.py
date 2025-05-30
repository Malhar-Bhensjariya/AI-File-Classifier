import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def classify_intent(content):
    prompt = (
        "You are an intent classifier for business documents. "
        "Given the following text, classify the document intent into one of the following: "
        "RFQ, Complaint, Invoice, Regulation, General.\n\n"
        f"Text:\n{content.decode(errors='ignore')[:1000]}\n\n"
        "Respond with only the intent label."
    )

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return "General"
