import os
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig

from src.nlp.prompt_templates import BASE_PROMPT

PROJECT_ID = os.getenv("lendingclubvertexai")
LOCATION = "us-central1"
MODEL_NAME = "gemini-1.5-flash"

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
)

model = GenerativeModel(MODEL_NAME)


def question_to_sql(question: str) -> str:
    """
    Convert natural language question to BigQuery SQL.
    """

    full_prompt = f"""
{BASE_PROMPT}

User Question:
{question}
"""

    response = model.generate_content(
        full_prompt,
        generation_config=GenerationConfig(
            temperature=0.2,
            max_output_tokens=512,
        ),
    )

    sql = response.text.strip()

    # Clean markdown if model adds it
    if sql.startswith("```"):
        sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql
