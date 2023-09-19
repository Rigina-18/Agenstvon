import os
import django
from telegram.ext import Updater, CommandHandler

updater = Updater(token='6662913180:AAGeMktuOvjdE5rbDS8f-T_oUW8ag11QFDI', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a bot!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
