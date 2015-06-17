#!/usr/bin/env python
# -*- coding: utf-8 -*-

quote = raw_input("Введите цитату ")

quote1 = quote[:].upper()
quote2 = quote[:].lower()
quote3 = quote[0].upper() + quote[1:].lower()

old = raw_input("Какое слово заменить? ")
old1 = old[:].upper()
new = "Good"

print "%s\n%s\n%s" % (quote1.replace(old1, "Good"), quote2.replace(old, "Good"), quote3.replace(old, "Good"))
