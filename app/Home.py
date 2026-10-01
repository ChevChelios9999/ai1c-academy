"""Лендинг курса «AI-агенты в 1С». Точка входа Streamlit-приложения."""
import streamlit as st

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.config import SITE_NAME, SITE_TAGLINE

from app.core.config import SITE_NAME, SITE_TAGLINE
from app.core.database import add_lead, init_db
from app.ui.components import (
    render_benefits,
    render_faq,
    render_footer,
    render_for_whom,
    render_hero,
    render_navbar,
    render_program,
    render_pricing,
    render_why_now,
)
from app.ui.styles import inject_base_css

st.set_page_config(
    page_title=SITE_NAME,
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

init_db()
st.markdown(inject_base_css(), unsafe_allow_html=True)

render_navbar()
render_hero()
render_why_now()
render_for_whom()
render_benefits()
render_program()
render_pricing()

# --- Форма заявки -----------------------------------------------------------
st.markdown('<div id="preorder" class="anchor-offset"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Оставить заявку</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="section-sub">{SITE_TAGLINE}. Оставьте контакты — '
    "пришлём подробности о ближайшем потоке.</div>",
    unsafe_allow_html=True,
)

with st.form("lead_form", clear_on_submit=True, border=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Имя")
    with col2:
        email = st.text_input("Email")
    message = st.text_area("Комментарий (необязательно)", height=90)
    submitted = st.form_submit_button("Отправить заявку")

if submitted:
    if not name.strip() or "@" not in email:
        st.error("Заполните имя и корректный email.")
    else:
        add_lead(name, email, message)
        st.success("Заявка отправлена! Мы свяжемся с вами по указанному email.")

render_faq()
render_footer()
