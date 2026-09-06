from ai.gemini import ask_gemini
from ai.deepseek import ask_deepseek


async def ask_ai(text):

    try:
        return await ask_gemini(text)

    except Exception:

        try:
            return await ask_deepseek(text)

        except Exception:
            return "❌ هیچ سرویس هوش مصنوعی در دسترس نیست."
