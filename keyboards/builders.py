from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from utils.localization import get_string
from config import PRO_PRICE_STARS, ULTRA_PRICE_STARS

def language_selection_kb():
    """Клавиатура выбора языка при /start"""
    buttons = [
        [InlineKeyboardButton(text="Русский 🇷🇺", callback_data="set_lang_ru")],
        [InlineKeyboardButton(text="English 🇬🇧", callback_data="set_lang_en")],
        [InlineKeyboardButton(text="Español 🇪🇸", callback_data="set_lang_es")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def main_menu_kb(lang_code: str):
    """Главное меню """
    buttons = [
        [KeyboardButton(text=get_string(lang_code, 'main_menu_chat'))],
        [
            KeyboardButton(text=get_string(lang_code, 'main_menu_model')),
            KeyboardButton(text=get_string(lang_code, 'main_menu_tariffs')),
            KeyboardButton(text=get_string(lang_code, 'main_menu_profile'))
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def models_choice_kb(current_model: str, lang_code: str):
    """Выбор 'модели' (п. 2.2 ТЗ)"""
    
    models = ["GPT-5", "Gemini", "Claude", "Mistral"]
    buttons = []
    for model in models:
        text = f"✅ {model}" if model == current_model else model
        buttons.append([InlineKeyboardButton(text=text, callback_data=f"select_model_{model}")])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def tariffs_kb(lang_code: str):
    """Выбор тарифа"""
    buttons = [
        [InlineKeyboardButton(
            text=get_string(lang_code, 'tariff_pro_button').format(price=PRO_PRICE_STARS), 
            callback_data="buy_tariff_PRO"
        )],
        [InlineKeyboardButton(
            text=get_string(lang_code, 'tariff_ultra_button').format(price=ULTRA_PRICE_STARS), 
            callback_data="buy_tariff_ULTRA"
        )]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def profile_kb(lang_code: str):
    """Кнопки в профиле"""
    buttons = [
        [InlineKeyboardButton(
            text=get_string(lang_code, 'profile_renew_button'), 
            callback_data="goto_tariffs"
        )], 
        [InlineKeyboardButton(
            text=get_string(lang_code, 'profile_clear_history'), 
            callback_data="clear_context"
        )]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)