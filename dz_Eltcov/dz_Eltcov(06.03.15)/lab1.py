#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

res = re.findall(r'[+]7[-]?[\s]?[\(]?\d{3}[-]?[\s]?[\)]?[\s]?\d{3}[-]?[\s]?\d{2}[-]?[\s]?\d{2}', '+7-913-432-12-32, +7 (383) 432 1232, +74213214213')

print res
