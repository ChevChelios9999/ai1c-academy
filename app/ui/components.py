"""Блоки разметки лендинга. Каждая функция рендерит один смысловой раздел."""
import streamlit as st

from app.core.config import SITE_NAME


def render_navbar() -> None:
    st.markdown(
        f"""
        <div class="navbar">
            <a class="logo" href="#top">{SITE_NAME.split(" ")[0]}<span>.1C</span></a>
            <div class="navlinks">
                <a href="#about">О курсе</a>
                <a href="#program">Программа</a>
                <a href="#pricing">Тарифы</a>
                <a href="#faq">Вопросы</a>
            </div>
        </div>
        <div id="top"></div>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns([6, 1, 1])
    with cols[1]:
        st.page_link("pages/1_login.py", label="Войти", icon="🔑")
    with cols[2]:
        st.page_link("pages/2_register.py", label="Начать", icon="🚀")


def render_hero() -> None:
    st.markdown(
        """
        <span class="badge">🤖 Новый практический курс · набор открыт</span>
        <div class="hero-title">
            Учим 1С-разработчиков<br>
            работать с <span class="accent">ИИ-агентами</span>
        </div>
        <div class="hero-sub">
            Практический курс о том, как встроить языковые модели и AI-агентов
            (Cursor, Claude Code и другие) в повседневную разработку на платформе
            1С:Предприятие — от первого промпта до собственных инструментов
            автоматизации.
        </div>
        """,
        unsafe_allow_html=True,
    )
    c1, c2, c3 = st.columns([1.1, 1.3, 3])
    with c1:
        st.page_link("pages/2_register.py", label="Оставить заявку", icon="✍️")
    with c2:
        st.markdown('<a href="#program" style="text-decoration:none;">'
                     '<div style="padding:0.55rem 1.2rem;border:1px solid var(--border);'
                     'border-radius:10px;color:var(--text);font-weight:600;text-align:center;">'
                     'Программа курса</div></a>', unsafe_allow_html=True)
    st.markdown("<div style='height:36px'></div>", unsafe_allow_html=True)


def _card(icon: str, title: str, text: str) -> str:
    return f"""
    <div class="card">
        <div class="icon">{icon}</div>
        <h4>{title}</h4>
        <p>{text}</p>
    </div>
    """


def render_why_now() -> None:
    st.markdown('<div id="about" class="anchor-offset"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Почему это стоит освоить сейчас</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Разработчики, которые уже умеют делегировать рутину '
        'ИИ-агентам, решают типовые задачи 1С в разы быстрее — и получают больше времени '
        'на архитектуру и сложные кейсы.</div>',
        unsafe_allow_html=True,
    )
    cols = st.columns(3)
    cards = [
        ("🛠️", "Практика на реальных задачах",
         "Никаких абстрактных примеров — только рабочие кейсы 1С-разработчика, "
         "которые можно сразу применить в своих проектах."),
        ("🧭", "Фундаментальные принципы",
         "Разбираемся, как устроены языковые модели и агенты, чтобы навык оставался "
         "актуальным при смене конкретных инструментов."),
        ("📦", "Модульная структура",
         "Короткие уроки с чёткой целью: разобрали тему — сразу применили на практике, "
         "без многочасовых марафонов."),
    ]
    for col, (icon, title, text) in zip(cols, cards):
        with col:
            st.markdown(_card(icon, title, text), unsafe_allow_html=True)
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)


def render_for_whom() -> None:
    st.markdown('<div class="section-title">Кому подойдёт курс</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Материал рассчитан на практикующих специалистов 1С '
        'с разным уровнем знакомства с ИИ.</div>',
        unsafe_allow_html=True,
    )
    items = [
        ("👨‍💻", "1С-разработчики", "Хотите ускорить рутинные задачи и высвободить время на архитектуру."),
        ("🧪", "Уже пробуете ИИ", "Хотите систематизировать разрозненные приёмы в понятный процесс."),
        ("🌱", "Только начинаете с ИИ", "Хотите сразу получить рабочую карту действий без месяцев проб и ошибок."),
        ("🧑‍🏫", "Тимлиды", "Хотите внедрить практики ИИ-разработки во всей команде, а не только у энтузиастов."),
    ]
    cols = st.columns(4)
    for col, (icon, title, text) in zip(cols, items):
        with col:
            st.markdown(_card(icon, title, text), unsafe_allow_html=True)
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)


def render_benefits() -> None:
    st.markdown('<div class="section-title">Что вы получите</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Конкретные навыки, применимые в работе с первой недели.</div>',
        unsafe_allow_html=True,
    )
    benefits = [
        ("Уверенная работа с LLM", "Понимание принципов работы моделей и навык формулировать запросы так, "
                                    "чтобы получать нужный результат с первого раза."),
        ("Настроенный AI-стек", "Практика работы в AI-редакторах и с CLI-агентами применительно к задачам 1С."),
        ("Промпт- и контекст-инжиниринг", "Подготовка контекста конфигурации 1С для моделей: вручную и через "
                                          "автоматизированные инструменты."),
        ("MCP-инструменты под свои задачи", "Базовые принципы подключения внешних инструментов к моделям "
                                             "и идеи для собственных интеграций с базой 1С."),
    ]
    html = "".join(
        f"""<div class="checkline"><div class="tick">✓</div>
            <div><b>{title}</b><span class="desc">{text}</span></div></div>"""
        for title, text in benefits
    )
    st.markdown(f'<div class="card">{html}</div>', unsafe_allow_html=True)
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)


def render_program() -> None:
    st.markdown('<div id="program" class="anchor-offset"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Программа курса</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Модули открываются постепенно — на практику '
        'остаётся достаточно времени.</div>',
        unsafe_allow_html=True,
    )
    modules = [
        ("Модуль 1. Основы работы с языковыми моделями",
         "Что такое LLM и как они устроены. Первые практические задачи 1С прямо в чате с моделью."),
        ("Модуль 2. Инструменты AI-разработки",
         "Установка и настройка AI-редакторов и CLI-агентов, подготовка рабочего окружения."),
        ("Модуль 3. Рабочий процесс разработчика",
         "Структура файлов конфигурации, версионирование и связка «Конфигуратор + AI-инструменты»."),
        ("Модуль 4. Промпт-инжиниринг",
         "Анатомия рабочего промпта, шаблоны и приёмы под типовые задачи 1С-разработки."),
        ("Модуль 5. Контекст и MCP",
         "Формирование контекста конфигурации для модели вручную и через MCP-серверы."),
        ("Модуль 6. AI-driven разработка",
         "ИИ на всех этапах задачи: анализ требований, проектирование, реализация и проверка."),
    ]
    for title, text in modules:
        with st.expander(title):
            st.write(text)
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)


def render_pricing() -> None:
    st.markdown('<div id="pricing" class="anchor-offset"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Тарифы</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Все материалы курса доступны на любом тарифе — '
        'различается только формат поддержки.</div>',
        unsafe_allow_html=True,
    )
    tiers = [
        ("Базовый", "от 19 900 ₽", False,
         ["Все видеоуроки курса", "Практические задания", "Доступ к материалам навсегда", "Чат студентов"]),
        ("Стандарт", "от 34 900 ₽", True,
         ["Всё из тарифа «Базовый»", "Проверка домашних заданий куратором",
          "Разбор работ в формате видео", "Именной сертификат"]),
        ("Премиум", "от 69 900 ₽", False,
         ["Всё из тарифа «Стандарт»", "Индивидуальные консультации",
          "Code review кода, написанного с ИИ", "Сопровождение месяц после курса"]),
    ]
    cols = st.columns(3)
    for col, (name, price, featured, items) in zip(cols, tiers):
        with col:
            klass = "price-card featured" if featured else "price-card"
            badge = '<div class="price-tag">Рекомендуем</div>' if featured else '<div class="price-tag">&nbsp;</div>'
            items_html = "".join(f"<li>✓ {i}</li>" for i in items)
            st.markdown(
                f"""<div class="{klass}">
                    {badge}
                    <h4 style="margin:2px 0 0 0;">{name}</h4>
                    <div class="price-amount">{price}</div>
                    <ul class="price-list">{items_html}</ul>
                </div>""",
                unsafe_allow_html=True,
            )
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)


def render_faq() -> None:
    st.markdown('<div id="faq" class="anchor-offset"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Частые вопросы</div>', unsafe_allow_html=True)
    faq = [
        ("Нужен ли опыт работы с ИИ?",
         "Нет. Курс начинается с базовых понятий и постепенно переходит к продвинутым техникам."),
        ("Какой уровень 1С нужен?",
         "Курс рассчитан на практикующих 1С-разработчиков — знания платформы на уровне решения типовых задач."),
        ("Нужно ли переходить на 1С:EDT?",
         "Нет, примеры построены вокруг связки «Конфигуратор + AI-редактор». Материал легко адаптировать под EDT."),
        ("Остаётся ли доступ к материалам после окончания?",
         "Да, доступ к материалам и их обновлениям сохраняется без ограничения по времени."),
    ]
    for q, a in faq:
        with st.expander(q):
            st.write(a)
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)


def render_footer() -> None:
    st.markdown(
        f"""
        <div class="footer">
            {SITE_NAME} · Практический курс по ИИ-агентам для 1С-разработчиков<br>
            Есть вопросы — напишите нам, форма заявки выше.
        </div>
        """,
        unsafe_allow_html=True,
    )
