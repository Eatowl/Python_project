#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
D = raw_input("Введите диаметр бассеина: ")
H = raw_input("Введите глубину бассеина: ")

V = math.pi * ((float(D) / 2) ** 2) * float(H)

print V
