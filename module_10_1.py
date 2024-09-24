import time                                         # Импорты необходимых модулей и функций
from threading import Thread
from datetime import datetime
from time import sleep

def write_words(word_count, file_name):              # Объявление функции write_words
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(1, word_count + 1):
        file.write(f'Какое-то слово № {i} \n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    file.close()

time_start_1 = datetime.now()                         # Взятие текущего времени

write_words_1 = write_words(10, 'example1.txt')   # Запуск функций с аргументами из задачи
write_words_2 = write_words(30, 'example2.txt')
write_words_3 = write_words(200, 'example3.txt')
write_words_4 = write_words(100, 'example4.txt')

time_end_1 = datetime.now()                           # Взятие текущего времени
time_res_1 = time_end_1 - time_start_1
print(f'Работа потоков {time_res_1}')                 # Вывод разницы начала и конца работы функций

time_start_2 = datetime.now()                         # Взятие текущего времени

write_words_first = Thread(target= write_words, args= (10, 'example5.txt'))
write_words_second = Thread(target= write_words, args= (30, 'example6.txt'))
write_words_third = Thread(target= write_words, args= (200, 'example7.txt'))
write_words_fourth = Thread(target= write_words, args= (100, 'example8.txt'))

write_words_first.start()
write_words_second.start()
write_words_third.start()
write_words_fourth.start()

write_words_first.join()
write_words_second.join()
write_words_third.join()
write_words_fourth.join()

time_end_2 = datetime.now()                             # Взятие текущего времени
time_res_2 = time_end_2 - time_start_2
print(f'Работа потоков {time_res_2}')                   # Вывод разницы начала и конца работы потоков