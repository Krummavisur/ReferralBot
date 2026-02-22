from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, Message

from keyboards import (
    admin_panel_keyboard,
    app_keyboard,
    live_keyboard,
    main_menu_keyboard,
    mirror_keyboard,
)
from state import MessageState

MIRROR_URL = "https://xf38lo22j1y0ihymst.com/B2mU"
APP_URL = "https://n37ztcmb.com/SPsU"
LIVE_URL = "https://imhzqqmb.com/live"

PROMO_TEXT = """Вводи промокод FREEMORS
при регистрации и получи 200% к депозиту

Промокод также действует для старых пользователей"""


class BotService:
    def __init__(self, bot: Bot, message_state: MessageState) -> None:
        self._bot = bot
        self._message_state = message_state

    async def _ensure_anchor(self, chat_id: int) -> None:
        if self._message_state.has_anchor(chat_id):
            return

        text = """Приветствую вас в Телеграм-боте сайта mostbet.com 👋

Как насчёт того, чтобы забрать фриспины по промокоду?
Нажмите на кнопку «Авторизоваться» и получите 200% к депозиту при первом пополнении."""

        sent = await self._bot.send_message(chat_id=chat_id, text=text)
        if sent and sent.message_id:
            self._message_state.save_anchor(chat_id, sent.message_id)

    async def _send_clean(
        self,
        chat_id: int,
        text: str,
        keyboard: InlineKeyboardMarkup | None = None,
    ) -> None:
        await self._ensure_anchor(chat_id)

        last_msg = self._message_state.get_last_message(chat_id)
        if last_msg:
            try:
                await self._bot.delete_message(chat_id=chat_id, message_id=last_msg)
            except Exception:
                pass

        sent = await self._bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=keyboard,
        )
        if sent and sent.message_id:
            self._message_state.save_message(chat_id, sent.message_id)

    async def send_welcome(self, chat_id: int) -> None:
        text = """Это официальный Telegram-бот Mostbet.
Используйте кнопки ниже для навигации."""
        await self._send_clean(chat_id, text, main_menu_keyboard())

    async def send_mirror(self, chat_id: int) -> None:
        text = f"""🔗 Актуальное зеркало:
{MIRROR_URL}"""
        await self._send_clean(chat_id, text, mirror_keyboard(MIRROR_URL))

    async def send_app(self, chat_id: int) -> None:
        text = f"""📲 Скачать приложение:
{APP_URL}"""
        await self._send_clean(chat_id, text, app_keyboard(APP_URL))

    async def send_live(self, chat_id: int) -> None:
        text = f"""🔴 Прямой эфир:
{LIVE_URL}"""
        await self._send_clean(chat_id, text, live_keyboard(LIVE_URL))

    async def send_promo(self, chat_id: int) -> None:
        await self._send_clean(chat_id, PROMO_TEXT, mirror_keyboard(MIRROR_URL))

    async def send_authorization(self, chat_id: int) -> None:
        await self._send_clean(chat_id, PROMO_TEXT, mirror_keyboard(MIRROR_URL))

    async def send_plain(self, chat_id: int, text: str) -> None:
        await self._send_clean(chat_id, text)

    async def send_admin_panel(self, chat_id: int) -> None:
        text = """⚙️ <b>Админ панель</b>

Выберите действие из меню ниже:"""
        await self._send_clean(chat_id, text, admin_panel_keyboard())

    async def send_admin_stats(self, chat_id: int) -> None:
        users = self._message_state.get_users()
        total_users = len(users)
        
        text = f"""📊 <b>Статистика бота</b>

👥 Всего пользователей: <b>{total_users}</b>
📨 Сообщений отправлено: <b>{len(self._message_state._last_bot_messages)}</b>
🔗 Активных сессий: <b>{len(self._message_state._anchor_messages)}</b>"""
        
        from keyboards import admin_panel_keyboard
        await self._send_clean(chat_id, text, admin_panel_keyboard())

    async def send_admin_users(self, chat_id: int) -> None:
        users = self._message_state.get_users()
        total_users = len(users)
        
        if total_users == 0:
            text = "👥 <b>Пользователи</b>\n\nПользователей пока нет."
        else:
            # Показываем первые 10 пользователей
            users_list = list(users)[:10]
            users_text = "\n".join([f"• <code>{user_id}</code>" for user_id in users_list])
            more_text = f"\n\n... и ещё {total_users - 10}" if total_users > 10 else ""
            
            text = f"""👥 <b>Пользователи</b>

Всего: <b>{total_users}</b>

Последние пользователи:
{users_text}{more_text}"""
        
        from keyboards import admin_panel_keyboard
        await self._send_clean(chat_id, text, admin_panel_keyboard())

    async def send_admin_broadcast_prompt(self, chat_id: int) -> None:
        text = """📢 <b>Рассылка</b>

Отправьте сообщение для рассылки всем пользователям.
Можно использовать форматирование (HTML).

Для отмены отправьте /admin"""
        
        from keyboards import admin_panel_keyboard
        await self._send_clean(chat_id, text, admin_panel_keyboard())
