import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import webmoney


# Настройки бота
TOKEN = "YOUR_TELEGRAM_TOKEN"
WEBMONEY_PURSE = "YOUR_WEBMONEY_PURSE"
SECRET_KEY = "YOUR_SECRET_KEY"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Клавиатура с выбором валюты платежа
currency_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
currency_keyboard.add(KeyboardButton("WMR"))
currency_keyboard.add(KeyboardButton("WMZ"))

# Класс для состояний FSM
class PaymentStates(StatesGroup):
    waiting_for_currency = State()
    waiting_for_amount = State()
    waiting_for_purse = State()

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("Добро пожаловать! Для создания платежа выберите валюту:", reply_markup=currency_keyboard)
    await PaymentStates.waiting_for_currency.set()

# Обработчик выбора валюты платежа
@dp.message_handler(filters=Text(equals=["WMR", "WMZ"]), state=PaymentStates.waiting_for_currency)
async def choose_currency_handler(message: types.Message, state: FSMContext):
    currency = message.text
    await state.update_data(currency=currency)
    await message.reply("Введите сумму платежа:")
    await PaymentStates.waiting_for_amount.set()

# Обработчик ввода суммы платежа
@dp.message_handler(state=PaymentStates.waiting_for_amount)
async def enter_amount_handler(message: types.Message, state: FSMContext):
    amount = message.text
    await state.update_data(amount=amount)
    await message.reply("Введите номер вашего WebMoney кошелька:")
    await PaymentStates.waiting_for_purse.set()

# Обработчик ввода номера кошелька
@dp.message_handler(state=PaymentStates.waiting_for_purse)
async def enter_purse_handler(message: types.Message, state: FSMContext):
    purse = message.text
    await state.update_data(purse=purse)
    await message.reply("Ваш платеж принят. Ожидайте дальнейших инструкций.")

    # Создание платежа через WebMoney
    data = await state.get_data()
    currency = data.get("currency")
    amount = data.get("amount")
    wm = webmoney.WebMoney(SECRET_KEY)
    wm_response = wm.transfer_purse_to_purse(
        purse_from=WEBMONEY_PURSE,
        purse_to=purse,
        amount=amount,
        currency=currency,
        desc=f"Payment from Telegram Bot"
    )

    if wm_response.response_code == 0:
        await message.reply("Платеж успешно отправлен.")
    else:
        await message.reply("Произошла ошибка при отправке платежа.")

    # Сброс состояния FSM
    await state.reset_state()

# Обработчик ошибочного ввода
@dp.message_handler()
async def unknown_message_handler(message: types.Message):
    await message.reply("Ошибка. Воспользуйтесь командой /start для начала.")

# Запуск бота
if __name__ == "__main__":
    dp.middleware.setup(LoggingMiddleware())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dp.start_polling())