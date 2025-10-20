from sqlalchemy import create_engine, Column, Integer, String, BigInteger, DateTime, JSON, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    
    language_code = Column(String(2), default="ru")
    
    current_tariff = Column(String, default="FREE")
    tariff_expires_at = Column(DateTime, nullable=True)
    
    message_count = Column(Integer, default=0)
    last_message_date = Column(DateTime, default=func.now())
    
    selected_model = Column(String, default="GPT-5")
    chat_context = Column(JSON, default=[])
    
    user_prefs = Column(JSON, nullable=True) 
    is_admin = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=func.now())