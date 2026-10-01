"""
Слой доступа к данным.

Хранилище — SQLite (файл app/data/app.db). Для лендинга и MVP этого
достаточно: не требует отдельного сервера БД, файл легко бэкапить,
при росте проекта миграция на PostgreSQL/MySQL потребует только
переписать этот модуль (остальной код работает через функции ниже
и напрямую с sqlite3 не взаимодействует).
"""
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Iterator

from app.core.config import DB_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    email         TEXT UNIQUE NOT NULL,
    full_name     TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    created_at    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS leads (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL,
    email      TEXT NOT NULL,
    message    TEXT,
    created_at TEXT NOT NULL
);
"""


def get_connection() -> sqlite3.Connection:
    """Открывает соединение с БД, создавая каталог данных при необходимости."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


@contextmanager
def get_cursor() -> Iterator[sqlite3.Cursor]:
    """Контекстный менеджер: соединение + автоматический commit/close."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        yield cur
        conn.commit()
    finally:
        conn.close()


def init_db() -> None:
    """Создаёт таблицы, если их ещё нет. Безопасно вызывать при каждом запуске."""
    with get_cursor() as cur:
        cur.executescript(SCHEMA)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def add_lead(name: str, email: str, message: str = "") -> None:
    with get_cursor() as cur:
        cur.execute(
            "INSERT INTO leads (name, email, message, created_at) VALUES (?, ?, ?, ?)",
            (name.strip(), email.strip().lower(), message.strip(), now_iso()),
        )
