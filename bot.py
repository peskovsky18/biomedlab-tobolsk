# -*- coding: utf-8 -*-
"""
Telegram Bot для запуска Mini App «БиоМедЛаб Тобольск: Навигатор возможностей»
Библиотека: aiogram 3.x
"""

import os
import sys
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
    MenuButtonWebApp
)

# Токен бота (из переменной окружения или захардкоженный для тестов)
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# URL развернутого веб-приложения (GitHub Pages)
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://peskovsky18.github.io/biomedlab-tobolsk/")

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message, bot: Bot):
    """
    Обработчик команды /start.
    Отправляет карточку с кнопкой запуска Telegram Mini App
    и автоматически настраивает системную кнопку меню MenuButton.
    """
    # Настраиваем кнопку меню в левом нижнем углу чата
    try:
        await bot.set_chat_menu_button(
            chat_id=message.chat.id,
            menu_button=MenuButtonWebApp(
                text="Навигатор 🔬",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        )
    except Exception as e:
        logging.warning(f"Не удалось установить MenuButton: {e}")

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Открыть Навигатор возможностей",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ],
            [
                InlineKeyboardButton(
                    text="📄 О кейсе Полины (Тобольск)",
                    callback_data="about_case"
                )
            ]
        ]
    )

    greeting_text = (
        "👋 <b>Добро пожаловать в проект профессионального сопровождения!</b>\n\n"
        "🎓 <b>Субъект:</b> Полина, 16 лет, 10 класс, г. Тобольск.\n"
        "🔬 <b>Профиль:</b> Химия и биология, интерес к исследованиям устройств мира.\n"
        "⚖️ <b>Ключевой вызов:</b> Семья настаивает на профессии врача, а Полина испытывает стресс в больнице.\n\n"
        "💡 <b>Решение:</b> Интерактивный навигатор компромиссных образовательных маршрутов "
        "(Медицинская биохимия, Биотехнологии, Гидроэкотоксикология в СИБУР).\n\n"
        "Нажмите кнопку ниже, чтобы запустить <b>Telegram Mini App</b> 👇"
    )

    await message.answer(greeting_text, parse_mode="HTML", reply_markup=kb)

@dp.callback_query(lambda c: c.data == "about_case")
async def cb_about_case(callback: types.CallbackQuery):
    text = (
        "📋 <b>Паспорт индивидуального кейса:</b>\n\n"
        "• <b>Локация:</b> Тюменская область, г. Тобольск\n"
        "• <b>Ситуация:</b> Родители готовы оплатить переезд только в медвуз. "
        "Полина скрывает интерес к биотеху и проводит опыты с водой дома.\n"
        "• <b>Приоритетный выбор:</b> <code>30.05.01 Медицинская биохимия</code> в ТюмГМУ (г. Тюмень). "
        "Диплом государственного медицинского университета дает статус врача, но работа проходит в стерильной лаборатории без пациентов!\n\n"
        "Нажмите кнопку <b>«Навигатор 🔬»</b> внизу экрана для старта."
    )
    await callback.message.answer(text, parse_mode="HTML")
    await callback.answer()

async def main():
    token = BOT_TOKEN
    if not token:
        print("\n" + "="*60)
        print("ВНИМАНИЕ: BOT_TOKEN не задан!")
        print("Укажите токен при запуске, например:")
        print("  export BOT_TOKEN='123456789:ABCdef...'")
        print("  python bot.py")
        print("Или введите токен прямо сейчас в консоль:")
        print("="*60 + "\n")
        try:
            token = input("Введите токен Telegram-бота от @BotFather (или Enter для выхода): ").strip()
        except EOFError:
            token = ""
        if not token:
            print("Токен не введен. Завершение работы.")
            return

    bot = Bot(token=token)
    print(f"\nБот успешно запущен! Привязанный WebApp URL: {WEBAPP_URL}")
    print("Откройте вашего бота в Telegram и отправьте команду /start\n")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
