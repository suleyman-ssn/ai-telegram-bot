
import datetime
from database.db_manager import update_user

async def process_successful_payment(user_id: int, tariff: str):
    """Активирует тариф пользователю после успешной оплаты."""
    
    expires_date = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    
    await update_user(
        user_id, 
        current_tariff=tariff,
        tariff_expires_at=expires_date
    )
    print(f"Тариф {tariff} активирован для {user_id} до {expires_date}")