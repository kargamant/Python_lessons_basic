__author__ = "Деригазов Егор Дмитриевич"
import os
import shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def creatingdirs(num):
    namenumber = 1
    for itm in range (num):
        name = 'dir_' + str(namenumber)
        os.mkdir(name, mode=0o777, dir_fd=None)
        namenumber += 1
def deletingdirs(num):
    namenumber = 1
    for itm in range(num):
        name = 'dir_' + str(namenumber)
        os.remove(name)
        namenumber += 1
print(creatingdirs(9))
print(deletingdirs(9))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print(os.listdir(os.getcwd()))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

shutil.copy(os.getcwd(),'PycharmProjects\PyEducation')
