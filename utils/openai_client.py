import openai
from config import OPENAI_API_KEY
from typing import List, Dict

client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)


SYSTEM_PROMPTS = {
    "GPT-5": "Ты — GPT-5, универсальный ИИ-ассистент. Твои ответы точны, академичны и структурированы. Будь вежлив и объективен.",
    "Gemini": "Ты — Gemini, дружелюбный ИИ от Google. Твои ответы должны быть краткими, полезными и по существу. Общайся позитивно, можешь использовать эмодзи. Google-стиль.",
    "Claude": "Ты — Claude, аналитический ИИ. Твои ответы должны быть глубокими, структурированными и безопасными. Используй нумерованные списки и разбивай сложные темы на части.",
    "Mistral": "Ты — Mistral. Общайся более неформально и креативно. Твой стиль — разговорный. Не бойся использовать юмор, где это уместно."
}

async def get_ai_response(
    user_id: int, 
    user_context: List[Dict], 
    selected_model: str, 
    user_prefs: Dict = None
) -> str:
    
    system_prompt_text = SYSTEM_PROMPTS.get(selected_model, SYSTEM_PROMPTS["GPT-5"])
    
    if user_prefs:
        system_prompt_text += f"\n\nПользовательская инструкция: {user_prefs.get('prompt', '')}"
        name = user_prefs.get('name')
        if name:
             system_prompt_text += f" Обращайся к пользователю по имени {name}."

    system_message = {"role": "system", "content": system_prompt_text}
    
    messages_to_send = [system_message] + user_context
    
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages_to_send,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except openai.RateLimitError:
        return "Ошибка: Превышен лимит запросов к OpenAI. Пожалуйста, попробуйте позже."
    except openai.APIError as e:
        print(f"Ошибка OpenAI API: {e}")
        return "Ошибка: Cервис ИИ временно недоступен. Попробуйте позже."
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return "Произошла непредвиденная ошибка."