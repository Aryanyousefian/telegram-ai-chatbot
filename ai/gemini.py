import os
import google.generativeai as genai


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


async def ask_gemini(text):

    model = genai.GenerativeModel(
        "gemini-2.0-flash"
    )

    response = model.generate_content(
        text
    )

    return response.text
