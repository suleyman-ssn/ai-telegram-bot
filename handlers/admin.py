from aiogram import Router, F
from aiogram.filters import Command, Filter
from aiogram.types import Message
from typing import Union

from config import ADMIN_IDS
from database.db_manager import get_all_users_count, get_active_subs_count

class IsAdmin(Filter):
    async def __call__(self, message: Union[Message]) -> bool:
        return message.from_user.id in ADMIN_IDS

router = Router()
router.message.filter(IsAdmin()) 
@router.message(Command("admin"))
async def cmd_admin_panel(message: Message):
    await message.answer(
        "Добро пожаловать в Админ-панель:\n"
        "/stats - Статистика\n"
        "/sendall [текст] - Рассылка\n"
        "/set_tariff [user_id] [PRO/ULTRA/FREE] - Сменить тариф"
    )

@router.message(Command("stats"))
async def cmd_stats(message: Message):
    total_users = await get_all_users_count()
    active_subs = await get_active_subs_count()
    
    await message.answer(
        f"📊 Статистика:\n\n"
        f"Всего пользователей: {total_users}\n"
        f"Активных подписок (Pro/Ultra): {active_subs}"
    )

# TODO: Реализовать /sendall и /set_tariff 
# /sendall требует цикла по всем user_id из БД с обработкой ошибок
# /set_tariff требует парсинга аргументов и вызова update_user