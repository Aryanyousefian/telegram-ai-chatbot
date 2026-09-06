import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

from openai import AsyncOpenAI
from dotenv import load_dotenv


load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=TELEGRAM_TOKEN,
    parse_mode=ParseMode.HTML
)

dp = Dispatcher()

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY
)


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        """
🤖 سلام!

من یک دستیار هوش مصنوعی هستم.

هر سوالی داری بپرس:
- آموزش
- برنامه نویسی
- ترجمه
- ایده پردازی
- نوشتن متن
- حل مشکل

شروع کن 👇
        """
    )


@dp.message()
async def chat(message: types.Message):

    user_text = message.text

    if not user_text:
        return

    await bot.send_chat_action(
        chat_id=message.chat.id,
        action="typing"
    )

    try:
        response = await client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "تو یک دستیار هوش مصنوعی حرفه‌ای هستی. به زبان کاربر پاسخ بده."
                },
                {
                    "role": "user",
                    "content": user_text
                }
            ]
        )

        answer = response.choices[0].message.content

        await message.answer(answer)

    except Exception as e:
        logging.error(e)

        await message.answer(
            "❌ مشکلی در پردازش درخواست پیش آمد."
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
