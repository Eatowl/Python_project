#!/usr/bin/env python
# -*- coding: utf-8 -*-

elevator = 4, 3.2, 2	# Высота, длинна и ширина лифта 
refrigerator = 2, 2, 2	# Высота, длинна и ширина холодильника

volume_e = elevator[0] * elevator[1] * elevator[2]
volume_r = refrigerator[0] * refrigerator[1] * refrigerator[2]

if elevator[0] >= refrigerator[0] and elevator[1] >= refrigerator[1] and elevator[2] >= refrigerator[2] :
	volume_left = volume_e - volume_r
	print "Свободно %s м^2" % (volume_left)
else :
	print "Холодильник не войдёт в лифт"


