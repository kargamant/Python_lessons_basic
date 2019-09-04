__author__ = "Дериглазов Егор Дмитриевич"

import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangle:
    #подразумеваю, что в point значение будет передано в таком формате (x,y)
    def __init__(self, f, t, p):
        self.f = f
        self.t = t
        self.p = p
        def length(point1,point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
        self.ft = length(self.f, self.t)
        self.tp = length(self.t, self.p)
        self.fp = length(self.f, self.p)
    def triangleyardage (self):
        p =(self.ft + self.tp + self.fp)/2
        return math.sqrt(p*(p-self.fp) * (p-self.ft) * (p-self.tp))
    def triangleperimetr (self):
        return (self.ft + self.tp + self.fp)
    def hight (self):
        return self.triangleyardage() / (self.ft / 2)
tringle = triangle((3, 2), (6, 7), (0, 12))
print(tringle.triangleperimetr())
print(tringle.triangleyardage())
print(tringle.hight())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trapezium:
    def __init__(self, N, U, M, B):
        self.N = N
        self.U = U
        self.M = M
        self.B = B
        def slength(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
        self.NU = slength(self.N,self.U)
        self.NM = slength(self.N,self.M)
        self.NB = slength(self.N,self.B)
        self.UM = slength(self.U,self.M)
        self.UB = slength(self.U,self.B)
        self.MB = slength(self.M,self.B)
        self.diagonal_nm = slength(self.N, self.M)
        self.diagonal_ub = slength(self.U,self.B)
        def trapeziumperimetr (self):
            return (self.MB + self.UB + self.UM + self.NB + self.NM + self.NU)

        self.area = triangle.triangleyardage(self.UM, self.diagonal_nm, self.NU) \
                    + triangle.triangleyardage(self.diagonal_ub, self.NB, self.MB)
        def trapeziumyardage(self):
            return self.area

        def trapeziumtrue (self):
            if self.diagonal_nm == self.diagonal_ub:
                return True
            else:
                return False
