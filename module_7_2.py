info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

a = []
def custom_write(file_name, strings):     # file_name - название файла для записи, strings - список строк для записи
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(len(strings)):
        cursor_position = file.tell()
        file.write(strings[i])
        file.write('\n')
        a.append((i+1, cursor_position))
    file.close()
    b = dict(zip(a, strings))
    return b

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)