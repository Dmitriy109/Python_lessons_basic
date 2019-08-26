# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
m = int(input('Введите m-элементов: '))
def fibonacci(n, m):
    num1 = num2 = i = 1
    F = []
    while i <= m:
        if i == 1:
            num3 = 1
        else:
            num3 = num1 + num2
        num1, num2 = num2, num3
        F.append(num3)
        i +=1
    return F
print(fibonacci(1, m))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    res_list = []
    while origin_list:
        num_min = min(origin_list)
        res_list.append(num_min)
        origin_list.pop(origin_list.index(num_min))
    return res_list

print(sort_to_max([2,10,-12,2.5,20,-11,4,4,0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

mixed =['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
new_mix = [itm for itm in mixed if itm == 'мак']
print(new_mix)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
from math import sqrt
def _paral(a,b,c,d):
    def length(A1, A2):
        return sqrt((A1[0] - A2[0])**2 + (A1[1] - A2[1])**2)

    AB = length(a,b)
    BC = length(b,c)
    CD = length(c, d)
    AD = length(a, d)
    if AB == BC and CD == AD:
        return ("Параллелограмм")
    else:
        return ("Не параллелограмм")
print(_paral((-2.3, 4), (8.5, 0.7), (5, 10), (3, 7)))


