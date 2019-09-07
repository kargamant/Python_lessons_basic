__author__ = "Дериглазов Егор Дмитриевич"

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class pupil:
    teachers_list = []
    subjects = []
    form = None
    def __init__(self, fio, form, father, mother):
        self.fio = fio
        self.form = form
        self.father = father
        self.mother = mother
    def pupilinfo(self):
        print(f'Имя ученика: {self.fio}\nкласс: {self.form}\nимя отца: {self.father}\nимя матери: {self.mother}\n')
    def subjects (self):
        return self.subjects
    def add_subjects(self):
        self.subjects.append(subject)
    def teachers(self):
        return self.teachers
    def add_teacher(self):
        self.teachers_list.append(teacher.fio)
        teacher.pupils_list.append(self)
class teacher:
    forms = []
    pupils_list = []
    teachers = []
    def __init__(self, fio):
        self.fio = fio
        self.subject = subject
    def teacherinfo(self):
        print(f'Имя учителя: {self.fio}\nпредмет: {self.subject}\n')
    def forms(self):
        return self.forms
    def add_forms(self):
        self.forms.append(form)
        form.teachers.append(self)
    def pupils(self):
        return self.pupils
    def add_pupil(self):
        self.pupils.append(pupil)
        pupil.teachers.append(self)
class subject:
    def __init__(self):
        self.name
class form:
    teachers  = []
    pupils = []
    def __init__(self,name):
        self.name = name
    @property
    def teachers(self):
        return self.teachers
    def add_teacher(self):
        self.teachers.append(teacher)
        teacher.forms.append(self)
    @property
    def pupils(self):
        return self.pupils
    def add_pupil(self):
        self.pupils.append(pupil)
        pupil.form = self.name
class school:
    forms_list = []
    teachers_list = []
    pupils_list = []
    def __init__(self, number):
        self.number = number
    @property
    def forms(self):
        return self.forms_list
    def add_form(self):
        self.forms_list.append(form)
    @property
    def pupils(self):
        return self.pupils_list

    def add_pupil(self):
        self.pupils_list.append(pupil)
        pupil.form = self.name
    @property
    def teachers(self):
        return self.teachers_list
    def add_teacher(self):
        self.teachers_list.append(teacher)
        teacher.forms.append(self)
teacher.fio = 'Порфирий Иванович'
