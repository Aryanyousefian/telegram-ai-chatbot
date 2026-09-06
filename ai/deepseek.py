import os
from openai import AsyncOpenAI


client = AsyncOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


async def ask_deepseek(text):

    response = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content
