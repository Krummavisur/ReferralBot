from aiogram import Router

from .callbacks import router as callback_router
from .commands import router as command_router

router = Router()
router.include_router(command_router)
router.include_router(callback_router)
