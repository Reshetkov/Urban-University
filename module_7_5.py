import os
import time

os.chdir(r'D:\PythonProject\Urban\directory')
for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
  #      filepath = os.path.abspath(file)
        filesize = os.path.getsize(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = root
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')