# Развёртывание за Apache 2.4 (reverse-proxy)

Streamlit — это отдельный сервер (не WSGI/CGI-приложение), поэтому Apache
здесь не запускает Python напрямую, а работает перед ним как обратный
прокси. Схема: `Браузер → Apache (порт 80/443) → Streamlit (127.0.0.1:8501)`.

## 1. Запустите Streamlit как фоновый процесс

```bash
cd ai1c-academy
. .venv/bin/activate
streamlit run app/Home.py
```

Приложение слушает `127.0.0.1:8501` (см. `.streamlit/config.toml`).
Для постоянной работы оформите это как службу (см. ниже — пример systemd).

## 2. Debian/Ubuntu (Apache через apt)

```bash
sudo a2enmod proxy proxy_http proxy_wstunnel rewrite headers
sudo cp deploy/apache/ai1c-academy.conf /etc/apache2/sites-available/ai1c-academy.conf
sudo a2ensite ai1c-academy.conf
sudo apache2ctl configtest
sudo systemctl reload apache2
```

Добавьте в `/etc/hosts` (для локальной проверки без реального домена):

```
127.0.0.1 ai1c-academy.local
```

Откройте `http://ai1c-academy.local/` в браузере.

## 3. Windows (Apache24, например из XAMPP)

1. В `conf/httpd.conf` раскомментируйте строки:
   ```
   LoadModule proxy_module modules/mod_proxy.so
   LoadModule proxy_http_module modules/mod_proxy_http.so
   LoadModule proxy_wstunnel_module modules/mod_proxy_wstunnel.so
   LoadModule rewrite_module modules/mod_rewrite.so
   LoadModule headers_module modules/mod_headers.so
   ```
2. Подключите конфиг виртуального хоста (в конец `httpd.conf` или через `Include`):
   ```
   Include conf/extra/ai1c-academy.conf
   ```
   и положите `deploy/apache/ai1c-academy.conf` в `conf/extra/`.
3. Добавьте в `C:\Windows\System32\drivers\etc\hosts`:
   ```
   127.0.0.1 ai1c-academy.local
   ```
4. Перезапустите Apache через панель управления/`httpd.exe -k restart`.
5. Запустите `run.bat`, затем откройте `http://ai1c-academy.local/`.

## 4. Автозапуск Streamlit как службы (Linux, systemd) — опционально

```ini
# /etc/systemd/system/ai1c-academy.service
[Unit]
Description=AI1C Academy (Streamlit)
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/ai1c-academy
ExecStart=/path/to/ai1c-academy/.venv/bin/streamlit run app/Home.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now ai1c-academy
```

## 5. При переходе на реальный хостинг

- Смените `ServerName` на реальный домен, добавьте `<VirtualHost *:443>` с
  SSL-сертификатом (Let's Encrypt/certbot).
- Убедитесь, что порт `8501` не открыт наружу напрямую — доступ только
  через Apache (Streamlit слушает `127.0.0.1`, что уже это обеспечивает).
- Смените `SECRET_KEY` в `.env` на случайную строку.
