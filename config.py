import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'

    # Telegram Bot Configuration
    TELEGRAM_TOKEN = "8148823820:AAGX7OjvLEIz6ZQXvQSyhWWHst_nafMT26s"
    TELEGRAM_CHAT_ID = "@ziyu07062002"
    TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"