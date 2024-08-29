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









  # def custom_write(file_name, strings):  # file_name - название файла для записи, strings - список строк для записи
  #     file = open(file_name, 'wb')
  #     print(file.tell())
  #     pickle.dump(strings, file)
  #     print(file.tell())
  #     for i in range(1, len(strings) + 1):
  #         print(file.tell())
  #         c.append((i, file.tell()))
  #
  #     file.close()
  #     file = open(file_name, 'rb')
  #     t1 = pickle.load(file)
  #     file.close()
  #
  #     b = dict(zip(c, t1))
  #     return b
