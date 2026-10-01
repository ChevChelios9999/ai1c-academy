"""Инъекция CSS для оформления лендинга поверх стандартных виджетов Streamlit."""

CSS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
:root {
    --bg: #0b0f19;
    --bg-soft: #121826;
    --card: #161d2e;
    --border: #232b3d;
    --text: #e6e9f2;
    --muted: #9aa4b8;
    --accent: #7c5cff;
    --accent-2: #35d0ba;
    --gradient: linear-gradient(135deg, #7c5cff 0%, #4f7bff 55%, #35d0ba 100%);
}

html, body, [class*="css"] {
    font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: var(--bg);
    color: var(--text);
}

/* Скрываем служебные элементы Streamlit для вида полноценного лендинга */
#MainMenu, footer, header[data-testid="stHeader"] {
    visibility: hidden;
    height: 0;
}
[data-testid="stSidebarNav"] { display: none; }
[data-testid="stSidebar"] { display: none; }
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1120px;
}

/* ---------- Навигация ---------- */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 8px;
}
.navbar .logo {
    font-weight: 800;
    font-size: 1.15rem;
    color: var(--text);
    text-decoration: none;
}
.navbar .logo span { color: var(--accent-2); }
.navlinks { display: flex; gap: 22px; }
.navlinks a {
    color: var(--muted);
    text-decoration: none;
    font-size: 0.92rem;
    font-weight: 500;
}
.navlinks a:hover { color: var(--text); }

/* ---------- Бейдж / хиро ---------- */
.badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 999px;
    background: rgba(124, 92, 255, 0.12);
    border: 1px solid rgba(124, 92, 255, 0.35);
    color: #b9a9ff;
    font-size: 0.82rem;
    font-weight: 600;
    margin-bottom: 18px;
}
.hero-title {
    font-size: 2.7rem;
    font-weight: 800;
    line-height: 1.15;
    margin: 0 0 16px 0;
    letter-spacing: -0.02em;
}
.hero-title .accent {
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-sub {
    font-size: 1.12rem;
    color: var(--muted);
    max-width: 640px;
    margin-bottom: 28px;
    line-height: 1.6;
}

/* ---------- Секции ---------- */
.section-title {
    font-size: 1.9rem;
    font-weight: 800;
    margin-top: 0.4rem;
    margin-bottom: 0.35rem;
    letter-spacing: -0.01em;
}
.section-sub {
    color: var(--muted);
    margin-bottom: 1.6rem;
    font-size: 1rem;
}
.anchor-offset { position: relative; top: -70px; }

/* ---------- Карточки ---------- */
.card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 22px;
    height: 100%;
}
.card h4 {
    margin: 10px 0 8px 0;
    font-size: 1.05rem;
    font-weight: 700;
}
.card p {
    color: var(--muted);
    font-size: 0.92rem;
    line-height: 1.55;
    margin: 0;
}
.card .icon { font-size: 1.6rem; }

.checkline {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    padding: 14px 0;
    border-bottom: 1px solid var(--border);
}
.checkline:last-child { border-bottom: none; }
.checkline .tick {
    color: var(--accent-2);
    font-weight: 800;
    font-size: 1.05rem;
}
.checkline b { display: block; margin-bottom: 3px; }
.checkline span.desc { color: var(--muted); font-size: 0.92rem; }

/* ---------- Тарифы ---------- */
.price-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 26px;
    height: 100%;
}
.price-card.featured {
    border: 1px solid var(--accent);
    box-shadow: 0 0 0 1px rgba(124,92,255,0.25), 0 12px 30px -12px rgba(124,92,255,0.35);
}
.price-tag {
    font-size: 0.78rem;
    font-weight: 700;
    color: var(--accent-2);
    text-transform: uppercase;
    letter-spacing: 0.04em;
}
.price-amount {
    font-size: 2rem;
    font-weight: 800;
    margin: 6px 0 14px 0;
}
.price-list { list-style: none; padding: 0; margin: 0; }
.price-list li {
    color: var(--muted);
    font-size: 0.9rem;
    padding: 6px 0;
}

/* ---------- Футер ---------- */
.footer {
    border-top: 1px solid var(--border);
    margin-top: 3rem;
    padding-top: 22px;
    color: var(--muted);
    font-size: 0.85rem;
    text-align: center;
}

/* ---------- Кнопки Streamlit ---------- */
div.stButton > button, div.stFormSubmitButton > button {
    background: var(--gradient);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.55rem 1.2rem;
    font-weight: 700;
}
div.stButton > button:hover, div.stFormSubmitButton > button:hover {
    filter: brightness(1.08);
    color: white;
}
a[data-testid="stPageLink-NavLink"] {
    color: var(--muted) !important;
}

/* Поля ввода */
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {
    background: var(--bg-soft) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
}
</style>
"""


def inject_base_css() -> str:
    return CSS
