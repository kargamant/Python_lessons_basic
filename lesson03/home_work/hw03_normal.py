__author__ = "Дериглазов Егор Дмитриевич"

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibbonachialgo (n,m):
    a = b = 1
    if n < 2:
        quit()
    print(a, end=' ')
    print(b, end=' ')
    for itm in range(n, m):
        a, b = b, a + b
        print(b, end=' ')

print(fibbonachialgo(2,20))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sortingnumbers (array):
    if len(array) > 1:
        indx = len(array) // 2
        small = []
        big = []

        for itm, val in enumerate(array):
            if itm != indx:
                if val < array[indx]:
                    small.append(val)
                else:
                    big.append(val)

        sortingnumbers(small)
        sortingnumbers(big)
        array[:] = small + [array[indx]] + big
    return array
array = [1,5,3,4,2]
print(sortingnumbers(array))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter (elements):
    for itm in elements:
        if itm is False:
            elements.remove(itm)
        else:
            pass
    return elements
print(my_filter([1,2,5,7,8,0,"string"]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def sqangles (x1,x2,x3,x4,y1,y2,y3,y4):
    if y1 == y4 and y2 == y3 and abs(x1 - x2) == abs(x3 - x4):
        return "Будут"
    else:
        return "не будут"
print(sqangles(5,2,9,6,3,5,5,3))
