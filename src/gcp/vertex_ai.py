import os
import vertexai
from vertexai.preview.generative_models import GenerativeModel

PROJECT_ID = os.getenv("lendingclubvertexai")
LOCATION = "us-central1"

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
)

model = GenerativeModel("gemini-1.5-flash-002")

def explain_results(question, df):
    prompt = f"""
    Question: {question}

    Query result:
    {df.to_string(index=False)}

    Provide a concise explanation.
    """
    response = model.generate_content(prompt)
    return response.text