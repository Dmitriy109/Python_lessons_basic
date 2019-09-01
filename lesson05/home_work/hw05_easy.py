# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil

def save_dir(name):
   os.mkdir(name)

[save_dir('dir_' + str(itm)) for itm in range(1,10)]

def del_dir(name):
    os.rmdir(name)

[del_dir('dir_' + str(itm)) for itm in range(1,10)]

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    pat = os.listdir()
    return print(pat)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
__file__ = 'hw05_easy.py'
shutil.copy2(__file__, 'fail.py')