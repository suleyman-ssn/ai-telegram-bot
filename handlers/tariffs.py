from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, PreCheckoutQuery, Message
from aiogram.types.successful_payment import SuccessfulPayment
from config import PRO_PRICE_STARS, ULTRA_PRICE_STARS
from utils.payment import process_successful_payment
from utils.localization import get_string
from database.db_manager import get_user

router = Router()

@router.callback_query(F.data.startswith("buy_tariff_"))
async def cb_buy_tariff(callback: CallbackQuery, bot: Bot):
    user = await get_user(callback.from_user.id) 
    lang = user.language_code 
    
    tariff = callback.data.split("_")[-1]
    
    price = 0
    title_key = ""
    if tariff == "PRO":
        price = PRO_PRICE_STARS
        title = "Pro"
    elif tariff == "UNLIMITED":
        price = ULTRA_PRICE_STARS
        title = "Unlimited"
    else:
        await callback.answer("Tariff not found", show_alert=True)
        return

    
    invoice_title = get_string(lang, 'tariff_invoice_title').format(tariff_name=title)
    invoice_desc = get_string(lang, 'tariff_invoice_desc').format(tariff_name=title)

    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title=invoice_title, 
        description=invoice_desc, 
        payload=f"monthly_subscription_{tariff}",
        provider_token="", 
        currency="XTR",
        prices=[{"label": "Подписка", "amount": price}],
    )
    await callback.answer()

@router.pre_checkout_query()
async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.pre_checkout_query_answer(pre_checkout_query.id, ok=True)

@router.message(F.successful_payment)
async def successful_payment_handler(message: Message):
    user = await get_user(message.from_user.id) 
    lang = user.language_code 
    
    payload = message.successful_payment.invoice_payload
    
    if payload.startswith("monthly_subscription_"):
        tariff = payload.split("_")[-1]
        
        await process_successful_payment(message.from_user.id, tariff)
        
        await message.answer(
            get_string(lang, 'tariff_success').format(tariff_name=tariff)
        )
