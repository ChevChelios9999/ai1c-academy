"""Страница регистрации нового пользователя."""
import streamlit as st

from app.core.auth import AuthError, register_user
from app.core.config import SITE_NAME
from app.ui.styles import inject_base_css

st.set_page_config(page_title=f"Регистрация — {SITE_NAME}", page_icon="✍️", initial_sidebar_state="collapsed")
st.markdown(inject_base_css(), unsafe_allow_html=True)

if st.session_state.get("user"):
    st.switch_page("pages/3_dashboard.py")

st.markdown('<div class="section-title">Регистрация</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-sub">Создайте аккаунт, чтобы получить доступ к личному кабинету курса.</div>',
    unsafe_allow_html=True,
)

with st.form("register_form", border=True):
    full_name = st.text_input("Имя")
    email = st.text_input("Email")
    password = st.text_input("Пароль", type="password", help="Не короче 6 символов")
    password_confirm = st.text_input("Повторите пароль", type="password")
    submitted = st.form_submit_button("Зарегистрироваться")

if submitted:
    try:
        user = register_user(email, full_name, password, password_confirm)
    except AuthError as exc:
        st.error(str(exc))
    else:
        st.session_state["user"] = {"id": user.id, "email": user.email, "full_name": user.full_name}
        st.success("Регистрация выполнена!")
        st.switch_page("pages/3_dashboard.py")

st.page_link("pages/1_login.py", label="Уже есть аккаунт? Войти", icon="🔑")
st.page_link("Home.py", label="← Вернуться на главную", icon="🏠")
