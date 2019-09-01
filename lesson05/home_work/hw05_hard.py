# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
import os
import sys
import shutil

print('sys.argv = ', sys.argv)

def print_help():
    print("\n\thelp - получение справки\n"
          "\tmkdir <dir_name> - создание директории\n"
          "\tcp <file_name> - создает копию указанного файла\n"
          "\trm <file_name> - удаляет указанный файл (запросить подтверждение операции)\n"
          "\tcd <full_path or relative_path> - меняет текущую директорию на указанную\n"
          "\tls - отображение полного пути текущей директории\n")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def cp_file():
    if not dir_name:
        print("Необходимо указать имя файла который вы хотите скопировать: ")
        return
    dir_join = os.path.join(os.getcwd(), dir_name)
    dir_join2 = os.path.join(os.getcwd(), _org)
    try:
        shutil.copy2(dir_join, dir_join2)
        print('файл {} скопирован'.format(dir_name))
    except FileNotFoundError:
        print('файд {} с таким именем уже существует'.format(dir_name))

def del_file():
    if not dir_name:
        print("Необходимо указать имя файла который вы хотите удалить: ")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.remove(dir_path)
        print('файл {} удалён'.format(dir_name))
    except FileNotFoundError:
        print('файл {} не найден'.format(dir_name))

def dir_ls():
    print('Полный путь к текущей директории: ' + os.path.join(os.getcwd()))

def dir_cd():
    if not dir_name:
        print("Необходимо ввести директорию для перехода: ")
        return
    try:
        os.chdir(dir_name)
        print('вы перешли в директорию {}'.format(os.getcwd()))

    except FileNotFoundError:
        print('директория {} не найдена'.format(dir_name))

do = {
    "help": print_help,
    "mkdir": make_dir,
    'cp' : cp_file,
    'rm': del_file,
    'cd': dir_cd,
    'ls': dir_ls
}

try:
    _org = sys.argv[3]
except IndexError:
    _org = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")