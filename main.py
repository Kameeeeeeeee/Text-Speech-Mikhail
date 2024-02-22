import logging
import os

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import database
import config
import markups as nav
import tts as t2os

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=config.tg_token)
dp = Dispatcher(bot, storage=storage)


class text_input(StatesGroup):
    text = State()


class voice_state(StatesGroup):
    voice = State()


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    database.add_user(message)
    await message.answer(config.messages['start'], reply_markup=nav.change_menu)


@dp.callback_query_handler(text='nachat')
async def nachat(callback: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback.from_user.id, config.messages['input'], reply_markup=nav.change_menu)
    await state.set_state(text_input.text)


@dp.message_handler(state=text_input.text)
async def tts(message: types.Message, state: FSMContext):
    await message.answer(config.messages['tts'][0])
    try:
        t2os.text_to_speech(database.get_provider(message), database.get_voice(message), message.text, message.chat.id)
        await bot.send_voice(message.chat.id, open(f'{message.chat.id}.wav', 'rb'))
        await message.answer(config.messages['tts'][1], reply_markup=nav.change_menu)
        os.remove(f'{message.chat.id}.wav')
    except:
        await message.answer(config.messages['tts'][2], reply_markup=nav.change_menu)
    await state.finish()


@dp.message_handler(state=voice_state.voice)
async def set_voice(message: types.Message, state: FSMContext):
    database.change_voice(message, message.text)
    await message.answer(config.messages['set_voice'], reply_markup=nav.change_menu)
    await state.finish()


@dp.message_handler()
async def mh(message: types.Message, state: FSMContext):
    if message.text == 'Готово':
        await message.answer(config.messages['ready'], reply_markup=nav.stmenu)

    elif message.text == 'Сменить провайдер':
        await message.answer(config.messages['change_provider'][0], reply_markup=nav.change_provider_menu)

    elif message.text == 'Microsoft' or message.text == 'LovoAI' or message.text == 'IBM' or \
         message.text == 'Amazon' or message.text == 'ElevanLabs' or message.text == 'Google':
        database.change_provider(message=message, provider=message.text)
        database.change_voice(message, config.default_voices[database.get_provider(message)])
        await message.answer(config.messages['change_provider'][1], reply_markup=nav.change_menu)

    elif message.text == 'Сменить голос':
        if database.get_provider(message) == 'microsoft':
            await message.answer(config.messages['change_voice'][0], reply_markup=nav.micorsoft_voices)
        elif database.get_provider(message) == 'lovoai':
            await message.answer(config.messages['change_voice'][0], reply_markup=nav.lovo_voices)
        elif database.get_provider(message) == 'ibm':
            await message.answer(config.messages['change_voice'][0], reply_markup=nav.ibm_voices)
        elif database.get_provider(message) == 'amazon':
            await message.answer(config.messages['change_voice'][0], reply_markup=nav.amazon_voices)
        elif database.get_provider(message) == 'elevanlabs':
            await message.answer(config.messages['change_voice'][0], reply_markup=nav.elevanlabs_voices)
        elif database.get_provider(message) == 'google':
            await message.answer(config.messages['change_voice'][0], reply_markup=nav.google_voices)
        await state.set_state(voice_state.voice)

    else:
        await message.answer(config.messages['error'], reply_markup=nav.change_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)