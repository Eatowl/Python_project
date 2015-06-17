#!/usr/bin/env python
# -*- coding: utf-8 -*-

quote = raw_input("Введите цитату ")

quote1 = quote[:].upper()
quote2 = quote[:].lower()
quote3 = quote[0].upper() + quote[1:].lower()

print "%s\n%s\n%s" % (quote1, quote2, quote3)
