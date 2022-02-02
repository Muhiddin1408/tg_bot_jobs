import os
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from aiogram.dispatcher import FSMContext

from loader import dp, bot


# Start State
@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    print('sd')

