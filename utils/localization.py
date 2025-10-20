# utils/localization.py

STRINGS = {
    'ru': {
        'welcome': (
            "👋 Привет, {first_name}!\n\n"
            "Я — ваш персональный ИИ-ассистент.\n"
            "🔹 Вы можете общаться со мной в этом чате.\n"
            "🔹 В меню '⚙️ Модель' можно сменить мою 'личность'.\n"
            "🔹 На тарифе Free у вас {limit} сообщений в день.\n"
            
        ),
        'start_chat_prompt': "Я вас слушаю. Какой у вас вопрос?",
        'select_language': "Пожалуйста, выберите ваш язык:",
        'language_selected': "✅ Язык изменен.\n\n",
        
        'main_menu_chat': "💬 Начать чат",
        'main_menu_model': "⚙️ Модель",
        'main_menu_tariffs': "💎 Тарифы",
        'main_menu_profile': "👤 Профиль",
        
        'model_select_prompt': "Выберите 'модель', которая будет вам отвечать.\n\nЭто изменит мой стиль общения.",
        'model_select_pro_alert': "Эта модель доступна только на Pro/Ultra тарифе.",
        'model_changed': "Модель изменена на {model_name}",
        'model_already_selected': "Эта модель уже выбрана.",
        
        'tariffs_prompt': "Выберите подходящий тариф для снятия ограничений.\nОплата происходит через Telegram Stars."
                            "💎 PRO - Расширенный доступ ко всем моделям\n"
                            "🔓 Unlimited - Неограниченный доступ ко всем моделям",
        'tariff_pro_button': "Pro - {price} Stars",
        'tariff_ultra_button': "Unlimited - {price} Stars",
        'tariff_invoice_title': "Тариф {tariff_name} (30 дней)",
        'tariff_invoice_desc': "Активация тарифа '{tariff_name}' на 30 дней.",
        'tariff_success': "🎉 Оплата прошла успешно!\n\nВам активирован тариф **{tariff_name}** на 30 дней.",
        
        'profile_title': "👤 Ваш профиль:",
        'profile_name': "Имя",
        'profile_id': "ID",
        'profile_tariff': "Тариф",
        'profile_limit_free': "Остаток сообщений: {count}",
        'profile_limit_paid': "Тариф активен до: {date}",
        'profile_limit_never': "Никогда",
        'profile_renew_button': "🔄 Продлить тариф",
        'profile_clear_history': "🧹 Очистить историю",
        'history_cleared': "История диалога очищена!",
        
        'limit_exceeded': (
            "Ваш дневной лимит ({limit} сообщений) исчерпан. 😕\n"
            "Чтобы продолжить общение без ограничений, выберите платный тариф."
        )
    },
    'en': {
        'welcome': (
            "👋 Hi, {first_name}!\n\n"
            "I am your personal AI assistant.\n"
            "🔹 You can chat with me here.\n"
            "🔹 In the '⚙️ Model' menu, you can change my 'personality'.\n"
            "🔹 On the Free plan, you have {limit} messages per day.\n"
            
        ),
        'start_chat_prompt': "I'm listening. What is your question?",
        'select_language': "Please select your language:",
        'language_selected': "✅ Language changed.\n\n",

        'main_menu_chat': "💬 Start Chat",
        'main_menu_model': "⚙️ Model",
        'main_menu_tariffs': "💎 Tariffs",
        'main_menu_profile': "👤 Profile",

        'model_select_prompt': "Choose the 'model' that will respond to you.\n\nThis will change my communication style.",
        'model_select_pro_alert': "This model is only available on the Pro/Ultra plan.",
        'model_changed': "Model changed to {model_name}",
        'model_already_selected': "This model is already selected.",

        'tariffs_prompt': "Choose a suitable plan to remove restrictions.\nPayment is via Telegram Stars."
                            "💎 PRO - Extended access to all models\n"
                            "🔓 Unlimited - Unlimited access to all models",
        'tariff_pro_button': "Pro - {price} Stars",
        'tariff_ultra_button': "Unlimitet - {price} Stars",
        'tariff_invoice_title': "Plan {tariff_name} (30 days)",
        'tariff_invoice_desc': "Activation of '{tariff_name}' plan for 30 days.",
        'tariff_success': "🎉 Payment successful!\n\nYou have activated the **{tariff_name}** plan for 30 days.",
        
        'profile_title': "👤 Your Profile:",
        'profile_name': "Name",
        'profile_id': "ID",
        'profile_tariff': "Plan",
        'profile_limit_free': "Messages remaining: {count}",
        'profile_limit_paid': "Plan active until: {date}",
        'profile_limit_never': "Never",
        'profile_renew_button': "🔄 Renew Plan",
        'profile_clear_history': "🧹 Clear History",
        'history_cleared': "Chat history cleared!",

        'limit_exceeded': (
            "Your daily limit ({limit} messages) is exhausted. 😕\n"
            "To continue chatting without limits, please choose a paid plan."
        )
    },
    'es': {
        'welcome': (
            "👋 ¡Hola, {first_name}!\n\n"
            "Soy tu asistente personal de IA.\n"
            "🔹 Puedes chatear conmigo aquí.\n"
            "🔹 En el menú '⚙️ Modelo', puedes cambiar mi 'personalidad'.\n"
            "🔹 En el plan Gratuito, tienes {limit} mensajes al día.\n"

        ),
        'start_chat_prompt': "Te escucho. ¿Cuál es tu pregunta?",
        'select_language': "Por favor, selecciona tu idioma:",
        'language_selected': "✅ Idioma cambiado.\n\n",
        
        'main_menu_chat': "💬 Iniciar Chat",
        'main_menu_model': "⚙️ Modelo",
        'main_menu_tariffs': "💎 Tarifas",
        'main_menu_profile': "👤 Perfil",

        'model_select_prompt': "Elige el 'modelo' que te responderá.\n\nEsto cambiará mi estilo de comunicación.",
        'model_select_pro_alert': "Este modelo solo está disponible en el plan Pro/Ultra.",
        'model_changed': "Modelo cambiado a {model_name}",
        'model_already_selected': "Este modelo ya está seleccionado.",
        
        'tariffs_prompt': "Elige un plan adecuado para eliminar las restricciones.\nEl pago se realiza mediante Telegram Stars."
                            "💎 PRO - Acceso ampliado a todos los modelos\n"
                            "🔓 Unlimited Acceso ilimitado a todos los modelos",
        'tariff_pro_button': "Pro - {price} Stars",
        'tariff_ultra_button': "Unlimited - {price} Stars",
        'tariff_invoice_title': "Plan {tariff_name} (30 días)",
        'tariff_invoice_desc': "Activación del plan '{tariff_name}' por 30 días.",
        'tariff_success': "🎉 ¡Pago exitoso!\n\nHas activado el plan **{tariff_name}** por 30 días.",
        
        'profile_title': "👤 Tu Perfil:",
        'profile_name': "Nombre",
        'profile_id': "ID",
        'profile_tariff': "Plan",
        'profile_limit_free': "Mensajes restantes: {count}",
        'profile_limit_paid': "Plan activo hasta: {date}",
        'profile_limit_never': "Nunca",
        'profile_renew_button': "🔄 Renovar Plan",
        'profile_clear_history': "🧹 Limpiar Historial",
        'history_cleared': "¡Historial de chat limpiado!",

        'limit_exceeded': (
            "Tu límite diario ({limit} mensajes) se ha agotado. 😕\n"
            "Para seguir chateando sin límites, elige un plan de pago."
        )
    }
}

def get_string(lang_code: str, key: str) -> str:
    """
    Получает строку перевода по ключу и коду языка.
    Фоллбэк на 'en', если 'ru' или 'es' не найдены, 
    и на 'en', если ключ не найден в 'ru'.
    """
    if lang_code not in STRINGS:
        lang_code = 'en' 
        
    lang_strings = STRINGS.get(lang_code)
    
    return lang_strings.get(key, STRINGS['en'].get(key, f"_{key}_"))