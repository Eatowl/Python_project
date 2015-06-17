#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

file = open('invoice.txt')
a = file.read()
summa = 0
res = re.findall('\d+[\s*]+\d+[\.]?[\d]?', a)
for b in res:
	c = b.split()
	c = int(c[0]) * float(c[1])
	summa = summa + c
print summa
