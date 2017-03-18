from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text = 'Стартуем!')

def help(bot, update):
    print('Вызван /help')
    bot.sendMessage(update.message.chat_id, text = 'Бог тебе поможет!')

def about(bot, update):
    print('Вызван /about')
    bot.sendMessage(update.message.chat_id, text = 'Я - бот, который мало умеет, но много учится!')

def get_answer(question):
    answers={  
        'Привет': 'И тебе привет!',
        'Как дела?': 'Лучше всех', 
        'Пока': 'Увидимся' 
        }
    return answers.get(question,'Не понимаю тебя!')

def talk_to_me(bot, update):
    answer = get_answer(update.message.text)
    print(answer)
    bot.sendMessage(update.message.chat_id,answer)

def show_error(bot, update, error):
    print(error)

def main():
    updater = Updater('300303088:AAGtkjxU_MHJKLzhEdrlgPI33Ky8ifRuvZQ')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('about', about))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()