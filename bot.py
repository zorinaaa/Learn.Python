from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def greet_user(bot, update):
    print('Вызван /start')
    print('Вызван /help')
    print(update)
    bot.sendMessage(update.message.chat_id, text = 'Пообщаемся?')

def show_error(bot, update, error):
    print(error)

def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)

def main():
    updater = Updater('300303088:AAGtkjxU_MHJKLzhEdrlgPI33Ky8ifRuvZQ')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()
main()