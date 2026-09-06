from ai.client import ask_ai


async def chat(message):

    answer = await ask_ai(
        message.text
    )

    await message.answer(
        answer
    )
