from aiogram import Router, F
from aiogram.types import CallbackQuery
from database.db_manager import update_user, get_user
from keyboards.builders import models_choice_kb
from utils.localization import get_string 
router = Router()

@router.callback_query(F.data.startswith("select_model_"))
async def cb_select_model(callback: CallbackQuery):
    user = await get_user(callback.from_user.id)
    lang = user.language_code 
    model_name = callback.data.split("_")[-1]

    if user.selected_model == model_name:
        await callback.answer(get_string(lang, 'model_already_selected')) 
        return

    if user.current_tariff == "FREE" and model_name != "GPT-5":
        await callback.answer(
            get_string(lang, 'model_select_pro_alert'),
            show_alert=True
        )
        return

    await update_user(callback.from_user.id, selected_model=model_name)
    
    await callback.answer(
        get_string(lang, 'model_changed').format(model_name=model_name) 
    )
    
    await callback.message.edit_reply_markup(
        reply_markup=models_choice_kb(model_name, lang) 
    )