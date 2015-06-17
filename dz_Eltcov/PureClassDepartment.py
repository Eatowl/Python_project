#!/usr/bin/python
# -*- coding: utf-8 -*-

class Person:
    
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def raise_pay(self, percent):
        self.pay = int(self.pay * (1 + percent/100))

    def __str__(self):
        # return '[Person: %s, %s]' % (self.name, self.pay)
        # улучшаем вывод занных о пользователе:
        return '[%s: %s, %s]' % (self.__class__.__name__, self.name, self.pay)



class Manager(Person):
    def raise_pay(self, percent, bonus=10):
        # self.pay = int(self.pay * (1 + (percent + bonus)/100))
        # Правильнее будет вызвать оригинальную версию с новыми аргументами
        Person.raise_pay(self, percent+bonus)

    # переопределим конструктор, вызовем оригинальный конструктор, 
    # задав значение по умолчанию
    def __init__(self, name, pay):
        Person.__init__(self, name, 'Manager', pay)


class Department:
    def __init__(self, *args):
        self.members = list(args) 

    def addMember(self, person):
        self.members.append(person)

    def DeleteMember(self, person):
        self.members.remove(person) 

    def raise_pays(self, percent):
        for person in self.members: 
            person.raise_pay(percent)

    def showAll(self):
        print('Department persons:')
        for person in self.members:
            print(person)


obj = Person("Petr", "OOO Oik", 9000)
obj1 = Person("Vasya", "OOO AAA", 3000)
obj2 = Person("Lena", "OOO Oik", 1000)
obj3 = Person("Masha", "OOO Oik", 15000)
obj4 = Manager("Sasha", 13000)
obj5 = Manager("Viktor", 10000)
obj6 = Department(obj, obj1, obj2, obj3, obj4, obj5)
obj6.showAll()
obj6.DeleteMember(obj4)
obj6.showAll()


