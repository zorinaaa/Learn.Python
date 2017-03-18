list = ['Вася','Маша','Петя','Валера']

i = 0
while i < len(list):
    if list.pop(i) == 'Валера':
        print('Валера нашелся!')
    