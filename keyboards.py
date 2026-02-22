from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callbacks import (
    ADMIN_BACK,
    ADMIN_BROADCAST,
    ADMIN_PANEL,
    ADMIN_STATS,
    ADMIN_USERS,
    GET_AUTH,
    GET_APP,
    GET_LIVE,
    GET_MIRROR,
    GET_PROMO,
    MAIN_MENU,
)


def back_to_main() -> InlineKeyboardButton:
    return InlineKeyboardButton(text="🏠 На главную", callback_data=MAIN_MENU)


def url_button(text: str, url: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, url=url)


def callback_button(text: str, callback: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, callback_data=callback)


def mirror_keyboard(url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [back_to_main(), url_button("↗ Перейти", url)],
        ]
    )


def app_keyboard(url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [back_to_main(), url_button("📲 Скачать", url)],
        ]
    )


def live_keyboard(url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [back_to_main(), url_button("🔴 Смотреть", url)],
        ]
    )


def main_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [callback_button("🎰 Зеркало", GET_MIRROR)],
            [callback_button("📲 Приложение", GET_APP)],
            [callback_button("🔴 Лайв", GET_LIVE)],
            [callback_button("🎁 Промокоды", GET_PROMO)],
            [callback_button("🔑 Авторизация", GET_AUTH)],
        ]
    )


def admin_panel_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [callback_button("📊 Статистика", ADMIN_STATS)],
            [callback_button("👥 Пользователи", ADMIN_USERS)],
            [callback_button("📢 Рассылка", ADMIN_BROADCAST)],
        ]
    )
