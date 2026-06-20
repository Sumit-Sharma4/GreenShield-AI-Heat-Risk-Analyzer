import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Load API key from .env
GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

# Configure Gemini
genai.configure(
    api_key=GEMINI_API_KEY
)

# Select model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(
    city: str,
    city_data: dict,
    question: str
):

    prompt = f"""
You are GreenShield AI.

City: {city}

City Data:
{city_data}

Question:
{question}

Rules:
1. Maximum 300 words.
2. Plain text only.
3. No markdown.
4. No ### headings.
5. No ** symbols.
6. Maximum 3 reasons.
7. Maximum 3 recommendations.

Format:

Answer:
• Reason 1
• Reason 2
• Reason 3

Recommendations:
• Recommendation 1
• Recommendation 2
• Recommendation 3
"""

    try:

        response = model.generate_content(
           prompt,
           generation_config={
               "max_output_tokens": 1000,
               "temperature": 0.3,
            }
        )
        print(response.text)

        return response.text

    except Exception as e:

        return (
            f"Gemini Error: {str(e)}"
        )