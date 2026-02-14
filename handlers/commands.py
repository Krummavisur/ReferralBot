from aiogram import Bot, F, Router
from aiogram.types import Message

from bot_service import BotService

router = Router()


@router.message(F.text.in_(["/start", "На главную"]))
async def cmd_start(message: Message, bot: Bot, bot_service: BotService) -> None:
    await delete_user_message(message, bot)
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


@router.message(F.text)
async def unknown_command(message: Message, bot: Bot, bot_service: BotService) -> None:
    await delete_user_message(message, bot)
    await bot_service.send_plain(message.chat.id, "Нажмите кнопку из меню 👇")


async def delete_user_message(message: Message, bot: Bot) -> None:
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception:
        pass
