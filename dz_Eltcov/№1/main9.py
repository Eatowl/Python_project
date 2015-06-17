#!/usr/bin/env python
# -*- coding: utf-8 -*-

year = input("Введите год: ")
month = raw_input("Введите месяц: ")
number = input("Введите день: ")

data_y = {'year':'г',}
data_m = {'month': ['Января ','Февраля ','Марта ','Апреля ','Мая ','Июня ','Июля ','Августа ','Сентября ','Октября ','Ноября ','Декабря '],}
data_n = {'day':'-ое ',}

print str(number) + data_n['day'] + data_m['month'][month-1] + str(year) + data_y['year']
