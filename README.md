# БиоМедЛаб Тобольск: Навигатор возможностей (Telegram Mini App)

Проект психолого-педагогического сопровождения обучающейся 10 класса (Полина, 16 лет, г. Тобольск).
Разработан в соответствии с регламентом аттестационной работы «Маршрут возможностей».

---

## 🚀 Как развернуть Telegram Mini App за 2 минуты

### Способ 1. Бесплатный хостинг на GitHub Pages
1. Создайте новый публичный репозиторий на [GitHub.com](https://github.com/new) (например, `biomedlab-tobolsk`).
2. Загрузите файлы репозитория:
   ```bash
   git remote add origin https://github.com/ВАШ_ЛОГИН/biomedlab-tobolsk.git
   git branch -M main
   git push -u origin main
   ```
3. В настройках репозитория на GitHub перейдите в **Settings → Pages** → в разделе **Branch** выберите `main` (папка `/root`) и нажмите **Save**.
4. Через 30 секунд появится готовая ссылка:
   `https://ВАШ_ЛОГИН.github.io/biomedlab-tobolsk/`

---

### Способ 2. Мгновенный деплой на Vercel
1. Зайдите на [vercel.com](https://vercel.com) под своим GitHub-аккаунтом.
2. Нажмите **Add New... → Project**, выберите репозиторий `biomedlab-tobolsk`.
3. Нажмите **Deploy** — через 10 секунд получите ссылку вида:
   `https://biomedlab-tobolsk.vercel.app`

---

## 🤖 Как подключить Mini App к вашему Telegram-боту

### Вариант А: Через официального бота @BotFather (без кода)
1. Откройте в Telegram бота **[@BotFather](https://t.me/BotFather)**.
2. Отправьте команду `/mybots` и выберите вашего бота (или создайте нового через `/newbot`).
3. Перейдите в: **Bot Settings → Menu Button → Configure menu button**.
4. Отправьте полученную ссылку на сайт (например: `https://ВАШ_ЛОГИН.github.io/biomedlab-tobolsk/`).
5. Напишите название кнопки, например: `Навигатор 🔬`.
6. Готово! Теперь в вашем боте внизу слева всегда будет активна кнопка открытия Mini App.

### Вариант Б: Запуск через готовый скрипт `bot.py`
1. Задайте токен вашего бота и адрес веб-приложения:
   ```bash
   export BOT_TOKEN="ВАШ_ТОКЕН_ОТ_BOTFATHER"
   export WEBAPP_URL="https://ВАШ_ЛОГИН.github.io/biomedlab-tobolsk/"
   ```
2. Запустите бота:
   ```bash
   python3 bot.py
   ```
3. Откройте бота в Telegram и отправьте `/start`.
