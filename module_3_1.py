calls = 0
my_list = []


def count_calls(x):
    x += 1
    return x


def string_info(x):
    global calls
    calls = count_calls(calls)
    y = (len(x), x.upper(), x.lower())
    return y


def is_contains(string, list_to_search):
    global calls
    calls = count_calls(calls)
    string = string.lower()
    n = len(list_to_search)
    for i in list_to_search:
        if string in i:
            x = True
            break
        else:
            x = False
    return x



def f_list(z):
    global my_list
    for i in range(z):
        print('Введите элемент ', i+1)
        d = input('Вашего списка: ').lower()
        my_list.append(d)
    return my_list

string_1 = input('Для того, чтобы узнать, находится ли строка в списке, введите строку: ').lower()
number = int(input('Сколько элементов будет содержать Ваш список?: '))
my_list = f_list(number)
string_2 = input('Для того, чтобы узнать информацию о строке, введите строку: ')
info_1 = is_contains(string_1, my_list)
info_2 = string_info(string_2)
print(info_2)
print(info_1)
print(calls)