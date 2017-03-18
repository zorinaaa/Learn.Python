age = input('Введите ваш возраст:')
age = int(age)

def age_comp(age):
    if age >= 3 and age <= 6:
        print('Дай угадаю, ты учишься в детском саду.')

    elif age >=7 and age <= 17:
        print('Ты сто пудово школьник.')

    elif age >=18 and age <=21:
        print('Я надеюсь ты учишься в ВУЗе')

    elif age >=22 and age <=55:
        print('Ты должно быть где-то работаешь')
        
    else:
        print('Наверно ты уже на пенсии')

result = age_comp(age)
print(result)