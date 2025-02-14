import os
import time

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(os.getcwd(), file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, '
            f'Путь: {filepath}, '
            f'Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}')
