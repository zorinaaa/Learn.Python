answers = {  
        'Привет': 'И тебе привет!',
        'Как дела?': 'Лучше всех', 
        'Пока': 'Увидимся' 
}

def get_answer(question, answers):    
    return answers.get(question)


def ask_user(answers):
    while True:
        user_input = input('Скажи что-нибудь:')
        answer = get_answer(user_input, answers)
        print(answer)

    if user_input == 'Пока':
        break
    

if __name__ == '__main__':
    ask_user(answers)




