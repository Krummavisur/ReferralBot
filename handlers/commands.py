from aiogram import Bot, F, Router
from aiogram.types import Message
from config import ADMIN_ID

from bot_service import BotService

router = Router()


@router.message(F.text.in_(["/start", "На главную"]))
async def cmd_start(message: Message, bot: Bot, bot_service: BotService) -> None:
    await delete_user_message(message, bot)
    bot_service._message_state.add_user(message.chat.id)
    await bot_service.send_welcome(message.chat.id)


@router.message(F.text.in_(["/mirror", "Получить зеркало"]))
async def cmd_mirror(message: Message, bot: Bot, bot_service: BotService) -> None:
    await delete_user_message(message, bot)
    await bot_service.send_mirror(message.chat.id)


@router.message(F.text.in_(["/app", "Скачать приложение"]))
async def cmd_app(message: Message, bot: Bot, bot_service: BotService) -> None:
    await delete_user_message(message, bot)
    await bot_service.send_app(message.chat.id)


@router.message(F.text.in_(["/live", "Лайв"]))
async def cmd_live(message: Message, bot: Bot, bot_service: BotService) -> None:
    await delete_user_message(message, bot)
    await bot_service.send_live(message.chat.id)


@router.message(F.text.in_(["/auth", "Авторизация"]))
async def cmd_auth(message: Message, bot: Bot, bot_service: BotService) -> None:
    await delete_user_message(message, bot)
    await bot_service.send_authorization(message.chat.id)


@router.message(F.text.in_(["/promo", "Промокоды"]))
async def cmd_promo(message: Message, bot: Bot, bot_service: BotService) -> None:
    await delete_user_message(message, bot)
    await bot_service.send_promo(message.chat.id)


@router.message(F.text & ~F.text.startswith("/"))
async def unknown_command(message: Message, bot: Bot, bot_service: BotService) -> None:
    await delete_user_message(message, bot)
    await bot_service.send_plain(message.chat.id, "Нажмите кнопку из меню 👇")


async def delete_user_message(message: Message, bot: Bot) -> None:
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception:
        pass

@router.message(F.text == "/admin")
async def admin_panel(message: Message, bot: Bot, bot_service: BotService) -> None:
    if message.from_user.id not in ADMIN_ID:
        return

    await delete_user_message(message, bot)
    await bot_service.send_admin_panel(message.chat.id)

@router.message(F.text.startswith("/broadcast "))
async def admin_broadcast(message: Message, bot: Bot, bot_service: BotService) -> None:
    if message.from_user.id not in ADMIN_ID:
        return

    await delete_user_message(message, bot)
    
    text = message.text.replace("/broadcast ", "", 1)
    if not text:
        await bot_service.send_admin_broadcast_prompt(message.chat.id)
        return

    users = bot_service._message_state.get_users()
    sent = 0
    failed = 0

    for user_id in users:
        try:
            await bot.send_message(user_id, text, parse_mode="HTML")
            sent += 1
        except Exception:
            failed += 1

    result_text = f"""✅ <b>Рассылка завершена</b>

📤 Отправлено: <b>{sent}</b>
❌ Ошибок: <b>{failed}</b>
👥 Всего пользователей: <b>{len(users)}</b>"""
    
    await bot_service.send_plain(message.chat.id, result_text)

