string_first = input('Введите первую строку:')
string_second = input('Введите вторую строку:')

def comparison(string_first, string_second):

    if string_first == string_second:
        return 1

    elif len(string_first) > len(string_second):
        return 2

    elif string_first != string_second and string_first == 'learn':
        return 3

result = comparison(string_first, string_second)
print(result)

