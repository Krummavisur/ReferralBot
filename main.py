import asyncio
import logging
import os

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN, BOT_USERNAME
from handlers import router
from bot_service import BotService
from state import MessageState

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main() -> None:
    token = BOT_TOKEN
    masked = token[: token.index(":") + 2] + "***" if len(token) > 8 and ":" in token else "***"
    logger.info("[ReferralBot] ===== INITIALIZATION START =====")
    logger.info("[ReferralBot] username=%s, token=%s", BOT_USERNAME, masked)

    bot = Bot(token=token)

    try:
        me = await bot.get_me()
        logger.info(
            "[ReferralBot] ✓ getMe() success: id=%s, username=%s, firstName=%s",
            me.id,
            me.username,
            me.first_name,
        )
    except Exception as e:
        logger.error("[ReferralBot] ✗ getMe() failed: %s", e, exc_info=True)

    logger.info("[ReferralBot] ===== INITIALIZATION COMPLETE =====")

    message_state = MessageState()
    bot_service = BotService(bot=bot, message_state=message_state)

    dp = Dispatcher(bot_service=bot_service)
    dp.include_router(router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
