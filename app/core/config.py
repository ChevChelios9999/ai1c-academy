"""
Общая конфигурация приложения.

Значения читаются из переменных окружения (.env в корне проекта).
Если .env отсутствует — используются безопасные значения по умолчанию,
достаточные для локального запуска.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
APP_DIR = BASE_DIR / "app"

load_dotenv(BASE_DIR / ".env")

# --- Общие настройки сайта -------------------------------------------------
SITE_NAME = os.getenv("SITE_NAME", "AI-Агенты в 1С")
SITE_TAGLINE = os.getenv(
    "SITE_TAGLINE",
    "Практический курс по использованию ИИ-агентов в разработке на 1С:Предприятие",
)

# --- Хранилище ---------------------------------------------------------------
DATA_DIR = Path(os.getenv("DATA_DIR", APP_DIR / "data"))
DB_PATH = Path(os.getenv("DB_PATH", DATA_DIR / "app.db"))

# --- Безопасность --------------------------------------------------------
# Используется как "соль" для дополнительных операций (не для хранения паролей —
# пароли всегда хешируются через bcrypt, см. core/auth.py).
SECRET_KEY = os.getenv("SECRET_KEY", "dev-insecure-secret-change-me")

MIN_PASSWORD_LENGTH = 6
