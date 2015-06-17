#!/usr/bin/env python
# -*- coding: utf-8 -*-

Rub = int(raw_input("Укажите какой суммой денег в рублях, вы располагаете: "))
Euro = int(raw_input("Укажите текущий курс евро: "))

sum_e = Rub / Euro
fifty = sum_e / 50
sum_e = sum_e - fifty * 50
twenty = sum_e / 20
sum_e = sum_e - twenty * 20
ten = sum_e / 10
sum_e = sum_e - ten * 10
five = sum_e / 5


print "У вас в наличии %s банкнот по 50 евро, %s по 20 евро, %s по 10 евро, %s по 5 евро, " % (fifty, twenty, ten, five)
