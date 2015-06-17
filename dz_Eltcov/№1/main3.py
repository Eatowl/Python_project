#!/usr/bin/env python
# -*- coding: utf-8 -*-

Rub = int(raw_input("Укажите какой суммой денег в рублях, вы располагаете: "))
Euro = int(raw_input("Укажите текущий курс евро: "))

Euro = Rub / Euro

print "У вас в наличии %s евро" % (Euro)

