from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import datetime
from keyboards.builders import (
    main_menu_kb, profile_kb, models_choice_kb, 
    tariffs_kb, language_selection_kb
)
from database.db_manager import get_or_create_user, clear_chat_context, get_user, update_user
from config import FREE_LIMIT_MESSAGES
from utils.localization import get_string

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    
    await get_or_create_user(message.from_user.id, message.from_user.username, message.from_user.first_name)

    await message.answer(
        get_string('ru', 'select_language'),
        reply_markup=language_selection_kb()
    )

@router.callback_query(F.data.startswith("set_lang_"))
async def cb_set_language(callback: CallbackQuery):
    """
    Хэндлер, который ловит выбор языка, сохраняет его в БД
    и отправляет приветственное сообщение.
    """
    lang_code = callback.data.split("_")[-1] 
    user_id = callback.from_user.id
    
    await update_user(user_id, language_code=lang_code)
    
    user = await get_user(user_id)
    
    welcome_text = get_string(lang_code, 'welcome').format(
        first_name=user.first_name or 'User',
        limit=FREE_LIMIT_MESSAGES
    )
    
    await callback.message.edit_text(
        get_string(lang_code, 'language_selected') + welcome_text,
        reply_markup=None 
    )
    
    await callback.message.answer(
        get_string(lang_code, 'start_chat_prompt'),
        reply_markup=main_menu_kb(lang_code)
    )
    await callback.answer()


@router.message(F.text.in_([
    get_string('ru', 'main_menu_chat'), 
    get_string('en', 'main_menu_chat'), 
    get_string('es', 'main_menu_chat')
]))
async def msg_start_chat(message: Message):
    user = await get_user(message.from_user.id)
    await message.answer(get_string(user.language_code, 'start_chat_prompt'))

@router.message(F.text.in_([
    get_string('ru', 'main_menu_model'), 
    get_string('en', 'main_menu_model'), 
    get_string('es', 'main_menu_model')
]))
async def msg_models(message: Message):
    user = await get_user(message.from_user.id)
    await message.answer(
        get_string(user.language_code, 'model_select_prompt'),
        reply_markup=models_choice_kb(user.selected_model, user.language_code)
    )

@router.message(F.text.in_([
    get_string('ru', 'main_menu_tariffs'), 
    get_string('en', 'main_menu_tariffs'), 
    get_string('es', 'main_menu_tariffs')
]))
async def msg_tariffs(message: Message):
    user = await get_user(message.from_user.id)
    await message.answer(
        get_string(user.language_code, 'tariffs_prompt'),
        reply_markup=tariffs_kb(user.language_code)
    )

@router.message(F.text.in_([
    get_string('ru', 'main_menu_profile'), 
    get_string('en', 'main_menu_profile'), 
    get_string('es', 'main_menu_profile')
]))
async def msg_profile(message: Message):
    user = await get_user(message.from_user.id)
    lang = user.language_code
    
    if user.current_tariff == "FREE":
        limit_text = get_string(lang, 'profile_limit_free').format(
            count=(FREE_LIMIT_MESSAGES - user.message_count)
        )
    else:
        expires = user.tariff_expires_at.strftime("%d.%m.%Y") if user.tariff_expires_at else get_string(lang, 'profile_limit_never')
        limit_text = get_string(lang, 'profile_limit_paid').format(date=expires)

    profile_text = (
        f"{get_string(lang, 'profile_title')}\n\n"
        f"{get_string(lang, 'profile_name')}: {user.first_name}\n"
        f"{get_string(lang, 'profile_id')}: {user.user_id}\n"
        f"{get_string(lang, 'profile_tariff')}: {user.current_tariff}\n"
        f"{limit_text}"
    )
    
    await message.answer(profile_text, reply_markup=profile_kb(lang))

@router.callback_query(F.data == "clear_context")
async def cb_clear_context(callback: CallbackQuery):
    await clear_chat_context(callback.from_user.id)
    user = await get_user(callback.from_user.id)
    
    await callback.answer(
        get_string(user.language_code, 'history_cleared'), 
        show_alert=True
    )
    await callback.message.delete() 

@router.callback_query(F.data == "goto_tariffs")
async def cb_goto_tariffs(callback: CallbackQuery):
    """Переход к тарифам из профиля"""
    user = await get_user(callback.from_user.id)
    await callback.message.answer(
        get_string(user.language_code, 'tariffs_prompt'),
        reply_markup=tariffs_kb(user.language_code)
    )
    await callback.answer()