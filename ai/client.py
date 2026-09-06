from openai import AsyncOpenAI
from config import OPENAI_API_KEY


client = AsyncOpenAI(
    api_key=OPENAI_API_KEY
)


async def ask_ai(text):

    response = await client.chat.completions.create(
        model="gpt-4.1-mini",

        messages=[
            {
                "role": "system",
                "content": "تو یک دستیار هوش مصنوعی فارسی زبان هستی."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content
