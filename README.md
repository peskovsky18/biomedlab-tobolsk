# БиоМедЛаб Тобольск: Навигатор возможностей (Telegram Mini App)

Проект психолого-педагогического сопровождения обучающейся 10 класса (Полина, 16 лет, г. Тобольск).
Разработан в соответствии с регламентом аттестационной работы «Маршрут возможностей».

🔗 **Готовый URL приложения (GitHub Pages):**  
`https://peskovsky18.github.io/biomedlab-tobolsk/`

---

## 🚀 Как включить GitHub Pages в репозитории (1 минута)
1. Откройте настройки репозитория: [https://github.com/peskovsky18/biomedlab-tobolsk/settings/pages](https://github.com/peskovsky18/biomedlab-tobolsk/settings/pages).
2. В разделе **Build and deployment → Branch**:
   * Выберите ветку: `main`
   * Папку: `/ (root)`
   * Нажмите **Save**.
3. Через 30–60 секунд сайт будет доступен по адресу:  
   `https://peskovsky18.github.io/biomedlab-tobolsk/`

---

## 🤖 Как привязать Mini App к Telegram-боту

### Вариант 1: Через бота @BotFather (без программирования)
1. Откройте в Telegram бота **[@BotFather](https://t.me/BotFather)**.
2. Отправьте `/mybots` и выберите вашего бота.
3. Нажмите: **Bot Settings → Menu Button → Configure menu button**.
4. Вставьте адрес:  
   `https://peskovsky18.github.io/biomedlab-tobolsk/`
5. Введите название кнопки: `Навигатор 🔬`.
6. Готово! В чате с ботом появится постоянная кнопка внизу слева.

### Вариант 2: Запуск готового бота bot.py
```bash
export BOT_TOKEN="ВАШ_ТОКЕН_ОТ_BOTFATHER"
python3 bot.py
```
