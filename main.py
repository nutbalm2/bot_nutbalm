import telebot
from telebot import types

# Создание экземпляра бота
bot = telebot.TeleBot("6022394035:AAHv9dIZ758fDXQ-Z6f3T2scwi_2sLH80lE")  # Укажите ваш токен бота

# Обработка команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Опоздание')
    button2 = types.KeyboardButton('Не приду')
    button3 = types.KeyboardButton('Староста')
    button4 = types.KeyboardButton('Зам. старосты')
    button5 = types.KeyboardButton('Контакты')
    markup.add(button1, button2, button3, button4, button5)
    bot.reply_to(message, "Выберите раздел:", reply_markup=markup)

# Обработка кнопок разделов
@bot.message_handler(func=lambda message: True)
def handle_section_button(message):
    if message.text == 'Опоздание':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        button1 = types.KeyboardButton('8:00')
        button2 = types.KeyboardButton('8:30')
        button3 = types.KeyboardButton('9:00')
        button4 = types.KeyboardButton('9:30')
        markup.add(button1, button2, button3, button4)
        bot.reply_to(message, "Выберите время опоздания:", reply_markup=markup)
    elif message.text == 'Не приду':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        button1 = types.KeyboardButton('Болезнь')
        button2 = types.KeyboardButton('Семейные обстоятельства')
        button3 = types.KeyboardButton('Личные дела')
        button4 = types.KeyboardButton('Другая причина')
        markup.add(button1, button2, button3, button4)
        bot.reply_to(message, "Пожалуйста, укажите причину вашего отсутствия:", reply_markup=markup)
    elif message.text == 'Староста':
        bot.reply_to(message, "Вы выбрали раздел 'Староста'.")
    elif message.text == 'Зам. старосты':
        bot.reply_to(message, "Вы выбрали раздел 'Зам. старосты'.")
    elif message.text == 'Контакты':
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Ссылка на страницу", url="https://example.com")
        markup.add(button)
        bot.reply_to(message, "Вот ссылка на нашу страницу:", reply_markup=markup)

# Запуск бота
bot.polling()

import logging

import updater as updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler

# Устанавливаем уровень логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Создаем объект Bot
bot_token = '6022394035:AAHv9dIZ758fDXQ-Z6f3T2scwi_2sLH80lE'
import telegram
bot = telegram.Bot(token=bot_token)

# Инициализируем обновление
dispatcher = updater.dispatcher

# Определяем состояния разговора
FIRST, SECOND, THIRD = range(3)


def start(update, context):
    # Создаем кнопки
    keyboard = [
        [InlineKeyboardButton("Кнопка 1", callback_data=str(FIRST))],
        [InlineKeyboardButton("Кнопка 2", callback_data=str(SECOND))],
        [InlineKeyboardButton("Кнопка 3", callback_data=str(THIRD))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем приветственное сообщение с кнопками
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привет! Выбери одну из кнопок ниже:",
                             reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    choice = int(query.data)

    # Создаем новые кнопки в зависимости от выбранной кнопки
    if choice == FIRST:
        keyboard = [
            [InlineKeyboardButton("Кнопка 4", callback_data="4")],
            [InlineKeyboardButton("Кнопка 5", callback_data="5")],
            [InlineKeyboardButton("Кнопка 6", callback_data="6")]
        ]
    elif choice == SECOND:
        keyboard = [
            [InlineKeyboardButton("Кнопка 7", callback_data="7")],
            [InlineKeyboardButton("Кнопка 8", callback_data="8")],
            [InlineKeyboardButton("Кнопка 9", callback_data="9")]
        ]
    elif choice == THIRD:
        keyboard = [
            [InlineKeyboardButton("Кнопка 10", callback_data="10")],
            [InlineKeyboardButton("Кнопка 11", callback_data="11")],
            [InlineKeyboardButton("Кнопка 12", callback_data="12")]
        ]
    else:
        # В случае нажатия кнопки, которая не имеет новых кнопок, отправляем сообщение определенному пользователю
        context.bot.send_message(chat_id=update.effective_chat.id, text="Вы выбрали кнопку {}".format(choice))
        return

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Выбери одну из кнопок ниже:",
                             reply_markup=reply_markup)


# Регистрируем обработчики команд и кнопок
start_handler = CommandHandler('start', start)
button_handler = CallbackQueryHandler(button)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_handler)

# Запускаем бота
updater.start_polling(True)


