from vertexai.preview.generative_models import GenerativeModel

model = GenerativeModel("gemini-1.0-pro")

def explain_results(question, df):
    prompt = f"""
    Question: {question}

    Query result:
    {df.to_string(index=False)}

    Provide a concise explanation.
    """
    response = model.generate_content(prompt)
    return response.text