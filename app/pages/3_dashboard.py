"""Личный кабинет. Доступен только авторизованным пользователям."""
import streamlit as st

from app.core.config import SITE_NAME
from app.ui.styles import inject_base_css

st.set_page_config(page_title=f"Кабинет — {SITE_NAME}", page_icon="👤", initial_sidebar_state="collapsed")
st.markdown(inject_base_css(), unsafe_allow_html=True)

user = st.session_state.get("user")
if not user:
    st.warning("Пожалуйста, войдите, чтобы открыть личный кабинет.")
    st.page_link("pages/1_login.py", label="Войти", icon="🔑")
    st.stop()

st.markdown('<div class="section-title">Личный кабинет</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="section-sub">Вы вошли как <b>{user["full_name"]}</b> ({user["email"]}).</div>',
    unsafe_allow_html=True,
)

st.info(
    "Здесь появится доступ к модулям курса, домашним заданиям и материалам. "
    "Пока это заглушка, подтверждающая, что авторизация и хранение данных работают."
)

if st.button("Выйти из аккаунта"):
    del st.session_state["user"]
    st.switch_page("Home.py")

st.page_link("Home.py", label="← Вернуться на главную", icon="🏠")
