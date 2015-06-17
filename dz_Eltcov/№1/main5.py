#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
R = raw_input("Введите радиус окружности: ")

S = math.pi * (float(R) ** 2)
P = 2 * math.pi * float(R)

print "Площадь окружности = %s\nДлина окружности = %s" % (S, P)


