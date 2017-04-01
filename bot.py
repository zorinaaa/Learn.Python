import operator
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#from cities.py import cities
#from answers.py import get_answer

def start(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text = 'Стартуем!')

def help(bot, update):
    print('Вызван /help')
    bot.sendMessage(update.message.chat_id, text = 'Бог тебе поможет!')

def about(bot, update):
    print('Вызван /about')
    bot.sendMessage(update.message.chat_id, text = 'Я - бот, который мало умеет, но много учится!')

def workcount(bot, update):
    print('Вызван /workcount')
    count = len(update.message.text.split())-1
    bot.sendMessage(update.message.chat_id, text = 'Количество введенных слов: {} '.format(count))
    if count == 0:
        bot.sendMessage(update.message.chat_id, text = 'Вы ничего не ввели!')

def get_answer(question):
    answers = {  
        'Привет': 'И тебе привет!',
        'Как дела?': 'Лучше всех', 
        'Пока': 'Увидимся' 
    }
    return answers.get(question, 'Не понимаю тебя!')

def count_it(bot, update):
    text = update.message.text
    text = text[9:]

    actions = {
        '-': operator.sub,
        '+': operator.add,
        '*': operator.mul,
        '/': operator.truediv,
    }
"""
    for action_sign in actions:
        if action_sign in text:
            action = action_sign

    if action == '/' and text.split(action)[1] == '0':
        result = 'На ноль делить нелья'
    else:
        result = actions[action](
            int(text.split(action)[0]),
            int(text.split(action)[1]),
        )

"""
    if '-' in text:
        a, b = text.split('-')
        result = a - b
    elif '+' in text:
        a, b = text.split('+')
        result = a + b
    elif '*' in text:
        a, b = text.split('*')
        result = a * b
    elif '/' in text:
        a, b = text.split('/')
        result = a / b

    bot.sendMessage(update.message.chat_id, text=result)




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