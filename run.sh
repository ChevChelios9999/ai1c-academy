#!/usr/bin/env bash
# Быстрый запуск проекта локально: venv + зависимости + Streamlit.
set -e

cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
    echo "Создаю виртуальное окружение..."
    python3 -m venv .venv
fi

# shellcheck disable=SC1091
. .venv/bin/activate

echo "Устанавливаю зависимости..."
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt

if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "Создан .env из .env.example — при необходимости отредактируйте его."
fi

echo "Запускаю приложение на http://127.0.0.1:8501 ..."
streamlit run app/Home.py
