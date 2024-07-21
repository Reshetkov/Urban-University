def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(1, 'строка', c = True)
print_params(1, 'строка')
print_params(1,2,3)
#print_params(a = 2, b, c) так нельзя
print_params(1, 2, c = False)
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [1, 'True', True]
values_dict = {'a': 2, 'b': [3,4], 'c': (5,6)}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = ['string', 5]
print_params(*values_list_2, 42)