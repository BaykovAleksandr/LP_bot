import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': 'settings.PROXY_URL',
    'urllib3_proxy_kwargs': {Settings.PROXY_USERNAME, Settings.PROXY_PASSWORD}}


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(Settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Бот стартовал!')
    mybot.start_polling()
    mybot.idle()
if __name__ == '__main__':
    main()
