"""
Юнит-тесты для core/auth.py и core/database.py.

Запуск:  pytest -q
Тесты используют временную БД (не трогают app/data/app.db).
"""
import importlib
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


@pytest.fixture()
def fresh_db(tmp_path, monkeypatch):
    """Подменяет DB_PATH на временный файл перед каждым тестом."""
    db_file = tmp_path / "test.db"
    monkeypatch.setenv("DB_PATH", str(db_file))

    # Модули читают DB_PATH при импорте — перезагружаем их для чистоты теста.
    for name in ("app.core.config", "app.core.database", "app.core.auth"):
        sys.modules.pop(name, None)

    config = importlib.import_module("app.core.config")
    monkeypatch.setattr(config, "DB_PATH", db_file, raising=False)
    database = importlib.import_module("app.core.database")
    monkeypatch.setattr(database, "DB_PATH", db_file, raising=False)
    auth = importlib.import_module("app.core.auth")

    database.init_db()
    return auth, database


def test_register_and_authenticate(fresh_db):
    auth, _ = fresh_db
    user = auth.register_user("Test@Example.com", "Тестовый Пользователь", "secret1", "secret1")
    assert user.email == "test@example.com"

    logged_in = auth.authenticate_user("test@example.com", "secret1")
    assert logged_in.full_name == "Тестовый Пользователь"


def test_duplicate_email_rejected(fresh_db):
    auth, _ = fresh_db
    auth.register_user("dup@example.com", "Первый", "secret1", "secret1")
    with pytest.raises(auth.AuthError):
        auth.register_user("dup@example.com", "Второй", "secret2", "secret2")


def test_wrong_password_rejected(fresh_db):
    auth, _ = fresh_db
    auth.register_user("user@example.com", "Пользователь", "secret1", "secret1")
    with pytest.raises(auth.AuthError):
        auth.authenticate_user("user@example.com", "wrong-password")


def test_password_mismatch_rejected(fresh_db):
    auth, _ = fresh_db
    with pytest.raises(auth.AuthError):
        auth.register_user("user2@example.com", "Пользователь", "secret1", "secret2")


def test_short_password_rejected(fresh_db):
    auth, _ = fresh_db
    with pytest.raises(auth.AuthError):
        auth.register_user("user3@example.com", "Пользователь", "123", "123")


def test_add_lead(fresh_db):
    _, database = fresh_db
    database.add_lead("Пётр", "petr@example.com", "хочу на курс")
    conn = database.get_connection()
    row = conn.execute("SELECT * FROM leads WHERE email = ?", ("petr@example.com",)).fetchone()
    conn.close()
    assert row is not None
    assert row["name"] == "Пётр"
