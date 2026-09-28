"""Страница входа в личный кабинет."""
import streamlit as st

from app.core.auth import AuthError, authenticate_user
from app.core.config import SITE_NAME
from app.ui.styles import inject_base_css

st.set_page_config(page_title=f"Вход — {SITE_NAME}", page_icon="🔑", initial_sidebar_state="collapsed")
st.markdown(inject_base_css(), unsafe_allow_html=True)

if st.session_state.get("user"):
    st.switch_page("pages/3_dashboard.py")

st.markdown('<div class="section-title">Вход в личный кабинет</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Ещё нет аккаунта?</div>', unsafe_allow_html=True)
st.page_link("pages/2_register.py", label="Зарегистрироваться", icon="✍️")

with st.form("login_form", border=True):
    email = st.text_input("Email")
    password = st.text_input("Пароль", type="password")
    submitted = st.form_submit_button("Войти")

if submitted:
    try:
        user = authenticate_user(email, password)
    except AuthError as exc:
        st.error(str(exc))
    else:
        st.session_state["user"] = {"id": user.id, "email": user.email, "full_name": user.full_name}
        st.success(f"Добро пожаловать, {user.full_name}!")
        st.switch_page("pages/3_dashboard.py")

st.page_link("Home.py", label="← Вернуться на главную", icon="🏠")
