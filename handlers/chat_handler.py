from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio

from database.db_manager import (
    get_user, check_and_update_limits, get_chat_context, 
    get_or_create_user, update_user 
)
from utils.openai_client import get_ai_response
from keyboards.builders import tariffs_kb
from utils.localization import get_string
from config import FREE_LIMIT_MESSAGES

router = Router()

class ChatState(StatesGroup):
    chatting = State()

@router.message(F.text & ~F.text.startswith('/'))
async def handle_chat_message(message: Message, state: FSMContext, bot: Bot):
    user = await get_or_create_user(
        message.from_user.id, 
        message.from_user.username, 
        message.from_user.first_name
    )
    lang = user.language_code 

    is_limit_exceeded = await check_and_update_limits(user)
    if is_limit_exceeded:
        await message.answer(
            get_string(lang, 'limit_exceeded').format(limit=FREE_LIMIT_MESSAGES),
            reply_markup=tariffs_kb(lang) 
        )
        return
        
    await state.set_state(ChatState.chatting)
    await bot.send_chat_action(message.chat.id, 'typing')
    
    if user.current_tariff == "FREE":
        await asyncio.sleep(1.5)

    prompt = message.text
    user_context = await get_chat_context(user.user_id)
    user_message_entry = {"role": "user", "content": prompt}
    user_context.append(user_message_entry)

    ai_response = await get_ai_response(
        user.user_id, 
        user_context, 
        user.selected_model,
        user.user_prefs if user.current_tariff == "ULTRA" else None
    )

    ai_message_entry = {"role": "assistant", "content": ai_response}
    user_context.append(ai_message_entry) 
    
    max_context_size = 10 
    if len(user_context) > max_context_size:
        user_context = user_context[-max_context_size:]
        
    await update_user(user.user_id, chat_context=user_context)

    await message.answer(ai_response, parse_mode=None) 
    await state.clear()