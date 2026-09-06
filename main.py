import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from config import TELEGRAM_TOKEN
from ai.router import ask_ai


logging.basicConfig(level=logging.INFO)


bot = Bot(
    token=TELEGRAM_TOKEN
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):

    await message.answer(
        "🤖 سلام\n\n"
        "من دستیار هوش مصنوعی هستم.\n"
        "هر سوالی داری بپرس."
    )


@dp.message()
async def chat(message: types.Message):

    if not message.text:
        return

    await bot.send_chat_action(
        chat_id=message.chat.id,
        action="typing"
    )

    try:

        answer = await ask_ai(
            message.text
        )

        await message.answer(
            answer
        )

    except Exception as e:

        logging.error(e)

        await message.answer(
            "❌ خطایی رخ داد."
        )


async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
