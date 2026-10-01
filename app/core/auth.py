"""
Авторизация пользователей.

Пароли никогда не хранятся в открытом виде — используется bcrypt
(соль генерируется автоматически на каждый пароль).
"""
import re
import sqlite3
from dataclasses import dataclass

import bcrypt

from app.core.config import MIN_PASSWORD_LENGTH
from app.core.database import get_connection, get_cursor, now_iso

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class AuthError(Exception):
    """Ошибка регистрации/входа, безопасная для показа пользователю."""


@dataclass
class User:
    id: int
    email: str
    full_name: str


def _validate_email(email: str) -> str:
    email = email.strip().lower()
    if not EMAIL_RE.match(email):
        raise AuthError("Введите корректный email.")
    return email


def _validate_password(password: str) -> None:
    if len(password) < MIN_PASSWORD_LENGTH:
        raise AuthError(f"Пароль должен быть не короче {MIN_PASSWORD_LENGTH} символов.")


def register_user(email: str, full_name: str, password: str, password_confirm: str) -> User:
    """Регистрирует нового пользователя. Бросает AuthError при некорректных данных."""
    email = _validate_email(email)
    full_name = full_name.strip()

    if not full_name:
        raise AuthError("Укажите имя.")
    if password != password_confirm:
        raise AuthError("Пароли не совпадают.")
    _validate_password(password)

    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    with get_cursor() as cur:
        try:
            cur.execute(
                "INSERT INTO users (email, full_name, password_hash, created_at) "
                "VALUES (?, ?, ?, ?)",
                (email, full_name, password_hash, now_iso()),
            )
        except sqlite3.IntegrityError as exc:
            raise AuthError("Пользователь с таким email уже зарегистрирован.") from exc
        user_id = cur.lastrowid

    return User(id=user_id, email=email, full_name=full_name)


def authenticate_user(email: str, password: str) -> User:
    """Проверяет email/пароль. Бросает AuthError, если вход не удался."""
    email = email.strip().lower()

    conn = get_connection()
    try:
        row = conn.execute(
            "SELECT id, email, full_name, password_hash FROM users WHERE email = ?",
            (email,),
        ).fetchone()
    finally:
        conn.close()

    generic_error = "Неверный email или пароль."
    if row is None:
        raise AuthError(generic_error)
    if not bcrypt.checkpw(password.encode("utf-8"), row["password_hash"].encode("utf-8")):
        raise AuthError(generic_error)

    return User(id=row["id"], email=row["email"], full_name=row["full_name"])
