from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot_service import BotService
from callbacks import (
    GET_APP,
    GET_AUTH,
    GET_LIVE,
    GET_MIRROR,
    GET_PROMO,
    MAIN_MENU,
)

router = Router()


@router.callback_query(F.data == MAIN_MENU)
async def cb_main_menu(callback: CallbackQuery, bot_service: BotService) -> None:
    if callback.message and callback.message.chat:
        await bot_service.send_welcome(callback.message.chat.id)
    await callback.answer()


@router.callback_query(F.data == GET_MIRROR)
async def cb_get_mirror(callback: CallbackQuery, bot_service: BotService) -> None:
    if callback.message and callback.message.chat:
        await bot_service.send_mirror(callback.message.chat.id)
    await callback.answer()


@router.callback_query(F.data == GET_APP)
async def cb_get_app(callback: CallbackQuery, bot_service: BotService) -> None:
    if callback.message and callback.message.chat:
        await bot_service.send_app(callback.message.chat.id)
    await callback.answer()


@router.callback_query(F.data == GET_LIVE)
async def cb_get_live(callback: CallbackQuery, bot_service: BotService) -> None:
    if callback.message and callback.message.chat:
        await bot_service.send_live(callback.message.chat.id)
    await callback.answer()


@router.callback_query(F.data == GET_PROMO)
async def cb_get_promo(callback: CallbackQuery, bot_service: BotService) -> None:
    if callback.message and callback.message.chat:
        await bot_service.send_promo(callback.message.chat.id)
    await callback.answer()


@router.callback_query(F.data == GET_AUTH)
async def cb_get_auth(callback: CallbackQuery, bot_service: BotService) -> None:
    if callback.message and callback.message.chat:
        await bot_service.send_authorization(callback.message.chat.id)
    await callback.answer()
