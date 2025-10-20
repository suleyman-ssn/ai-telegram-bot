from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, update, delete
from sqlalchemy import func
import datetime

from database.models import Base, User
from config import DB_URL, ADMIN_IDS

engine = create_async_engine(DB_URL)
AsyncSessionFactory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    """Инициализация БД и создание таблиц."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with AsyncSessionFactory() as session:
        for admin_id in ADMIN_IDS:
            admin_user = await session.get(User, admin_id)
            if admin_user:
                admin_user.is_admin = True
            else:
                admin_user = User(user_id=admin_id, is_admin=True, current_tariff="ULTRA")
                session.add(admin_user)
        await session.commit()

async def get_or_create_user(user_id: int, username: str = None, first_name: str = None) -> User:
    """Получает или создает пользователя в БД."""
    async with AsyncSessionFactory() as session:
        user = await session.get(User, user_id)
        if not user:
            user = User(
                user_id=user_id, 
                username=username, 
                first_name=first_name,
                is_admin=(user_id in ADMIN_IDS)
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user

async def get_user(user_id: int) -> User | None:
    async with AsyncSessionFactory() as session:
        return await session.get(User, user_id)

async def update_user(user_id: int, **kwargs):
    """Обновляет данные пользователя."""
    async with AsyncSessionFactory() as session:
        stmt = update(User).where(User.user_id == user_id).values(**kwargs)
        await session.execute(stmt)
        await session.commit()


async def check_and_update_limits(user: User) -> bool:
    """
    Проверяет лимиты. 
    Возвращает True, если лимит исчерпан, иначе False.
    """
    if user.current_tariff != "FREE":
        return False

    today = datetime.datetime.utcnow().date()
    last_msg_date = user.last_message_date.date()

    if today > last_msg_date:
        await update_user(user.user_id, message_count=1, last_message_date=func.now())
        return False
    
    if user.message_count >= 10:
        return True 

    await update_user(user.user_id, message_count=user.message_count + 1)
    return False

async def get_chat_context(user_id: int) -> list:
    user = await get_user(user_id)
    return user.chat_context if user else []

async def update_chat_context(user_id: int, new_message: dict, max_context_size=10):
    """Добавляет сообщение в контекст и обрезает его."""
    current_context = await get_chat_context(user_id)
    current_context.append(new_message)
    
    if len(current_context) > max_context_size:
        current_context = current_context[-max_context_size:]
        
    await update_user(user_id, chat_context=current_context)

async def clear_chat_context(user_id: int):
    await update_user(user_id, chat_context=[])

async def get_all_users_count() -> int:
    async with AsyncSessionFactory() as session:
        result = await session.execute(select(func.count(User.user_id)))
        return result.scalar_one()

async def get_active_subs_count() -> int:
    async with AsyncSessionFactory() as session:
        result = await session.execute(
            select(func.count(User.user_id)).where(
                User.current_tariff != "FREE",
                User.tariff_expires_at > func.now()
            )
        )
        return result.scalar_one()